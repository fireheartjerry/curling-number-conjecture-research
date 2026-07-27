"""Enumerate small extended fitting cap-cycle equality systems.

This is exploratory finite evidence.  Root-one square nodes may use distance
one (root symbol 3) or the terminal external distance three (root symbol 2).
All other nodes use 1 <= d <= min(3, r).  The script tests the exact selected
square/cube equalities and forced high/low labels, but deliberately does not
impose the full proper-profile equation at unselected cuts.
"""

from __future__ import annotations

import argparse
from itertools import product

from check_cap_ancestry_cycle_graph import label_compatible, windings


def distance_options(root: int) -> tuple[int, ...]:
    if root == 1:
        return (1, 3)
    return tuple(range(1, min(3, root) + 1))


def canonical_rotation(
    roots: tuple[int, ...], distances: tuple[int, ...]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    pairs = tuple(zip(roots, distances))
    rotations = tuple(pairs[i:] + pairs[:i] for i in range(len(pairs)))
    best = min(rotations)
    return tuple(x for x, _ in best), tuple(d for _, d in best)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root-max", type=int, default=6)
    parser.add_argument("--cycle-max", type=int, default=5)
    args = parser.parse_args()
    root_max = args.root_max
    cycle_max = args.cycle_max
    compatible: set[tuple[tuple[int, ...], tuple[int, ...], int, int]] = set()
    counts: dict[int, tuple[int, int]] = {}

    for length in range(1, cycle_max + 1):
        tested = 0
        found = 0
        for roots in product(range(1, root_max + 1), repeat=length):
            if roots[0] != min(roots):
                continue
            for distances in product(*(distance_options(r) for r in roots)):
                if not any(r == 1 and d == 3 for r, d in zip(roots, distances)):
                    continue
                total = sum(roots) + sum(distances)
                for winding in windings(total, max(roots)):
                    tested += 1
                    if not label_compatible(roots, distances, winding):
                        continue
                    canonical_roots, canonical_distances = canonical_rotation(
                        roots, distances
                    )
                    period = total // winding
                    record = (
                        canonical_roots,
                        canonical_distances,
                        winding,
                        period,
                    )
                    if record not in compatible:
                        compatible.add(record)
                        found += 1
        counts[length] = tested, found

    print({"counts": counts, "compatible": len(compatible)})
    by_period = sorted(compatible, key=lambda x: (x[3], len(x[0]), x))
    for record in by_period[:100]:
        print(record)


if __name__ == "__main__":
    main()
