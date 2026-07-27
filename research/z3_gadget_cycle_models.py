"""Search negative-exact, cube-covered singleton-3 run codes.

Unlike ``z3_run_code_fixed.py``, this diagnostic does *not* require
squares at 2-labelled cuts.  It requires exactly the constraints used
by the tight gadget graph:

* every defect (run length 1 or 2) has a nonunary cube at its 3-cut;
* no 2-cut has a cube; and
* no 3-cut has a fourth power.

It then computes WSQ holes and the tight-gadget cycle graph by executed
code.  This is intended to test the proposed inequality

    number of WSQ holes >= minimum number of gadget cycles - 1.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Implies, Int, Not, Or, Solver, Sum, sat  # type: ignore

from check_run_length_grammar import binary_word, primitive, proper_profile
from explore_gadget_cycles import (
    directed_cycles,
    perfect_matchings,
    wsq_holes,
)


def build_solver(
    m: int,
    require_nontrivial: bool,
    require_g2: bool,
    timeout_ms: int,
):
    solver = Solver()
    solver.set(timeout=timeout_ms)
    a = [Int(f"a_{i}") for i in range(m)]
    for x in a:
        solver.add(1 <= x, x <= 3)
    solver.add(*(a[0] <= x for x in a))
    for p in range(1, m):
        if m % p == 0:
            solver.add(Or(*(a[j] != a[j % p] for j in range(p, m))))

    binary_length = Sum(*(x + 1 for x in a))

    def power(i: int, r, h: int, exponent: int):
        base = a[(i - h) % m]
        clauses = [
            r <= base,
            a[(i - exponent * h) % m] >= base - r,
            Sum(*(a[(i - h + j) % m] + 1 for j in range(h)))
            < binary_length,
        ]
        clauses.extend(
            a[(i - block * h) % m] == base
            for block in range(2, exponent)
        )
        clauses.extend(
            a[(i - block * h + j) % m] == a[(i - h + j) % m]
            for block in range(2, exponent + 1)
            for j in range(1, h)
        )
        return And(*clauses)

    for i in range(m):
        for r in range(3):
            solver.add(
                Implies(
                    a[i] >= r + 1,
                    Not(
                        Or(
                            *(
                                power(i, r, h, 3)
                                for h in range(1, m)
                            )
                        )
                    ),
                )
            )
        cubes = tuple(power(i, a[i], h, 3) for h in range(1, m))
        fourths = tuple(power(i, a[i], h, 4) for h in range(1, m))
        solver.add(Or(a[i] == 3, *cubes))
        solver.add(Not(Or(*fourths)))

    if require_nontrivial:
        solver.add(
            Or(
                *(
                    And(a[i] <= 2, power(i, a[i], h, 3))
                    for i in range(m)
                    for h in range(2, m)
                )
            )
        )
    if require_g2:
        solver.add(
            Or(
                *(
                    And(
                        a[i] == 1,
                        a[(i - 3 * h) % m] == 1,
                        a[(i - h) % m] == 2,
                        power(i, a[i], h, 3),
                    )
                    for i in range(m)
                    for h in range(1, m)
                )
            )
        )
    return solver, a


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("m", type=int)
    parser.add_argument("--timeout-ms", type=int, default=120_000)
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--nontrivial", action="store_true")
    parser.add_argument("--g2", action="store_true")
    args = parser.parse_args()

    solver, symbols = build_solver(
        args.m,
        args.nontrivial,
        args.g2,
        args.timeout_ms,
    )
    count = 0
    while count < args.limit and solver.check() == sat:
        model = solver.model()
        a = tuple(model.eval(x).as_long() for x in symbols)
        assert primitive(a)
        q = binary_word(a)
        f = proper_profile(q)
        holes = wsq_holes(a)
        matchings = perfect_matchings(a, limit=1000)
        cycle_counts = tuple(
            sorted({len(directed_cycles(x)) for x in matchings})
        )
        print(
            f"A={''.join(map(str, a))} |Q|={len(q)} "
            f"holes={holes} matchings={len(matchings)} "
            f"cycles={cycle_counts} disagreements="
            f"{tuple(i for i, (x, y) in enumerate(zip(q, f)) if x != y)}"
        )
        count += 1
        for shift in range(args.m):
            solver.add(
                Or(
                    *(
                        symbols[j] != a[(j + shift) % args.m]
                        for j in range(args.m)
                    )
                )
            )
    print(f"models={count}, residual={solver.check()}")


if __name__ == "__main__":
    main()
