"""Finite audits used in ``cross_rank_tower_audit.md``.

Run the repository's A094004 total-orbit-length calibration immediately
before this script.  The Fibonacci rows are bounded diagnostics only; the
unbounded Fibonacci construction is proved in ``recurrent_tower.md``.
"""

from __future__ import annotations

from fractions import Fraction

from check_external_reset_tau_rank import (
    primitive,
    proper_circular_profile,
)
from check_fixed_origin_delimiters import (
    encode_fibonacci,
    fibonacci_roots,
)
from curling import curling_number


Word = tuple[int, ...]


def circular_power(
    word: Word, cut: int, root: int, exponent: int
) -> bool:
    """Whether an exponent-power of root ``root`` ends at a circular cut."""
    n = len(word)
    return all(
        word[(cut - block * root + offset) % n]
        == word[(cut - root + offset) % n]
        for block in range(2, exponent + 1)
        for offset in range(root)
    )


def full_first_copy_fitting(word: Word) -> bool:
    """Check the square/cube fitting equivalences for a binary profile."""
    n = len(word)
    for cut in range(n):
        for exponent in (2, 3):
            circular = any(
                circular_power(word, cut, root, exponent)
                for root in range(1, n)
            )
            fitting = any(
                exponent * root <= n + cut
                and circular_power(word, cut, root, exponent)
                for root in range(1, n)
            )
            if circular != fitting:
                return False
    return True


def least_period(word: Word) -> int:
    """Return the least positive finite-word period."""
    for period in range(1, len(word) + 1):
        if all(
            word[index] == word[index + period]
            for index in range(len(word) - period)
        ):
            return period
    raise AssertionError("the full length is always a period")


def maximum_suffix_exponent(word: Word) -> Fraction:
    """Largest rational exponent among all nonempty suffixes."""
    return max(
        Fraction(len(word) - start, least_period(word[start:]))
        for start in range(len(word))
    )


def q21_golden_threshold_audit() -> tuple[int, int, Fraction]:
    """A replay cut whose strongest suffix repetition has order two."""
    root = tuple(map(int, "223222322232322232223"))
    assert primitive(root)
    assert proper_circular_profile(root) == root
    assert full_first_copy_fitting(root)

    state = root
    for offset in range(3):
        value = curling_number(state)
        assert value == root[offset]
        state += (value,)

    assert len(state) == 24
    assert curling_number(state) == root[3] == 2
    exponent = maximum_suffix_exponent(state)
    assert exponent == 2
    return len(root), len(state), exponent


def fibonacci_finite_audit() -> tuple[
    tuple[int, int, bool, int, int, bool], ...
]:
    """Check the strengthened near-model through root length 233."""
    roots = fibonacci_roots(3)
    encoded = tuple(encode_fibonacci(root) for root in roots)
    rows = []
    for level, root in enumerate(encoded[1:], start=1):
        profile = proper_circular_profile(root)
        rows.append(
            (
                level,
                len(root),
                primitive(root),
                min(profile),
                max(profile),
                full_first_copy_fitting(root),
            )
        )
        old_cube = encoded[level - 1] * 3
        assert encoded[level][: len(old_cube)] == old_cube
    expected = (
        (1, 13, True, 2, 3, True),
        (2, 55, True, 2, 3, True),
        (3, 233, True, 2, 3, True),
    )
    assert tuple(rows) == expected
    return tuple(rows)


def longest_common_suffix(left: Word, right: Word) -> int:
    """Length of the longest common suffix of two finite words."""
    length = 0
    while (
        length < min(len(left), len(right))
        and left[-1 - length] == right[-1 - length]
    ):
        length += 1
    return length


def external_child_seam_audit() -> tuple[
    tuple[str, int, int, int], ...
]:
    """Recompute the two archived all-external near-model seams."""
    q21 = tuple(map(int, "223222322232322232223"))
    partial = tuple(
        map(
            int,
            "223222322232322232223223222322232322232223"
            "2232223222323222322233"
            "232333332333322332222332222332232223232223"
            "2223323233333233332233"
            "222233222233",
        )
    )
    actual_parent = tuple(map(int, "223232223222322322232"))
    actual_child = actual_parent * 3 + (3,) + tuple(
        map(int, "2223222322322232")
    )

    partial_lcs = longest_common_suffix(partial, q21 * 3)
    actual_lcs = longest_common_suffix(actual_child, actual_parent * 3)
    assert (len(partial), partial_lcs) == (140, 1)
    assert (len(actual_child), actual_lcs) == (80, 25)

    forced_cut = 3 * len(actual_parent) - actual_lcs
    actual_profile = proper_circular_profile(actual_child)
    assert forced_cut == 38
    assert (
        actual_child[forced_cut],
        actual_profile[forced_cut],
    ) == (2, 3)
    return (
        ("partial", len(partial), partial_lcs, -1),
        ("actual", len(actual_child), actual_lcs, forced_cut),
    )


if __name__ == "__main__":
    print("Q21_GOLDEN=" + repr(q21_golden_threshold_audit()))
    print("FIBONACCI_NEAR_MODEL=" + repr(fibonacci_finite_audit()))
    print("EXTERNAL_CHILD_SEAM=" + repr(external_child_seam_audit()))
