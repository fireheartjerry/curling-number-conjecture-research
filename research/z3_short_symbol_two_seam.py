"""Bounded falsifier for the residual short external symbol-two seam.

For every requested length this asks for a primitive binary word ``P`` with
its exact proper circular curling profile equal to ``P`` and for a split
``s`` satisfying the short-seam overlap

    P[:n+1-s] = P[s:] + (2,),   P[n+1-s] = 3,

together with ``s > gcd(n,s)``.  A satisfiable model is recomputed by the
independent concrete profile implementation.  This is bounded evidence only.

Run the A094004 total-orbit-length calibration before using any output.
"""

from __future__ import annotations

import argparse
from math import gcd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))

from z3 import And, Or, sat, unknown  # type: ignore[import-not-found]

from check_general_rotation_status import primitive, proper_circular_profile
from z3_cyclic_fixed import build_solver


def candidate_constraint(q, n: int, split: int):
    hidden = n + 1 - split
    return And(
        *(q[index] == q[split + index] for index in range(hidden - 1)),
        q[hidden - 1] == 2,
        q[hidden] == 3,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-n", type=int, default=3)
    parser.add_argument("--max-n", type=int, default=40)
    parser.add_argument("--timeout-ms", type=int, default=0)
    args = parser.parse_args()

    results: list[tuple[int, str]] = []
    for n in range(args.min_n, args.max_n + 1):
        splits = tuple(
            split
            for split in range(2, n)
            if split > gcd(n, split) and n < 3 * split
        )
        if not splits:
            results.append((n, "no_split"))
            continue

        solver, q = build_solver(n, 3, first_symbol=2)
        if args.timeout_ms:
            solver.set(timeout=args.timeout_ms)
        solver.add(Or(*(candidate_constraint(q, n, split) for split in splits)))
        result = solver.check()
        if result == unknown:
            results.append((n, "unknown"))
            continue
        if result != sat:
            results.append((n, "unsat"))
            continue

        model = solver.model()
        word = tuple(model.eval(symbol).as_long() for symbol in q)
        assert primitive(word)
        assert proper_circular_profile(word) == word
        matching = tuple(
            split
            for split in splits
            if word[: n + 1 - split] == word[split:] + (2,)
            and word[n + 1 - split] == 3
        )
        assert matching
        diagnostics = []
        for split in matching:
            hidden = n + 1 - split
            remainder = n - split
            quotient, u_length = divmod(remainder, split)
            assert quotient in (0, 1)
            assert 0 < u_length < split
            u = word[:u_length]
            v = word[u_length:split]
            assert word == (u + v) * (quotient + 1) + u
            y = word * 2 + word[:split]
            y_profile = proper_circular_profile(y)
            holes = tuple(
                phase
                for phase in range(hidden)
                if y[phase] == 2 and y_profile[phase] == 1
            )
            diagnostics.append(
                {
                    "split": split,
                    "hidden": hidden,
                    "quotient": quotient,
                    "U": "".join(map(str, u)),
                    "V": "".join(map(str, v)),
                    "Y_holes": holes,
                    "Y_profile": "".join(map(str, y_profile)),
                }
            )
        results.append(
            (n, "sat:" + "".join(map(str, word)) + ":" + repr(diagnostics))
        )

    print(
        {
            "range": (args.min_n, args.max_n),
            "results": results,
            "sat": sum(status.startswith("sat:") for _, status in results),
            "unsat": sum(status == "unsat" for _, status in results),
            "unknown": sum(status == "unknown" for _, status in results),
        }
    )


if __name__ == "__main__":
    main()
