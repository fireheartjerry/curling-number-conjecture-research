"""Search the residual late-bordered ``k=2`` fixed-profile normal form.

The structural equations are

    C = E U,
    Y = U E U,
    Q = E U U E U,

with ``E,U`` nonempty, ``pc_Q = Q``, ``Q[0] = 2``, and ``cn(Q)=1``.
The latter is encoded by excluding every square suffix which fits in one
linear copy of Q.  This is a bounded falsifier only.

Run the A094004 calibration before accepting any later finite
curling-number recomputation of a returned model.
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
    """Return ``(e,h)`` with ``length=2e+3h`` and the border bound."""
    result = []
    for h in range(1, length):
        residual = length - 3 * h
        if residual <= 0 or residual % 2:
            continue
        e = residual // 2
        r = e + 2 * h
        if h < r - gcd(r, length):
            result.append((e, h))
    return tuple(result)


def structural_equalities(q, e: int, h: int):
    """Encode ``Q=E U U E U`` for fixed block lengths."""
    constraints = []
    # Second U equals first U.
    constraints.extend(q[e + h + i] == q[e + i] for i in range(h))
    # Second E equals first E.
    constraints.extend(
        q[e + 2 * h + i] == q[i] for i in range(e)
    )
    # Final U equals first U.
    constraints.extend(
        q[2 * e + 2 * h + i] == q[e + i] for i in range(h)
    )
    return And(*constraints)


def search_length(length: int, max_symbol: int, timeout_ms: int):
    candidates = shapes(length)
    if not candidates:
        return "no-shape", None

    solver, q = build_solver(length, max_symbol)
    if timeout_ms:
        solver.set(timeout=timeout_ms)
    solver.add(
        Or(
            *(structural_equalities(q, e, h) for e, h in candidates)
        )
    )
    solver.add(
        *(
            Not(power(q, 0, root, 2))
            for root in range(1, length // 2 + 1)
        )
    )

    result = solver.check()
    if result != sat:
        return str(result), None

    model = solver.model()
    word = tuple(model.eval(symbol).as_long() for symbol in q)
    matching = tuple(
        (e, h)
        for e, h in candidates
        if word
        == (
            word[:e]
            + word[e : e + h]
            + word[e : e + h]
            + word[:e]
            + word[e : e + h]
        )
    )
    return "sat", (word, matching)


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
            word, matching = model
            print(
                {
                    "length": length,
                    "word": "".join(map(str, word)),
                    "shapes": matching,
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
