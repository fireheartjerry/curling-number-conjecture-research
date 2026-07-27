"""Executed checks for ``moving_boundary_context_loss.md``.

The A094004 calibration is deliberately kept in the test suite because its
length-22 exhaustive enumeration is expensive.  Run

    python -m unittest \
      tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration

before using this script's output.
"""

from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference, tail_length


Word = tuple[int, ...]


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def nontrivial_whole_power(word: Word) -> bool:
    n = len(word)
    return any(
        n % root_length == 0
        and n // root_length >= 2
        and word == word[:root_length] * (n // root_length)
        for root_length in range(1, n)
    )


def main() -> None:
    root = tuple(map(int, "2322232"))
    exponent = 3
    reset = root * exponent
    deleted = reset[1:]
    driven = deleted + (exponent,)
    high_successor = reset + (exponent,)

    words = {
        "A": reset,
        "D": deleted,
        "E": driven,
        "E.tail": driven[1:],
        "A3": high_successor,
    }
    expected = {
        "A": (21, 3, 60),
        "D": (20, 2, 4),
        "E": (21, 2, 59),
        "E.tail": (20, 2, 59),
        "A3": (22, 2, 59),
    }

    for name, word in words.items():
        observed = (
            len(word),
            exact_cn(word),
            tail_length(word, step_limit=1000),
        )
        assert observed == expected[name], (name, observed, expected[name])
        print(
            name,
            f"length={observed[0]}",
            f"cn={observed[1]}",
            f"tau={observed[2]}",
        )

    assert exact_cn(driven) == exact_cn(high_successor)
    assert not nontrivial_whole_power(high_successor)

    old_sum = len(reset) - 1 + tail_length(deleted, step_limit=1000)
    shifted_sum = (
        len(driven) - 1 + tail_length(driven[1:], step_limit=1000)
    )
    assert (old_sum, shifted_sum) == (24, 79)
    print(
        "essential_endpoint_rank",
        f"old={old_sum}",
        f"shifted={shifted_sum}",
    )

    # A complete finite promotion which returns to the same deleted hitting
    # time while increasing the primitive reset-root length from 4 to 21.
    old_root = tuple(map(int, "2322"))
    old_exponent = 3
    old_reset = old_root * old_exponent
    old_deleted = old_reset[1:]
    wrong_deleted = old_deleted + (old_exponent,)
    moved = wrong_deleted[1:]
    moved_deleted = moved[1:]

    promotion_expected = {
        "old_reset": (old_reset, 12, 3, 53),
        "old_deleted": (old_deleted, 11, 2, 4),
        "wrong_deleted": (wrong_deleted, 12, 2, 54),
        "moved": (moved, 11, 2, 54),
        "moved_deleted": (moved_deleted, 10, 2, 56),
    }
    for name, (word, length, value, tail) in promotion_expected.items():
        observed = (
            len(word),
            exact_cn(word),
            tail_length(word, step_limit=1000),
        )
        assert observed == (length, value, tail), (
            name,
            observed,
            (length, value, tail),
        )

    high = moved
    low = moved_deleted
    common_outputs: list[int] = []
    while True:
        high_value = exact_cn(high)
        low_value = exact_cn(low)
        if high_value != low_value:
            break
        assert high_value != 1
        common_outputs.append(high_value)
        high += (high_value,)
        low += (low_value,)

    assert len(common_outputs) == 52
    assert (high_value, low_value) == (3, 2)
    assert len(high) == 63
    promoted_root = high[:21]
    assert high == promoted_root * 3
    assert tail_length(low, step_limit=1000) == 4
    assert tail_length(high, step_limit=1000) == 2
    assert "".join(map(str, promoted_root)) == "222322232232223222323"
    print(
        "promotion_countermodel",
        "old_root_length=4",
        "boundary_move=1",
        "moved_deleted_tau=56",
        "common_steps=52",
        "residual_deleted_tau=4",
        "new_root_length=21",
    )

    carrier_root = tuple(map(int, "232223"))
    carrier_cut = 2
    carrier_high = carrier_root + carrier_root[:carrier_cut]
    carrier_low = carrier_high[1:]
    assert exact_cn(carrier_root) == 1
    assert exact_cn((carrier_root * 2)[1:]) == 1
    assert tail_length(carrier_high, step_limit=1000) == 58
    assert tail_length(carrier_low, step_limit=1000) == 4
    for phase in range(carrier_cut, len(carrier_root)):
        expected_value = carrier_root[phase]
        high_phase = carrier_root + carrier_root[:phase]
        low_phase = carrier_root[1:] + carrier_root[:phase]
        assert exact_cn(high_phase) == expected_value
        assert exact_cn(low_phase) == expected_value
    assert exact_cn(carrier_root * 2) == 2
    assert exact_cn((carrier_root * 2)[1:]) == 1
    print(
        "terminal_hidden_full_profile",
        "root=232223",
        "h=2",
        "generated=2223",
        "high_tau=58",
        "low_tau=4",
    )

    for run_length in range(0, 101):
        family_root = (2,) * run_length + (3, 3, 2)
        family_high = family_root + family_root[:-1]
        family_low = family_high[1:]
        observed = (
            exact_cn(family_root),
            exact_cn((family_root * 2)[1:]),
            exact_cn(family_high),
            exact_cn(family_low),
            exact_cn(family_root * 2),
        )
        assert observed == (1, 1, 2, 2, 2), (run_length, observed)
    print("bounded_defect_family_checked", "run_length=0..100", "delta=1")
    print("A094004 calibration: run separately before accepting this output")


if __name__ == "__main__":
    main()
