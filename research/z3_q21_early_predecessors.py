"""Classify early predecessor powers for marker-tight Q21 replay contexts.

For a fixed left-context length L, impose the exact curling-number profile
of U on its first copy.  Every positive square witness at a 2-phase is
allowed to use any fitting root.  Every cube at a 3-phase must have a root
at most 21, and all fitting cube roots longer than 21 are forbidden.  All
power ranges are explicitly clipped by exponent * root <= cut.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, Solver, is_true, sat


U = tuple(map(int, "223232223222322322232"))
GLOBAL_CUBE_MAX = len(U)


def eq(xs, ys):
    return And(*(x == y for x, y in zip(xs, ys)))


def power(word, cut, root, exponent):
    assert exponent * root <= cut
    blocks = [
        word[cut - (block + 1) * root : cut - block * root]
        for block in range(exponent)
    ]
    return And(*(eq(blocks[0], block) for block in blocks[1:]))


def power_or(word, cut, exponent, lo=1, hi=None):
    maximum = cut // exponent
    if hi is not None:
        maximum = min(maximum, hi)
    lo = max(1, lo)
    if lo > maximum:
        return False
    return Or(*(power(word, cut, root, exponent) for root in range(lo, maximum + 1)))


def make_solver(left_len, phases, require_squares=True):
    left = [Bool(f"x_{left_len}_{i}") for i in range(left_len)]
    word = left + [symbol == 3 for symbol in U * 3]
    solver = Solver()
    solver.add(left[-1])  # marker-tight: expected U[-1]=2, actual predecessor=3
    for phase, label in enumerate((U * 3)[:phases]):
        cut = left_len + phase
        squares = power_or(word, cut, 2)
        bounded_cubes = power_or(word, cut, 3, hi=GLOBAL_CUBE_MAX)
        long_cubes = power_or(
            word, cut, 3, lo=GLOBAL_CUBE_MAX + 1
        )
        fourths = power_or(word, cut, 4)
        if label == 2:
            if require_squares:
                solver.add(squares)
            solver.add(Not(bounded_cubes), Not(long_cubes))
        else:
            solver.add(bounded_cubes, Not(long_cubes), Not(fourths))
    return solver, left, word


def roots_possible(solver, word, cut, exponent, maximum):
    roots = []
    for root in range(1, min(maximum, cut // exponent) + 1):
        solver.push()
        solver.add(power(word, cut, root, exponent))
        if solver.check() == sat:
            roots.append(root)
        solver.pop()
    return tuple(roots)


def pair_roots(solver, left, word, first=(2, 4)):
    pairs = []
    cuts = tuple(len(left) + phase for phase in first)
    for q0 in range(1, GLOBAL_CUBE_MAX + 1):
        if 3 * q0 > cuts[0]:
            continue
        for q1 in range(1, GLOBAL_CUBE_MAX + 1):
            if 3 * q1 > cuts[1]:
                continue
            solver.push()
            solver.add(power(word, cuts[0], q0, 3))
            solver.add(power(word, cuts[1], q1, 3))
            if solver.check() == sat:
                pairs.append((q0, q1))
            solver.pop()
    return tuple(pairs)


def model_text(solver, left):
    assert solver.check() == sat
    model = solver.model()
    return "".join(
        "3" if is_true(model.eval(bit, model_completion=True)) else "2"
        for bit in left
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-left", type=int, default=1)
    parser.add_argument("--max-left", type=int, default=100)
    parser.add_argument("--phases", type=int, default=len(U))
    parser.add_argument("--no-squares", action="store_true")
    args = parser.parse_args()
    for left_len in range(args.min_left, args.max_left + 1):
        solver, left, word = make_solver(
            left_len, args.phases, require_squares=not args.no_squares
        )
        result = solver.check()
        if result != sat:
            continue
        roots2 = roots_possible(
            solver, word, left_len + 2, 3, GLOBAL_CUBE_MAX
        )
        roots4 = roots_possible(
            solver, word, left_len + 4, 3, GLOBAL_CUBE_MAX
        )
        pairs = pair_roots(solver, left, word)
        print(
            f"L={left_len} q2={roots2} q4={roots4} pairs={pairs} "
            f"model={model_text(solver, left)}"
        )


if __name__ == "__main__":
    main()
