"""Finite symbolic certificate for the forced U/B predecessor two-cycle.

Only the sign of bounded cube existence is used:

    displayed symbol = 3  iff  some cube root q <= 21 exists.

At every displayed cut, all such cubes lie in the final 63 symbols, so a
63-bit symbolic left suffix is exact and independent of older history.
Positive square requirements, fourth-power exclusions, and all roots above
21 are omitted.  Therefore every UNSAT result is a certificate for a
strict relaxation of the actual fixed-profile conditions.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, If, Not, Or, Solver, is_true, sat, unsat


U = tuple(map(int, "223232223222322322232"))
B = tuple(map(int, "223222323222322232232"))
BOUND = 21
LEFT = 3 * BOUND


def eq(xs, ys):
    return And(*(x == y for x, y in zip(xs, ys)))


def cube(word, cut, root):
    assert 3 * root <= cut
    final = word[cut - root : cut]
    middle = word[cut - 2 * root : cut - root]
    first = word[cut - 3 * root : cut - 2 * root]
    return And(eq(first, final), eq(middle, final))


def node_data(current, phase, predecessor):
    q = predecessor
    left = [Bool(f"x_{q}_{i}") for i in range(LEFT)]
    root = [Bool(f"r_{q}_{i}") for i in range(q)]
    current_bits = [value == 3 for value in current * 3]
    displayed = root * 3 + current_bits[phase:]
    current_start = 3 * q - phase
    overlap = [
        displayed[current_start + offset] == (current[offset] == 3)
        for offset in range(phase)
    ]
    word = left + displayed
    conditions = []
    for index, label in enumerate(displayed):
        cut = LEFT + index
        has_cube = Or(*(cube(word, cut, r) for r in range(1, BOUND + 1)))
        conditions.append(If(label, has_cube, Not(has_cube)))
    return left, root, displayed, overlap, conditions


def check_subset(overlap, conditions, active, extra=()):
    solver = Solver()
    solver.add(*overlap, *extra)
    solver.add(*(conditions[index] for index in active))
    return solver.check(), solver


def tracked_core(overlap, conditions, extra=()):
    solver = Solver()
    solver.add(*overlap, *extra)
    for index, condition in enumerate(conditions):
        solver.assert_and_track(condition, f"p{index}")
    result = solver.check()
    if result != unsat:
        return result, (), solver
    core = tuple(
        int(str(atom)[1:])
        for atom in solver.unsat_core()
        if str(atom).startswith("p")
    )
    return result, core, solver


def minimize_core(overlap, conditions, core, extra=()):
    active = list(core)
    changed = True
    while changed:
        changed = False
        for index in tuple(active):
            trial = [phase for phase in active if phase != index]
            result, _ = check_subset(
                overlap, conditions, trial, extra=extra
            )
            if result == unsat:
                active = trial
                changed = True
    return tuple(sorted(active))


def certify_transition(name, current, phase):
    rows = []
    for q in range(1, BOUND + 1):
        left, root, displayed, overlap, conditions = node_data(
            current, phase, q
        )
        result, core, solver = tracked_core(overlap, conditions)
        if result == unsat:
            minimized = minimize_core(overlap, conditions, core)
            rows.append(
                {
                    "q": q,
                    "status": "unsat",
                    "core": minimized,
                    "displayed_length": len(displayed),
                }
            )
            continue
        assert result == sat
        model = solver.model()
        root_values = tuple(
            is_true(model.eval(bit, model_completion=True))
            for bit in root
        )
        root_text = "".join("3" if value else "2" for value in root_values)

        bit_cores = []
        for bit_index, (bit, value) in enumerate(zip(root, root_values)):
            opposite = (bit != value)
            bit_result, bit_core, _ = tracked_core(
                overlap, conditions, extra=(opposite,)
            )
            assert bit_result == unsat
            bit_core = minimize_core(
                overlap, conditions, bit_core, extra=(opposite,)
            )
            bit_cores.append((bit_index, 3 if value else 2, bit_core))

        rows.append(
            {
                "q": q,
                "status": "unique",
                "root": root_text,
                "bit_cores": bit_cores,
                "displayed_length": len(displayed),
            }
        )
    return {
        "name": name,
        "current": "".join(map(str, current)),
        "phase": phase,
        "rows": rows,
    }


def main():
    certificates = (
        certify_transition("U_to_B", U, 4),
        certify_transition("B_to_U", B, 8),
    )
    for certificate in certificates:
        unique = [
            row for row in certificate["rows"] if row["status"] == "unique"
        ]
        assert len(unique) == 1 and unique[0]["q"] == 21
        print(
            f"{certificate['name']}: unique q=21 root={unique[0]['root']}"
        )
        print(
            "unsat cores: "
            + " ".join(
                f"{row['q']}:{','.join(map(str, row['core'])) or '-'}"
                for row in certificate["rows"]
                if row["status"] == "unsat"
            )
        )
        print(
            "forced-bit cores: "
            + " ".join(
                f"{index}={value}[{','.join(map(str, core)) or '-'}]"
                for index, value, core in unique[0]["bit_cores"]
            )
        )
if __name__ == "__main__":
    main()
