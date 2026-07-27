"""Audit the extended fitting cap-ancestry cycle of Q21.

Unlike the earlier square-ancestry graph, this graph continues through a
root-one square whose one-symbol root is 2.  Its nearest preceding high is
then three cuts away.  This script performs no finite curling-number
computation; it recomputes the proper circular profile and all power roots.
"""

from __future__ import annotations

from check_max_square_terminal_forest import (
    directed_cycles,
    fitting,
)
from check_run_length_grammar import (
    primitive,
    proper_profile,
    word_power_root_lengths,
)


Q21 = tuple(map(int, "223222322232322232223"))


def extended_fitting_ancestry(
    word: tuple[int, ...],
) -> tuple[
    set[tuple[int, int]],
    dict[tuple[int, int], tuple[tuple[int, int, int, int], ...]],
]:
    size = len(word)
    vertices = {
        (cut, root)
        for cut, value in enumerate(word)
        if value == 2
        for root in word_power_root_lengths(word, cut, 2)
        if fitting(word, cut, 2, root)
    }
    edges: dict[
        tuple[int, int],
        tuple[tuple[int, int, int, int], ...],
    ] = {}
    for cut, root in vertices:
        distance = next(
            distance
            for distance in range(1, 4)
            if word[(cut - distance) % size] == 3
        )
        high = (cut - distance) % size
        children = tuple(
            ((high - child_root) % size, child_root, distance, high)
            for child_root in word_power_root_lengths(word, high, 3)
            if fitting(word, high, 3, child_root)
        )
        assert children
        assert all(child[:2] in vertices for child in children)
        edges[cut, root] = children
    return vertices, edges


def main() -> None:
    word = Q21
    size = len(word)
    assert size == 21
    assert primitive(word)
    assert proper_profile(word) == word

    vertices, edges = extended_fitting_ancestry(word)
    cycles = directed_cycles(vertices, edges)
    expected_cycle = (
        (5, 1),
        (19, 4),
        (15, 1),
        (8, 4),
    )
    assert cycles == {expected_cycle}

    records = tuple(
        (
            expected_cycle[index],
            edges[expected_cycle[index]][0],
        )
        for index in range(len(expected_cycle))
    )
    assert tuple(record[1][2] for record in records) == (3, 3, 3, 2)
    assert tuple(record[1][1] for record in records) == (4, 1, 4, 1)

    lifted_caps = [expected_cycle[0][0]]
    for parent, child_record in records:
        child_cut, child_root, distance, _ = child_record
        lifted_caps.append(lifted_caps[-1] - distance - child_root)
        assert lifted_caps[-1] % size == child_cut
    assert tuple(lifted_caps) == (5, -2, -6, -13, -16)
    assert lifted_caps[-1] == lifted_caps[0] - size

    external_source_edges = tuple(
        (
            parent,
            child_record,
        )
        for parent, child_record in records
        if child_record[2] > parent[1]
    )
    assert tuple(parent for parent, _ in external_source_edges) == (
        (5, 1),
        (15, 1),
    )
    for (cut, root), child_record in external_source_edges:
        assert root == 1
        assert child_record[2] == 3
        assert tuple(
            word[(cut - offset) % size]
            for offset in (3, 2, 1, 0)
        ) == (3, 2, 2, 2)

    print(
        {
            "word": "".join(map(str, word)),
            "vertices": len(vertices),
            "edges": sum(map(len, edges.values())),
            "directed_cycles": tuple(cycles),
            "cycle_records": records,
            "lifted_caps": tuple(lifted_caps),
            "winding": 1,
            "root_one_2_external_source_edges": external_source_edges,
        }
    )


if __name__ == "__main__":
    main()
