"""Bounded audit of the circular terminal-prefix lemma.

The retained circular hypotheses are only:

* every cut has a proper square;
* a cut has a proper cube exactly when its displayed letter is ``3``;
* the distinguished first letter is ``2``.

The negated conclusion says that the final displayed letter's required
power does not fit in ``P[:-1]``.  No first-copy fitting equations,
fourth-power exclusions, or explicit primitivity constraints are used.

SAT models are checked with both finite curling-number implementations.
UNSAT is a bounded result only.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from z3 import And, Bool, Not, Or, Solver, is_true, sat  # type: ignore

from curling import curling_number, curling_number_reference


Word = tuple[int, ...]


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def circular_power(word: Word, cut: int, root: int, exponent: int) -> bool:
    n = len(word)
    return all(
        word[(cut - block * root + offset) % n]
        == word[(cut - root + offset) % n]
        for block in range(2, exponent + 1)
        for offset in range(root)
    )


def direct_audit(
    word: Word,
    require_squares: bool,
    require_cube_labels: bool,
    require_terminal_target: bool,
) -> None:
    n = len(word)
    assert word[0] == 2
    for cut in range(n):
        has_square = any(
            circular_power(word, cut, root, 2) for root in range(1, n)
        )
        has_cube = any(
            circular_power(word, cut, root, 3) for root in range(1, n)
        )
        if require_squares:
            assert has_square
        if require_cube_labels:
            assert has_cube == (word[cut] == 3)
        if require_terminal_target and cut == n - 1:
            assert has_square
    assert exact_cn(word[:-1]) < word[-1]


def build_solver(
    n: int,
    timeout_ms: int,
    require_squares: bool,
    require_cube_labels: bool,
    require_terminal_target: bool,
):
    solver = Solver()
    if timeout_ms:
        solver.set(timeout=timeout_ms)

    word = [Bool(f"w_{index}") for index in range(n)]

    def power(cut: int, root: int, exponent: int):
        return And(
            *(
                word[(cut - block * root + offset) % n]
                == word[(cut - root + offset) % n]
                for block in range(2, exponent + 1)
                for offset in range(root)
            )
        )

    squares = {
        (cut, root): power(cut, root, 2)
        for cut in range(n)
        for root in range(1, n)
    }
    cubes = {
        (cut, root): power(cut, root, 3)
        for cut in range(n)
        for root in range(1, n)
    }

    for cut in range(n):
        some_square = Or(*(squares[cut, root] for root in range(1, n)))
        some_cube = Or(*(cubes[cut, root] for root in range(1, n)))
        if require_squares:
            solver.add(some_square)
        if require_cube_labels:
            solver.add(word[cut] == some_cube)

    if require_terminal_target and not require_squares:
        terminal_square = Or(
            *(squares[n - 1, root] for root in range(1, n))
        )
        # A final 2 needs a square.  A final 3 already needs a cube when
        # cube-label equivalence is enabled, and a cube is also a square.
        solver.add(Or(word[-1], terminal_square))

    solver.add(Not(word[0]))

    short_squares = [
        squares[n - 1, root]
        for root in range(1, n)
        if 2 * root <= n - 1
    ]
    short_cubes = [
        cubes[n - 1, root]
        for root in range(1, n)
        if 3 * root <= n - 1
    ]
    no_short_square = Not(Or(*short_squares)) if short_squares else True
    no_short_cube = Not(Or(*short_cubes)) if short_cubes else True
    solver.add(
        And(
            Or(word[-1], no_short_square),
            Or(Not(word[-1]), no_short_cube),
        )
    )
    return solver, word


def solve_length(
    n: int,
    timeout_ms: int,
    require_squares: bool,
    require_cube_labels: bool,
    require_terminal_target: bool,
) -> str:
    solver, symbols = build_solver(
        n,
        timeout_ms,
        require_squares,
        require_cube_labels,
        require_terminal_target,
    )
    result = solver.check()
    if result != sat:
        return str(result)
    model = solver.model()
    word = tuple(3 if is_true(model.eval(symbol)) else 2 for symbol in symbols)
    direct_audit(
        word,
        require_squares,
        require_cube_labels,
        require_terminal_target,
    )
    return (
        "sat P="
        + "".join(map(str, word))
        + f" last={word[-1]} prefix_cn={exact_cn(word[:-1])}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("minimum", type=int)
    parser.add_argument("maximum", type=int, nargs="?")
    parser.add_argument("--timeout-ms", type=int, default=30_000)
    parser.add_argument("--omit-squares", action="store_true")
    parser.add_argument("--omit-cube-labels", action="store_true")
    parser.add_argument("--terminal-target-only", action="store_true")
    args = parser.parse_args()
    maximum = args.minimum if args.maximum is None else args.maximum
    if args.minimum < 2 or maximum < args.minimum:
        raise SystemExit(2)

    require_squares = not args.omit_squares
    require_cube_labels = not args.omit_cube_labels
    for n in range(args.minimum, maximum + 1):
        print(
            "length="
            + str(n)
            + " result="
            + solve_length(
                n,
                args.timeout_ms,
                require_squares,
                require_cube_labels,
                args.terminal_target_only,
            ),
            flush=True,
        )


if __name__ == "__main__":
    main()
