"""Executable audits for the restricted adjacent-2/3 Hamming rank.

Run the A094004 calibration before this file.  Every curling number and
every orbit step below is recomputed by the two independent implementations
in ``curling.py``.

The examples are finite timing near-models.  They do not contain a bad word
and therefore do not refute a theorem which uses infinite badness.
"""

from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference


Word = tuple[int, ...]


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def exact_tail(word: Word, limit: int = 10_000) -> int:
    state = word
    for step in range(limit + 1):
        value = exact_cn(state)
        if value == 1:
            return step
        state = state + (value,)
    raise AssertionError(("tail limit exceeded", word, limit))


def maximizing_roots(word: Word) -> tuple[tuple[int, Word, int], ...]:
    """Return (root length, root, powered-suffix start) for every maximizer."""

    exponent = exact_cn(word)
    records: list[tuple[int, Word, int]] = []
    for root_length in range(1, len(word) // exponent + 1):
        root = word[-root_length:]
        start = len(word) - exponent * root_length
        if word[start:] == root * exponent:
            records.append((root_length, root, start))
    assert records
    return tuple(records)


def is_primitive(word: Word) -> bool:
    return all(
        word != word[:period] * (len(word) // period)
        for period in range(1, len(word))
        if len(word) % period == 0
    )


def conserved_rank_orientation_switch() -> dict[str, object]:
    """A unique defect-crossing cube reverses the timing orientation."""

    common = tuple(map(int, "223222322232"))
    long_side = common + (2,)
    short_side = common + (3,)
    defect = len(common)

    assert exact_cn(long_side) == 3
    assert exact_cn(short_side) == 2
    assert exact_tail(long_side) == 53
    assert exact_tail(short_side) == 52

    roots = maximizing_roots(long_side)
    assert roots == ((4, (2, 3, 2, 2), 1),)
    root_length, root, start = roots[0]
    assert start <= defect < start + 3 * root_length

    cut_long = long_side[start:]
    cut_short = short_side[start:]
    assert cut_long == root * 3
    assert exact_tail(cut_long) == 53
    assert exact_tail(cut_short) == 62

    parent_endpoint = len(short_side) + exact_tail(short_side)
    # After the cut the finite long/short timing orientation reverses, so the
    # shorter-tail endpoint is cut_long.
    child_endpoint = len(cut_long) + exact_tail(cut_long)
    assert parent_endpoint == child_endpoint == 65

    for word in (long_side, short_side):
        assert word.count(2) >= 2
        assert word.count(3) >= 2

    return {
        "common_prefix": "".join(map(str, common)),
        "long_side": "".join(map(str, long_side)),
        "short_side": "".join(map(str, short_side)),
        "defect_index": defect,
        "curling_numbers": (exact_cn(long_side), exact_cn(short_side)),
        "tail_lengths": (exact_tail(long_side), exact_tail(short_side)),
        "unique_larger_cn_root": {
            "root": "".join(map(str, root)),
            "root_length": root_length,
            "powered_suffix_start": start,
        },
        "cut_words": (
            "".join(map(str, cut_long)),
            "".join(map(str, cut_short)),
        ),
        "cut_tail_lengths": (exact_tail(cut_long), exact_tail(cut_short)),
        "parent_endpoint": parent_endpoint,
        "reoriented_child_endpoint": child_endpoint,
    }


def pure_cube_actual_completion_rank_increase() -> dict[str, object]:
    """An actual 3-completion whose short crossing-root cut raises rank."""

    root = tuple(map(int, "23222322232"))
    assert is_primitive(root)
    cube = root * 3
    actual = cube + (3,)
    wrong = cube + (2,)

    assert exact_cn(cube) == 3
    assert exact_cn(actual) == 2
    assert exact_cn(wrong) == 3
    assert exact_tail(actual) == 42
    assert exact_tail(wrong) == 3

    roots = maximizing_roots(wrong)
    assert roots == (
        (4, (2, 3, 2, 2), 22),
        (11, (3, 2, 2, 2, 3, 2, 2, 2, 3, 2, 2), 1),
    )

    short_start = roots[0][2]
    short_actual = actual[short_start:]
    short_wrong = wrong[short_start:]
    assert exact_tail(short_actual) == 62
    assert exact_tail(short_wrong) == 53

    parent_endpoint = len(wrong) + exact_tail(wrong)
    short_root_endpoint = len(short_wrong) + exact_tail(short_wrong)
    assert parent_endpoint == 37
    assert short_root_endpoint == 65

    ambient_start = roots[1][2]
    ambient_actual = actual[ambient_start:]
    ambient_wrong = wrong[ambient_start:]
    assert exact_tail(ambient_actual) == 42
    assert exact_tail(ambient_wrong) == 3
    ambient_endpoint = len(ambient_wrong) + exact_tail(ambient_wrong)
    assert ambient_endpoint == 36

    return {
        "primitive_source_root": "".join(map(str, root)),
        "source_cube_length": len(cube),
        "source_cube_cn": exact_cn(cube),
        "actual_3_completion": {
            "word": "".join(map(str, actual)),
            "cn": exact_cn(actual),
            "tail": exact_tail(actual),
        },
        "wrong_2_completion": {
            "word": "".join(map(str, wrong)),
            "cn": exact_cn(wrong),
            "tail": exact_tail(wrong),
        },
        "wrong_completion_maximizing_roots": tuple(
            {
                "length": length,
                "root": "".join(map(str, candidate)),
                "start": start,
            }
            for length, candidate, start in roots
        ),
        "parent_endpoint": parent_endpoint,
        "short_root_cut": {
            "tails": (exact_tail(short_actual), exact_tail(short_wrong)),
            "endpoint": short_root_endpoint,
            "delta": short_root_endpoint - parent_endpoint,
        },
        "ambient_root_cut": {
            "tails": (exact_tail(ambient_actual), exact_tail(ambient_wrong)),
            "endpoint": ambient_endpoint,
            "delta": ambient_endpoint - parent_endpoint,
        },
    }


def reverse_actual_completion_whole_power() -> dict[str, object]:
    """The reverse actual completion may already be the whole crossing power."""

    source_root = (2, 3)
    cube = source_root * 3
    deleted = cube[1:]
    actual = deleted + (2,)
    wrong = deleted + (3,)

    assert exact_cn(cube) == 3
    assert exact_cn(deleted) == 2
    assert exact_cn(actual) == 3
    assert exact_cn(wrong) == 2
    assert exact_tail(actual) == 3
    assert exact_tail(wrong) == 1

    roots = maximizing_roots(actual)
    assert roots == ((2, (3, 2), 0),)
    parent_endpoint = len(wrong) + exact_tail(wrong)
    assert parent_endpoint == 7

    return {
        "source_cube": "".join(map(str, cube)),
        "deleted_base": "".join(map(str, deleted)),
        "deleted_base_cn": exact_cn(deleted),
        "actual_2_completion": {
            "word": "".join(map(str, actual)),
            "cn": exact_cn(actual),
            "tail": exact_tail(actual),
        },
        "wrong_3_completion": {
            "word": "".join(map(str, wrong)),
            "cn": exact_cn(wrong),
            "tail": exact_tail(wrong),
        },
        "unique_maximizing_root": {
            "length": roots[0][0],
            "root": "".join(map(str, roots[0][1])),
            "start": roots[0][2],
        },
        "endpoint_before_and_after_whole_power_cut": (parent_endpoint,) * 2,
    }


def main() -> None:
    print(
        {
            "conserved_rank_orientation_switch": (
                conserved_rank_orientation_switch()
            ),
            "pure_cube_actual_completion_rank_increase": (
                pure_cube_actual_completion_rank_increase()
            ),
            "reverse_actual_completion_whole_power": (
                reverse_actual_completion_whole_power()
            ),
        }
    )


if __name__ == "__main__":
    main()
