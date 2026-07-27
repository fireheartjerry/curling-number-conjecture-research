"""Enumerate the finite primitive two-cycle terminal Q21 macro table.

A terminal g=3 span-six edge has one of eight oriented clipped run-code
factors of length 19.  In a two-residue terminal configuration, one such
factor contains the six consecutive vertices of the other cycle.  That
cycle's unique long edge bridges this chain to its next translate.

The counting argument gives circumference 33 in the primitive case.
This script overlays the two oriented factors, checks the selected
terminal edges directly, and reports every compatible code and its exact
negative/WSQ obstructions.
"""

from __future__ import annotations

from check_run_length_grammar import primitive
from check_terminal_q21_overlaps import oriented_roots
from explore_gadget_cycles import (
    cycle_winding,
    defect_graph,
    directed_cycles,
    exact_negative_constraints,
    perfect_matchings,
    wsq_holes,
)


def factor(record) -> tuple[int, ...]:
    _, period, alpha, beta, _ = record
    c = period[:-1]
    return (alpha,) + c + (3,) + c + (3,) + c + (beta,)


def defect_offset(record) -> int:
    f = factor(record)
    residues = {
        i % 3 for i in range(1, 18) if f[i] < 3
    }
    assert len(residues) == 1
    return next(iter(residues))


def overlay(
    circumference: int,
    placements: tuple[tuple[int, tuple[int, ...]], ...],
) -> tuple[int, ...] | None:
    values: list[int | None] = [None] * circumference
    for start, f in placements:
        for offset, value in enumerate(f):
            phase = (start + offset) % circumference
            if values[phase] is not None and values[phase] != value:
                return None
            values[phase] = value
    if any(value is None for value in values):
        return None
    return tuple(int(value) for value in values)


def main() -> None:
    roots = tuple(x for x in oriented_roots() if x[1][-1] == 3)
    assert len(roots) == 8
    classes: dict[tuple[int, ...], dict] = {}
    compatible = 0
    for parent in roots:
        delta = defect_offset(parent)
        parent_start = 0
        child_start = delta + 15
        for child in roots:
            # The child factor must contain the six parent vertices in
            # its interior, hence its internal-defect offset is 3-delta.
            if defect_offset(child) != 3 - delta:
                continue
            a = overlay(
                33,
                (
                    (parent_start, factor(parent)),
                    (child_start, factor(child)),
                ),
            )
            if a is None:
                continue
            compatible += 1
            if not primitive(a):
                continue
            rotations = tuple(a[k:] + a[:k] for k in range(len(a)))
            key = min(rotations)
            classes.setdefault(
                key,
                {
                    "examples": [],
                    "holes": wsq_holes(key),
                    "negative": exact_negative_constraints(key),
                },
            )["examples"].append(
                (
                    parent[0],
                    parent[2],
                    parent[3],
                    child[0],
                    child[2],
                    child[3],
                )
            )

    print(f"compatible_oriented_pairs={compatible}")
    print(f"rotation_classes={len(classes)}")
    assert compatible == 8
    assert len(classes) == 4
    for key, data in sorted(classes.items()):
        a = key
        graph = defect_graph(a)
        assert data["holes"]
        matchings = perfect_matchings(a)
        assert len(matchings) == 1
        cycles = directed_cycles(matchings[0])
        assert len(cycles) == 2
        assert all(cycle_winding(a, matchings[0], cycle) == 1 for cycle in cycles)
        assert all(
            span in (1, 6) and join == 3
            for edges in graph.values()
            for _, span, join in edges
        )
        assert sum(
            span == 6
            for edges in graph.values()
            for _, span, _ in edges
        ) == 2
        failed = data["holes"][0]
        certificate = []
        for h in range(1, len(a)):
            early = a[(failed - 2 * h) % len(a)]
            late = a[(failed - h) % len(a)]
            if early < late:
                certificate.append((h, "capacity"))
                continue
            mismatch = next(
                (
                    j
                    for j in range(1, h)
                    if a[(failed - 2 * h + j) % len(a)]
                    != a[(failed - h + j) % len(a)]
                ),
                None,
            )
            assert mismatch is not None
            certificate.append((h, mismatch))
        print(
            "A="
            + "".join(map(str, a))
            + f" holes={data['holes']} negative={data['negative']} "
            + f"orientations={data['examples']}"
        )
        print("  long_edges=" + repr(
            tuple(
                (i, edge)
                for i, edges in graph.items()
                for edge in edges
                if edge[1] == 6
            )
        ))
        print(f"  failed_run={failed} certificate={tuple(certificate)}")


if __name__ == "__main__":
    main()
