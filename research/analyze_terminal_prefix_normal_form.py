"""Enumerate the exact normal form of a hypothetical final-2 prefix drop.

Let ``P=T2`` with ``cn(T)=1``.  A circular square of root ``q`` ending
immediately before the final symbol and crossing the origin has

    T = X Y X,       |X| = |T|-q,       |Y| = 2q-|T|,

and the wrapping equality is equivalent to

    suffix_|Y|(T2) = Y.

This script enumerates these word equations and records where the
self-encoded proper-cube profile first fails.  It is diagnostic only.
All finite curling numbers are checked with both implementations.
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


def cube_roots(word: Word, cut: int) -> tuple[int, ...]:
    n = len(word)
    return tuple(
        root
        for root in range(1, n)
        if all(
            word[(cut - block * root + offset) % n]
            == word[(cut - root + offset) % n]
            for block in (2, 3)
            for offset in range(root)
        )
    )


def words(length: int):
    for bits in itertools.product((2, 3), repeat=length):
        yield bits


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-sum", type=int, default=16)
    parser.add_argument("--examples", type=int, default=3)
    args = parser.parse_args()

    for total in range(2, args.max_sum + 1):
        count = 0
        first_mismatch: dict[int, int] = {}
        last_symbol: dict[int, int] = {}
        suffix_relation: dict[str, int] = {}
        quotient_class: dict[int, int] = {}
        first_by_quotient: dict[tuple[int, int], int] = {}
        examples = []
        for h in range(1, total):
            e = total - h
            for x in words(h):
                if x[0] != 2:
                    continue
                for y in words(e):
                    t = x + y + x
                    p = t + (2,)
                    if p[-e:] != y or exact_cn(t) != 1:
                        continue
                    roots = [cube_roots(p, cut) for cut in range(len(p))]
                    mismatches = tuple(
                        cut
                        for cut, found in enumerate(roots)
                        if (p[cut] == 3) != bool(found)
                    )
                    assert mismatches
                    count += 1
                    s = h + 1
                    quotient = e // s
                    assert quotient <= 1 or 0 in mismatches
                    quotient_class[quotient] = quotient_class.get(quotient, 0) + 1
                    first_key = (quotient, mismatches[0])
                    first_by_quotient[first_key] = (
                        first_by_quotient.get(first_key, 0) + 1
                    )
                    first_mismatch[mismatches[0]] = (
                        first_mismatch.get(mismatches[0], 0) + 1
                    )
                    last_symbol[t[-1]] = last_symbol.get(t[-1], 0) + 1
                    relation = (
                        "Y_suffix_X"
                        if e <= h and x[-e:] == y
                        else "not_Y_suffix_X"
                    )
                    suffix_relation[relation] = suffix_relation.get(relation, 0) + 1
                    if len(examples) < args.examples:
                        examples.append(
                            (
                                "".join(map(str, x)),
                                "".join(map(str, y)),
                                "".join(map(str, p)),
                                mismatches,
                                tuple((cut, roots[cut]) for cut in mismatches),
                            )
                        )
        if count:
            print(
                f"h_plus_e={total} count={count} "
                f"first_mismatch={first_mismatch} "
                f"last_symbol={last_symbol} suffix={suffix_relation}"
                f" quotient={quotient_class} first_by_q={first_by_quotient}"
            )
            for example in examples:
                print("  " + repr(example))


if __name__ == "__main__":
    main()
