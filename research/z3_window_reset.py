"""SMT search for a binary finite-window reset counterexample.

The target statement is:

    If a primitive word P satisfies pc(P)=P and P[0]=2, and the orbit
    from P^3 3 avoids 1 for p=|P| outputs, then those p outputs form a
    cyclic rotation of P (with the preceding promoted 3 aligned too).

This model searches the binary subcase P,D in {2,3}.  A satisfying
assignment is always rechecked using the independent executable
definitions from ``curling.py`` and ``check_run_length_grammar.py``.
The SMT encoding may use the proved post-promotion bound and therefore
only asks for roots shorter than p; exact rechecking considers every
root length.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE / ".vendor"))
sys.path.insert(0, str(ROOT))

from z3 import And, Bool, BoolVal, Not, Or, Solver, is_true, sat  # type: ignore

from curling import curling_number, curling_number_reference
from research.check_run_length_grammar import primitive, proper_profile


def nonempty_and(items):
    items = tuple(items)
    return And(*items) if items else BoolVal(True)


def nonempty_or(items):
    items = tuple(items)
    return Or(*items) if items else BoolVal(False)


def build_solver(p: int, timeout_ms: int, require_nonfactor: bool):
    """Build the exact binary-profile/short-root orbit encoding."""
    if p < 2:
        raise ValueError("p must be at least two")

    solver = Solver()
    solver.set(timeout=timeout_ms)

    # True denotes 3 and False denotes 2.
    word = [Bool(f"P_{i}") for i in range(p)]
    output = [Bool(f"D_{i}") for i in range(p + 1)]
    solver.add(Not(word[0]))
    solver.add(output[0])  # the promoted symbol 3

    # Cyclic primitivity: every nonzero shift changes some position.
    for shift in range(1, p):
        solver.add(
            Or(*(word[i] != word[(i + shift) % p] for i in range(p)))
        )

    def circular_power(cut: int, root: int, exponent: int):
        return And(
            *(
                word[(cut - block * root + j) % p]
                == word[(cut - root + j) % p]
                for block in range(2, exponent + 1)
                for j in range(root)
            )
        )

    # pc(P)=P in the alphabet {2,3}: every cut has a square, a cut is
    # labelled 3 exactly when it has a cube, and no cut has a fourth
    # power.
    for cut in range(p):
        squares = [circular_power(cut, root, 2) for root in range(1, p)]
        cubes = [circular_power(cut, root, 3) for root in range(1, p)]
        fourths = [
            circular_power(cut, root, 4) for root in range(1, p)
        ]
        solver.add(Or(*squares))
        solver.add(word[cut] == Or(*cubes))
        solver.add(*(Not(power) for power in fourths))

    def finite_symbol(index: int):
        if index < 3 * p:
            return word[index % p]
        return output[index - 3 * p]

    def finite_power(end: int, root: int, exponent: int):
        assert exponent * root <= end
        return And(
            *(
                finite_symbol(end - block * root + j)
                == finite_symbol(end - root + j)
                for block in range(2, exponent + 1)
                for j in range(root)
            )
        )

    # At state P^3 D[:e], 1<=e<=p, the next output D[e] is 2 or 3.
    # The post-promotion root theorem permits restriction to root<p.
    for e in range(1, p + 1):
        end = 3 * p + e
        squares = [
            finite_power(end, root, 2) for root in range(1, p)
        ]
        cubes = [
            finite_power(end, root, 3)
            for root in range(1, p)
            if 3 * root <= end
        ]
        fourths = [
            finite_power(end, root, 4)
            for root in range(1, p)
            if 4 * root <= end
        ]
        solver.add(Or(*squares))
        solver.add(output[e] == nonempty_or(cubes))
        solver.add(*(Not(power) for power in fourths))

    # A reset requires D[0:p+1] to be a length-(p+1) cyclic factor of
    # P.  Ask for its negation when looking for a counterexample.
    if require_nonfactor:
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
    p_word = tuple(3 if is_true(model.eval(x)) else 2 for x in word)
    d_model = tuple(3 if is_true(model.eval(x)) else 2 for x in output)

    assert primitive(p_word)
    assert proper_profile(p_word) == p_word
    state = p_word * 3 + (3,)
    produced: list[int] = []
    spectra: list[tuple[int, ...]] = []
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
    d_exact = (3,) + tuple(produced)
    assert d_exact == d_model
    assert all(value in (2, 3) for value in produced)
    return {
        "P": "".join(map(str, p_word)),
        "D": "".join(map(str, d_exact)),
        "H": "".join(map(str, produced)),
        "D_is_cyclic_factor": cyclic_factor(p_word, d_exact),
        "H_is_rotation": cyclic_factor(p_word, tuple(produced)),
        "root_spectra": spectra,
    }


def solve(p: int, timeout_ms: int, require_nonfactor: bool):
    solver, word, output = build_solver(p, timeout_ms, require_nonfactor)
    result = solver.check()
    if result != sat:
        return str(result), None
    certificate = extract_and_verify(solver.model(), word, output)
    return str(result), certificate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=int)
    parser.add_argument("--timeout-ms", type=int, default=120_000)
    parser.add_argument(
        "--allow-reset",
        action="store_true",
        help="find any surviving model, rather than a nonreset model",
    )
    args = parser.parse_args()
    status, certificate = solve(
        args.p, args.timeout_ms, not args.allow_reset
    )
    print({"p": args.p, "status": status, "certificate": certificate})


if __name__ == "__main__":
    main()
