"""Search a binary replay-fixed root extending the Q21 cube delimiter.

The unknown primitive word R begins Q^3 3, where Q is the checked
length-21 replay root.  Exact source equations make the orbit from R append
one copy of R; exact proper circular equations then make it append the
second copy as well.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, Solver, sat  # type: ignore


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("--timeout-ms", type=int, default=300000)
    parser.add_argument(
        "--max-cut",
        type=int,
        help="impose replay/profile equations only through this cut",
    )
    parser.add_argument(
        "--extra-cut",
        type=int,
        action="append",
        default=[],
        help="additional cut equation to impose (repeatable)",
    )
    parser.add_argument(
        "--copy-start",
        type=int,
        action="append",
        default=[],
        help="force another copy of W=Q21^3 3 2 at this root phase",
    )
    parser.add_argument(
        "--reset-closure",
        action="store_true",
        help=(
            "at the endpoint of every circular occurrence of "
            "W=Q21^3 3 2, impose the exact replay equation"
        ),
    )
    args = parser.parse_args()
    n = args.length
    q21 = "223222322232322232223"
    prefix = q21 * 3 + "3"
    if n < len(prefix):
        raise SystemExit(f"length must be at least {len(prefix)}")

    is_three = [Bool(f"t_{i}") for i in range(n)]
    solver = Solver()
    solver.set(timeout=args.timeout_ms)
    for i, symbol in enumerate(prefix):
        solver.add(is_three[i] if symbol == "3" else Not(is_three[i]))
    reset = prefix + "2"
    for start in args.copy_start:
        if start < 0 or start + len(reset) > n:
            raise SystemExit("copy does not fit")
        for offset, symbol in enumerate(reset):
            variable = is_three[start + offset]
            solver.add(variable if symbol == "3" else Not(variable))

    def equal(i: int, j: int):
        return is_three[i % n] == is_three[j % n]

    powers = {}
    implied_extra_cuts = [
        start + len(reset) for start in args.copy_start
        if start + len(reset) < n
    ]
    active_cuts = tuple(sorted(set(
        range(n if args.max_cut is None else min(n, args.max_cut + 1))
    ) | {
        cut for cut in args.extra_cut + implied_extra_cuts
        if 0 <= cut < n
    }))
    for cut in active_cuts:
        for root in range(1, n):
            previous = []
            for exponent in range(2, 5):
                previous.extend(
                    equal(cut - exponent * root + offset,
                          cut - root + offset)
                    for offset in range(root)
                )
                powers[cut, root, exponent] = And(*previous)

    for cut in active_cuts:
        circular_square = Or(
            *(powers[cut, root, 2] for root in range(1, n))
        )
        circular_cube = Or(
            *(powers[cut, root, 3] for root in range(1, n))
        )
        circular_fourth = Or(
            *(powers[cut, root, 4] for root in range(1, n))
        )
        solver.add(circular_square)
        solver.add(is_three[cut] == circular_cube)
        solver.add(Not(circular_fourth))

        fitting_squares = [
            powers[cut, root, 2]
            for root in range(1, n)
            if 2 * root <= n + cut
        ]
        fitting_cubes = [
            powers[cut, root, 3]
            for root in range(1, n)
            if 3 * root <= n + cut
        ]
        fitting_fourths = [
            powers[cut, root, 4]
            for root in range(1, n)
            if 4 * root <= n + cut
        ]
        solver.add(Or(*fitting_squares))
        solver.add(is_three[cut] == Or(*fitting_cubes))
        solver.add(Not(Or(*fitting_fourths)))

    if args.reset_closure:
        def occurrence(start: int):
            return And(
                *(
                    is_three[(start + offset) % n]
                    if symbol == "3"
                    else Not(is_three[(start + offset) % n])
                    for offset, symbol in enumerate(reset)
                )
            )

        def local_power(cut: int, root: int, exponent: int):
            equalities = []
            for block in range(2, exponent + 1):
                equalities.extend(
                    equal(cut - block * root + offset,
                          cut - root + offset)
                    for offset in range(root)
                )
            return And(*equalities)

        # Every occurrence whose endpoint lies in the root has an actual
        # source replay cut there.  Conditionalizing avoids imposing the
        # full profile away from reset occurrences.
        for start in range(n):
            cut = (start + len(reset)) % n
            square_roots = [
                local_power(cut, root, 2)
                for root in range(1, n)
                if 2 * root <= n + cut
            ]
            cube_roots = [
                local_power(cut, root, 3)
                for root in range(1, n)
                if 3 * root <= n + cut
            ]
            fourth_roots = [
                local_power(cut, root, 4)
                for root in range(1, n)
                if 4 * root <= n + cut
            ]
            exact_reset_cut = And(
                Or(*square_roots),
                is_three[cut] == Or(*cube_roots),
                Not(Or(*fourth_roots)),
            )
            solver.add(Or(Not(occurrence(start)), exact_reset_cut))

    for period in range(1, n):
        if n % period != 0:
            continue
        solver.add(
            Or(
                *(
                    is_three[i] != is_three[i % period]
                    for i in range(period, n)
                )
            )
        )

    result = solver.check()
    print(
        f"length={n} prefix_length={len(prefix)} "
        f"max_cut={args.max_cut} result={result}"
    )
    if result == sat:
        model = solver.model()
        word = "".join(
            "3" if model.eval(is_three[i]) else "2"
            for i in range(n)
        )
        print("root=" + word)


if __name__ == "__main__":
    main()
