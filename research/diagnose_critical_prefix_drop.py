"""Diagnose which critical-word constraints exclude a strict prefix drop.

This is not a proof.  It builds named Z3 constraint families so that:

* every relaxation can be searched independently;
* concrete SAT models are audited against the encoded predicates; and
* UNSAT cores can expose which cuts are load-bearing at each finite length.

The cut convention agrees with ``z3_critical_prefix_drop.py``: a power
at cut ``j`` ends immediately before ``P[j]`` in the circular word.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from z3 import And, Bool, BoolRef, Not, Or, Solver, is_true, sat  # type: ignore

from curling import curling_number, curling_number_reference


Word = tuple[int, ...]


@dataclass(frozen=True)
class Families:
    circular_square: bool = True
    circular_cube_profile: bool = True
    circular_no_fourth: bool = True
    fitting_square: bool = True
    fitting_cube_profile: bool = True
    primitive: bool = True


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def build(
    n: int,
    families: Families,
    timeout_ms: int,
    tracked: bool = False,
) -> tuple[Solver, list[BoolRef], dict[str, BoolRef]]:
    solver = Solver()
    if timeout_ms:
        solver.set(timeout=timeout_ms)
    word = [Bool(f"w_{index}") for index in range(n)]
    names: dict[str, BoolRef] = {}

    def add(name: str, formula: BoolRef) -> None:
        if tracked:
            tag = Bool(name)
            names[name] = tag
            solver.assert_and_track(formula, tag)
        else:
            solver.add(formula)

    def power(cut: int, root: int, exponent: int) -> BoolRef:
        return And(
            *(
                word[(cut - block * root + offset) % n]
                == word[(cut - root + offset) % n]
                for block in range(2, exponent + 1)
                for offset in range(root)
            )
        )

    powers = {
        (cut, root, exponent): power(cut, root, exponent)
        for cut in range(n)
        for root in range(1, n)
        for exponent in (2, 3, 4)
    }

    for cut in range(n):
        squares = Or(*(powers[cut, root, 2] for root in range(1, n)))
        cubes = Or(*(powers[cut, root, 3] for root in range(1, n)))
        fourths = Or(*(powers[cut, root, 4] for root in range(1, n)))
        if families.circular_square:
            add(f"cs_{cut}", squares)
        if families.circular_cube_profile:
            add(f"cc_{cut}", word[cut] == cubes)
        if families.circular_no_fourth:
            add(f"c4_{cut}", Not(fourths))

        fitting_squares = [
            powers[cut, root, 2]
            for root in range(1, n)
            if 2 * root <= n + cut - 1
        ]
        fitting_cubes = [
            powers[cut, root, 3]
            for root in range(1, n)
            if 3 * root <= n + cut - 1
        ]
        if families.fitting_square:
            add(
                f"fs_{cut}",
                Or(*fitting_squares) if fitting_squares else False,
            )
        if families.fitting_cube_profile:
            add(
                f"fc_{cut}",
                word[cut]
                == (Or(*fitting_cubes) if fitting_cubes else False),
            )

    add("origin", Not(word[0]))

    short_squares = [
        powers[n - 1, root, 2]
        for root in range(1, n)
        if 2 * root <= n - 1
    ]
    short_cubes = [
        powers[n - 1, root, 3]
        for root in range(1, n)
        if 3 * root <= n - 1
    ]
    no_short_square = Not(Or(*short_squares)) if short_squares else True
    no_short_cube = Not(Or(*short_cubes)) if short_cubes else True
    add(
        "drop",
        And(
            Or(word[-1], no_short_square),
            Or(Not(word[-1]), no_short_cube),
        ),
    )

    if families.primitive:
        for period in range(1, n):
            if n % period == 0:
                add(
                    f"prim_{period}",
                    Or(
                        *(
                            word[index] != word[index % period]
                            for index in range(period, n)
                        )
                    ),
                )
    return solver, word, names


def model_word(solver: Solver, symbols: list[BoolRef]) -> Word:
    model = solver.model()
    return tuple(3 if is_true(model.eval(symbol)) else 2 for symbol in symbols)


def family_variants() -> list[tuple[str, Families]]:
    all_families = Families()
    variants = [("all", all_families)]
    for name in Families.__dataclass_fields__:
        values = all_families.__dict__ | {name: False}
        variants.append((f"minus_{name}", Families(**values)))
    variants.extend(
        (
            (
                "circular_only",
                Families(
                    fitting_square=False,
                    fitting_cube_profile=False,
                ),
            ),
            (
                "fitting_square_only",
                Families(
                    circular_square=False,
                    circular_cube_profile=False,
                    circular_no_fourth=False,
                    fitting_cube_profile=False,
                ),
            ),
            (
                "fitting_cube_only",
                Families(
                    circular_square=False,
                    circular_cube_profile=False,
                    circular_no_fourth=False,
                    fitting_square=False,
                ),
            ),
            (
                "square_both",
                Families(
                    circular_cube_profile=False,
                    circular_no_fourth=False,
                    fitting_cube_profile=False,
                ),
            ),
            (
                "cube_both",
                Families(
                    circular_square=False,
                    circular_no_fourth=False,
                    fitting_square=False,
                ),
            ),
            (
                "circular_minus_square",
                Families(
                    circular_square=False,
                    fitting_square=False,
                    fitting_cube_profile=False,
                ),
            ),
            (
                "circular_minus_cube",
                Families(
                    circular_cube_profile=False,
                    fitting_square=False,
                    fitting_cube_profile=False,
                ),
            ),
            (
                "circular_minus_fourth",
                Families(
                    circular_no_fourth=False,
                    fitting_square=False,
                    fitting_cube_profile=False,
                ),
            ),
            (
                "circular_no_primitive",
                Families(
                    fitting_square=False,
                    fitting_cube_profile=False,
                    primitive=False,
                ),
            ),
        )
    )
    return variants


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("minimum", type=int)
    parser.add_argument("maximum", type=int, nargs="?")
    parser.add_argument("--timeout-ms", type=int, default=10_000)
    parser.add_argument("--cores", action="store_true")
    args = parser.parse_args()
    maximum = args.minimum if args.maximum is None else args.maximum

    if args.cores:
        for n in range(args.minimum, maximum + 1):
            solver, _, _ = build(n, Families(), args.timeout_ms, tracked=True)
            result = solver.check()
            core = sorted(str(item) for item in solver.unsat_core())
            print(f"length={n} result={result} core={','.join(core)}")
        return

    for name, families in family_variants():
        records = []
        for n in range(args.minimum, maximum + 1):
            solver, symbols, _ = build(n, families, args.timeout_ms)
            result = solver.check()
            if result == sat:
                word = model_word(solver, symbols)
                records.append(
                    f"{n}:"
                    + "".join(map(str, word))
                    + f":prefix_cn={exact_cn(word[:-1])}"
                )
                break
            records.append(f"{n}:{result}")
        print(f"{name} first_sat_or_last={' '.join(records[-1:])}")


if __name__ == "__main__":
    main()
