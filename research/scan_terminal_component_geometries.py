"""Scan one-high/two-low all-long terminal-marker geometries.

This is discovery code.  It incrementally imposes the exact binary circular
profile in forward phase order on the symbolic macro from
``z3_terminal_component_refinement`` and reports the first inconsistent
phase (or a full fixed profile).  Curling-number claims are independently
rechecked on any full model.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from curling import curling_number, curling_number_reference
from z3_terminal_component_refinement import build_case, model_word


def exact_circular_profile(word: tuple[int, ...]) -> tuple[int, ...]:
    n = len(word)
    values = []
    for phase in range(n):
        state = word * 2 + word[:phase]
        first = curling_number(state)
        second = curling_number_reference(state)
        assert first == second
        values.append(first)
    return tuple(values)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-root", type=int, default=35)
    parser.add_argument("--timeout-ms", type=int, default=2_000)
    parser.add_argument("--prefix", type=int, default=0)
    args = parser.parse_args()

    for root_text in ("2", "23", "223", "2223"):
        marker_length = 3 * len(root_text) + 2
        for incoming in range(len(root_text) + 1, args.max_root + 1):
            for outgoing in range(marker_length, 3 * incoming):
                solver, exact_profile, ancestry, letters = build_case(
                    root_text, incoming, outgoing
                )
                solver.set(timeout=args.timeout_ms)
                result = solver.check()
                if str(result) != "sat":
                    continue
                n = outgoing + 2 * incoming
                if args.prefix:
                    for cut in range(min(args.prefix, n)):
                        if cut not in ancestry:
                            solver.add(exact_profile(cut))
                    result = solver.check()
                    if str(result) != "unsat":
                        print(
                            "PREFIX_SURVIVOR",
                            root_text,
                            incoming,
                            outgoing,
                            n,
                            str(result),
                        )
                    continue
                first_bad = None
                for cut in range(n):
                    if cut in ancestry:
                        continue
                    solver.add(exact_profile(cut))
                    result = solver.check()
                    if str(result) != "sat":
                        first_bad = (cut, str(result))
                        break
                if first_bad is None:
                    text = model_word(solver, letters)
                    word = tuple(map(int, text))
                    profile = exact_circular_profile(word)
                    assert profile == word
                    print("FULL", root_text, incoming, outgoing, n, text)
                elif first_bad[0] >= 12 or first_bad[1] == "unknown":
                    print(
                        "LATE",
                        root_text,
                        incoming,
                        outgoing,
                        n,
                        first_bad,
                    )


if __name__ == "__main__":
    main()
