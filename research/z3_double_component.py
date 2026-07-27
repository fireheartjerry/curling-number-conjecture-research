"""Search for a squareful double-3 component with disjoint cube roots.

For a binary circular word ``Q`` of fixed physical length ``n``, the
constraints in the default mode are:

* ``Q[-1:]+Q[:3] = 2,3,3,2``;
* every proper circular cut ends in a square;
* no proper cut ends in a fourth power;
* cuts 0 and 1 end in cubes, while cut 2 does not; and
* no root length gives cubes at both cuts 0 and 1.

Thus a satisfying model would refute the proposed intermediate lemma
that global squarefulness plus the exact local ``332`` profile forces a
same-period bridge.  ``--fixed`` strengthens the constraints to the full
fixed-profile equation ``proper_profile(Q) == Q``.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, Solver, is_true, sat  # type: ignore

from check_run_length_grammar import (
    primitive,
    proper_profile,
    word_power_root_lengths,
)


def build_solver(n: int, fixed: bool, timeout_ms: int):
    if n < 4:
        raise ValueError("n must be at least four")

    solver = Solver()
    solver.set(timeout=timeout_ms)
    word = [Bool(f"w_{i}") for i in range(n)]  # True=3, False=2

    # A normalized maximal double component.
    solver.add(Not(word[-1]), word[0], word[1], Not(word[2]))

    square = {}
    cube = {}
    fourth = {}
    for cut in range(n):
        for p in range(1, n):
            copy_2 = And(
                *(
                    word[(cut - 2 * p + j) % n]
                    == word[(cut - p + j) % n]
                    for j in range(p)
                )
            )
            copy_3 = And(
                *(
                    word[(cut - 3 * p + j) % n]
                    == word[(cut - p + j) % n]
                    for j in range(p)
                )
            )
            copy_4 = And(
                *(
                    word[(cut - 4 * p + j) % n]
                    == word[(cut - p + j) % n]
                    for j in range(p)
                )
            )
            square[cut, p] = copy_2
            cube[cut, p] = And(copy_2, copy_3)
            fourth[cut, p] = And(copy_2, copy_3, copy_4)

    for cut in range(n):
        has_square = Or(*(square[cut, p] for p in range(1, n)))
        has_cube = Or(*(cube[cut, p] for p in range(1, n)))
        solver.add(has_square)
        solver.add(*(Not(fourth[cut, p]) for p in range(1, n)))
        if fixed:
            solver.add(has_cube == word[cut])

    solver.add(Or(*(cube[0, p] for p in range(1, n))))
    solver.add(Or(*(cube[1, p] for p in range(1, n))))
    solver.add(*(Not(cube[2, p]) for p in range(1, n)))
    solver.add(
        *(Not(And(cube[0, p], cube[1, p])) for p in range(1, n))
    )
    return solver, word


def solve_length(n: int, fixed: bool, timeout_ms: int) -> str:
    solver, symbols = build_solver(n, fixed, timeout_ms)
    result = solver.check()
    if result != sat:
        return str(result)

    model = solver.model()
    q = tuple(3 if is_true(model.eval(x)) else 2 for x in symbols)
    f = proper_profile(q)
    left = word_power_root_lengths(q, 0, 3)
    right = word_power_root_lengths(q, 1, 3)

    assert primitive(q)
    assert all(value in (2, 3) for value in f)
    assert f[:3] == (3, 3, 2)
    assert not set(left).intersection(right)
    if fixed:
        assert f == q

    return (
        f"sat Q={''.join(map(str, q))} "
        f"F={''.join(map(str, f))} "
        f"roots0={left} roots1={right}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("max_n", type=int)
    parser.add_argument("--min-n", type=int, default=4)
    parser.add_argument("--fixed", action="store_true")
    parser.add_argument("--timeout-ms", type=int, default=30_000)
    args = parser.parse_args()

    for n in range(args.min_n, args.max_n + 1):
        print(
            f"n={n}: {solve_length(n, args.fixed, args.timeout_ms)}",
            flush=True,
        )


if __name__ == "__main__":
    main()
