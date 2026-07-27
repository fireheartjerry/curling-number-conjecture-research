"""Search primitive circular weighted curling profiles.

Tokens range over 0,...,sigma-1.  Each token has a weight in {2,3}, and
the exact proper circular curling number at a cut must equal the weight
of the token stored at that cut.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, If, Int, Not, Or, Solver, Sum, sat  # type: ignore[import-not-found]


def power(tokens, cut: int, root: int, exponent: int):
    n = len(tokens)
    return And(
        *(
            tokens[(cut - block * root + offset) % n]
            == tokens[(cut - root + offset) % n]
            for block in range(2, exponent + 1)
            for offset in range(root)
        )
    )


def solve(
    length: int,
    alphabet: int,
    timeout_ms: int,
    fixed_weights: tuple[int, ...] | None = None,
):
    tokens = [Int(f"u_{i}") for i in range(length)]
    weights = [Int(f"weight_{a}") for a in range(alphabet)]
    solver = Solver()
    solver.set(timeout=timeout_ms)
    solver.add(*(And(0 <= token, token < alphabet) for token in tokens))
    solver.add(*(And(2 <= weight, weight <= 3) for weight in weights))
    if fixed_weights is not None:
        if len(fixed_weights) != alphabet:
            raise ValueError((fixed_weights, alphabet))
        solver.add(
            *(weight == value
              for weight, value in zip(weights, fixed_weights))
        )
    solver.add(tokens[0] == 0)
    solver.add(
        *(
            Or(*(token == symbol for token in tokens))
            for symbol in range(alphabet)
        )
    )

    # A restricted-growth symmetry break: before token a first occurs,
    # token a-1 must already have occurred.
    for position in range(length):
        for symbol in range(1, alphabet):
            solver.add(
                Or(
                    tokens[position] != symbol,
                    Or(
                        *(tokens[earlier] == symbol - 1
                          for earlier in range(position))
                    ),
                )
            )

    for period in range(1, length):
        if length % period == 0:
            solver.add(
                Or(
                    *(
                        tokens[i] != tokens[i % period]
                        for i in range(period, length)
                    )
                )
            )

    for cut in range(length):
        token_weight = Sum(
            *(
                If(tokens[cut] == symbol, weights[symbol], 0)
                for symbol in range(alphabet)
            )
        )
        squares = Or(
            *(power(tokens, cut, root, 2)
              for root in range(1, length))
        )
        cubes = Or(
            *(power(tokens, cut, root, 3)
              for root in range(1, length))
        )
        fourths = Or(
            *(power(tokens, cut, root, 4)
              for root in range(1, length))
        )
        solver.add(squares)
        solver.add((token_weight == 3) == cubes)
        solver.add(Not(fourths))

    result = solver.check()
    if result != sat:
        return result, None
    model = solver.model()
    word = tuple(model.eval(token).as_long() for token in tokens)
    weight_map = tuple(model.eval(weight).as_long() for weight in weights)
    return result, (word, weight_map)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("--alphabet", type=int, default=3)
    parser.add_argument("--timeout-ms", type=int, default=120000)
    parser.add_argument(
        "--weights",
        help="fixed weight string, for example 223",
    )
    args = parser.parse_args()
    fixed_weights = (
        tuple(map(int, args.weights))
        if args.weights is not None
        else None
    )
    result, model = solve(
        args.length,
        args.alphabet,
        args.timeout_ms,
        fixed_weights,
    )
    print(f"result={result} model={model}")


if __name__ == "__main__":
    main()
