"""Exact audit for the retrospective terminal-square birth lemma."""

from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from curling import curling_number, curling_number_reference


Word = tuple[int, ...]


def cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def primitive(word: Word) -> bool:
    n = len(word)
    return not any(
        n % period == 0
        and word == word[:period] * (n // period)
        for period in range(1, n)
    )


def maximizing_roots(word: Word) -> tuple[int, ...]:
    value = cn(word)
    return tuple(
        root
        for root in range(1, len(word) // value + 1)
        if word[-value * root :] == word[-root:] * value
    )


def ends_power(word: Word, root: int, exponent: int) -> bool:
    return (
        exponent * root <= len(word)
        and word[-exponent * root :] == word[-root:] * exponent
    )


def normalized_replay(word: Word) -> bool:
    if not primitive(word) or word[0] != 2:
        return False
    state = word
    for step in range(2 * len(word)):
        value = cn(state)
        if value != word[step % len(word)]:
            return False
        state += (value,)
    return cn(state) == 3


def main() -> None:
    marker_root = tuple(map(int, "2232"))
    larger = tuple(map(int, "223222322232322232223"))
    promoted = marker_root * 3 + (3,)
    p = len(marker_root)
    n = len(larger)

    assert primitive(marker_root)
    assert primitive(larger)
    assert larger[: len(promoted)] == promoted

    # This is an actual orbit from the old promotion marker into larger.
    state = promoted
    postpromotion_outputs: list[int] = []
    while len(state) < n:
        value = cn(state)
        postpromotion_outputs.append(value)
        assert value == larger[len(state)]
        state += (value,)
    assert state == larger
    assert tuple(postpromotion_outputs) == (
        2,
        2,
        2,
        3,
        2,
        2,
        2,
        3,
    )

    # The larger word satisfies every replay equation through its cube.
    assert normalized_replay(larger)
    replay_state = larger
    for step in range(2 * n):
        value = cn(replay_state)
        assert value == larger[step % n]
        replay_state += (value,)
    assert replay_state == larger * 3
    assert cn(replay_state) == 3

    assert cn(larger) == 2
    assert maximizing_roots(larger) == (4, 10)
    root = 4
    c = n - 2 * root
    d = n - root
    terminal_root = larger[d:n]
    assert larger[c:d] == terminal_root
    assert terminal_root == tuple(map(int, "2223"))

    # Maximal left extension of the terminal period-root run.
    left = c
    while (
        left > 0
        and larger[left - 1] == larger[left - 1 + root]
    ):
        left -= 1
    delta = c - left
    birth = left + 2 * root
    assert (left, c, d, n, delta, birth) == (11, 13, 17, 21, 2, 19)
    assert all(
        larger[index] == larger[index + root]
        for index in range(left, n - root)
    )
    assert larger[left - 1] != larger[left - 1 + root]

    tower_word = larger * 3
    cut_records: list[
        tuple[int, int, tuple[int, ...], bool]
    ] = []
    for cut in range(birth, n + 1):
        prefix = tower_word[:cut]
        value = cn(prefix)
        roots = maximizing_roots(prefix)
        square_available = ends_power(prefix, root, 2)
        assert square_available
        assert not ends_power(prefix, root, 3)
        assert (root in roots) == (value == 2)
        cut_records.append((cut, value, roots, root in roots))
    assert cut_records == [
        (19, 2, (1, 4), True),
        (20, 3, (1,), False),
        (21, 2, (4, 10), True),
    ]

    target_records: list[
        tuple[int, int, bool, bool, int, tuple[int, ...]]
    ] = []
    for offset in range(root):
        target = d + offset
        parent = c + offset
        assert larger[target] == larger[parent]
        cut = target + 1
        prefix = tower_word[:cut]
        available = ends_power(prefix, root, 2)
        value = cn(prefix)
        roots = maximizing_roots(prefix)
        target_records.append(
            (target, parent, available, root in roots, value, roots)
        )
    assert target_records == [
        (17, 13, False, False, 2, (6,)),
        (18, 14, True, True, 2, (1, 4)),
        (19, 15, True, False, 3, (1,)),
        (20, 16, True, True, 2, (4, 10)),
    ]

    # Exhaust every possible intermediate prefix length in this model.
    intermediate_replays = tuple(
        length
        for length in range(p + 1, n)
        if normalized_replay(larger[:length])
    )
    assert intermediate_replays == ()

    # The caveat is explicit: the small marker root itself is not replay
    # fixed, so this is a full postpromotion/upper-level model rather than
    # a full two-level tower model.
    assert not normalized_replay(marker_root)
    assert cn(marker_root) == 1

    print(
        "postpromotion_orbit="
        f"start={len(promoted)} end={n} "
        f"outputs={tuple(postpromotion_outputs)}"
    )
    print(
        "larger_replay="
        f"length={n} phase_zero={cn(larger)} "
        f"roots={maximizing_roots(larger)} cube_value={cn(larger * 3)}"
    )
    print(
        "terminal_square_episode="
        f"root={root} left={left} birth={birth} delta={delta} "
        f"cuts={cut_records}"
    )
    print(f"target_birth_parents={target_records}")
    print(f"intermediate_replay_prefixes={intermediate_replays}")


if __name__ == "__main__":
    main()
