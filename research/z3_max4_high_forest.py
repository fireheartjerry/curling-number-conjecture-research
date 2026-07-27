"""Search max-4 high-component forest countermodels.

Unlike ``z3_cyclic_fixed_bool.py``, cuts labelled 2 are deliberately left
unconstrained.  Cuts labelled 3 or 4 have their exact proper circular
curling value, and every 4-cut must have a 4-root over {3,4}.  Thus every
maximum-label source edge and every phase in its high root is itself
profile-correct.  A model shows that the maximum-label forest alone does
not force coverage of the 2-cuts.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, Solver, sat  # type: ignore[import-not-found]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("--timeout-ms", type=int, default=0)
    parser.add_argument("--top-entrance", action="store_true")
    parser.add_argument("--marker-successors", action="store_true")
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

    for cut in range(n):
        square = Or(*(powers[cut, root, 2] for root in range(1, n)))
        cube = Or(*(powers[cut, root, 3] for root in range(1, n)))
        fourth = Or(*(powers[cut, root, 4] for root in range(1, n)))
        fifth = Or(*(powers[cut, root, 5] for root in range(1, n)))
        solver.add(Or(Not(ge3[cut]), cube))
        if args.marker_successors:
            solver.add(Or(Not(ge4[(cut - 1) % n]), square))
        solver.add(ge4[cut] == fourth)
        solver.add(Not(fifth))

        high_fourth_roots = []
        for root in range(1, n):
            high_root = And(
                powers[cut, root, 4],
                *(ge3[(cut - root + j) % n] for j in range(root)),
            )
            high_fourth_roots.append(high_root)
        solver.add(Or(Not(ge4[cut]), Or(*high_fourth_roots)))

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

    result = solver.check()
    print(f"length={n} result={result}")
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
        print("word=" + "".join(map(str, word)))


if __name__ == "__main__":
    main()
