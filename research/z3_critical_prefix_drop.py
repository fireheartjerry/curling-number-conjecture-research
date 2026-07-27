"""Bounded search for a critical word with a strict final-prefix drop.

For a binary primitive word ``P`` the critical equations are encoded as

    pc_P(j) = P[j]

together with a label-matched proper circular witness whose powered span
is at most ``n+j-1`` at every phase.  By the fitting-witness theorem these
are equivalent to the two-copy deletion synchronization equations.

The extra condition is

    cn(P[:-1]) < P[-1].

This script is a bounded falsifier for the proposed terminal-prefix
equality theorem.  Every SAT model is checked against the original finite
curling-number equations using both implementations in ``curling.py``.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from z3 import And, Bool, Not, Or, Solver, is_true, sat  # type: ignore

from curling import curling_number, curling_number_reference


Word = tuple[int, ...]


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def primitive(word: Word) -> bool:
    n = len(word)
    return not any(
        n % period == 0
        and all(word[index] == word[index % period] for index in range(period, n))
        for period in range(1, n)
    )


def full_synchronization(word: Word) -> bool:
    n = len(word)
    for copies in (1, 2):
        for cut in range(n):
            target = word[cut]
            high = word * copies + word[:cut]
            deleted = word[1:] + word * (copies - 1) + word[:cut]
            if exact_cn(high) != target or exact_cn(deleted) != target:
                return False
    return True


def build_solver(n: int, timeout_ms: int):
    solver = Solver()
    if timeout_ms:
        solver.set(timeout=timeout_ms)

    # True is 3 and False is 2.
    word = [Bool(f"w_{index}") for index in range(n)]

    def power(cut: int, root: int, exponent: int):
        return And(
            *(
                word[(cut - block * root + offset) % n]
                == word[(cut - root + offset) % n]
                for block in range(2, exponent + 1)
                for offset in range(root)
            )
        )

    powers = {
        (cut, root, exponent): power(cut, root, exponent)
        for cut in range(n)
        for root in range(1, n)
        for exponent in (2, 3, 4)
    }

    for cut in range(n):
        squares = Or(*(powers[cut, root, 2] for root in range(1, n)))
        cubes = Or(*(powers[cut, root, 3] for root in range(1, n)))
        fourths = Or(*(powers[cut, root, 4] for root in range(1, n)))
        solver.add(squares, word[cut] == cubes, Not(fourths))

        fitting_squares = [
            powers[cut, root, 2]
            for root in range(1, n)
            if 2 * root <= n + cut - 1
        ]
        fitting_cubes = [
            powers[cut, root, 3]
            for root in range(1, n)
            if 3 * root <= n + cut - 1
        ]
        solver.add(Or(*fitting_squares) if fitting_squares else False)
        solver.add(
            word[cut]
            == (Or(*fitting_cubes) if fitting_cubes else False)
        )

    # The critical minimum and the strict terminal-prefix drop.
    solver.add(Not(word[0]))
    short_squares = [
        powers[n - 1, root, 2]
        for root in range(1, n)
        if 2 * root <= n - 1
    ]
    short_cubes = [
        powers[n - 1, root, 3]
        for root in range(1, n)
        if 3 * root <= n - 1
    ]
    no_short_square = Not(Or(*short_squares)) if short_squares else True
    no_short_cube = Not(Or(*short_cubes)) if short_cubes else True
    solver.add(
        # Last label 2: no square in P[:-1].
        # Last label 3: no cube in P[:-1].
        And(
            Or(word[-1], no_short_square),
            Or(Not(word[-1]), no_short_cube),
        )
    )

    for period in range(1, n):
        if n % period == 0:
            solver.add(
                Or(
                    *(
                        word[index] != word[index % period]
                        for index in range(period, n)
                    )
                )
            )
    return solver, word


def solve_length(n: int, timeout_ms: int) -> str:
    solver, symbols = build_solver(n, timeout_ms)
    result = solver.check()
    if result != sat:
        return str(result)

    model = solver.model()
    word = tuple(3 if is_true(model.eval(symbol)) else 2 for symbol in symbols)
    assert primitive(word)
    assert word[0] == 2
    assert full_synchronization(word)
    prefix_value = exact_cn(word[:-1])
    assert prefix_value < word[-1]
    return (
        "sat P="
        + "".join(map(str, word))
        + f" last={word[-1]} prefix_cn={prefix_value}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("minimum", type=int)
    parser.add_argument("maximum", type=int, nargs="?")
    parser.add_argument("--timeout-ms", type=int, default=30_000)
    args = parser.parse_args()
    maximum = args.minimum if args.maximum is None else args.maximum
    if args.minimum < 2 or maximum < args.minimum:
        raise SystemExit(2)

    for n in range(args.minimum, maximum + 1):
        print(
            f"length={n} result={solve_length(n, args.timeout_ms)}",
            flush=True,
        )


if __name__ == "__main__":
    main()
