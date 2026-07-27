"""Probe the max-four threshold-component equations.

The encoding fixes the forced entrance ``233334``.  It enforces the exact
cube/fourth/fifth-power profile at every cut, but normally does not require
square coverage at cuts labelled two.  ``--square-after-entrance`` adds
the one square equation that a genuine fixed profile needs immediately
after the forced entrance.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, Solver, is_true, sat  # type: ignore


def solve(
    n: int,
    timeout_ms: int,
    square_after_entrance: bool,
    *,
    require_cubes: bool = True,
    exact_fourths: bool = True,
    require_fourths: bool = True,
    forbid_fifths: bool = True,
    high_fourth_roots: bool = True,
    exempt_cube_cuts: frozenset[int] = frozenset(),
    require_primitive: bool = True,
    enforce_unary_fourths: bool = False,
):
    ge3 = [Bool(f"h_{i}") for i in range(n)]
    ge4 = [Bool(f"t_{i}") for i in range(n)]
    solver = Solver()
    solver.set(timeout=timeout_ms)
    solver.add(*(Or(Not(ge4[i]), ge3[i]) for i in range(n)))

    def equal(i: int, j: int):
        return And(
            ge3[i % n] == ge3[j % n],
            ge4[i % n] == ge4[j % n],
        )

    powers = {}
    for cut in range(n):
        for root in range(1, n):
            comparisons = []
            for exponent in range(2, 6):
                comparisons.extend(
                    equal(cut - block * root + j, cut - root + j)
                    for block in range(2, exponent + 1)
                    for j in range(root)
                )
                powers[cut, root, exponent] = And(*comparisons)

    for cut in range(n):
        cube = Or(*(powers[cut, root, 3] for root in range(1, n)))
        fourth = Or(*(powers[cut, root, 4] for root in range(1, n)))
        fifth = Or(*(powers[cut, root, 5] for root in range(1, n)))
        if require_cubes and cut not in exempt_cube_cuts:
            solver.add(Or(Not(ge3[cut]), cube))
        if require_fourths:
            if exact_fourths:
                solver.add(ge4[cut] == fourth)
            else:
                solver.add(Or(Not(ge4[cut]), fourth))
        if forbid_fifths:
            solver.add(Not(fifth))
        if high_fourth_roots:
            solver.add(
                Or(
                    Not(ge4[cut]),
                    Or(
                        *(
                            And(
                                powers[cut, root, 4],
                                *(
                                    ge3[(cut - root + j) % n]
                                    for j in range(root)
                                ),
                            )
                            for root in range(1, n)
                        )
                    ),
                )
            )
        if enforce_unary_fourths:
            trailing_four_threes = And(
                *(
                    And(
                        ge3[(cut - offset) % n],
                        Not(ge4[(cut - offset) % n]),
                    )
                    for offset in range(1, 5)
                )
            )
            solver.add(Or(Not(trailing_four_threes), ge4[cut]))

    if require_primitive:
        for period in range(1, n):
            if n % period == 0:
                solver.add(
                    Or(
                        *(
                            Not(equal(i, i % period))
                            for i in range(period, n)
                        )
                    )
                )

    solver.add(Not(ge3[0]))
    for i in range(1, 5):
        solver.add(ge3[i], Not(ge4[i]))
    solver.add(ge3[5], ge4[5])
    if square_after_entrance:
        solver.add(
            Or(*(powers[6, root, 2] for root in range(1, n)))
        )

    result = solver.check()
    word = None
    if result == sat:
        model = solver.model()
        word = tuple(
            4
            if is_true(model.eval(ge4[i]))
            else 3
            if is_true(model.eval(ge3[i]))
            else 2
            for i in range(n)
        )
    return result, word


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("--timeout-ms", type=int, default=120_000)
    parser.add_argument("--square-after-entrance", action="store_true")
    parser.add_argument("--no-cubes", action="store_true")
    parser.add_argument("--one-way-fourths", action="store_true")
    parser.add_argument("--no-fourths", action="store_true")
    parser.add_argument("--allow-fifths", action="store_true")
    parser.add_argument("--no-high-root", action="store_true")
    parser.add_argument(
        "--exempt-cube-cut", action="append", type=int, default=[]
    )
    parser.add_argument("--allow-imprimitive", action="store_true")
    parser.add_argument("--unary-fourths-only", action="store_true")
    args = parser.parse_args()
    result, word = solve(
        args.length,
        args.timeout_ms,
        args.square_after_entrance,
        require_cubes=not args.no_cubes,
        exact_fourths=not args.one_way_fourths,
        require_fourths=not args.no_fourths,
        forbid_fifths=not args.allow_fifths,
        high_fourth_roots=not args.no_high_root,
        exempt_cube_cuts=frozenset(
            cut % args.length for cut in args.exempt_cube_cut
        ),
        require_primitive=not args.allow_imprimitive,
        enforce_unary_fourths=args.unary_fourths_only,
    )
    print({"length": args.length, "status": str(result), "word": word})


if __name__ == "__main__":
    main()
