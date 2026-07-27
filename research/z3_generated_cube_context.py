"""Search a left context that generates every symbol of a displayed cube.

The displayed root is fixed.  An unknown finite prefix is followed by three
copies of the root.  At every cut in those copies, the current curling number
must equal the symbol being appended.  Primitive cube roots are globally
bounded by ``--cube-max``; all square witnesses and all forbidden powers are
tested only when the complete power fits the available prefix.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, Solver, is_true, sat


def eq(xs, ys):
    return And(*(x == y for x, y in zip(xs, ys)))


def power(word, cut, root, exponent):
    assert exponent * root <= cut
    blocks = [
        word[cut - (block + 1) * root : cut - block * root]
        for block in range(exponent)
    ]
    return And(*(eq(blocks[0], block) for block in blocks[1:]))


def disjunction(word, cut, exponent, low=1, high=None):
    stop = cut // exponent
    if high is not None:
        stop = min(stop, high)
    low = max(1, low)
    if low > stop:
        return False
    return Or(*(power(word, cut, q, exponent) for q in range(low, stop + 1)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root")
    parser.add_argument("--left", type=int, default=63)
    parser.add_argument("--cube-max", type=int, default=21)
    parser.add_argument("--tight-left", action="store_true")
    parser.add_argument("--copies", type=int, default=3)
    parser.add_argument("--core", action="store_true")
    args = parser.parse_args()

    root = tuple(map(int, args.root))
    labels = root * args.copies
    left = [Bool(f"x_{i}") for i in range(args.left)]
    word = left + [symbol == 3 for symbol in labels]
    solver = Solver()
    if args.tight_left:
        solver.add(left[-1] != (root[-1] == 3))

    for phase, label in enumerate(labels):
        cut = args.left + phase
        bounded_cubes = disjunction(
            word, cut, 3, high=args.cube_max
        )
        long_cubes = disjunction(
            word, cut, 3, low=args.cube_max + 1
        )
        fourths = disjunction(word, cut, 4)
        if label == 2:
            condition = And(
                disjunction(word, cut, 2),
                Not(bounded_cubes),
                Not(long_cubes),
            )
        elif label == 3:
            condition = And(bounded_cubes, Not(long_cubes), Not(fourths))
        else:
            raise ValueError("binary root required")
        if args.core:
            solver.assert_and_track(condition, f"phase_{phase}_{label}")
        else:
            solver.add(condition)

    result = solver.check()
    print(
        f"root={args.root} left={args.left} copies={args.copies} "
        f"cube_max={args.cube_max} result={result}"
    )
    if result == sat:
        model = solver.model()
        context = "".join(
            "3" if is_true(model.eval(bit, model_completion=True)) else "2"
            for bit in left
        )
        print("context=" + context)
    elif args.core:
        print("core=" + repr(solver.unsat_core()))


if __name__ == "__main__":
    main()
