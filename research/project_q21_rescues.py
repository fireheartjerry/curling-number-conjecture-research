"""Project exact first-copy Q21 completions onto early cube-root lengths."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, Solver, sat

U = tuple(map(int, "223232223222322322232"))
RMAX = 21


def eq(xs, ys):
    return And(*(x == y for x, y in zip(xs, ys)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("left", type=int, nargs="?", default=84)
    args = parser.parse_args()
    left = [Bool(f"x_{i}") for i in range(args.left)]
    word = left + [bool(x == 3) for x in U * 3]

    def power(cut, q, k):
        blocks = [word[cut - (b + 1) * q : cut - b * q] for b in range(k)]
        return And(*(eq(blocks[0], block) for block in blocks[1:]))

    solver = Solver()
    solver.add(left[-1])
    for j, k in enumerate(U):
        cut = args.left + j
        solver.add(Or(*(power(cut, q, k) for q in range(1, cut // k + 1))))
        solver.add(Not(Or(*(power(cut, q, k + 1) for q in range(1, cut // (k + 1) + 1)))))
        # In the target application no cube root can exceed the global maximum 21.
        if k == 2:
            solver.add(Not(Or(*(power(cut, q, 3) for q in range(RMAX + 1, cut // 3 + 1)))))
    print("base", solver.check())
    for j in (2, 4):
        cut = args.left + j
        feasible = []
        for q in range(1, RMAX + 1):
            solver.push()
            solver.add(power(cut, q, 3))
            if solver.check() == sat:
                feasible.append(q)
            solver.pop()
        print(j, feasible)


if __name__ == "__main__":
    main()
