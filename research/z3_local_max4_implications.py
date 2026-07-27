"""Probe word-equation consequences of the local 233334 profile motif.

Solver output is used only to identify candidate lemmas and falsifiers.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Int, Not, Or, Solver, sat  # type: ignore[import-not-found]

from z3_local_max4 import power


def local_solver(n: int, radius: int):
    q = [Int(f"q_{i}") for i in range(n)]
    solver = Solver()
    solver.add(*(And(2 <= x, x <= 4) for x in q))
    solver.add(*(q[i] == x for i, x in enumerate((2, 3, 3, 3, 3, 4))))
    cuts = sorted({i % n for i in range(-radius, 6 + radius)})
    powers = {}
    for cut in cuts:
        for exponent in range(2, 6):
            witnesses = []
            for root in range(1, n):
                formula = power(q, cut, root, exponent)
                powers[cut, root, exponent] = formula
                witnesses.append(formula)
            exists = Or(*witnesses)
            if exponent <= 4:
                solver.add((q[cut] >= exponent) == exists)
            else:
                solver.add(Not(exists))
    return solver, q, powers


def common_root(
    powers, cuts: tuple[int, ...], exponent: int, n: int
):
    return Or(
        *(
            And(*(powers[cut, root, exponent] for cut in cuts))
            for root in range(1, n)
        )
    )


def check_implication(
    solver: Solver, conclusion, name: str
) -> None:
    solver.push()
    solver.add(Not(conclusion))
    result = solver.check()
    if result == sat:
        print(f"{name}=not_forced")
    else:
        print(f"{name}=forced")
    solver.pop()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("--radius", type=int, default=2)
    args = parser.parse_args()
    n = args.length
    solver, q, powers = local_solver(n, args.radius)
    if solver.check() != sat:
        print("base=unsat")
        return
    print("base=sat")
    check_implication(
        solver,
        common_root(powers, (2, 3), 3, n),
        "common_cube_2_3",
    )
    check_implication(
        solver,
        common_root(powers, (2, 3, 4), 3, n),
        "common_cube_2_3_4",
    )

    # The cut-4 cube has the trivial root one.  Test whether the local
    # equations force an additional common nontrivial root.
    common_nontrivial = Or(
        *(
            And(
                powers[2, root, 3],
                powers[3, root, 3],
                powers[4, root, 3],
            )
            for root in range(2, n)
        )
    )
    check_implication(
        solver, common_nontrivial, "common_nontrivial_cube_2_3_4"
    )

    # Test whether one common root carries the profile equations across
    # the fourth-power delimiter to cuts 6 and 7 at their required
    # exponents.
    across = Or(
        *(
            And(
                powers[2, root, 3],
                powers[3, root, 3],
                powers[4, root, 3],
                Or(
                    And(q[6] == 2, powers[6, root, 2]),
                    And(q[6] == 3, powers[6, root, 3]),
                    And(q[6] == 4, powers[6, root, 4]),
                ),
                Or(
                    And(q[7] == 2, powers[7, root, 2]),
                    And(q[7] == 3, powers[7, root, 3]),
                    And(q[7] == 4, powers[7, root, 4]),
                ),
            )
            for root in range(2, n)
        )
    )
    check_implication(solver, across, "common_root_across_2_through_7")


if __name__ == "__main__":
    main()
