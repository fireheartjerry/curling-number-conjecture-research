"""Exact integer-alphabet SMT search for the finite-window reset claim.

Unlike ``z3_window_reset.py``, symbols are unbounded integer variables
whose values are constrained to equal their exact proper circular
curling numbers.  Finite-state curling numbers are represented as the
maximum of the exact suffix exponents for every root shorter than p;
the proved post-promotion root bound justifies that restriction while
the resulting model is still rechecked against every root length.
"""

from __future__ import annotations

import argparse
from math import gcd
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE / ".vendor"))
sys.path.insert(0, str(ROOT))

from z3 import And, BoolVal, If, Int, Not, Or, Solver, Sum, sat  # type: ignore

from curling import curling_number, curling_number_reference
from research.check_run_length_grammar import primitive, proper_profile


def conjunction(items):
    items = tuple(items)
    return And(*items) if items else BoolVal(True)


def exact_exponent(block_equalities):
    """Return one plus the number of consecutively equal prior blocks."""
    prefix = BoolVal(True)
    at_least = []
    for equality in block_equalities:
        prefix = And(prefix, equality)
        at_least.append(prefix)
    return 1 + Sum(*(If(condition, 1, 0) for condition in at_least))


def constrain_maximum(solver, maximum, candidates) -> None:
    candidates = tuple(candidates)
    solver.add(*(maximum >= candidate for candidate in candidates))
    solver.add(Or(*(maximum == candidate for candidate in candidates)))


def build_solver(
    p: int,
    timeout_ms: int,
    require_nonfactor: bool,
    orbit_steps: int | None = None,
):
    if p < 2:
        raise ValueError("p must be at least two")
    solver = Solver()
    solver.set(timeout=timeout_ms)

    word = [Int(f"P_{i}") for i in range(p)]
    output = [Int(f"D_{i}") for i in range(p + 1)]
    solver.add(word[0] == 2)
    solver.add(output[0] == 3)

    # Cyclic primitivity.
    for shift in range(1, p):
        solver.add(
            Or(*(word[i] != word[(i + shift) % p] for i in range(p)))
        )

    # Exact pc(P)=P.  If P is primitive, Fine--Wilf bounds the exponent
    # for root r by floor((p+r-gcd(p,r)-1)/r).
    for cut in range(p):
        root_exponents = []
        for root in range(1, p):
            cap = (p + root - gcd(p, root) - 1) // root
            block_equalities = []
            for block in range(2, cap + 1):
                block_equalities.append(
                    And(
                        *(
                            word[(cut - block * root + j) % p]
                            == word[(cut - root + j) % p]
                            for j in range(root)
                        )
                    )
                )
            # Equality for one further block is incompatible with
            # primitivity by the same Fine--Wilf bound.
            forbidden_block = cap + 1
            forbidden_power = And(
                *(
                    word[(cut - block * root + j) % p]
                    == word[(cut - root + j) % p]
                    for block in range(2, forbidden_block + 1)
                    for j in range(root)
                )
            )
            solver.add(Not(forbidden_power))
            root_exponents.append(exact_exponent(block_equalities))
        constrain_maximum(solver, word[cut], root_exponents)

    def finite_symbol(index: int):
        if index < 3 * p:
            return word[index % p]
        return output[index - 3 * p]

    if orbit_steps is None:
        orbit_steps = p
    if not 0 <= orbit_steps <= p:
        raise ValueError("orbit_steps must lie between zero and p")

    # Exact orbit outputs, using the theorem that a maximizing root is
    # shorter than p throughout this window.
    for e in range(1, orbit_steps + 1):
        end = 3 * p + e
        root_exponents = []
        for root in range(1, p):
            block_equalities = []
            for block in range(2, end // root + 1):
                block_equalities.append(
                    And(
                        *(
                            finite_symbol(end - block * root + j)
                            == finite_symbol(end - root + j)
                            for j in range(root)
                        )
                    )
                )
            root_exponents.append(exact_exponent(block_equalities))
        constrain_maximum(solver, output[e], root_exponents)
        solver.add(output[e] >= 2)

    if require_nonfactor:
        if orbit_steps != p:
            raise ValueError("nonfactor search requires all p orbit steps")
        for start in range(p):
            solver.add(
                Or(
                    *(
                        output[i] != word[(start + i) % p]
                        for i in range(p + 1)
                    )
                )
            )

    return solver, word, output


def exact_cn(word: tuple[int, ...]) -> int:
    fast = curling_number(word)
    slow = curling_number_reference(word)
    assert fast == slow
    return fast


def cyclic_factor(
    p_word: tuple[int, ...], candidate: tuple[int, ...]
) -> bool:
    p = len(p_word)
    return any(
        candidate
        == tuple(p_word[(start + i) % p] for i in range(len(candidate)))
        for start in range(p)
    )


def extract_and_verify(model, word, output):
    p_word = tuple(model.eval(symbol).as_long() for symbol in word)
    d_model = tuple(model.eval(symbol).as_long() for symbol in output)
    assert primitive(p_word)
    assert proper_profile(p_word) == p_word

    state = p_word * 3 + (3,)
    produced = []
    spectra = []
    for _ in range(len(p_word)):
        value = exact_cn(state)
        produced.append(value)
        roots = tuple(
            root
            for root in range(1, len(state) // value + 1)
            if state[-value * root :] == state[-root:] * value
        )
        spectra.append(roots)
        state += (value,)
    exact_d = (3,) + tuple(produced)
    assert exact_d == d_model
    assert all(value >= 2 for value in produced)
    return {
        "P": p_word,
        "D": exact_d,
        "D_is_cyclic_factor": cyclic_factor(p_word, exact_d),
        "H_is_rotation": cyclic_factor(p_word, tuple(produced)),
        "root_spectra": spectra,
    }


def solve(p: int, timeout_ms: int, require_nonfactor: bool):
    solver, word, output = build_solver(p, timeout_ms, require_nonfactor)
    status = solver.check()
    if status != sat:
        return str(status), None
    return str(status), extract_and_verify(solver.model(), word, output)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=int)
    parser.add_argument("--timeout-ms", type=int, default=120_000)
    parser.add_argument("--allow-reset", action="store_true")
    args = parser.parse_args()
    status, certificate = solve(
        args.p, args.timeout_ms, not args.allow_reset
    )
    print({"p": args.p, "status": status, "certificate": certificate})


if __name__ == "__main__":
    main()
