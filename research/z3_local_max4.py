"""Find how many phase equations near 233334 are needed for max-4 UNSAT."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Int, Or, Solver, sat  # type: ignore[import-not-found]


def power(q, cut: int, root: int, exponent: int):
    n = len(q)
    return And(*(q[(cut - block * root + j) % n]
                 == q[(cut - root + j) % n]
                 for block in range(2, exponent + 1)
                 for j in range(root)))


def solve(n: int, radius: int):
    q = [Int(f"q_{i}") for i in range(n)]
    s = Solver()
    s.add(*(And(2 <= x, x <= 4) for x in q))
    s.add(*(q[i] == x for i, x in enumerate((2, 3, 3, 3, 3, 4))))
    cuts = sorted({i % n for i in range(-radius, 6 + radius)})
    cache = {}
    for cut in cuts:
        for exponent in range(2, 6):
            witnesses = []
            for root in range(1, n):
                key = (cut, root, exponent)
                cache[key] = power(q, cut, root, exponent)
                witnesses.append(cache[key])
            exists = Or(*witnesses)
            if exponent <= 4:
                s.add((q[cut] >= exponent) == exists)
            else:
                s.add(~exists)
    result = s.check()
    if result != sat:
        return False, cuts, None
    model = s.model()
    return True, cuts, tuple(model.eval(x).as_long() for x in q)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("--max-radius", type=int, default=30)
    args = parser.parse_args()
    for radius in range(args.max_radius + 1):
        ok, cuts, word = solve(args.length, radius)
        print(f"radius={radius} cuts={len(cuts)} sat={ok} word={word}")
        if not ok:
            break
