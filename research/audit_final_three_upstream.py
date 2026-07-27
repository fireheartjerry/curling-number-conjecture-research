"""Audit the hypotheses upstream of the final-3 middle-cut lemma.

The previous draft incorrectly inferred ``cn(A X)=1`` from
``cn(X A X A X)=2``.  This program removes that inference and enumerates
the literal canonical forms

    Q = X A X A X,  A a proper suffix of X,
    X[0] = 3, A[0] = 2,

subject to the exact proper circular {2,3}-profile and the inherited
positive-phase fitting inequalities.  Every finite curling number is
checked by both implementations.
"""

from __future__ import annotations

import argparse
import itertools
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference


Word = tuple[int, ...]


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def has_circular_power(word: Word, cut: int, exponent: int, root: int) -> bool:
    n = len(word)
    return all(
        word[(cut - block * root + offset) % n]
        == word[(cut - root + offset) % n]
        for block in range(2, exponent + 1)
        for offset in range(root)
    )


def roots(word: Word, cut: int, exponent: int) -> tuple[int, ...]:
    return tuple(
        root
        for root in range(1, len(word))
        if has_circular_power(word, cut, exponent, root)
    )


def primitive(word: Word) -> bool:
    n = len(word)
    return not any(
        n % root == 0 and word == word[:root] * (n // root)
        for root in range(1, n)
    )


def exact_profile_and_fitting(word: Word) -> bool:
    n = len(word)
    for cut, label in enumerate(word):
        target_roots = roots(word, cut, label)
        if not target_roots:
            return False
        if roots(word, cut, label + 1):
            return False
        if cut > 0 and not any(
            label * root <= n + cut - 2 for root in target_roots
        ):
            return False
    return True


def calibrate_countermodels() -> None:
    records = (
        ("cn-one inference", (3, 2, 2), (2,)),
        ("border-length inference", (3, 2), (2, 3, 2)),
    )
    for label, x, a in records:
        z = a + x
        q = x + z + z
        assert z[-len(a) :] == a
        assert a + q == z * 3
        values = {
            "cn(X)": exact_cn(x),
            "cn(Z)": exact_cn(z),
            "cn(Q)": exact_cn(q),
            "cn(Q[1:])": exact_cn(q[1:]),
        }
        print(
            f"{label}: "
            f"X={''.join(map(str, x))} "
            f"A={''.join(map(str, a))} "
            f"Z={''.join(map(str, z))} "
            f"Q={''.join(map(str, q))} "
            f"values={values}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-x", type=int, default=15)
    parser.add_argument("--examples", type=int, default=10)
    args = parser.parse_args()

    calibrate_countermodels()

    counts: Counter[tuple[int, int]] = Counter()
    examples: dict[tuple[int, int], list[tuple[object, ...]]] = {}
    total = 0
    for x_length in range(2, args.max_x + 1):
        for x in itertools.product((2, 3), repeat=x_length):
            if x[0] != 3:
                continue
            for a_length in range(1, x_length):
                a = x[-a_length:]
                if a[0] != 2:
                    continue
                z = a + x
                q = x + a + x + a + x
                if not primitive(q):
                    continue
                if exact_cn(q) != 2:
                    continue
                if not exact_profile_and_fitting(q):
                    continue
                total += 1
                key = (exact_cn(x), exact_cn(z))
                counts[key] += 1
                bucket = examples.setdefault(key, [])
                if len(bucket) < args.examples:
                    middle = x_length + a_length
                    bucket.append(
                        (
                            "".join(map(str, x)),
                            "".join(map(str, a)),
                            "".join(map(str, q)),
                            roots(q, middle, 3),
                        )
                    )
        print(f"audited through |X|={x_length}")

    print(f"total={total}")
    print(f"(cn(X),cn(AX)) counts={dict(counts)}")
    for key, records in sorted(examples.items()):
        for record in records:
            print(f"{key}: {record}")


if __name__ == "__main__":
    main()
