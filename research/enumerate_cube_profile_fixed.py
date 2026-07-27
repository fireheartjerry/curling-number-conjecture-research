"""Enumerate binary circular words that encode their proper cube endpoints.

For a word ``w`` of length ``n``, the fixed equation is

    w[j] == 3  iff  some root 1 <= q < n gives a circular q-cube at cut j.

Models are independently audited with direct modular indexing.  Curling
numbers reported for rotations are recomputed by both implementations in
``curling.py``.  Enumeration is finite evidence, not a classification proof.
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


def circular_power(word: Word, cut: int, root: int, exponent: int) -> bool:
    n = len(word)
    return all(
        word[(cut - block * root + offset) % n]
        == word[(cut - root + offset) % n]
        for block in range(2, exponent + 1)
        for offset in range(root)
    )


def cube_roots(word: Word, cut: int) -> tuple[int, ...]:
    return tuple(
        root
        for root in range(1, len(word))
        if circular_power(word, cut, root, 3)
    )


def audit(word: Word) -> None:
    for cut, label in enumerate(word):
        assert bool(cube_roots(word, cut)) == (label == 3)


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def least_rotation(word: Word) -> Word:
    return min(word[index:] + word[:index] for index in range(len(word)))


def enumerate_models(n: int, timeout_ms: int, limit: int) -> list[Word]:
    symbols = [Bool(f"w_{index}") for index in range(n)]
    solver = Solver()
    if timeout_ms:
        solver.set(timeout=timeout_ms)

    def cube(cut: int, root: int):
        return And(
            *(
                symbols[(cut - block * root + offset) % n]
                == symbols[(cut - root + offset) % n]
                for block in range(2, 4)
                for offset in range(root)
            )
        )

    for cut in range(n):
        solver.add(
            symbols[cut]
            == Or(*(cube(cut, root) for root in range(1, n)))
        )
    solver.add(Not(symbols[0]))

    models: list[Word] = []
    while len(models) < limit and solver.check() == sat:
        model = solver.model()
        word = tuple(
            3 if is_true(model.eval(symbol)) else 2 for symbol in symbols
        )
        audit(word)
        models.append(word)
        solver.add(
            Or(
                *(
                    symbol != is_true(model.eval(symbol))
                    for symbol in symbols
                )
            )
        )
    return models


def describe(word: Word) -> str:
    roots = {
        cut: cube_roots(word, cut)
        for cut, label in enumerate(word)
        if label == 3
    }
    rotation_cns = tuple(
        exact_cn(word[index:] + word[:index])
        for index in range(len(word))
    )
    return (
        "word="
        + "".join(map(str, word))
        + " canonical="
        + "".join(map(str, least_rotation(word)))
        + f" roots={roots} rotation_cns={rotation_cns}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("minimum", type=int)
    parser.add_argument("maximum", type=int, nargs="?")
    parser.add_argument("--timeout-ms", type=int, default=30_000)
    parser.add_argument("--limit", type=int, default=10_000)
    args = parser.parse_args()
    maximum = args.minimum if args.maximum is None else args.maximum

    for n in range(args.minimum, maximum + 1):
        models = enumerate_models(n, args.timeout_ms, args.limit)
        necklaces = sorted({least_rotation(word) for word in models})
        print(
            f"length={n} models_with_first_2={len(models)} "
            f"necklaces={len(necklaces)}",
            flush=True,
        )
        for word in necklaces:
            print("  " + describe(word), flush=True)


if __name__ == "__main__":
    main()

