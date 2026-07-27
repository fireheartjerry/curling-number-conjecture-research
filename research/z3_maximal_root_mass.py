"""Test a candidate mass inequality for a maximal primitive cube root.

Let ``U`` be the primitive period word of a globally maximal tight cube
``U^3`` in the singleton-3 branch.  Every internal 3-cut in the third
copy has a primitive child cube root ``q`` satisfying

    2*q + gcd(|U|, q) < |U|.

At a 2-position ``r`` of the first copy, call ``r`` a square hole when
no square ending at that cut is wholly contained in ``U[0:r]``.

This solver asks for a local root word violating the experimental budget

    sum(minimum child q at each 3-position) + number of holes <= |U|.

The local constraints include the exact cube/no-cube labels, absence of
proper fourth powers, the maximal-period descent bound, and the tight
boundary symbols ``U[0]=U[-1]=2``.  UNSAT output is bounded evidence
only; a SAT model is directly recomputed before being reported.
"""

from __future__ import annotations

import argparse
import sys
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, If, Not, Or, Solver, Sum, is_true, sat  # type: ignore


def direct_power(
    word: tuple[int, ...], cut: int, root: int, exponent: int
) -> bool:
    n = len(word)
    return all(
        word[(cut - block * root + j) % n]
        == word[(cut - root + j) % n]
        for block in range(2, exponent + 1)
        for j in range(root)
    )


def direct_metrics(word: tuple[int, ...]):
    n = len(word)
    children = []
    for cut, symbol in enumerate(word):
        roots = tuple(
            q for q in range(1, n) if direct_power(word, cut, q, 3)
        )
        fourth = tuple(
            q for q in range(1, n) if direct_power(word, cut, q, 4)
        )
        assert not fourth
        assert bool(roots) == (symbol == 3)
        assert all(2 * q + gcd(n, q) < n for q in roots)
        if roots:
            children.append((cut, min(roots)))

    holes = tuple(
        cut
        for cut, symbol in enumerate(word)
        if symbol == 2
        and not any(
            all(
                word[cut - 2 * q + j] == word[cut - q + j]
                for j in range(q)
            )
            for q in range(1, cut // 2 + 1)
        )
    )
    return tuple(children), holes


def build_solver(
    n: int,
    timeout_ms: int,
    singleton_threes: bool = False,
    packing_violation: bool = False,
):
    solver = Solver()
    solver.set(timeout=timeout_ms)
    word = [Bool(f"u_{i}") for i in range(n)]  # True=3, False=2
    solver.add(Not(word[0]), Not(word[-1]), Or(*word))
    if singleton_threes:
        solver.add(
            *(
                Not(And(word[i], word[(i + 1) % n]))
                for i in range(n)
            )
        )

    cube = {}
    fourth = {}
    for cut in range(n):
        for q in range(1, n):
            copy_2 = And(
                *(
                    word[(cut - 2 * q + j) % n]
                    == word[(cut - q + j) % n]
                    for j in range(q)
                )
            )
            copy_3 = And(
                *(
                    word[(cut - 3 * q + j) % n]
                    == word[(cut - q + j) % n]
                    for j in range(q)
                )
            )
            copy_4 = And(
                *(
                    word[(cut - 4 * q + j) % n]
                    == word[(cut - q + j) % n]
                    for j in range(q)
                )
            )
            cube[cut, q] = And(copy_2, copy_3)
            fourth[cut, q] = And(copy_2, copy_3, copy_4)

    child_costs = []
    minimum_child = {}
    holes = []
    for cut in range(n):
        roots = [cube[cut, q] for q in range(1, n)]
        solver.add(Or(*roots) == word[cut])
        solver.add(*(Not(fourth[cut, q]) for q in range(1, n)))
        solver.add(
            *(
                Not(cube[cut, q])
                for q in range(1, n)
                if 2 * q + gcd(n, q) >= n
            )
        )

        for q in range(1, n):
            minimum_child[cut, q] = And(
                cube[cut, q],
                *(Not(cube[cut, s]) for s in range(1, q)),
            )
            child_costs.append(
                q * If(minimum_child[cut, q], 1, 0)
            )

        contained_squares = []
        for q in range(1, cut // 2 + 1):
            contained_squares.append(
                And(
                    *(
                        word[cut - 2 * q + j]
                        == word[cut - q + j]
                        for j in range(q)
                    )
                )
            )
        holes.append(
            And(
                Not(word[cut]),
                Not(Or(*contained_squares)) if contained_squares else True,
            )
        )

    if packing_violation:
        collisions = []
        for cut in range(n):
            for q in range(1, n):
                # The forward q-slot arc either reaches the next 3 too
                # early or contains a first-copy square hole.
                collisions.append(
                    And(
                        minimum_child[cut, q],
                        Or(
                            *(
                                Or(
                                    word[(cut + step) % n],
                                    holes[(cut + step) % n],
                                )
                                for step in range(1, q)
                            ),
                            holes[cut],
                        ),
                    )
                )
        solver.add(Or(*collisions))
    else:
        solver.add(
            Sum(*child_costs)
            + Sum(*(If(hole, 1, 0) for hole in holes))
            > n
        )
    return solver, word


def solve_length(
    n: int,
    timeout_ms: int,
    singleton_threes: bool,
    packing_violation: bool,
) -> str:
    solver, symbols = build_solver(
        n, timeout_ms, singleton_threes, packing_violation
    )
    result = solver.check()
    if result != sat:
        return str(result)

    model = solver.model()
    word = tuple(3 if is_true(model.eval(x)) else 2 for x in symbols)
    children, holes = direct_metrics(word)
    mass = sum(q for _, q in children) + len(holes)
    assert word[0] == word[-1] == 2
    if not packing_violation:
        assert mass > n
    return (
        f"sat U={''.join(map(str, word))} "
        f"children={children} holes={holes} mass={mass}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("max_n", type=int)
    parser.add_argument("--min-n", type=int, default=3)
    parser.add_argument("--timeout-ms", type=int, default=30_000)
    parser.add_argument("--singleton-threes", action="store_true")
    parser.add_argument("--packing-violation", action="store_true")
    args = parser.parse_args()

    for n in range(args.min_n, args.max_n + 1):
        print(
            f"n={n}: "
            f"{solve_length(n, args.timeout_ms, args.singleton_threes, args.packing_violation)}",
            flush=True,
        )


if __name__ == "__main__":
    main()
