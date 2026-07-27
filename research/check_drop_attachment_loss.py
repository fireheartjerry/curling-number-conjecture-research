"""Executed local countergeometry to automatic attachment in a DROP step.

The finite word is indexed from -2 through 14.  It simultaneously has

* a primitive root-7 square on [0, 14);
* a primitive root-2 cube on [6, 12);
* a primitive root-5 square on [-2, 8).

Thus the root-5 mask is a strict DROP from seven, but it crosses the
left boundary of the parent square and does not contain the child cube.
The three distinguished finite suffixes have exact curling values
2, 3, and 2; both independent implementations recompute them.

This is a local word-equation certificate, not a circular fixed profile.
It shows that attachment cannot be deduced from the period-overlap and
endpoint-value hypotheses alone.
"""

from __future__ import annotations

import sys
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from curling import curling_number, curling_number_reference

from check_run_length_grammar import primitive


Word = tuple[int, ...]

LEFT = -2
WORD: Word = tuple(map(int, "23323233232323322"))

PARENT_START = 0
PARENT_END = 14
PARENT_ROOT = 7

CHILD_START = 6
CHILD_END = 12
CHILD_ROOT = 2

MASK_START = -2
MASK_END = 8
MASK_ROOT = 5

DISTANCE = 2
HOLE_PHASE = 0
PRE_HOLE_HIGH = 7


def factor(start: int, end: int) -> Word:
    assert LEFT <= start <= end <= LEFT + len(WORD)
    return WORD[start - LEFT : end - LEFT]


def is_power(word: Word, root: int, exponent: int) -> bool:
    return len(word) == root * exponent and word == word[:root] * exponent


def circular_ends_power(
    word: Word,
    cut: int,
    root: int,
    exponent: int,
) -> bool:
    size = len(word)
    return all(
        word[(cut - block * root + offset) % size]
        == word[(cut - root + offset) % size]
        for block in range(2, exponent + 1)
        for offset in range(root)
    )


def checked_cn_at(cut: int) -> int:
    prefix = factor(LEFT, cut)
    value = curling_number(prefix)
    assert value == curling_number_reference(prefix)
    return value


def known_square_mismatches(cut: int, root: int) -> tuple[tuple[int, int], ...]:
    """Known unequal coordinate pairs needed by the final two root blocks."""
    values = {
        LEFT + offset: value
        for offset, value in enumerate(WORD)
    }
    mismatches = []
    for offset in range(root):
        right = cut - root + offset
        left = cut - 2 * root + offset
        if (
            right in values
            and left in values
            and values[right] != values[left]
        ):
            mismatches.append((right, left))
    return tuple(mismatches)


def main() -> None:
    parent = factor(PARENT_START, PARENT_END)
    child = factor(CHILD_START, CHILD_END)
    mask = factor(MASK_START, MASK_END)

    assert is_power(parent, PARENT_ROOT, 2)
    assert is_power(child, CHILD_ROOT, 3)
    assert is_power(mask, MASK_ROOT, 2)

    parent_word = parent[:PARENT_ROOT]
    child_word = child[:CHILD_ROOT]
    mask_word = mask[:MASK_ROOT]
    assert primitive(parent_word)
    assert primitive(child_word)
    assert primitive(mask_word)

    # The selected phase zero of V=(2,3) has no proper circular square.
    assert not any(
        circular_ends_power(child_word, HOLE_PHASE, root, 2)
        for root in range(1, CHILD_ROOT)
    )

    p = PARENT_ROOT
    q = CHILD_ROOT
    s = MASK_ROOT
    d = DISTANCE
    t = HOLE_PHASE
    D = PARENT_END - d - 2 * q + t - PARENT_START

    assert D == MASK_END - PARENT_START == 8
    assert p > 2 * q + gcd(p, q)
    assert s < p
    assert 2 * s > D
    assert MASK_START == MASK_END - 2 * s < PARENT_START
    assert not (
        MASK_START <= CHILD_START and CHILD_END <= MASK_END
    )

    curling_values = {
        MASK_END: checked_cn_at(MASK_END),
        CHILD_END: checked_cn_at(CHILD_END),
        PARENT_END: checked_cn_at(PARENT_END),
    }
    assert curling_values == {8: 2, 12: 3, 14: 2}

    # This local geometry cannot be embedded in the globally maximal
    # p=7 circular setup.  Exactness at the preceding high cut 7 would
    # require a cube root at most seven.  Roots other than five already
    # fail a known equality in their final two blocks.
    mismatch_roots = {
        root: known_square_mismatches(PRE_HOLE_HIGH, root)
        for root in range(1, PARENT_ROOT + 1)
    }
    assert all(
        mismatch_roots[root]
        for root in (1, 2, 3, 4, 6, 7)
    )
    assert mismatch_roots[5] == ()

    # A hypothetical root-five cube ending at 7 extends one symbol to
    # the low cut 8.  The new equality P[7]=P[2] is supplied by the
    # displayed root-five mask square, and both symbols are three.
    assert WORD[PRE_HOLE_HIGH - LEFT] == 3
    assert WORD[PRE_HOLE_HIGH - MASK_ROOT - LEFT] == 3
    root_five_extends_to_low = True

    print(
        {
            "indexed_word": (LEFT, "".join(map(str, WORD))),
            "parent": (
                (PARENT_START, PARENT_END),
                PARENT_ROOT,
                "".join(map(str, parent_word)),
            ),
            "child": (
                (CHILD_START, CHILD_END),
                CHILD_ROOT,
                "".join(map(str, child_word)),
            ),
            "mask": (
                (MASK_START, MASK_END),
                MASK_ROOT,
                "".join(map(str, mask_word)),
            ),
            "D": D,
            "mask_crosses_parent_left": True,
            "mask_contains_child": False,
            "curling_values": curling_values,
            "pre_hole_high": PRE_HOLE_HIGH,
            "cube_roots_1_to_7_rejected_by_known_mismatch": tuple(
                root for root in mismatch_roots if mismatch_roots[root]
            ),
            "remaining_root_5_extends_to_low_cut_8": root_five_extends_to_low,
            "embeddable_with_global_cube_bound_7": False,
        }
    )


if __name__ == "__main__":
    main()
