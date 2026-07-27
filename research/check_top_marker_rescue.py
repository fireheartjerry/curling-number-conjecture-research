"""Small exact regressions for ``top_marker_rescue.md``."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from curling import curling_number, curling_number_reference


def checked_cn(word: tuple[int, ...]) -> int:
    fast = curling_number(word)
    slow = curling_number_reference(word)
    assert fast == slow
    return fast


def maximizing_roots(word: tuple[int, ...]) -> tuple[int, ...]:
    exponent = checked_cn(word)
    return tuple(
        root
        for root in range(1, len(word) // exponent + 1)
        if word[-exponent * root :] == word[-root:] * exponent
    )


def main() -> None:
    root = (2, 3)
    cube = root * 3
    broken = cube + (3,)
    assert checked_cn(cube) == 3
    assert checked_cn(broken) == 2
    assert maximizing_roots(broken) == (1,)

    # A contaminated scale can also reset to a unary clean maximum root
    # without leaving the high component.
    reset_root = (2, 3, 3)
    reset_cube = reset_root * 3
    assert checked_cn(reset_cube) == 3
    assert maximizing_roots(reset_cube) == (3,)
    reset_once = reset_cube + (3,)
    assert checked_cn(reset_once) == 3
    assert maximizing_roots(reset_once) == (1,)
    reset_twice = reset_once + (3,)
    assert checked_cn(reset_twice) == 4
    assert maximizing_roots(reset_twice) == (1,)

    family_records = []
    entrance_records = []
    for maximum in (4, 5, 6, 7):
        high = maximum - 1
        low = maximum - 2
        family_root = (low,) + (high,) * (high - 1)
        first = family_root * high
        second = first + (high,)
        third = second + (high,)
        assert checked_cn(first) == high
        assert maximizing_roots(first) == (high,)
        assert checked_cn(second) == high
        assert 1 in maximizing_roots(second)
        assert checked_cn(third) == maximum
        assert maximizing_roots(third) == (1,)
        family_records.append(
            (
                maximum,
                family_root,
                (high, high, maximum),
            )
        )

        # A second contaminated family realizes the complete forced
        # top entrance high^maximum, maximum.  The long root replays its
        # high-symbol prefix, the unary run ties it at the last high cut,
        # and then the unary root creates the maximum.
        entrance_root = (high,) * high + (low,)
        entrance_state = entrance_root * high
        entrance_values = []
        entrance_roots = []
        for _ in range(high + 2):
            value = checked_cn(entrance_state)
            entrance_values.append(value)
            entrance_roots.append(maximizing_roots(entrance_state))
            entrance_state += (value,)
        assert tuple(entrance_values) == (
            (high,) * maximum + (maximum,)
        )
        assert all(
            len(entrance_root) in roots
            for roots in entrance_roots[:high]
        )
        assert entrance_roots[high] == (1, len(entrance_root))
        assert entrance_roots[-1] == (1,)
        entrance_records.append(
            (
                maximum,
                entrance_root,
                tuple(entrance_values),
                tuple(entrance_roots),
            )
        )
    print(
        {
            "R": root,
            "cn_R3": 3,
            "broken": broken,
            "cn_broken": 2,
            "maximizing_roots_broken": (1,),
            "scale_reset": {
                "R": reset_root,
                "values": (3, 3, 4),
                "maximizing_roots": ((3,), (1,), (1,)),
            },
            "family_records": tuple(family_records),
            "forced_entrance_records": tuple(entrance_records),
        }
    )


if __name__ == "__main__":
    main()
