import json
from dataclasses import FrozenInstanceError, replace
from itertools import product

import pytest

from curling import curling_number, curling_number_reference
from research import generated_two_cube_falsifier as falsifier
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


def test_extract_record_square_candidates_counts_rebased_cube_in_record_accounting():
    original_seed = tuple(map(int, "22323222322"))
    original_events, _ = trace_orbit(original_seed, 500)
    original_cube = original_events[52]
    cube_seed = original_cube.word
    events, _ = trace_orbit(cube_seed, 500)
    prior_cube = events[0]
    terminal = events[16]
    G = events[terminal.time - terminal.period]
    R = G.word[-G.period :]
    b = terminal.period - G.period
    B = R[-b:]
    Y = B + R
    prior_square_periods = [
        event.period for event in events[: terminal.time] if event.exponent == 2
    ]

    assert (original_cube.exponent, original_cube.period) == (3, 21)
    assert prior_cube.word == cube_seed
    assert (prior_cube.exponent, prior_cube.period) == (3, 21)
    assert (terminal.exponent, terminal.period) == (2, 7)
    assert prior_cube.time < terminal.time
    assert prior_cube.period >= terminal.period
    assert max(prior_square_periods) == 6
    assert terminal.period > max(prior_square_periods)
    assert terminal.entire_power_generated()
    assert (G.exponent, G.period) == (2, 4)
    assert b > 0
    assert 2 * G.period - terminal.period > 0
    assert terminal.word == G.word + Y
    assert terminal.word[-2 * terminal.period :] == Y + Y
    assert all(
        candidate.terminal_time != terminal.time
        for candidate in extract_record_square_candidates(events)
    )


def test_extract_record_square_candidates_rejects_deleted_prior_record_event():
    seed = tuple(map(int, "22322232"))
    events, _ = trace_orbit(seed, 500)
    prior_record = events[20]
    terminal = events[41]
    G = events[terminal.time - terminal.period]
    R = G.word[-G.period :]
    b = terminal.period - G.period
    B = R[-b:]
    Y = B + R

    assert (prior_record.exponent, prior_record.period) == (2, 7)
    assert (terminal.exponent, terminal.period) == (2, 7)
    assert terminal.entire_power_generated()
    assert (G.exponent, G.period) == (2, 4)
    assert b > 0
    assert 2 * G.period - terminal.period > 0
    assert terminal.word == G.word + Y
    assert terminal.word[-2 * terminal.period :] == Y + Y
    assert [
        candidate.terminal_time
        for candidate in extract_record_square_candidates(events)
    ] == [prior_record.time]

    # Deleting t20 used to manufacture t41 as a "strict" record because the
    # local-span checks never noticed the globally incomplete orbit prefix.
    incomplete = events[:20] + events[21:]
    assert extract_record_square_candidates(incomplete) == ()


def test_extract_record_square_candidates_rejects_trace_missing_time_zero():
    seed = tuple(map(int, "23222323"))
    events, _ = trace_orbit(seed, 1000)

    assert extract_record_square_candidates(events[1:16]) == ()


def test_extract_record_square_candidates_rejects_reordered_terminal():
    seed = tuple(map(int, "23222323"))
    events, _ = trace_orbit(seed, 1000)
    terminal_first = (events[15], *events[:15], *events[16:])

    assert extract_record_square_candidates(terminal_first) == ()


def test_extract_record_square_candidates_rejects_duplicate_after_candidate():
    seed = tuple(map(int, "23222323"))
    events, _ = trace_orbit(seed, 1000)
    duplicate_after_terminal = (*events[:17], events[16])

    assert extract_record_square_candidates(duplicate_after_terminal) == ()


def test_extract_record_square_candidates_rejects_foreign_event_after_candidate():
    seed = tuple(map(int, "23222323"))
    events, _ = trace_orbit(seed, 1000)
    foreign_seed = tuple(map(int, "22322232"))
    foreign_events, _ = trace_orbit(foreign_seed, 500)
    mixed_trace = (*events[:16], foreign_events[16])

    assert foreign_events[16].time == 16
    assert foreign_events[16].seed_length == len(seed)
    assert foreign_events[16].word[: len(seed)] != seed
    assert extract_record_square_candidates(mixed_trace) == ()


def test_extract_record_square_candidates_rejects_event_after_one():
    seed = tuple(map(int, "23222323"))
    events, _ = trace_orbit(seed, 1000)
    hit_one = events[-1]
    continued_word = hit_one.word + (hit_one.exponent,)
    exponent, period = canonical_witness(continued_word)
    continued = OrbitEvent(
        time=hit_one.time + 1,
        word=continued_word,
        exponent=exponent,
        period=period,
        seed_length=hit_one.seed_length,
    )

    assert hit_one.exponent == 1
    assert continued.time == len(events)
    assert len(continued.word) == continued.seed_length + continued.time
    assert continued.word[: continued.seed_length] == seed
    assert canonical_witness(continued.word) == (
        continued.exponent,
        continued.period,
    )
    assert hit_one.word + (hit_one.exponent,) == continued.word
    assert extract_record_square_candidates((*events, continued)) == ()


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


@pytest.mark.parametrize(
    ("cube_start", "ybt_start", "r", "q", "P", "expected"),
    [
        (10, 10, 4, 4, 7, "C"),
        (11, 10, 4, 4, 7, "C"),
        (9, 10, 4, 4, 7, "A"),
        (9, 10, 5, 4, 7, "B"),
        (9, 10, 3, 4, 7, "unclassified"),
    ],
)
def test_classify_first_failure_cell_uses_half_open_geometry(
    cube_start, ybt_start, r, q, P, expected
):
    assert (
        falsifier.classify_first_failure_cell(
            cube_start=cube_start,
            ybt_start=ybt_start,
            r=r,
            q=q,
            P=P,
        )
        == expected
    )


@pytest.mark.parametrize(
    ("cube_start", "ybt_start"),
    [
        (-1, 0),
        (0, -1),
    ],
)
def test_classify_first_failure_cell_rejects_negative_coordinates(
    cube_start, ybt_start
):
    with pytest.raises(
        ValueError,
        match="^cube_start and ybt_start must be nonnegative$",
    ):
        falsifier.classify_first_failure_cell(
            cube_start=cube_start,
            ybt_start=ybt_start,
            r=1,
            q=1,
            P=2,
        )


@pytest.mark.parametrize(
    ("q", "P"),
    [
        (0, 2),
        (2, 2),
        (3, 2),
    ],
)
def test_classify_first_failure_cell_requires_strict_bridge_period_domain(q, P):
    with pytest.raises(ValueError, match=r"^requires 0 < q < P$"):
        falsifier.classify_first_failure_cell(
            cube_start=0,
            ybt_start=1,
            r=1,
            q=q,
            P=P,
        )


@pytest.mark.parametrize("r", [0, 2, 3])
def test_classify_first_failure_cell_rejects_r_outside_terminal_period(r):
    with pytest.raises(ValueError, match=r"^requires 0 < r < P$"):
        falsifier.classify_first_failure_cell(
            cube_start=0,
            ybt_start=1,
            r=r,
            q=1,
            P=2,
        )


def test_check_standalone_promotion_rejects_empty_root():
    with pytest.raises(
        ValueError,
        match="^check_standalone_promotion requires a nonempty root$",
    ):
        falsifier.check_standalone_promotion(())


def test_audit_reviewed_candidate_verifies_promotion_and_exact_paired_windows():
    seed = tuple(map(int, "23222323"))
    events, _ = trace_orbit(seed, 1000)
    candidates = extract_record_square_candidates(events)

    assert len(candidates) == 1
    candidate = candidates[0]
    audit = falsifier.audit_record_square_candidate(events, candidate)

    assert audit.status == "promotion_root"
    assert audit.candidate == candidate
    assert audit.invalid_reason is None
    assert audit.first_failure is None
    assert len(audit.standalone_checks) == candidate.q
    assert len(audit.paired_windows) == candidate.q

    for check, expected in zip(audit.standalone_checks, candidate.R):
        j = check.j
        assert check.expected == expected == candidate.R[j]
        assert check.word == candidate.R + candidate.R + candidate.R[:j]
        assert (check.exponent, check.period) == canonical_witness(check.word)
        assert check.exponent == expected

    for window in audit.paired_windows:
        j = window.j
        T = candidate.R[:j]
        U = candidate.R[j:]
        m = candidate.q - j
        expected_e_times = tuple(
            candidate.second_r_start_time + j + ell for ell in range(m + 1)
        )
        expected_f_times = tuple(
            candidate.g_time + candidate.b + j + ell for ell in range(m + 1)
        )

        assert window.T == T
        assert window.U == U
        assert tuple(event.time for event in window.E_events) == expected_e_times
        assert tuple(event.time for event in window.F_events) == expected_f_times
        assert tuple(event.word for event in window.E_events) == tuple(
            candidate.L + candidate.R + T + U[:ell] for ell in range(m + 1)
        )
        assert tuple(event.word for event in window.F_events) == tuple(
            candidate.L
            + candidate.R
            + candidate.R
            + candidate.B
            + T
            + U[:ell]
            for ell in range(m + 1)
        )
        assert tuple(event.exponent for event in window.E_events[:-1]) == U
        assert tuple(event.exponent for event in window.F_events[:-1]) == U
        assert window.E_events[-1] == events[candidate.g_time]
        assert window.F_events[-1] == events[candidate.terminal_time]
        assert window.I_events == window.E_events + window.F_events[:-1]
        assert events[candidate.g_time] in window.I_events
        assert events[candidate.terminal_time] not in window.I_events
        assert window.max_period_over_I == max(
            events[time].period
            for time in (*expected_e_times, *expected_f_times[:-1])
        )


def test_standalone_promotion_check_reports_the_least_direct_failure():
    R = tuple(map(int, "233323"))

    promotion = falsifier.check_standalone_promotion(R)

    assert promotion.status == "first_failure"
    assert promotion.first_failure_j == 1
    assert tuple(check.expected for check in promotion.checks) == R
    assert tuple(check.exponent for check in promotion.checks) == (2, 2, 2, 2, 3, 2)
    assert promotion.checks[1].word == R + R + R[:1]
    assert (
        promotion.checks[1].exponent,
        promotion.checks[1].period,
    ) == canonical_witness(promotion.checks[1].word)


def test_audit_rejects_mutated_candidate_not_reextracted_from_trace():
    seed = tuple(map(int, "23222323"))
    events, _ = trace_orbit(seed, 1000)
    candidate = extract_record_square_candidates(events)[0]
    mutated = replace(candidate, P=candidate.P + 1)

    audit = falsifier.audit_record_square_candidate(events, mutated)

    assert audit.status == "invalid_provenance"
    assert audit.candidate is None
    assert audit.invalid_reason == "missing_bridge_hypothesis"
    assert audit.first_failure is None


def test_first_failure_report_preserves_noncube_anomaly_as_unclassified(
    monkeypatch,
):
    seed = tuple(map(int, "23222323"))
    events, _ = trace_orbit(seed, 1000)
    candidate = extract_record_square_candidates(events)[0]
    natural = falsifier.check_standalone_promotion(candidate.R)
    forced_checks = (
        replace(natural.checks[0], exponent=3, period=1),
        *natural.checks[1:],
    )
    forced = falsifier.StandalonePromotionAudit(
        status="first_failure",
        checks=forced_checks,
        first_failure_j=0,
    )
    monkeypatch.setattr(
        falsifier,
        "check_standalone_promotion",
        lambda R: forced,
    )

    audit = falsifier.audit_record_square_candidate(events, candidate)

    assert audit.status == "first_failure"
    report = audit.first_failure
    assert report is not None
    assert report.seed == seed
    assert report.seed_length == len(seed)
    assert report.j == 0
    assert report.expected == 2
    assert (report.standalone_exponent, report.standalone_period) == (3, 1)
    assert (report.E_exponent, report.E_period) == (2, 6)
    assert (report.F_exponent, report.F_period) == (2, 3)
    assert (report.G_exponent, report.G_period) == (2, candidate.q)
    assert report.cube_start is None
    assert report.cell == "unclassified"
    assert not report.g2cs_antecedent
    assert not report.g2cs_counterexample
    assert events[candidate.g_time] in report.I_events
    assert events[candidate.terminal_time] not in report.I_events
    assert report.max_period_over_I == max(
        event.period for event in report.I_events
    )
    serialized = json.loads(falsifier.serialize_first_failure(report))
    assert serialized["seed_length"] == len(seed)
    assert serialized["cube_start"] is None
    assert serialized["cell"] == "unclassified"


def test_exponent_four_mismatch_is_outside_g2cs_cells_and_counts(monkeypatch):
    seed = tuple(map(int, "23222323"))
    events, _ = trace_orbit(seed, 1000)
    candidate = extract_record_square_candidates(events)[0]
    natural_checker = falsifier.check_standalone_promotion

    def force_exponent_four(R):
        natural = natural_checker(R)
        assert natural.checks[3].expected == 3
        assert natural.checks[3].exponent == 3
        return falsifier.StandalonePromotionAudit(
            status="first_failure",
            checks=(
                *natural.checks[:3],
                replace(natural.checks[3], exponent=4, period=1),
            ),
            first_failure_j=3,
        )

    monkeypatch.setattr(
        falsifier,
        "check_standalone_promotion",
        force_exponent_four,
    )

    audit = falsifier.audit_record_square_candidate(events, candidate)

    assert audit.status == "first_failure"
    report = audit.first_failure
    assert report is not None
    assert report.expected == 3
    assert report.standalone_exponent == 4
    assert (report.E_exponent, report.F_exponent) == (3, 3)
    assert not report.g2cs_antecedent
    assert report.cube_start is None
    assert report.cell == "unclassified"

    summary = falsifier.scan_binary_seeds(max_seed_length=8, step_limit=100)
    assert summary.first_failures == 2
    assert summary.g2cs_antecedents == 0
    assert summary.g2cs_verified == 0
    assert summary.g2cs_counterexamples == 0
    assert (summary.cell_A, summary.cell_B, summary.cell_C) == (0, 0, 0)
    assert summary.unclassified == summary.first_failures


def test_exponent_two_mismatch_counts_positive_g2cs_cell_c(monkeypatch):
    seed = tuple(map(int, "23222323"))
    events, _ = trace_orbit(seed, 1000)
    candidate = extract_record_square_candidates(events)[0]
    natural_checker = falsifier.check_standalone_promotion

    def force_exponent_two(R):
        natural = natural_checker(R)
        assert natural.checks[3].expected == 3
        assert natural.checks[3].exponent == 3
        return falsifier.StandalonePromotionAudit(
            status="first_failure",
            checks=(
                *natural.checks[:3],
                replace(natural.checks[3], exponent=2, period=1),
            ),
            first_failure_j=3,
        )

    monkeypatch.setattr(
        falsifier,
        "check_standalone_promotion",
        force_exponent_two,
    )

    audit = falsifier.audit_record_square_candidate(events, candidate)

    assert audit.status == "first_failure"
    report = audit.first_failure
    assert report is not None
    assert report.g2cs_antecedent
    assert report.g2cs_counterexample
    assert report.cube_start == len(report.F_event.word) - 3 * report.r == 19
    assert report.cell == "C"

    summary = falsifier.scan_binary_seeds(max_seed_length=8, step_limit=100)
    assert summary.candidates == 2
    assert summary.promotion_roots == 0
    assert summary.first_failures == 2
    assert summary.g2cs_antecedents == 2
    assert summary.g2cs_counterexamples == 2
    assert summary.g2cs_verified == 0
    assert (summary.cell_A, summary.cell_B, summary.cell_C) == (0, 0, 2)
    assert summary.unclassified == 0


def test_missing_strict_record_bridge_impostor_is_rejected_despite_generating_R():
    D = tuple(map(int, "223222"))
    R = tuple(map(int, "322232"))
    events, _ = trace_orbit(D + R, len(R))
    B = R[-1:]
    impostor = RecordSquareCandidate(
        seed=D + R,
        L=D,
        A=R[:-1],
        B=B,
        R=R,
        Y=B + R,
        P=len(R) + len(B),
        q=len(R),
        b=len(B),
        second_r_start_time=0,
        g_time=len(R),
        terminal_time=2 * len(R) + len(B),
    )

    assert tuple(event.exponent for event in events[:-1]) == R
    assert events[-1].word == D + R + R
    assert extract_record_square_candidates(events) == ()

    audit = falsifier.audit_record_square_candidate(events, impostor)
    assert audit.status == "invalid_provenance"
    assert audit.invalid_reason == "missing_bridge_hypothesis"


def test_static_paired_generation_impostor_records_desired_versus_actual():
    L = tuple(map(int, "23332322333232"))
    R = tuple(map(int, "233323"))
    B = tuple(map(int, "23"))
    j = 1
    events, _ = trace_orbit(L + R, len(R))
    actual = tuple(event.exponent for event in events[:-1])

    assert B == R[-len(B) :]
    assert R[:j] == (2,)
    assert R == tuple(map(int, "233323"))
    assert actual == tuple(map(int, "232332"))
    assert actual != R
    with pytest.raises(ValueError, match=r"^expected 3 but generated 2$"):
        generated_states(L + R, R)
    assert extract_record_square_candidates(events) == ()


def test_bounded_scan_counts_every_binary_seed_and_no_hidden_termination():
    summary = falsifier.scan_binary_seeds(max_seed_length=3, step_limit=0)

    assert summary.max_seed_length == 3
    assert summary.step_limit == 0
    assert summary.seeds == sum(2**length for length in range(1, 4))
    assert summary.hit_one + summary.capped == summary.seeds
    assert summary.candidates == summary.promotion_roots + summary.first_failures
    assert (
        summary.cell_A
        + summary.cell_B
        + summary.cell_C
        + summary.unclassified
        == summary.first_failures
    )
    assert summary.g2cs_antecedents <= summary.first_failures
    assert summary.g2cs_counterexamples <= summary.g2cs_antecedents
    assert (
        summary.g2cs_verified
        == summary.g2cs_antecedents - summary.g2cs_counterexamples
    )

    with pytest.raises(FrozenInstanceError):
        summary.seeds = 0


def test_bounded_scan_audits_real_extracted_candidates():
    summary = falsifier.scan_binary_seeds(max_seed_length=8, step_limit=100)

    assert summary.seeds == 510
    assert summary.candidates == 2
    assert summary.candidates == summary.promotion_roots + summary.first_failures
    assert summary.promotion_roots == 2
    assert summary.first_failures == 0
    assert summary.first_failure_reports == ()


def test_bounded_scan_extracts_candidates_once_per_orbit(monkeypatch):
    extraction_calls = 0
    real_extract = falsifier.extract_record_square_candidates

    def counting_extract(events):
        nonlocal extraction_calls
        extraction_calls += 1
        return real_extract(events)

    monkeypatch.setattr(
        falsifier,
        "extract_record_square_candidates",
        counting_extract,
    )

    summary = falsifier.scan_binary_seeds(max_seed_length=8, step_limit=100)

    assert summary.candidates == 2
    assert extraction_calls == summary.seeds == 510


def test_cli_prints_calibration_parameters_counts_and_no_proof_warning(capsys):
    exit_code = falsifier.main(
        ["--max-seed-length", "3", "--step-limit", "5"]
    )

    output = capsys.readouterr().out
    assert exit_code == 0
    assert "calibration_terminal_lengths=5,66,142 status=PASS" in output
    assert "max_seed_length=3" in output
    assert "step_limit=5" in output
    assert "fully_generated_specialization" in output
    assert "seeds=14" in output
    assert "hit_one=" in output
    assert "capped=" in output
    assert "candidates=" in output
    assert "promotion_roots=" in output
    assert "first_failures=" in output
    assert "g2cs_antecedents=" in output
    assert "g2cs_verified=" in output
    assert "g2cs_counterexamples=" in output
    assert "cell_A=" in output
    assert "cell_B=" in output
    assert "cell_C=" in output
    assert "unclassified=" in output
    assert "NOT_A_PROOF" in output
