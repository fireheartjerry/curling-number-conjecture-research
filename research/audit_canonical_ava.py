"""Exhaustive diagnostics for the canonical terminal-2 word ``Q=A V A``.

The mathematical reduction is:

* ``cn(Q)=1``;
* ``V`` is a nonempty proper suffix of ``A``;
* the proper circular square of root ``R=V A`` ending at cut zero is
  witnessed linearly by ``V Q=(V A)^2``.

This script does not treat finite evidence as a proof.  It enumerates the
normal form directly, computes every proper circular square and cube root,
and looks for the first hypotheses which distinguish the normal form from
an exact self-encoded curling profile.
"""

from __future__ import annotations

import argparse
import itertools
import sys
from pathlib import Path

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
        any(word[index] != word[index % period] for index in range(period, n))
        for period in range(1, n)
        if n % period == 0
    )


def power(word: Word, cut: int, root: int, exponent: int) -> bool:
    n = len(word)
    return all(
        word[(cut - block * root + offset) % n]
        == word[(cut - root + offset) % n]
        for block in range(2, exponent + 1)
        for offset in range(root)
    )


def roots(word: Word, cut: int, exponent: int) -> tuple[int, ...]:
    return tuple(
        root
        for root in range(1, len(word))
        if power(word, cut, root, exponent)
    )


def canonical_decompositions(word: Word) -> tuple[tuple[int, int], ...]:
    """Return ``(|A|,|V|)`` for all ``word=A V A`` with ``V`` suffix ``A``."""
    n = len(word)
    out = []
    for a in range(1, n):
        b = n - 2 * a
        if not 1 <= b < a:
            continue
        left = word[:a]
        middle = word[a : a + b]
        right = word[a + b :]
        if left == right and left[-b:] == middle and exact_cn(left) == 1:
            out.append((a, b))
    return tuple(out)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-length", type=int, default=24)
    parser.add_argument("--examples", type=int, default=12)
    args = parser.parse_args()

    totals = {
        "canonical": 0,
        "all_square": 0,
        "cube_exact": 0,
        "full_profile": 0,
        "outer_global_max": 0,
    }
    best: list[
        tuple[
            int,
            int,
            int,
            Word,
            tuple[int, ...],
            tuple[int, ...],
            tuple[tuple[int, int], ...],
        ]
    ] = []

    for a in range(2, (args.max_length - 1) // 2 + 1):
        for symbols in itertools.product((2, 3), repeat=a - 2):
            block_a = (2, 2) + symbols
            if exact_cn(block_a) != 1:
                continue
            for b in range(1, a):
                n = 2 * a + b
                if n > args.max_length:
                    continue
                block_v = block_a[-b:]
                word = block_a + block_v + block_a
                if exact_cn(word) != 1 or not primitive(word):
                    continue
                totals["canonical"] += 1

                square_sets = tuple(roots(word, cut, 2) for cut in range(n))
                cube_sets = tuple(roots(word, cut, 3) for cut in range(n))
                square_missing = tuple(
                    cut for cut, found in enumerate(square_sets) if not found
                )
                cube_mismatch = tuple(
                    cut
                    for cut, found in enumerate(cube_sets)
                    if bool(found) != (word[cut] == 3)
                )
                if not square_missing:
                    totals["all_square"] += 1
                if not cube_mismatch:
                    totals["cube_exact"] += 1
                if not square_missing and not cube_mismatch:
                    totals["full_profile"] += 1

                outer = a + b
                assert power(word, 0, outer, 2)
                max_square = max(
                    root
                    for found in square_sets
                    for root in found
                )
                if outer == max_square:
                    totals["outer_global_max"] += 1

                decompositions = canonical_decompositions(word)
                assert (a, b) in decompositions
                assert len(decompositions) == 1
                score = len(square_missing) + len(cube_mismatch)
                best.append(
                    (
                        score,
                        n,
                        outer,
                        word,
                        square_missing,
                        cube_mismatch,
                        decompositions,
                    )
                )

    print("convention: cuts are zero-based; roots are proper (< word length)")
    print("totals=" + repr(totals))
    for (
        score,
        n,
        outer,
        word,
        square_missing,
        cube_mismatch,
        decompositions,
    ) in sorted(best)[: args.examples]:
        square_sets = tuple(roots(word, cut, 2) for cut in range(n))
        max_square = max(root for found in square_sets for root in found)
        print(
            " ".join(
                (
                    f"score={score}",
                    f"n={n}",
                    f"outer={outer}",
                    f"max_square={max_square}",
                    "Q=" + "".join(map(str, word)),
                    f"missing_square={square_missing}",
                    f"cube_mismatch={cube_mismatch}",
                    f"decompositions={decompositions}",
                )
            )
        )


if __name__ == "__main__":
    main()
