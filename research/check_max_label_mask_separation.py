"""Executed regression for ``max_label_mask_separation.md``."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from curling import curling_number, curling_number_reference


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return all(
        not (n % d == 0 and word == word[:d] * (n // d))
        for d in range(1, n)
    )


def checked_cn(word: tuple[int, ...]) -> int:
    fast = curling_number(word)
    slow = curling_number_reference(word)
    assert fast == slow
    return fast


def high_components(word: tuple[int, ...], high: int):
    result = []
    current = []
    for i, value in enumerate(word):
        if value == high:
            current.append(i)
        elif current:
            result.append(tuple(current))
            current = []
    if current:
        result.append(tuple(current))
    return tuple(result)


def main() -> None:
    y = tuple(map(int, "34344434443444"))
    assert primitive(y)
    assert checked_cn(y * 3) == 3
    assert checked_cn(y * 4) == 4
    values = tuple(checked_cn(y * 3 + y[:t]) for t in range(len(y)))
    assert values == (3,) * len(y)
    masks = tuple(i for i, value in enumerate(y) if value == 4)
    assert masks == (1, 3, 4, 5, 7, 8, 9, 11, 12, 13)
    components = high_components(y, 4)
    assert components == (
        (1,),
        (3, 4, 5),
        (7, 8, 9),
        (11, 12, 13),
    )
    print(
        {
            "Y": "".join(map(str, y)),
            "primitive": True,
            "cn_Y3": 3,
            "cn_Y4": 4,
            "prefix_values": values,
            "masked_components": components,
            "ambient_lower_bound": 113,
        }
    )


if __name__ == "__main__":
    main()
