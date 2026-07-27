"""Equality-graph diagnostics for a fitting long cube at an AVA mismatch.

No curling-number value is inferred by this script.  It asks which square
suffixes are forced purely by the AVA equations, first-prefix agreement,
and one selected circular cube.
"""

from __future__ import annotations

import argparse


class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x != y:
            self.p[y] = x


def graph(a: int, v: int, j: int, d: int):
    n = 2 * a + v
    e = a + j
    r = a + d
    uf = DSU(n)
    # Q=A V A and V=suffix_v(A).
    for i in range(a):
        uf.union(i, a + v + i)
    for i in range(v):
        uf.union(a + i, a - v + i)
    # First mismatch agreement.
    for i in range(j):
        uf.union(i, a + i)
    # Selected circular cube at E.
    for block in (2, 3):
        for offset in range(r):
            uf.union((e - block * r + offset) % n, (e - r + offset) % n)
    return uf


def forced_suffix_squares(uf: DSU, n: int):
    return [
        s
        for s in range(1, n // 2 + 1)
        if all(uf.find(n - 2 * s + i) == uf.find(n - s + i) for i in range(s))
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("maximum_a", type=int)
    args = parser.parse_args()
    misses = []
    for a in range(3, args.maximum_a + 1):
        for v in range(1, a):
            n = 2 * a + v
            for j in range(v):
                for d in range(1, v // 2 + 1):
                    r = a + d
                    # Strict FW branch, primitive-span bound, first-copy fit.
                    if not (d > j + 1 and 2 * r + 1 < n):
                        continue
                    if not (3 * r <= n + (a + j) - 1):
                        continue
                    uf = graph(a, v, j, d)
                    # A[j] and V[j] must remain distinguishable.
                    if uf.find(j) == uf.find(a + j):
                        continue
                    roots = forced_suffix_squares(uf, n)
                    if not roots:
                        misses.append((a, v, j, d))
                    else:
                        print(
                            f"a={a} v={v} j={j} d={d} "
                            f"m={v-2*d} forced={roots}"
                        )
    print(f"misses={len(misses)}")
    if misses:
        print("first_misses=" + repr(misses[:50]))


if __name__ == "__main__":
    main()
