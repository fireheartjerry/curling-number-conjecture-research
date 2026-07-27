"""Boolean SAT encoding for max-four proper circular curling fixed points."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, Solver, sat  # type: ignore[import-not-found]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("--top-entrance", action="store_true")
    parser.add_argument("--timeout-ms", type=int, default=0)
    args = parser.parse_args()
    n = args.length
    if n < 1:
        raise SystemExit(2)

    # ge3[i] and ge4[i] encode symbols 2, 3, 4 monotonically.
    ge3 = [Bool(f"h_{i}") for i in range(n)]
    ge4 = [Bool(f"t_{i}") for i in range(n)]
    solver = Solver()
    if args.timeout_ms:
        solver.set(timeout=args.timeout_ms)
    solver.add(*(Or(Not(ge4[i]), ge3[i]) for i in range(n)))

    def equal(i: int, j: int):
        return And(ge3[i % n] == ge3[j % n], ge4[i % n] == ge4[j % n])

    powers = {}
    for cut in range(n):
        for root in range(1, n):
            previous = []
            for exponent in range(2, 6):
                previous.extend(
                    equal(cut - exponent * root + j, cut - root + j)
                    for j in range(root)
                )
                powers[cut, root, exponent] = And(*previous)

    for cut in range(n):
        square = Or(*(powers[cut, root, 2] for root in range(1, n)))
        cube = Or(*(powers[cut, root, 3] for root in range(1, n)))
        fourth = Or(*(powers[cut, root, 4] for root in range(1, n)))
        fifth = Or(*(powers[cut, root, 5] for root in range(1, n)))
        solver.add(square)
        solver.add(ge3[cut] == cube)
        solver.add(ge4[cut] == fourth)
        solver.add(Not(fifth))

    # Primitive word.
    for period in range(1, n):
        if n % period == 0:
            solver.add(
                Or(
                    *(
                        Not(equal(i, i % period))
                        for i in range(period, n)
                    )
                )
            )

    # Require the maximum and remove rotation symmetry.
    solver.add(Or(*ge4))
    if args.top_entrance:
        if n < 6:
            solver.add(False)
        else:
            # 2 3 3 3 3 4
            solver.add(Not(ge3[0]), Not(ge4[0]))
            for i in range(1, 5):
                solver.add(ge3[i], Not(ge4[i]))
            solver.add(ge3[5], ge4[5])

    result = solver.check()
    print(f"length={n} result={result}")
    if result == sat:
        model = solver.model()
        word = []
        for i in range(n):
            word.append(
                4
                if model.eval(ge4[i])
                else 3
                if model.eval(ge3[i])
                else 2
            )
        print("word=" + "".join(map(str, word)))


if __name__ == "__main__":
    main()
