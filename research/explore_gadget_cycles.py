"""Explore tight cube-gadget graphs in singleton-3 run codes.

This is a finite diagnostic, not a proof.  It keeps the run-code
equations explicit and reports:

* every tight primitive gadget at every defect endpoint;
* the bipartite endpoint-to-leading-defect graph;
* perfect matchings and their directed cycle decompositions; and
* weak-square (WSQ) holes at first-2 cuts.

The definitions are imported from ``check_run_length_grammar.py`` so
that the exploratory graph uses exactly the already calibrated cube and
square equations.
"""

from __future__ import annotations

from itertools import product

from check_run_length_grammar import (
    A33,
    binary_word,
    code_square_witnesses,
    defect_gadget,
    direct_power_root_lengths,
    primitive,
    proper_profile,
    run_starts,
    word_power_root_lengths,
)


def tight_gadgets(a: tuple[int, ...], i: int):
    """Return all tight primitive gadgets ending at defect ``i``."""
    m = len(a)
    out = []
    for s in range(1, m):
        g = defect_gadget(a, i, s)
        if g is not None and a[(i - 3 * s) % m] == g.alpha:
            out.append(g)
    return tuple(out)


def defect_graph(a: tuple[int, ...]):
    """Map each defect endpoint to its possible leading defects."""
    return {
        i: tuple(
            sorted(
                {
                    ((i - 3 * g.span) % len(a), g.span, g.alpha + g.beta)
                    for g in tight_gadgets(a, i)
                }
            )
        )
        for i, value in enumerate(a)
        if value < 3
    }


def perfect_matchings(a: tuple[int, ...], limit: int = 1000):
    """Enumerate endpoint-to-leading-defect perfect matchings."""
    graph = defect_graph(a)
    left = tuple(sorted(graph, key=lambda i: len(graph[i])))
    defects = frozenset(left)
    out = []

    def visit(pos: int, used: frozenset[int], chosen: dict[int, tuple[int, int, int]]):
        if len(out) >= limit:
            return
        if pos == len(left):
            out.append(dict(chosen))
            return
        i = left[pos]
        for edge in graph[i]:
            j, _, _ = edge
            if j not in defects or j in used:
                continue
            chosen[i] = edge
            visit(pos + 1, used | {j}, chosen)
            del chosen[i]

    visit(0, frozenset(), {})
    return tuple(out)


def directed_cycles(matching: dict[int, tuple[int, int, int]]):
    """Cycle decomposition of a bijective endpoint map."""
    unseen = set(matching)
    cycles = []
    while unseen:
        start = min(unseen)
        cycle = []
        cur = start
        while cur not in cycle:
            cycle.append(cur)
            unseen.discard(cur)
            cur = matching[cur][0]
        assert cur == start
        cycles.append(tuple(cycle))
    return tuple(cycles)


def cycle_winding(
    a: tuple[int, ...],
    matching: dict[int, tuple[int, int, int]],
    cycle: tuple[int, ...],
) -> int:
    """Total clockwise edge length divided by the code circumference."""
    total = sum(3 * matching[i][1] for i in cycle)
    assert total % len(a) == 0
    return total // len(a)


def lifted_run_start(a: tuple[int, ...], index: int) -> int:
    """Physical start coordinate of lifted run ``index``."""
    m = len(a)
    n = sum(x + 1 for x in a)
    turns, phase = divmod(index, m)
    return turns * n + sum(a[j] + 1 for j in range(phase))


def physical_gadget_interval(
    a: tuple[int, ...], endpoint: int, edge: tuple[int, int, int]
):
    """Return (left,right,period) for the lift ending at ``endpoint``."""
    _, span, _ = edge
    end_lift = endpoint
    start_lift = end_lift - 3 * span
    left = lifted_run_start(a, start_lift)
    right = lifted_run_start(a, end_lift) + a[endpoint % len(a)]
    assert (right - left) % 3 == 0
    return left, right, (right - left) // 3


def crossing_report(a: tuple[int, ...]) -> None:
    """Report physical crossings among a unique matching's gadget runs."""
    matchings = perfect_matchings(a)
    if len(matchings) != 1:
        print("crossing report requires a unique matching")
        return
    matching = matchings[0]
    n = len(binary_word(a))
    intervals = {
        i: physical_gadget_interval(a, i, edge)
        for i, edge in matching.items()
    }
    holes = wsq_holes(a)
    hole_cuts = tuple(run_starts(a)[i] for i in holes)
    print("physical interval crossings:")
    seen = set()
    for i, (left, right, p) in intervals.items():
        for j, base in intervals.items():
            if i == j:
                continue
            for shift in range(-2, 3):
                left2, right2, q = (
                    base[0] + shift * n,
                    base[1] + shift * n,
                    base[2],
                )
                if left < left2 < right < right2:
                    key = (i, j, shift)
                    if key in seen:
                        continue
                    seen.add(key)
                    overlap = right - left2
                    exposed = (right, left2 + q)
                    hole_lifts = tuple(
                        h + turn * n
                        for h in hole_cuts
                        for turn in range(-2, 3)
                        if right <= h + turn * n < left2 + q
                    )
                    print(
                        f"  edge {i}(p={p}) crosses "
                        f"edge {j}+{shift}N(p={q}): overlap={overlap}, "
                        f"threshold={p+q-__import__('math').gcd(p,q)}, "
                        f"exposed-first-tail={exposed}, holes={hole_lifts}"
                    )


def last_defect_transition_report(a: tuple[int, ...]) -> None:
    """Inspect cube roots at the last internal defect of each gadget root."""
    matchings = perfect_matchings(a)
    if len(matchings) != 1:
        print("transition report requires a unique matching")
        return
    qword = binary_word(a)
    n = len(qword)
    starts = run_starts(a)
    print("last-defect transitions:")
    for endpoint, edge in sorted(matchings[0].items()):
        left, right, p = physical_gadget_interval(a, endpoint, edge)
        third_start = right - p
        candidates = []
        for run_index in range(endpoint - edge[1] - 1, endpoint + 1):
            phase = run_index % len(a)
            cut = lifted_run_start(a, run_index) + a[phase]
            if third_start < cut < right and a[phase] < 3:
                candidates.append((run_index, cut))
        if not candidates:
            print(f"  edge {endpoint} p={p}: no internal defect")
            continue
        run_index, cut = max(candidates, key=lambda x: x[1])
        roots = word_power_root_lengths(qword, cut % n, 3)
        delta = right - cut
        print(
            f"  edge {endpoint} p={p}: last defect run={run_index} "
            f"phase={cut % n}, delta={delta}, cube-roots={roots}"
        )


def wsq_holes(a: tuple[int, ...]):
    """Defect/run indices whose first-2 cut has no proper square."""
    return tuple(
        i for i in range(len(a)) if not code_square_witnesses(a, i, 0)
    )


def exact_profile(a: tuple[int, ...]) -> bool:
    return proper_profile(binary_word(a)) == binary_word(a)


def exact_negative_constraints(a: tuple[int, ...]) -> bool:
    """Check no cube at any 2-cut and no fourth at any 3-cut."""
    for i, run in enumerate(a):
        for r in range(run):
            if direct_power_root_lengths(a, i, r, 3):
                return False
        if direct_power_root_lengths(a, i, run, 4):
            return False
    return True


def graph_signature(a: tuple[int, ...]):
    graph = defect_graph(a)
    matchings = perfect_matchings(a)
    cycle_counts = tuple(sorted({len(directed_cycles(x)) for x in matchings}))
    return (
        len(graph),
        sum(len(edges) for edges in graph.values()),
        len(matchings),
        cycle_counts,
        wsq_holes(a),
    )


def print_code_report(label: str, a: tuple[int, ...]) -> None:
    print(f"\n{label}: A={''.join(map(str, a))}, m={len(a)}")
    print(
        f"primitive={primitive(a)}, exact={exact_profile(a)}, "
        f"negative={exact_negative_constraints(a)}, holes={wsq_holes(a)}"
    )
    graph = defect_graph(a)
    for i in sorted(graph):
        rendered = ", ".join(
            f"{j}(s={s},g={g})" for j, s, g in graph[i]
        )
        print(f"  {i}:{a[i]} -> {rendered or '-'}")
    matchings = perfect_matchings(a)
    print(f"perfect matchings={len(matchings)}")
    for matching in matchings[:20]:
        cycles = directed_cycles(matching)
        print(
            "  cycles",
            tuple((cycle, cycle_winding(a, matching, cycle)) for cycle in cycles),
        )


def enumerate_small(max_m: int = 11) -> None:
    """Exhaustively enumerate primitive WSQ/cube-covered codes."""
    for m in range(1, max_m + 1):
        counts = {
            "primitive": 0,
            "wsq": 0,
            "covered": 0,
            "matching": 0,
            "negative": 0,
            "exact": 0,
        }
        examples_no_matching = []
        examples_multi_cycle = []
        for a in product((1, 2, 3), repeat=m):
            if not primitive(a):
                continue
            counts["primitive"] += 1
            if wsq_holes(a):
                continue
            counts["wsq"] += 1
            graph = defect_graph(a)
            if any(not edges for edges in graph.values()):
                continue
            counts["covered"] += 1
            matchings = perfect_matchings(a, limit=2)
            if not matchings:
                if len(examples_no_matching) < 3:
                    examples_no_matching.append(a)
                continue
            counts["matching"] += 1
            if any(len(directed_cycles(x)) > 1 for x in matchings):
                if len(examples_multi_cycle) < 3:
                    examples_multi_cycle.append(a)
            if not exact_negative_constraints(a):
                continue
            counts["negative"] += 1
            if exact_profile(a):
                counts["exact"] += 1
        print(
            f"m={m}: "
            + " ".join(f"{key}={value}" for key, value in counts.items())
        )
        if examples_no_matching:
            print(
                "  no matching:",
                " ".join("".join(map(str, a)) for a in examples_no_matching),
            )
        if examples_multi_cycle:
            print(
                "  multi-cycle:",
                " ".join("".join(map(str, a)) for a in examples_multi_cycle),
            )


def enumerate_covered_negative(max_m: int = 12) -> None:
    """Test cycle-count versus WSQ-hole count without assuming WSQ."""
    for m in range(1, max_m + 1):
        covered = 0
        matched = 0
        negative = 0
        violations = []
        sharp = []
        for a in product((1, 2, 3), repeat=m):
            if not primitive(a):
                continue
            graph = defect_graph(a)
            if not graph or any(not edges for edges in graph.values()):
                continue
            covered += 1
            matchings = perfect_matchings(a, limit=100)
            if not matchings:
                continue
            matched += 1
            if not exact_negative_constraints(a):
                continue
            negative += 1
            holes = len(wsq_holes(a))
            min_cycles = min(len(directed_cycles(x)) for x in matchings)
            if holes < min_cycles - 1:
                violations.append((a, holes, min_cycles))
            elif holes == min_cycles - 1 and len(sharp) < 3:
                sharp.append((a, holes, min_cycles))
        print(
            f"covered-negative m={m}: covered={covered} matched={matched} "
            f"negative={negative} violations={len(violations)}"
        )
        if violations:
            print(
                "  violations:",
                " ".join(
                    f"{''.join(map(str, a))}[h={h},c={c}]"
                    for a, h, c in violations[:3]
                ),
            )
        if sharp:
            print(
                "  sharp:",
                " ".join(
                    f"{''.join(map(str, a))}[h={h},c={c}]"
                    for a, h, c in sharp
                ),
            )


def main() -> None:
    print_code_report("Q21", tuple(map(int, "133233")))
    print_code_report("A33", A33)
    enumerate_small()
    enumerate_covered_negative()


if __name__ == "__main__":
    main()
