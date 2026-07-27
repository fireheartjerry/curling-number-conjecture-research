"""Exact audit for inherited cube bounds and record relocation."""

from __future__ import annotations

from itertools import product
from math import gcd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from curling import curling_number, curling_number_reference
from research.check_critical_seed_induction import (
    proper_circular_maximizing_roots,
    proper_circular_profile,
)


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


def maximizing_roots(word: Word, value: int) -> tuple[int, ...]:
    return tuple(
        root
        for root in range(1, len(word) // value + 1)
        if word[-value * root :] == word[-root:] * value
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


def first_larger_cube_record(
    root: Word, step_limit: int = 200
) -> tuple[int, int, int, int, int] | None:
    p = len(root)
    state = root * 3 + (3,)
    for step in range(step_limit):
        value = cn(state)
        if value >= 3:
            larger = tuple(
                candidate
                for candidate in maximizing_roots(state, value)
                if candidate > p
            )
            if larger:
                candidate = min(larger)
                return (
                    step,
                    len(state),
                    value,
                    candidate,
                    len(state) - value * candidate,
                )
        if value == 1:
            return None
        state += (value,)
    raise RuntimeError("orbit trace limit reached")


def main() -> None:
    # Exhaustive promoted-orbit search through old-root length seven.
    promoted_records: list[
        tuple[int, str, int, int, int, int, int]
    ] = []
    for p in range(1, 8):
        for tail in product((2, 3), repeat=p - 1):
            root = (2,) + tail
            if not primitive(root):
                continue
            if cn(root * 3) != 3:
                continue
            record = first_larger_cube_record(root)
            if record is None:
                continue
            step, cut, value, candidate, origin = record
            promoted_records.append(
                (
                    p,
                    "".join(map(str, root)),
                    step,
                    cut,
                    value,
                    candidate,
                    origin,
                )
            )

    assert promoted_records == [
        (4, "2232", 50, 63, 3, 21, 0),
        (4, "2322", 50, 63, 3, 21, 0),
        (7, "2322232", 54, 76, 3, 21, 13),
    ]

    old = tuple(map(int, "2322232"))
    p = len(old)
    promoted = old * 3 + (3,)
    state = promoted
    while len(state) < 76:
        value = cn(state)
        state += (value,)
    orbit_word = state
    assert len(orbit_word) == 76

    value = cn(orbit_word)
    assert value == 3
    assert maximizing_roots(orbit_word, value) == (21,)
    q = 21
    origin = len(orbit_word) - 3 * q
    assert origin == 13
    new_root = orbit_word[-q:]
    assert primitive(new_root)
    assert orbit_word[origin:] == new_root * 3
    assert "".join(map(str, new_root)) == "223222323222322232232"
    assert normalized_replay(new_root)

    previous = orbit_word[:-1]
    previous_value = cn(previous)
    assert previous_value == 2
    assert maximizing_roots(previous, previous_value) == (3, 21)
    assert previous + (previous_value,) == orbit_word
    assert cn(orbit_word) == 3

    old_cube_end = 3 * p
    overlap = old_cube_end - origin
    threshold = p + q - gcd(p, q)
    assert (overlap, threshold, threshold - overlap) == (8, 21, 13)
    assert orbit_word[origin:old_cube_end] == (
        old * 3
    )[origin:old_cube_end]
    assert (
        orbit_word[old_cube_end],
        orbit_word[old_cube_end + q],
        orbit_word[old_cube_end + 2 * q],
    ) == (3, 3, 3)

    intermediate_prefixes = tuple(
        length
        for length in range(p + 1, len(orbit_word))
        if normalized_replay(orbit_word[:length])
    )
    assert intermediate_prefixes == ()
    assert not normalized_replay(old)
    assert cn(old) == 1

    # Q21 proper bound and every exact postpromotion branch.
    base = tuple(map(int, "223222322232322232223"))
    n = len(base)
    assert primitive(base)
    assert proper_circular_profile(base) == base
    proper_cube_roots = tuple(
        root
        for cut, symbol in enumerate(base)
        if symbol == 3
        for root in proper_circular_maximizing_roots(base, cut)
    )
    assert max(proper_cube_roots) == 4

    branch_maxima: dict[int, int] = {}
    branch_records: dict[
        int, tuple[tuple[int, int, int, int], ...]
    ] = {}
    for shift in range(n):
        root = base[shift:] + base[:shift]
        if root[0] != 2:
            continue
        assert normalized_replay(root)
        branch = root * 3 + (3,)
        maximum = 0
        records: list[tuple[int, int, int, int]] = []
        for step in range(300):
            branch_value = cn(branch)
            if branch_value >= 3:
                for candidate in maximizing_roots(
                    branch, branch_value
                ):
                    if candidate > maximum:
                        maximum = candidate
                        records.append(
                            (
                                step,
                                candidate,
                                len(branch)
                                - branch_value * candidate,
                                branch_value,
                            )
                        )
            if branch_value == 1:
                break
            branch += (branch_value,)
        else:
            raise RuntimeError("Q21 branch trace limit reached")
        branch_maxima[shift] = maximum
        branch_records[shift] = tuple(records)

    assert branch_maxima == {
        0: 0,
        1: 10,
        3: 0,
        4: 1,
        5: 3,
        7: 0,
        8: 21,
        9: 7,
        11: 0,
        13: 0,
        14: 2,
        15: 0,
        17: 0,
        18: 6,
        19: 1,
    }
    assert all(value <= n for value in branch_maxima.values())
    assert branch_records[8] == (
        (3, 1, 64, 3),
        (10, 4, 62, 3),
        (54, 21, 55, 3),
    )

    print(f"promoted_record_scan={promoted_records}")
    print(
        "relocated_record="
        f"old={''.join(map(str, old))} cut={len(orbit_word)} "
        f"root={q} origin={origin} overlap={overlap}/{threshold} "
        f"new_root={''.join(map(str, new_root))}"
    )
    print(
        "relocated_maturation="
        f"previous_cn={previous_value} "
        f"previous_roots={maximizing_roots(previous, previous_value)} "
        f"cube_cn={cn(orbit_word)}"
    )
    print(f"intermediate_prefixes={intermediate_prefixes}")
    print(
        "q21_cube_bounds="
        f"proper={max(proper_cube_roots)} "
        f"postpromotion={branch_maxima}"
    )
    print(f"q21_shift8_records={branch_records[8]}")


if __name__ == "__main__":
    main()
