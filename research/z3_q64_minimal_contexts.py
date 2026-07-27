"""Classify left-minimal contexts which repair all three Q64 holes.

For a context ``H`` followed by the critical 64-letter word ``W``, every
phase of ``W`` is required to have its labelled square/cube and to exclude
the next exponent.  The context is *left-minimal* when deleting its first
letter destroys positive coverage at at least one of the three holes.

Because suffix powers only look left, left-minimality is equivalent to an
active hole having a witness whose powered factor starts at context
coordinate zero and having no witness for that hole which starts later.
The script checks each of the three possible anchored holes separately.
It is a bounded structural diagnostic, not a proof for unbounded contexts.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import Not, Or, is_true, sat  # type: ignore

from z3_q64_witness_charges import HOLES, W, build, concrete_roots


def anchor_formula(power, left_len: int, phase: int):
    exponent = W[phase]
    cut = left_len + phase
    if cut % exponent:
        return None
    root = cut // exponent
    if root < 1:
        return None
    later = tuple(
        power(cut, candidate, exponent)
        for candidate in range(1, root)
    )
    return power(cut, root, exponent), Not(Or(*later)), root


def first_model(
    left_len: int,
    phase: int,
    cube_max: int | None,
):
    solver, left, _, power = build(left_len, 3, cube_max)
    anchored = anchor_formula(power, left_len, phase)
    if anchored is None:
        return None
    anchor, no_later_witness, root = anchored
    solver.add(anchor, no_later_witness)
    if solver.check() != sat:
        return None
    model = solver.model()
    context = "".join(
        "3" if is_true(model.eval(bit, model_completion=True)) else "2"
        for bit in left
    )
    word = context + "".join(map(str, W))
    roots = {
        hole: concrete_roots(word, left_len + hole, W[hole])
        for hole in HOLES
    }
    return {
        "left_len": left_len,
        "anchor_phase": phase,
        "anchor_root": root,
        "context": context,
        "roots": roots,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-left", type=int, default=1)
    parser.add_argument("--max-left", type=int, default=100)
    parser.add_argument("--anchor-phase", type=int, choices=HOLES)
    parser.add_argument("--cube-max", type=int)
    args = parser.parse_args()
    counts = {phase: 0 for phase in HOLES}
    for left_len in range(args.min_left, args.max_left + 1):
        phases = HOLES if args.anchor_phase is None else (args.anchor_phase,)
        for phase in phases:
            answer = first_model(left_len, phase, args.cube_max)
            if answer is not None:
                counts[phase] += 1
                print(answer)
    print(
        {
            "range": (args.min_left, args.max_left),
            "counts_by_anchor_phase": counts,
        }
    )


if __name__ == "__main__":
    main()
