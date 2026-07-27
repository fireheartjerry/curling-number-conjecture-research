"""Require a selected predecessor cube and the remainder of a fixed cube.

For a fixed current root P and a 3-labelled phase t, a variable root Q of
length q satisfies Q^3 ending at cut t of P^3.  The displayed word starts
at Q^3, continues with the remaining symbols of P^3, and every displayed
symbol must be generated exactly under the global cube-root bound.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, If, Not, Or, Solver, is_true, sat


CUBE_MAX = 21


def eq(xs, ys):
    return And(*(x == y for x, y in zip(xs, ys)))


def power(word, cut, root, exponent):
    assert exponent * root <= cut
    blocks = [
        word[cut - (block + 1) * root : cut - block * root]
        for block in range(exponent)
    ]
    return And(*(eq(blocks[0], block) for block in blocks[1:]))


def powers(word, cut, exponent, low=1, high=None):
    stop = cut // exponent
    if high is not None:
        stop = min(stop, high)
    low = max(1, low)
    if low > stop:
        return False
    return Or(*(power(word, cut, q, exponent) for q in range(low, stop + 1)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("current")
    parser.add_argument("phase", type=int)
    parser.add_argument("predecessor", type=int)
    parser.add_argument("--left", type=int, default=63)
    parser.add_argument("--no-squares", action="store_true")
    parser.add_argument(
        "--cube-sign-only",
        action="store_true",
        help="impose only: label 3 iff some root<=21 cube exists",
    )
    parser.add_argument("--timeout-ms", type=int, default=120000)
    args = parser.parse_args()

    current = tuple(map(int, args.current))
    p = len(current)
    t = args.phase
    q = args.predecessor
    if not (0 <= t < p and current[t] == 3):
        raise SystemExit("phase must be a 3-position of current")
    if not (1 <= q <= CUBE_MAX):
        raise SystemExit("predecessor must lie in 1..21")

    left = [Bool(f"x_{i}") for i in range(args.left)]
    predecessor = [Bool(f"q_{i}") for i in range(q)]
    current_bits = [value == 3 for value in current * 3]
    displayed = predecessor * 3 + current_bits[t:]
    # P^3 begins t symbols before the end of Q^3.
    current_start = 3 * q - t
    solver = Solver()
    solver.set(timeout=args.timeout_ms)
    for offset in range(t):
        solver.add(
            displayed[current_start + offset] == (current[offset] == 3)
        )

    word = left + displayed
    for phase, label_is_three in enumerate(displayed):
        cut = args.left + phase
        bounded_cubes = powers(word, cut, 3, high=CUBE_MAX)
        long_cubes = powers(word, cut, 3, low=CUBE_MAX + 1)
        fourths = powers(word, cut, 4)
        squares = powers(word, cut, 2)
        if args.cube_sign_only:
            cond2 = Not(bounded_cubes)
            cond3 = bounded_cubes
        else:
            cond2 = And(
                squares if not args.no_squares else True,
                Not(bounded_cubes),
                Not(long_cubes),
            )
            cond3 = And(bounded_cubes, Not(long_cubes), Not(fourths))
        solver.assert_and_track(
            If(label_is_three, cond3, cond2),
            f"phase_{phase}",
        )

    result = solver.check()
    print(
        f"P={args.current} t={t} q={q} left={args.left} "
        f"squares={not args.no_squares} cube_sign_only={args.cube_sign_only} "
        f"result={result}"
    )
    if result == sat:
        model = solver.model()
        q_text = "".join(
            "3" if is_true(model.eval(bit, model_completion=True)) else "2"
            for bit in predecessor
        )
        left_text = "".join(
            "3" if is_true(model.eval(bit, model_completion=True)) else "2"
            for bit in left
        )
        print("Q=" + q_text)
        print("left=" + left_text)
        solver.push()
        solver.add(
            Or(
                *(
                    bit != is_true(model.eval(bit, model_completion=True))
                    for bit in predecessor
                )
            )
        )
        print("different_Q=" + str(solver.check()))
        solver.pop()
    else:
        print("core=" + repr(solver.unsat_core()))


if __name__ == "__main__":
    main()
