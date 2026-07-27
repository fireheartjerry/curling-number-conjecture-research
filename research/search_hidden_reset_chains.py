"""Search the exact word-equation shadow of hidden reset towers.

The search does not assert orbit compatibility.  It enumerates primitive
binary roots U for exact square resets cn(U^2)=2,
cn((U^2)[1:])=1, and follows every hidden next-root equation

    V = U U[:h],  h a proper period of U,  h>|U|/2,
    U[|U|-h] = 2.

Every curling number is recomputed by both reference implementations.
"""

from __future__ import annotations

import argparse
import itertools

from curling import curling_number, curling_number_reference


def cn(word: tuple[int, ...]) -> int:
    a = curling_number(word)
    b = curling_number_reference(word)
    assert a == b
    return a


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return not any(
        n % d == 0 and word == word[:d] * (n // d)
        for d in range(1, n)
    )


def periods(word: tuple[int, ...]) -> tuple[int, ...]:
    n = len(word)
    return tuple(
        h
        for h in range(n // 2 + 1, n)
        if all(word[i] == word[i - h] for i in range(h, n))
    )


def robust_square_root(word: tuple[int, ...]) -> bool:
    return (
        primitive(word)
        and cn(word * 2) == 2
        and cn((word * 2)[1:]) == 1
    )


def children(word: tuple[int, ...]) -> tuple[tuple[int, tuple[int, ...]], ...]:
    n = len(word)
    result = []
    for h in periods(word):
        if word[n - h] != 2:
            continue
        child = word + word[:h]
        if robust_square_root(child):
            result.append((h, child))
    return tuple(result)


def render(word: tuple[int, ...]) -> str:
    return "".join(map(str, word))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-start", type=int, default=16)
    parser.add_argument("--max-root", type=int, default=600)
    args = parser.parse_args()

    best: list[tuple[int, tuple[int, ...], tuple[int, ...]]] = []
    total = 0
    for n in range(1, args.max_start + 1):
        for word in itertools.product((2, 3), repeat=n):
            if not robust_square_root(word):
                continue
            total += 1
            stack = [(word, (), (n,))]
            while stack:
                current, hs, lengths = stack.pop()
                nxt = children(current) if len(current) < args.max_root else ()
                if not nxt:
                    best.append((len(hs), word, hs))
                for h, child in nxt:
                    if len(child) <= args.max_root:
                        stack.append((child, hs + (h,), lengths + (len(child),)))

    best.sort(reverse=True, key=lambda item: item[0])
    print("convention: exact square reset has cn(U^2)=2 and deleted cn=1")
    print(f"robust_starts={total}")
    print("longest_hidden_k2_chains")
    for depth, start, hs in best[:30]:
        lengths = [len(start)]
        p = len(start)
        for h in hs:
            p += h
            lengths.append(p)
        print(
            f"depth={depth} start={render(start)} "
            f"lengths={tuple(lengths)} periods={hs}"
        )


if __name__ == "__main__":
    main()
