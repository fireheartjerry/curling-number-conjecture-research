"""Search local overlaps of two exact compressed g=2 gadgets.

This deliberately omits cyclic closure and global cube constraints.  Its
purpose is adversarial: determine which proposed predecessor ranks already
fail for a locally consistent binary word with no ``22``.
"""

from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Int, Or, Solver, sat  # type: ignore


def nonpower(block):
    n = len(block)
    clauses = []
    for d in range(1, n):
        if n % d == 0:
            clauses.append(Or(*(block[j] != block[j % d] for j in range(n))))
    return And(*clauses)


def solve_pair(h: int, r: int, k: int):
    """Parent starts 0; selected third-copy 11 ends at x=2h+r."""
    x = 2 * h + r
    y = x - 3 * k
    lo, hi = min(0, y), 3 * h
    z = {j: Int(f"z_{j}") for j in range(lo, hi + 1)}
    s = Solver()
    for value in z.values():
        s.add(1 <= value, value <= 2)
    for j in range(lo, hi):
        s.add(Or(z[j] != 2, z[j + 1] != 2))

    # Parent [1,C,2,C,2,C,1].
    s.add(z[0] == 1, z[h] == 2, z[2 * h] == 2, z[3 * h] == 1)
    for j in range(1, h):
        s.add(z[j] == z[h + j], z[j] == z[2 * h + j])
    s.add(nonpower([z[j] for j in range(1, h + 1)]))

    # r is the second position of the leftmost internal 11 in C.
    s.add(z[r - 1] == 1, z[r] == 1)
    for j in range(2, r):
        s.add(Or(z[j - 1] != 1, z[j] != 1))

    # Child [1,D,2,D,2,D,1].
    s.add(z[y] == 1, z[y + k] == 2, z[y + 2 * k] == 2, z[x] == 1)
    for j in range(1, k):
        s.add(z[y + j] == z[y + k + j])
        s.add(z[y + j] == z[y + 2 * k + j])
    s.add(nonpower([z[y + j] for j in range(1, k + 1)]))

    if s.check() != sat:
        return None
    model = s.model()
    word = "".join(str(model.eval(z[j]).as_long()) for j in range(lo, hi + 1))
    return lo, hi, word, y, x


def main(limit: int = 24) -> None:
    examples = {
        "contained": None,
        "middle": None,
        "left_crossing_smaller": None,
        "left_crossing_equal": None,
        "left_crossing_larger": None,
    }
    for h in range(3, limit + 1):
        for r in range(2, h):
            if r % 2:
                continue
            for k in range(2, limit + 1):
                answer = solve_pair(h, r, k)
                if answer is None:
                    continue
                y = answer[3]
                if y >= 2 * h + 1:
                    kind = "contained"
                elif y >= 1:
                    kind = "middle"
                elif k < h:
                    kind = "left_crossing_smaller"
                elif k == h:
                    kind = "left_crossing_equal"
                else:
                    kind = "left_crossing_larger"
                if examples[kind] is None:
                    examples[kind] = (h, r, k, answer)
    for kind, example in examples.items():
        print(kind, example)


if __name__ == "__main__":
    bound = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    main(bound)
