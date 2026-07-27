"""Executed shallow same-scale revisit below the period-gluing threshold.

The finite word is indexed from -16 through 14.  It contains a
root-seven cube ending at cut 5 and a different root-seven square
ending at cut 14.  Their period-seven intervals overlap in only five
symbols, so they need not belong to one maximal period-seven run.

This is a local countergeometry to an unconditional claim that revisiting
a previous numerical cap automatically violates the leftmost-square
choice.  It is not a circular fixed profile.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from curling import curling_number, curling_number_reference

from check_run_length_grammar import primitive


Word = tuple[int, ...]

LEFT = -16
WORD: Word = tuple(map(int, "2222223222222322222233222223322"))
ROOT = 7

CUBE_START = -16
CUBE_END = 5
SQUARE_START = 0
SQUARE_END = 14


def factor(start: int, end: int) -> Word:
    return WORD[start - LEFT : end - LEFT]


def checked_cn(cut: int) -> int:
    prefix = factor(LEFT, cut)
    value = curling_number(prefix)
    assert value == curling_number_reference(prefix)
    return value


def main() -> None:
    cube = factor(CUBE_START, CUBE_END)
    square = factor(SQUARE_START, SQUARE_END)
    cube_root = cube[:ROOT]
    square_root = square[:ROOT]

    assert cube == cube_root * 3
    assert square == square_root * 2
    assert primitive(cube_root)
    assert primitive(square_root)
    assert cube_root != square_root

    overlap = CUBE_END - SQUARE_START
    assert overlap == 5 < ROOT
    assert WORD[CUBE_END - LEFT] == 3
    assert WORD[CUBE_END + 1 - LEFT] == 2
    assert WORD[SQUARE_END - LEFT] == 2

    curling_values = {
        CUBE_END: checked_cn(CUBE_END),
        SQUARE_END: checked_cn(SQUARE_END),
    }
    assert curling_values == {5: 3, 14: 2}

    print(
        {
            "indexed_word": (LEFT, "".join(map(str, WORD))),
            "cube": (
                (CUBE_START, CUBE_END),
                ROOT,
                "".join(map(str, cube_root)),
            ),
            "square": (
                (SQUARE_START, SQUARE_END),
                ROOT,
                "".join(map(str, square_root)),
            ),
            "overlap": overlap,
            "period_gluing_threshold": ROOT,
            "same_numerical_cap": True,
            "same_period_run_forced": False,
            "curling_values": curling_values,
        }
    )


if __name__ == "__main__":
    main()
