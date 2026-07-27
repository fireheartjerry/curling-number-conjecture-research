"""Executed audit for the one-letter pointed-return straddle.

Run the repository A094004 calibration before this script.  Every
curling number below is recomputed by both independent implementations.
The symbolic companion note is ``pointed_return_suffix_rank.md``.
"""

from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference


Word = tuple[int, ...]


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def primitive(word: Word) -> bool:
    n = len(word)
    return all(
        word != word[:d] * (n // d)
        for d in range(1, n)
        if n % d == 0
    )


def occurrence_ends(word: Word, marker: Word) -> tuple[int, ...]:
    f = len(marker)
    return tuple(
        end
        for end in range(f, len(word) + 1)
        if word[end - f : end] == marker
    )


def audit(limit_m: int = 10, limit_gap: int = 16) -> int:
    checked = 0
    for maximum in range(4, limit_m + 1):
        high = maximum - 1
        for exit_symbol in range(2, maximum - 1):
            marker = (high,) * maximum + (maximum, exit_symbol)
            f = len(marker)

            for gap in range(limit_gap + 1):
                short_return = (exit_symbol,) * gap + marker
                long_return = (exit_symbol,) + short_return

                # The first copy of long_return starts at the final
                # symbol of the initial marker.  Its remaining suffix is
                # exactly short_return, beginning at the straddling
                # marker boundary.
                state = marker[:-1] + long_return * 2
                q = len(long_return)
                first_boundary = f
                aligned_boundary = f - 1 + q
                final_boundary = aligned_boundary + q

                assert state[first_boundary:aligned_boundary] == short_return
                assert state[aligned_boundary:final_boundary] == long_return
                assert state[-2 * q :] == long_return * 2
                assert primitive(long_return)

                # There are exactly the initial straddling marker and
                # the terminal markers of the two root copies.
                assert occurrence_ends(state, marker) == (
                    first_boundary,
                    aligned_boundary,
                    final_boundary,
                )

                # The pointed root block is not a context-free state:
                # isolated, it already has curling number one, while
                # the actual endpoint with its preceding equal copy has
                # value two.
                assert exact_cn(long_return) == 1
                assert exact_cn(state) == 2
                checked += 1

    return checked


def main() -> None:
    checked = audit()
    print(f"one_letter_models={checked} M_max=10 gap_max=16")


if __name__ == "__main__":
    main()
