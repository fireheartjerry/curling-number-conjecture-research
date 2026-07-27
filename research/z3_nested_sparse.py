"""Test the small cut set extracted from the length-129 nested core."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Int, Or, Solver  # type: ignore

from z3_cyclic_fixed import power


CUTS = (4, 6, 7, 11, 61, 62, 64, 65)


def check_length(n: int, timeout_ms: int):
    q = [Int(f"q_{i}") for i in range(n)]
    solver = Solver()
    solver.set(timeout=timeout_ms)
    for x in q:
        solver.add(2 <= x, x <= 3)
    text = "223222322232322232223" * 3 + "3"
    for i, value in enumerate(text):
        solver.add(q[i] == int(value))
    for cut in CUTS:
        for exponent in (2, 3):
            circular = [
                power(q, cut, root, exponent)
                for root in range(1, n)
            ]
            fitting = [
                circular[root - 1]
                for root in range(1, n)
                if exponent * root <= n + cut
            ]
            solver.add((q[cut] >= exponent) == Or(*circular))
            solver.add((q[cut] >= exponent) == Or(*fitting))
        fourth = [power(q, cut, root, 4) for root in range(1, n)]
        solver.add(~Or(*fourth))
    return solver.check()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("minimum", type=int)
    parser.add_argument("maximum", type=int)
    parser.add_argument("--timeout-ms", type=int, default=30_000)
    args = parser.parse_args()
    for n in range(args.minimum, args.maximum + 1):
        print(n, check_length(n, args.timeout_ms), flush=True)


if __name__ == "__main__":
    main()
