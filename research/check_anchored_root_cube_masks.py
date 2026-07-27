"""Audit cube-hole masks in the final copy of an anchored root power.

If a primitive word ``B`` occurs as ``B^e`` and phase ``j`` is a cube
hole of B's proper circular profile, a cube ending at phase ``j`` of the
last copy cannot start inside the displayed power: that would already be
a proper circular cube of B.  Hence its root ``q`` must satisfy

    3q > (e-1)|B| + j.

For the Q64 branch a globally maximal cube has root 21, so ``q<=21``.
This script exhausts the resulting finite root tuples and checks their
raw overlap equations against the fixed ``B^e`` factor.
"""

from __future__ import annotations

from itertools import product

from check_run_length_grammar import primitive, proper_profile


CUBE_MAX = 21
CASES = (
    ("Q64_stage3_b15", "223232223322232", 3),
    ("Q64_cube_anchor_b18", "232223232223322232", 3),
    ("Q64_cube_anchor_b19", "2332223232223322232", 3),
    ("Q64_cube_anchor_b20", "22232223232223322232", 3),
    ("Q64_cube_anchor_b21", "233222323222323322232", 3),
    ("R15_square_anchor_b36", "232322232223232223222323222323222332", 2),
)


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


def compatible(
    root_word: tuple[int, ...],
    copies: int,
    holes: tuple[int, ...],
    roots: tuple[int, ...],
) -> bool:
    uf = UnionFind()
    for position, value in enumerate(root_word * copies):
        if not uf.set_value(position, value):
            return False
    offset = (copies - 1) * len(root_word)
    for phase, root in zip(holes, roots):
        cut = offset + phase
        origin = cut - 3 * root
        for index in range(root):
            if not uf.union(origin + index, origin + root + index):
                return False
            if not uf.union(origin + index, origin + 2 * root + index):
                return False
    return True


def audit(name: str, text: str, copies: int):
    root_word = tuple(map(int, text))
    profile = proper_profile(root_word)
    holes = tuple(
        phase
        for phase, value in enumerate(root_word)
        if value == 3 and profile[phase] < 3
    )
    negative_failures = tuple(
        (phase, root_word[phase], profile[phase])
        for phase in range(len(root_word))
        if profile[phase] > root_word[phase]
    )
    assert primitive(root_word)
    ranges = tuple(
        tuple(
            range(
                ((copies - 1) * len(root_word) + phase) // 3 + 1,
                CUBE_MAX + 1,
            )
        )
        for phase in holes
    )
    assignments = tuple(product(*ranges)) if all(ranges) else ()
    survivors = tuple(
        roots
        for roots in assignments
        if compatible(root_word, copies, holes, roots)
    )
    return {
        "name": name,
        "length": len(root_word),
        "copies": copies,
        "proper_profile": "".join(map(str, profile)),
        "cube_holes": holes,
        "negative_failures": negative_failures,
        "root_ranges": ranges,
        "assignments": len(assignments),
        "compatible_root_tuples": survivors,
    }


def main() -> None:
    for case in CASES:
        print(audit(*case))


if __name__ == "__main__":
    main()
