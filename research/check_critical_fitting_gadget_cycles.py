"""Audit the critical fitting condition on tight-gadget cycles.

The two examples separate the three global requirements which are
simultaneously available in an exact singleton-3 fixed profile:

* positive cube coverage at every defect;
* square coverage at every 2-cut; and
* exclusion of cubes at every 2-cut.

All power data below are recomputed directly in the expanded binary
word.  No displayed curling-number or root value is hand evaluated.
"""

from __future__ import annotations

from check_run_length_grammar import (
    binary_word,
    direct_power_root_lengths,
    primitive,
)
from explore_gadget_cycles import (
    cycle_winding,
    defect_graph,
    directed_cycles,
    exact_negative_constraints,
    perfect_matchings,
    wsq_holes,
)


A15 = tuple(map(int, "233133133233133"))
A24 = tuple(map(int, "122133122133233122133233"))


def fitting(m: int, endpoint: int, span: int) -> bool:
    """Code form of first-deleted-copy containment."""
    return 3 * span <= m + endpoint - 1


def all_square_holes(a: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    """Every (run, offset) 2-cut with no proper circular square."""
    return tuple(
        (i, r)
        for i, run in enumerate(a)
        for r in range(run)
        if not direct_power_root_lengths(a, i, r, 2)
    )


def selected_cycle(
    a: tuple[int, ...],
    choices: dict[int, int],
) -> dict[int, tuple[int, int, int]]:
    """Resolve endpoint/span choices against the exact gadget graph."""
    graph = defect_graph(a)
    selected: dict[int, tuple[int, int, int]] = {}
    for endpoint, span in choices.items():
        hits = tuple(edge for edge in graph[endpoint] if edge[1] == span)
        assert len(hits) == 1
        selected[endpoint] = hits[0]
    return selected


def audit_a15() -> None:
    a = A15
    assert primitive(a)
    matching = selected_cycle(
        a,
        {
            0: 1,
            12: 1,
            9: 1,
            6: 6,
            3: 1,
        },
    )
    assert set(matching) == set(defect_graph(a))
    assert all(fitting(len(a), i, edge[1]) for i, edge in matching.items())
    cycles = directed_cycles(matching)
    assert cycles == ((0, 12, 9, 6, 3),)
    assert cycle_winding(a, matching, cycles[0]) == 2
    assert wsq_holes(a) == ()
    assert all_square_holes(a) == ()

    # The long edge is the unique g=2 edge in the selected cycle.
    assert matching[6] == (3, 6, 2)
    assert all(
        edge[2] == 3
        for endpoint, edge in matching.items()
        if endpoint != 6
    )

    # Direct binary enumeration finds the exact negative obstruction.
    q = binary_word(a)
    bad = tuple(
        (i, r, direct_power_root_lengths(a, i, r, 3))
        for i, run in enumerate(a)
        for r in range(run)
        if direct_power_root_lengths(a, i, r, 3)
    )
    assert bad == ((9, 0, (10,)), (9, 1, (10,)))
    assert not exact_negative_constraints(a)
    print(
        "A15: primitive, every defect selected, every selected edge fitting, "
        "WSQ complete, winding=2"
    )
    print(f"A15 expanded length={len(q)}; forbidden 2-cut cubes={bad}")


def audit_a24() -> None:
    a = A24
    assert primitive(a)
    matching = selected_cycle(
        a,
        {
            0: 1,
            21: 1,
            18: 1,
            15: 1,
            12: 1,
            9: 1,
            6: 9,
            3: 1,
        },
    )
    assert all(fitting(len(a), i, edge[1]) for i, edge in matching.items())
    cycles = directed_cycles(matching)
    assert cycles == ((0, 21, 18, 15, 12, 9, 6, 3),)
    assert cycle_winding(a, matching, cycles[0]) == 2
    assert exact_negative_constraints(a)

    graph = defect_graph(a)
    uncovered = tuple(i for i, value in enumerate(a) if value < 3 and not graph[i])
    holes = wsq_holes(a)
    all_holes = all_square_holes(a)
    assert uncovered
    assert holes
    assert all_holes == ((8, 0), (17, 0))
    print(
        "A24: primitive, selected fitting winding=2 cycle, "
        "no forbidden cube at a 2-cut"
    )
    print(
        f"A24 uncovered defects={uncovered}; "
        f"square holes={all_holes}"
    )


def main() -> None:
    audit_a15()
    audit_a24()


if __name__ == "__main__":
    main()
