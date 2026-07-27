from __future__ import annotations

from collections.abc import Sequence

Word = tuple[int, ...]


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
