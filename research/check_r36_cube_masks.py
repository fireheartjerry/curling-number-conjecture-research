"""Exact overlap audit for cube masks forced across the R36 square origin.

The stage-3 Q64 repair produces an R15 cube.  Repairing the full profile
of R15 in its shortest arbitrary context produces the primitive square
root

    R36 = 232322232223232223222323222323222332.

The displayed square ``R36^2`` occupies coordinates ``[0,72)``.  The
proper circular profile of R36 has cube holes at phases 1, 3, 13, and
23.  At the corresponding cuts in the second copy, any root shorter than
36 which did not cross coordinate zero would already be a proper circular
cube of R36.  Under the Q64 branch's globally maximal cube bound 21, the
only possible root ranges are therefore finite.

This script exhausts all root tuples in those ranges and checks the raw
word equations.  It does not use a hand-evaluated curling number.
"""

from __future__ import annotations

from itertools import product

from check_run_length_grammar import primitive, proper_profile


R36 = tuple(map(int, "232322232223232223222323222323222332"))
CUBE_HOLES = (1, 3, 13, 23)
CUBE_MAX = 21


class UnionFind:
    def __init__(self):
        self.parent: dict[int, int] = {}
        self.fixed: dict[int, int] = {}

    def find(self, item: int) -> int:
        self.parent.setdefault(item, item)
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def set_value(self, item: int, value: int) -> bool:
        root = self.find(item)
        old = self.fixed.get(root)
        if old is not None and old != value:
            return False
        self.fixed[root] = value
        return True

    def union(self, left: int, right: int) -> bool:
        a = self.find(left)
        b = self.find(right)
        if a == b:
            return True
        va = self.fixed.get(a)
        vb = self.fixed.get(b)
        self.parent[b] = a
        if va is not None and vb is not None and va != vb:
            return False
        if va is None and vb is not None:
            self.fixed[a] = vb
        elif va is not None:
            self.fixed[a] = va
        self.fixed.pop(b, None)
        return True


def compatible(roots: tuple[int, ...]) -> bool:
    uf = UnionFind()
    for position, value in enumerate(R36 * 2):
        if not uf.set_value(position, value):
            return False
    for phase, root in zip(CUBE_HOLES, roots):
        cut = len(R36) + phase
        origin = cut - 3 * root
        for offset in range(root):
            if not uf.union(origin + offset, origin + root + offset):
                return False
            if not uf.union(origin + offset, origin + 2 * root + offset):
                return False
    return True


def main() -> None:
    profile = proper_profile(R36)
    holes = tuple(
        phase
        for phase, value in enumerate(R36)
        if value == 3 and profile[phase] < 3
    )
    assert primitive(R36)
    assert holes == CUBE_HOLES
    ranges = tuple(
        tuple(
            range(
                (len(R36) + phase) // 3 + 1,
                CUBE_MAX + 1,
            )
        )
        for phase in CUBE_HOLES
    )
    assignments = tuple(product(*ranges))
    survivors = tuple(roots for roots in assignments if compatible(roots))
    print(
        {
            "R36_length": len(R36),
            "proper_profile": "".join(map(str, profile)),
            "cube_holes": CUBE_HOLES,
            "root_ranges": ranges,
            "assignments": len(assignments),
            "compatible_root_tuples": survivors,
        }
    )


if __name__ == "__main__":
    main()
