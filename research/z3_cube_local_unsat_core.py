"""Extract a phase-level UNSAT core for bounded cube-profile compatibility."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, Solver, unsat

ROOT = tuple(map(int, "22322323222322232232"))
RMAX = 21


def eq(xs, ys):
    return And(*(x == y for x, y in zip(xs, ys)))


def power(word, cut, q, k):
    blocks = [word[cut - (b + 1) * q : cut - b * q] for b in range(k)]
    return And(*(eq(blocks[0], block) for block in blocks[1:]))


def main() -> None:
    left_len = 4 * RMAX
    left = [Bool(f"x_{i}") for i in range(left_len)]
    word = left + [bool(x == 3) for x in ROOT]
    solver = Solver()
    solver.assert_and_track(left[-1], "boundary")
    for j, label in enumerate(ROOT):
        cut = left_len + j
        cubes = Or(
            *(
                power(word, cut, q, 3)
                for q in range(1, min(RMAX, cut // 3) + 1)
            )
        )
        fourths = Or(
            *(
                power(word, cut, q, 4)
                for q in range(1, min(RMAX, cut // 4) + 1)
            )
        )
        condition = And(cubes, Not(fourths)) if label == 3 else Not(cubes)
        solver.assert_and_track(condition, f"phase_{j}_{label}")
    assert solver.check() == unsat
    print(solver.unsat_core())


if __name__ == "__main__":
    main()
