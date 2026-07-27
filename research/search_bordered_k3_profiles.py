"""Search the residual late-bordered ``k=3`` fixed-profile normal form.

For nonempty words U,C the equations are

    Y = U C = D U,
    Q = C U C U C,
    pc_Q = Q,
    Q[0] = 3,
    cn(Q) = 2.

The suffix-border equation is imposed directly on ``Y=UC``.  This is a
bounded falsifier only.
"""

from __future__ import annotations

import argparse
from math import gcd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Not, Or, sat  # type: ignore[import-not-found]

from z3_cyclic_fixed import build_solver, power


def shapes(length: int) -> tuple[tuple[int, int], ...]:
    """Return ``(c,h)`` with ``length=3c+2h`` and the border bound."""
    result = []
    for h in range(1, length):
        residual = length - 2 * h
        if residual <= 0 or residual % 3:
            continue
        c = residual // 3
        r = c + h
        if h < r - gcd(r, h):
            result.append((c, h))
    return tuple(result)


def structure(q, c: int, h: int):
    """Encode Q=C U C U C and suffix_h(U C)=U."""
    constraints = []
    first_u = c
    second_c = c + h
    second_u = 2 * c + h
    third_c = 2 * c + 2 * h
    constraints.extend(q[second_c + i] == q[i] for i in range(c))
    constraints.extend(
        q[second_u + i] == q[first_u + i] for i in range(h)
    )
    constraints.extend(q[third_c + i] == q[i] for i in range(c))

    y = list(q[first_u : first_u + h]) + list(q[:c])
    u = list(q[first_u : first_u + h])
    constraints.extend(
        y[len(y) - h + i] == u[i] for i in range(h)
    )
    return And(*constraints)


def search_length(length: int, max_symbol: int, timeout_ms: int):
    candidates = shapes(length)
    if not candidates:
        return "no-shape", None

    solver, q = build_solver(
        length, max_symbol, first_symbol=3
    )
    if timeout_ms:
        solver.set(timeout=timeout_ms)
    solver.add(
        Or(*(structure(q, c, h) for c, h in candidates))
    )
    # cn(Q)=2: the displayed terminal Y^2 supplies the lower bound;
    # exclude every fitting cube at phase zero.
    solver.add(
        *(
            Not(power(q, 0, root, 3))
            for root in range(1, length // 3 + 1)
        )
    )

    result = solver.check()
    if result != sat:
        return str(result), None
    model = solver.model()
    word = tuple(model.eval(symbol).as_long() for symbol in q)
    return "sat", word


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-length", type=int, default=40)
    parser.add_argument("--max-symbol", type=int, default=4)
    parser.add_argument("--timeout-ms", type=int, default=0)
    args = parser.parse_args()

    counts: dict[str, int] = {}
    for length in range(1, args.max_length + 1):
        status, model = search_length(
            length, args.max_symbol, args.timeout_ms
        )
        counts[status] = counts.get(status, 0) + 1
        if model is not None:
            print(
                {
                    "length": length,
                    "word": "".join(map(str, model)),
                }
            )
            break
    print(
        {
            "max_length": args.max_length,
            "max_symbol": args.max_symbol,
            "status_counts": counts,
        }
    )


if __name__ == "__main__":
    main()
