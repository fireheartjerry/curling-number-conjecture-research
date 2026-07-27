"""Executed local model of two consecutive slow cap ascents.

The word is indexed from -58 through 1. It contains a root-six square
ending at cut 1, a root-nine cube ending at cut 0, and a root-sixteen
cube ending at cut -10. The cube midpoints give the intervening cap
squares ending at -9 and -26.

This is a local word-equation certificate, not a circular fixed profile.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from curling import curling_number, curling_number_reference

from check_run_length_grammar import primitive


Word = tuple[int, ...]

LEFT = -58
WORD: Word = tuple(
    map(
        int,
        "233232232233232223323223223323222332322322332322322332322332",
    )
)

S = 6
D = 1
K = 3
U = S + K

D_PRIME = 1
L = 7
V = U + L

OLD_SQUARE_END = 1
FIRST_CUBE_END = 0
MIDPOINT_ONE = -U
SECOND_CUBE_END = MIDPOINT_ONE - D_PRIME
MIDPOINT_TWO = SECOND_CUBE_END - V


def factor(start: int, end: int) -> Word:
    return WORD[start - LEFT : end - LEFT]


def checked_cn(cut: int) -> int:
    prefix = factor(LEFT, cut)
    value = curling_number(prefix)
    assert value == curling_number_reference(prefix)
    return value


def main() -> None:
    assert len(WORD) == OLD_SQUARE_END - LEFT + 1

    old_square = factor(OLD_SQUARE_END - 2 * S, OLD_SQUARE_END)
    old_root = old_square[:S]
    assert old_square == old_root * 2
    assert primitive(old_root)

    first_cube = factor(FIRST_CUBE_END - 3 * U, FIRST_CUBE_END)
    first_root = first_cube[:U]
    assert first_cube == first_root * 3
    assert primitive(first_root)

    midpoint_square_one = factor(MIDPOINT_ONE - 2 * U, MIDPOINT_ONE)
    assert midpoint_square_one == first_root * 2

    second_cube = factor(SECOND_CUBE_END - 3 * V, SECOND_CUBE_END)
    second_root = second_cube[:V]
    assert second_cube == second_root * 3
    assert primitive(second_root)

    midpoint_square_two = factor(MIDPOINT_TWO - 2 * V, MIDPOINT_TWO)
    assert midpoint_square_two == second_root * 2

    assert K < S - D
    assert L < U - D_PRIME
    assert WORD[FIRST_CUBE_END - LEFT] == 3
    assert WORD[OLD_SQUARE_END - LEFT] == 2
    assert WORD[SECOND_CUBE_END - LEFT] == 3
    assert WORD[MIDPOINT_ONE - LEFT] == 2
    assert WORD[MIDPOINT_TWO - LEFT] == 2

    curling_values = {
        MIDPOINT_TWO: checked_cn(MIDPOINT_TWO),
        SECOND_CUBE_END: checked_cn(SECOND_CUBE_END),
        MIDPOINT_ONE: checked_cn(MIDPOINT_ONE),
        FIRST_CUBE_END: checked_cn(FIRST_CUBE_END),
        OLD_SQUARE_END: checked_cn(OLD_SQUARE_END),
    }
    assert curling_values == {
        MIDPOINT_TWO: 2,
        SECOND_CUBE_END: 3,
        MIDPOINT_ONE: 2,
        FIRST_CUBE_END: 3,
        OLD_SQUARE_END: 2,
    }

    print(
        {
            "indexed_word": (LEFT, "".join(map(str, WORD))),
            "ascents": ((S, U, K, D), (U, V, L, D_PRIME)),
            "roots": {
                S: "".join(map(str, old_root)),
                U: "".join(map(str, first_root)),
                V: "".join(map(str, second_root)),
            },
            "curling_values": curling_values,
        }
    )


if __name__ == "__main__":
    main()
