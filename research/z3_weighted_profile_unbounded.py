"""SMT search for weighted profiles with an unrestricted token alphabet.

Token identities are represented as a restricted-growth string, so every
set partition of the positions occurs exactly once up to token relabeling.
Each token type has a consistent weight in {2,3}, encoded by the position
booleans plus pairwise consistency.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, If, Implies, Int, Not, Or, Solver, Sum, sat  # type: ignore


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("--max-threes", type=int)
    parser.add_argument("--all-weights", action="store_true")
    parser.add_argument("--min-colors", type=int, default=1)
    args = parser.parse_args()
    n = args.length
    if n < 1:
        raise SystemExit(2)

    solver = Solver()
    token = [Int(f"u_{i}") for i in range(n)]
    is_three = [Bool(f"t_{i}") for i in range(n)]
    maximum = [Int(f"m_{i}") for i in range(n)]
    solver.add(token[0] == 0, maximum[0] == 0)
    for i in range(n):
        solver.add(0 <= token[i], token[i] <= i)
    for i in range(1, n):
        solver.add(
            maximum[i]
            == If(token[i] > maximum[i - 1], token[i], maximum[i - 1])
        )
        solver.add(token[i] <= maximum[i - 1] + 1)
    solver.add(maximum[n - 1] >= args.min_colors - 1)
    for i in range(n):
        for j in range(i):
            solver.add(
                Implies(token[i] == token[j], is_three[i] == is_three[j])
            )
    if args.max_threes is not None:
        solver.add(
            Sum(*(If(value, 1, 0) for value in is_three))
            <= args.max_threes
        )

    def power(cut: int, root: int, exponent: int):
        return And(
            *(
                token[(cut - block * root + j) % n]
                == token[(cut - root + j) % n]
                for block in range(2, exponent + 1)
                for j in range(root)
            )
        )

    for cut in range(n):
        square = Or(*(power(cut, root, 2) for root in range(1, n)))
        cube = Or(*(power(cut, root, 3) for root in range(1, n)))
        fourth = Or(*(power(cut, root, 4) for root in range(1, n)))
        solver.add(square)
        solver.add(is_three[cut] == cube)
        solver.add(Not(fourth))

    for period in range(1, n):
        if n % period == 0:
            solver.add(
                Or(
                    *(
                        token[i] != token[i % period]
                        for i in range(period, n)
                    )
                )
            )

    result = solver.check()
    print(f"length={n} result={result}")
    if result == sat and not args.all_weights:
        model = solver.model()
        word = tuple(model.eval(x).as_long() for x in token)
        weights = tuple(3 if model.eval(x) else 2 for x in is_three)
        print("tokens=" + " ".join(map(str, word)))
        print("weights=" + " ".join(map(str, weights)))
    elif result == sat:
        weight_words = []
        while result == sat:
            model = solver.model()
            weights = tuple(3 if model.eval(x) else 2 for x in is_three)
            weight_words.append(weights)
            solver.add(
                Or(
                    *(
                        value != (symbol == 3)
                        for value, symbol in zip(is_three, weights)
                    )
                )
            )
            result = solver.check()

        def least_dihedral(word):
            rotations = []
            for source in (word, tuple(reversed(word))):
                rotations.extend(
                    source[i:] + source[:i] for i in range(len(source))
                )
            return min(rotations)

        classes = sorted({least_dihedral(word) for word in weight_words})
        print(f"weight_words={len(weight_words)} dihedral_classes={len(classes)}")
        for word in classes:
            print("class=" + "".join(map(str, word)))


if __name__ == "__main__":
    main()
