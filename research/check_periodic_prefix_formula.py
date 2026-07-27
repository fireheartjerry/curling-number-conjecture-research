"""Exhaustive bounded audit of the periodic-prefix formula.

The formula itself is proved with Fine--Wilf in
``moving_boundary_context_loss.md``.  This script only checks phase
conventions and edge cases.

Run the A094004 calibration before accepting the output:

    python -m unittest \
      tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference


Word = tuple[int, ...]


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def primitive_root(word: Word) -> Word:
    for length in range(1, len(word) + 1):
        if (
            len(word) % length == 0
            and word == word[:length] * (len(word) // length)
        ):
            return word[:length]
    raise AssertionError("nonempty word has a primitive root")


def exponent_for_root(word: Word, root_length: int) -> int:
    root = word[-root_length:]
    exponent = 0
    while len(word) >= (exponent + 1) * root_length:
        start = len(word) - (exponent + 1) * root_length
        end = len(word) - exponent * root_length
        if word[start:end] != root:
            break
        exponent += 1
    return exponent


def proper_circular_value(period: Word, phase: int) -> int:
    length = len(period)
    context = period * 3 + period[:phase]
    return max(
        (
            exponent_for_root(context, root_length)
            for root_length in range(1, length)
        ),
        default=1,
    )


def periodic_prefix(period: Word, length: int) -> Word:
    copies, remainder = divmod(length, len(period))
    return period * copies + period[:remainder]


def main() -> None:
    primitive_periods = 0
    checked_prefixes = 0
    checked_locked = 0

    for length in range(1, 11):
        for period in product((2, 3), repeat=length):
            if primitive_root(period) != period:
                continue
            primitive_periods += 1

            for total_length in range(2 * length, 4 * length + 1):
                phase = total_length % length
                expected = max(
                    proper_circular_value(period, phase),
                    total_length // length,
                )
                word = periodic_prefix(period, total_length)
                assert exact_cn(word) == expected
                checked_prefixes += 1

            for exponent in range(2, 5):
                for appended in range(0, 2 * length + 1):
                    total_length = exponent * length + appended
                    phase = appended % length
                    expected = max(
                        proper_circular_value(period, phase),
                        total_length // length,
                    )
                    word = period * exponent + periodic_prefix(
                        period, appended
                    )
                    assert exact_cn(word) == expected
                    checked_locked += 1

    print(
        "periodic_prefix_formula_audit",
        "binary_primitive_period_length<=10",
        f"periods={primitive_periods}",
        f"general_prefixes={checked_prefixes}",
        f"locked_prefixes={checked_locked}",
    )
    print("A094004 calibration: run separately before accepting this output")


if __name__ == "__main__":
    main()
