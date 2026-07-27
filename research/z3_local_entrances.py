"""Find two nearby top entrances satisfying the six local profile equations."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, Solver, sat  # type: ignore


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("period", type=int)
    parser.add_argument("distance", type=int)
    args = parser.parse_args()
    n = args.period
    distance = args.distance
    if n <= 2 * distance + 12:
        raise SystemExit("choose a period longer than twice the local window")

    ge3 = [Bool(f"h_{i}") for i in range(n)]
    ge4 = [Bool(f"t_{i}") for i in range(n)]
    solver = Solver()
    solver.add(*(Or(Not(ge4[i]), ge3[i]) for i in range(n)))
    # Necessary global fixed-profile condition: the next value rises by at
    # most one.  In the {2,3,4} encoding only 2 -> 4 is forbidden.
    solver.add(
        *(
            Or(ge3[i], Not(ge4[(i + 1) % n]))
            for i in range(n)
        )
    )

    def equal(i: int, j: int):
        return And(ge3[i % n] == ge3[j % n], ge4[i % n] == ge4[j % n])

    def power(cut: int, root: int, exponent: int):
        return And(
            *(
                equal(cut - block * root + j, cut - root + j)
                for block in range(2, exponent + 1)
                for j in range(root)
            )
        )

    entrance = [2, 3, 3, 3, 3, 4]

    def fix_symbol(index: int, value: int):
        if value == 2:
            solver.add(Not(ge3[index % n]), Not(ge4[index % n]))
        elif value == 3:
            solver.add(ge3[index % n], Not(ge4[index % n]))
        else:
            solver.add(ge3[index % n], ge4[index % n])

    for i, value in enumerate(entrance):
        fix_symbol(i, value)
        fix_symbol(i - distance, value)

    for cut, value in enumerate(entrance):
        squares = Or(*(power(cut, p, 2) for p in range(1, n)))
        cubes = Or(*(power(cut, p, 3) for p in range(1, n)))
        fourths = Or(*(power(cut, p, 4) for p in range(1, n)))
        fifths = Or(*(power(cut, p, 5) for p in range(1, n)))
        solver.add(squares)
        solver.add(cubes if value >= 3 else Not(cubes))
        solver.add(fourths if value >= 4 else Not(fourths))
        solver.add(Not(fifths))

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

    result = solver.check()
    print(f"period={n} distance={distance} result={result}")
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
        lo = -distance - 20
        rendered = "".join(str(word[i % n]) for i in range(lo, 12))
        print(f"window_start={lo} window={rendered}")
        print("word=" + "".join(map(str, word)))


if __name__ == "__main__":
    main()
