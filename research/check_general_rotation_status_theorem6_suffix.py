"""Audit the residual word in ``general_rotation_status.md``, Theorem 6.

Run the A094004 calibration before this script.  Every displayed curling
number is computed by both project implementations.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from curling import curling_number, curling_number_reference

from check_run_length_grammar import primitive


def checked_cn(word: tuple[int, ...]) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def general_identity(
    c: tuple[int, ...], s: int
) -> dict[str, object]:
    """Check the suffix-square identity; no profile hypothesis is used."""
    n = len(c)
    assert 0 < s < n
    a = c[:s]
    b = c[s:]
    y = c + c + a
    u = y + y
    v = u[1:]
    square_root = b + a
    assert y == a + b + a + b + a
    assert v[-2 * n :] == square_root + square_root
    return {
        "n": n,
        "s": s,
        "A": a,
        "B": b,
        "Y": y,
        "V_suffix_root": square_root,
        "V_has_square_suffix": True,
    }


def numeric_audit() -> dict[str, object]:
    # This primitive C satisfies every residual equation (18)--(19):
    # n=5, s=3, h=3, a=C[0]=3.
    c = (3, 2, 3, 3, 2)
    n = len(c)
    s = 3
    h = n + 1 - s
    a = c[0]
    assert primitive(c)
    assert 2 <= s <= n - 1
    assert 2 <= h <= n - 1
    assert c[:h] == c[s:] + (a,)
    assert c[h - 1] == a
    assert c[h] == max(3, c[1])

    y = c + c + c[:s]
    u = y + y
    v = u[1:]
    suffix = v[-2 * n :]
    assert suffix == (c[s:] + c[:s]) * 2
    values = {
        "C": checked_cn(c),
        "Y": checked_cn(y),
        "U": checked_cn(u),
        "V": checked_cn(v),
        "V_square_suffix": checked_cn(suffix),
    }
    assert values["U"] == 2
    assert values["V"] >= 2
    return {
        "C": c,
        "n": n,
        "s": s,
        "h": h,
        "Y": y,
        "lengths": {
            "C": len(c),
            "Y": len(y),
            "U": len(u),
            "V": len(v),
            "V_square_suffix": len(suffix),
        },
        "curling_numbers": values,
        "V_square_suffix": suffix,
        "V_square_root": c[s:] + c[:s],
    }


def main() -> None:
    identity = general_identity((7, 4, 9, 2, 6, 5, 8), 3)
    example = numeric_audit()
    print({"general_suffix_identity": identity, "numeric_audit": example})


if __name__ == "__main__":
    main()
