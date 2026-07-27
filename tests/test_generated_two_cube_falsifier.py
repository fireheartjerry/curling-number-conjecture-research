from dataclasses import FrozenInstanceError
from itertools import product

import pytest

from curling import curling_number, curling_number_reference
from research.generated_two_cube_falsifier import (
    OrbitEvent,
    RecordSquareCandidate,
    canonical_witness,
    extract_record_square_candidates,
    generated_states,
    synchronization_evaluation_states,
    trace_orbit,
)


def test_canonical_witness_checks_every_block_length():
    assert canonical_witness((2, 3, 2, 3, 2)) == (2, 2)


def test_canonical_witness_uses_shortest_maximizing_period():
    assert canonical_witness((2, 2, 2, 2)) == (4, 1)


def test_canonical_witness_uses_whole_word_sentinel_for_exponent_one():
    assert canonical_witness((2, 3)) == (1, 2)


def test_canonical_witness_rejects_empty_word():
    with pytest.raises(
        ValueError, match="^canonical_witness requires a nonempty word$"
    ):
        canonical_witness(())


def test_canonical_witness_matches_reference_implementations_on_small_ternary_words():
    for length in range(1, 9):
        for word in product((-1, 0, 1), repeat=length):
            exponent, period = canonical_witness(word)
            assert exponent == curling_number(word)
            assert exponent == curling_number_reference(word)
            if exponent == 1:
                assert period == len(word)
                continue

            periods = []
            for candidate in range(1, len(word) // exponent + 1):
                block = word[-candidate:]
                if block * exponent == word[-candidate * exponent :]:
                    periods.append(candidate)
            assert period == min(periods)


def test_orbit_event_distinguishes_final_copy_from_entire_generated_power():
    event = OrbitEvent(
        time=0,
        word=(2, 3, 2, 3, 2, 3),
        exponent=2,
        period=2,
        seed_length=3,
    )

    assert event.final_copy_generated()
    assert not event.entire_power_generated()


def test_orbit_event_counts_final_copy_starting_at_seed_boundary_as_generated():
    event = OrbitEvent(
        time=2,
        word=(9, 2, 3, 2, 3),
        exponent=2,
        period=2,
        seed_length=3,
    )

    assert len(event.word) - event.period == event.seed_length
    assert event.final_copy_generated()


def test_orbit_event_rejects_final_copy_starting_before_seed_boundary():
    event = OrbitEvent(
        time=1,
        word=(2, 3, 2, 3),
        exponent=2,
        period=2,
        seed_length=3,
    )

    assert len(event.word) - event.period == event.seed_length - 1
    assert not event.final_copy_generated()


def test_orbit_event_counts_power_starting_at_seed_boundary_as_entirely_generated():
    event = OrbitEvent(
        time=0,
        word=(2, 3, 2, 3, 2, 3, 2),
        exponent=2,
        period=2,
        seed_length=3,
    )

    assert event.entire_power_generated()


def test_orbit_event_fields_are_immutable():
    event = OrbitEvent(
        time=0,
        word=(2, 2),
        exponent=2,
        period=1,
        seed_length=2,
    )

    with pytest.raises(FrozenInstanceError):
        event.time = 1


def test_trace_orbit_rejects_empty_seed():
    with pytest.raises(ValueError, match="^trace_orbit requires a nonempty seed$"):
        trace_orbit((), 0)


def test_trace_orbit_rejects_negative_step_limit():
    with pytest.raises(ValueError, match="^step_limit must be nonnegative$"):
        trace_orbit((2, 2), -1)


def test_trace_orbit_zero_cap_keeps_seed_evaluation_and_reports_cutoff():
    events, termination = trace_orbit((2, 2), 0)

    assert [(event.time, event.word, event.exponent, event.period) for event in events] == [
        (0, (2, 2), 2, 1)
    ]
    assert termination == "step_limit"


def test_trace_orbit_one_step_cap_keeps_state_after_exactly_one_append():
    events, termination = trace_orbit((2, 2), 1)

    assert [(event.time, event.word, event.exponent, event.period) for event in events] == [
        (0, (2, 2), 2, 1),
        (1, (2, 2, 2), 3, 1),
    ]
    assert termination == "step_limit"


def test_trace_orbit_continues_through_exponent_four_until_one():
    events, termination = trace_orbit((2, 2, 2, 2), 1)

    assert [event.exponent for event in events] == [4, 1]
    assert termination == "hit_one"


@pytest.mark.parametrize(
    ("digits", "terminal_length"),
    [
        ("322", 5),
        ("23222323", 66),
        ("2322322323222323223223", 142),
    ],
)
def test_trace_orbit_calibration_hits_one_at_reviewed_total_length(
    digits, terminal_length
):
    seed = tuple(map(int, digits))

    events, termination = trace_orbit(seed, 1000)

    assert termination == "hit_one"
    assert len(events[-1].word) == terminal_length
    assert events[-1].exponent == 1


def test_extract_record_square_candidates_finds_reviewed_unique_candidate():
    seed = tuple(map(int, "23222323"))
    events, _ = trace_orbit(seed, 1000)

    candidates = extract_record_square_candidates(events)

    assert len(candidates) == 1
    candidate = candidates[0]
    assert candidate == RecordSquareCandidate(
        seed=seed,
        L=seed,
        A=(2,),
        B=(2, 2, 3),
        R=(2, 2, 2, 3),
        Y=(2, 2, 3, 2, 2, 2, 3),
        P=7,
        q=4,
        b=3,
        second_r_start_time=4,
        g_time=8,
        terminal_time=15,
    )
    assert candidate.R == candidate.A + candidate.B
    assert candidate.Y == candidate.B + candidate.R
    assert (
        events[candidate.g_time].word
        == candidate.L + candidate.R + candidate.R
    )
    assert (
        events[candidate.terminal_time].word
        == candidate.L
        + candidate.R
        + candidate.R
        + candidate.B
        + candidate.R
    )
    assert events[candidate.terminal_time].word[-2 * candidate.P :] == (
        candidate.Y + candidate.Y
    )
    assert (
        events[candidate.second_r_start_time].word + candidate.R
        == events[candidate.g_time].word
    )


def test_record_square_candidate_fields_are_immutable():
    seed = tuple(map(int, "23222323"))
    events, _ = trace_orbit(seed, 1000)
    candidate = extract_record_square_candidates(events)[0]

    with pytest.raises(FrozenInstanceError):
        candidate.P = 8


def test_extract_record_square_candidates_returns_empty_for_empty_events():
    assert extract_record_square_candidates(()) == ()


def test_extract_record_square_candidates_counts_every_exponent_in_record_accounting():
    seed = tuple(map(int, "23222323"))
    events, _ = trace_orbit(seed, 1000)
    cube_root = tuple(range(1, 8))
    prior_cube = OrbitEvent(
        time=-1,
        word=cube_root * 3,
        exponent=3,
        period=7,
        seed_length=len(cube_root * 3),
    )

    # This is a record-accounting unit test, not one combined orbit: the
    # unique negative timestamp leaves every real candidate span unchanged.
    assert canonical_witness(prior_cube.word) == (
        prior_cube.exponent,
        prior_cube.period,
    )
    assert all(event.time != prior_cube.time for event in events)
    assert len(extract_record_square_candidates(events)) == 1
    assert extract_record_square_candidates((prior_cube, *events)) == ()


def test_extract_record_square_candidates_rejects_empty_g_without_raising():
    seed = tuple(map(int, "23222323"))
    events, _ = trace_orbit(seed, 1000)
    malformed = list(events)
    malformed[8] = OrbitEvent(
        time=8,
        word=(),
        exponent=2,
        period=4,
        seed_length=len(seed),
    )

    assert extract_record_square_candidates(malformed) == ()


def test_extract_record_square_candidates_rejects_missing_required_span_event():
    seed = tuple(map(int, "23222323"))
    events, _ = trace_orbit(seed, 1000)
    missing_time_six = tuple(event for event in events if event.time != 6)

    assert extract_record_square_candidates(missing_time_six) == ()


def test_extract_record_square_candidates_rejects_duplicate_required_span_event():
    seed = tuple(map(int, "23222323"))
    events, _ = trace_orbit(seed, 1000)
    duplicate_time_six = (*events[:7], events[6], *events[7:])

    assert extract_record_square_candidates(duplicate_time_six) == ()


def test_extract_record_square_candidates_rejects_corrupted_interior_replay():
    seed = tuple(map(int, "23222323"))
    events, _ = trace_orbit(seed, 1000)
    candidate = extract_record_square_candidates(events)[0]
    original = events[6]
    corrupted_word = original.word[:-1] + (3,)
    corrupted_exponent, corrupted_period = canonical_witness(corrupted_word)
    corrupted_event = OrbitEvent(
        time=original.time,
        word=corrupted_word,
        exponent=corrupted_exponent,
        period=corrupted_period,
        seed_length=original.seed_length,
    )
    corrupted = list(events)
    corrupted[6] = corrupted_event

    assert len(corrupted_event.word) == len(original.word)
    assert corrupted_event.word[: len(seed)] == seed
    assert canonical_witness(corrupted_event.word) == (
        corrupted_event.exponent,
        corrupted_event.period,
    )
    assert corrupted_event.period < candidate.P
    assert corrupted[candidate.second_r_start_time] == events[
        candidate.second_r_start_time
    ]
    assert corrupted[candidate.g_time] == events[candidate.g_time]
    assert corrupted[candidate.terminal_time] == events[candidate.terminal_time]
    assert (
        corrupted[candidate.second_r_start_time].word + candidate.R
        == corrupted[candidate.g_time].word
    )
    assert (
        corrupted[candidate.g_time].word + candidate.Y
        == corrupted[candidate.terminal_time].word
    )
    assert extract_record_square_candidates(corrupted) == ()


def test_extract_record_square_candidates_requires_entire_power_to_be_generated():
    seed = tuple(map(int, "2322232322"))
    events, _ = trace_orbit(seed, 1000)
    terminal = events[13]

    assert terminal.exponent == 2
    assert terminal.period == 7
    assert terminal.final_copy_generated()
    assert not terminal.entire_power_generated()
    assert extract_record_square_candidates(events[:14]) == ()


def test_generated_states_include_start_and_terminal():
    states = generated_states((2, 2), (2,))
    assert states == ((2, 2), (2, 2, 2))


def test_generated_states_reject_wrong_requested_symbol():
    with pytest.raises(ValueError, match=r"^expected 2 but generated 1$"):
        generated_states((2, 3), (2,))


def test_generated_states_accept_empty_requested_block():
    assert generated_states((2, 3), ()) == ((2, 3),)


def test_generated_states_recomputes_witness_after_each_append():
    assert generated_states((2, 2), (2, 3)) == (
        (2, 2),
        (2, 2, 2),
        (2, 2, 2, 3),
    )


def test_generated_states_rejects_empty_start_word():
    with pytest.raises(
        ValueError, match=r"^generated_states requires a nonempty start word$"
    ):
        generated_states((), ())


def test_synchronization_evaluation_states_includes_g_and_excludes_h():
    early = ((1,), (1, 2))
    later = ((3,), (3, 2))
    assert synchronization_evaluation_states(early, later) == ((1,), (1, 2), (3,))


@pytest.mark.parametrize(
    ("early", "later", "message"),
    [
        (
            (),
            ((3,),),
            "synchronization_evaluation_states requires nonempty early_states",
        ),
        (
            ((1,),),
            (),
            "synchronization_evaluation_states requires nonempty later_states",
        ),
    ],
)
def test_synchronization_evaluation_states_rejects_empty_state_traces(
    early, later, message
):
    with pytest.raises(ValueError, match=f"^{message}$"):
        synchronization_evaluation_states(early, later)


def test_synchronization_evaluation_states_preserves_order_and_duplicate_states():
    repeated = (1,)
    early = (repeated, repeated)
    later = (repeated, repeated)
    assert synchronization_evaluation_states(early, later) == (
        repeated,
        repeated,
        repeated,
    )


def test_synchronization_evaluation_states_normalizes_mutable_inner_states():
    early = [[1], [1, 2]]
    later = [[3], [3, 2]]

    states = synchronization_evaluation_states(early, later)
    early[0].append(99)
    later[0].append(99)

    assert states == ((1,), (1, 2), (3,))
