"""Executed certificates for the terminal-marker ancestry lemmas.

All finite curling numbers are checked with both implementations in
``curling.py``.  Proper circular values are exhaustively checked over
every root length below the circular period.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from curling import curling_number, curling_number_reference


Word = tuple[int, ...]
TERMINAL_ROOTS: tuple[Word, ...] = tuple(
    tuple(map(int, text)) for text in ("2", "23", "223", "2223")
)


def checked_cn(word: Word) -> int:
    fast = curling_number(word)
    slow = curling_number_reference(word)
    assert fast == slow
    return fast


def primitive(word: Word) -> bool:
    n = len(word)
    return not any(
        n % period == 0
        and word == word[:period] * (n // period)
        for period in range(1, n)
    )


def proper_cut(word: Word, cut: int) -> tuple[int, tuple[int, ...]]:
    """Return the exact proper circular value and all maximizing roots."""

    n = len(word)
    best = 1
    roots: list[int] = []
    for root in range(1, n):
        matched = 0
        while (
            matched < n
            and word[(cut - 1 - matched) % n]
            == word[(cut - 1 - matched - root) % n]
        ):
            matched += 1
        value = 1 + matched // root
        if value > best:
            best = value
            roots = [root]
        elif value == best:
            roots.append(root)
    return best, tuple(roots)


def terminal(root: Word) -> Word:
    return root * 3 + (3, 2)


def borders(word: Word) -> tuple[int, ...]:
    return tuple(
        length
        for length in range(1, len(word))
        if word[:length] == word[-length:]
    )


def short_macro_records():
    records = {}
    surviving_high_masks = {}
    for root in TERMINAL_ROOTS:
        marker = terminal(root)
        rotated = marker[1:]
        promoted = rotated * 3
        assert primitive(rotated)
        assert checked_cn(marker) == 1
        assert checked_cn(promoted) == 3

        candidates = []
        for copy_length in range(len(marker), 3 * len(rotated)):
            copied = promoted[-copy_length:]
            if copied[0] != 3 or not primitive(copied):
                continue
            if checked_cn(copied * 2) != 2:
                continue
            finite_values = tuple(
                checked_cn(promoted + copied[:offset])
                for offset in range(copy_length)
            )
            overflow = tuple(
                offset
                for offset, (value, label) in enumerate(
                    zip(finite_values, copied)
                )
                if value > label
            )
            masks = tuple(
                offset
                for offset, (value, label) in enumerate(
                    zip(finite_values, copied)
                )
                if value < label
            )
            candidates.append((copy_length, overflow, masks))
        records["".join(map(str, root))] = tuple(candidates)
        surviving_high_masks["".join(map(str, root))] = tuple(
            (
                copy_length,
                tuple(
                    offset
                    for offset in masks
                    if promoted[-copy_length:][offset] == 3
                ),
            )
            for copy_length, overflow, masks in candidates
            if not overflow
        )

    expected = {
        "2": ((6, (), ()), (10, (), ())),
        "23": (
            (9, (1, 3, 5, 6, 7), ()),
            (10, (4,), (3, 5)),
            (12, (1, 8), (5, 7)),
            (16, (1, 3, 5, 6, 7), (9, 11)),
            (17, (4,), (3, 5, 10, 12)),
        ),
        "223": (
            (12, (8,), (1, 3, 4, 6)),
            (13, (), (1, 4, 5, 6, 7)),
            (16, (), (1, 3, 4, 7, 9, 10)),
            (19, (), (1, 3, 4, 6, 7, 10, 12, 13)),
            (22, (8,), (1, 3, 4, 6, 13, 15, 16)),
            (23, (), (1, 4, 5, 6, 7, 14, 16, 17)),
            (26, (), (1, 3, 4, 7, 9, 10, 17, 20)),
        ),
        "2223": (
            (15, (11,), (1, 5, 6)),
            (16, (), (1, 6, 7)),
            (20, (), (1, 5, 11)),
            (24, (), (1, 5, 6, 9, 15)),
            (28, (11,), (1, 5, 6, 19)),
            (29, (), (1, 6, 7, 20)),
            (33, (), (1, 5, 11, 24)),
            (37, (), (1, 5, 6, 9, 15)),
        ),
    }
    assert records == expected
    assert surviving_high_masks == {
        "2": ((6, ()), (10, ())),
        "23": (),
        "223": (
            (13, (1, 4, 7)),
            (16, (3, 4, 7, 10)),
            (19, (3, 6, 7, 10, 13)),
            (23, (1, 4, 7, 14, 17)),
            (26, (3, 4, 7, 10, 17, 20)),
        ),
        "2223": (
            (16, (1,)),
            (20, (5,)),
            (24, (9,)),
            (29, (1,)),
            (33, (5,)),
            (37, (9,)),
        ),
    }
    return records, surviving_high_masks


def circular_factor_ending(word: Word, cut: int, length: int) -> Word:
    n = len(word)
    return tuple(word[(cut - length + offset) % n] for offset in range(length))


def all_long_countermodel():
    root = tuple(map(int, "223"))
    marker = terminal(root)
    word = tuple(
        map(int, "33223223223322332232232233223322322322332")
    )
    n = len(word)
    assert n == 41
    assert primitive(word)
    assert borders(marker) == (1,)
    assert checked_cn(marker) == 1

    marker_ends = tuple(
        cut
        for cut in range(n)
        if circular_factor_ending(word, cut, len(marker)) == marker
    )
    assert marker_ends == (0, 13, 27)

    # One all-long ancestry cycle:
    #
    # * the high marker at cut 0 has an incoming root-14 cube;
    # * its first and second root-copy endpoints are cuts 13 and 27;
    # * the low marker at cut 13 has a root-13 square whose parent marker
    #   is the high marker at cut 0 in the preceding circular lift.
    assert proper_cut(word, 0) == (3, (14,))
    assert proper_cut(word, 13) == (2, (13,))
    assert proper_cut(word, 27) == (2, (14, 27))

    incoming = circular_factor_ending(word, 0, 14)
    outgoing = circular_factor_ending(word, 13, 13)
    assert incoming == tuple(map(int, "23322322322332"))
    assert outgoing == tuple(map(int, "3322322322332"))
    assert circular_factor_ending(word, 0, 42) == incoming * 3
    assert circular_factor_ending(word, 13, 26) == outgoing * 2
    assert primitive(incoming)
    assert primitive(outgoing)

    # Every declared marker has the exact local terminal history 3,2.
    terminal_profiles = tuple(
        (
            cut,
            proper_cut(word, (cut - 2) % n),
            proper_cut(word, (cut - 1) % n),
            proper_cut(word, cut),
        )
        for cut in marker_ends
    )
    assert terminal_profiles == (
        (0, (3, (3,)), (2, (1, 14)), (3, (14,))),
        (13, (3, (3,)), (2, (1, 13)), (2, (13,))),
        (27, (3, (3,)), (2, (1, 27)), (2, (14, 27))),
    )

    # Rotate to an origin whose first symbol is 2.  All roots used by the
    # displayed ancestry are first-copy fitting there.
    shift = 2
    rotated = word[shift:] + word[:shift]
    assert rotated[0] == 2
    rotated_high = (-shift) % n
    rotated_first_low = (13 - shift) % n
    rotated_second_low = (27 - shift) % n
    assert (rotated_high, rotated_first_low, rotated_second_low) == (
        39,
        11,
        25,
    )
    assert 3 * 14 <= n + rotated_high - 1
    assert 2 * 13 <= n + rotated_first_low - 1
    assert 2 * 14 <= n + rotated_second_low - 1

    profile = tuple(proper_cut(word, cut)[0] for cut in range(n))
    mismatches = tuple(
        cut for cut in range(n) if profile[cut] != word[cut]
    )
    assert len(mismatches) == 16
    return {
        "word": "".join(map(str, word)),
        "length": n,
        "marker_ends": marker_ends,
        "terminal_profiles": terminal_profiles,
        "incoming_cube_root": "".join(map(str, incoming)),
        "outgoing_square_root": "".join(map(str, outgoing)),
        "rotated_origin": shift,
        "rotated_ancestry_cuts": (
            rotated_high,
            rotated_first_low,
            rotated_second_low,
        ),
        "off_ancestry_profile_mismatches": mismatches,
    }


def all_long_first_refinement():
    """Certify that the length-41 local macro dies at its first new cut."""

    words = tuple(
        tuple(map(int, text))
        for text in (
            "32223223223322322232232233223222322322332",
            "33223223223322332232232233223322322322332",
        )
    )
    n = 41
    marker = terminal(tuple(map(int, "223")))

    # Equality closure of the root-14 cube and the two displayed squares.
    parent = list(range(n))

    def find(value: int) -> int:
        while parent[value] != value:
            parent[value] = parent[parent[value]]
            value = parent[value]
        return value

    def union(left: int, right: int) -> None:
        left = find(left)
        right = find(right)
        if left != right:
            parent[right] = left

    def add_power(cut: int, exponent: int, root: int) -> None:
        for block in range(2, exponent + 1):
            for offset in range(root):
                union(
                    (cut - block * root + offset) % n,
                    (cut - root + offset) % n,
                )

    add_power(0, 3, 14)
    add_power(13, 2, 13)
    add_power(27, 2, 14)

    fixed: dict[int, int] = {}

    def set_value(index: int, value: int) -> None:
        component = find(index % n)
        if component in fixed:
            assert fixed[component] == value
        fixed[component] = value

    for offset, value in enumerate(marker):
        set_value(-len(marker) + offset, value)
    set_value(0, 3)
    set_value(13, 2)
    set_value(27, 2)
    for endpoint in (0, 13, 27):
        set_value(endpoint - 2, 3)
        set_value(endpoint - 1, 2)

    components: dict[int, list[int]] = {}
    for index in range(n):
        components.setdefault(find(index), []).append(index)
    free = tuple(
        tuple(indices)
        for component, indices in components.items()
        if component not in fixed
    )
    assert free == ((1, 15, 29),)

    reconstructed = []
    for free_value in (2, 3):
        assignment = dict(fixed)
        assignment[find(1)] = free_value
        reconstructed.append(
            tuple(assignment[find(index)] for index in range(n))
        )
    assert tuple(reconstructed) == words

    ancestry_cuts = (0, 11, 12, 13, 25, 26, 27, 39, 40)
    for word in words:
        assert primitive(word)
        assert proper_cut(word, 1)[0] == 1
        assert tuple(
            (cut, proper_cut(word, cut))
            for cut in ancestry_cuts
        ) == (
            (0, (3, (14,))),
            (11, (3, (3,))),
            (12, (2, (1, 13))),
            (13, (2, (13,))),
            (25, (3, (3,))),
            (26, (2, (1, 27))),
            (27, (2, (14, 27))),
            (39, (3, (3,))),
            (40, (2, (1, 14))),
        )

    # For every proposed square root at cut 1, give a coordinate mismatch
    # which is independent of the one free bit.
    mismatch_certificate = []
    for root in range(1, n):
        mismatch = next(
            (
                (
                    offset,
                    (1 - 2 * root + offset) % n,
                    (1 - root + offset) % n,
                    words[0][(1 - 2 * root + offset) % n],
                    words[0][(1 - root + offset) % n],
                )
                for offset in range(root)
                if all(
                    word[(1 - 2 * root + offset) % n]
                    != word[(1 - root + offset) % n]
                    for word in words
                )
            ),
            None,
        )
        assert mismatch is not None
        mismatch_certificate.append((root,) + mismatch)

    def marker_location(index: int) -> str:
        phase = index % n
        if phase == 0:
            return "H"
        if phase == 13:
            return "L1"
        if phase == 27:
            return "L2"
        if phase < 13:
            return "A"
        if phase < 27:
            return "B"
        return "C"

    intersection_classes: list[tuple[str, str, tuple[int, ...]]] = []
    for root in range(1, n):
        key = (
            marker_location(1 - 2 * root),
            marker_location(1 - root),
        )
        if intersection_classes and intersection_classes[-1][:2] == key:
            old = intersection_classes[-1]
            intersection_classes[-1] = (old[0], old[1], old[2] + (root,))
        else:
            intersection_classes.append((key[0], key[1], (root,)))
    assert tuple(intersection_classes) == (
        ("C", "H", (1,)),
        ("C", "C", (2, 3, 4, 5, 6, 7)),
        ("B", "C", (8, 9, 10, 11, 12, 13, 14)),
        ("A", "L2", (15,)),
        ("A", "B", (16, 17, 18, 19, 20)),
        ("H", "B", (21,)),
        ("C", "B", (22, 23, 24, 25, 26, 27)),
        ("L2", "B", (28,)),
        ("B", "L1", (29,)),
        ("B", "A", (30, 31, 32, 33, 34)),
        ("L1", "A", (35,)),
        ("A", "A", (36, 37, 38, 39, 40)),
    )
    return {
        "base_words": tuple("".join(map(str, word)) for word in words),
        "free_component": free,
        "first_new_cut": 1,
        "first_new_value": tuple(proper_cut(word, 1)[0] for word in words),
        "intersection_classes": tuple(intersection_classes),
        "mismatch_certificate": tuple(mismatch_certificate),
    }


def component_quotient_survivors():
    cases = (
        (
            "2",
            7,
            6,
            "32223223222322322232",
            (1, 2, 3),
            7,
        ),
        (
            "223",
            22,
            21,
            "32232233232232232233223223223323223223223322322322332322322322332",
            (1, 2),
            3,
        ),
        (
            "2223",
            29,
            15,
            "3222322232223322223222322233232223222322233222232223222332322232223222332",
            tuple(range(1, 11)),
            11,
        ),
    )
    records = []
    for root_text, incoming, outgoing, text, replay_cuts, failure in cases:
        word = tuple(map(int, text))
        n = len(word)
        assert n == outgoing + 2 * incoming
        assert primitive(word)
        marker = terminal(tuple(map(int, root_text)))
        endpoints = (0, outgoing, outgoing + incoming)
        for endpoint in endpoints:
            assert circular_factor_ending(
                word, endpoint, len(marker)
            ) == marker
            assert proper_cut(word, (endpoint - 2) % n)[0] == 3
            assert proper_cut(word, (endpoint - 1) % n)[0] == 2
        assert proper_cut(word, 0) == (3, (incoming,))
        assert proper_cut(word, outgoing)[0] == 2
        assert outgoing in proper_cut(word, outgoing)[1]
        assert proper_cut(word, outgoing + incoming)[0] == 2
        assert incoming in proper_cut(word, outgoing + incoming)[1]
        replay_profile = tuple(
            (cut, word[cut], proper_cut(word, cut))
            for cut in replay_cuts
        )
        assert all(label == value[0] for _, label, value in replay_profile)
        failure_record = (
            failure,
            word[failure],
            proper_cut(word, failure),
        )
        records.append(
            {
                "terminal_root": root_text,
                "incoming": incoming,
                "outgoing": outgoing,
                "length": n,
                "replay_profile": replay_profile,
                "displayed_model_failure": failure_record,
            }
        )
    return tuple(records)


def main() -> None:
    marker_data = tuple(
        (
            "".join(map(str, root)),
            "".join(map(str, terminal(root))),
            borders(terminal(root)),
            checked_cn(terminal(root)),
        )
        for root in TERMINAL_ROOTS
    )
    assert all(border == (1,) and value == 1 for _, _, border, value in marker_data)
    print("terminal_markers", marker_data)
    short_records, high_masks = short_macro_records()
    print("short_macro_records", short_records)
    print("surviving_short_macro_high_masks", high_masks)
    print("all_long_local_countermodel", all_long_countermodel())
    print("all_long_first_refinement", all_long_first_refinement())
    print("component_quotient_survivors", component_quotient_survivors())


if __name__ == "__main__":
    main()
