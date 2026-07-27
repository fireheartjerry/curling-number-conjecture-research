"""Exhaust small whole-cycle cap-ancestry equality graphs.

A cycle is encoded by primitive cap-root lengths ``r_i >= 2`` and
last-high distances ``1 <= d_i <= min(3, r_i)``.  Its lifted cap
coordinates obey

    c_{i+1} = c_i - d_i - r_{i+1}.

For winding ``w`` in a circular word of length ``n`` this gives

    sum_i (d_i + r_{i+1}) = w*n.

At each node the script imposes the root-r_i square ending at c_i, the
root-r_{i+1} cube ending at c_i-d_i, the high label 3 there, and all
low labels through c_i.  It retains only the necessary root transition
split

    r_{i+1} > r_i
    or
    r_i > 2*r_{i+1} + gcd(r_i, r_{i+1}).

No other fixed-profile equation is imposed.  A genuine circular
cap-ancestry cycle in the searched range would therefore give one of
these equality graphs.  The exhaustive result below says that every
such graph already identifies a forced 2-coordinate with a forced
3-coordinate.
"""

from __future__ import annotations

from collections import deque
from itertools import product
from math import gcd

from check_run_length_grammar import (
    primitive,
    proper_profile,
    word_power_root_lengths,
)


ROOT_MIN = 2
ROOT_MAX = 12
MIN_CYCLE_LENGTH = 2
MAX_CYCLE_LENGTH = 5


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, value: int) -> int:
        value %= len(self.parent)
        root = value
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[value] != value:
            value, self.parent[value] = self.parent[value], root
        return root

    def union(self, left: int, right: int) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root != right_root:
            self.parent[right_root] = left_root


def admissible_scale_edge(parent: int, child: int) -> bool:
    return (
        child > parent
        or parent > 2 * child + gcd(parent, child)
    )


def windings(total_fall: int, largest_root: int) -> tuple[int, ...]:
    return tuple(
        winding
        for winding in range(1, total_fall // largest_root + 1)
        if total_fall % winding == 0
        and total_fall // winding > largest_root
    )


def label_compatible(
    roots: tuple[int, ...],
    distances: tuple[int, ...],
    winding: int,
) -> bool:
    total_fall = sum(roots) + sum(distances)
    assert total_fall % winding == 0
    period = total_fall // winding
    assert period > max(roots)

    union_find = UnionFind(period)
    caps = [0]
    for index, parent_root in enumerate(roots):
        child_root = roots[(index + 1) % len(roots)]
        cap = caps[-1]
        high = cap - distances[index]

        for offset in range(parent_root):
            union_find.union(
                cap - 2 * parent_root + offset,
                cap - parent_root + offset,
            )
        for offset in range(child_root):
            union_find.union(
                high - 3 * child_root + offset,
                high - 2 * child_root + offset,
            )
            union_find.union(
                high - 2 * child_root + offset,
                high - child_root + offset,
            )
        caps.append(high - child_root)

    assert caps[-1] % period == 0

    forced: dict[int, int] = {}

    def force(coordinate: int, value: int) -> bool:
        component = union_find.find(coordinate)
        prior = forced.get(component)
        if prior is not None and prior != value:
            return False
        forced[component] = value
        return True

    for index, cap in enumerate(caps[:-1]):
        high = cap - distances[index]
        if not force(high, 3):
            return False
        for coordinate in range(high + 1, cap + 1):
            if not force(coordinate, 2):
                return False
    return True


def contradiction_certificate(
    roots: tuple[int, ...],
    distances: tuple[int, ...],
    winding: int,
) -> dict[str, object]:
    """Return a shortest explicit equality path from a high to a low.

    This is a diagnostic companion to ``label_compatible``.  Each edge
    records the actual lifted equality which generated the corresponding
    edge between residues modulo the ambient period.
    """
    total_fall = sum(roots) + sum(distances)
    assert total_fall % winding == 0
    period = total_fall // winding
    assert period > max(roots)
    size = len(roots)

    adjacency: list[list[tuple[int, dict[str, object]]]] = [
        [] for _ in range(period)
    ]

    def add_equality(
        left: int,
        right: int,
        source: str,
        node: int,
        root: int,
    ) -> None:
        left_residue = left % period
        right_residue = right % period
        record: dict[str, object] = {
            "source": source,
            "node": node,
            "root": root,
            "lifted_equality": (left, right),
            "residue_equality": (left_residue, right_residue),
        }
        adjacency[left_residue].append((right_residue, record))
        adjacency[right_residue].append((left_residue, record))

    caps = [0]
    highs: list[int] = []
    lows: list[tuple[int, int]] = []
    for index, parent_root in enumerate(roots):
        child_root = roots[(index + 1) % size]
        cap = caps[-1]
        high = cap - distances[index]
        highs.append(high)
        lows.extend((coordinate, index) for coordinate in range(high + 1, cap + 1))

        for offset in range(parent_root):
            add_equality(
                cap - 2 * parent_root + offset,
                cap - parent_root + offset,
                "square",
                index,
                parent_root,
            )
        for offset in range(child_root):
            add_equality(
                high - 3 * child_root + offset,
                high - 2 * child_root + offset,
                "cube copies 1=2",
                index,
                child_root,
            )
            add_equality(
                high - 2 * child_root + offset,
                high - child_root + offset,
                "cube copies 2=3",
                index,
                child_root,
            )
        caps.append(high - child_root)

    assert caps[-1] % period == 0

    low_by_residue: dict[int, tuple[int, int]] = {}
    for coordinate, node in lows:
        low_by_residue.setdefault(coordinate % period, (coordinate, node))

    queue: deque[int] = deque()
    predecessor: dict[int, tuple[int, dict[str, object]] | None] = {}
    origin: dict[int, tuple[int, int]] = {}
    for node, coordinate in enumerate(highs):
        residue = coordinate % period
        if residue not in predecessor:
            predecessor[residue] = None
            origin[residue] = (coordinate, node)
            queue.append(residue)

    target: int | None = None
    while queue:
        residue = queue.popleft()
        if residue in low_by_residue:
            target = residue
            break
        for neighbor, record in adjacency[residue]:
            if neighbor in predecessor:
                continue
            predecessor[neighbor] = (residue, record)
            origin[neighbor] = origin[residue]
            queue.append(neighbor)

    assert target is not None
    path_residues = [target]
    path_equalities: list[dict[str, object]] = []
    cursor = target
    while predecessor[cursor] is not None:
        prior, record = predecessor[cursor]
        path_equalities.append(record)
        path_residues.append(prior)
        cursor = prior
    path_residues.reverse()
    path_equalities.reverse()

    high_coordinate, high_node = origin[target]
    low_coordinate, low_node = low_by_residue[target]
    return {
        "roots": roots,
        "distances": distances,
        "winding": winding,
        "period": period,
        "caps": tuple(caps[:-1]),
        "highs": tuple(highs),
        "forced_high": {
            "node": high_node,
            "coordinate": high_coordinate,
            "residue": high_coordinate % period,
        },
        "forced_low": {
            "node": low_node,
            "coordinate": low_coordinate,
            "residue": low_coordinate % period,
        },
        "path_residues": tuple(path_residues),
        "equalities": tuple(path_equalities),
    }


def audit_q21() -> dict[str, int]:
    """Check that the exact length-21 profile has no cap-ancestry cycle."""
    word = tuple(map(int, "223222322232322232223"))
    size = len(word)
    assert primitive(word)
    assert proper_profile(word) == word

    vertices = {
        (cut, root)
        for cut, value in enumerate(word)
        if value == 2
        for root in word_power_root_lengths(word, cut, 2)
    }
    edges: dict[tuple[int, int], tuple[tuple[int, int], ...]] = {}
    for cut, root in vertices:
        distances = tuple(
            distance
            for distance in range(1, root + 1)
            if word[(cut - distance) % size] == 3
        )
        if not distances:
            edges[cut, root] = ()
            continue
        high = (cut - distances[0]) % size
        children = tuple(
            ((high - child_root) % size, child_root)
            for child_root in word_power_root_lengths(word, high, 3)
        )
        assert all(child in vertices for child in children)
        edges[cut, root] = children

    color: dict[tuple[int, int], int] = {
        vertex: 0 for vertex in vertices
    }

    def visit(vertex: tuple[int, int]) -> None:
        color[vertex] = 1
        for child in edges[vertex]:
            if color[child] == 1:
                raise AssertionError(("Q21 cap cycle", vertex, child))
            if color[child] == 0:
                visit(child)
        color[vertex] = 2

    for vertex in vertices:
        if color[vertex] == 0:
            visit(vertex)

    return {
        "vertices": len(vertices),
        "edges": sum(map(len, edges.values())),
        "directed_cycles": 0,
    }


def main() -> None:
    counts: dict[int, dict[str, int]] = {}
    for cycle_length in range(
        MIN_CYCLE_LENGTH,
        MAX_CYCLE_LENGTH + 1,
    ):
        root_tuples = 0
        distance_tuples = 0
        winding_graphs = 0
        compatible_graphs = 0

        for roots in product(
            range(ROOT_MIN, ROOT_MAX + 1),
            repeat=cycle_length,
        ):
            if roots[0] != min(roots):
                continue
            if not all(
                admissible_scale_edge(
                    roots[index],
                    roots[(index + 1) % cycle_length],
                )
                for index in range(cycle_length)
            ):
                continue
            root_tuples += 1

            distance_ranges = tuple(
                range(1, min(3, root) + 1)
                for root in roots
            )
            for distances in product(*distance_ranges):
                distance_tuples += 1
                total_fall = sum(roots) + sum(distances)
                for winding in windings(total_fall, max(roots)):
                    winding_graphs += 1
                    if label_compatible(roots, distances, winding):
                        compatible_graphs += 1
                        raise AssertionError(
                            (
                                "compatible cap-ancestry cycle",
                                roots,
                                distances,
                                winding,
                            )
                        )

        counts[cycle_length] = {
            "root_tuples": root_tuples,
            "distance_tuples": distance_tuples,
            "winding_graphs": winding_graphs,
            "compatible_graphs": compatible_graphs,
        }

    print(
        {
            "root_range": (ROOT_MIN, ROOT_MAX),
            "cycle_length_range": (
                MIN_CYCLE_LENGTH,
                MAX_CYCLE_LENGTH,
            ),
            "counts": counts,
            "representative_certificates": tuple(
                contradiction_certificate(
                    roots,
                    (1,) * len(roots),
                    1,
                )
                for roots in (
                    (2, 7),
                    (2, 3, 7),
                    (2, 3, 4, 7),
                    (2, 3, 4, 5, 7),
                )
            ),
            "q21_audit": audit_q21(),
        }
    )


if __name__ == "__main__":
    main()
