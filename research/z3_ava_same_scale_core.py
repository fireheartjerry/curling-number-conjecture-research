"""Unsat-core diagnostics for the same-scale AVA mismatch.

The structural branch is

    Q = A V A,  V = suffix_v(A),

with the first mismatch ``A[j]=2, V[j]=3`` and an ``|A|``-root cube at
the corresponding middle cut.  The script greedily minimizes the circular
cube-label cuts needed for contradiction.  It is proof-discovery code; an
UNSAT result is only bounded evidence.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))

from z3 import And, Bool, BoolRef, Not, Or, Solver, is_true, sat  # type: ignore


def build(a: int, v: int, j: int):
    if not (2 <= a and 1 <= v < a and 0 <= j < v):
        raise ValueError
    A = [Bool(f"A_{i}") for i in range(a)]
    V = A[a - v :]
    Q = A + V + A
    n = len(Q)

    def power(word: list[BoolRef], cut: int, root: int, exp: int, circular: bool):
        length = len(word)

        def at(index: int):
            return word[index % length] if circular else word[index]

        return And(
            *(
                at(cut - block * root + offset)
                == at(cut - root + offset)
                for block in range(2, exp + 1)
                for offset in range(root)
            )
        )

    base: list[BoolRef] = [Not(A[0]), Not(A[1])]
    base.extend(A[k] == V[k] for k in range(j))
    base.extend((Not(A[j]), V[j]))

    # The autonomous-one facts cn(A)=cn(Q)=1.
    for word in (A, Q):
        length = len(word)
        base.extend(
            Not(power(word, length, root, 2, False))
            for root in range(1, length // 2 + 1)
        )

    middle = a + j
    base.append(power(Q, middle, a, 3, True))

    cut_formulas = []
    for cut in range(n):
        cubes = [power(Q, cut, root, 3, True) for root in range(1, n)]
        cut_formulas.append(Q[cut] == Or(*cubes))
    return A, Q, base, cut_formulas


def solve(base, formulas, cuts, timeout_ms: int):
    solver = Solver()
    solver.set(timeout=timeout_ms)
    solver.add(*base)
    solver.add(*(formulas[c] for c in cuts))
    result = solver.check()
    return result, solver.model() if result == sat else None


def greedy(base, formulas, timeout_ms: int):
    cuts = list(range(len(formulas)))
    result, _ = solve(base, formulas, cuts, timeout_ms)
    if str(result) != "unsat":
        return result, cuts
    changed = True
    while changed:
        changed = False
        for cut in tuple(cuts):
            trial = [c for c in cuts if c != cut]
            trial_result, _ = solve(base, formulas, trial, timeout_ms)
            if str(trial_result) == "unsat":
                cuts = trial
                changed = True
    return result, cuts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int)
    parser.add_argument("v", type=int)
    parser.add_argument("j", type=int)
    parser.add_argument("--timeout-ms", type=int, default=30_000)
    parser.add_argument("--near", action="store_true")
    args = parser.parse_args()
    A, Q, base, formulas = build(args.a, args.v, args.j)
    result, cuts = greedy(base, formulas, args.timeout_ms)
    print(
        f"a={args.a} v={args.v} z={args.a-args.v} j={args.j} "
        f"result={result} core={cuts}",
        flush=True,
    )
    if args.near and str(result) == "unsat":
        for removed in cuts:
            trial = [c for c in cuts if c != removed]
            trial_result, model = solve(base, formulas, trial, args.timeout_ms)
            if model is None:
                print(f"  remove={removed} result={trial_result}")
                continue
            a_word = "".join("3" if is_true(model.eval(x)) else "2" for x in A)
            q_word = "".join("3" if is_true(model.eval(x)) else "2" for x in Q)
            print(
                f"  remove={removed} result={trial_result} A={a_word} Q={q_word}"
            )


if __name__ == "__main__":
    main()
