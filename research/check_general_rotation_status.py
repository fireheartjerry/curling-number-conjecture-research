"""Finite audit for ``general_rotation_status.md``.

Run the A094004 total-orbit-length calibration before accepting output:

    python -m unittest \
      tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration

Every curling number below is evaluated by both independent
implementations in ``curling.py``.
"""

from __future__ import annotations

from itertools import product
from math import gcd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference


Word = tuple[int, ...]


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def primitive(word: Word) -> bool:
    return not any(
        len(word) % period == 0
        and word == word[:period] * (len(word) // period)
        for period in range(1, len(word))
    )


def rotate_left(word: Word, amount: int) -> Word:
    amount %= len(word)
    return word[amount:] + word[:amount]


def proper_circular_profile(word: Word) -> Word:
    n = len(word)
    assert primitive(word)
    profile: list[int] = []
    for cut in range(n):
        best = 1
        for root in range(1, n):
            matched = 0
            while (
                matched < n
                and word[(cut - 1 - matched) % n]
                == word[(cut - 1 - matched - root) % n]
            ):
                matched += 1
            assert matched < n
            best = max(best, 1 + matched // root)
        profile.append(best)
    return tuple(profile)


def audit_periodic_prefix_formula(max_n: int) -> int:
    cases = 0
    for n in range(2, max_n + 1):
        for word in product((2, 3, 4), repeat=n):
            if not primitive(word):
                continue
            profile = proper_circular_profile(word)
            for phase in range(n):
                root = rotate_left(word, phase)
                rotated_profile = rotate_left(profile, phase)
                for exponent in range(2, 6):
                    for tail_length in range(n):
                        state = root * exponent + root[:tail_length]
                        assert exact_cn(state) == max(
                            exponent,
                            rotated_profile[tail_length],
                        )
                        cases += 1
    return cases


def audit_local_fixed_phases(max_n: int) -> int:
    cases = 0
    for n in range(2, max_n + 1):
        for word in product((2, 3, 4), repeat=n):
            if not primitive(word):
                continue
            profile = proper_circular_profile(word)
            for phase in range(n):
                a = word[phase]
                if a < 3 or profile[phase] != a:
                    continue
                root = rotate_left(word, phase)
                next_root = rotate_left(word, phase + 1)
                cube = root * 3
                deleted = cube[1:]
                assert exact_cn(cube) == a
                assert exact_cn(deleted) == a
                assert deleted + (a,) == next_root * 3

                high = (a,) + next_root * 3
                low = next_root * 3
                expected = max(
                    3,
                    proper_circular_profile(next_root)[0],
                )
                assert exact_cn(high) == exact_cn(low) == expected
                cases += 1
    return cases


def audit_high_minimum_replays(
    max_root_length: int,
) -> tuple[int, int]:
    """Search finite roots satisfying all replay equations of Lemma 4."""
    tested = 0
    survivors = 0
    alphabet = (2, 3, 4, 5)
    for length in range(2, max_root_length + 1):
        for root in product(alphabet, repeat=length):
            a = root[0]
            if a < 3 or not primitive(root):
                continue
            tested += 1
            if not all(
                exact_cn(root * (a - 1) + root[:tail]) == root[tail]
                and exact_cn(root * a + root[:tail]) == root[tail]
                for tail in range(length)
            ):
                continue
            survivors += 1
            profile = proper_circular_profile(root)
            assert profile == root
            assert min(root) >= 3
    return tested, survivors


def audit_square_overlap(max_n: int) -> tuple[int, int]:
    overlap_words = 0
    complete_replays = 0
    for n in range(3, max_n + 1):
        for tail in product((2, 3, 4), repeat=n - 1):
            for a in (3, 4):
                conjugate = (a,) + tail
                for offset in range(2, n):
                    hidden = n + 1 - offset
                    if offset <= gcd(n, offset):
                        continue
                    if (
                        conjugate[:hidden]
                        != conjugate[offset:] + (a,)
                    ):
                        continue
                    overlap_words += 1
                    assert conjugate[hidden - 1] == a

                    low_root = conjugate[1:] + (a,)
                    high_initial = (a,) + low_root * 3
                    low_initial = low_root * 3
                    reset_root = (
                        conjugate * 2 + conjugate[:offset]
                    )
                    whole = reset_root * 2
                    deleted = whole[1:]
                    initial_length = len(high_initial)

                    if (
                        exact_cn(whole) != 2
                        or exact_cn(deleted) != 1
                        or exact_cn(high_initial)
                        != exact_cn(low_initial)
                    ):
                        continue
                    if not all(
                        exact_cn(whole[:cut])
                        == exact_cn(whole[1:cut])
                        == whole[cut]
                        for cut in range(initial_length, len(whole))
                    ):
                        continue
                    complete_replays += 1
                    assert conjugate[hidden] == exact_cn(high_initial)
    return overlap_words, complete_replays


def audit_square_reset_suffix(max_n: int) -> int:
    """Check the universal square suffix missed in Theorem 6.

    For ``Y=C^2 C[:s]`` with ``0<s<n``, writing ``C=A B`` gives
    ``Y=A B A B A``.  Its last ``2n`` symbols are
    ``B A B A=(B A)^2``.  Hence ``V=(Y^2)[1:]`` always has curling
    number at least two, independent of the symbols of ``C``.
    """
    cases = 0
    for n in range(2, max_n + 1):
        for conjugate in product((2, 3, 4), repeat=n):
            for split in range(1, n):
                left = conjugate[:split]
                right = conjugate[split:]
                reset_root = conjugate * 2 + left
                whole = reset_root * 2
                deleted = whole[1:]
                explicit_square = (right + left) * 2
                assert len(explicit_square) == 2 * n
                assert reset_root[-2 * n :] == explicit_square
                assert deleted[-2 * n :] == explicit_square
                assert exact_cn(deleted) >= 2
                cases += 1
    return cases


def main() -> None:
    prefix_cases = audit_periodic_prefix_formula(7)
    fixed_phase_cases = audit_local_fixed_phases(8)
    replay_tested, replay_survivors = audit_high_minimum_replays(7)
    overlap_words, complete_replays = audit_square_overlap(10)
    square_reset_suffix_cases = audit_square_reset_suffix(8)

    print("periodic_prefix_cases", prefix_cases)
    print("local_fixed_phase_cases", fixed_phase_cases)
    print("high_minimum_replay_roots_tested", replay_tested)
    print("high_minimum_replay_survivors", replay_survivors)
    print("square_overlap_words_through_length_10", overlap_words)
    print("complete_square_replays_through_length_10", complete_replays)
    print("square_reset_suffix_cases", square_reset_suffix_cases)


if __name__ == "__main__":
    main()
