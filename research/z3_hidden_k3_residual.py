"""Search the last algebraic residual of a hidden cubic reset.

After the Euclidean split, the only possible form is

    U = C A,             |C| = h, |A| = a, p = h + a,
    A = U[:a] = U[h:],
    U[0] = 2, U[a] = 3.

If the child V = C A C A C were fixed, its inherited period-p cube
forces lcs(A,C) to be either zero, or one with the common symbol 3.
Also, fixedness of V would force C to be primitive.  This script asks
whether those *necessary* child conditions are already incompatible
with exact fixedness of U.

The search is a finite falsifier only.  It intentionally imposes the
proper circular profile of U, not first-copy fitting.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from z3 import Bool, Not, Or, Solver, is_true, sat  # type: ignore

from curling import curling_number, curling_number_reference
from research.check_run_length_grammar import primitive, proper_profile
from research.z3_hidden_k3_fixed_pair import (
    add_binary_fixed_replay,
    add_primitive,
)


def decode(model, bits) -> tuple[int, ...]:
    return tuple(3 if is_true(model.eval(bit)) else 2 for bit in bits)


def lcs(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    """Length of the longest common suffix of two finite words."""
    bound = min(len(left), len(right))
    return next(
        (
            length - 1
            for length in range(1, bound + 2)
            if left[-length:] != right[-length:]
        ),
        bound,
    )


def exact_fixed(word: tuple[int, ...]) -> bool:
    """Cross-check the circular profile by two direct CN implementations."""
    if proper_profile(word) != word:
        return False
    for cut, label in enumerate(word):
        state = word + word[:cut]
        if (
            curling_number(state) != label
            or curling_number_reference(state) != label
        ):
            return False
    return True


def build(p: int, a: int):
    h = p - a
    solver = Solver()
    u = [Bool(f"u_{p}_{a}_{i}") for i in range(p)]

    # False denotes 2 and True denotes 3.
    solver.add(Not(u[0]))
    solver.add(u[a])
    solver.add(*(u[i] == u[h + i] for i in range(a)))
    add_primitive(solver, u)
    add_primitive(solver, u[:h])

    # Necessary seam condition from the inherited period-p cube:
    # lcs(A,C)=0, or lcs(A,C)=1 and the common symbol is 3.
    seam_zero = u[a - 1] != u[h - 1]
    if a == 1:
        solver.add(seam_zero)
    else:
        seam_one_high = (
            u[a - 1]
            & u[h - 1]
            & (u[a - 2] != u[h - 2])
        )
        solver.add(Or(seam_zero, seam_one_high))

    add_binary_fixed_replay(solver, u, "U", fitting=False)
    return solver, u


def audit_model(model, bits, a: int):
    u = decode(model, bits)
    p = len(u)
    h = p - a
    c = u[:h]
    aa = u[:a]
    v = u + u + u[:h]

    assert u[h:] == aa
    assert u[0] == 2 and u[a] == 3
    assert primitive(u) and primitive(c)
    assert exact_fixed(u)
    seam = lcs(aa, c)
    assert seam == 0 or (
        seam == 1 and aa[-1] == c[-1] == 3
    )

    v_profile = proper_profile(v)
    mismatches = tuple(
        (cut, v[cut], v_profile[cut])
        for cut in range(len(v))
        if v[cut] != v_profile[cut]
    )
    return u, c, v, seam, mismatches


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("p_min", type=int)
    parser.add_argument("p_max", type=int)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--timeout-ms", type=int, default=0)
    args = parser.parse_args()

    checked = unknown = models = 0
    for p in range(max(3, args.p_min), args.p_max + 1):
        for a in range(1, (p - 1) // 2 + 1):
            solver, bits = build(p, a)
            if args.timeout_ms:
                solver.set(timeout=args.timeout_ms)
            result = solver.check()
            checked += 1
            if result == sat:
                u, c, v, seam, mismatches = audit_model(
                    solver.model(), bits, a
                )
                print(
                    f"SAT p={p} a={a} h={p-a} seam={seam} "
                    f"U={''.join(map(str, u))} "
                    f"C={''.join(map(str, c))}"
                )
                print(
                    "V-mismatches="
                    + ",".join(
                        f"{cut}:{label}->{actual}"
                        for cut, label, actual in mismatches
                    )
                )
                models += 1
                if not args.all:
                    print(
                        f"checked={checked} unknown={unknown} "
                        f"models={models}"
                    )
                    return
            elif str(result) == "unknown":
                unknown += 1
                print(
                    f"UNKNOWN p={p} a={a} "
                    f"reason={solver.reason_unknown()}"
                )
    print(f"checked={checked} unknown={unknown} models={models}")


if __name__ == "__main__":
    main()
