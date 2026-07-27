"""Executed audit of decorated phase transport after cube promotion."""

from __future__ import annotations

from pathlib import Path
import sys


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from curling import curling_number, curling_number_reference


Word = tuple[int, ...]
BASE: Word = tuple(map(int, "223222322232322232223"))


def cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def maximizing_roots(word: Word, value: int) -> tuple[int, ...]:
    if value == 1:
        return ()
    roots = tuple(
        root
        for root in range(1, len(word) // value + 1)
        if word[-value * root :] == word[-root:] * value
    )
    assert roots
    return roots


def decorated_profile(word: Word) -> tuple[tuple[int, int], ...]:
    result = []
    for phase in range(len(word)):
        state = word * 2 + word[:phase]
        value = cn(state)
        roots = maximizing_roots(state, value)
        result.append((value, min(roots)))
    return tuple(result)


def post_trace(word: Word) -> tuple[
    tuple[tuple[int, int], ...], tuple[Word, ...]
]:
    state = word * 3 + (3,)
    decorated = []
    states = []
    for _ in range(len(word)):
        states.append(state)
        value = cn(state)
        roots = maximizing_roots(state, value)
        decorated.append((value, min(roots) if roots else 0))
        if value == 1:
            break
        state += (value,)
    return tuple(decorated), tuple(states)


def rotation(word: Word, shift: int) -> Word:
    return word[shift:] + word[:shift]


def audit_full_survivor() -> dict[str, object]:
    word = rotation(BASE, 8)
    profile = decorated_profile(word)
    post, _ = post_trace(word)
    assert len(post) == len(word)
    outputs = tuple(value for value, _ in post)
    roots = tuple(root for _, root in post)
    assert outputs == rotation(word, 5)
    assert roots == tuple(root for _, root in rotation(profile, 5))

    symbol_candidates = []
    decorated_candidates = []
    for length in range(1, len(word) + 1):
        symbol_candidates.append(
            tuple(
                phase
                for phase in range(len(word))
                if all(
                    outputs[offset] == word[(phase + offset) % len(word)]
                    for offset in range(length)
                )
            )
        )
        decorated_candidates.append(
            tuple(
                phase
                for phase in range(len(word))
                if all(
                    post[offset] == profile[(phase + offset) % len(word)]
                    for offset in range(length)
                )
            )
        )
    assert symbol_candidates[0] == (
        0, 1, 3, 5, 6, 7, 9, 10, 11, 13, 14, 16, 17, 18, 20
    )
    assert symbol_candidates[2] == (5, 9, 16, 20)
    assert symbol_candidates[6] == (5, 16)
    assert symbol_candidates[9] == (5,)
    assert decorated_candidates[0] == (5, 6)
    assert decorated_candidates[1] == (5,)
    assert all(candidates == (5,) for candidates in decorated_candidates[1:])
    return {
        "word": "".join(map(str, word)),
        "outputs": "".join(map(str, outputs)),
        "roots": roots,
        "symbol_candidates": tuple(symbol_candidates),
        "decorated_candidates": tuple(decorated_candidates),
    }


def audit_all_rotations() -> tuple[
    tuple[int, tuple[int, ...], int, int | None], ...
]:
    records = []
    high_events = []
    for shift in range(len(BASE)):
        word = rotation(BASE, shift)
        if word[0] != 2:
            continue
        profile = decorated_profile(word)
        post, states = post_trace(word)
        candidates = tuple(
            phase
            for phase in range(len(word))
            if word[phase - 1] == 3 and post[0] == profile[phase]
        )
        nonone = next(
            (index for index, pair in enumerate(post) if pair[0] == 1),
            len(post),
        )
        if nonone > 2:
            assert candidates

        mismatch = None
        if candidates:
            assert len(candidates) == 1
            phase = candidates[0]
            mismatch = next(
                (
                    index
                    for index, pair in enumerate(post)
                    if pair != profile[(phase + index) % len(word)]
                ),
                None,
            )
            if (
                mismatch is not None
                and post[mismatch][0] == 3
                and profile[(phase + mismatch) % len(word)][0] == 2
            ):
                state = states[mismatch]
                root = post[mismatch][1]
                child = state[-root:]
                assert state[-3 * root :] == child * 3
                local = child * 3 + (3,)
                first = cn(local)
                local += (first,)
                second = cn(local)
                assert (first, second) == (2, 1)
                high_events.append(
                    (
                        shift,
                        phase,
                        mismatch,
                        root,
                        "".join(map(str, child)),
                    )
                )
        records.append((shift, candidates, nonone, mismatch))

    assert tuple(high_events) == (
        (1, 12, 8, 10, "2322232223"),
        (9, 15, 4, 7, "2232223"),
        (18, 16, 4, 6, "232223"),
    )
    return tuple(records)


def main() -> None:
    survivor = audit_full_survivor()
    records = audit_all_rotations()
    print("survivor=" + repr(survivor))
    print("rotation_records=" + repr(records))


if __name__ == "__main__":
    main()

