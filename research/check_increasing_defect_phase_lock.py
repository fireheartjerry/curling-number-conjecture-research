"""Exact audits for the increasing hidden-cubic defect.

The symbolic argument is in ``increasing_defect_phase_lock.md``.  This file
does three independent jobs:

* exhausts the integer equality graph in Lemma 3 through ``p = 80``;
* checks the rotating-square identities on explicit local words;
* recomputes every displayed finite curling number with both independent
  implementations in ``curling.py``.

The local words deliberately fail the complete proper-circular fixed
profile.  They are countermodels to stronger inferences from only the
displayed border and emitted-phase equations.
"""

from __future__ import annotations

from math import gcd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference
from research.check_critical_seed_induction import (
    maximizing_roots,
    primitive,
    proper_circular_profile,
)


Word = tuple[int, ...]


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def components(
    p: int, a: int, e: int, r: int
) -> tuple[tuple[int, ...], ...]:
    """Equality components forced by ``U^3 U[a:a+e]`` ending in an r-cube."""
    n = 3 * p + e
    parent = list(range(p))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> None:
        x = find(x)
        y = find(y)
        if x != y:
            parent[y] = x

    def source_index(position: int) -> int:
        if position < 3 * p:
            return position % p
        return a + position - 3 * p

    for copy in (2, 3):
        for offset in range(r):
            union(
                source_index(n - copy * r + offset),
                source_index(n - r + offset),
            )

    classes: dict[int, list[int]] = {}
    for vertex in range(p):
        classes.setdefault(find(vertex), []).append(vertex)
    return tuple(tuple(group) for group in classes.values())


def audit_equality_graph(limit: int = 80) -> int:
    checked = 0
    for p in range(3, limit + 1):
        for r in range(p // 2 + 1, p):
            delta = 2 * r - p
            for e in range(delta + 1, r - 1):
                for a in range(1, r - e):
                    groups = components(p, a, e, r)
                    common = gcd(p, a, r)
                    expected = {
                        tuple(range(residue, p, common))
                        for residue in range(common)
                    }
                    assert set(groups) == expected
                    checked += 1
    return checked


def local_record(
    digits: str, a: int, d: int, expected_root: int
) -> dict[str, object]:
    u = tuple(map(int, digits))
    p = len(u)
    c = u[:-a]
    prefix_a = u[:a]
    prefix_d = c[:d]
    eword = prefix_d[a:]
    v = c + prefix_a + c + prefix_a + c

    assert primitive(u)
    assert primitive(v)
    assert u[-a:] == prefix_a
    assert c[-d:] == prefix_d
    assert u[a] == c[d] == 3

    values: list[int] = []
    roots: list[tuple[int, ...]] = []
    for phase in range(len(eword) + 1):
        state = u * 3 + eword[:phase]
        value = exact_cn(state)
        values.append(value)
        roots.append(maximizing_roots(state, value))

    final_state = u * 3 + eword
    assert values[-1] == 3
    assert expected_root in roots[-1]
    r = expected_root
    assert r > d
    final_root = final_state[-r:]
    assert primitive(final_root)
    fword = final_root[: -len(eword)]
    assert final_root == fword + eword

    for phase in range(len(eword) + 1):
        rotated = (
            eword[phase:] + fword + eword[:phase]
        )
        assert len(rotated) == r
        state = u * 3 + eword[:phase]
        assert state[-2 * r :] == rotated * 2

    profile_u = proper_circular_profile(u)
    profile_v = proper_circular_profile(v)
    return {
        "p": p,
        "a": a,
        "d": d,
        "r": r,
        "E": "".join(map(str, eword)),
        "values": tuple(values),
        "roots": tuple(roots),
        "pc_u_fixed": profile_u == u,
        "pc_v_fixed": profile_v == v,
        "pc_v_segment": profile_v[a : d + 1],
        "target_segment": v[a : d + 1],
        "pc_v_mismatches": sum(
            left != right for left, right in zip(profile_v, v)
        ),
    }


def main() -> None:
    graph_cases = audit_equality_graph()

    # Exact emitted-phase local model with d < r < 2d.  It refutes both
    # ``r=d`` and ``r>=2d`` if the global fixed-profile equations are
    # omitted.
    below_twice_d = local_record(
        "23233223232232322", a=1, d=3, expected_root=5
    )
    assert below_twice_d["values"] == (3, 2, 3)
    assert below_twice_d["pc_v_segment"] == (3, 2, 3)
    assert below_twice_d["target_segment"] == (3, 2, 3)
    assert not below_twice_d["pc_u_fixed"]
    assert not below_twice_d["pc_v_fixed"]

    # At both internal 2-cuts the phase-locked length-seven square is
    # maximizing.  At the second one a second root of length four also
    # maximizes, so phase locking does not imply uniqueness.
    nonunique_square = local_record(
        "23223322232232223223222",
        a=1,
        d=4,
        expected_root=7,
    )
    assert nonunique_square["values"] == (3, 2, 2, 3)
    assert nonunique_square["roots"][1] == (7,)
    assert nonunique_square["roots"][2] == (4, 7)

    # A one-symbol left extension of the final root-eight cube is
    # compatible with the local emitted segment ``3223``.  This is the
    # sharp boundary allowed by the no-circular-333 argument.
    one_left_extension = local_record(
        "23223322323223223232232232",
        a=1,
        d=5,
        expected_root=8,
    )
    assert one_left_extension["values"] == (3, 2, 2, 3, 3)
    assert one_left_extension["roots"][3] == (8,)
    assert one_left_extension["roots"][4] == (8,)

    print(f"equality_graph_cases={graph_cases} p_max=80")
    print(f"below_twice_d={below_twice_d}")
    print(f"nonunique_phase_locked_square={nonunique_square}")
    print(f"one_left_extension={one_left_extension}")


if __name__ == "__main__":
    main()
