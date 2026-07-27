"""Search full critical-synchronization words containing adjacent ``33``.

For a primitive binary word P of length n, the critical synchronization
equations are

    cn(P**a + P[:j]) = P[j]
    cn(P[1:] + P**(a-1) + P[:j]) = P[j]

for a in {1, 2} and 0 <= j < n.  Under the exact proper-circular profile
equation pc_P=P, these equations are equivalent to the first deleted-copy
fitting conditions encoded below:

    some P[j]-power ending at circular cut j has span <= n+j-1.

The direct checker audits the original finite curling-number equations for
every satisfying SAT model.  This script is a bounded falsifier, not a
proof of unsatisfiability at arbitrary length.
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


def primitive(word: Word) -> bool:
    n = len(word)
    return not any(
        n % period == 0
        and all(word[index] == word[index % period] for index in range(period, n))
        for period in range(1, n)
    )


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


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


def build_solver(n: int, timeout_ms: int, require_adjacent: bool = True):
    solver = Solver()
    if timeout_ms:
        solver.set(timeout=timeout_ms)

    # True means 3 and False means 2.
    word = [Bool(f"w_{index}") for index in range(n)]

    def equal(left: int, right: int):
        return word[left % n] == word[right % n]

    def power(cut: int, root: int, exponent: int):
        return And(
            *(
                equal(cut - block * root + offset, cut - root + offset)
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

    # Exact proper circular profile in {2,3}.
    for cut in range(n):
        squares = Or(*(powers[cut, root, 2] for root in range(1, n)))
        cubes = Or(*(powers[cut, root, 3] for root in range(1, n)))
        fourths = Or(*(powers[cut, root, 4] for root in range(1, n)))
        solver.add(squares)
        solver.add(word[cut] == cubes)
        solver.add(Not(fourths))

        # The deleted first-copy state has length n+cut-1.  Require a
        # label-matched witness whose complete powered suffix fits.
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

    # The actual deleted symbol is the critical minimum label 2.
    solver.add(Not(word[0]))

    if require_adjacent:
        solver.add(
            Or(
                *(
                    And(word[cut], word[(cut + 1) % n])
                    for cut in range(n)
                )
            )
        )

    # Exclude every divisor period of P.
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
    assert any(
        word[cut] == word[(cut + 1) % n] == 3 for cut in range(n)
    )
    assert full_synchronization(word)
    return "sat P=" + "".join(map(str, word))


def calibrate_known_word() -> None:
    known = tuple(map(int, "223222322232322232223"))
    assert primitive(known)
    assert full_synchronization(known)
    assert not any(
        known[cut] == known[(cut + 1) % len(known)] == 3
        for cut in range(len(known))
    )

    solver, symbols = build_solver(
        len(known), timeout_ms=0, require_adjacent=False
    )
    solver.add(
        *(symbol == (value == 3) for symbol, value in zip(symbols, known))
    )
    assert solver.check() == sat


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("minimum", type=int)
    parser.add_argument("maximum", type=int, nargs="?")
    parser.add_argument("--timeout-ms", type=int, default=30_000)
    args = parser.parse_args()
    maximum = args.minimum if args.maximum is None else args.maximum
    if args.minimum < 2 or maximum < args.minimum:
        raise SystemExit(2)

    calibrate_known_word()
    for n in range(args.minimum, maximum + 1):
        print(
            f"length={n} result={solve_length(n, args.timeout_ms)}",
            flush=True,
        )


if __name__ == "__main__":
    main()
