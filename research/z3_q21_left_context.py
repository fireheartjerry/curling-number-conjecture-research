"""Search left contexts that realize Q21's profile on the first copy of U^3."""
from __future__ import annotations

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, If, Not, Or, Solver, sat

def eq(xs, ys):
    return And(*(x == y for x, y in zip(xs, ys)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default="223232223222322322232")
    parser.add_argument("--max-left", type=int, default=None)
    parser.add_argument("--allow-left-two", action="store_true")
    parser.add_argument("--phases", type=int, default=None)
    args = parser.parse_args()
    U = tuple(map(int, args.root))
    n = len(U)
    phases = n if args.phases is None else min(args.phases, n)
    max_left = args.max_left or 6 * n
    for left_len in range(1, max_left + 1):
        left = [Bool(f"x_{left_len}_{i}") for i in range(left_len)]
        # False encodes 2, True encodes 3.
        word = left + [bool(x == 3) for x in U * 3]
        solver = Solver()
        if not args.allow_left_two:
            solver.add(left[-1])  # tight binary cube root is preceded by 3
        for j, k in enumerate(U[:phases]):
            cut = left_len + j
            witnesses = []
            for q in range(1, cut // k + 1):
                blocks = [word[cut - (b + 1) * q : cut - b * q] for b in range(k)]
                witnesses.append(And(*(eq(blocks[0], block) for block in blocks[1:])))
            solver.add(Or(*witnesses))
            forbidden = []
            for q in range(1, cut // (k + 1) + 1):
                blocks = [word[cut - (b + 1) * q : cut - b * q] for b in range(k + 1)]
                forbidden.append(And(*(eq(blocks[0], block) for block in blocks[1:])))
            if forbidden:
                solver.add(Not(Or(*forbidden)))

        # Rule out the literal preceding U copy whenever it fits.
        if left_len >= n:
            solver.add(Or(*(left[left_len - n + i] != bool(U[i] == 3) for i in range(n))))
        result = solver.check()
        if result == sat:
            model = solver.model()
            context = tuple(3 if model.eval(x) else 2 for x in left)
            print(left_len, "".join(map(str, context)))
            return
        print(left_len, result)


if __name__ == "__main__":
    main()
