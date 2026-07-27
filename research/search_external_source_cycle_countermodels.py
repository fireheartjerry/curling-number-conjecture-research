"""Search relaxations of the external-source terminality implications.

All power-root sets and proper circular profiles in the emitted records are
computed by ``check_run_length_grammar``.  Run the A094004 calibration first:

    python -m unittest \
      tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration

The search ranges over primitive singleton-3 codes A in {1,2,3}^m and all
physical rotations of Q(A).  It looks for a directed cycle in the *extended*
first-copy-fitting square-ancestry graph containing

* a root-one/root-symbol-2 external edge whose selected cube has q=1; or
* such an edge with q>1 whose circular primitive root code is nonterminal.

This is a search for countermodels to local implications, not a proof about
unbounded exact fixed profiles.
"""

from __future__ import annotations

import argparse
from itertools import product

from check_max_square_terminal_forest import fitting
from check_run_length_grammar import (
    binary_word,
    primitive,
    proper_profile,
    word_power_root_lengths,
)
from check_terminal_source_gadget_bridge import (
    circular_run_code_rotations,
    terminal,
    tight_gadget,
)


Word = tuple[int, ...]
Vertex = tuple[int, int]
Record = tuple[int, int, int, int]


def root_word(word: Word, endpoint: int, root: int) -> Word:
    return tuple(
        word[(endpoint - root + offset) % len(word)]
        for offset in range(root)
    )


def period_code_terminal(code: tuple[int, ...]) -> bool:
    """Section-7 terminality, stated directly on a primitive period code."""
    return all(
        tight_gadget(code, endpoint, 1) is not None
        for endpoint, value in enumerate(code)
        if value in (1, 2)
    )


def extended_graph(
    word: Word,
) -> tuple[set[Vertex], dict[Vertex, tuple[Record, ...]]]:
    n = len(word)
    square_roots = {
        cut: word_power_root_lengths(word, cut, 2) for cut in range(n)
    }
    cube_roots = {
        cut: word_power_root_lengths(word, cut, 3) for cut in range(n)
    }
    vertices = {
        (cut, root)
        for cut in range(n)
        if word[cut] == 2
        for root in square_roots[cut]
        if fitting(word, cut, 2, root)
    }
    edges: dict[Vertex, tuple[Record, ...]] = {}
    for cut, root in vertices:
        preceding_highs = tuple(
            distance
            for distance in range(1, root + 1)
            if word[(cut - distance) % n] == 3
        )
        if root == 1 and root_word(word, cut, 1) == (2,):
            preceding_highs = tuple(
                distance
                for distance in range(1, 4)
                if word[(cut - distance) % n] == 3
            )
        if not preceding_highs:
            edges[cut, root] = ()
            continue
        distance = preceding_highs[0]
        high = (cut - distance) % n
        children = tuple(
            ((high - q) % n, q, distance, high)
            for q in cube_roots[high]
            if fitting(word, high, 3, q)
            and ((high - q) % n, q) in vertices
        )
        edges[cut, root] = children
    return vertices, edges


def can_reach(
    edges: dict[Vertex, tuple[Record, ...]],
    start: Vertex,
    target: Vertex,
) -> bool:
    pending = [start]
    seen: set[Vertex] = set()
    while pending:
        current = pending.pop()
        if current == target:
            return True
        if current in seen:
            continue
        seen.add(current)
        pending.extend(
            record[:2]
            for record in edges.get(current, ())
            if record[:2] not in seen
        )
    return False


def shortest_path(
    edges: dict[Vertex, tuple[Record, ...]],
    start: Vertex,
    target: Vertex,
) -> tuple[tuple[Vertex, Record], ...] | None:
    """A shortest directed edge path, represented by source/record pairs."""
    pending: list[
        tuple[Vertex, tuple[tuple[Vertex, Record], ...]]
    ] = [(start, ())]
    seen: set[Vertex] = set()
    while pending:
        current, path = pending.pop(0)
        if current == target:
            return path
        if current in seen:
            continue
        seen.add(current)
        pending.extend(
            (
                record[:2],
                path + ((current, record),),
            )
            for record in edges.get(current, ())
            if record[:2] not in seen
        )
    return None


def cycle_edges(word: Word) -> tuple[
    tuple[Vertex, Record, tuple[int, ...] | None, bool | None], ...
]:
    _, edges = extended_graph(word)
    records: list[
        tuple[Vertex, Record, tuple[int, ...] | None, bool | None]
    ] = []
    for source, outgoing in edges.items():
        cut, root = source
        if root != 1 or root_word(word, cut, 1) != (2,):
            continue
        for record in outgoing:
            child = record[:2]
            child_root, distance = record[1], record[2]
            if distance != 3 or not can_reach(edges, child, source):
                continue
            if child_root == 1:
                records.append((source, record, None, None))
                continue
            selected = root_word(word, record[3], child_root)
            rotations = circular_run_code_rotations(selected)
            code = min(rotations)
            records.append(
                (source, record, code, period_code_terminal(code))
            )
    return tuple(records)


def audit_record(
    code: tuple[int, ...],
    shift: int,
    word: Word,
    edge: tuple[Vertex, Record, tuple[int, ...] | None, bool | None],
) -> dict[str, object]:
    profile = proper_profile(word)
    vertices, edges = extended_graph(word)
    source, record, period_code, is_terminal = edge
    child = record[:2]
    high = record[3]
    return_path = shortest_path(edges, child, source)
    assert return_path is not None
    cycle = ((source, record),) + return_path
    component = tuple(
        sorted(
            vertex
            for vertex in vertices
            if can_reach(edges, source, vertex)
            and can_reach(edges, vertex, source)
        )
    )
    component_set = set(component)
    sink_component = all(
        out[:2] in component_set
        for vertex in component
        for out in edges[vertex]
    )
    cycle_exact = all(
        profile[vertex[0]] == word[vertex[0]]
        and all(
            profile[out[3]] == word[out[3]]
            for out in edges[vertex]
            if out[:2] in component_set
        )
        for vertex in component
    )
    full_fitting_failures = tuple(
        cut
        for cut, exponent in enumerate(word)
        if not any(
            fitting(word, cut, exponent, root)
            for root in word_power_root_lengths(word, cut, exponent)
        )
    )
    mismatch = tuple(
        cut
        for cut, pair in enumerate(zip(profile, word))
        if pair[0] != pair[1]
    )
    return {
        "run_code": code,
        "physical_shift": shift,
        "word": "".join(map(str, word)),
        "primitive_word": primitive(word),
        "source": source,
        "edge_record_child_cut_root_distance_high": record,
        "child": child,
        "selected_root_word": root_word(word, high, record[1]),
        "period_code": period_code,
        "terminal": is_terminal,
        "source_boundary": tuple(
            word[(high + offset) % len(word)] for offset in range(4)
        ),
        "proper_profile": profile,
        "profile_mismatch_cuts": mismatch,
        "full_first_copy_fitting_failures": full_fitting_failures,
        "cycle_source_edge_records": cycle,
        "strong_component": component,
        "strong_component_is_sink": sink_component,
        "strong_component_internal_edges": tuple(
            (vertex, out)
            for vertex in component
            for out in edges[vertex]
            if out[:2] in component_set
        ),
        "cycle_component_exact_at_its_low_and_high_cuts": cycle_exact,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=8)
    parser.add_argument("--limit", type=int, default=1)
    parser.add_argument("--known-only", action="store_true")
    args = parser.parse_args()

    best: dict[str, tuple[tuple[int, ...], dict[str, object]]] = {}
    if args.known_only:
        for code in ((1, 3, 3, 3), (1, 3, 3, 2, 3, 2, 3)):
            word = binary_word(code)
            for edge in cycle_edges(word):
                q = edge[1][1]
                kind = (
                    "unary"
                    if q == 1
                    else "nonterminal"
                    if edge[3] is False
                    else "terminal"
                )
                if kind != "terminal":
                    print({"known": kind, **audit_record(code, 0, word, edge)})
        return

    for m in range(2, args.max_m + 1):
        for code in product((1, 2, 3), repeat=m):
            if not primitive(code):
                continue
            circular = binary_word(code)
            if not primitive(circular):
                continue
            profile0 = proper_profile(circular)
            mismatch_count = sum(
                left != right for left, right in zip(profile0, circular)
            )
            for shift in range(len(circular)):
                word = circular[shift:] + circular[:shift]
                for edge in cycle_edges(word):
                    q = edge[1][1]
                    terminal_value = edge[3]
                    kind = (
                        "unary"
                        if q == 1
                        else "nonterminal"
                        if terminal_value is False
                        else "terminal"
                    )
                    if kind == "terminal":
                        continue
                    record = audit_record(code, shift, word, edge)
                    fitting_failures = len(
                        record["full_first_copy_fitting_failures"]
                    )
                    key = (
                        mismatch_count,
                        fitting_failures,
                        len(circular),
                        m,
                    )
                    previous = best.get(kind)
                    if previous is None or key < previous[0]:
                        best[kind] = (key, record)
                        print({"new_best": kind, "score": key, **record})
        if all(kind in best for kind in ("unary", "nonterminal")):
            print(
                {
                    "completed_m": m,
                    "best_scores": {
                        kind: value[0] for kind, value in best.items()
                    },
                }
            )

    print({"final_best": {kind: value[1] for kind, value in best.items()}})


if __name__ == "__main__":
    main()
