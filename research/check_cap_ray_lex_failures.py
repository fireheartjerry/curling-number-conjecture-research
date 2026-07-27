"""Executed countermodels to nodewise lexicographic cap ranks.

Each finite word is given with an integer left coordinate.  Every
distinguished square/cube equality is asserted, and every displayed
curling number is recomputed by both implementations in ``curling.py``.
The models are local transition records, not circular fixed profiles.
"""

from __future__ import annotations

import sys
from math import lcm
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from curling import curling_number, curling_number_reference

from check_run_length_grammar import primitive, proper_profile


Word = tuple[int, ...]


def factor(word: Word, left: int, start: int, end: int) -> Word:
    return word[start - left : end - left]


def checked_cn(word: Word, left: int, cut: int) -> int:
    prefix = factor(word, left, left, cut)
    value = curling_number(prefix)
    assert value == curling_number_reference(prefix)
    return value


def periodic_compare(a: Word, b: Word) -> tuple[int, int]:
    """Compare a^omega and b^omega; return sign and first mismatch."""
    for index in range(lcm(len(a), len(b))):
        left_value = a[index % len(a)]
        right_value = b[index % len(b)]
        if left_value != right_value:
            return (
                1 if left_value > right_value else -1,
                index,
            )
    return (0, -1)


def reversed_endpoint_ray(root: Word) -> Word:
    return root[::-1]


def high_oriented_ray(root: Word, distance: int) -> Word:
    """One period read leftward, starting at the last high symbol."""
    return tuple(
        root[(-distance - index) % len(root)]
        for index in range(len(root))
    )


def least_conjugate(root: Word) -> Word:
    return min(
        root[index:] + root[:index]
        for index in range(len(root))
    )


def assert_power(
    word: Word,
    left: int,
    end: int,
    root_length: int,
    exponent: int,
) -> Word:
    powered = factor(
        word,
        left,
        end - exponent * root_length,
        end,
    )
    root = powered[:root_length]
    assert powered == root * exponent
    assert primitive(root)
    return root


def endpoint_ray_models() -> dict[str, object]:
    slow_left = -26
    slow_word = tuple(map(int, "233223232332232323322323322"))
    slow_parent = assert_power(slow_word, slow_left, 0, 6, 2)
    slow_child = assert_power(slow_word, slow_left, -2, 8, 3)
    assert slow_parent == tuple(map(int, "232332"))
    assert slow_child == tuple(map(int, "23322323"))
    slow_order = periodic_compare(
        reversed_endpoint_ray(slow_parent),
        reversed_endpoint_ray(slow_child),
    )
    assert slow_order == (-1, 0)
    slow_cn = {
        cut: checked_cn(slow_word, slow_left, cut)
        for cut in (-10, -2, 0)
    }
    assert slow_cn == {-10: 2, -2: 3, 0: 2}

    drop_left = -14
    drop_word = tuple(map(int, "323233232323322"))
    drop_parent = assert_power(drop_word, drop_left, 0, 7, 2)
    drop_child = assert_power(drop_word, drop_left, -2, 2, 3)
    assert drop_parent == tuple(map(int, "3232332"))
    assert drop_child == tuple(map(int, "23"))
    drop_order = periodic_compare(
        reversed_endpoint_ray(drop_parent),
        reversed_endpoint_ray(drop_child),
    )
    assert drop_order == (-1, 0)
    drop_cn = {
        cut: checked_cn(drop_word, drop_left, cut)
        for cut in (-4, -2, 0)
    }
    assert drop_cn == {-4: 2, -2: 3, 0: 2}

    return {
        "slow_ascent": {
            "indexed_word": (slow_left, "".join(map(str, slow_word))),
            "roots": tuple(
                "".join(map(str, root))
                for root in (slow_parent, slow_child)
            ),
            "reversed_ray_order": slow_order,
            "curling_values": slow_cn,
        },
        "drop": {
            "indexed_word": (drop_left, "".join(map(str, drop_word))),
            "roots": tuple(
                "".join(map(str, root))
                for root in (drop_parent, drop_child)
            ),
            "reversed_ray_order": drop_order,
            "curling_values": drop_cn,
        },
    }


def high_ray_two_edge_model() -> dict[str, object]:
    left = -26
    word = tuple(map(int, "233223233223233223322332322"))
    first = assert_power(word, left, 0, 2, 2)
    second = assert_power(word, left, -2, 4, 3)
    third = assert_power(word, left, -8, 6, 3)
    assert first == tuple(map(int, "32"))
    assert second == tuple(map(int, "2332"))
    assert third == tuple(map(int, "233223"))

    first_order = periodic_compare(
        high_oriented_ray(first, 2),
        high_oriented_ray(second, 2),
    )
    second_order = periodic_compare(
        high_oriented_ray(second, 2),
        high_oriented_ray(third, 1),
    )
    assert first_order == (-1, 1)
    assert second_order == (1, 1)

    curling_values = {
        cut: checked_cn(word, left, cut)
        for cut in (-14, -8, -6, -2, 0)
    }
    assert curling_values == {
        -14: 2,
        -8: 3,
        -6: 2,
        -2: 3,
        0: 2,
    }
    return {
        "indexed_word": (left, "".join(map(str, word))),
        "roots": tuple(
            "".join(map(str, root))
            for root in (first, second, third)
        ),
        "high_ray_orders": (first_order, second_order),
        "curling_values": curling_values,
    }


def necklace_nonterminal_model() -> dict[str, object]:
    left = -37
    word = tuple(
        map(int, "23232332232232323322322323233223232332")
    )
    first = assert_power(word, left, 0, 8, 2)
    second = assert_power(word, left, -1, 2, 3)
    third = assert_power(word, left, -4, 11, 3)
    assert first == tuple(map(int, "22323233"))
    assert second == tuple(map(int, "23"))
    assert third == tuple(map(int, "23232332232"))
    assert max(proper_profile(first)) <= 3
    assert max(proper_profile(second)) <= 3
    assert max(proper_profile(third)) <= 3

    necklaces = tuple(map(least_conjugate, (first, second, third)))
    first_order = periodic_compare(necklaces[0], necklaces[1])
    contracted_order = periodic_compare(necklaces[0], necklaces[2])
    assert first_order == (-1, 1)
    assert contracted_order[0] == 1

    curling_values = {
        cut: checked_cn(word, left, cut)
        for cut in (-15, -4, -3, -1, 0)
    }
    assert curling_values == {
        -15: 2,
        -4: 3,
        -3: 2,
        -1: 3,
        0: 2,
    }
    return {
        "indexed_word": (left, "".join(map(str, word))),
        "roots": tuple(
            "".join(map(str, root))
            for root in (first, second, third)
        ),
        "least_conjugates": tuple(
            "".join(map(str, root))
            for root in necklaces
        ),
        "first_edge_order": first_order,
        "contracted_peak_order": contracted_order,
        "curling_values": curling_values,
    }


def main() -> None:
    print(
        {
            "endpoint_rays": endpoint_ray_models(),
            "high_oriented_two_edge": high_ray_two_edge_model(),
            "least_conjugate_nonterminal": necklace_nonterminal_model(),
        }
    )


if __name__ == "__main__":
    main()
