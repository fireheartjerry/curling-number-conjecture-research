"""Search critical replay roots with a literal cubic-parent marker.

This is a finite falsifier for the proposed sibling-tail inequality.  A
model ``U`` satisfies the complete proper-circular and first-copy fitting
profile used for late cubic reset roots, and begins ``P^3 3`` for a
primitive word ``P``.  The script then evaluates the two terminal siblings

    (U^3)[1:] 2,    (U^3)[1:] 3

with the executable curling-number implementation.

The marker equations alone are weaker than actual external ancestry:
they do not assert that ``U`` is the orbit continuation of ``P^3``.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from curling import curling_number, tail_length  # noqa: E402

from z3_cyclic_fixed import build_solver  # noqa: E402

try:
    from z3 import And, Or, sat
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
    from z3 import And, Or, sat  # type: ignore[no-redef]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("max_symbol", type=int, nargs="?", default=3)
    parser.add_argument("--parent-length", type=int)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--model-limit", type=int, default=100)
    parser.add_argument("--tail-limit", type=int, default=10000)
    parser.add_argument("--timeout-ms", type=int, default=300000)
    args = parser.parse_args()

    n = args.length
    solver, symbols = build_solver(
        n,
        args.max_symbol,
        replay=True,
        require_max=args.max_symbol > 3,
    )
    solver.set(timeout=args.timeout_ms)

    candidate_parent_lengths = (
        [args.parent_length]
        if args.parent_length is not None
        else list(range(1, (n - 1) // 3 + 1))
    )
    parent_choice = []
    for p in candidate_parent_lengths:
        if p is None or 3 * p >= n:
            continue
        marker = And(
            *(
                [symbols[i] == symbols[i % p] for i in range(3 * p)]
                + [symbols[3 * p] == 3]
                + [
                    Or(
                        *(
                            symbols[i] != symbols[i % d]
                            for i in range(d, p)
                        )
                    )
                    for d in range(1, p)
                    if p % d == 0
                ]
            )
        )
        parent_choice.append(marker)
    if not parent_choice:
        raise SystemExit("no admissible parent length")
    solver.add(Or(*parent_choice))

    count = 0
    violations = 0
    while count < args.model_limit and solver.check() == sat:
        model = solver.model()
        word = tuple(model.eval(x).as_long() for x in symbols)
        actual_parent_lengths = [
            p
            for p in candidate_parent_lengths
            if p is not None
            and 3 * p < n
            and word[: 3 * p] == word[:p] * 3
            and word[3 * p] == 3
        ]
        deleted_cube = (word * 3)[1:]
        assert curling_number(deleted_cube) == 2
        try:
            low_tail = tail_length(
                deleted_cube + (2,), step_limit=args.tail_limit
            )
            high_tail = tail_length(
                deleted_cube + (3,), step_limit=args.tail_limit
            )
            tail_report = f"tau2={low_tail} tau3={high_tail}"
            if high_tail > low_tail:
                violations += 1
                tail_report += " VIOLATION"
        except RuntimeError:
            tail_report = f"tail_limit={args.tail_limit}"
        print(
            "word="
            + "".join(map(str, word))
            + " parents="
            + ",".join(map(str, actual_parent_lengths))
            + " "
            + tail_report
        )
        count += 1
        if not args.all:
            break
        solver.add(Or(*(x != value for x, value in zip(symbols, word))))

    print(
        f"length={n} max_symbol={args.max_symbol} "
        f"models_reported={count} violations={violations} "
        f"solver_status={solver.check()}"
    )


if __name__ == "__main__":
    main()
