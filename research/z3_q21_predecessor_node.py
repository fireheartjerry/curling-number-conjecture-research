"""Test a selected pair of early Q21 cube roots as a generated predecessor.

Let ``a`` be a cube-root length at U-phase 2 and ``b`` a cube-root length
at U-phase 4.  The latter occurrence is a displayed variable cube B^3.
Its final four symbols are U[:4].  We require every symbol of B^3 and the
rest of U^3 to be generated with its displayed value, under a global bound
21 on primitive cube-root lengths.

This is stronger than checking an arbitrary left context for U: symbols in
the predecessor cube are themselves required to satisfy the orbit rule.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, If, Not, Or, Solver, is_true, sat


U = tuple(map(int, "223232223222322322232"))
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


def build(a, b, left_len, require_squares, full_u):
    if b < 4:
        # B^3 still ends in the four-symbol suffix U[:4], but the suffix
        # crosses a B boundary.  Handle it uniformly below by constraining
        # the expanded displayed cube rather than B[-4:].
        pass
    left = [Bool(f"x_{i}") for i in range(left_len)]
    root = [Bool(f"b_{i}") for i in range(b)]
    tail_values = U[4:] + (U * 2 if full_u else ())
    displayed = root * 3 + [value == 3 for value in tail_values]
    word = left + displayed
    solver = Solver()

    # U starts four symbols before the end of B^3.
    u_start = 3 * b - 4
    for offset, value in enumerate(U[:4]):
        solver.add(displayed[u_start + offset] == (value == 3))
    # Marker-tightness of the outer U^3 occurrence.
    solver.add(displayed[u_start - 1])

    # Selected phase-2 predecessor cube.
    q2_cut = left_len + u_start + 2
    solver.add(power(word, q2_cut, a, 3))

    # Every displayed symbol is itself the output at its preceding cut.
    for phase, label_is_three in enumerate(displayed):
        cut = left_len + phase
        bounded_cubes = powers(word, cut, 3, high=CUBE_MAX)
        long_cubes = powers(word, cut, 3, low=CUBE_MAX + 1)
        fourths = powers(word, cut, 4)
        square = powers(word, cut, 2)
        cond2 = And(
            square if require_squares else True,
            Not(bounded_cubes),
            Not(long_cubes),
        )
        cond3 = And(bounded_cubes, Not(long_cubes), Not(fourths))
        solver.assert_and_track(
            If(label_is_three, cond3, cond2),
            f"phase_{phase}",
        )
    return solver, left, root, u_start


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    parser.add_argument("--left", type=int, default=63)
    parser.add_argument("--no-squares", action="store_true")
    parser.add_argument("--first-u-only", action="store_true")
    parser.add_argument("--timeout-ms", type=int, default=120000)
    args = parser.parse_args()
    if not (1 <= args.a <= CUBE_MAX and 1 <= args.b <= CUBE_MAX):
        raise SystemExit("roots must lie in 1..21")
    solver, left, root, u_start = build(
        args.a,
        args.b,
        args.left,
        require_squares=not args.no_squares,
        full_u=not args.first_u_only,
    )
    solver.set(timeout=args.timeout_ms)
    result = solver.check()
    print(
        f"a={args.a} b={args.b} left={args.left} "
        f"squares={not args.no_squares} full_u={not args.first_u_only} "
        f"result={result}"
    )
    if result == sat:
        model = solver.model()
        root_text = "".join(
            "3" if is_true(model.eval(bit, model_completion=True)) else "2"
            for bit in root
        )
        context = "".join(
            "3" if is_true(model.eval(bit, model_completion=True)) else "2"
            for bit in left
        )
        print(f"B={root_text} u_start={u_start}")
        print("left=" + context)
    else:
        print("core=" + repr(solver.unsat_core()))


if __name__ == "__main__":
    main()
