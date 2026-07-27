"""Executed regression for adjacent_root_stack.md."""

from pathlib import Path
import math
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference


def maximizing_roots(word):
    k = curling_number(word)
    roots = []
    for p in range(1, len(word) // k + 1):
        if word[-k * p :] == word[-p:] * k:
            roots.append(p)
    return k, tuple(roots)


def maximal_run_left(word, p):
    left = len(word) - p
    while left > 0 and word[left - 1] == word[left - 1 + p]:
        left -= 1
    return left


def main():
    word = tuple(map(int, "22322232"))
    rows = []
    for _ in range(58):
        k, roots = maximizing_roots(word)
        assert k == curling_number_reference(word)
        if k == 1:
            break
        p = min(roots)
        rows.append((len(word), k, p, maximal_run_left(word, p)))
        next_word = word + (k,)
        ell, next_roots = maximizing_roots(next_word)
        assert ell == curling_number_reference(next_word)
        if ell >= 2:
            q = min(next_roots)
            if q == p:
                assert ell in (k, k + 1)
            elif q > p:
                assert (ell * q - 1) >= k * p
                assert q > (k - 1) * p + math.gcd(p, q)
            else:
                assert (ell * q - 1) < k * p
                assert p >= (ell - 1) * q + math.gcd(p, q)
        word = next_word

    selected = {cut: (k, p, left) for cut, k, p, left in rows}
    assert selected[8] == (2, 4, 0)
    assert selected[12] == (3, 4, 0)
    assert selected[17] == (2, 6, 5)
    assert selected[18] == (2, 6, 5)
    assert 0 < 5 < 12 < 18
    print("all adjacent root transitions passed")
    print("maximal runs cross: period 4 [0,12), period 6 [5,18)")


if __name__ == "__main__":
    main()
