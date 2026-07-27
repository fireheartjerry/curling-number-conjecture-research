"""Audit the two surviving forms of a one-edge restart cycle.

This file supplies finite local models only.  Every displayed high word
terminates, so none is a Curling Number Conjecture counterexample.

Run the A094004 calibration before accepting the output:

    python -m unittest \
      tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration
"""

from __future__ import annotations

from math import gcd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference, tail_length


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


def attaining_root_lengths(word: Word, exponent: int) -> list[int]:
    roots: list[int] = []
    for length in range(1, len(word) // exponent + 1):
        root = word[-length:]
        if word[-exponent * length :] == root * exponent:
            roots.append(length)
    return roots


def follow_common_output(
    high: Word, low: Word, output: Word
) -> tuple[Word, Word]:
    for symbol in output:
        assert exact_cn(high) == symbol
        assert exact_cn(low) == symbol
        high += (symbol,)
        low += (symbol,)
    return high, low


def audit_locked_model() -> None:
    root = tuple(map(int, "32"))
    exponent = 3
    reset = root * exponent
    output_block = root
    moved = root * (exponent - 1) + (exponent,)
    common_output = output_block[1:]

    assert root[0] == exponent
    assert moved + common_output == reset
    high, low = follow_common_output(
        moved, moved[1:], common_output
    )
    assert high == reset
    assert low == reset[1:]
    assert exact_cn(reset) == exponent
    assert exact_cn(reset[1:]) == exponent - 1
    assert tail_length(reset, step_limit=1000) == 3

    actual = reset
    assert exact_cn(actual) == output_block[0]
    actual += (output_block[0],)
    restarted = moved
    assert exact_cn(actual) == 3
    assert exact_cn(restarted) == output_block[1] == 2
    assert actual[-len(restarted) :] == restarted
    assert attaining_root_lengths(actual, 3) == [len(root)]

    print(
        "locked_one_edge_local_model",
        "Y=32",
        "k=3",
        "Q=32",
        "C=32323",
        "P=2",
        "tau(W)=3",
        "first_divergence=(t=1,actual=3,restarted=2,root=2=|Q|)",
    )


def audit_bordered_q21_model() -> None:
    base = tuple(map(int, "223222322232322232223"))
    root = base[1:] + base[:1]
    root_length = len(root)
    exponent = 3
    border_length = 11
    border = root[:border_length]

    assert primitive_root(root) == root
    assert border == root[-border_length:]
    assert border_length < root_length - gcd(
        root_length, border_length
    )
    assert root[0] == exponent - 1
    assert root[border_length] == exponent

    reset = root * exponent
    cycle_length = len(reset) - border_length
    deleted_block = reset[:cycle_length]
    output_block = reset[-cycle_length:]
    moved = reset[cycle_length:] + (exponent,)
    common_output = output_block[1:]

    assert output_block[0] == exponent
    assert primitive_root(output_block) == output_block
    assert exact_cn(output_block) == exponent - 1
    assert reset + output_block == deleted_block + reset
    assert moved == root[: border_length + 1]
    high, low = follow_common_output(
        moved, moved[1:], common_output
    )
    assert high == reset
    assert low == reset[1:]
    assert exact_cn(reset) == exponent
    assert exact_cn(reset[1:]) == exponent - 1

    reset_tail_time = tail_length(reset[1:], step_limit=100000)
    moved_tail_time = tail_length(moved[1:], step_limit=100000)
    reset_time = tail_length(reset, step_limit=100000)
    moved_time = tail_length(moved, step_limit=100000)
    assert reset_tail_time == 4
    assert moved_tail_time == len(common_output) + reset_tail_time
    assert len(reset) + reset_tail_time == len(moved) + moved_tail_time
    assert reset_time == 11
    assert moved_time == 62

    actual = reset
    restarted = reset
    divergence_time = None
    for time in range(len(output_block)):
        restarted_value = output_block[time]
        actual_value = exact_cn(actual)
        if actual_value != restarted_value:
            divergence_time = time
            break
        actual += (actual_value,)
        if time == 0:
            restarted = (restarted + (restarted_value,))[cycle_length:]
        else:
            restarted += (restarted_value,)
        assert restarted == actual[-len(restarted) :]
        assert exact_cn(restarted) == output_block[time + 1]

    assert divergence_time == 9
    assert exact_cn(actual) == 3
    assert output_block[divergence_time] == exact_cn(restarted) == 2
    assert actual[-len(restarted) :] == restarted
    crossing_roots = attaining_root_lengths(actual, 3)
    assert crossing_roots == [10]
    assert 3 * crossing_roots[0] > len(restarted)
    assert crossing_roots[0] < len(output_block)
    crossing_power = actual[-3 * crossing_roots[0] :]
    restarted_rank = len(restarted) + tail_length(
        restarted[1:], step_limit=100000
    )
    ancestor_expression = len(actual) + tail_length(
        actual[1:], step_limit=100000
    )
    crossing_expression = len(crossing_power) + tail_length(
        crossing_power[1:], step_limit=100000
    )
    assert restarted_rank == 67
    assert ancestor_expression == 74
    assert crossing_expression == 34
    assert tail_length(crossing_power, step_limit=100000) == 2

    print(
        "bordered_one_edge_q21_local_model",
        "Y=232223222323222322232",
        "h=11",
        "k=3",
        f"|W|={len(reset)}",
        f"|Q|={len(output_block)}",
        f"|C|={len(moved)}",
        f"|P|={len(common_output)}",
        f"R={len(reset) + reset_tail_time}",
        f"tau(W)={reset_time}",
        f"tau(C)={moved_time}",
        "first_divergence=(t=9,actual=3,restarted=2,root=10<|Q|)",
        "endpoint_expressions=(restarted=67,ancestor=74,crossing_power=34)",
        "tau(crossing_power)=2",
    )


def main() -> None:
    audit_locked_model()
    audit_bordered_q21_model()
    print("A094004 calibration: run separately before accepting this output")


if __name__ == "__main__":
    main()
