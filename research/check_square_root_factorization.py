"""Audit minimal-square factorizations of rotations of a periodic word.

For each phase, greedily take the shortest square beginning at the current
phase.  Report whether the resulting consecutive squares close after one
period in square-root length, equivalently after two periods in source
length, and whether their root concatenation is the starting rotation.
"""

from __future__ import annotations


def shortest_square_root(word: tuple[int, ...], phase: int) -> int:
    n = len(word)
    for root in range(1, n):
        if all(word[(phase + j) % n] == word[(phase + root + j) % n]
               for j in range(root)):
            return root
    raise ValueError(f"no proper square at phase {phase}")


def audit(word: tuple[int, ...], phase: int) -> dict[str, object]:
    n = len(word)
    source_used = 0
    roots: list[tuple[int, ...]] = []
    lengths: list[int] = []
    current = phase
    seen: set[tuple[int, int]] = set()
    while source_used < 2 * n:
        state = (current, source_used)
        if state in seen:
            break
        seen.add(state)
        r = shortest_square_root(word, current)
        if source_used + 2 * r > 2 * n:
            break
        root_word = tuple(word[(current + j) % n] for j in range(r))
        roots.append(root_word)
        lengths.append(r)
        current = (current + 2 * r) % n
        source_used += 2 * r
    square_root = tuple(x for root in roots for x in root)
    rotation = tuple(word[(phase + j) % n] for j in range(n))
    return {
        "phase": phase,
        "lengths": tuple(lengths),
        "source_used": source_used,
        "root_length": len(square_root),
        "root_equals_rotation": square_root == rotation,
        "root": square_root,
        "rotation": rotation,
    }


if __name__ == "__main__":
    q = tuple(map(int, "223222322232322232223"))
    for start in range(len(q)):
        result = audit(q, start)
        print(result)
