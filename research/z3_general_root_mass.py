"""Search the generalized maximal-root mass budget for a counterexample.

The model is a primitive binary circular word ``Q`` with exact proper
profile in ``{2,3}``.  A globally maximum cube period ``p`` has a
left-maximal occurrence ``U^3`` starting at cut zero.  For its third-copy
3-cuts, charge the least smaller cube period.  For its first-copy 2-cuts,
charge a square hole only when the aligned third-copy cut is also labelled
2.  The target is total charge greater than ``p``.

This aligned definition agrees with the raw first-copy charge under the
fixed-profile equation, while avoiding the exact length-17 double charge
caused by profile misalignment.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, If, Not, Or, Solver, Sum, is_true, sat  # type: ignore

from check_run_length_grammar import (
    primitive,
    proper_profile,
    word_power_root_lengths,
)


def build_solver(n: int, p: int, timeout_ms: int):
    if not 1 <= p < n:
        raise ValueError("require 1 <= p < n")
    solver = Solver()
    solver.set(timeout=timeout_ms)
    word = [Bool(f"w_{i}") for i in range(n)]  # True=3, False=2

    square = {}
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
            square[cut, q] = copy_2
            cube[cut, q] = And(copy_2, copy_3)
            fourth[cut, q] = And(copy_2, copy_3, copy_4)

    profile_three = {}
    for cut in range(n):
        solver.add(Or(*(square[cut, q] for q in range(1, n))))
        solver.add(*(Not(fourth[cut, q]) for q in range(1, n)))
        profile_three[cut] = Or(*(cube[cut, q] for q in range(1, n)))
        solver.add(*(Not(cube[cut, q]) for q in range(p + 1, n)))

    # U^3 starts at zero, has primitive period p, and cannot extend left.
    main_cut = (3 * p) % n
    solver.add(cube[main_cut, p])
    solver.add(word[-1] != word[(p - 1) % n])

    child_cost = []
    holes = []
    for offset in range(p):
        third_cut = (2 * p + offset) % n
        smaller_children = [cube[third_cut, q] for q in range(1, p)]
        solver.add(Or(*smaller_children) == profile_three[third_cut])
        for q in range(1, p):
            child_cost.append(
                q
                * If(
                    And(
                        cube[third_cut, q],
                        *(Not(cube[third_cut, s]) for s in range(1, q)),
                    ),
                    1,
                    0,
                )
            )

        first_cut = offset % n
        contained_squares = []
        for q in range(1, offset // 2 + 1):
            contained_squares.append(
                And(
                    *(
                        word[offset - 2 * q + j]
                        == word[offset - q + j]
                        for j in range(q)
                    )
                )
            )
        holes.append(
            And(
                Not(profile_three[first_cut]),
                Not(profile_three[third_cut]),
                Not(Or(*contained_squares)) if contained_squares else True,
            )
        )

    solver.add(
        Sum(*child_cost) + Sum(*(If(hole, 1, 0) for hole in holes)) > p
    )
    return solver, word


def direct_metrics(word: tuple[int, ...], p: int):
    n = len(word)
    profile = proper_profile(word)
    children = []
    for offset in range(p):
        cut = (2 * p + offset) % n
        if profile[cut] != 3:
            continue
        roots = tuple(q for q in word_power_root_lengths(word, cut, 3) if q < p)
        assert roots
        children.append((offset, min(roots)))

    holes = []
    for offset in range(p):
        first = offset % n
        third = (2 * p + offset) % n
        if profile[first] != 2 or profile[third] != 2:
            continue
        contained = any(
            all(
                word[offset - 2 * q + j] == word[offset - q + j]
                for j in range(q)
            )
            for q in range(1, offset // 2 + 1)
        )
        if not contained:
            holes.append(offset)
    return profile, tuple(children), tuple(holes)


def solve(n: int, p: int, timeout_ms: int) -> str:
    solver, symbols = build_solver(n, p, timeout_ms)
    result = solver.check()
    if result != sat:
        return str(result)
    model = solver.model()
    word = tuple(3 if is_true(model.eval(x)) else 2 for x in symbols)
    profile, children, holes = direct_metrics(word, p)
    periods = tuple(
        q
        for cut in range(n)
        for q in word_power_root_lengths(word, cut, 3)
    )
    mass = sum(q for _, q in children) + len(holes)

    assert primitive(word)
    assert all(value in (2, 3) for value in profile)
    assert max(periods) == p
    assert word[-1] != word[(p - 1) % n]
    assert mass > p
    return (
        f"sat Q={''.join(map(str, word))} "
        f"F={''.join(map(str, profile))} "
        f"children={children} holes={holes} mass={mass}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("p", type=int)
    parser.add_argument("--timeout-ms", type=int, default=30_000)
    args = parser.parse_args()
    print(f"n={args.n} p={args.p}: {solve(args.n, args.p, args.timeout_ms)}")


if __name__ == "__main__":
    main()
