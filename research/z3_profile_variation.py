"""Search for a counterexample to the binary profile-variation inequality.

For a primitive binary circular word ``Q``, let ``F`` be its exact proper
circular curling profile.  This encoding restricts ``F`` to ``{2,3}``
and asks whether

    Var(F) > Var(Q),

where variation counts cyclic adjacent changes.  A satisfying model is
recomputed by the direct profile implementation before it is reported.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, If, Not, Or, Solver, Sum, is_true, sat  # type: ignore

from check_run_length_grammar import primitive, proper_profile


def build_solver(n: int, timeout_ms: int):
    if n < 2:
        raise ValueError("n must be at least two")

    solver = Solver()
    solver.set(timeout=timeout_ms)
    word = [Bool(f"w_{i}") for i in range(n)]  # True=3, False=2

    # Complement and rotation symmetry: cut zero is a 3->2 boundary.
    solver.add(word[-1], Not(word[0]))

    square = {}
    cube = {}
    fourth = {}
    for cut in range(n):
        for p in range(1, n):
            copy_2 = And(
                *(
                    word[(cut - 2 * p + j) % n]
                    == word[(cut - p + j) % n]
                    for j in range(p)
                )
            )
            copy_3 = And(
                *(
                    word[(cut - 3 * p + j) % n]
                    == word[(cut - p + j) % n]
                    for j in range(p)
                )
            )
            copy_4 = And(
                *(
                    word[(cut - 4 * p + j) % n]
                    == word[(cut - p + j) % n]
                    for j in range(p)
                )
            )
            square[cut, p] = copy_2
            cube[cut, p] = And(copy_2, copy_3)
            fourth[cut, p] = And(copy_2, copy_3, copy_4)

    profile_is_three = []
    for cut in range(n):
        solver.add(Or(*(square[cut, p] for p in range(1, n))))
        solver.add(*(Not(fourth[cut, p]) for p in range(1, n)))
        profile_is_three.append(
            Or(*(cube[cut, p] for p in range(1, n)))
        )

    word_variation = Sum(
        *[
            If(word[i] != word[(i + 1) % n], 1, 0)
            for i in range(n)
        ]
    )
    profile_variation = Sum(
        *[
            If(
                profile_is_three[i]
                != profile_is_three[(i + 1) % n],
                1,
                0,
            )
            for i in range(n)
        ]
    )
    solver.add(profile_variation > word_variation)
    return solver, word


def solve_length(n: int, timeout_ms: int) -> str:
    solver, symbols = build_solver(n, timeout_ms)
    result = solver.check()
    if result != sat:
        return str(result)

    model = solver.model()
    q = tuple(3 if is_true(model.eval(x)) else 2 for x in symbols)
    f = proper_profile(q)
    var_q = sum(q[i] != q[(i + 1) % n] for i in range(n))
    var_f = sum(f[i] != f[(i + 1) % n] for i in range(n))

    assert primitive(q)
    assert all(value in (2, 3) for value in f)
    assert var_f > var_q
    return (
        f"sat Q={''.join(map(str, q))} "
        f"F={''.join(map(str, f))} "
        f"Var(Q)={var_q} Var(F)={var_f}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("max_n", type=int)
    parser.add_argument("--min-n", type=int, default=2)
    parser.add_argument("--timeout-ms", type=int, default=30_000)
    args = parser.parse_args()

    for n in range(args.min_n, args.max_n + 1):
        print(f"n={n}: {solve_length(n, args.timeout_ms)}", flush=True)


if __name__ == "__main__":
    main()
