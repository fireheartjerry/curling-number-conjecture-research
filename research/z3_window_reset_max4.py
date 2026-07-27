"""Efficient finite-window reset search over the alphabet {2,3,4}.

Each symbol is represented monotonically by two Booleans ``ge3, ge4``.
The circular fixed-profile and every post-promotion output are exact:

* a square exists at every relevant cut;
* ``ge3`` is equivalent to existence of a cube;
* ``ge4`` is equivalent to existence of a fourth power; and
* no fifth power exists.

The proved first-window root bound permits finite roots to be restricted
to lengths below p.  Any satisfying model is independently executed
with the unrestricted curling-number implementation.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE / ".vendor"))
sys.path.insert(0, str(ROOT))

from z3 import And, Bool, Not, Or, Solver, is_true, sat  # type: ignore

from curling import curling_number, curling_number_reference
from research.check_run_length_grammar import primitive, proper_profile


def build_solver(p: int, timeout_ms: int, require_nonfactor: bool):
    solver = Solver()
    solver.set(timeout=timeout_ms)

    p3 = [Bool(f"P3_{i}") for i in range(p)]
    p4 = [Bool(f"P4_{i}") for i in range(p)]
    d3 = [Bool(f"D3_{i}") for i in range(p + 1)]
    d4 = [Bool(f"D4_{i}") for i in range(p + 1)]

    solver.add(*(Or(Not(p4[i]), p3[i]) for i in range(p)))
    solver.add(*(Or(Not(d4[i]), d3[i]) for i in range(p + 1)))
    solver.add(Not(p3[0]), Not(p4[0]))
    solver.add(d3[0], Not(d4[0]))

    def p_equal(i: int, j: int):
        return And(
            p3[i % p] == p3[j % p],
            p4[i % p] == p4[j % p],
        )

    for shift in range(1, p):
        solver.add(Or(*(Not(p_equal(i, i + shift)) for i in range(p))))

    def circular_power(cut: int, root: int, exponent: int):
        return And(
            *(
                p_equal(cut - block * root + j, cut - root + j)
                for block in range(2, exponent + 1)
                for j in range(root)
            )
        )

    for cut in range(p):
        squares = [circular_power(cut, root, 2) for root in range(1, p)]
        cubes = [circular_power(cut, root, 3) for root in range(1, p)]
        fourths = [
            circular_power(cut, root, 4) for root in range(1, p)
        ]
        fifths = [circular_power(cut, root, 5) for root in range(1, p)]
        solver.add(Or(*squares))
        solver.add(p3[cut] == Or(*cubes))
        solver.add(p4[cut] == Or(*fourths))
        solver.add(Not(Or(*fifths)))

    def finite_pair(index: int):
        if index < 3 * p:
            return p3[index % p], p4[index % p]
        return d3[index - 3 * p], d4[index - 3 * p]

    def finite_equal(i: int, j: int):
        i3, i4 = finite_pair(i)
        j3, j4 = finite_pair(j)
        return And(i3 == j3, i4 == j4)

    def finite_power(end: int, root: int, exponent: int):
        return And(
            *(
                finite_equal(
                    end - block * root + j,
                    end - root + j,
                )
                for block in range(2, exponent + 1)
                for j in range(root)
            )
        )

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
        fifths = [
            finite_power(end, root, 5)
            for root in range(1, p)
            if 5 * root <= end
        ]
        solver.add(Or(*squares))
        solver.add(d3[e] == Or(*cubes))
        solver.add(d4[e] == Or(*fourths))
        solver.add(Not(Or(*fifths)))

    if require_nonfactor:
        for start in range(p):
            solver.add(
                Or(
                    *(
                        Or(
                            d3[i] != p3[(start + i) % p],
                            d4[i] != p4[(start + i) % p],
                        )
                        for i in range(p + 1)
                    )
                )
            )

    return solver, (p3, p4), (d3, d4)


def value(model, pair, index: int) -> int:
    ge3, ge4 = pair
    return (
        4
        if is_true(model.eval(ge4[index]))
        else 3
        if is_true(model.eval(ge3[index]))
        else 2
    )


def cyclic_factor(word, candidate) -> bool:
    p = len(word)
    return any(
        candidate
        == tuple(word[(start + i) % p] for i in range(len(candidate)))
        for start in range(p)
    )


def verify(model, p_pair, d_pair):
    p = len(p_pair[0])
    word = tuple(value(model, p_pair, i) for i in range(p))
    d_model = tuple(value(model, d_pair, i) for i in range(p + 1))
    assert primitive(word)
    assert proper_profile(word) == word
    state = word * 3 + (3,)
    produced = []
    spectra = []
    for _ in range(p):
        fast = curling_number(state)
        slow = curling_number_reference(state)
        assert fast == slow
        produced.append(fast)
        spectra.append(
            tuple(
                root
                for root in range(1, len(state) // fast + 1)
                if state[-fast * root :] == state[-root:] * fast
            )
        )
        state += (fast,)
    d_exact = (3,) + tuple(produced)
    assert d_exact == d_model
    return {
        "P": "".join(map(str, word)),
        "D": "".join(map(str, d_exact)),
        "D_is_factor": cyclic_factor(word, d_exact),
        "roots": spectra,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=int)
    parser.add_argument("--timeout-ms", type=int, default=120_000)
    parser.add_argument("--allow-reset", action="store_true")
    args = parser.parse_args()
    solver, p_pair, d_pair = build_solver(
        args.p, args.timeout_ms, not args.allow_reset
    )
    status = solver.check()
    certificate = (
        verify(solver.model(), p_pair, d_pair) if status == sat else None
    )
    print({"p": args.p, "status": str(status), "certificate": certificate})


if __name__ == "__main__":
    main()
