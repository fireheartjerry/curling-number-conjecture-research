"""Probe uniformly recurrent binary words for cuts with no square suffix.

Finite evidence only.  A cut is L-squareless when no square of root at most
L ends there inside the generated window.
"""

from __future__ import annotations


def morphic(seed: str, morphism: dict[str, str], rounds: int) -> str:
    word = seed
    for _ in range(rounds):
        word = "".join(morphism[c] for c in word)
    return word


def least_square_root(word: str, cut: int, cap: int) -> int | None:
    for root in range(1, min(cap, cut // 2) + 1):
        if word[cut - 2 * root : cut - root] == word[cut - root : cut]:
            return root
    return None


def report(name: str, word: str, cap: int) -> None:
    margin = 2 * cap
    holes = [
        cut
        for cut in range(margin, len(word) - margin)
        if least_square_root(word, cut, cap) is None
    ]
    by_next = {c: sum(word[cut] == c for cut in holes) for c in "01"}
    print(name, len(word), cap, len(holes), by_next, holes[:10])


def main() -> None:
    tm = morphic("0", {"0": "01", "1": "10"}, 18)
    fib = morphic("0", {"0": "01", "1": "0"}, 27)
    period_doubling = morphic("0", {"0": "01", "1": "00"}, 18)
    for cap in (32, 128, 512, 2048):
        report("thue-morse", tm, cap)
        report("fibonacci", fib, cap)
        report("period-doubling", period_doubling, cap)


if __name__ == "__main__":
    main()
