"""Search for an exact winding>1 midpoint cycle in a circular squareful word.

This is a falsifier.  A returned model is independently checkable by
enumerating all circular square roots at every cut.
"""

from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Int, Not, Or, Solver, sat  # type: ignore[import-not-found]


def build_base(length: int, alphabet: int, require_squareful: bool):
    letters = [Int(f"w_{i}") for i in range(length)]
    solver = Solver()
    solver.add(*(And(0 <= x, x < alphabet) for x in letters))
    solver.add(letters[0] == 0)

    squares = [[None] * length for _ in range(length)]
    for cut in range(length):
        for root in range(1, length):
            squares[cut][root] = And(
                *(
                    letters[(cut - 2 * root + j) % length]
                    == letters[(cut - root + j) % length]
                    for j in range(root)
                )
            )
        if require_squareful:
            solver.add(
                Or(*(squares[cut][root] for root in range(1, length)))
            )

    for period in range(1, length):
        if length % period == 0:
            solver.add(
                Or(
                    *(
                        letters[i] != letters[i % period]
                        for i in range(period, length)
                    )
                )
            )

    minima = [[None] * length for _ in range(length)]
    for cut in range(length):
        shorter = []
        for root in range(1, length):
            minima[cut][root] = And(
                squares[cut][root],
                *(Not(square) for square in shorter),
            )
            shorter.append(squares[cut][root])
    return solver, letters, minima


def cycle_roots(cycle: list[int], length: int) -> list[int]:
    return [
        (cycle[i] - cycle[(i + 1) % len(cycle)]) % length
        for i in range(len(cycle))
    ]


def candidate_cycle(
    rng: random.Random, length: int, maximum_cycle: int
) -> tuple[list[int], list[int]] | None:
    size = rng.randint(3, min(length, maximum_cycle))
    cycle = [0] + rng.sample(range(1, length), size - 1)
    rng.shuffle(cycle)
    zero = cycle.index(0)
    cycle = cycle[zero:] + cycle[:zero]
    roots = cycle_roots(cycle, length)
    if any(root == 0 for root in roots):
        return None
    if sum(roots) != 2 * length:
        return None
    if any(2 * roots[(i + 1) % size] <= roots[i] for i in range(size)):
        return None
    return cycle, roots


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("--alphabet", type=int, default=3)
    parser.add_argument("--trials", type=int, default=10000)
    parser.add_argument("--maximum-cycle", type=int, default=10)
    parser.add_argument("--seed", type=int, default=20260723)
    parser.add_argument("--cycle-only", action="store_true")
    args = parser.parse_args()

    solver, letters, minima = build_base(
        args.length, args.alphabet, not args.cycle_only
    )
    rng = random.Random(args.seed)
    checked = 0
    generated = 0
    seen = set()
    for _ in range(args.trials):
        candidate = candidate_cycle(rng, args.length, args.maximum_cycle)
        if candidate is None:
            continue
        cycle, roots = candidate
        key = tuple(cycle)
        if key in seen:
            continue
        seen.add(key)
        generated += 1
        solver.push()
        solver.add(
            *(minima[cut][root] for cut, root in zip(cycle, roots))
        )
        result = solver.check()
        checked += 1
        if result == sat:
            model = solver.model()
            word = tuple(model.eval(x).as_long() for x in letters)
            print(
                f"word={word} cycle={tuple(cycle)} roots={tuple(roots)} "
                f"winding={sum(roots) // args.length}"
            )
            return
        solver.pop()
    print(
        f"no_model length={args.length} alphabet={args.alphabet} "
        f"generated={generated} checked={checked}"
    )


if __name__ == "__main__":
    main()
