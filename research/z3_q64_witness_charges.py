"""Add the three missing positive witnesses of the Q64 bridge one by one.

At every displayed phase we always impose the exact negative condition:
no cube at a 2-label and no fourth power at a 3-label.  At all ordinary
phases we also impose the required positive power.  The three bridge holes
are phases 1, 5, and 10.  A stage requires the first ``stage`` holes to
have their positive witness and explicitly keeps the remaining holes
unwitnessed.

This is a local-context diagnostic.  The symbolic left context is not
itself required to be generated.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, Solver, is_true, sat  # type: ignore


W = tuple(
    map(
        int,
        "2223232223222322322232223232223222322322232223232223222322322233",
    )
)
HOLES = (1, 5, 10)


def equal(xs, ys):
    return And(*(x == y for x, y in zip(xs, ys)))


def build(
    left_len: int,
    stage: int,
    cube_max: int | None = None,
):
    left = [Bool(f"x_{stage}_{left_len}_{i}") for i in range(left_len)]
    word = left + [value == 3 for value in W]
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

    active = frozenset(HOLES[:stage])
    inactive = frozenset(HOLES[stage:])
    for phase, label in enumerate(W):
        cut = left_len + phase
        wanted = powers(
            cut,
            label,
            cube_max if label == 3 else None,
        )
        forbidden = powers(cut, label + 1)
        solver.add(Not(forbidden))
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
        if phase in inactive:
            solver.add(Not(wanted))
        else:
            solver.add(wanted)
    return solver, left, word, power


def feasible_roots(solver, power, cut: int, exponent: int):
    out = []
    for root in range(1, cut // exponent + 1):
        solver.push()
        solver.add(power(cut, root, exponent))
        if solver.check() == sat:
            out.append(root)
        solver.pop()
    return tuple(out)


def primitive(block: str) -> bool:
    return all(
        block != block[:period] * (len(block) // period)
        for period in range(1, len(block))
        if len(block) % period == 0
    )


def concrete_roots(word: str, cut: int, exponent: int):
    out = []
    for root in range(1, cut // exponent + 1):
        factor = word[cut - exponent * root : cut]
        block = factor[:root]
        if factor == block * exponent:
            out.append(
                {
                    "root": root,
                    "origin": cut - exponent * root,
                    "block": block,
                    "exponent": exponent,
                    "primitive": primitive(block),
                }
            )
    return tuple(out)


def first_model(stage: int, max_left: int, cube_max: int | None):
    for left_len in range(1, max_left + 1):
        solver, left, word, power = build(left_len, stage, cube_max)
        if solver.check() != sat:
            continue
        model = solver.model()
        context = "".join(
            "3" if is_true(model.eval(bit, model_completion=True)) else "2"
            for bit in left
        )
        feasible = {
            phase: feasible_roots(
                solver,
                power,
                left_len + phase,
                W[phase],
            )
            for phase in HOLES
        }
        concrete_word = context + "".join(map(str, W))
        realized = {
            phase: concrete_roots(
                concrete_word,
                left_len + phase,
                W[phase],
            )
            for phase in HOLES
        }
        return {
            "left_len": left_len,
            "context": context,
            "feasible_roots": feasible,
            "realized_certificates": realized,
        }
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-left", type=int, default=80)
    parser.add_argument("--cube-max", type=int)
    args = parser.parse_args()
    for stage in range(4):
        answer = first_model(stage, args.max_left, args.cube_max)
        print(f"stage={stage} answer={answer}")


if __name__ == "__main__":
    main()
