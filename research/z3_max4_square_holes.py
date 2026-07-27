"""Search exact max-4 circular profiles with a bounded number of square holes.

Every cut has the exact cube/fourth/fifth status prescribed by its symbol.
Only the existence of a square may fail.  Such a failure is necessarily a
``2 -> 1`` hole.  This isolates the final constraint missing from a proper
circular fixed point.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, If, Not, Or, Solver, Sum, sat  # type: ignore[import-not-found]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("max_holes", type=int)
    parser.add_argument("--timeout-ms", type=int, default=0)
    parser.add_argument("--top-entrance", action="store_true")
    parser.add_argument("--square-after-entrance", action="store_true")
    args = parser.parse_args()
    n = args.length

    ge3 = [Bool(f"h_{i}") for i in range(n)]
    ge4 = [Bool(f"t_{i}") for i in range(n)]
    solver = Solver()
    if args.timeout_ms:
        solver.set(timeout=args.timeout_ms)
    solver.add(*(Or(Not(ge4[i]), ge3[i]) for i in range(n)))
    solver.add(Or(*ge4), Or(*(Not(x) for x in ge3)))

    def equal(i: int, j: int):
        return And(ge3[i % n] == ge3[j % n], ge4[i % n] == ge4[j % n])

    powers = {}
    for cut in range(n):
        for root in range(1, n):
            comparisons = []
            for exponent in range(2, 6):
                comparisons.extend(
                    equal(cut - exponent * root + j, cut - root + j)
                    for j in range(root)
                )
                powers[cut, root, exponent] = And(*comparisons)

    squares = []
    for cut in range(n):
        square = Or(*(powers[cut, root, 2] for root in range(1, n)))
        cube = Or(*(powers[cut, root, 3] for root in range(1, n)))
        fourth = Or(*(powers[cut, root, 4] for root in range(1, n)))
        fifth = Or(*(powers[cut, root, 5] for root in range(1, n)))
        squares.append(square)
        solver.add(ge3[cut] == cube)
        solver.add(ge4[cut] == fourth)
        solver.add(Not(fifth))

    solver.add(Sum(*(If(square, 0, 1) for square in squares)) <= args.max_holes)

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

    if args.top_entrance:
        if n < 6:
            solver.add(False)
        else:
            solver.add(Not(ge3[0]))
            for i in range(1, 5):
                solver.add(ge3[i], Not(ge4[i]))
            solver.add(ge4[5])
            if args.square_after_entrance:
                solver.add(squares[6 % n])

    result = solver.check()
    print(f"length={n} holes<={args.max_holes} result={result}")
    if result == sat:
        model = solver.model()
        word = tuple(
            4
            if model.eval(ge4[i])
            else 3
            if model.eval(ge3[i])
            else 2
            for i in range(n)
        )
        holes = tuple(i for i, square in enumerate(squares) if not model.eval(square))
        print("word=" + "".join(map(str, word)))
        print("holes=" + ",".join(map(str, holes)))


if __name__ == "__main__":
    main()
