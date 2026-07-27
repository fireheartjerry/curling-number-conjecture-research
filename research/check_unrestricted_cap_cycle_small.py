"""Exhaust small cap-cycle equality graphs without the root-scale split.

This is deliberately a larger necessary-condition superfamily than
``check_cap_ancestry_cycle_graph.py``: every root transition is accepted.
It performs no curling-number computation.
"""

from __future__ import annotations

from itertools import product

from check_cap_ancestry_cycle_graph import label_compatible, windings


ROOT_MIN = 2
ROOT_MAX = 7
MIN_CYCLE_LENGTH = 2
MAX_CYCLE_LENGTH = 5


def main() -> None:
    counts: dict[int, int] = {}
    compatible = 0
    for cycle_length in range(
        MIN_CYCLE_LENGTH,
        MAX_CYCLE_LENGTH + 1,
    ):
        tested = 0
        for roots in product(
            range(ROOT_MIN, ROOT_MAX + 1),
            repeat=cycle_length,
        ):
            # Remove cyclic duplicates but retain tuples with repeated minima.
            if roots[0] != min(roots):
                continue
            distance_ranges = tuple(
                range(1, min(3, root) + 1) for root in roots
            )
            for distances in product(*distance_ranges):
                total_fall = sum(roots) + sum(distances)
                for winding in windings(total_fall, max(roots)):
                    tested += 1
                    if label_compatible(roots, distances, winding):
                        compatible += 1
                        raise AssertionError(
                            (
                                "compatible unrestricted cap cycle",
                                roots,
                                distances,
                                winding,
                            )
                        )
        counts[cycle_length] = tested

    print(
        {
            "root_range": (ROOT_MIN, ROOT_MAX),
            "cycle_length_range": (
                MIN_CYCLE_LENGTH,
                MAX_CYCLE_LENGTH,
            ),
            "winding_graphs_by_length": counts,
            "winding_graphs_total": sum(counts.values()),
            "compatible_graphs": compatible,
        }
    )


if __name__ == "__main__":
    main()
