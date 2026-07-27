"""Regression and exact pointed-return checks for marker quotients.

Every reported proper circular curling profile is exhaustively enumerated.
The script checks the marker-loss inequality and the strict raw-length
edge in the pointed defect equation on Q21, the all-weight-two length-31
profile, and the mixed-weight length-37 profile.
"""

from __future__ import annotations

from dataclasses import dataclass


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return all(
        n % p != 0 or word != word[:p] * (n // p)
        for p in range(1, n)
    )


def is_power(
    word: tuple[int, ...], cut: int, root: int, exponent: int
) -> bool:
    n = len(word)
    final = tuple(word[(cut - root + j) % n] for j in range(root))
    return all(
        tuple(
            word[(cut - block * root + j) % n]
            for j in range(root)
        )
        == final
        for block in range(2, exponent + 1)
    )


def proper_profile(word: tuple[int, ...]) -> tuple[int, ...]:
    n = len(word)
    result: list[int] = []
    for cut in range(n):
        best = 1
        for root in range(1, n):
            exponent = 2
            while is_power(word, cut, root, exponent):
                best = max(best, exponent)
                exponent += 1
        result.append(best)
    return tuple(result)


@dataclass(frozen=True)
class Audit:
    name: str
    token_word: tuple[int, ...]
    proposed_weights: tuple[int, ...]
    token_profile: tuple[int, ...]
    return_lengths: tuple[int, ...]
    defect_edges: tuple[tuple[int, int], ...]
    aligned_sources: tuple[int, ...]
    aligned_cuts: int
    longest_quotient: tuple[int, ...]
    longest_quotient_profile: tuple[int, ...]


def landmark_quotient(
    word: tuple[int, ...], selected_colors: set[int]
) -> tuple[int, ...]:
    """Return-word color cycle between occurrences of selected colors."""
    n = len(word)
    landmarks = [
        position
        for position, color in enumerate(word)
        if color in selected_colors
    ]
    assert landmarks
    raw_to_color: dict[tuple[int, ...], int] = {}
    quotient: list[int] = []
    for index, current in enumerate(landmarks):
        previous = landmarks[index - 1]
        positions: list[int] = []
        cursor = (previous + 1) % n
        while True:
            positions.append(cursor)
            if cursor == current:
                break
            cursor = (cursor + 1) % n
        return_word = tuple(word[position] for position in positions)
        quotient.append(
            raw_to_color.setdefault(return_word, len(raw_to_color))
        )
    return tuple(quotient)


def audit(
    name: str, raw: tuple[int, ...], weights: dict[int, int]
) -> Audit:
    n = len(raw)
    wanted = tuple(weights[token] for token in raw)
    assert primitive(raw)
    assert proper_profile(raw) == wanted
    maximum = max(wanted)

    marker_positions = {
        position
        for position, token in enumerate(raw)
        if weights[token] == maximum
    }
    marker_cuts = {(position + 1) % n for position in marker_positions}

    def is_marker_cut(cut: int) -> bool:
        return cut % n in marker_cuts

    def factor(left: int, right: int) -> tuple[int, ...]:
        return tuple(raw[position % n] for position in range(left, right))

    def next_marker(cut: int) -> int:
        result = cut + 1
        while not is_marker_cut(result):
            result += 1
        return result

    def previous_marker(cut: int) -> int:
        result = cut - 1
        while not is_marker_cut(result):
            result -= 1
        return result

    raw_to_color: dict[tuple[int, ...], int] = {}
    returns_at_cuts: list[tuple[int, int, tuple[int, ...]]] = []
    for end in sorted(marker_cuts):
        start = previous_marker(end)
        return_word = factor(start, end)
        color = raw_to_color.setdefault(return_word, len(raw_to_color))
        returns_at_cuts.append((end, color, return_word))
    color_to_raw = {color: word for word, color in raw_to_color.items()}

    def token_interval(left: int, right: int) -> tuple[int, ...]:
        assert left <= right
        assert is_marker_cut(left) and is_marker_cut(right)
        result: list[int] = []
        cursor = left
        while cursor < right:
            end = next_marker(cursor)
            assert end <= right
            return_word = factor(cursor, end)
            assert return_word in raw_to_color
            result.append(raw_to_color[return_word])
            cursor = end
        return tuple(result)

    token_word = tuple(color for _, color, _ in returns_at_cuts)
    proposed_weights = tuple(
        weights[return_word[0]] for _, _, return_word in returns_at_cuts
    )
    token_cn = proper_profile(token_word)
    assert all(
        prescribed - 1 <= actual <= prescribed
        for actual, prescribed in zip(token_cn, proposed_weights)
    )

    defect_edges: list[tuple[int, int]] = []
    aligned_sources: list[int] = []
    aligned = 0
    for base_cut in sorted(marker_cuts):
        # Use a positive lift for intervals that wrap around coordinate zero.
        end = base_cut if base_cut > 0 else n
        exponent = weights[raw[end % n]]
        roots = [
            root
            for root in range(1, n)
            if is_power(raw, end, root, exponent)
            and primitive(factor(end - root, end))
        ]
        assert roots
        root = min(roots)

        # Copying the terminal maximum-weight token gives the previous
        # marker endpoint.
        assert is_marker_cut(end - root)
        z = token_interval(end - root, end)
        assert z
        power_start = end - exponent * root

        if is_marker_cut(power_start):
            assert token_interval(power_start, end) == z * exponent
            aligned += 1
            aligned_sources.append(z[0])
            continue

        prior_marker = previous_marker(power_start)
        first_marker = next_marker(power_start)
        first_color = z[0]
        first_raw = color_to_raw[first_color]

        # The first raw piece in the unaligned block is a copy of the first
        # ordinary return, but it is preceded by a nonempty partial return.
        assert first_marker == power_start + len(first_raw)
        assert factor(power_start, first_marker) == first_raw
        defect_raw = factor(prior_marker, first_marker)
        defect_color = raw_to_color[defect_raw]
        assert len(defect_raw) > len(first_raw)
        assert defect_raw[-len(first_raw) :] == first_raw

        tail = token_interval(
            first_marker, end - (exponent - 1) * root
        )
        actual = token_interval(prior_marker, end)
        assert actual == (defect_color,) + tail + z * (exponent - 1)
        defect_edges.append((first_color, defect_color))

    lengths = tuple(
        len(color_to_raw[color]) for color in range(len(color_to_raw))
    )
    for source, target in defect_edges:
        assert lengths[source] < lengths[target]

    longest_colors = {
        color
        for color, length in enumerate(lengths)
        if length == max(lengths)
    }
    assert all(source not in longest_colors for source, _ in defect_edges)
    longest_quotient = landmark_quotient(token_word, longest_colors)
    longest_profile = proper_profile(longest_quotient)

    return Audit(
        name=name,
        token_word=token_word,
        proposed_weights=proposed_weights,
        token_profile=token_cn,
        return_lengths=lengths,
        defect_edges=tuple(defect_edges),
        aligned_sources=tuple(aligned_sources),
        aligned_cuts=aligned,
        longest_quotient=longest_quotient,
        longest_quotient_profile=longest_profile,
    )


def main() -> None:
    audits = [
        audit(
            "Q21",
            tuple(map(int, "223222322232322232223")),
            {2: 2, 3: 3},
        ),
        audit(
            "all-weight-2 length 31",
            tuple(map(int, "0010200100101001020010200100101")),
            {0: 2, 1: 2, 2: 2},
        ),
        audit(
            "mixed-weight length 37",
            tuple(map(int, "0020010010100100020010010100100020010")),
            {0: 2, 1: 2, 2: 3},
        ),
    ]
    for result in audits:
        print(result)

    # Fixed regression values, stated in the accompanying note.
    q21, all_two, mixed = audits
    assert sorted(q21.return_lengths) == [2, 3, 4]
    assert q21.proposed_weights == (2,) * 6
    assert q21.token_profile.count(1) == 4
    assert q21.token_profile[1:] + q21.token_profile[:1] == (
        2,
        1,
        1,
        2,
        1,
        1,
    )
    assert len(q21.defect_edges) == 4
    assert q21.aligned_sources == (0, 0)
    assert q21.longest_quotient_profile == (1, 1, 1, 1)

    assert len(all_two.token_word) == 31
    assert all_two.token_profile == (2,) * 31
    assert not all_two.defect_edges
    assert len(all_two.longest_quotient) == 31
    assert all_two.longest_quotient_profile == (2,) * 31

    assert sorted(mixed.return_lengths) == [7, 15]
    assert mixed.proposed_weights == (2, 2, 2)
    assert mixed.token_profile == (2, 1, 1)
    assert mixed.defect_edges == ((0, 1), (0, 1))
    assert mixed.aligned_sources == (1,)
    assert mixed.longest_quotient_profile == (1, 1)


if __name__ == "__main__":
    main()
