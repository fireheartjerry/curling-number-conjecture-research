"""Finite diagnostic for a hidden late k=3 root over {2,3,4}.

The U-only mode imposes a primitive root U with U[0]=2, its exact proper
circular profile, exact first-copy replay, and the hidden-edge conditions

    h is a period of U,  h>|U|/3,  U[|U|-h]=3.

The optional full mode also imposes these fixed-profile/replay equations on
V=U U U[:h].  Symbols are represented by monotone Boolean thresholds.
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / ".vendor"))
sys.path.insert(0, str(HERE.parent))

from z3 import And, Bool, Not, Or, Solver, is_true, sat  # type: ignore

from curling import curling_number, curling_number_reference
from research.check_run_length_grammar import primitive, proper_profile


def equal(pair, i: int, j: int):
    ge3, ge4 = pair
    n = len(ge3)
    return And(ge3[i % n] == ge3[j % n], ge4[i % n] == ge4[j % n])


def power(pair, cut: int, root: int, exponent: int):
    n = len(pair[0])
    return And(
        *(
            equal(pair, cut - block * root + offset, cut - root + offset)
            for block in range(2, exponent + 1)
            for offset in range(root)
        )
    )


def add_primitive(solver: Solver, pair) -> None:
    n = len(pair[0])
    for divisor in range(1, n):
        if n % divisor == 0:
            solver.add(
                Or(
                    *(
                        Not(equal(pair, i, i % divisor))
                        for i in range(divisor, n)
                    )
                )
            )


def add_fixed_first_replay(solver: Solver, pair) -> None:
    ge3, ge4 = pair
    n = len(ge3)
    for i in range(n):
        solver.add(Or(Not(ge4[i]), ge3[i]))
    add_primitive(solver, pair)
    for cut in range(n):
        square = [power(pair, cut, root, 2) for root in range(1, n)]
        cube = [power(pair, cut, root, 3) for root in range(1, n)]
        fourth = [power(pair, cut, root, 4) for root in range(1, n)]
        fifth = [power(pair, cut, root, 5) for root in range(1, n)]
        fit_square = [
            power(pair, cut, root, 2)
            for root in range(1, n)
            if 2 * root <= n + cut
        ]
        fit_cube = [
            power(pair, cut, root, 3)
            for root in range(1, n)
            if 3 * root <= n + cut
        ]
        fit_fourth = [
            power(pair, cut, root, 4)
            for root in range(1, n)
            if 4 * root <= n + cut
        ]
        solver.add(Or(*square), Not(Or(*fifth)))
        solver.add(ge3[cut] == Or(*cube))
        solver.add(ge4[cut] == Or(*fourth))
        solver.add(Or(*fit_square))
        solver.add(ge3[cut] == Or(*fit_cube))
        solver.add(ge4[cut] == Or(*fit_fourth))


def decode(model, pair) -> tuple[int, ...]:
    ge3, ge4 = pair
    return tuple(
        4
        if is_true(model.eval(ge4[i]))
        else 3
        if is_true(model.eval(ge3[i]))
        else 2
        for i in range(len(ge3))
    )


def audit_first_replay(word: tuple[int, ...]) -> None:
    assert primitive(word)
    assert proper_profile(word) == word
    for cut in range(len(word)):
        state = word + word[:cut]
        fast = curling_number(state)
        slow = curling_number_reference(state)
        assert fast == slow == word[cut]


def build(p: int, h: int, full: bool):
    solver = Solver()
    u3 = [Bool(f"u3_{p}_{h}_{i}") for i in range(p)]
    u4 = [Bool(f"u4_{p}_{h}_{i}") for i in range(p)]
    u = (u3, u4)
    solver.add(Not(u3[0]), Not(u4[0]))
    a = p - h
    solver.add(u3[a], Not(u4[a]))
    for i in range(h, p):
        solver.add(u3[i] == u3[i - h], u4[i] == u4[i - h])
    add_fixed_first_replay(solver, u)
    if full:
        v = (u3 + u3 + u3[:h], u4 + u4 + u4[:h])
        add_fixed_first_replay(solver, v)
    return solver, u


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("p_min", type=int)
    parser.add_argument("p_max", type=int)
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--timeout-ms", type=int, default=30_000)
    args = parser.parse_args()

    totals = {"sat": 0, "unsat": 0, "unknown": 0}
    for p in range(args.p_min, args.p_max + 1):
        for h in range(p // 3 + 1, p):
            if math.gcd(p, h) == h:
                continue
            solver, u_pair = build(p, h, args.full)
            solver.set(timeout=args.timeout_ms)
            result = solver.check()
            key = str(result)
            totals[key] += 1
            print(f"p={p} h={h} q={2*p+h} status={key}", flush=True)
            if result == sat:
                u = decode(solver.model(), u_pair)
                audit_first_replay(u)
                print(f"  U={''.join(map(str, u))}", flush=True)
                if not args.all:
                    print(f"totals={totals}")
                    return
            elif key == "unknown":
                print(f"  reason={solver.reason_unknown()}", flush=True)
    print(f"totals={totals}")


if __name__ == "__main__":
    main()
