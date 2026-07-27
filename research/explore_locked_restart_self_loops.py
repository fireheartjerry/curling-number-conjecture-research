"""Enumerate finite local models of a one-edge locked restart cycle.

This is exploratory evidence, not a proof and not an assertion of badness.
Run the A094004 calibration before accepting any reported curling number:

    python -m unittest \
      tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration
"""

from __future__ import annotations

from itertools import product
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


def follows_common_output(high: Word, low: Word, output: Word) -> bool:
    for symbol in output:
        if exact_cn(high) != symbol or exact_cn(low) != symbol:
            return False
        high += (symbol,)
        low += (symbol,)
    return True


def main() -> None:
    models: list[tuple[Word, int, int, Word, int | None]] = []
    for root_length in range(1, 11):
        for root in product((2, 3), repeat=root_length):
            if primitive_root(root) != root:
                continue
            for exponent in range(2, 5):
                reset = root * exponent
                if root[0] != exponent:
                    continue
                if exact_cn(reset) != exponent:
                    continue
                if exact_cn(reset[1:]) != exponent - 1:
                    continue
                for deleted_root_copies in range(1, exponent):
                    output_block = root * deleted_root_copies
                    common_output = output_block[1:]
                    moved = (
                        root * (exponent - deleted_root_copies)
                        + (exponent,)
                    )
                    if moved + common_output != reset:
                        continue
                    if not follows_common_output(
                        moved, moved[1:], common_output
                    ):
                        continue
                    assert exact_cn(reset) == exponent
                    assert exact_cn(reset[1:]) == exponent - 1
                    try:
                        hitting_time = tail_length(reset, step_limit=10000)
                    except RuntimeError:
                        hitting_time = None
                    models.append(
                        (
                            root,
                            exponent,
                            deleted_root_copies,
                            common_output,
                            hitting_time,
                        )
                    )

    nonterminating_within_limit = [
        model for model in models if model[-1] is None
    ]
    print(
        "locked_restart_self_loop_search",
        "binary_roots_length<=10",
        "exponents=2..4",
        f"models={len(models)}",
        f"not_terminated_within_10000={len(nonterminating_within_limit)}",
    )
    for root, exponent, deleted_copies, output, hitting_time in models:
        print(
            "model",
            f"Y={''.join(map(str, root))}",
            f"k={exponent}",
            f"e={deleted_copies}",
            f"P={''.join(map(str, output))}",
            f"tau(W)={hitting_time}",
        )
    print("A094004 calibration: run separately before accepting this output")


if __name__ == "__main__":
    main()
