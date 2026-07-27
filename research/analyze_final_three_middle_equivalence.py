"""Classify equality consequences of a cube at the final-3 middle cut.

The word variables are the letters of ``X``.  ``A`` is represented as
the length-``a`` suffix of ``X``.  For each possible cube root, union-find
computes the equalities forced by that cube in the circular word
``Q = X A X A X`` at cut ``|X|+|A|``.  It then asks whether those
equalities alone force one of:

* ``first(X) = first(A)``;
* a square suffix of ``X``;
* a square suffix of ``A X``.

This is an arithmetic pattern finder for a symbolic proof.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, value: int) -> int:
        while self.parent[value] != value:
            self.parent[value] = self.parent[self.parent[value]]
            value = self.parent[value]
        return value

    def union(self, left: int, right: int) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root != right_root:
            self.parent[right_root] = left_root

    def equal(self, left: int, right: int) -> bool:
        return self.find(left) == self.find(right)


def forced_square(
    union_find: UnionFind, positions: tuple[int, ...]
) -> tuple[int, ...]:
    roots: list[int] = []
    length = len(positions)
    for root in range(1, length // 2 + 1):
        if all(
            union_find.equal(
                positions[length - 2 * root + offset],
                positions[length - root + offset],
            )
            for offset in range(root)
        ):
            roots.append(root)
    return tuple(roots)


def classify(x_length: int, a_length: int, cube_root: int):
    a_positions = tuple(range(x_length - a_length, x_length))
    q_positions = (
        tuple(range(x_length))
        + a_positions
        + tuple(range(x_length))
        + a_positions
        + tuple(range(x_length))
    )
    n = len(q_positions)
    cut = x_length + a_length
    union_find = UnionFind(x_length)
    for block in (2, 3):
        for offset in range(cube_root):
            union_find.union(
                q_positions[(cut - block * cube_root + offset) % n],
                q_positions[(cut - cube_root + offset) % n],
            )
    mismatch = union_find.equal(0, x_length - a_length)
    x_squares = forced_square(union_find, tuple(range(x_length)))
    z_squares = forced_square(
        union_find, a_positions + tuple(range(x_length))
    )
    return mismatch, x_squares, z_squares


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-x", type=int, default=100)
    parser.add_argument("--show", type=int, default=30)
    parser.add_argument(
        "--fitting",
        action="store_true",
        help=(
            "restrict to roots satisfying the positive-phase fitting bound "
            "3r <= |Q| + (|X|+|A|) - 1"
        ),
    )
    args = parser.parse_args()

    counter: Counter[str] = Counter()
    examples: defaultdict[str, list[tuple[object, ...]]] = defaultdict(list)
    uncovered: list[tuple[int, int, int]] = []
    for x_length in range(2, args.max_x + 1):
        for a_length in range(1, x_length):
            n = 3 * x_length + 2 * a_length
            for cube_root in range(1, n):
                if (
                    args.fitting
                    and 3 * cube_root
                    > n + x_length + a_length - 1
                ):
                    continue
                mismatch, x_squares, z_squares = classify(
                    x_length, a_length, cube_root
                )
                kinds = (
                    ("mismatch" if mismatch else "")
                    + ("X" if x_squares else "")
                    + ("Z" if z_squares else "")
                )
                if not kinds:
                    uncovered.append((x_length, a_length, cube_root))
                    continue
                counter[kinds] += 1
                if len(examples[kinds]) < args.show:
                    examples[kinds].append(
                        (
                            x_length,
                            a_length,
                            cube_root,
                            x_squares,
                            z_squares,
                        )
                    )
        print(f"classified through |X|={x_length}")

    print(f"classes={dict(counter)}")
    for kind, records in sorted(examples.items()):
        print(kind, records)
    print(f"uncovered_count={len(uncovered)}")
    print(f"uncovered_examples={uncovered[:args.show]}")


if __name__ == "__main__":
    main()
