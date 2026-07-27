"""Audit the bridge from an external root-one source to a run-code gadget.

Run the A094004 calibration test before this script:

    python -m unittest \
      tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration

The first audit is Q21, where both external ancestry edges happen to select
terminal span-one gadgets with period code ``(3,)``.  The second audit is a
local countermodel: the same exact endpoint labels, fitting inequalities, and
anchored ``3,2,2,2`` source coexist with a tight span-two gadget whose period
code is ``(3,2)`` and is not terminal.  The countermodel is not asserted to
have the full fixed profile at every cut.
"""

from __future__ import annotations

from check_max_square_terminal_forest import fitting
from check_run_length_grammar import (
    Gadget,
    binary_word,
    defect_gadget,
    primitive,
    proper_profile,
    run_starts,
    word_power_root_lengths,
)


Q21_CODE = (2, 3, 3, 1, 3, 3)
LOCAL_CODE = (1, 3, 2, 3, 2, 3)


def tight_gadget(
    code: tuple[int, ...], endpoint: int, span: int
) -> Gadget | None:
    """Return a gadget only when its leading capacity is exact."""
    gadget = defect_gadget(code, endpoint, span)
    if gadget is None:
        return None
    leading = (endpoint - 3 * span) % len(code)
    if code[leading] != gadget.alpha:
        return None
    return gadget


def terminal(gadget: Gadget) -> bool:
    """Section 7 terminality for the gadget's primitive period code."""
    period_code = gadget.period_code
    for endpoint, value in enumerate(period_code):
        if value in (1, 2) and tight_gadget(period_code, endpoint, 1) is None:
            return False
    return True


def circular_run_code_rotations(
    word: tuple[int, ...],
) -> set[tuple[int, ...]]:
    """All rotations of the circular 2-run code of a singleton-3 word."""
    assert 3 in word
    assert all(
        not (word[index] == word[(index + 1) % len(word)] == 3)
        for index in range(len(word))
    )
    markers = [index for index, value in enumerate(word) if value == 3]
    runs: list[int] = []
    for marker_index, marker in enumerate(markers):
        next_marker = markers[(marker_index + 1) % len(markers)]
        distance = (next_marker - marker) % len(word)
        if distance == 0:
            distance = len(word)
        runs.append(distance - 1)
    code = tuple(runs)
    return {
        code[offset:] + code[:offset]
        for offset in range(len(code))
    }


def root_word(
    word: tuple[int, ...], endpoint: int, root: int
) -> tuple[int, ...]:
    return tuple(
        word[(endpoint - root + offset) % len(word)]
        for offset in range(root)
    )


def audit_q21() -> tuple[dict[str, object], ...]:
    word = binary_word(Q21_CODE)
    assert "".join(map(str, word)) == "223222322232322232223"
    assert primitive(word)
    assert proper_profile(word) == word

    starts = run_starts(Q21_CODE)
    records: list[dict[str, object]] = []
    for endpoint, expected_source in ((0, 5), (3, 15)):
        gadget = tight_gadget(Q21_CODE, endpoint, 1)
        assert gadget is not None
        assert gadget.period_code == (3,)
        assert terminal(gadget)

        high = starts[endpoint] + Q21_CODE[endpoint]
        source = (high + 3) % len(word)
        assert source == expected_source
        assert Q21_CODE[(endpoint + 1) % len(Q21_CODE)] == 3
        assert tuple(word[(high + offset) % len(word)] for offset in range(4)) == (
            3,
            2,
            2,
            2,
        )

        cube_roots = word_power_root_lengths(word, high, 3)
        assert cube_roots == (4,)
        selected_root = root_word(word, high, 4)
        assert gadget.period_code in circular_run_code_rotations(selected_root)
        assert fitting(word, high, 3, 4)
        assert fitting(word, source, 2, 1)

        records.append(
            {
                "source_square": (source, 1),
                "high_cut": high,
                "selected_cube_root": 4,
                "gadget_endpoint": endpoint,
                "gadget_span": gadget.span,
                "period_code": gadget.period_code,
                "terminal": terminal(gadget),
                "root_word": selected_root,
            }
        )
    return tuple(records)


def audit_local_countermodel() -> dict[str, object]:
    circular_word = binary_word(LOCAL_CODE)
    assert primitive(LOCAL_CODE)
    assert primitive(circular_word)

    endpoint = 0
    gadget = tight_gadget(LOCAL_CODE, endpoint, 2)
    assert gadget is not None
    assert gadget.period_code == (3, 2)
    assert not terminal(gadget)
    assert tight_gadget(gadget.period_code, 1, 1) is None

    starts = run_starts(LOCAL_CODE)
    old_high = starts[endpoint] + LOCAL_CODE[endpoint]
    assert old_high == 1
    assert LOCAL_CODE[(endpoint + 1) % len(LOCAL_CODE)] == 3

    # Move the distinguished physical origin one symbol to the left.  This
    # leaves all circular factors unchanged and makes the selected cube
    # first-copy fitting at canonical high cut 2.
    shift = len(circular_word) - 1
    word = circular_word[shift:] + circular_word[:shift]
    high = (old_high - shift) % len(word)
    source = (old_high + 3 - shift) % len(word)
    assert (high, source) == (2, 5)

    profile = proper_profile(word)
    assert profile[high] == 3
    assert profile[source] == 2
    assert tuple(word[(high + offset) % len(word)] for offset in range(4)) == (
        3,
        2,
        2,
        2,
    )

    cube_roots = word_power_root_lengths(word, high, 3)
    assert cube_roots == (7,)
    selected_root = root_word(word, high, 7)
    assert gadget.period_code in circular_run_code_rotations(selected_root)
    assert fitting(word, high, 3, 7)
    assert fitting(word, source, 2, 1)

    child = (high - 7) % len(word)
    assert 7 in word_power_root_lengths(word, child, 2)
    assert fitting(word, child, 2, 7)

    return {
        "run_code": LOCAL_CODE,
        "rotated_word": "".join(map(str, word)),
        "source_square": (source, 1),
        "high_cut": high,
        "selected_cube_root": 7,
        "child_square": (child, 7),
        "gadget_endpoint": endpoint,
        "gadget_span": gadget.span,
        "period_code": gadget.period_code,
        "terminal": terminal(gadget),
        "missing_span_one_child_at_period_code_defect": 1,
        "local_profile": (profile[high], profile[source]),
        "root_word": selected_root,
    }


def main() -> None:
    print(
        {
            "Q21_external_edges": audit_q21(),
            "local_nonterminal_countermodel": audit_local_countermodel(),
        }
    )


if __name__ == "__main__":
    main()
