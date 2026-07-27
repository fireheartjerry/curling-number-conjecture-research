"""Explore the residual circular cube-profile equation Q = A V A.

This is a bounded diagnostic only.  A Boolean letter is ``True`` for 3
and ``False`` for 2.  Every SAT model is audited by the repository's two
independent curling-number implementations.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from z3 import And, Bool, BoolVal, Not, Or, Solver, is_true, sat  # type: ignore

from curling import curling_number, curling_number_reference


def circular_power(word: tuple[int, ...], cut: int, root: int, exponent: int) -> bool:
    n = len(word)
    return all(
        word[(cut - block * root + offset) % n]
        == word[(cut - root + offset) % n]
        for block in range(2, exponent + 1)
        for offset in range(root)
    )


def build(
    a: int,
    v: int,
    timeout_ms: int,
    tracked: bool = False,
    require_q1_low: bool = True,
):
    assert 1 <= v < a
    n = 2 * a + v
    solver = Solver()
    solver.set(timeout=timeout_ms)
    q = [Bool(f"q_{i}") for i in range(n)]

    def add(constraint, name: str):
        if tracked:
            solver.assert_and_track(constraint, Bool(name))
        else:
            solver.add(constraint)

    # Q = A V A, with V the length-v suffix of A.
    for i in range(a):
        add(q[a + v + i] == q[i], f"A2_{i}")
    for i in range(v):
        add(q[a + i] == q[a - v + i], f"Vmid_{i}")

    add(Not(q[0]), "q0")
    if require_q1_low:
        add(Not(q[1]), "q1")

    cubes = {}
    for cut in range(n):
        roots = []
        for root in range(1, n):
            cube = And(
                *(
                    q[(cut - block * root + offset) % n]
                    == q[(cut - root + offset) % n]
                    for block in range(2, 4)
                    for offset in range(root)
                )
            )
            cubes[cut, root] = cube
            roots.append(cube)
        add(q[cut] == Or(*roots), f"profile_{cut}")

    # cn(Q)=1: no square suffix of Q.
    for root in range(1, n // 2 + 1):
        square = And(
            *(q[n - 2 * root + i] == q[n - root + i] for i in range(root))
        )
        add(Not(square), f"nosq_{root}")
    return solver, q, cubes


def audit(
    word: tuple[int, ...],
    a: int,
    v: int,
    require_q1_low: bool = True,
) -> None:
    n = len(word)
    assert word[:a] == word[a + v :]
    assert word[a : a + v] == word[a - v : a]
    assert word[0] == 2
    if require_q1_low:
        assert word[1] == 2
    assert curling_number(word) == 1
    assert curling_number_reference(word) == 1
    for cut in range(n):
        has_cube = any(circular_power(word, cut, root, 3) for root in range(1, n))
        assert has_cube == (word[cut] == 3)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("max_a", type=int)
    parser.add_argument("--min-a", type=int, default=2)
    parser.add_argument("--timeout-ms", type=int, default=30_000)
    parser.add_argument("--cores", action="store_true")
    parser.add_argument("--allow-q1-three", action="store_true")
    args = parser.parse_args()
    for a in range(args.min_a, args.max_a + 1):
        for v in range(1, a):
            solver, q, _ = build(
                a,
                v,
                args.timeout_ms,
                args.cores,
                not args.allow_q1_three,
            )
            result = solver.check()
            line = f"a={a} v={v} n={2*a+v} result={result}"
            if result == sat:
                model = solver.model()
                word = tuple(3 if is_true(model.eval(x)) else 2 for x in q)
                audit(word, a, v, not args.allow_q1_three)
                line += " Q=" + "".join(map(str, word))
            elif args.cores and str(result) == "unsat":
                line += " core=" + ",".join(str(x) for x in solver.unsat_core())
            print(line, flush=True)


if __name__ == "__main__":
    main()
