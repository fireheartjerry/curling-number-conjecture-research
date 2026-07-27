"""Search finite maximum-root words whose only replay masks are terminal.

For M=4, enumerate primitive words Y over {3,4}, beginning in 3, with

    cn(Y^3)=3, cn(Y^4)=4,

and compute every intermediate replay value cn(Y^3 Y[:t]).  Retain words
for which any 4->3 loss occurs only in the final run of 4s.  The exact
curling values are cross-checked by both reference implementations.

These finite words need not embed in a circular fixed profile.  The search
is a diagnostic for the residual terminal-mask branch after choosing a
globally longest maximum root.
"""

from __future__ import annotations

import argparse
from itertools import product
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from curling import curling_number, curling_number_reference


def checked_cn(word: tuple[int, ...]) -> int:
    fast = curling_number(word)
    slow = curling_number_reference(word)
    assert fast == slow
    return fast


def primitive(word: tuple[int, ...]) -> bool:
    return all(
        not (
            len(word) % period == 0
            and word == word[:period] * (len(word) // period)
        )
        for period in range(1, len(word))
    )


def terminal_start(word: tuple[int, ...], high: int) -> int:
    start = len(word)
    while start and word[start - 1] == high:
        start -= 1
    return start


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-length", type=int, default=16)
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()
    M = 4
    found = 0
    checked = 0
    for length in range(2, args.max_length + 1):
        for tail in product((M - 1, M), repeat=length - 1):
            word = (M - 1,) + tail
            if word[-1] != M or not primitive(word):
                continue
            checked += 1
            if checked_cn(word * (M - 1)) != M - 1:
                continue
            if checked_cn(word * M) != M:
                continue
            values = tuple(
                checked_cn(word * (M - 1) + word[:phase])
                for phase in range(length)
            )
            if any(
                value not in (M - 1, word[phase])
                for phase, value in enumerate(values)
            ):
                continue
            masks = tuple(
                phase
                for phase in range(length)
                if word[phase] == M and values[phase] == M - 1
            )
            if not masks:
                continue
            start = terminal_start(word, M)
            if any(phase < start for phase in masks):
                continue
            print(
                {
                    "Y": "".join(map(str, word)),
                    "length": length,
                    "terminal_start": start,
                    "values": values,
                    "masks": masks,
                }
            )
            found += 1
            if found >= args.limit:
                print({"checked": checked, "reported": found})
                return
    print({"checked": checked, "reported": found})


if __name__ == "__main__":
    main()
