from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from dataclasses import asdict, dataclass
from itertools import product
from typing import Literal

Word = tuple[int, ...]
TraceTermination = Literal["hit_one", "step_limit"]
FailureCell = Literal["A", "B", "C", "unclassified"]
PromotionStatus = Literal["promotion_root", "first_failure"]
CandidateAuditStatus = Literal[
    "promotion_root", "first_failure", "invalid_provenance"
]


@dataclass(frozen=True)
class OrbitEvent:
    time: int
    word: Word
    exponent: int
    period: int
    seed_length: int

    def final_copy_generated(self) -> bool:
        return len(self.word) - self.period >= self.seed_length

    def entire_power_generated(self) -> bool:
        return len(self.word) - self.exponent * self.period >= self.seed_length


@dataclass(frozen=True)
class RecordSquareCandidate:
    seed: Word
    L: Word
    A: Word
    B: Word
    R: Word
    Y: Word
    P: int
    q: int
    b: int
    second_r_start_time: int
    g_time: int
    terminal_time: int


@dataclass(frozen=True)
class StandalonePromotionCheck:
    j: int
    expected: int
    word: Word
    exponent: int
    period: int


@dataclass(frozen=True)
class StandalonePromotionAudit:
    status: PromotionStatus
    checks: tuple[StandalonePromotionCheck, ...]
    first_failure_j: int | None


@dataclass(frozen=True)
class PairedGenerationWindow:
    j: int
    T: Word
    U: Word
    E_events: tuple[OrbitEvent, ...]
    F_events: tuple[OrbitEvent, ...]
    I_events: tuple[OrbitEvent, ...]
    max_period_over_I: int


@dataclass(frozen=True)
class CandidateTraceTimes:
    second_r_start_time: int
    g_time: int
    terminal_time: int
    E_times: tuple[int, ...]
    F_times: tuple[int, ...]
    I_times: tuple[int, ...]


@dataclass(frozen=True)
class FirstFailureReport:
    seed: Word
    seed_length: int
    P: int
    q: int
    b: int
    j: int
    expected: int
    standalone_exponent: int
    standalone_period: int
    E_exponent: int
    E_period: int
    F_exponent: int
    F_period: int
    G_exponent: int
    G_period: int
    p: int
    r: int
    max_period_over_I: int
    cube_start: int | None
    ybt_start: int
    cell: FailureCell
    trace_times: CandidateTraceTimes
    E_event: OrbitEvent
    F_event: OrbitEvent
    G_event: OrbitEvent
    I_events: tuple[OrbitEvent, ...]
    g2cs_antecedent: bool
    g2cs_counterexample: bool


@dataclass(frozen=True)
class CandidateAudit:
    status: CandidateAuditStatus
    candidate: RecordSquareCandidate | None
    standalone_checks: tuple[StandalonePromotionCheck, ...]
    paired_windows: tuple[PairedGenerationWindow, ...]
    first_failure: FirstFailureReport | None
    invalid_reason: str | None


@dataclass(frozen=True)
class ScanSummary:
    max_seed_length: int
    step_limit: int
    seeds: int
    hit_one: int
    capped: int
    candidates: int
    promotion_roots: int
    first_failures: int
    g2cs_antecedents: int
    g2cs_verified: int
    g2cs_counterexamples: int
    cell_A: int
    cell_B: int
    cell_C: int
    unclassified: int
    first_failure_reports: tuple[FirstFailureReport, ...]


def classify_first_failure_cell(
    *, cube_start: int, ybt_start: int, r: int, q: int, P: int
) -> FailureCell:
    """Classify the later canonical cube by half-open start coordinates."""
    if cube_start < 0 or ybt_start < 0:
        raise ValueError("cube_start and ybt_start must be nonnegative")
    if not 0 < q < P:
        raise ValueError("requires 0 < q < P")
    if not 0 < r < P:
        raise ValueError("requires 0 < r < P")
    if cube_start >= ybt_start:
        return "C"
    if r == q:
        return "A"
    if q < r < P:
        return "B"
    return "unclassified"


def check_standalone_promotion(R: Sequence[int]) -> StandalonePromotionAudit:
    """Evaluate every direct standalone state R^2 R[:j]."""
    root: Word = tuple(R)
    if not root:
        raise ValueError("check_standalone_promotion requires a nonempty root")
    checks = []
    first_failure_j = None
    for j, expected in enumerate(root):
        word = root + root + root[:j]
        exponent, period = canonical_witness(word)
        checks.append(
            StandalonePromotionCheck(
                j=j,
                expected=expected,
                word=word,
                exponent=exponent,
                period=period,
            )
        )
        if first_failure_j is None and exponent != expected:
            first_failure_j = j

    return StandalonePromotionAudit(
        status="promotion_root" if first_failure_j is None else "first_failure",
        checks=tuple(checks),
        first_failure_j=first_failure_j,
    )


def canonical_witness(sequence: Sequence[int]) -> tuple[int, int]:
    """Return the maximal suffix exponent and its canonical period."""
    word: Word = tuple(sequence)
    if not word:
        raise ValueError("canonical_witness requires a nonempty word")

    length = len(word)
    best_exponent = 1
    best_period = length
    for period in range(1, length + 1):
        block = word[length - period :]
        copies = 1
        cursor = length - 2 * period
        while cursor >= 0 and word[cursor : cursor + period] == block:
            copies += 1
            cursor -= period
        if copies > best_exponent or (
            copies == best_exponent and copies >= 2 and period < best_period
        ):
            best_exponent = copies
            best_period = period

    return best_exponent, best_period


def trace_orbit(
    seed: Sequence[int], step_limit: int
) -> tuple[tuple[OrbitEvent, ...], TraceTermination]:
    """Trace every evaluated state through one or a capped number of appends."""
    current: Word = tuple(seed)
    if not current:
        raise ValueError("trace_orbit requires a nonempty seed")
    if step_limit < 0:
        raise ValueError("step_limit must be nonnegative")

    events = []
    seed_length = len(current)
    for time in range(step_limit + 1):
        exponent, period = canonical_witness(current)
        events.append(OrbitEvent(time, current, exponent, period, seed_length))
        if exponent == 1:
            return tuple(events), "hit_one"
        if time == step_limit:
            return tuple(events), "step_limit"
        current += (exponent,)

    raise AssertionError("unreachable")


def _is_generated_span(
    events_by_time: dict[int, OrbitEvent],
    start_time: int,
    end_time: int,
    generated: Word,
    seed: Word,
) -> bool:
    if end_time - start_time != len(generated):
        return False

    span = [events_by_time.get(time) for time in range(start_time, end_time + 1)]
    if any(event is None for event in span):
        return False

    typed_span = tuple(event for event in span if event is not None)
    if any(
        not event.word
        or event.seed_length != len(seed)
        or len(event.word) != event.seed_length + event.time
        or event.word[: event.seed_length] != seed
        or canonical_witness(event.word) != (event.exponent, event.period)
        for event in typed_span
    ):
        return False

    for current, following in zip(typed_span, typed_span[1:]):
        if current.word + (current.exponent,) != following.word:
            return False

    return (
        tuple(event.exponent for event in typed_span[:-1]) == generated
        and typed_span[0].word + generated == typed_span[-1].word
    )


def _is_complete_orbit_prefix(events: Sequence[OrbitEvent]) -> bool:
    if not events:
        return False

    seed_length = events[0].seed_length
    if seed_length <= 0:
        return False
    seed = events[0].word

    for expected_time, event in enumerate(events):
        if (
            event.time != expected_time
            or event.seed_length != seed_length
            or not event.word
            or len(event.word) != seed_length + expected_time
            or event.word[:seed_length] != seed
            or canonical_witness(event.word) != (event.exponent, event.period)
            or (event.exponent == 1 and expected_time != len(events) - 1)
        ):
            return False
        if expected_time and (
            events[expected_time - 1].word
            + (events[expected_time - 1].exponent,)
            != event.word
        ):
            return False

    return True


def extract_record_square_candidates(
    events: Sequence[OrbitEvent],
) -> tuple[RecordSquareCandidate, ...]:
    """Extract fully generated strict-record squares with audited trace provenance."""
    if not events or not _is_complete_orbit_prefix(events):
        return ()

    event_counts: dict[int, int] = {}
    events_by_time: dict[int, OrbitEvent] = {}
    for event in events:
        event_counts[event.time] = event_counts.get(event.time, 0) + 1
        events_by_time[event.time] = event
    events_by_time = {
        time: event
        for time, event in events_by_time.items()
        if event_counts[time] == 1
    }

    candidates = []
    prior_record_period = 0
    for terminal in events:
        is_strict_record = terminal.period > prior_record_period
        prior_record_period = max(prior_record_period, terminal.period)

        if (
            terminal.exponent != 2
            or not is_strict_record
            or not terminal.entire_power_generated()
            or terminal.seed_length <= 0
            or len(terminal.word) != terminal.seed_length + terminal.time
            or event_counts.get(terminal.time) != 1
        ):
            continue

        P = terminal.period
        g_time = terminal.time - P
        G = events_by_time.get(g_time)
        if (
            G is None
            or event_counts.get(g_time) != 1
            or not G.word
            or canonical_witness(G.word) != (G.exponent, G.period)
            or G.exponent != 2
        ):
            continue

        q = G.period
        if not 0 < q < P:
            continue
        b = P - q
        a = 2 * q - P
        if b <= 0 or a <= 0:
            continue

        R = G.word[-q:]
        B = R[-b:]
        A = R[: q - b]
        Y = B + R
        L = G.word[: -2 * q]
        seed = terminal.word[: terminal.seed_length]
        second_r_start_time = g_time - q
        second_r_start = events_by_time.get(second_r_start_time)

        if (
            len(A) != a
            or R != A + B
            or Y != B + R
            or G.word != L + R + R
            or terminal.word != G.word + Y
            or terminal.word != L + R + R + B + R
            or terminal.word[-2 * P :] != Y + Y
            or second_r_start is None
            or event_counts.get(second_r_start_time) != 1
            or second_r_start.word + R != G.word
            or not _is_generated_span(
                events_by_time,
                second_r_start_time,
                g_time,
                R,
                seed,
            )
            or not _is_generated_span(
                events_by_time,
                g_time,
                terminal.time,
                Y,
                seed,
            )
        ):
            continue

        candidates.append(
            RecordSquareCandidate(
                seed=seed,
                L=L,
                A=A,
                B=B,
                R=R,
                Y=Y,
                P=P,
                q=q,
                b=b,
                second_r_start_time=second_r_start_time,
                g_time=g_time,
                terminal_time=terminal.time,
            )
        )

    return tuple(candidates)


def _paired_generation_window(
    events_by_time: dict[int, OrbitEvent],
    candidate: RecordSquareCandidate,
    j: int,
) -> PairedGenerationWindow | None:
    T = candidate.R[:j]
    U = candidate.R[j:]
    m = candidate.q - j
    E_times = tuple(
        candidate.second_r_start_time + j + ell for ell in range(m + 1)
    )
    F_times = tuple(
        candidate.g_time + candidate.b + j + ell for ell in range(m + 1)
    )
    try:
        E_events = tuple(events_by_time[time] for time in E_times)
        F_events = tuple(events_by_time[time] for time in F_times)
    except KeyError:
        return None

    expected_E_words = tuple(
        candidate.L + candidate.R + T + U[:ell] for ell in range(m + 1)
    )
    expected_F_words = tuple(
        candidate.L
        + candidate.R
        + candidate.R
        + candidate.B
        + T
        + U[:ell]
        for ell in range(m + 1)
    )
    if (
        tuple(event.word for event in E_events) != expected_E_words
        or tuple(event.word for event in F_events) != expected_F_words
        or tuple(event.exponent for event in E_events[:-1]) != U
        or tuple(event.exponent for event in F_events[:-1]) != U
    ):
        return None

    I_events = E_events + F_events[:-1]
    return PairedGenerationWindow(
        j=j,
        T=T,
        U=U,
        E_events=E_events,
        F_events=F_events,
        I_events=I_events,
        max_period_over_I=max(event.period for event in I_events),
    )


def audit_record_square_candidate(
    events: Sequence[OrbitEvent], candidate: RecordSquareCandidate
) -> CandidateAudit:
    """Re-extract and audit a candidate before treating it as evidence."""
    validated = next(
        (
            extracted
            for extracted in extract_record_square_candidates(events)
            if extracted == candidate
        ),
        None,
    )
    if validated is None:
        return CandidateAudit(
            status="invalid_provenance",
            candidate=None,
            standalone_checks=(),
            paired_windows=(),
            first_failure=None,
            invalid_reason="missing_bridge_hypothesis",
        )

    return _audit_validated_record_square_candidate(events, validated)


def _audit_validated_record_square_candidate(
    events: Sequence[OrbitEvent], validated: RecordSquareCandidate
) -> CandidateAudit:
    """Audit a candidate already returned by extraction for these events."""
    events_by_time = {event.time: event for event in events}
    paired_windows = []
    for j in range(validated.q):
        window = _paired_generation_window(events_by_time, validated, j)
        if window is None:
            return CandidateAudit(
                status="invalid_provenance",
                candidate=None,
                standalone_checks=(),
                paired_windows=(),
                first_failure=None,
                invalid_reason="paired_generation_mismatch",
            )
        paired_windows.append(window)

    promotion = check_standalone_promotion(validated.R)
    if promotion.first_failure_j is None:
        return CandidateAudit(
            status="promotion_root",
            candidate=validated,
            standalone_checks=promotion.checks,
            paired_windows=tuple(paired_windows),
            first_failure=None,
            invalid_reason=None,
        )

    j = promotion.first_failure_j
    standalone = promotion.checks[j]
    window = paired_windows[j]
    E_event = window.E_events[0]
    F_event = window.F_events[0]
    G_event = window.E_events[-1]
    H_event = window.F_events[-1]
    p = E_event.period
    r = F_event.period
    g2cs_antecedent = (
        standalone.expected == 3
        and standalone.exponent == 2
        and E_event.exponent == 3
        and F_event.exponent == 3
        and G_event.exponent == 2
        and G_event.period == validated.q
        and H_event.exponent == 2
        and H_event.period == validated.P
    )
    cube_start = len(F_event.word) - 3 * r if g2cs_antecedent else None
    ybt_start = len(F_event.word) - (validated.P + validated.b + j)
    trace_times = CandidateTraceTimes(
        second_r_start_time=validated.second_r_start_time,
        g_time=validated.g_time,
        terminal_time=validated.terminal_time,
        E_times=tuple(event.time for event in window.E_events),
        F_times=tuple(event.time for event in window.F_events),
        I_times=tuple(event.time for event in window.I_events),
    )
    first_failure = FirstFailureReport(
        seed=validated.seed,
        seed_length=len(validated.seed),
        P=validated.P,
        q=validated.q,
        b=validated.b,
        j=j,
        expected=standalone.expected,
        standalone_exponent=standalone.exponent,
        standalone_period=standalone.period,
        E_exponent=E_event.exponent,
        E_period=E_event.period,
        F_exponent=F_event.exponent,
        F_period=F_event.period,
        G_exponent=G_event.exponent,
        G_period=G_event.period,
        p=p,
        r=r,
        max_period_over_I=window.max_period_over_I,
        cube_start=cube_start,
        ybt_start=ybt_start,
        cell=(
            classify_first_failure_cell(
                cube_start=cube_start,
                ybt_start=ybt_start,
                r=r,
                q=validated.q,
                P=validated.P,
            )
            if cube_start is not None
            else "unclassified"
        ),
        trace_times=trace_times,
        E_event=E_event,
        F_event=F_event,
        G_event=G_event,
        I_events=window.I_events,
        g2cs_antecedent=g2cs_antecedent,
        g2cs_counterexample=(
            g2cs_antecedent and window.max_period_over_I < validated.P
        ),
    )
    return CandidateAudit(
        status="first_failure",
        candidate=validated,
        standalone_checks=promotion.checks,
        paired_windows=tuple(paired_windows),
        first_failure=first_failure,
        invalid_reason=None,
    )


def _audit_extracted_candidates(
    events: Sequence[OrbitEvent],
    candidates: Sequence[RecordSquareCandidate],
) -> tuple[CandidateAudit, ...]:
    """Batch-audit candidates from one validated extraction."""
    return tuple(
        _audit_validated_record_square_candidate(events, candidate)
        for candidate in candidates
    )


def generated_states(start: Sequence[int], requested: Sequence[int]) -> tuple[Word, ...]:
    """Return the ordered generated trace, including its start and terminal states."""
    current: Word = tuple(start)
    if not current:
        raise ValueError("generated_states requires a nonempty start word")

    states = [current]
    for expected in requested:
        actual, _ = canonical_witness(current)
        if actual != expected:
            raise ValueError(f"expected {expected} but generated {actual}")
        current += (actual,)
        states.append(current)
    return tuple(states)


def synchronization_evaluation_states(
    early_states: Sequence[Sequence[int]], later_states: Sequence[Sequence[int]]
) -> tuple[Word, ...]:
    """Return the ordered evaluation family: G included; H excluded.

    Sequence order and duplicate states are preserved for trace provenance;
    each state is normalized to an immutable word.
    """
    early = tuple(tuple(state) for state in early_states)
    later = tuple(tuple(state) for state in later_states)
    if not early:
        raise ValueError(
            "synchronization_evaluation_states requires nonempty early_states"
        )
    if not later:
        raise ValueError(
            "synchronization_evaluation_states requires nonempty later_states"
        )
    return early + later[:-1]


def scan_binary_seeds(max_seed_length: int, step_limit: int) -> ScanSummary:
    """Audit every seed over {2,3} in deterministic length/lexical order."""
    if max_seed_length < 0:
        raise ValueError("max_seed_length must be nonnegative")
    if step_limit < 0:
        raise ValueError("step_limit must be nonnegative")

    seeds = 0
    hit_one = 0
    capped = 0
    candidates_count = 0
    promotion_roots = 0
    reports = []

    for length in range(1, max_seed_length + 1):
        for seed in product((2, 3), repeat=length):
            seeds += 1
            events, termination = trace_orbit(seed, step_limit)
            if termination == "hit_one":
                hit_one += 1
            elif termination == "step_limit":
                capped += 1
            else:
                raise AssertionError(f"unexpected termination: {termination}")

            candidates = extract_record_square_candidates(events)
            candidates_count += len(candidates)
            for audit in _audit_extracted_candidates(events, candidates):
                if audit.status == "invalid_provenance":
                    raise RuntimeError(
                        "extractor returned candidate that failed provenance audit: "
                        f"{audit.invalid_reason}"
                    )
                if audit.status == "promotion_root":
                    promotion_roots += 1
                elif audit.status == "first_failure":
                    if audit.first_failure is None:
                        raise AssertionError("first failure audit lacks report")
                    reports.append(audit.first_failure)
                else:
                    raise AssertionError(f"unexpected audit status: {audit.status}")

    reports.sort(
        key=lambda report: (
            report.seed,
            report.P,
            report.q,
            report.b,
            report.j,
            report.expected,
            report.standalone_exponent,
            report.standalone_period,
        )
    )
    cell_counts = {
        cell: sum(report.cell == cell for report in reports)
        for cell in ("A", "B", "C", "unclassified")
    }
    g2cs_antecedents = sum(report.g2cs_antecedent for report in reports)
    g2cs_counterexamples = sum(report.g2cs_counterexample for report in reports)
    return ScanSummary(
        max_seed_length=max_seed_length,
        step_limit=step_limit,
        seeds=seeds,
        hit_one=hit_one,
        capped=capped,
        candidates=candidates_count,
        promotion_roots=promotion_roots,
        first_failures=len(reports),
        g2cs_antecedents=g2cs_antecedents,
        g2cs_verified=g2cs_antecedents - g2cs_counterexamples,
        g2cs_counterexamples=g2cs_counterexamples,
        cell_A=cell_counts["A"],
        cell_B=cell_counts["B"],
        cell_C=cell_counts["C"],
        unclassified=cell_counts["unclassified"],
        first_failure_reports=tuple(reports),
    )


def _calibration_terminal_lengths() -> tuple[int, ...]:
    cases = (
        ("322", 5),
        ("23222323", 66),
        ("2322322323222323223223", 142),
    )
    actual_lengths = []
    for digits, expected_length in cases:
        events, termination = trace_orbit(tuple(map(int, digits)), 1000)
        actual_length = len(events[-1].word)
        if termination != "hit_one" or actual_length != expected_length:
            raise RuntimeError(
                "calibration failed for "
                f"seed={digits}: termination={termination}, "
                f"terminal_length={actual_length}, expected={expected_length}"
            )
        actual_lengths.append(actual_length)
    return tuple(actual_lengths)


def serialize_first_failure(report: FirstFailureReport) -> str:
    """Serialize a complete first-failure record deterministically."""
    return json.dumps(asdict(report), sort_keys=True, separators=(",", ":"))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Bounded falsifier for the Generated Two-Cube wall."
    )
    parser.add_argument("--max-seed-length", type=int, default=18)
    parser.add_argument("--step-limit", type=int, default=500)
    args = parser.parse_args(argv)

    calibration_lengths = _calibration_terminal_lengths()
    print(
        "calibration_terminal_lengths="
        + ",".join(map(str, calibration_lengths))
        + " status=PASS"
    )
    print("label=fully_generated_specialization")
    summary = scan_binary_seeds(args.max_seed_length, args.step_limit)
    for field in (
        "max_seed_length",
        "step_limit",
        "seeds",
        "hit_one",
        "capped",
        "candidates",
        "promotion_roots",
        "first_failures",
        "g2cs_antecedents",
        "g2cs_verified",
        "g2cs_counterexamples",
        "cell_A",
        "cell_B",
        "cell_C",
        "unclassified",
    ):
        print(f"{field}={getattr(summary, field)}")
    print(f"first_failure_records={len(summary.first_failure_reports)}")
    for report in summary.first_failure_reports:
        print(f"first_failure_record={serialize_first_failure(report)}")
    print(
        "NOT_A_PROOF: bounded fully_generated_specialization scan; "
        "zero bounded counterexamples is not a proof."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
