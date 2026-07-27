"""Search terminal canonical matchings with at least three origin crossings.

This tests the gap in the statement "terminal all-g=3 cycles have winding
one."  Winding one was proved when 3 divides the code circumference; a
cycle of winding divisible by three is the remaining arithmetic branch.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, If, Int, Not, Or, Solver, Sum, sat  # type: ignore

from check_terminal_q21_overlaps import oriented_roots
from explore_gadget_cycles import (
    cycle_winding,
    defect_graph,
    directed_cycles,
)


def terminal_factors() -> tuple[tuple[int, ...], ...]:
    out = []
    for _, period, alpha, beta, _ in oriented_roots():
        if period[-1] != 3:
            continue
        c = period[:-1]
        out.append((alpha,) + c + (3,) + c + (3,) + c + (beta,))
    assert len(out) == 8
    return tuple(out)


def build(m: int, negative: bool, wsq: bool):
    solver = Solver()
    a = [Int(f"a_{i}") for i in range(m)]
    for value in a:
        solver.add(1 <= value, value <= 3)

    factors = terminal_factors()

    def equals_factor(start: int, f: tuple[int, ...]):
        return And(*(a[(start + j) % m] == value for j, value in enumerate(f)))

    def short(i: int):
        return Or(
            And(
                a[(i - 3) % m] == 1,
                a[(i - 2) % m] == 3,
                a[(i - 1) % m] == 3,
                a[i] == 2,
            ),
            And(
                a[(i - 3) % m] == 2,
                a[(i - 2) % m] == 3,
                a[(i - 1) % m] == 3,
                a[i] == 1,
            ),
        )

    def long(i: int):
        if not (6 < m and 18 <= m + i - 1):
            return False
        return Or(*(equals_factor(i - 18, f) for f in factors))

    selected_short = [short(i) for i in range(m)]
    selected_long = [And(Not(short(i)), long(i)) for i in range(m)]
    for i in range(m):
        solver.add(Or(a[i] == 3, selected_short[i], selected_long[i]))
    solver.add(Or(*(a[i] < 3 for i in range(m))))

    crossings = [
        If(And(selected_short[i], i < 3), 1, 0)
        + If(And(selected_long[i], i < 18), 1, 0)
        for i in range(m)
    ]
    solver.add(Sum(*crossings) >= 3)

    binary_length = Sum(*(value + 1 for value in a))

    def power(i: int, r, h: int, exponent: int):
        base = a[(i - h) % m]
        clauses = [
            r <= base,
            a[(i - exponent * h) % m] >= base - r,
            Sum(*(a[(i - h + j) % m] + 1 for j in range(h)))
            < binary_length,
        ]
        clauses.extend(
            a[(i - block * h) % m] == base
            for block in range(2, exponent)
        )
        clauses.extend(
            a[(i - block * h + j) % m] == a[(i - h + j) % m]
            for block in range(2, exponent + 1)
            for j in range(1, h)
        )
        return And(*clauses)

    if negative:
        for i in range(m):
            for r in range(3):
                solver.add(
                    Or(
                        a[i] < r + 1,
                        Not(Or(*(power(i, r, h, 3) for h in range(1, m)))),
                    )
                )
            solver.add(
                Not(Or(*(power(i, a[i], h, 4) for h in range(1, m))))
            )
    if wsq:
        for i in range(m):
            solver.add(Or(*(power(i, 0, h, 2) for h in range(1, m))))

    return solver, a


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-m", type=int, default=7)
    parser.add_argument("--max-m", type=int, default=80)
    parser.add_argument("--negative", action="store_true")
    parser.add_argument("--wsq", action="store_true")
    parser.add_argument("--timeout-ms", type=int, default=30_000)
    args = parser.parse_args()

    for m in range(args.min_m, args.max_m + 1):
        solver, symbols = build(m, args.negative, args.wsq)
        solver.set(timeout=args.timeout_ms)
        result = solver.check()
        if result != sat:
            print(f"m={m}: {result}")
            continue
        model = solver.model()
        a = tuple(model.eval(x).as_long() for x in symbols)
        graph = defect_graph(a)
        canonical = {}
        for i, edges in graph.items():
            short = tuple(edge for edge in edges if edge[1] == 1)
            terminal_long = tuple(edge for edge in edges if edge[1] == 6 and edge[2] == 3)
            chosen = short[0] if short else terminal_long[0]
            canonical[i] = chosen
        cycles = directed_cycles(canonical)
        print(
            f"m={m}: A={''.join(map(str, a))} "
            f"cycles={tuple((c, cycle_winding(a, canonical, c)) for c in cycles)}"
        )
        break


if __name__ == "__main__":
    main()
