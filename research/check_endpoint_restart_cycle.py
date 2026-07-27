"""Executed finite model for the endpoint-rank restart-cycle obstruction.

Run the A094004 calibration before accepting this output:

    python -m unittest \
      tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration

The model satisfies every finite curling-number, first-disagreement, and
endpoint-rank equation used by the restart transition.  Its high words
terminate, so it is not a counterexample to the Curling Number Conjecture.
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


def main() -> None:
    reset = tuple(map(int, "323232"))
    deleted = reset[1:]
    exponent = exact_cn(reset)
    driven = deleted + (exponent,)

    boundary_depth = 1
    moved = driven[boundary_depth:]
    moved_deleted = moved[1:]
    common_output = (2,)
    promoted = moved + common_output
    promoted_deleted = moved_deleted + common_output

    assert exponent == 3
    assert exact_cn(deleted) == 2
    assert exact_cn(driven) == 3
    assert exact_cn(moved) == exact_cn(moved_deleted) == 2
    assert promoted == reset
    assert promoted_deleted == deleted
    assert exact_cn(promoted) == 3
    assert exact_cn(promoted_deleted) == 2

    reset_rank = len(reset) + tail_length(deleted, step_limit=1000)
    moved_rank = len(moved) + tail_length(
        moved_deleted, step_limit=1000
    )
    assert tail_length(deleted, step_limit=1000) == 3
    assert tail_length(moved_deleted, step_limit=1000) == 4
    assert reset_rank == moved_rank == 9

    # The formal restart deletes ``32`` and appends ``32``.  If those
    # separately restarted outputs are retained instead, the context makes
    # the next curling number larger immediately.
    output_block = (exponent,) + common_output
    assert output_block == tuple(map(int, "32"))
    ancestor_after_first_output = reset + (exponent,)
    assert exact_cn(ancestor_after_first_output) == 3
    assert exact_cn(moved) == 2

    for cycle_count in range(0, 101):
        accumulated = reset + output_block * cycle_count
        assert exact_cn(accumulated) == 3 + cycle_count
        if cycle_count >= 1:
            assert tail_length(accumulated, step_limit=1000) == 1

    one_cycle_tape = reset + output_block
    assert tail_length(one_cycle_tape, step_limit=1000) == 1
    assert tail_length(one_cycle_tape[1:], step_limit=1000) == 2
    assert one_cycle_tape[-len(reset) :] == reset
    assert tail_length(reset, step_limit=1000) == 3

    print(
        "restart_cycle_model",
        "reset=323232",
        "deleted=23232",
        "driven=232323",
        "moved=32323",
        "common_output=2",
        "endpoint_rank=9",
    )
    print(
        "context_amplification",
        "cn(3232323)=3",
        "cn(32323)=2",
        "cn(323232(32)^q)=3+q checked for q=0..100",
        "tau=1 checked for q=1..100",
    )
    print(
        "suffix_tau_nonmonotonicity",
        "tau(32323232)=1",
        "tau(2323232)=2",
        "tau(323232)=3",
    )
    print("A094004 calibration: run separately before accepting this output")


if __name__ == "__main__":
    main()
