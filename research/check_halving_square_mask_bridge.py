"""Exact countermodel to automatic low-square inheritance.

The mathematical record is ``halving_square_mask_bridge.md``.  This script
checks a rotation of the length-21 exact binary circular profile.  It verifies
that a globally maximal primitive cube has a primitive period word with two
low phases that are not internally squareful.  The ambient rescue squares at
those phases both cross the cube's left boundary, and their maximal runs meet
the cube run at exactly the Fine--Wilf threshold minus one.

Run the repository's A094004 calibration immediately before this script.
"""

from __future__ import annotations

from math import gcd

from check_max_square_terminal_forest import fitting
from check_run_length_grammar import (
    primitive,
    proper_profile,
    word_power_root_lengths,
)


Word = tuple[int, ...]
Q21: Word = tuple(map(int, "223222322232322232223"))
PARENT_CUT = 12
PARENT_ROOT = 4
PARENT_LEFT = PARENT_CUT - 3 * PARENT_ROOT


def factor(word: Word, left: int, right: int) -> Word:
    """Read ``[left,right)`` from the bi-infinite periodic lift."""

    n = len(word)
    return tuple(word[index % n] for index in range(left, right))


def least_period(word: Word) -> int:
    """Return the least ordinary period of a nonempty finite word."""

    return next(
        period
        for period in range(1, len(word) + 1)
        if all(word[index] == word[index - period]
               for index in range(period, len(word)))
    )


def maximal_run(
    word: Word, left: int, right: int, period: int
) -> tuple[int, int]:
    """Extend a periodic interval maximally in the periodic lift."""

    n = len(word)
    while word[(left - 1) % n] == word[(left - 1 + period) % n]:
        left -= 1
    while word[right % n] == word[(right - period) % n]:
        right += 1
    return left, right


def root_set_table(word: Word) -> tuple[tuple[tuple[int, ...], ...], ...]:
    """All proper circular square/cube/fourth root sets at every cut."""

    return tuple(
        tuple(word_power_root_lengths(word, cut, exponent)
              for exponent in (2, 3, 4))
        for cut in range(len(word))
    )


def main() -> None:
    n = len(Q21)
    assert n == 21
    assert primitive(Q21)
    assert proper_profile(Q21) == Q21
    assert all(
        Q21[index] != 3 or Q21[(index + 1) % n] != 3
        for index in range(n)
    )

    # This is the full critical first-copy fitting condition, not merely
    # circular exactness.
    assert all(
        any(
            fitting(Q21, cut, value, root)
            for root in word_power_root_lengths(Q21, cut, value)
        )
        for cut, value in enumerate(Q21)
    )

    table = root_set_table(Q21)
    cube_records = tuple(
        (cut, table[cut][1])
        for cut, value in enumerate(Q21)
        if value == 3
    )
    assert cube_records == (
        (2, (4,)),
        (6, (1,)),
        (10, (1,)),
        (12, (4,)),
        (16, (1,)),
        (20, (1,)),
    )
    assert max(root for _, roots in cube_records for root in roots) == 4

    parent = factor(Q21, PARENT_LEFT, PARENT_CUT)
    root = factor(Q21, PARENT_LEFT, PARENT_LEFT + PARENT_ROOT)
    assert PARENT_LEFT == 0
    assert root == tuple(map(int, "2232"))
    assert primitive(root)
    assert parent == root * 3
    assert Q21[PARENT_CUT] == 3
    assert fitting(Q21, PARENT_CUT, 3, PARENT_ROOT)

    parent_run = maximal_run(
        Q21, PARENT_LEFT, PARENT_CUT, PARENT_ROOT
    )
    assert parent_run == (0, 12)
    assert least_period(factor(Q21, *parent_run)) == PARENT_ROOT

    root_profile = proper_profile(root)
    assert root_profile == (1, 2, 3, 1)
    holes = tuple(
        phase
        for phase, value in enumerate(root)
        if value == 2
        and not word_power_root_lengths(root, phase, 2)
    )
    assert holes == (0, 3)

    # Put each hole in the second copy of root^3.  The complete lists of
    # ambient proper square roots are respectively one strict DROP and one
    # strict ASCENT relative to the parent period four.
    records = []
    expected = {
        0: (4, (3,), (-2, 4), (-3, 5), "232"),
        3: (7, (7,), (-7, 7), (-7, 9), "2232223"),
    }
    for phase in holes:
        cut = PARENT_ROOT + phase
        roots = word_power_root_lengths(Q21, cut, 2)
        expected_cut, expected_roots, square_interval, run_interval, text = (
            expected[phase]
        )
        assert cut == expected_cut
        assert roots == expected_roots
        assert word_power_root_lengths(Q21, cut, 3) == ()
        assert Q21[cut] == 2

        rescue_root = roots[0]
        assert fitting(Q21, cut, 2, rescue_root)
        assert square_interval == (cut - 2 * rescue_root, cut)
        square = factor(Q21, *square_interval)
        rescue_word = factor(
            Q21, square_interval[0], square_interval[0] + rescue_root
        )
        assert square == rescue_word * 2
        assert primitive(rescue_word)
        assert "".join(map(str, rescue_word)) == text
        assert square_interval[0] < PARENT_LEFT

        rescue_run = maximal_run(
            Q21, square_interval[0], square_interval[1], rescue_root
        )
        assert rescue_run == run_interval
        assert least_period(factor(Q21, *rescue_run)) == rescue_root

        overlap_left = max(parent_run[0], rescue_run[0])
        overlap_right = min(parent_run[1], rescue_run[1])
        overlap = overlap_right - overlap_left
        threshold = PARENT_ROOT + rescue_root - gcd(
            PARENT_ROOT, rescue_root
        )
        assert overlap == threshold - 1

        records.append(
            {
                "phase": phase,
                "child_cut": cut,
                "child_internal_square_roots": (),
                "ambient_square_roots": roots,
                "ambient_square_interval": square_interval,
                "ambient_square_root_word": text,
                "ambient_maximal_run": rescue_run,
                "parent_maximal_run": parent_run,
                "run_overlap": overlap,
                "fine_wilf_threshold": threshold,
            }
        )

    assert records[0]["ambient_square_roots"][0] < PARENT_ROOT
    assert records[1]["ambient_square_roots"][0] > PARENT_ROOT

    print(
        {
            "ambient": "".join(map(str, Q21)),
            "ambient_length": n,
            "ambient_exact_profile": True,
            "ambient_full_first_copy_fitting": True,
            "singleton_3_runs": True,
            "global_max_cube_root": PARENT_ROOT,
            "parent_cube": (
                (PARENT_LEFT, PARENT_CUT),
                "".join(map(str, root)),
            ),
            "child_profile": root_profile,
            "child_low_square_holes": holes,
            "crossing_rescues": tuple(records),
        }
    )


if __name__ == "__main__":
    main()
