"""Audit counterexamples to short cap-cycle contradiction-path bounds.

This script performs no curling-number computation.  It reconstructs the
complete selected cube-equality graph modulo the proposed ambient period and
uses multi-source breadth-first search, so the reported distance is the exact
shortest number of equality edges from any forced high coordinate to any
forced low coordinate.
"""

from __future__ import annotations

from math import gcd

from check_cap_ancestry_cycle_graph import (
    admissible_scale_edge,
    contradiction_certificate,
    label_compatible,
)
from explore_cap_cycle_contradiction_paths import shortest_collision_path


def main() -> None:
    roots = (297, 359, 428, 650)
    distances = (1, 2, 1, 1)
    winding = 1
    period = (sum(roots) + sum(distances)) // winding

    assert period == 1739
    assert period > max(roots)
    assert all(
        admissible_scale_edge(
            roots[index],
            roots[(index + 1) % len(roots)],
        )
        for index in range(len(roots))
    )
    assert roots[-1] > 2 * roots[0] + gcd(roots[-1], roots[0])

    cube_only = shortest_collision_path(roots, distances, winding)
    assert cube_only is not None
    assert cube_only["path_length"] == 5
    assert cube_only["vertices"] == (1377, 1736, 647, 219, 1308, 949)
    assert cube_only["edge_witnesses"] == (
        (1, 359),
        (3, 650),
        (2, 428),
        (3, 650),
        (1, 359),
    )

    full_graph = contradiction_certificate(roots, distances, winding)
    assert len(full_graph["equalities"]) == 5
    assert not label_compatible(roots, distances, winding)

    longer_roots = (1629, 1936, 2299, 4691, 5132, 6266, 9979)
    longer_distances = (1, 1, 2, 2, 1, 1, 2)
    longer_period = sum(longer_roots) + sum(longer_distances)
    assert longer_period == 31942
    assert longer_period > max(longer_roots)
    assert all(
        admissible_scale_edge(
            longer_roots[index],
            longer_roots[(index + 1) % len(longer_roots)],
        )
        for index in range(len(longer_roots))
    )

    longer_cube_only = shortest_collision_path(
        longer_roots,
        longer_distances,
        1,
    )
    assert longer_cube_only is not None
    assert longer_cube_only["path_length"] == 7
    assert longer_cube_only["vertices"] == (
        23010,
        27701,
        25402,
        20711,
        15579,
        25558,
        27857,
        17878,
    )
    assert longer_cube_only["edge_witnesses"] == (
        (3, 4691),
        (2, 2299),
        (3, 4691),
        (4, 5132),
        (6, 9979),
        (2, 2299),
        (6, 9979),
    )

    longer_full_graph = contradiction_certificate(
        longer_roots,
        longer_distances,
        1,
    )
    assert len(longer_full_graph["equalities"]) == 7
    assert not label_compatible(longer_roots, longer_distances, 1)

    print(
        {
            "distance_five": {
                "roots": roots,
                "distances": distances,
                "winding": winding,
                "period": period,
                "scale_edges": tuple(
                    admissible_scale_edge(
                        roots[index],
                        roots[(index + 1) % len(roots)],
                    )
                    for index in range(len(roots))
                ),
                "cube_only_shortest_path": cube_only,
                "full_graph_shortest_length": len(full_graph["equalities"]),
            },
            "distance_seven": {
                "roots": longer_roots,
                "distances": longer_distances,
                "winding": 1,
                "period": longer_period,
                "scale_edges": tuple(
                    admissible_scale_edge(
                        longer_roots[index],
                        longer_roots[(index + 1) % len(longer_roots)],
                    )
                    for index in range(len(longer_roots))
                ),
                "cube_only_shortest_path": longer_cube_only,
                "full_graph_shortest_length": len(
                    longer_full_graph["equalities"]
                ),
            },
        }
    )


if __name__ == "__main__":
    main()
