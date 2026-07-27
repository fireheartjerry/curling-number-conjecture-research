"""Enumerate root-length projections for the V20 local cube core."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, Solver, sat

ROOT = tuple(map(int, "22322323"))
RMAX = 21
LEFT = 4 * RMAX


def eq(xs, ys):
    return And(*(x == y for x, y in zip(xs, ys)))


def main() -> None:
    x = [Bool(f"x_{i}") for i in range(LEFT)]
    word = x + [bool(a == 3) for a in ROOT]

    def power(j: int, q: int, k: int):
        cut = LEFT + j
        blocks = [word[cut - (b + 1) * q : cut - b * q] for b in range(k)]
        return And(*(eq(blocks[0], block) for block in blocks[1:]))

    solver = Solver()
    solver.add(x[-1])
    for j, label in enumerate(ROOT):
        cubes = Or(*(power(j, q, 3) for q in range(1, RMAX + 1)))
        fourths = Or(*(power(j, q, 4) for q in range(1, RMAX + 1)))
        solver.add(Not(fourths) if label == 3 else Not(cubes))

    feasible = {}
    for j in (2, 5, 7):
        values = []
        for q in range(1, RMAX + 1):
            solver.push()
            solver.add(power(j, q, 3))
            if solver.check() == sat:
                values.append(q)
            solver.pop()
        feasible[j] = tuple(values)
    print("individual", feasible)

    pairs = []
    for q2 in feasible[2]:
        for q5 in feasible[5]:
            solver.push()
            solver.add(power(2, q2, 3), power(5, q5, 3))
            if solver.check() == sat:
                pairs.append((q2, q5))
            solver.pop()
    print("pairs25", pairs)

    for q2, q5 in pairs:
        q7s = []
        for q7 in feasible[7]:
            solver.push()
            solver.add(power(2, q2, 3), power(5, q5, 3), power(7, q7, 3))
            if solver.check() == sat:
                q7s.append(q7)
            solver.pop()
        print("continuation", (q2, q5), q7s)


if __name__ == "__main__":
    main()
