"""Finite audit for ``immediate_power_coupling.md``.

This checks the append bound, the same-scale-or-drop inequality, the
distinct-completion separation inequality, and the displayed calibration.
It is a bounded falsifier, not part of the proofs.
"""

from __future__ import annotations

from itertools import product
from math import gcd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import (
    curling_number,
    curling_number_reference,
    tail_length,
)


Word = tuple[int, ...]


def primitive(word: Word) -> bool:
    n = len(word)
    return not any(
        n % d == 0 and word == word[:d] * (n // d)
        for d in range(1, n)
    )


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def primitive_power_suffixes(word: Word):
    n = len(word)
    for exponent in range(2, n + 1):
        for root_length in range(1, n // exponent + 1):
            root = word[-root_length:]
            if primitive(root) and word[-exponent * root_length :] == root * exponent:
                yield exponent, root_length


def check_append_bound() -> int:
    checked = 0
    for n in range(1, 9):
        for word in product((2, 3, 4), repeat=n):
            old = exact_cn(word)
            for value in (1, 2, 3, 4, 5):
                assert exact_cn(word + (value,)) <= old + 1
                checked += 1
    return checked


def check_same_scale_or_drop() -> int:
    checked = 0
    for r in range(1, 8):
        for root in product((2, 3, 4), repeat=r):
            if not primitive(root):
                continue
            for exponent in range(2, 6):
                for value in (1, 2, 3, 4, 5):
                    words = (
                        root * exponent + (value,),
                        root[1:] + root * (exponent - 1) + (value,),
                    )
                    for word in words:
                        for power, length in primitive_power_suffixes(word):
                            if length == r:
                                assert value == root[0]
                            else:
                                assert (power - 1) * length + gcd(r, length) <= r
                            checked += 1
    return checked


def check_distinct_completions() -> int:
    checked = 0
    for n in range(0, 8):
        for prefix in product((2, 3), repeat=n):
            left = prefix + (2,)
            right = prefix + (3,)
            for u, p in primitive_power_suffixes(left):
                for v, q in primitive_power_suffixes(right):
                    assert p != q
                    g = gcd(p, q)
                    if p < q:
                        assert (u - 1) * p + g <= q
                    else:
                        assert (v - 1) * q + g <= p
                    checked += 1
    return checked


def calibration() -> None:
    root = tuple(map(int, "2322232"))
    exponent = 3
    high = root * exponent
    low = high[1:]
    actual = high + (exponent,)
    wrong = high + (exponent - 1,)
    actual_deleted = actual[1:]
    wrong_deleted = wrong[1:]

    expected = {
        "A": (high, 3, 60, (7,)),
        "L": (low, 2, 4, (4, 7)),
        "H": (actual, 2, 59, (2,)),
        "W": (wrong, 3, 3, (7,)),
        "C": (actual_deleted, 2, 59, (2,)),
        "B": (wrong_deleted, 3, 3, (7,)),
    }
    for name, (word, value, tail, roots) in expected.items():
        assert exact_cn(word) == value
        assert tail_length(word, step_limit=1000) == tail
        maximizing = tuple(
            length
            for length in range(1, len(word) // value + 1)
            if word[-value * length :] == word[-length:] * value
        )
        assert maximizing == roots, (name, maximizing, roots)


def check_root_two_orbits() -> int:
    checked = 0
    for exponent in range(2, 31):
        for other in tuple(range(-2, 33)) + (1000,):
            if other == exponent:
                continue
            for root, expected in (
                (
                    (other, exponent),
                    (2, 2, 3, 1) if exponent == 2 else (exponent, 2, 1),
                ),
                (
                    (exponent, other),
                    (2, 2, 2, 3, 1)
                    if exponent == 2
                    else (exponent, exponent, 2, 1),
                ),
            ):
                word = root * exponent
                observed = []
                for _ in expected:
                    value = exact_cn(word)
                    observed.append(value)
                    if value != 1:
                        word += (value,)
                assert tuple(observed) == expected
                checked += 1
    return checked


def main() -> None:
    append_cases = check_append_bound()
    drop_cases = check_same_scale_or_drop()
    separation_cases = check_distinct_completions()
    calibration()
    root_two_cases = check_root_two_orbits()
    print(
        "audit passed",
        f"append_cases={append_cases}",
        f"drop_witnesses={drop_cases}",
        f"separation_pairs={separation_cases}",
        f"root_two_orbits={root_two_cases}",
        "calibration=passed",
    )


if __name__ == "__main__":
    main()
