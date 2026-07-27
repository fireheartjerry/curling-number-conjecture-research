"""SAT search for binary proper-profile words with a normalized ``332``.

This is a falsifier for the proposed elimination of adjacent 3-labelled
cuts.  A model with ``max_failures=0`` is a genuine primitive fixed
profile.  Positive ``max_failures`` searches for globally near-fixed
words while retaining every power/root possibility; no root cap smaller
than the proper cap ``n-1`` is used.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import (  # type: ignore[import-not-found]
    And,
    Bool,
    If,
    Not,
    Or,
    Solver,
    Sum,
    is_true,
    sat,
)


def build_solver(
    n: int, max_failures: int, timeout_ms: int, admissible: bool = False
):
    assert n >= 4
    is_three = [Bool(f"b_{i}") for i in range(n)]
    solver = Solver()
    if timeout_ms:
        solver.set(timeout=timeout_ms)

    def equal(left: int, right: int):
        return is_three[left % n] == is_three[right % n]

    def power(cut: int, root: int, exponent: int):
        return And(
            *(
                equal(cut - block * root + offset, cut - root + offset)
                for block in range(2, exponent + 1)
                for offset in range(root)
            )
        )

    squares = []
    cubes = []
    fourths = []
    for cut in range(n):
        squares.append(
            Or(*(power(cut, root, 2) for root in range(1, n)))
        )
        cubes.append(
            Or(*(power(cut, root, 3) for root in range(1, n)))
        )
        fourths.append(
            Or(*(power(cut, root, 4) for root in range(1, n)))
        )

    fixed = [
        And(
            squares[cut],
            is_three[cut] == cubes[cut],
            Not(fourths[cut]),
        )
        for cut in range(n)
    ]
    solver.add(Sum(*(If(condition, 0, 1) for condition in fixed)) <= max_failures)
    if admissible:
        solver.add(
            *(squares[cut] for cut in range(n)),
            *(Not(fourths[cut]) for cut in range(n)),
        )

    # Normalize one maximal double-3 component.  In a true fixed profile,
    # 333 is impossible, so the surrounding symbols must both be 2.
    solver.add(
        is_three[0],
        is_three[1],
        Not(is_three[2]),
        Not(is_three[n - 1]),
    )

    # Exclude every proper divisor period.
    for period in range(1, n):
        if n % period == 0:
            solver.add(
                Or(
                    *(
                        is_three[index] != is_three[index % period]
                        for index in range(period, n)
                    )
                )
            )

    return solver, is_three, fixed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("--max-failures", type=int, default=0)
    parser.add_argument("--timeout-ms", type=int, default=60_000)
    parser.add_argument(
        "--admissible",
        action="store_true",
        help="hard-require squarefulness and absence of fourth powers",
    )
    args = parser.parse_args()
    solver, is_three, fixed = build_solver(
        args.length,
        args.max_failures,
        args.timeout_ms,
        args.admissible,
    )
    result = solver.check()
    print(
        f"length={args.length} max_failures={args.max_failures} "
        f"result={result}"
    )
    if result != sat:
        return
    model = solver.model()
    word = tuple(
        3 if is_true(model.eval(symbol)) else 2 for symbol in is_three
    )
    failures = tuple(
        cut
        for cut, condition in enumerate(fixed)
        if not is_true(model.eval(condition))
    )
    print("word=" + "".join(map(str, word)))
    print("failures=" + repr(failures))


if __name__ == "__main__":
    main()
