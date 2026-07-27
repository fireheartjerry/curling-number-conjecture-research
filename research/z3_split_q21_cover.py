"""Try to split the weight-2 letter in cyclic covers of the Q21 profile.

The base word is the exact binary weighted profile of length 21.  A cover
uses one common weight-3 token at the old 3-positions and independently
colors each old 2-position by either of two weight-2 tokens.  Exact proper
curling values are imposed on the resulting primitive ternary cycle.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, If, Not, Or, Solver, sat  # type: ignore


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("copies", type=int)
    parser.add_argument(
        "--split-weight",
        type=int,
        choices=(2, 3),
        default=2,
    )
    parser.add_argument("--timeout-ms", type=int, default=300000)
    args = parser.parse_args()
    if args.copies < 1:
        raise SystemExit(2)

    base = tuple(map(int, "223222322232322232223"))
    profile = base * args.copies
    n = len(profile)
    split = [Bool(f"s_{i}") for i in range(n)]
    solver = Solver()
    solver.set(timeout=args.timeout_ms)

    # At positions of the selected weight, the Boolean chooses between two
    # token colors.  Positions of the other weight use one common token.
    def equal(i: int, j: int):
        i %= n
        j %= n
        if profile[i] != profile[j]:
            return False
        if profile[i] != args.split_weight:
            return True
        return split[i] == split[j]

    def power(cut: int, root: int, exponent: int):
        return And(
            *(
                equal(cut - block * root + offset, cut - root + offset)
                for block in range(2, exponent + 1)
                for offset in range(root)
            )
        )

    for cut, wanted in enumerate(profile):
        square = Or(*(power(cut, root, 2) for root in range(1, n)))
        cube = Or(*(power(cut, root, 3) for root in range(1, n)))
        fourth = Or(*(power(cut, root, 4) for root in range(1, n)))
        solver.add(square)
        solver.add(cube if wanted == 3 else Not(cube))
        solver.add(Not(fourth))

    # Both split colors occur.
    split_positions = [
        i for i, value in enumerate(profile)
        if value == args.split_weight
    ]
    solver.add(Or(*(split[i] for i in split_positions)))
    solver.add(Or(*(Not(split[i]) for i in split_positions)))

    # Exclude every proper circular period, not only periods inherited from
    # the base cover.
    for period in range(1, n):
        if n % period != 0:
            continue
        differences = []
        for i in range(period, n):
            j = i % period
            differences.append(Not(equal(i, j)))
        solver.add(Or(*differences))

    result = solver.check()
    print(f"copies={args.copies} length={n} result={result}")
    if result == sat:
        model = solver.model()
        rendered_symbols = []
        for i, wanted in enumerate(profile):
            if wanted != args.split_weight:
                rendered_symbols.append("0")
            else:
                rendered_symbols.append(
                    "2" if model.eval(split[i]) else "1"
                )
        rendered = "".join(rendered_symbols)
        print("tokens=" + rendered)
        print("weights=" + "".join(map(str, profile)))


if __name__ == "__main__":
    main()
