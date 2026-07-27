"""Search the exact singleton-3 fixed-profile run-code system.

For a cyclic code A in {1,2,3}^m, expand

    Q(A) = product_i 2**A[i] 3.

The constraints below say exactly that the proper circular curling
profile of Q(A) equals Q(A):

* every cut whose next symbol is 2 has a square and no cube;
* every cut whose next symbol is 3 has a cube and no fourth power; and
* every root is proper (physical root length < |Q|).

The power predicates use run counts, not a bounded physical-word
unrolling.  ``--nontrivial`` additionally requires a cube ending before
a 3 whose root contains at least two 3 symbols.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import (  # type: ignore
    And,
    Implies,
    Int,
    Not,
    Or,
    Solver,
    Sum,
    is_true,
    sat,
)

from check_run_length_grammar import binary_word, primitive, proper_profile


def build_solver(m: int, require_nontrivial: bool, timeout_ms: int):
    solver = Solver()
    solver.set(timeout=timeout_ms)
    a = [Int(f"a_{i}") for i in range(m)]
    for x in a:
        solver.add(1 <= x, x <= 3)

    # Rotation symmetry breaking: put a minimum run length at index zero.
    solver.add(*(a[0] <= x for x in a))

    # A primitive run code gives a primitive binary circular word.
    for p in range(1, m):
        if m % p == 0:
            solver.add(Or(*(a[j] != a[j % p] for j in range(p, m))))

    binary_length = Sum(*(x + 1 for x in a))

    def power(i: int, r, h: int, exponent: int):
        """A proper nonunary exponent-th power at cut (i,r)."""
        base = a[(i - h) % m]
        clauses = [
            r <= base,
            a[(i - exponent * h) % m] >= base - r,
            Sum(*(a[(i - h + j) % m] + 1 for j in range(h)))
            < binary_length,
        ]
        # All intermediate copy boundaries occur at the same offset r.
        clauses.extend(
            a[(i - block * h) % m] == base
            for block in range(2, exponent)
        )
        # The h-1 complete internal runs agree in every copy.
        clauses.extend(
            a[(i - block * h + j) % m] == a[(i - h + j) % m]
            for block in range(2, exponent + 1)
            for j in range(1, h)
        )
        return And(*clauses)

    powers = {
        (i, r, h, exponent): power(i, r, h, exponent)
        for i in range(m)
        for r in range(3)
        for h in range(1, m)
        for exponent in (2, 3)
    }

    for i in range(m):
        # r=0 is always the cut before the first 2 in a run.
        solver.add(Or(*(powers[i, 0, h, 2] for h in range(1, m))))
        solver.add(
            Not(Or(*(powers[i, 0, h, 3] for h in range(1, m))))
        )

        # r=1 exists for a run of length at least two.
        solver.add(
            Implies(
                a[i] >= 2,
                Or(*(powers[i, 1, h, 2] for h in range(1, m))),
            )
        )
        solver.add(
            Implies(
                a[i] >= 2,
                Not(Or(*(powers[i, 1, h, 3] for h in range(1, m)))),
            )
        )

        # r=2 exists only in a length-three run.  Its unary square is
        # automatic, while a cube must still be excluded.
        solver.add(
            Implies(
                a[i] == 3,
                Not(Or(*(powers[i, 2, h, 3] for h in range(1, m)))),
            )
        )

        # At r=a_i the cut is immediately before the following 3.
        cubes = [power(i, a[i], h, 3) for h in range(1, m)]
        fourths = [power(i, a[i], h, 4) for h in range(1, m)]
        # a_i=3 supplies the unary cube 222; a_i<=2 needs a nonunary one.
        solver.add(Or(a[i] == 3, *cubes))
        # No unary fourth exists because a_i<=3.
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

    return solver, a, power


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("max_m", type=int, nargs="?", default=22)
    parser.add_argument("--min-m", type=int, default=1)
    parser.add_argument("--nontrivial", action="store_true")
    parser.add_argument("--timeout-ms", type=int, default=10_000)
    args = parser.parse_args()

    for m in range(args.min_m, args.max_m + 1):
        solver, a, power = build_solver(
            m, args.nontrivial, args.timeout_ms
        )
        result = solver.check()
        if result != sat:
            print(f"m={m}: {result}")
            continue

        classes: list[tuple[int, ...]] = []
        while result == sat:
            model = solver.model()
            code = tuple(model.eval(x).as_long() for x in a)
            q = binary_word(code)
            f = proper_profile(q)
            assert primitive(code) and primitive(q)
            assert q == f
            witnesses = tuple(
                (i, h)
                for i in range(m)
                for h in range(1, m)
                if code[i] <= 2
                and is_true(model.eval(power(i, a[i], h, 3)))
            )
            classes.append(code)
            print(
                f"m={m}: sat A={''.join(map(str, code))} "
                f"|Q|={len(q)} cube-witnesses={witnesses}"
            )

            # Enumerate rotation classes rather than individual rotations.
            for shift in range(m):
                solver.add(
                    Or(
                        *(
                            a[j] != code[(j + shift) % m]
                            for j in range(m)
                        )
                    )
                )
            result = solver.check()
        print(f"m={m}: rotation classes={len(classes)}, residual={result}")


if __name__ == "__main__":
    main()
