from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

Word = tuple[int, ...]
TraceTermination = Literal["hit_one", "step_limit"]


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


def extract_record_square_candidates(
    events: Sequence[OrbitEvent],
) -> tuple[RecordSquareCandidate, ...]:
    """Extract fully generated strict-record squares with audited trace provenance."""
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
        if not terminal.word:
            continue
        actual_witness = canonical_witness(terminal.word)
        is_strict_record = actual_witness[1] > prior_record_period
        prior_record_period = max(prior_record_period, actual_witness[1])

        if (
            actual_witness != (terminal.exponent, terminal.period)
            or terminal.exponent != 2
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
