"""Unsat-core diagnostics for the still-valid final-3 cn(Z)=2 branches.

For fixed ``x=|X|`` and ``s=|B|`` this encodes either

    k=0: A=B,   Z=B X,     Q=X B X B X,
    k=1: A=B X, Z=B X X,   Q=X B X X B X X,

where ``B`` is the length-``s`` suffix of ``X``.  It imposes the exact
proper circular {2,3}-profile, inherited positive-phase fitting,
``cn(Q[1:]) <= 2``, and ``cn(Z)=2``.  Per-cut constraints are guarded by
assumption literals so Z3 can expose small conflicting sets of cuts.

This is a fixed-length diagnostic.  An UNSAT core is not an unbounded
proof.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))

from z3 import And, Bool, BoolVal, Implies, Not, Or, Solver, unsat


def nonempty_or(items):
    items = tuple(items)
    return Or(*items) if items else BoolVal(False)


def power_at_cut(word, cut: int, exponent: int, root: int):
    n = len(word)
    return And(
        *(
            word[(cut - block * root + offset) % n]
            == word[(cut - root + offset) % n]
            for block in range(2, exponent + 1)
            for offset in range(root)
        )
    )


def finite_suffix_power(word, exponent: int, root: int):
    n = len(word)
    return And(
        *(
            word[n - block * root + offset]
            == word[n - root + offset]
            for block in range(2, exponent + 1)
            for offset in range(root)
        )
    )


def primitive_constraint(word):
    n = len(word)
    return And(
        *(
            Or(*(word[index] != word[index % root] for index in range(root, n)))
            for root in range(1, n)
            if n % root == 0
        )
    )


def cut_description(cut: int, x: int, s: int, k: int) -> str:
    if k == 0:
        blocks = (("X1", x), ("B1", s), ("X2", x), ("B2", s), ("X3", x))
    else:
        blocks = (
            ("X1", x),
            ("B1", s),
            ("X2", x),
            ("X3", x),
            ("B2", s),
            ("X4", x),
            ("X5", x),
        )
    position = 0
    for name, length in blocks:
        if position <= cut < position + length:
            return f"{name}+{cut-position}"
        position += length
    raise AssertionError((cut, position))


def build_case(x_length: int, s_length: int, k: int):
    x = [Bool(f"x_{index}") for index in range(x_length)]
    b = x[x_length - s_length :]
    if k == 0:
        a = b
    else:
        a = b + x
    z = a + x
    q = x + z + z
    t = q[1:]
    n = len(q)

    solver = Solver()
    solver.set(unsat_core=True)
    assumptions = []
    labels = {}

    def guarded(name: str, formula):
        literal = Bool(name)
        assumptions.append(literal)
        labels[literal.decl().name()] = name
        solver.add(Implies(literal, formula))

    guarded(
        "base_symbols",
        And(
            x[0] == BoolVal(True),
            x[1] == BoolVal(False),
            b[0] == BoolVal(False),
        ),
    )
    guarded("base_primitive", primitive_constraint(q))
    guarded(
        "base_cnT_le_2",
        And(
            *(
                Not(finite_suffix_power(t, 3, root))
                for root in range(1, len(t) // 3 + 1)
            )
        ),
    )
    guarded(
        "base_cnZ_eq_2",
        And(
            nonempty_or(
                finite_suffix_power(z, 2, root)
                for root in range(1, len(z) // 2 + 1)
            ),
            *(
                Not(finite_suffix_power(z, 3, root))
                for root in range(1, len(z) // 3 + 1)
            ),
        ),
    )

    for cut, symbol in enumerate(q):
        bound = None if cut == 0 else n + cut - 2
        fitting_square_roots = (
            root
            for root in range(1, n)
            if bound is None or 2 * root <= bound
        )
        fitting_cube_roots = (
            root
            for root in range(1, n)
            if bound is None or 3 * root <= bound
        )
        target = Or(
            And(
                Not(symbol),
                nonempty_or(
                    power_at_cut(q, cut, 2, root)
                    for root in fitting_square_roots
                ),
            ),
            And(
                symbol,
                nonempty_or(
                    power_at_cut(q, cut, 3, root)
                    for root in fitting_cube_roots
                ),
            ),
        )
        upper = Or(
            And(
                Not(symbol),
                And(
                    *(
                        Not(power_at_cut(q, cut, 3, root))
                        for root in range(1, n)
                    )
                ),
            ),
            And(
                symbol,
                And(
                    *(
                        Not(power_at_cut(q, cut, 4, root))
                        for root in range(1, n)
                    )
                ),
            ),
        )
        guarded(f"target_{cut}", target)
        guarded(f"upper_{cut}", upper)

    return solver, assumptions, labels, q


def minimize_core(solver: Solver, core):
    current = list(core)
    index = 0
    while index < len(current):
        trial = current[:index] + current[index + 1 :]
        if solver.check(*trial) == unsat:
            current = trial
        else:
            index += 1
    return tuple(current)


def solve_case(x_length: int, s_length: int, k: int):
    solver, assumptions, labels, q = build_case(x_length, s_length, k)
    result = solver.check(*assumptions)
    if result != unsat:
        return result, (), len(q)
    core = minimize_core(solver, solver.unsat_core())
    return result, tuple(labels[item.decl().name()] for item in core), len(q)


def normalized_core(core, x: int, s: int, k: int):
    normalized = []
    for name in core:
        if name.startswith("target_") or name.startswith("upper_"):
            kind, raw_cut = name.split("_", 1)
            cut = int(raw_cut)
            normalized.append(f"{kind}:{cut_description(cut, x, s, k)}")
        else:
            normalized.append(name)
    return tuple(normalized)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-x", type=int, default=10)
    parser.add_argument("--k", type=int, choices=(0, 1))
    args = parser.parse_args()

    counts = Counter()
    examples = defaultdict(list)
    branches = (args.k,) if args.k is not None else (0, 1)
    for k in branches:
        for x_length in range(2, args.max_x + 1):
            for s_length in range(1, x_length):
                result, core, n = solve_case(x_length, s_length, k)
                normalized = normalized_core(core, x_length, s_length, k)
                key = (k, str(result), normalized)
                counts[key] += 1
                if len(examples[key]) < 8:
                    examples[key].append((x_length, s_length, n, core))
            print(f"k={k} audited through |X|={x_length}")

    for key, count in counts.most_common():
        print(f"count={count} signature={key}")
        for example in examples[key]:
            print(f"  {example}")


if __name__ == "__main__":
    main()

