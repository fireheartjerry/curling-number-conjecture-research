"""Enumerate bounded cube rescues at the two defective 3-phases of R20.

Coordinates put a tight occurrence R^3 at [0, 60).  The unknown binary
left context occupies [-63, 0), where False/True encode 2/3.  We impose
the exact cube part of the circular profile through phase 7:

* a label 2 forbids every cube root of length at most GLOBAL_MAX;
* a label 3 has a cube root of length at most GLOBAL_MAX and forbids
  every fourth-power root in that range.

Under the hypothesis that GLOBAL_MAX bounds every primitive cube root,
these are the exact positive/negative high-power constraints.  The
positive square witnesses at label 2 are irrelevant to this obstruction
and deliberately are not imposed.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, Solver, is_true, sat


R = tuple(map(int, "22322323222322232232"))
GLOBAL_MAX = 21
LEFT_LEN = 3 * GLOBAL_MAX


def eq(xs, ys):
    return And(*(x == y for x, y in zip(xs, ys)))


def power(word, cut, root, exponent):
    blocks = [
        word[cut - (block + 1) * root : cut - block * root]
        for block in range(exponent)
    ]
    return And(*(eq(blocks[0], block) for block in blocks[1:]))


def make_base(last_phase, tight=False):
    left = [Bool(f"x_{last_phase}_{int(tight)}_{i}") for i in range(LEFT_LEN)]
    word = left + [bool(x == 3) for x in R * 3]
    solver = Solver()
    if tight:
        # Tightness at the left end of the outer period-20 run:
        # its expected predecessor is R[-1] = 2, so the actual predecessor is 3.
        solver.add(left[-1])
    labels = (R * 3)[: last_phase + 1]
    for phase, label in enumerate(labels):
        cut = LEFT_LEN + phase
        cubes = Or(
            *(
                power(word, cut, root, 3)
                for root in range(1, min(GLOBAL_MAX, cut // 3) + 1)
            )
        )
        fourths = Or(
            *(
                power(word, cut, root, 4)
                for root in range(1, min(GLOBAL_MAX, cut // 4) + 1)
            )
        )
        solver.add(And(cubes, Not(fourths)) if label == 3 else Not(cubes))
    return solver, left, word


def model_context(solver, left):
    model = solver.model()
    return "".join(
        "3" if is_true(model.eval(bit, model_completion=True)) else "2"
        for bit in left
    )


def feasible_roots(phase, last_phase, tight=False):
    solver, left, word = make_base(last_phase, tight=tight)
    cut = LEFT_LEN + phase
    answer = []
    for root in range(1, GLOBAL_MAX + 1):
        solver.push()
        solver.add(power(word, cut, root, 3))
        if solver.check() == sat:
            answer.append((root, model_context(solver, left)))
        solver.pop()
    return answer


def pair_table(tight=False, last_phase=7):
    # Build the phase-0..6 constraints first.  At phase 7 impose a selected
    # cube and its exact no-fourth condition (already part of make_base(7)).
    solver, left, word = make_base(last_phase, tight=tight)
    cut5 = LEFT_LEN + 5
    cut7 = LEFT_LEN + 7
    rows = []
    for q5 in range(1, GLOBAL_MAX + 1):
        for q7 in range(1, GLOBAL_MAX + 1):
            solver.push()
            solver.add(power(word, cut5, q5, 3))
            solver.add(power(word, cut7, q7, 3))
            result = solver.check()
            if result == sat:
                rows.append((q5, q7, model_context(solver, left)))
            solver.pop()
    return rows


def branch_survival(tight=False):
    """For each q5 surviving phase 5, locate its first later obstruction."""
    before6, _, word6 = make_base(5, tight=tight)
    # Recover the left variables from the word prefix.
    left6 = word6[:LEFT_LEN]
    cut5 = LEFT_LEN + 5
    cut6 = LEFT_LEN + 6
    cut7 = LEFT_LEN + 7
    cube6 = Or(
        *(
            power(word6, cut6, root, 3)
            for root in range(1, min(GLOBAL_MAX, cut6 // 3) + 1)
        )
    )
    outputs = []
    for q5 in range(1, GLOBAL_MAX + 1):
        before6.push()
        before6.add(power(word6, cut5, q5, 3))
        if before6.check() != sat:
            before6.pop()
            continue
        context5 = model_context(before6, left6)

        before6.push()
        before6.add(Not(cube6))
        phase6_ok = before6.check() == sat
        q7s = []
        context6 = None
        if phase6_ok:
            context6 = model_context(before6, left6)
            fourth7 = Or(
                *(
                    power(word6, cut7, root, 4)
                    for root in range(1, min(GLOBAL_MAX, cut7 // 4) + 1)
                )
            )
            for q7 in range(1, GLOBAL_MAX + 1):
                before6.push()
                before6.add(power(word6, cut7, q7, 3), Not(fourth7))
                if before6.check() == sat:
                    q7s.append((q7, model_context(before6, left6)))
                before6.pop()
        before6.pop()
        outputs.append((q5, context5, phase6_ok, context6, q7s))
        before6.pop()
    return outputs


def main():
    print("R=" + "".join(map(str, R)))
    print(f"global_max={GLOBAL_MAX} left_len={LEFT_LEN}")
    for tight in (False, True):
        print(f"tight={tight}")
        for phase in (5, 7):
            for last_phase in sorted({phase, 7, len(R) - 1, 3 * len(R) - 1}):
                roots = feasible_roots(phase, last_phase, tight=tight)
                print(
                    f"phase={phase} exact_through={last_phase} "
                    f"roots={[root for root, _ in roots]}"
                )
        print("branches after exact phases 0..5:")
        for q5, context5, phase6_ok, context6, q7s in branch_survival(tight=tight):
            print(
                f"q5={q5} phase6_ok={phase6_ok} "
                f"q7s={[root for root, _ in q7s]}"
            )
            print(f"  phase5_context_suffix={context5[-63:]}")
            if context6 is not None:
                print(f"  phase6_context_suffix={context6[-63:]}")
            for q7, context7 in q7s:
                print(f"  q7={q7} context_suffix={context7[-63:]}")
        for last_phase in (7, len(R) - 1, 3 * len(R) - 1):
            print(
                f"phase5_phase7_pairs_through_{last_phase}="
                f"{pair_table(tight=tight, last_phase=last_phase)}"
            )


if __name__ == "__main__":
    main()
