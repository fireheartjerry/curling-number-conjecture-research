"""Executed checks for the one-letter straddle in top_return_straddle.md.

The construction is local: it verifies the exact curling numbers at the
two cuts used in the word equation.  It is not asserted to be a circular
fixed profile.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from curling import curling_number, curling_number_reference


def maximizing_roots(word: tuple[int, ...]) -> tuple[int, ...]:
    k = curling_number(word)
    n = len(word)
    roots: list[int] = []
    for q in range(1, n // k + 1):
        block = word[n - q :]
        if word[n - k * q :] == block * k:
            roots.append(q)
    return tuple(roots)


records = []
for maximum in range(4, 11):
    high = maximum - 1
    exit_symbol = 2
    component = (high,) * maximum + (maximum,)
    marker = component + (exit_symbol,)
    root = (exit_symbol,) + marker

    # component + root^2 = marker^2 + exit_symbol + marker.
    word = component + root * 2
    assert word == marker * 2 + (exit_symbol,) + marker

    aligned_cut = marker * 2
    assert curling_number(aligned_cut) == 2
    assert curling_number_reference(aligned_cut) == 2
    assert maximizing_roots(aligned_cut) == (len(marker),)

    assert curling_number(word) == 2
    assert curling_number_reference(word) == 2
    assert maximizing_roots(word) == (len(root),)

    # The earliest root begins at the last exit symbol of the first
    # marker.  The next aligned root begins immediately after the second
    # marker.  Their first symbols are both the exit symbol.
    earliest_start = len(component)
    aligned_start = earliest_start + len(root)
    assert word[earliest_start : earliest_start + len(root)] == root
    assert word[aligned_start : aligned_start + len(root)] == root
    assert word[earliest_start - len(component) : earliest_start + 1] == marker
    assert word[aligned_start - len(marker) : aligned_start] == marker

    records.append(
        (
            maximum,
            len(marker),
            len(root),
            curling_number(aligned_cut),
            maximizing_roots(aligned_cut),
            curling_number(word),
            maximizing_roots(word),
        )
    )

print(tuple(records))
