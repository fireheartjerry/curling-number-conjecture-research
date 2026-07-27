"""Bounded audit of the restart-cycle conjugacy classification.

Run the A094004 calibration before accepting this output:

    python -m unittest \
      tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration

The audit enumerates every binary whole-power reset of length at most 18
and every candidate cycle period no longer than the reset.  The ``n=0``
case has cycle period longer than the reset and is proved separately by
the conjugacy-equation length formula.
"""

from __future__ import annotations

from itertools import product
from math import gcd
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
    raise AssertionError("a nonempty word always has a primitive root")


def has_period(word: Word, period: int) -> bool:
    return all(
        word[index] == word[index + period]
        for index in range(len(word) - period)
    )


def main() -> None:
    audited = 0
    locked = 0
    bordered = 0
    pointed_locked = 0
    pointed_bordered = 0
    square_completion = 0

    for length in range(2, 19):
        for reset in product((2, 3), repeat=length):
            root = primitive_root(reset)
            root_length = len(root)
            exponent = length // root_length
            if exponent < 2:
                continue
            if exact_cn(reset) != exponent:
                continue
            if exact_cn(reset[1:]) != exponent - 1:
                continue

            for cycle_length in range(1, length + 1):
                if not has_period(reset, cycle_length):
                    continue

                deleted_block = reset[:cycle_length]
                output_block = reset[-cycle_length:]
                assert (
                    reset + output_block
                    == deleted_block + reset
                )

                copies, border_length = divmod(length, cycle_length)
                border = reset[:border_length]
                middle = deleted_block[border_length:]
                assert middle
                assert deleted_block == border + middle
                assert output_block == middle + border
                assert reset == border + output_block * copies

                common_divisor = gcd(root_length, cycle_length)
                audited += 1
                if (
                    length
                    >= root_length
                    + cycle_length
                    - common_divisor
                ):
                    assert cycle_length % root_length == 0
                    expected = root * (cycle_length // root_length)
                    assert deleted_block == output_block == expected
                    locked += 1
                    if output_block[0] == exponent:
                        pointed_locked += 1
                    continue

                assert copies == 1
                assert 0 < border_length < root_length - common_divisor
                assert reset == border + middle + border
                completion_root = primitive_root(output_block)
                completion_exponent = (
                    cycle_length // len(completion_root)
                )
                assert completion_exponent == 1
                bordered += 1
                if output_block[0] == exponent:
                    pointed_bordered += 1
                assert completion_exponent != 2

    # Small exact noncommuting model for the purely local equations.
    # It is not asserted to be a genuine restart transition.
    model_reset = tuple(map(int, "232232"))
    model_deleted_block = tuple(map(int, "23223"))
    model_output_block = tuple(map(int, "32232"))
    assert (
        model_reset + model_output_block
        == model_deleted_block + model_reset
    )
    assert exact_cn(model_reset) == 2
    assert exact_cn(model_reset[1:]) == 1
    assert primitive_root(model_output_block) == model_output_block

    # The pointed condition Q[0]=cn(W) is forced by a genuine restart
    # cycle because its first splice symbol is the reset output k.
    pointed_model_reset = tuple(map(int, "323323"))
    pointed_model_deleted_block = tuple(map(int, "32332"))
    pointed_model_output_block = tuple(map(int, "23323"))
    assert (
        pointed_model_reset + pointed_model_output_block
        == pointed_model_deleted_block + pointed_model_reset
    )
    assert exact_cn(pointed_model_reset) == 2
    assert exact_cn(pointed_model_reset[1:]) == 1
    assert pointed_model_output_block[0] == exact_cn(pointed_model_reset)
    assert (
        primitive_root(pointed_model_output_block)
        == pointed_model_output_block
    )

    # A commuting equation can also occur inside the n=0 over-window
    # alternative.  This audits the explicit n>=1 qualifier in Lemma 14.
    over_reset = tuple(map(int, "323232"))
    over_output_block = tuple(map(int, "32323232"))
    over_deleted_block = over_output_block
    assert len(over_output_block) > len(over_reset)
    assert (
        over_reset + over_output_block
        == over_deleted_block + over_reset
    )
    assert exact_cn(over_reset) == 3
    assert exact_cn(over_reset[1:]) == 2
    assert primitive_root(over_output_block) == tuple(map(int, "32"))

    print(
        "cycle_conjugacy_audit",
        "binary_reset_length<=18",
        f"cases={audited}",
        f"locked={locked}",
        f"bordered={bordered}",
        f"pointed_locked={pointed_locked}",
        f"pointed_bordered={pointed_bordered}",
        f"square_completion={square_completion}",
    )
    print(
        "bordered_local_model",
        "W=232232",
        "A=23223",
        "Q=32232",
        "WQ=AW",
        "cn(W)=2",
        "cn(W.tail)=1",
    )
    print(
        "pointed_bordered_local_model",
        "W=323323",
        "A=32332",
        "Q=23323",
        "WQ=AW",
        "Q[0]=cn(W)=2",
        "cn(W.tail)=1",
    )
    print(
        "commuting_over_window_local_model",
        "W=323232",
        "Q=A=32323232",
        "|Q|=8>|W|=6",
        "primitive_tape_period=2",
    )
    print("A094004 calibration: run separately before accepting this output")


if __name__ == "__main__":
    main()
