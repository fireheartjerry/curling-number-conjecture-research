"""Audit adjacent profile roots along midpoint edges of the Q21 fixed word.

All circular power values are enumerated over every proper root length.
"""

from __future__ import annotations


Q = tuple(map(int, "223222322232322232223"))


def circular_exponent(cut: int, root: int) -> int:
    n = len(Q)
    block = tuple(Q[(cut - root + j) % n] for j in range(root))
    copies = 1
    while copies <= n:
        prior = tuple(
            Q[(cut - (copies + 1) * root + j) % n] for j in range(root)
        )
        if prior != block:
            return copies
        copies += 1
    raise AssertionError("improper circular root")


def roots(cut: int, exponent: int) -> tuple[int, ...]:
    return tuple(
        r for r in range(1, len(Q)) if circular_exponent(cut, r) == exponent
    )


def profile(cut: int) -> int:
    return max(circular_exponent(cut, r) for r in range(1, len(Q)))


def main() -> None:
    assert tuple(profile(c) for c in range(len(Q))) == Q
    mu = tuple(min(r for r in range(1, len(Q)) if circular_exponent(c, r) >= 2)
               for c in range(len(Q)))
    for c, p in enumerate(mu):
        d = (c - p) % len(Q)
        a = Q[(c - 1) % len(Q)]
        assert a == Q[(d - 1) % len(Q)]
        left = roots((c - 1) % len(Q), a)
        right = roots((d - 1) % len(Q), a)
        print(
            f"c={c:2} d={d:2} p={p:2} color={a} "
            f"roots@c-1={left} roots@d-1={right}"
        )


if __name__ == "__main__":
    main()
