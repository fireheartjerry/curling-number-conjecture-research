"""Executable checks for the compactness/escaping-root countermodel.

The curling-number implementation used here is calibrated separately by

    python -m unittest \
      tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration

which checks the A094004 total-length values 5, 66, and 142 at starting
lengths 3, 8, and 22.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference


def hall_thue_prefix(minimum_length):
    """Return a prefix of the fixed point 0 -> 012, 1 -> 02, 2 -> 1."""
    word = (0,)
    while len(word) < minimum_length:
        word = tuple(
            output
            for letter in word
            for output in (
                (0, 1, 2)
                if letter == 0
                else (0, 2)
                if letter == 1
                else (1,)
            )
        )
    return word


def contains_power(word, exponent):
    """Return whether word has a contiguous factor equal to V^exponent."""
    for start in range(len(word)):
        remaining = len(word) - start
        for root_length in range(1, remaining // exponent + 1):
            root = word[start : start + root_length]
            if word[start : start + exponent * root_length] == root * exponent:
                return True
    return False


def suffix_exponent(word, root_length):
    """Number of consecutive copies of the final root-length block."""
    root = word[-root_length:]
    exponent = 0
    cursor = len(word)
    while cursor >= root_length and word[cursor - root_length : cursor] == root:
        exponent += 1
        cursor -= root_length
    return exponent


def maximizing_root_lengths(word):
    """Return the maximum suffix exponent and every root length attaining it."""
    spectrum = tuple(
        (root_length, suffix_exponent(word, root_length))
        for root_length in range(1, len(word) + 1)
    )
    maximum = max(exponent for _, exponent in spectrum)
    return maximum, tuple(
        root_length
        for root_length, exponent in spectrum
        if exponent == maximum
    )


def main():
    radii = (8, 13, 21, 34, 55)
    raw = hall_thue_prefix(1000)
    cut = next(
        index
        for index in range(300, len(raw) - max(radii))
        if raw[index] == 0
    )
    coded = tuple(letter + 2 for letter in raw)

    rows = []
    for radius in radii:
        left_context = coded[cut - radius : cut]
        right_context = coded[cut : cut + radius]
        assert coded[cut] == 2
        assert not contains_power(left_context, 2)

        # The fresh marker 5 is outside the coded Hall--Thue alphabet {2, 3, 4}.
        root = (5,) + left_context
        state = root * 2

        fast = curling_number(state)
        reference = curling_number_reference(state)
        maximum, maximizing_roots = maximizing_root_lengths(state)

        assert fast == reference == maximum == 2
        assert maximizing_roots == (len(root),)
        assert state[-radius:] == left_context

        centered_approximant = state + right_context
        assert centered_approximant[
            len(state) - radius : len(state) + radius
        ] == coded[cut - radius : cut + radius]

        rows.append(
            (
                radius,
                len(root),
                fast,
                maximizing_roots,
            )
        )

    print("convention: cn(state) is the maximum repeated-suffix exponent")
    print(f"Hall--Thue cut={cut}, coded cut symbol={coded[cut]}")
    for radius, root_length, value, roots in rows:
        print(
            f"radius={radius}: cn={value}, "
            f"least/maximizing roots={roots}, expected root={root_length}"
        )


if __name__ == "__main__":
    main()
