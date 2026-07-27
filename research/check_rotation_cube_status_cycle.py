"""Exact audit of the rotation/deletion coupling for the length-21 profile.

Run the A094004 calibration before accepting this output:

    python -m unittest \
      tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration

Every curling number used below is evaluated by both independent
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


def exact_tail(word: Word, step_limit: int = 10_000) -> int:
    current = word
    for step in range(step_limit + 1):
        value = exact_cn(current)
        if value == 1:
            return step
        current += (value,)
    raise RuntimeError("step limit reached before curling number one")


def primitive(word: Word) -> bool:
    return not any(
        len(word) % period == 0
        and word == word[:period] * (len(word) // period)
        for period in range(1, len(word))
    )


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


def rotate_left(word: Word, amount: int) -> Word:
    amount %= len(word)
    return word[amount:] + word[:amount]


def audit_static_prefix_window(max_n: int) -> int:
    """Exhaust the universal short-window implication on binary words."""
    cases = 0
    for n in range(3, max_n + 1):
        for root in product((2, 3), repeat=n):
            if not primitive(root):
                continue
            marker = root[-1]
            for tail_length in range(n + 2):
                for tail in product((2, 3), repeat=tail_length):
                    cases += 1
                    low = root * 3 + tail
                    high = (marker,) + low
                    low_cn = exact_cn(low)
                    high_cn = exact_cn(high)
                    if high_cn != low_cn:
                        assert tail_length == n - 1
                        assert tail == root[:-1]
    return cases


def audit_hidden_square_marker_contradiction(max_n: int) -> tuple[int, int]:
    """Audit the terminal-hidden square overlap before using orbit output."""
    tested = 0
    overlap_candidates = 0
    for n in range(3, max_n + 1):
        for root in product((2, 3), repeat=n):
            if (
                not primitive(root)
                or root[-1] != 3
                or any(
                    root[i] == root[(i + 1) % n] == 3
                    for i in range(n)
                )
            ):
                continue
            conjugate = (3,) + root[:-1]
            for offset in range(2, n):
                if offset <= gcd(n, offset):
                    continue
                tested += 1
                hidden = n + 1 - offset
                if (
                    conjugate[:hidden]
                    == conjugate[offset:] + (3,)
                ):
                    overlap_candidates += 1
                    # The overlap forces the first marker.  Asking the
                    # common output to begin in 3 would force the adjacent
                    # second marker and violate singleton 3-runs.
                    assert conjugate[hidden - 1] == 3
                    assert conjugate[hidden] != 3
    return tested, overlap_candidates


def audit_replay_visibility(
    max_root_length: int,
    max_exponent: int,
) -> tuple[int, int]:
    """Exhaust finite first-mismatch replays that cross the penultimate copy.

    A retained replay starts at a cut ``m`` of ``Y^k`` and has equal exact
    curling numbers for the word and its one-letter deletion at every cut
    from ``m`` through ``k|Y|-1``.  The shared values must spell the
    remaining letters of ``Y^k``.  At the final cut the exact values are
    ``k`` and ``k-1``.  The theorem uses only the subfamily with
    ``Y[0]=3`` and ``m<=(k-1)|Y|``.
    """
    retained = 0
    visible = 0
    for root_length in range(1, max_root_length + 1):
        for root in product((2, 3), repeat=root_length):
            if not primitive(root) or root[0] != 3:
                continue
            for exponent in range(2, max_exponent + 1):
                whole = root * exponent
                if (
                    exact_cn(whole) != exponent
                    or exact_cn(whole[1:]) != exponent - 1
                ):
                    continue
                prefix_values = [
                    (
                        exact_cn(whole[:cut]),
                        exact_cn(whole[1:cut]),
                    )
                    for cut in range(2, len(whole))
                ]
                for initial_length in range(2, len(whole)):
                    replay = prefix_values[initial_length - 2 :]
                    if not all(
                        high == low == whole[cut]
                        for cut, (high, low) in enumerate(
                            replay,
                            start=initial_length,
                        )
                    ):
                        continue
                    retained += 1
                    if initial_length <= (exponent - 1) * root_length:
                        visible += 1
                        penultimate = root * (exponent - 1)
                        assert exact_cn(penultimate) == exponent - 1
                        assert root[0] == exponent - 1
                        assert exponent == 4
    return retained, visible


def audit_reverse_fourth_power(max_root_length: int) -> tuple[int, int]:
    """Audit the exact two-step obstruction after a 4-versus-3 reset."""
    candidate_pairs = 0
    fresh_terminations = 0
    for root_length in range(1, max_root_length + 1):
        for root in product((2, 3), repeat=root_length):
            if not primitive(root) or root[0] != 3:
                continue
            whole = root * 4
            deleted = whole[1:]
            if exact_cn(whole) != 4 or exact_cn(deleted) != 3:
                continue
            candidate_pairs += 1
            rotated = rotate_left(root, 1)
            fourth_power = rotated * 4
            assert deleted + (3,) == fourth_power
            next_value = exact_cn(fourth_power)
            assert next_value >= 4
            assert next_value not in fourth_power
            assert exact_cn(fourth_power + (next_value,)) == 1
            fresh_terminations += 1
    return candidate_pairs, fresh_terminations


def main() -> None:
    profile = tuple(map(int, "223222322232322232223"))
    n = len(profile)
    assert n == 21
    assert primitive(profile)
    assert proper_circular_profile(profile) == profile
    static_cases = audit_static_prefix_window(7)
    hidden_tested, hidden_candidates = (
        audit_hidden_square_marker_contradiction(14)
    )
    replay_retained, replay_visible = audit_replay_visibility(9, 6)
    reverse_candidates, reverse_terminations = (
        audit_reverse_fourth_power(12)
    )

    rows: list[tuple[int, ...]] = []
    cube_tails: list[int] = []
    for phase in range(n):
        root = rotate_left(profile, phase)
        next_root = rotate_left(profile, phase + 1)
        cube = root * 3
        deleted = cube[1:]
        next_cube = next_root * 3

        assert exact_cn(cube) == 3
        assert exact_cn(deleted) == root[0]
        assert deleted + (root[0],) == next_cube

        cube_tail = exact_tail(cube)
        deleted_tail = exact_tail(deleted)
        next_tail = exact_tail(next_cube)
        assert deleted_tail == 1 + next_tail

        prefixed_next_tail = exact_tail((root[0],) + next_cube)
        if root[0] == 3:
            assert cube + (3,) == (3,) + next_cube
            assert cube_tail == 1 + prefixed_next_tail

            # Audit three members of the locked full-period family.
            marker_root = next_root
            assert marker_root[-1] == 3
            marker_prefix = marker_root[:-1]
            right_conjugate = (3,) + marker_prefix
            for locked_exponent in range(4, 7):
                locked_tail = (
                    marker_prefix
                    + right_conjugate * (locked_exponent - 4)
                )
                low_locked = marker_root * 3 + locked_tail
                high_locked = (3,) + low_locked
                assert high_locked == right_conjugate * locked_exponent
                assert exact_cn(low_locked) == locked_exponent - 1
                assert exact_cn(high_locked) == locked_exponent

        cube_tails.append(cube_tail)
        rows.append(
            (
                phase,
                root[0],
                cube_tail,
                deleted_tail,
                next_tail,
                prefixed_next_tail,
            )
        )

    assert len(cube_tails) == n
    print("profile", "".join(map(str, profile)))
    print("all_rotation_cubes_terminal", True)
    print(
        "columns",
        "phase symbol tau(cube) tau(deleted_cube) "
        "tau(next_rotation_cube) tau(symbol+next_rotation_cube)",
    )
    for row in rows:
        print(*row)
    print("cube_tail_min", min(cube_tails))
    print("cube_tail_max", max(cube_tails))
    print("locked_family_exponents_checked", "4..6 at every 3-phase")
    print("static_prefix_window_cases_through_n_7", static_cases)
    print(
        "hidden_square_marker_cases_through_n_14",
        hidden_tested,
        "overlap_candidates",
        hidden_candidates,
    )
    print(
        "first_mismatch_replays_through_root_length_9",
        replay_retained,
        "penultimate_copy_visible",
        replay_visible,
    )
    print(
        "reverse_4_vs_3_pairs_through_root_length_12",
        reverse_candidates,
        "fresh_marker_terminations",
        reverse_terminations,
    )


if __name__ == "__main__":
    main()
