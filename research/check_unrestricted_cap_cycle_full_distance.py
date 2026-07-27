"""Exhaust small cap cycles with the full distance range 1<=d_i<=r_i.

No root-scale transition condition is imposed.  This is a finite audit of
the unrestricted cyclic equality lemma; it performs no curling-number
computation.
"""

from __future__ import annotations

from itertools import product

from check_cap_ancestry_cycle_graph import label_compatible, windings


ROOT_MIN = 2
ROOT_MAX = 5
MIN_CYCLE_LENGTH = 1
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
            if roots[0] != min(roots):
                continue
            for distances in product(
                *(range(1, root + 1) for root in roots)
            ):
                total_fall = sum(roots) + sum(distances)
                for winding in windings(total_fall, max(roots)):
                    tested += 1
                    if label_compatible(roots, distances, winding):
                        compatible += 1
                        raise AssertionError(
                            (
                                "compatible full-distance cap cycle",
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
            "distance_rule": "1<=d_i<=r_i",
            "winding_graphs_by_length": counts,
            "winding_graphs_total": sum(counts.values()),
            "compatible_graphs": compatible,
        }
    )


if __name__ == "__main__":
    main()
