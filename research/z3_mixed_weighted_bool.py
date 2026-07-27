"""Boolean SMT search for a ternary mixed weighted profile.

Tokens 0 and 1 have weight two; token 2 has weight three.  This directly
targets a counterexample to injectivity of a mixed {2,3}-weight map.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, Solver, sat  # type: ignore


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("--timeout-ms", type=int, default=300000)
    parser.add_argument(
        "--seed",
        help="optional ternary word used only to set solver phases",
    )
    args = parser.parse_args()
    n = args.length
    if n < 1:
        raise SystemExit(2)

    is_one = [Bool(f"o_{i}") for i in range(n)]
    is_two = [Bool(f"t_{i}") for i in range(n)]
    solver = Solver()
    solver.set(timeout=args.timeout_ms)
    solver.add(*(Not(And(is_one[i], is_two[i])) for i in range(n)))

    # Break the interchangeable weight-2 color symmetry.
    solver.add(Not(is_one[0]), Not(is_two[0]))
    solver.add(Or(*is_one), Or(*is_two))
    solver.add(
        Or(
            *(
                And(Not(is_one[i]), Not(is_two[i]))
                for i in range(n)
            )
        )
    )

    def equal(i: int, j: int):
        i %= n
        j %= n
        return And(
            is_one[i] == is_one[j],
            is_two[i] == is_two[j],
        )

    power_cache = {}

    def power(cut: int, root: int, exponent: int):
        key = (cut, root, exponent)
        if key not in power_cache:
            power_cache[key] = And(
                *(
                    equal(
                        cut - block * root + offset,
                        cut - root + offset,
                    )
                    for block in range(2, exponent + 1)
                    for offset in range(root)
                )
            )
        return power_cache[key]

    for cut in range(n):
        squares = [power(cut, root, 2) for root in range(1, n)]
        cubes = [power(cut, root, 3) for root in range(1, n)]
        fourths = [power(cut, root, 4) for root in range(1, n)]
        solver.add(Or(*squares))
        solver.add(is_two[cut] == Or(*cubes))
        solver.add(Not(Or(*fourths)))

    for period in range(1, n):
        if n % period != 0:
            continue
        solver.add(
            Or(
                *(
                    Not(equal(i, i % period))
                    for i in range(period, n)
                )
            )
        )

    if args.seed is not None:
        if len(args.seed) != n or any(x not in "012" for x in args.seed):
            raise SystemExit("bad seed")
        # Z3 phase hints are not exposed per literal in this binding.  A soft
        # Hamming ball would change the problem, so the seed is reported only.
        print("seed=" + args.seed)

    result = solver.check()
    print(f"length={n} result={result}")
    if result == sat:
        model = solver.model()
        word = "".join(
            "2"
            if model.eval(is_two[i])
            else "1"
            if model.eval(is_one[i])
            else "0"
            for i in range(n)
        )
        print("tokens=" + word)
        print("weights=223")


if __name__ == "__main__":
    main()
