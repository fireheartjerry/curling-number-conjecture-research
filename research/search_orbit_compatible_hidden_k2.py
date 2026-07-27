"""Search for genuinely orbit-compatible hidden transitions after a k=2 reset.

This is an exhaustive finite diagnostic, not a proof.  A starting root U is
required to give the strict reset

    cn(U^2) = 2,        cn((U^2)[1:]) = 1.

If the next reset root V is hidden inside U^2 and has length p+h, the overlap
equations force h to be a period of U, h>p/2, and U[p-h]=2.  The counterorbit
alphabet is binary here, so the next reset exponent can only be 2 or 3.  For
each resulting target V^ell, this program asks whether every symbol between
U^2 and V^ell is exactly the curling number produced by the current prefix.

Every curling number used in a recorded candidate is recomputed with the two
independent implementations in curling.py.
"""

from __future__ import annotations

import argparse
import itertools
from collections import Counter

from curling import curling_number, curling_number_reference


Word = tuple[int, ...]


def cn(word: Word) -> int:
    first = curling_number(word)
    second = curling_number_reference(word)
    assert first == second, (word, first, second)
    return first


def primitive(word: Word) -> bool:
    n = len(word)
    return not any(
        n % d == 0 and word == word[:d] * (n // d)
        for d in range(1, n)
    )


def periods(word: Word) -> tuple[int, ...]:
    n = len(word)
    return tuple(
        h
        for h in range(n // 2 + 1, n)
        if word[h:] == word[: n - h]
    )


def render(word: Word) -> str:
    return "".join(map(str, word))


def compatible_prefix_length(start: Word, target: Word) -> tuple[int, int, int]:
    """Return matched appended symbols, first actual value, first target value.

    If the whole target is generated, the two final values are -1, -1.
    """
    assert target[: len(start)] == start
    state = start
    matched = 0
    while len(state) < len(target):
        value = cn(state)
        expected = target[len(state)]
        if value != expected:
            return matched, value, expected
        state += (value,)
        matched += 1
    return matched, -1, -1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-root", type=int, default=16)
    args = parser.parse_args()

    robust_roots = 0
    overlap_candidates = 0
    strict_targets = 0
    compatible: list[tuple[Word, int, Word, int]] = []
    mismatch_histogram: Counter[tuple[int, int, int, int]] = Counter()
    longest_mismatches: list[
        tuple[int, Word, int, Word, int, int, int]
    ] = []

    for p in range(1, args.max_root + 1):
        for root in itertools.product((2, 3), repeat=p):
            if not primitive(root):
                continue
            start = root * 2
            if cn(start) != 2 or cn(start[1:]) != 1:
                continue
            robust_roots += 1

            for h in periods(root):
                if root[p - h] != 2:
                    continue
                next_root = root + root[:h]
                assert next_root[:p] == root
                assert (next_root * 2)[: 2 * p] == start
                if not primitive(next_root):
                    continue
                overlap_candidates += 1

                for exponent in (2, 3):
                    target = next_root * exponent
                    if cn(target) != exponent:
                        continue
                    if cn(target[1:]) != exponent - 1:
                        continue
                    strict_targets += 1
                    matched, actual, expected = compatible_prefix_length(
                        start, target
                    )
                    if actual == -1:
                        compatible.append((root, h, next_root, exponent))
                    else:
                        mismatch_histogram[(exponent, matched, actual, expected)] += 1
                        longest_mismatches.append(
                            (
                                matched,
                                root,
                                h,
                                next_root,
                                exponent,
                                actual,
                                expected,
                            )
                        )

    print("convention: a transition is compatible only if the orbit from U^2")
    print("produces every intervening target symbol before V^ell")
    print(f"enumerated_binary_root_lengths=1..{args.max_root}")
    print(f"robust_k2_roots={robust_roots}")
    print(f"hidden_overlap_candidates={overlap_candidates}")
    print(f"strict_next_reset_targets={strict_targets}")
    print(f"fully_orbit_compatible={len(compatible)}")
    for root, h, next_root, exponent in compatible[:30]:
        print(
            "compatible "
            f"U={render(root)} p={len(root)} h={h} "
            f"V={render(next_root)} q={len(next_root)} ell={exponent}"
        )
    print("most_common_first_mismatches=(ell,matched,actual,expected):count")
    for key, count in mismatch_histogram.most_common(20):
        print(f"{key}:{count}")
    print("longest_compatible_proper_prefixes")
    for matched, root, h, next_root, exponent, actual, expected in sorted(
        longest_mismatches, reverse=True, key=lambda item: item[0]
    )[:30]:
        print(
            f"matched={matched} U={render(root)} p={len(root)} h={h} "
            f"q={len(next_root)} ell={exponent} "
            f"first_mismatch={actual}!={expected}"
        )


if __name__ == "__main__":
    main()
