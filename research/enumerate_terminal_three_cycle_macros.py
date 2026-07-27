"""Enumerate primitive terminal three-residue layouts at circumference 48.

For one macro unit, each residue cycle has six vertices, four span-one
edges, and two span-six edges.  This script first enumerates the exact
geometric layouts on the three residue grids, then the two alternating
value phases on each cycle.  Every selected long edge is checked against
the eight oriented terminal g=3 Q21 factors.
"""

from __future__ import annotations

from itertools import combinations, product

from check_run_length_grammar import primitive
from check_terminal_q21_overlaps import oriented_roots
from explore_gadget_cycles import (
    exact_negative_constraints,
    wsq_holes,
)


M = 48
SLOTS = 16


def cyclic_gaps(vertices: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        (vertices[(j + 1) % len(vertices)] - vertices[j]) % SLOTS
        for j in range(len(vertices))
    )


def layouts_one_residue() -> tuple[tuple[int, ...], ...]:
    out = []
    for vertices in combinations(range(SLOTS), 6):
        if sorted(cyclic_gaps(vertices)) == [1, 1, 1, 1, 6, 6]:
            out.append(vertices)
    return tuple(out)


def raw_vertices(residue: int, slots: tuple[int, ...]) -> frozenset[int]:
    return frozenset(residue + 3 * slot for slot in slots)


def forward_long_edges(
    residue: int, slots: tuple[int, ...]
) -> tuple[tuple[int, int], ...]:
    out = []
    for j, slot in enumerate(slots):
        nxt = slots[(j + 1) % len(slots)]
        if (nxt - slot) % SLOTS == 6:
            start = residue + 3 * slot
            out.append((start, start + 18))
    assert len(out) == 2
    return tuple(out)


def geometry_ok(slot_sets: tuple[tuple[int, ...], ...]) -> bool:
    raw = tuple(raw_vertices(r, slot_sets[r]) for r in range(3))
    for r in range(3):
        for start, _ in forward_long_edges(r, slot_sets[r]):
            hits = []
            for s in range(3):
                if s == r:
                    continue
                interior = {
                    (start + ((s - r) % 3) + 3 * k) % M
                    for k in range(6)
                }
                if interior <= raw[s]:
                    hits.append(s)
                elif interior & raw[s]:
                    return False
            if len(hits) != 1:
                return False
    return True


def alternating_values(
    residue: int, slots: tuple[int, ...], first: int
) -> dict[int, int]:
    values = {}
    current = first
    for slot in slots:
        values[(residue + 3 * slot) % M] = current
        current = 3 - current
    assert current == first
    return values


def terminal_factors() -> frozenset[tuple[int, ...]]:
    out = []
    for _, period, alpha, beta, _ in oriented_roots():
        if period[-1] != 3:
            continue
        c = period[:-1]
        out.append((alpha,) + c + (3,) + c + (3,) + c + (beta,))
    return frozenset(out)


def canonical(a: tuple[int, ...]) -> tuple[int, ...]:
    return min(a[k:] + a[:k] for k in range(len(a)))


def main() -> None:
    choices = layouts_one_residue()
    print(f"one_residue_layouts={len(choices)}")
    # Normalize by translating the whole code so residue-zero slot zero
    # is a vertex.
    c0s = tuple(x for x in choices if 0 in x)
    factors = terminal_factors()
    geometric = []
    for s0 in c0s:
        for s1 in choices:
            for s2 in choices:
                triple = (s0, s1, s2)
                if geometry_ok(triple):
                    geometric.append(triple)
    print(f"geometric_layouts_with_normalization={len(geometric)}")

    classes: dict[tuple[int, ...], dict] = {}
    for slots in geometric:
        for phases in product((1, 2), repeat=3):
            values: dict[int, int] = {}
            for r in range(3):
                values.update(alternating_values(r, slots[r], phases[r]))
            a = tuple(values.get(i, 3) for i in range(M))
            valid = True
            for r in range(3):
                for start, end in forward_long_edges(r, slots[r]):
                    f = tuple(a[(start + j) % M] for j in range(19))
                    if f not in factors:
                        valid = False
                        break
                if not valid:
                    break
            if not valid or not primitive(a):
                continue
            key = canonical(a)
            classes.setdefault(
                key,
                {
                    "holes": wsq_holes(key),
                    "negative": exact_negative_constraints(key),
                    "models": 0,
                },
            )["models"] += 1

    print(f"primitive_rotation_classes={len(classes)}")
    for a, data in sorted(classes.items()):
        print(
            "A="
            + "".join(map(str, a))
            + f" holes={data['holes']} negative={data['negative']} "
            + f"models={data['models']}"
        )


if __name__ == "__main__":
    main()
