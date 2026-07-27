"""Enumerate binary fixed-profile parents of the late internal-reset form.

This is a theorem-discovery diagnostic.  It blocks every satisfying parent
assignment, independently recomputes the finite and circular profiles, and
reports exactly where the prescribed child first fails.  It does not claim an
unbounded classification.
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from z3 import Or, is_true, sat

from curling import curling_number, curling_number_reference
from research.check_run_length_grammar import primitive, proper_profile
from research.z3_hidden_k3_fixed_pair import build


def decode(model, bits) -> tuple[int, ...]:
    return tuple(3 if is_true(model.eval(bit)) else 2 for bit in bits)


def roots_at(word: tuple[int, ...], cut: int, exponent: int) -> tuple[int, ...]:
    n = len(word)
    result: list[int] = []
    for root in range(1, n):
        if all(
            word[(cut - block * root + offset) % n]
            == word[(cut - root + offset) % n]
            for block in range(2, exponent + 1)
            for offset in range(root)
        ):
            result.append(root)
    return tuple(result)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("p_min", type=int)
    parser.add_argument("p_max", type=int)
    parser.add_argument("--limit-per-geometry", type=int, default=10000)
    parser.add_argument("--timeout-ms", type=int, default=0)
    args = parser.parse_args()

    models = 0
    child_fixed = 0
    failure_histogram: dict[tuple[int, int, int], int] = {}
    for p in range(args.p_min, args.p_max + 1):
        for h in range(p // 3 + 1, p):
            if math.gcd(p, h) == h:
                continue
            solver, bits = build(p, h, u_only=True)
            if args.timeout_ms:
                solver.set(timeout=args.timeout_ms)
            local_count = 0
            while local_count < args.limit_per_geometry and solver.check() == sat:
                model = solver.model()
                u = decode(model, bits)
                v = u + u + u[:h]
                assert primitive(u) and primitive(v)
                assert proper_profile(u) == u
                for cut, label in enumerate(u):
                    state = u + u[:cut]
                    assert curling_number(state) == curling_number_reference(state) == label

                profile = proper_profile(v)
                fitting = tuple(curling_number(v + v[:cut]) for cut in range(len(v)))
                bad = tuple(
                    cut
                    for cut, label in enumerate(v)
                    if profile[cut] != label or fitting[cut] != label
                )
                if not bad:
                    child_fixed += 1
                    print("CHILD_FIXED", p, h, "".join(map(str, u)))
                else:
                    first = bad[0]
                    key = (p - h, first, profile[first] - v[first])
                    failure_histogram[key] = failure_histogram.get(key, 0) + 1
                    print(
                        "FAIL",
                        f"p={p}",
                        f"h={h}",
                        f"a={p-h}",
                        f"first={first}",
                        f"label={v[first]}",
                        f"pc={profile[first]}",
                        f"fit={fitting[first]}",
                        f"sq={roots_at(v, first, 2)}",
                        f"cu={roots_at(v, first, 3)}",
                        f"U={''.join(map(str, u))}",
                    )

                solver.add(Or(*(bit != model.eval(bit) for bit in bits)))
                local_count += 1
                models += 1

    print(
        f"models={models} child_fixed={child_fixed} "
        f"failure_types={len(failure_histogram)}"
    )
    for key, count in sorted(failure_histogram.items()):
        print("HIST", key, count)


if __name__ == "__main__":
    main()
