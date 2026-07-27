"""Find the shortest symbolic left context realizing a binary word's profile.

The displayed word supplies the desired label at each phase.  A model
requires a labelled square/cube and excludes the next exponent at every
phase.  The script also computes, by executed finite circular enumeration,
which phases are positive holes in the displayed word's proper circular
profile.

This is an arbitrary-context diagnostic.  A satisfying context is not
required to arise from a generated critical seed.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, Solver, is_true, sat  # type: ignore

from check_run_length_grammar import proper_profile
from z3_q64_witness_charges import concrete_roots


def equal(xs, ys):
    return And(*(x == y for x, y in zip(xs, ys)))


def build(
    pattern: tuple[int, ...],
    left_len: int,
    cube_max: int | None = None,
):
    left = [Bool(f"x_{left_len}_{i}") for i in range(left_len)]
    word = left + [value == 3 for value in pattern]
    solver = Solver()

    def power(cut: int, root: int, exponent: int):
        blocks = [
            word[cut - block * root : cut - (block - 1) * root]
            for block in range(exponent, 0, -1)
        ]
        return And(*(equal(blocks[0], block) for block in blocks[1:]))

    def powers(cut: int, exponent: int, root_max: int | None = None):
        maximum = cut // exponent
        if root_max is not None:
            maximum = min(maximum, root_max)
        if maximum < 1:
            return False
        return Or(*(power(cut, root, exponent) for root in range(1, maximum + 1)))

    for phase, label in enumerate(pattern):
        cut = left_len + phase
        solver.add(
            powers(
                cut,
                label,
                cube_max if label == 3 else None,
            )
        )
        solver.add(Not(powers(cut, label + 1)))
        if cube_max is not None and label == 3:
            solver.add(
                Not(
                    Or(
                        *(
                            power(cut, root, 3)
                            for root in range(
                                cube_max + 1,
                                cut // 3 + 1,
                            )
                        )
                    )
                )
            )
    return solver, left


def first_model(
    pattern: tuple[int, ...],
    min_left: int,
    max_left: int,
    cube_max: int | None,
):
    for left_len in range(min_left, max_left + 1):
        solver, left = build(pattern, left_len, cube_max)
        if solver.check() != sat:
            continue
        model = solver.model()
        context = "".join(
            "3" if is_true(model.eval(bit, model_completion=True)) else "2"
            for bit in left
        )
        concrete = context + "".join(map(str, pattern))
        certificates = {
            phase: concrete_roots(
                concrete,
                left_len + phase,
                label,
            )
            for phase, label in enumerate(pattern)
        }
        return {
            "left_len": left_len,
            "context": context,
            "certificates": certificates,
        }
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("word")
    parser.add_argument("--min-left", type=int, default=1)
    parser.add_argument("--max-left", type=int, default=100)
    parser.add_argument("--cube-max", type=int)
    args = parser.parse_args()
    pattern = tuple(map(int, args.word))
    if not pattern or any(value not in (2, 3) for value in pattern):
        raise SystemExit("word must be a nonempty string over {2,3}")
    profile = proper_profile(pattern)
    holes = tuple(
        (phase, pattern[phase], profile[phase])
        for phase in range(len(pattern))
        if profile[phase] < pattern[phase]
    )
    print(
        {
            "word": args.word,
            "proper_profile": "".join(map(str, profile)),
            "positive_holes": holes,
        }
    )
    print(
        first_model(
            pattern,
            args.min_left,
            args.max_left,
            args.cube_max,
        )
    )


if __name__ == "__main__":
    main()
