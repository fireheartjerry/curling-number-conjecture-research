"""Enumerate the CLSW canonical form forced by a final-2 prefix drop.

After rotating ``P=T2`` to ``Q=2T``, CLSW Theorem 9 gives

    Q = X Y X,   cn(Q)=cn(X)=1,   Y a nonempty proper suffix of X.

The original and rotated origins imply ``Q[:2] == (2,2)``.  This script
records the failure cuts of the proper circular cube-indicator equation.
It is diagnostic only, and all finite curling numbers are checked by both
implementations.
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-x", type=int, default=15)
    parser.add_argument("--examples", type=int, default=2)
    args = parser.parse_args()

    for x_length in range(2, args.max_x + 1):
        count = 0
        location_types: dict[str, int] = {}
        first_locations: dict[str, int] = {}
        examples = []
        for x in itertools.product((2, 3), repeat=x_length):
            if x[:2] != (2, 2) or exact_cn(x) != 1:
                continue
            for y_length in range(1, x_length):
                y = x[-y_length:]
                q = x + y + x
                if exact_cn(q) != 1:
                    continue
                roots = tuple(cube_roots(q, cut) for cut in range(len(q)))
                mismatches = tuple(
                    cut
                    for cut in range(len(q))
                    if (q[cut] == 3) != bool(roots[cut])
                )
                assert mismatches
                count += 1
                a_length = x_length - y_length

                def kind(cut: int) -> str:
                    if cut == 0:
                        return "origin"
                    if cut == a_length:
                        return "A|Y"
                    if cut == x_length:
                        return "X|Y"
                    if cut == x_length + y_length:
                        return "Y|X"
                    if cut == 2 * x_length + y_length - 1:
                        return "last"
                    if cut < a_length:
                        return "A1"
                    if cut < x_length:
                        return "Y1"
                    if cut < x_length + y_length:
                        return "Y2"
                    if cut < 2 * x_length + y_length:
                        return "X2"
                    raise AssertionError

                for cut in mismatches:
                    label = kind(cut)
                    location_types[label] = location_types.get(label, 0) + 1
                first = kind(mismatches[0])
                first_locations[first] = first_locations.get(first, 0) + 1
                if len(examples) < args.examples:
                    examples.append(
                        (
                            "".join(map(str, x)),
                            "".join(map(str, y)),
                            "".join(map(str, q)),
                            tuple((cut, kind(cut), roots[cut]) for cut in mismatches),
                        )
                    )
        if count:
            print(
                f"|X|={x_length} count={count} "
                f"all_mismatch_types={location_types} "
                f"first_mismatch_types={first_locations}"
            )
            for example in examples:
                print("  " + repr(example))


if __name__ == "__main__":
    main()
