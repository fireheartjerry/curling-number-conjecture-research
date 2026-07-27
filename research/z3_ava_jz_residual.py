"""Bounded UNSAT-core diagnostics for the ``j=z`` AVA residual.

This is proof-discovery code, not a proof.  It builds the two exact
normal forms in Lemma 7 of ``ava_fixed_inheritance.md`` and minimizes
the set of exact cube-label cuts needed to refute each fixed length
tuple.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))

from z3 import And, Bool, BoolRef, Not, Or, Solver, is_true, sat  # type: ignore


def power(
    word: list[BoolRef], cut: int, root: int, exponent: int, circular: bool
) -> BoolRef:
    length = len(word)

    def at(index: int) -> BoolRef:
        return word[index % length] if circular else word[index]

    return And(
        *(
            at(cut - block * root + offset)
            == at(cut - root + offset)
            for block in range(2, exponent + 1)
            for offset in range(root)
        )
    )


def autonomous_one(word: list[BoolRef]) -> list[BoolRef]:
    length = len(word)
    return [
        Not(power(word, length, root, 2, False))
        for root in range(1, length // 2 + 1)
    ]


def primitive_constraints(word: list[BoolRef]) -> list[BoolRef]:
    length = len(word)
    return [
        Or(
            *(
                word[index] != word[index % period]
                for index in range(period, length)
            )
        )
        for period in range(1, length)
        if length % period == 0
    ]


def exact_cube_formulas(word: list[BoolRef]) -> list[BoolRef]:
    length = len(word)
    return [
        word[cut]
        == Or(
            *(
                power(word, cut, root, 3, True)
                for root in range(1, length)
            )
        )
        for cut in range(length)
    ]


def low_branch(x: int, h: int, c: int):
    """Return the branch ``D=X H X H X``."""
    if min(x, h, c) < 1:
        raise ValueError
    X = [Bool(f"X_{i}") for i in range(x)]
    H = [Bool(f"H_{i}") for i in range(h)]
    C = [Bool(f"C_{i}") for i in range(c)]
    D = X + H + X + H + X
    A = D + D + C
    V = D + C
    Q = A + V + A
    base = [Not(X[0]), C[0]]
    base.extend(
        H[index] == D[len(D) - len(H) + index]
        for index in range(len(H))
    )
    base.extend(primitive_constraints(D))
    base.extend(autonomous_one(A))
    base.extend(autonomous_one(Q))
    return X + H + C, D, A, Q, base, exact_cube_formulas(A)


def high_branch(d: int, e: int, c: int):
    """Return the branch with ``D`` period ``e`` and cube root ``d+e``."""
    if not (1 <= e < d and c >= 1):
        raise ValueError
    D = [Bool(f"D_{i}") for i in range(d)]
    C = [Bool(f"C_{i}") for i in range(c)]
    A = D + D + C
    V = D + C
    Q = A + V + A
    base = [Not(D[0]), C[0]]
    base.extend(D[index] == D[index - e] for index in range(e, d))
    base.extend(primitive_constraints(D))
    base.append(power(A, 2 * d, d + e, 3, True))
    base.extend(autonomous_one(A))
    base.extend(autonomous_one(Q))
    return D + C, D, A, Q, base, exact_cube_formulas(A)


def solve(base, formulas, cuts, timeout_ms: int):
    solver = Solver()
    solver.set(timeout=timeout_ms)
    solver.add(*base)
    solver.add(*(formulas[cut] for cut in cuts))
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
            trial = [candidate for candidate in cuts if candidate != cut]
            trial_result, _ = solve(base, formulas, trial, timeout_ms)
            if str(trial_result) == "unsat":
                cuts = trial
                changed = True
    return result, cuts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("branch", choices=("low", "high"))
    parser.add_argument("one", type=int)
    parser.add_argument("two", type=int)
    parser.add_argument("c", type=int)
    parser.add_argument("--timeout-ms", type=int, default=30_000)
    parser.add_argument("--near", action="store_true")
    args = parser.parse_args()
    built = (
        low_branch(args.one, args.two, args.c)
        if args.branch == "low"
        else high_branch(args.one, args.two, args.c)
    )
    symbols, D, A, Q, base, formulas = built
    result, cuts = greedy(base, formulas, args.timeout_ms)
    print(
        f"branch={args.branch} params=({args.one},{args.two},{args.c}) "
        f"|D|={len(D)} |A|={len(A)} result={result} core={cuts}",
        flush=True,
    )
    if args.near and str(result) == "unsat":
        for removed in cuts:
            trial = [cut for cut in cuts if cut != removed]
            trial_result, model = solve(base, formulas, trial, args.timeout_ms)
            if model is None:
                print(f"  remove={removed} result={trial_result}")
                continue
            assignment = "".join(
                "3" if is_true(model.eval(symbol)) else "2"
                for symbol in symbols
            )
            d_word = "".join(
                "3" if is_true(model.eval(symbol)) else "2" for symbol in D
            )
            a_word = "".join(
                "3" if is_true(model.eval(symbol)) else "2" for symbol in A
            )
            print(
                f"  remove={removed} result={trial_result} "
                f"symbols={assignment} D={d_word} A={a_word}"
            )


if __name__ == "__main__":
    main()
