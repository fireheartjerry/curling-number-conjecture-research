"""Extract shortest 2--3 equality paths in cap-ancestry cycle graphs.

This is exploratory: it records which cube-period edges witness the
contradiction in small parameter instances.  It does not perform any curling
number computation.
"""

from __future__ import annotations

from collections import deque
from itertools import islice, product
from math import gcd

from check_cap_ancestry_cycle_graph import (
    admissible_scale_edge,
    windings,
)


def shortest_collision_path(
    roots: tuple[int, ...],
    distances: tuple[int, ...],
    winding: int,
) -> dict[str, object] | None:
    total_fall = sum(roots) + sum(distances)
    period = total_fall // winding
    graph: list[list[tuple[int, tuple[int, int]]]] = [
        [] for _ in range(period)
    ]
    caps = [0]

    def add_edge(left: int, right: int, witness: tuple[int, int]) -> None:
        left %= period
        right %= period
        graph[left].append((right, witness))
        graph[right].append((left, witness))

    for index, parent_root in enumerate(roots):
        child_root = roots[(index + 1) % len(roots)]
        cap = caps[-1]
        high = cap - distances[index]

        # The square is contained in the incoming parent cube and is therefore
        # redundant.  Keep all three child-cube copy equalities, labelled by
        # (node, root).
        for offset in range(child_root):
            left = high - 3 * child_root + offset
            middle = high - 2 * child_root + offset
            right = high - child_root + offset
            add_edge(left, middle, (index + 1, child_root))
            add_edge(middle, right, (index + 1, child_root))
        caps.append(high - child_root)

    forced_two: set[int] = set()
    forced_three: set[int] = set()
    for index, cap in enumerate(caps[:-1]):
        high = cap - distances[index]
        forced_three.add(high % period)
        forced_two.update(
            coordinate % period
            for coordinate in range(high + 1, cap + 1)
        )

    queue = deque(forced_three)
    predecessor: dict[int, tuple[int, tuple[int, int]] | None] = {
        vertex: None for vertex in forced_three
    }
    source: dict[int, int] = {vertex: vertex for vertex in forced_three}
    target = next((vertex for vertex in queue if vertex in forced_two), None)
    while queue and target is None:
        current = queue.popleft()
        for nxt, witness in graph[current]:
            if nxt in predecessor:
                continue
            predecessor[nxt] = (current, witness)
            source[nxt] = source[current]
            if nxt in forced_two:
                target = nxt
                break
            queue.append(nxt)

    if target is None:
        return None

    edges: list[tuple[int, int]] = []
    vertices = [target]
    current = target
    while predecessor[current] is not None:
        prior, witness = predecessor[current]
        edges.append(witness)
        vertices.append(prior)
        current = prior
    vertices.reverse()
    edges.reverse()
    return {
        "roots": roots,
        "distances": distances,
        "winding": winding,
        "period": period,
        "source_three": source[target],
        "target_two": target,
        "vertices": tuple(vertices),
        "edge_witnesses": tuple(edges),
        "path_length": len(edges),
        "distinct_cube_nodes": len({node for node, _ in edges}),
    }


def main() -> None:
    records: list[dict[str, object]] = []
    for cycle_length in range(2, 6):
        for roots in product(range(2, 13), repeat=cycle_length):
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
            distance_ranges = tuple(
                range(1, min(3, root) + 1) for root in roots
            )
            for distances in product(*distance_ranges):
                total_fall = sum(roots) + sum(distances)
                for winding in windings(total_fall, max(roots)):
                    record = shortest_collision_path(
                        roots, distances, winding
                    )
                    if record is None:
                        raise AssertionError(
                            ("compatible graph", roots, distances, winding)
                        )
                    records.append(record)

    histogram: dict[tuple[int, int], int] = {}
    by_winding: dict[int, dict[int, int]] = {}
    by_cycle_length: dict[int, dict[int, int]] = {}
    for record in records:
        key = (
            int(record["path_length"]),
            int(record["distinct_cube_nodes"]),
        )
        histogram[key] = histogram.get(key, 0) + 1
        winding = int(record["winding"])
        path_length = int(record["path_length"])
        by_winding.setdefault(winding, {})[path_length] = (
            by_winding.setdefault(winding, {}).get(path_length, 0) + 1
        )
        cycle_length = len(record["roots"])
        by_cycle_length.setdefault(cycle_length, {})[path_length] = (
            by_cycle_length.setdefault(cycle_length, {}).get(path_length, 0)
            + 1
        )

    longest = sorted(
        records,
        key=lambda record: (
            int(record["path_length"]),
            int(record["distinct_cube_nodes"]),
        ),
        reverse=True,
    )
    print(
        {
            "instances": len(records),
            "path_histogram": dict(sorted(histogram.items())),
            "by_winding": {
                winding: dict(sorted(counts.items()))
                for winding, counts in sorted(by_winding.items())
            },
            "by_cycle_length": {
                cycle_length: dict(sorted(counts.items()))
                for cycle_length, counts in sorted(by_cycle_length.items())
            },
            "longest_examples": tuple(islice(longest, 20)),
        }
    )


if __name__ == "__main__":
    main()
