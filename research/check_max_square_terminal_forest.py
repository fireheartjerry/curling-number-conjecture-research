"""Executed audits for the longest-square / last-cube lemma.

The mathematical proof is in ``max_square_terminal_forest.md``.  This
script is only a finite calibration.  It recomputes every displayed
power-root set, proper circular profile, and finite curling number.
"""

from __future__ import annotations

import sys
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from curling import curling_number, curling_number_reference

from check_run_length_grammar import (
    binary_word,
    primitive,
    proper_profile,
    word_power_root_lengths,
)


Word = tuple[int, ...]


def checked_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def fitting(word: Word, cut: int, exponent: int, root: int) -> bool:
    """First-copy fitting in the distinguished critical-word lift."""
    return exponent * root <= len(word) + cut - 1


def global_low_square_length(word: Word) -> int:
    roots = [
        root
        for cut, value in enumerate(word)
        if value == 2
        for root in word_power_root_lengths(word, cut, 2)
    ]
    assert roots
    return max(roots)


def last_high_data(word: Word, cut: int, root: int) -> dict[str, object]:
    """Return the closest preceding 3 and all cube roots at that phase."""
    n = len(word)
    distance = next(
        d for d in range(1, root + 1) if word[(cut - d) % n] == 3
    )
    high_cut = (cut - distance) % n
    cube_roots = word_power_root_lengths(word, high_cut, 3)
    return {
        "distance": distance,
        "high_cut": high_cut,
        "cube_roots": cube_roots,
        "fitting_cube_roots": tuple(
            q for q in cube_roots if fitting(word, high_cut, 3, q)
        ),
    }


def audit_escape_equality_graph(max_p: int = 200) -> None:
    """Check the period-p, period-(p-1) threshold-minus-one graph.

    On an interval of length ``2p-3`` all coordinates except ``p-2``
    must be in one equality component.  In particular the two endpoint
    coordinates ``p-3`` and ``p-1`` are equal.
    """

    for p in range(3, max_p + 1):
        length = 2 * p - 3
        parent = list(range(length))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            x, y = find(x), find(y)
            if x != y:
                parent[y] = x

        for period in (p, p - 1):
            for i in range(length - period):
                union(i, i + period)

        components: dict[int, set[int]] = {}
        for i in range(length):
            components.setdefault(find(i), set()).add(i)
        component_sets = {frozenset(component) for component in components.values()}
        assert component_sets == {
            frozenset({p - 2}),
            frozenset(set(range(length)) - {p - 2}),
        }
        assert find(p - 3) == find(p - 1)


def fitting_square_ancestry(
    word: Word,
) -> tuple[
    set[tuple[int, int]],
    dict[tuple[int, int], tuple[tuple[int, int, int, int], ...]],
]:
    """Construct every edge of the fitting square-ancestry graph.

    An edge record is ``(child_cut, child_root, distance, high_cut)``.
    """

    n = len(word)
    vertices = {
        (cut, root)
        for cut, value in enumerate(word)
        if value == 2
        for root in word_power_root_lengths(word, cut, 2)
        if fitting(word, cut, 2, root)
    }
    edges: dict[
        tuple[int, int], tuple[tuple[int, int, int, int], ...]
    ] = {}
    for cut, root in vertices:
        distances = tuple(
            d
            for d in range(1, root + 1)
            if word[(cut - d) % n] == 3
        )
        if not distances:
            edges[cut, root] = ()
            continue
        distance = distances[0]
        high_cut = (cut - distance) % n
        children = tuple(
            ((high_cut - q) % n, q, distance, high_cut)
            for q in word_power_root_lengths(word, high_cut, 3)
            if fitting(word, high_cut, 3, q)
        )
        assert all(child[:2] in vertices for child in children)
        edges[cut, root] = children
    return vertices, edges


def directed_cycles(
    vertices: set[tuple[int, int]],
    edges: dict[tuple[int, int], tuple[tuple[int, int, int, int], ...]],
) -> set[tuple[tuple[int, int], ...]]:
    """Enumerate simple directed cycles; used only on the Q21 audit."""

    cycles: set[tuple[tuple[int, int], ...]] = set()

    def canonical(path: list[tuple[int, int]]) -> tuple[tuple[int, int], ...]:
        rotations = tuple(
            tuple(path[i:] + path[:i]) for i in range(len(path))
        )
        return min(rotations)

    def visit(
        start: tuple[int, int],
        current: tuple[int, int],
        path: list[tuple[int, int]],
    ) -> None:
        for record in edges[current]:
            child = record[:2]
            if child == start:
                cycles.add(canonical(path))
            elif child not in path:
                visit(start, child, path + [child])

    for vertex in vertices:
        visit(vertex, vertex, [vertex])
    return cycles


def audit_q21() -> dict[str, object]:
    word = tuple(map(int, "223222322232322232223"))
    n = len(word)
    assert primitive(word)
    assert proper_profile(word) == word

    # Recompute the full critical first-copy fitting condition.
    assert all(
        any(
            fitting(word, cut, value, root)
            for root in word_power_root_lengths(word, cut, value)
        )
        for cut, value in enumerate(word)
    )

    p = global_low_square_length(word)
    maximal_cuts = tuple(
        cut
        for cut, value in enumerate(word)
        if value == 2
        and p in word_power_root_lengths(word, cut, 2)
    )
    assert p == 10
    assert maximal_cuts == (0, 1)

    records = []
    for cut in maximal_cuts:
        data = last_high_data(word, cut, p)
        assert data["cube_roots"] == (1,)
        q = 1
        d = int(data["distance"])
        assert p > 2 * q + gcd(p, q)
        assert 3 * q + d <= 2 * p
        assert fitting(word, cut, 2, p)
        records.append((cut, data))

    # Every critical Q21 rotation whose first symbol is 2 also has the
    # terminal-prefix equality.  Both finite curling implementations
    # recompute these values.
    prefix_records = []
    for shift in range(n):
        rotation = word[shift:] + word[:shift]
        if rotation[0] != 2:
            continue
        assert proper_profile(rotation) == rotation
        assert all(
            any(
                fitting(rotation, cut, value, root)
                for root in word_power_root_lengths(rotation, cut, value)
            )
            for cut, value in enumerate(rotation)
        )
        prefix_value = checked_cn(rotation[:-1])
        assert prefix_value == rotation[-1]
        prefix_records.append((shift, prefix_value, rotation[-1]))
    assert len(prefix_records) == 15

    vertices, edges = fitting_square_ancestry(word)
    assert len(vertices) == 22
    assert sum(map(len, edges.values())) == 18
    assert directed_cycles(vertices, edges) == set()

    # Full critical fitting does not make root length decrease at every
    # edge and does not make the ancestry an arborescence.
    assert edges[3, 3] == ((19, 4, 1, 2),)
    assert edges[4, 3] == ((19, 4, 2, 2),)
    assert edges[5, 3] == ((19, 4, 3, 2),)
    parents_of_19_4 = tuple(
        vertex
        for vertex, children in edges.items()
        if any(child[:2] == (19, 4) for child in children)
    )
    assert set(parents_of_19_4) == {(3, 3), (4, 3), (5, 3)}

    return {
        "word": "".join(map(str, word)),
        "global_low_square_length": p,
        "maximal_cuts": maximal_cuts,
        "last_high_records": tuple(records),
        "terminal_prefix_rotations": tuple(prefix_records),
        "fitting_ancestry_vertices": len(vertices),
        "fitting_ancestry_edges": sum(map(len, edges.values())),
        "fitting_ancestry_cycles": (),
        "root_ascent": ((3, 3), (19, 4)),
        "multiple_parents_of_19_4": parents_of_19_4,
    }


def audit_q64() -> dict[str, object]:
    q21 = binary_word(tuple(map(int, "133233")))
    bridge_root = q21[16:] + q21[:16]
    raw = bridge_root * 3 + (3,)
    word = raw[1:] + raw[:1]
    profile = proper_profile(word)
    assert len(word) == 64
    assert primitive(word)
    assert tuple(
        cut for cut, (actual, target) in enumerate(zip(profile, word))
        if actual != target
    ) == (1, 5, 10)

    p = global_low_square_length(word)
    maximal_cuts = tuple(
        cut
        for cut, value in enumerate(word)
        if value == 2
        and p in word_power_root_lengths(word, cut, 2)
    )
    assert p == 43
    assert maximal_cuts == (42,)
    data = last_high_data(word, 42, p)
    assert data["distance"] == 1
    assert data["high_cut"] == 41
    assert data["cube_roots"] == (1,)
    assert profile[42] == word[42] == 2
    assert profile[41] == word[41] == 3
    assert p > 2 * 1 + gcd(p, 1)
    assert 3 + int(data["distance"]) <= 2 * p

    return {
        "word_length": len(word),
        "profile_mismatch_cuts": (1, 5, 10),
        "global_low_square_length": p,
        "maximal_cuts": maximal_cuts,
        "last_high_record": data,
    }


def main() -> None:
    audit_escape_equality_graph()
    print("Q21", audit_q21())
    print("Q64", audit_q64())
    print("escape equality graph audited for 3 <= p <= 200")


if __name__ == "__main__":
    main()
