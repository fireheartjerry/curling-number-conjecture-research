"""Search primitive circular fixed points of the proper curling rule.

This is a research falsifier, not a proof.  Symbols range from 2 through K.
At every circular cut, the symbol at the cut must equal the largest integer
power ending immediately before it with root length strictly below n.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Int, Or, Solver, sat  # type: ignore[import-not-found]


def power(q, cut: int, root: int, exponent: int):
    """Circular suffix at ``cut`` consists of ``exponent`` root copies."""
    n = len(q)
    return And(
        *(
            q[(cut - block * root + j) % n]
            == q[(cut - root + j) % n]
            for block in range(2, exponent + 1)
            for j in range(root)
        )
    )


def build_solver(
    n: int,
    max_symbol: int,
    replay: bool = False,
    source_only: bool = False,
    require_max: bool = False,
    top_entrance: bool = False,
    first_symbol: int = 2,
):
    solver = Solver()
    q = [Int(f"q_{i}") for i in range(n)]
    for x in q:
        solver.add(2 <= x, x <= max_symbol)
    if require_max:
        solver.add(Or(*(x == max_symbol for x in q)))
    if top_entrance:
        entrance = [max_symbol - 2] + [max_symbol - 1] * max_symbol + [
            max_symbol
        ]
        if len(entrance) > n:
            solver.add(False)
        else:
            solver.add(*(q[i] == value for i, value in enumerate(entrance)))

    # Select a distinguished phase.  Existing callers normalize at a
    # minimum-2 phase; specialized seam searches may instead normalize at
    # a forced higher phase.
    solver.add(q[0] == first_symbol)

    # Exclude every proper divisor period.
    for p in range(1, n):
        if n % p == 0:
            solver.add(Or(*(q[i] != q[i % p] for i in range(p, n))))

    powers = {
        (cut, root, exponent): power(q, cut, root, exponent)
        for cut in range(n)
        for root in range(1, n)
        for exponent in range(2, max_symbol + 2)
    }

    for cut in range(n):
        for exponent in range(2, max_symbol + 1):
            exists = Or(*(powers[cut, root, exponent] for root in range(1, n)))
            if not source_only:
                solver.add((q[cut] >= exponent) == exists)
            if replay or source_only:
                fitting_roots = [
                    root
                    for root in range(1, n)
                    if exponent * root <= n + cut
                ]
                fits_linear_source = Or(
                    *(powers[cut, root, exponent] for root in fitting_roots)
                )
                solver.add((q[cut] >= exponent) == fits_linear_source)
        if not source_only:
            # No proper root may witness a value beyond the declared alphabet.
            solver.add(
                ~Or(
                    *(
                        powers[cut, root, max_symbol + 1]
                        for root in range(1, n)
                    )
                )
            )
        else:
            fitting_roots = [
                root
                for root in range(1, n)
                if (max_symbol + 1) * root <= n + cut
            ]
            solver.add(
                ~Or(
                    *(
                        powers[cut, root, max_symbol + 1]
                        for root in fitting_roots
                    )
                )
            )

    if source_only:
        # The normalized square branch requires cn(Q^2)=2.  The outer root
        # Q witnesses two; exclude every proper cube at the boundary.
        solver.add(q[0] == 2)
        solver.add(
            ~Or(*(powers[0, root, 3] for root in range(1, n)))
        )
    return solver, q


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("max_symbol", type=int, nargs="?", default=3)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--replay", action="store_true")
    parser.add_argument("--source-only", action="store_true")
    parser.add_argument(
        "--require-max",
        action="store_true",
        help="require at least one occurrence of MAX_SYMBOL",
    )
    parser.add_argument(
        "--top-entrance",
        action="store_true",
        help="fix (K-2)(K-1)^K K at the beginning",
    )
    args = parser.parse_args()
    solver, q = build_solver(
        args.length,
        args.max_symbol,
        args.replay,
        args.source_only,
        args.require_max,
        args.top_entrance,
    )
    count = 0
    while solver.check() == sat:
        model = solver.model()
        word = tuple(model.eval(x).as_long() for x in q)
        print("word=" + " ".join(map(str, word)))
        count += 1
        if not args.all:
            break
        solver.add(Or(*(x != value for x, value in zip(q, word))))
    print(
        f"length={args.length} max_symbol={args.max_symbol} "
        f"models_reported={count}"
    )


if __name__ == "__main__":
    main()
