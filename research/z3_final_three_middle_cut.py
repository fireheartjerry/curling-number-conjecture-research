"""Search the proposed middle-cut obstruction in the final-3 normal form.

For fixed lengths, encode

    A is a nonempty proper suffix of X,
    first(X) = 3, first(A) = 2,
    cn(X) = cn(A X) = 1,
    Q = X A X A X,

and ask whether a proper circular cube can end at cut ``|X|+|A|`` of
``Q``.  SAT models are independently checked with both curling-number
implementations.  UNSAT output is bounded evidence, not a proof.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from z3 import Bool, BoolVal, Or, Solver, is_true, sat

from curling import curling_number, curling_number_reference


def no_square_suffix(bits: list[object]) -> list[object]:
    constraints: list[object] = []
    length = len(bits)
    for root in range(1, length // 2 + 1):
        constraints.append(
            Or(
                *(
                    bits[length - 2 * root + offset]
                    != bits[length - root + offset]
                    for offset in range(root)
                )
            )
        )
    return constraints


def solve_lengths(x_length: int, a_length: int, root: int):
    x = [Bool(f"x_{index}") for index in range(x_length)]
    a = x[x_length - a_length :]
    q = x + a + x + a + x
    n = len(q)
    cut = x_length + a_length

    solver = Solver()
    solver.add(x[0] == BoolVal(True))
    solver.add(a[0] == BoolVal(False))
    solver.add(*no_square_suffix(x))
    solver.add(*no_square_suffix(a + x))

    for block in (2, 3):
        for offset in range(root):
            solver.add(
                q[(cut - block * root + offset) % n]
                == q[(cut - root + offset) % n]
            )

    if solver.check() != sat:
        return None

    model = solver.model()
    x_word = tuple(3 if is_true(model.evaluate(bit)) else 2 for bit in x)
    a_word = x_word[-a_length:]
    q_word = x_word + a_word + x_word + a_word + x_word
    assert curling_number(x_word) == curling_number_reference(x_word) == 1
    assert curling_number(a_word + x_word) == curling_number_reference(
        a_word + x_word
    ) == 1
    assert all(
        q_word[(cut - block * root + offset) % len(q_word)]
        == q_word[(cut - root + offset) % len(q_word)]
        for block in (2, 3)
        for offset in range(root)
    )
    return x_word, a_word, q_word


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-x", type=int, default=40)
    args = parser.parse_args()

    cases = 0
    for x_length in range(2, args.max_x + 1):
        for a_length in range(1, x_length):
            n = 3 * x_length + 2 * a_length
            for root in range(1, n):
                cases += 1
                model = solve_lengths(x_length, a_length, root)
                if model is not None:
                    x_word, a_word, q_word = model
                    print(
                        "SAT",
                        f"|X|={x_length}",
                        f"|A|={a_length}",
                        f"root={root}",
                        f"X={''.join(map(str, x_word))}",
                        f"A={''.join(map(str, a_word))}",
                        f"Q={''.join(map(str, q_word))}",
                    )
                    return
        print(f"UNSAT through |X|={x_length}")
    print(f"UNSAT all {cases} fixed-length/root cases")


if __name__ == "__main__":
    main()
