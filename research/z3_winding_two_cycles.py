"""Search abstract tight-gadget cycles of winding two.

This deliberately omits square/cube profile constraints outside the
chosen cycle.  A SAT model therefore refutes any claim that winding two
is excluded by gadget equations and root primitivity alone.
"""

from __future__ import annotations

import argparse
import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import Int, Or, Solver, Sum, sat  # type: ignore


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x != y:
            self.parent[y] = x


def pure_g3_conflict(m: int, spans: tuple[int, ...]):
    """Classify contradiction from equality/3/complement constraints only."""
    endpoint = 0
    seen = {0}
    edges = []
    for span in spans:
        start = (endpoint - 3 * span) % m
        if start in seen and start != 0:
            return "repeated endpoint"
        edges.append((endpoint, span, start))
        endpoint = start
        seen.add(endpoint)
    if endpoint != 0 or len(seen) != len(spans):
        return "not one cycle"

    dsu = DSU(m)
    for endpoint, span, start in edges:
        for offset in range(1, span):
            dsu.union(
                (start + offset) % m,
                (start + span + offset) % m,
            )
            dsu.union(
                (start + offset) % m,
                (start + 2 * span + offset) % m,
            )
    forced_three = set()
    forced_defect = set()
    complements = []
    for endpoint, span, start in edges:
        forced_three.add(dsu.find((start + span) % m))
        forced_three.add(dsu.find((start + 2 * span) % m))
        forced_defect.add(dsu.find(start))
        forced_defect.add(dsu.find(endpoint))
        complements.append((dsu.find(start), dsu.find(endpoint)))
    forced_three = {dsu.find(x) for x in forced_three}
    forced_defect = {dsu.find(x) for x in forced_defect}
    if forced_three & forced_defect:
        return "endpoint equals a forced-3 class"

    graph: dict[int, list[int]] = {}
    for x, y in complements:
        x, y = dsu.find(x), dsu.find(y)
        if x == y:
            return "endpoint equals its complement"
        graph.setdefault(x, []).append(y)
        graph.setdefault(y, []).append(x)
    colors = {}
    for root in graph:
        if root in colors:
            continue
        colors[root] = 0
        stack = [root]
        while stack:
            x = stack.pop()
            for y in graph[x]:
                if y in colors:
                    if colors[y] == colors[x]:
                        return "odd complement cycle"
                else:
                    colors[y] = 1 - colors[x]
                    stack.append(y)
    return None


def compositions(total: int):
    """All positive compositions, represented as tuples."""
    if total == 0:
        yield ()
        return
    for mask in range(1 << (total - 1)):
        parts = []
        last = 0
        for position in range(1, total):
            if mask & (1 << (position - 1)):
                parts.append(position - last)
                last = position
        parts.append(total - last)
        yield tuple(parts)


def solve_pattern(
    m: int,
    spans: tuple[int, ...],
    require_g3: bool,
    require_primitive_roots: bool,
    require_primitive_code: bool,
    require_fitting: bool,
):
    a = [Int(f"a_{i}") for i in range(m)]
    solver = Solver()
    for x in a:
        solver.add(1 <= x, x <= 3)
    if require_primitive_code:
        for period in range(1, m):
            if m % period == 0:
                solver.add(
                    Or(
                        *(a[j] != a[j % period] for j in range(period, m))
                    )
                )
    n = Sum(*(x + 1 for x in a))

    endpoint = 0
    seen = {endpoint}
    edges = []
    for span in spans:
        if require_fitting and 3 * span > m + endpoint - 1:
            return None
        start = (endpoint - 3 * span) % m
        if start in seen and start != 0:
            return None
        edges.append((endpoint, span, start))
        endpoint = start
        seen.add(endpoint)
    if endpoint != 0 or len(seen) != len(spans):
        return None

    for endpoint, span, start in edges:
        beta = a[endpoint]
        alpha = a[start]
        g1 = a[(start + span) % m]
        g2 = a[(start + 2 * span) % m]
        solver.add(beta <= 2, g1 == g2, g1 == alpha + beta)
        if require_g3:
            solver.add(g1 == 3)
        for offset in range(1, span):
            solver.add(
                a[(start + offset) % m]
                == a[(start + span + offset) % m],
                a[(start + offset) % m]
                == a[(start + 2 * span + offset) % m],
            )
        period_code = [
            a[(start + offset) % m] for offset in range(1, span + 1)
        ]
        if require_primitive_roots:
            for period in range(1, span):
                if span % period == 0:
                    solver.add(
                        Or(
                            *(
                                period_code[j] != period_code[j % period]
                                for j in range(period, span)
                            )
                        )
                    )
        solver.add(Sum(*(x + 1 for x in period_code)) < n)

    if solver.check() != sat:
        return None
    model = solver.model()
    return tuple(model.eval(x).as_long() for x in a), edges


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("max_m", type=int, nargs="?", default=24)
    parser.add_argument("--g3", action="store_true")
    parser.add_argument("--allow-imprimitive-roots", action="store_true")
    parser.add_argument("--allow-imprimitive-code", action="store_true")
    parser.add_argument(
        "--fitting",
        action="store_true",
        help="require every selected cube to fit the deleted first-copy lift",
    )
    args = parser.parse_args()
    for m in range(3, args.max_m + 1, 3):
        total = 2 * m // 3
        tested = 0
        found = None
        for spans in compositions(total):
            # Returning after one winding would make this two cycles
            # written consecutively rather than one winding-two cycle.
            if any(
                sum(spans[:prefix]) == m // 3
                for prefix in range(1, len(spans))
            ):
                continue
            tested += 1
            found = solve_pattern(
                m,
                spans,
                args.g3,
                not args.allow_imprimitive_roots,
                not args.allow_imprimitive_code,
                args.fitting,
            )
            if found is not None:
                print(
                    f"m={m}: SAT spans={spans} "
                    f"A={''.join(map(str, found[0]))} edges={found[1]}"
                )
                break
        if found is None:
            print(f"m={m}: UNSAT across {tested} cycle patterns")


if __name__ == "__main__":
    main()
