"""Extract a cut-level UNSAT core for a nested binary replay candidate."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Implies, Int, Or, Solver, sat  # type: ignore

from z3_cyclic_fixed import power


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("--timeout-ms", type=int, default=120_000)
    args = parser.parse_args()
    n = args.length
    q = [Int(f"q_{i}") for i in range(n)]
    solver = Solver()
    solver.set(timeout=args.timeout_ms)
    solver.set("core.minimize", True)

    tags = []
    base = Bool("base")
    tags.append(base)
    base_constraints = [And(2 <= x, x <= 3) for x in q]
    for p in range(1, n):
        if n % p == 0:
            base_constraints.append(Or(*(q[i] != q[i % p] for i in range(p, n))))
    solver.add(Implies(base, And(*base_constraints)))

    text = "223222322232322232223" * 3 + "3"
    for i, value in enumerate(text):
        tag = Bool(f"prefix_{i}")
        tags.append(tag)
        solver.add(Implies(tag, q[i] == int(value)))

    powers = {
        (cut, root, exponent): power(q, cut, root, exponent)
        for cut in range(n)
        for root in range(1, n)
        for exponent in range(2, 5)
    }
    for cut in range(n):
        tag = Bool(f"cut_{cut}")
        tags.append(tag)
        constraints = []
        for exponent in (2, 3):
            exists = Or(*(powers[cut, root, exponent] for root in range(1, n)))
            constraints.append((q[cut] >= exponent) == exists)
            fitting = [
                root
                for root in range(1, n)
                if exponent * root <= n + cut
            ]
            fits_source = Or(*(powers[cut, root, exponent] for root in fitting))
            constraints.append((q[cut] >= exponent) == fits_source)
        constraints.append(
            ~Or(*(powers[cut, root, 4] for root in range(1, n)))
        )
        solver.add(Implies(tag, And(*constraints)))

    answer = solver.check(*tags)
    print(f"status={answer}")
    if answer == sat:
        model = solver.model()
        print("".join(str(model.eval(x).as_long()) for x in q))
    else:
        print("core=" + " ".join(str(x) for x in solver.unsat_core()))


if __name__ == "__main__":
    main()
