"""Audit timing obstructions in the O/C/R typed endpoint-rank graph.

Run the A094004 calibration first.  This checker does not search for a bad
word.  It recomputes finite terminal near-models showing that the terminal
tail differences left free by the symbolic O/C/R transitions can attain
the zero and positive values that defeat a rank made only from the base
endpoint plus a constant type offset.
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


def completion_zero_self_loop() -> dict[str, object]:
    common = tuple(map(int, "22232223222322"))
    child_common = common[1:]

    parent_bad_candidate = common + (3,)
    parent_terminal = common + (2,)
    child_bad_candidate = child_common + (3,)
    child_terminal = child_common + (2,)

    tails = {
        "parent_bad_candidate": exact_tail(parent_bad_candidate),
        "parent_terminal": exact_tail(parent_terminal),
        "child_bad_candidate": exact_tail(child_bad_candidate),
        "child_terminal": exact_tail(child_terminal),
    }
    assert tails == {
        "parent_bad_candidate": 52,
        "parent_terminal": 2,
        "child_bad_candidate": 52,
        "child_terminal": 3,
    }

    parent_endpoint = len(parent_terminal) + tails["parent_terminal"]
    child_endpoint = len(child_terminal) + tails["child_terminal"]
    assert parent_endpoint == child_endpoint == 17
    return {
        "common_prefix": "".join(map(str, common)),
        "tails": tails,
        "parent_terminal_endpoint": parent_endpoint,
        "child_terminal_endpoint": child_endpoint,
        "typed_delta_if_bad_sides_were_nonterminating": 0,
    }


def reverse_reset_timing() -> tuple[dict[str, object], ...]:
    records: list[dict[str, object]] = []
    for root in ((3,), (2, 3, 2, 2), (2, 2, 3, 2)):
        high = root * 3
        deleted = high[1:]
        terminal_completion = deleted + (3,)
        assert exact_cn(high) == 3
        assert exact_cn(deleted) == 2
        high_tail = exact_tail(high)
        completion_tail = exact_tail(terminal_completion)
        records.append(
            {
                "root": root,
                "tau_high": high_tail,
                "tau_terminal_completion": completion_tail,
                "R_to_C_base_delta": completion_tail - high_tail,
            }
        )
    assert tuple(record["R_to_C_base_delta"] for record in records) == (
        0,
        1,
        9,
    )
    return tuple(records)


def q21_sibling_spread() -> dict[str, object]:
    profile = tuple(map(int, "223222322232322232223"))
    records: list[tuple[int, int, int, int]] = []
    for phase, label in enumerate(profile):
        if label != 2:
            continue
        root = profile[phase:] + profile[:phase]
        deleted = (root * 3)[1:]
        wrong = deleted + (3,)
        actual = deleted + (2,)
        wrong_tail = exact_tail(wrong)
        actual_tail = exact_tail(actual)
        records.append(
            (phase, wrong_tail, actual_tail, wrong_tail - actual_tail)
        )
    assert min(record[3] for record in records) == -59
    assert max(record[3] for record in records) == 52
    return {
        "ordered_as_phase_tau_D3_tau_D2_difference": tuple(records),
        "minimum_difference": -59,
        "maximum_difference": 52,
    }


def offset_obstruction() -> dict[str, str]:
    # A strict C -> R edge of base delta zero requires
    #     w_R <= w_C - 1.
    # A strict R -> C edge of base delta zero requires
    #     w_C <= w_R - 1.
    # Adding them gives 0 <= -2.
    return {
        "C_to_R_zero_constraint": "w_R <= w_C - 1",
        "R_to_C_zero_constraint": "w_C <= w_R - 1",
        "sum": "0 <= -2 (impossible)",
    }


def main() -> None:
    print(
        {
            "relaxed_C_zero_self_loop": completion_zero_self_loop(),
            "reverse_reset_timing": reverse_reset_timing(),
            "Q21_wrong_vs_actual_sibling_spread": q21_sibling_spread(),
            "constant_type_offset_obstruction": offset_obstruction(),
        }
    )


if __name__ == "__main__":
    main()
