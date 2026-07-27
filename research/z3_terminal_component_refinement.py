"""Incremental exact-profile refinement of terminal-marker cycle macros.

The base formula contains one high root-r cube, its two low marker
endpoints, and a root-q loss square returning from the high marker to the
first low marker.  Exact profile equations are then added in forward cut
order.  The expected SAT/UNSAT boundary is asserted for four calibration
geometries.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, Solver, sat, unsat  # type: ignore


CASES = (
    # terminal root, incoming cube root, loss-square root,
    # additional SAT cuts, first UNSAT cut
    ("223", 14, 13, (), 1),
    ("2", 7, 6, (1, 2, 3), 7),
    ("223", 22, 21, (1, 2), 3),
    ("2223", 29, 15, tuple(range(1, 11)), 11),
)


def build_case(root_text: str, incoming: int, outgoing: int):
    root = tuple(map(int, root_text))
    marker = root * 3 + (3, 2)
    n = outgoing + 2 * incoming
    letters = [Bool(f"x_{root_text}_{incoming}_{outgoing}_{i}") for i in range(n)]
    solver = Solver()
    powers = {}

    def power(cut: int, exponent: int, period: int):
        key = (cut % n, exponent, period)
        if key not in powers:
            powers[key] = And(
                *(
                    letters[(cut - block * period + offset) % n]
                    == letters[(cut - period + offset) % n]
                    for block in range(2, exponent + 1)
                    for offset in range(period)
                )
            )
        return powers[key]

    def some_power(cut: int, exponent: int):
        return Or(*(power(cut, exponent, period) for period in range(1, n)))

    def exact_profile(cut: int):
        cut %= n
        return And(
            some_power(cut, 2),
            letters[cut] == some_power(cut, 3),
            Not(some_power(cut, 4)),
        )

    # Primitivity of the circular word.
    for period in range(1, n):
        if n % period == 0:
            solver.add(
                Or(
                    *(
                        letters[index] != letters[index % period]
                        for index in range(period, n)
                    )
                )
            )

    # One terminal marker, copied to both low cube endpoints by the base
    # power equations.
    for offset, value in enumerate(marker):
        variable = letters[(n - len(marker) + offset) % n]
        solver.add(variable if value == 3 else Not(variable))

    first_low = outgoing
    second_low = outgoing + incoming
    solver.add(
        power(0, 3, incoming),
        power(first_low, 2, outgoing),
        power(second_low, 2, incoming),
        letters[0],
        Not(letters[first_low]),
        Not(letters[second_low]),
    )

    ancestry_cuts = set()
    for endpoint in (0, first_low, second_low):
        solver.add(
            letters[(endpoint - 2) % n],
            Not(letters[(endpoint - 1) % n]),
        )
        ancestry_cuts.update(
            (endpoint % n, (endpoint - 2) % n, (endpoint - 1) % n)
        )
    for cut in ancestry_cuts:
        solver.add(exact_profile(cut))
    return solver, exact_profile, ancestry_cuts, letters


def model_word(solver: Solver, letters) -> str:
    model = solver.model()
    return "".join("3" if model.eval(letter) else "2" for letter in letters)


def main() -> None:
    for root, incoming, outgoing, sat_cuts, unsat_cut in CASES:
        solver, exact_profile, ancestry_cuts, letters = build_case(
            root, incoming, outgoing
        )
        assert solver.check() == sat
        records = [("base", "sat", model_word(solver, letters))]
        for cut in sat_cuts:
            assert cut not in ancestry_cuts
            solver.add(exact_profile(cut))
            assert solver.check() == sat
            records.append((cut, "sat", model_word(solver, letters)))
        assert unsat_cut not in ancestry_cuts
        solver.add(exact_profile(unsat_cut))
        assert solver.check() == unsat
        records.append((unsat_cut, "unsat", None))
        print(
            {
                "terminal_root": root,
                "incoming": incoming,
                "outgoing": outgoing,
                "length": outgoing + 2 * incoming,
                "records": tuple(records),
            }
        )


if __name__ == "__main__":
    main()
