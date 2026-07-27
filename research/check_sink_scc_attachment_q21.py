"""Exact Q21 counterexample to single-container SCC attachment.

Run the A094004 calibration test before this script.  Every power root,
profile value, fitting inequality, SCC, lifted edge, and interval relation
used by ``sink_scc_attachment.md`` is recomputed here.
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
Interval = tuple[int, int]


def descendants(
    start: Vertex,
    adjacency: dict[Vertex, set[Vertex]],
) -> set[Vertex]:
    seen: set[Vertex] = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex in seen:
            continue
        seen.add(vertex)
        stack.extend(adjacency[vertex] - seen)
    return seen


def strongly_connected_components(
    vertices: set[Vertex],
    adjacency: dict[Vertex, set[Vertex]],
) -> tuple[frozenset[Vertex], ...]:
    reach = {
        vertex: descendants(vertex, adjacency)
        for vertex in vertices
    }
    remaining = set(vertices)
    components: list[frozenset[Vertex]] = []
    while remaining:
        seed = min(remaining)
        component = frozenset(
            vertex
            for vertex in remaining
            if vertex in reach[seed] and seed in reach[vertex]
        )
        assert component
        components.append(component)
        remaining.difference_update(component)
    return tuple(sorted(components, key=lambda component: min(component)))


def contained(inner: Interval, outer: Interval) -> bool:
    return outer[0] <= inner[0] and inner[1] <= outer[1]


def overlap_length(left: Interval, right: Interval) -> int:
    return max(0, min(left[1], right[1]) - max(left[0], right[0]))


def main() -> None:
    word = Q21
    size = len(word)
    assert size == 21
    assert primitive(word)
    assert proper_profile(word) == word

    vertices, edge_records = extended_fitting_ancestry(word)
    adjacency = {
        vertex: {record[:2] for record in records}
        for vertex, records in edge_records.items()
    }
    components = strongly_connected_components(vertices, adjacency)
    sink_components = tuple(
        component
        for component in components
        if all(
            child in component
            for vertex in component
            for child in adjacency[vertex]
        )
    )

    expected_cycle = (
        (5, 1),
        (19, 4),
        (15, 1),
        (8, 4),
    )
    expected_component = frozenset(expected_cycle)
    assert directed_cycles(vertices, edge_records) == {expected_cycle}
    assert sink_components == (expected_component,)

    fitting_cubes = tuple(
        (cut, root)
        for cut, value in enumerate(word)
        if value == 3
        for root in word_power_root_lengths(word, cut, 3)
        if fitting(word, cut, 3, root)
    )
    maximum_root = max(root for _, root in fitting_cubes)
    maximum_cubes = tuple(
        record for record in fitting_cubes if record[1] == maximum_root
    )
    assert maximum_root == 4
    assert maximum_cubes == ((2, 4), (12, 4))

    # The midpoint squares of both globally maximal fitting cubes belong to
    # the unique sink SCC.
    midpoint_vertices = tuple(
        ((cut - root) % size, root)
        for cut, root in maximum_cubes
    )
    assert midpoint_vertices == ((19, 4), (8, 4))
    assert all(vertex in expected_component for vertex in midpoint_vertices)

    lifted_caps = (5, -2, -6, -13, -16)
    lifted_records: list[dict[str, object]] = []
    for index, parent in enumerate(expected_cycle):
        parent_lift = lifted_caps[index]
        child_lift = lifted_caps[index + 1]
        record = edge_records[parent][0]
        child, child_root, distance, canonical_high = record
        high = parent_lift - distance
        assert high % size == canonical_high
        assert child_lift == high - child_root
        assert child_lift % size == child
        cube_interval = (high - 3 * child_root, high)
        assert fitting(word, canonical_high, 3, child_root)
        lifted_records.append(
            {
                "parent": parent,
                "parent_lift": parent_lift,
                "child": (child, child_root),
                "child_lift": child_lift,
                "distance": distance,
                "high": high,
                "cube_root": child_root,
                "cube_interval": cube_interval,
            }
        )

    first_maximum = lifted_records[0]["cube_interval"]
    first_descent = lifted_records[1]["cube_interval"]
    second_maximum = lifted_records[2]["cube_interval"]
    second_descent = lifted_records[3]["cube_interval"]
    assert isinstance(first_maximum, tuple)
    assert isinstance(first_descent, tuple)
    assert isinstance(second_maximum, tuple)
    assert isinstance(second_descent, tuple)
    assert first_maximum == (-10, 2)
    assert first_descent == (-8, -5)
    assert second_maximum == (-21, -9)
    assert second_descent == (-18, -15)

    # Each root-one descent is contained in its immediately preceding
    # maximum cube, but the external reset creates a second maximum cube
    # outside the first common lift.
    assert contained(first_descent, first_maximum)
    assert contained(second_descent, second_maximum)
    assert not contained(second_maximum, first_maximum)
    assert not contained(first_maximum, second_maximum)
    assert overlap_length(first_maximum, second_maximum) == 1

    print(
        {
            "word": "".join(map(str, word)),
            "vertices": len(vertices),
            "scc_count": len(components),
            "sink_scc": tuple(sorted(expected_component)),
            "globally_maximal_fitting_cubes": maximum_cubes,
            "midpoint_vertices": midpoint_vertices,
            "lifted_cycle_records": tuple(lifted_records),
            "first_maximum_interval": first_maximum,
            "second_maximum_interval": second_maximum,
            "maximum_interval_overlap": overlap_length(
                first_maximum, second_maximum
            ),
            "single_container_attachment": False,
        }
    )


if __name__ == "__main__":
    main()
