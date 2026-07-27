"""Search the exact late hidden-reset pair for exponent three.

Let U be a primitive proper-circular fixed profile beginning in 2.  A
hidden transition to the next reset root has

    V = U U U[:h],
    p/3 < h < p,
    h a period of U,
    U[p-h] = 3.

Both U and V are actual self-replaying reset roots, so this script imposes
both the exact binary proper-circular profile and first-copy fitting at
every phase.  It is a falsifier for the two Euclidean forms; it is not a
proof of unsatisfiability at unbounded length.
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from z3 import (  # type: ignore[import-not-found]
    And,
    Bool,
    Not,
    Or,
    Solver,
    is_true,
    sat,
)

from curling import curling_number, curling_number_reference
from research.check_run_length_grammar import primitive, proper_profile


def power(word, cut: int, root: int, exponent: int):
    """A circular exponent-power of the indicated proper root ends at cut."""
    n = len(word)
    return And(
        *(
            word[(cut - block * root + j) % n]
            == word[(cut - root + j) % n]
            for block in range(2, exponent + 1)
            for j in range(root)
        )
    )


def add_binary_fixed_replay(
    solver: Solver, word, name: str, fitting: bool = True
) -> None:
    """Impose exact {2,3} proper profile, optionally with first-copy fitting."""
    n = len(word)
    for cut in range(n):
        squares = [power(word, cut, root, 2) for root in range(1, n)]
        cubes = [power(word, cut, root, 3) for root in range(1, n)]
        fourths = [power(word, cut, root, 4) for root in range(1, n)]
        fitting_squares = [
            power(word, cut, root, 2)
            for root in range(1, n)
            if 2 * root <= n + cut
        ]
        fitting_cubes = [
            power(word, cut, root, 3)
            for root in range(1, n)
            if 3 * root <= n + cut
        ]
        solver.add(Or(*squares))
        solver.add(word[cut] == Or(*cubes))
        solver.add(Not(Or(*fourths)))
        if fitting:
            solver.add(Or(*fitting_squares))
            solver.add(word[cut] == Or(*fitting_cubes))

    # Keep assertion names available in an SMT dump/debugger.
    del name


def add_primitive(solver: Solver, word) -> None:
    n = len(word)
    for divisor in range(1, n):
        if n % divisor == 0:
            solver.add(
                Or(*(word[i] != word[i % divisor] for i in range(divisor, n)))
            )


def decode(bits) -> tuple[int, ...]:
    return tuple(3 if is_true(bit) else 2 for bit in bits)


def check_model(model, u_bits, h: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    u = decode(tuple(model.eval(x) for x in u_bits))
    v = u + u + u[:h]
    assert primitive(u)
    assert primitive(v)
    assert proper_profile(u) == u
    assert proper_profile(v) == v
    for word in (u, v):
        n = len(word)
        for cut in range(n):
            state = word + word[:cut]
            c1 = curling_number(state)
            c2 = curling_number_reference(state)
            assert c1 == c2 == word[cut]
    return u, v


def build(
    p: int, h: int, u_only: bool = False, v_only: bool = False
):
    solver = Solver()
    u = [Bool(f"u_{i}") for i in range(p)]  # False=2, True=3
    solver.add(Not(u[0]))
    solver.add(u[p - h])
    solver.add(*(u[i] == u[i + h] for i in range(p - h)))
    add_primitive(solver, u)
    v = u + u + u[:h]
    add_primitive(solver, v)
    if not v_only:
        add_binary_fixed_replay(solver, u, "U")
    if not u_only:
        add_binary_fixed_replay(solver, v, "V")
    return solver, u


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("p_min", type=int)
    parser.add_argument("p_max", type=int)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--u-only", action="store_true")
    parser.add_argument("--v-only", action="store_true")
    parser.add_argument("--timeout-ms", type=int, default=0)
    args = parser.parse_args()

    checked = 0
    unknown = 0
    models = 0
    for p in range(args.p_min, args.p_max + 1):
        for h in range(p // 3 + 1, p):
            if math.gcd(p, h) == h:
                continue
            if args.u_only and args.v_only:
                raise ValueError("--u-only and --v-only are mutually exclusive")
            solver, u_bits = build(p, h, args.u_only, args.v_only)
            if args.timeout_ms:
                solver.set(timeout=args.timeout_ms)
            result = solver.check()
            checked += 1
            if result == sat:
                if args.u_only or args.v_only:
                    u = decode(tuple(solver.model().eval(x) for x in u_bits))
                    v = u + u + u[:h]
                    assert primitive(u)
                    checked_word = v if args.v_only else u
                    assert primitive(checked_word)
                    assert proper_profile(checked_word) == checked_word
                    for cut in range(len(checked_word)):
                        state = checked_word + checked_word[:cut]
                        c1 = curling_number(state)
                        c2 = curling_number_reference(state)
                        assert c1 == c2 == checked_word[cut]
                else:
                    u, v = check_model(solver.model(), u_bits, h)
                quotient = 1 if h * 2 > p else 2
                print(
                    f"SAT p={p} h={h} quotient={quotient} "
                    f"U={''.join(map(str, u))} V={''.join(map(str, v))}"
                )
                models += 1
                if not args.all:
                    print(
                        f"checked={checked} unknown={unknown} models={models}"
                    )
                    return
            elif str(result) == "unknown":
                unknown += 1
                print(f"UNKNOWN p={p} h={h} reason={solver.reason_unknown()}")
    print(f"checked={checked} unknown={unknown} models={models}")


if __name__ == "__main__":
    main()
