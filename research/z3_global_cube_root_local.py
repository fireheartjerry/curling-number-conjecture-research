"""Local bounded-cube compatibility for a root preceded by a marker."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, Solver, is_true, sat


def eq(xs, ys):
    return And(*(x == y for x, y in zip(xs, ys)))


def power(word, cut, q, k):
    if k * q > cut:
        return False
    blocks = [word[cut - (b + 1) * q : cut - b * q] for b in range(k)]
    return And(*(eq(blocks[0], block) for block in blocks[1:]))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root")
    parser.add_argument("max_cube", type=int)
    args = parser.parse_args()
    root = tuple(map(int, args.root))
    left_len = 4 * args.max_cube
    left = [Bool(f"x_{i}") for i in range(left_len)]
    word = left + [bool(x == 3) for x in root]
    solver = Solver()
    solver.add(left[-1])
    for j, label in enumerate(root):
        cut = left_len + j
        cubes = [power(word, cut, q, 3) for q in range(1, args.max_cube + 1)]
        fourths = [power(word, cut, q, 4) for q in range(1, args.max_cube + 1)]
        if label == 3:
            solver.add(Or(*cubes))
            solver.add(Not(Or(*fourths)))
        else:
            solver.add(Not(Or(*cubes)))
    result = solver.check()
    print(result)
    if result == sat:
        model = solver.model()
        context = "".join(
            "3" if is_true(model.eval(x, model_completion=True)) else "2"
            for x in left
        )
        print(context)
        for j, label in enumerate(root):
            cut = left_len + j
            roots = [
                q
                for q in range(1, args.max_cube + 1)
                if is_true(model.eval(power(word, cut, q, 3)))
            ]
            print(j, label, roots)

    # Project the complete solution set onto each label-3 root length.
    if result == sat:
        for j, label in enumerate(root):
            if label != 3:
                continue
            cut = left_len + j
            feasible = []
            for q in range(1, args.max_cube + 1):
                solver.push()
                solver.add(power(word, cut, q, 3))
                if solver.check() == sat:
                    feasible.append(q)
                solver.pop()
            print("feasible", j, feasible)


if __name__ == "__main__":
    main()
