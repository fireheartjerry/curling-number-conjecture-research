"""Root-by-root diagnostics for the circular terminal-prefix implication.

This script is proof-discovery instrumentation.  It fixes the final label and
one long terminal power root, tracks the circular cube-profile equation at
each cut, and greedily minimizes the set of cuts needed for bounded UNSAT.
The resulting cores are finite evidence only.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))

from z3 import And, Bool, BoolRef, Not, Or, Solver, is_true, sat  # type: ignore


def build_formulas(n: int, final_label: int, root: int):
    word = [Bool(f"w_{index}") for index in range(n)]

    def power(cut: int, q: int, exponent: int) -> BoolRef:
        return And(
            *(
                word[(cut - block * q + offset) % n]
                == word[(cut - q + offset) % n]
                for block in range(2, exponent + 1)
                for offset in range(q)
            )
        )

    cubes = {
        (cut, q): power(cut, q, 3)
        for cut in range(n)
        for q in range(1, n)
    }
    squares = {
        (cut, q): power(cut, q, 2)
        for cut in range(n)
        for q in range(1, n)
    }

    cut_formulas = [
        word[cut] == Or(*(cubes[cut, q] for q in range(1, n)))
        for cut in range(n)
    ]
    base = [Not(word[0]), word[-1] if final_label == 3 else Not(word[-1])]

    terminal_exponent = final_label
    base.append(
        cubes[n - 1, root]
        if terminal_exponent == 3
        else squares[n - 1, root]
    )

    short_roots = range(1, (n - 1) // terminal_exponent + 1)
    short_powers = [
        cubes[n - 1, q] if terminal_exponent == 3 else squares[n - 1, q]
        for q in short_roots
    ]
    if short_powers:
        base.append(Not(Or(*short_powers)))
    return word, base, cut_formulas


def check_subset(base, cut_formulas, cuts, timeout_ms: int):
    solver = Solver()
    if timeout_ms:
        solver.set(timeout=timeout_ms)
    solver.add(*base)
    solver.add(*(cut_formulas[cut] for cut in cuts))
    result = solver.check()
    model_word = None
    if result == sat:
        model = solver.model()
        model_word = "".join(
            "3" if is_true(model.eval(symbol)) else "2" for symbol in symbols
        )
    return result, model_word


def greedy_core(base, cut_formulas, n: int, timeout_ms: int):
    cuts = list(range(n))
    result, _ = check_subset(base, cut_formulas, cuts, timeout_ms)
    if str(result) != "unsat":
        return result, cuts
    changed = True
    while changed:
        changed = False
        for cut in tuple(cuts):
            trial = [other for other in cuts if other != cut]
            trial_result, _ = check_subset(
                base, cut_formulas, trial, timeout_ms
            )
            if str(trial_result) == "unsat":
                cuts = trial
                changed = True
    return result, cuts


def candidate_roots(n: int, final_label: int):
    exponent = final_label
    return range((n - 1) // exponent + 1, n)


def concrete_power(word: str, cut: int, root: int, exponent: int) -> bool:
    n = len(word)
    return all(
        word[(cut - block * root + offset) % n]
        == word[(cut - root + offset) % n]
        for block in range(2, exponent + 1)
        for offset in range(root)
    )


def cut_summary(word: str, cut: int) -> str:
    roots = [
        root
        for root in range(1, len(word))
        if concrete_power(word, cut, root, 3)
    ]
    return f"cut={cut} label={word[cut]} cube_roots={roots}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--final", type=int, choices=(2, 3), required=True)
    parser.add_argument("--root", type=int)
    parser.add_argument("--timeout-ms", type=int, default=30_000)
    parser.add_argument("--show-near-models", action="store_true")
    args = parser.parse_args()

    roots = (
        [args.root]
        if args.root is not None
        else candidate_roots(args.n, args.final)
    )
    for root in roots:
        global symbols
        symbols, base, cut_formulas = build_formulas(
            args.n, args.final, root
        )
        result, cuts = greedy_core(
            base, cut_formulas, args.n, args.timeout_ms
        )
        print(
            f"n={args.n} final={args.final} root={root} "
            f"result={result} cuts={','.join(map(str, cuts))}",
            flush=True,
        )
        if args.show_near_models and str(result) == "unsat":
            for removed in cuts:
                trial = [cut for cut in cuts if cut != removed]
                trial_result, model_word = check_subset(
                    base, cut_formulas, trial, args.timeout_ms
                )
                print(
                    f"  remove={removed} result={trial_result} "
                    f"model={model_word}",
                    flush=True,
                )
                if model_word is not None:
                    print("    " + cut_summary(model_word, removed))


if __name__ == "__main__":
    main()
