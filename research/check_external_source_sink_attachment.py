"""Audit attachment versus containment for the exact Q21 sink SCC.

The Q21 extended fitting ancestry graph has a unique nontrivial sink SCC.
It is reached immediately as the midpoint square of either globally
maximal fitting cube.  Nevertheless, following the SCC does not remain in
one contained halving hierarchy: each root-one external edge selects a
new maximal cube outside its parent square.

Run the A094004 calibration before this script.  All profile and root data
are recomputed by the imported exact enumerators.
"""

from __future__ import annotations

from check_extended_cap_ancestry_q21 import (
    Q21,
    extended_fitting_ancestry,
)
from check_max_square_terminal_forest import (
    directed_cycles,
    fitting,
)
from check_run_length_grammar import (
    primitive,
    proper_profile,
    word_power_root_lengths,
)


Vertex = tuple[int, int]
Record = tuple[int, int, int, int]


def reachable(
    edges: dict[Vertex, tuple[Record, ...]],
    start: Vertex,
) -> set[Vertex]:
    pending = [start]
    seen: set[Vertex] = set()
    while pending:
        current = pending.pop()
        if current in seen:
            continue
        seen.add(current)
        pending.extend(record[:2] for record in edges[current])
    return seen


def main() -> None:
    word = Q21
    n = len(word)
    assert primitive(word)
    assert proper_profile(word) == word
    assert all(
        any(
            fitting(word, cut, exponent, root)
            for root in word_power_root_lengths(word, cut, exponent)
        )
        for cut, exponent in enumerate(word)
    )

    vertices, edges = extended_fitting_ancestry(word)
    cycle = (
        (5, 1),
        (19, 4),
        (15, 1),
        (8, 4),
    )
    assert directed_cycles(vertices, edges) == {cycle}
    component = set(cycle)
    assert all(
        record[:2] in component
        for vertex in component
        for record in edges[vertex]
    )
    assert all(
        component & reachable(edges, vertex)
        for vertex in vertices
    )

    fitting_cubes = tuple(
        (cut, root)
        for cut, value in enumerate(word)
        if value == 3
        for root in word_power_root_lengths(word, cut, 3)
        if fitting(word, cut, 3, root)
    )
    maximum_root = max(root for _, root in fitting_cubes)
    maximum_cubes = tuple(
        (cut, root)
        for cut, root in fitting_cubes
        if root == maximum_root
    )
    assert maximum_root == 4
    assert maximum_cubes == ((2, 4), (12, 4))
    midpoint_squares = tuple(
        ((cut - root) % n, root) for cut, root in maximum_cubes
    )
    assert midpoint_squares == ((19, 4), (8, 4))
    assert all(midpoint in component for midpoint in midpoint_squares)

    # Use the one-turn lift already fixed by the cap-cycle audit.
    lifted_caps = (5, -2, -6, -13, -16)
    edge_geometry: list[dict[str, object]] = []
    for index, parent in enumerate(cycle):
        record = edges[parent][0]
        child_cut, q, distance, high_mod = record
        c = lifted_caps[index]
        child_c = lifted_caps[index + 1]
        r = parent[1]
        high = c - distance
        assert high % n == high_mod
        assert child_c == high - q
        assert child_c % n == child_cut

        parent_square = (c - 2 * r, c)
        child_cube = (high - 3 * q, high)
        midpoint_square = (high - 3 * q, high - q)
        cube_contained_in_parent = (
            parent_square[0] <= child_cube[0]
            and child_cube[1] <= parent_square[1]
        )
        assert cube_contained_in_parent == (
            3 * q + distance <= 2 * r
        )
        assert midpoint_square[0] == child_cube[0]
        assert midpoint_square[1] == child_c
        edge_geometry.append(
            {
                "parent": parent,
                "lifted_parent_cap": c,
                "distance": distance,
                "selected_cube_root": q,
                "lifted_high": high,
                "parent_square_interval": parent_square,
                "selected_cube_interval": child_cube,
                "child_midpoint_square_interval": midpoint_square,
                "child": record[:2],
                "cube_contained_in_parent_square": cube_contained_in_parent,
            }
        )

    assert tuple(
        item["cube_contained_in_parent_square"]
        for item in edge_geometry
    ) == (False, True, False, True)
    assert tuple(
        item["selected_cube_root"] for item in edge_geometry
    ) == (4, 1, 4, 1)

    print(
        {
            "word": "".join(map(str, word)),
            "maximum_fitting_cubes": maximum_cubes,
            "their_midpoint_squares": midpoint_squares,
            "unique_sink_SCC": cycle,
            "all_vertices_reach_sink_SCC": True,
            "lifted_edge_geometry": tuple(edge_geometry),
            "conclusion": (
                "the sink SCC is attached directly to both maximum cubes, "
                "but each external root-one edge escapes its parent square"
            ),
        }
    )


if __name__ == "__main__":
    main()
