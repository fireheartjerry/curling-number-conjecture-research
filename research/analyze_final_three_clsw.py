"""Enumerate the exact final-3 CLSW normal form.

The symbolic reduction gives

    Q = X A X A X,
    Z = A X,
    A a nonempty proper suffix of X,
    X[0] = 3, A[0] = 2,
    cn(Q) = 2, cn(Z) = cn(X) = 1.

This diagnostic splits by ``cn(XAX)`` and records failures of the proper
circular cube-indicator profile.  It supplies examples for proof search;
it is not a proof of the unbounded statement.
"""

from __future__ import annotations

import argparse
import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference


Word = tuple[int, ...]


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def cube_roots(word: Word, cut: int) -> tuple[int, ...]:
    n = len(word)
    return tuple(
        root
        for root in range(1, n)
        if all(
            word[(cut - block * root + offset) % n]
            == word[(cut - root + offset) % n]
            for block in (2, 3)
            for offset in range(root)
        )
    )


def theorem_13_decompositions(a: Word, x: Word) -> tuple[tuple[Word, Word], ...]:
    """Return every literal ``a+x = s+r+s`` decomposition from Theorem 13."""

    z = a + x
    records: list[tuple[Word, Word]] = []
    for s_length in range(1, (len(z) + 1) // 2):
        r_length = len(z) - 2 * s_length
        if not 0 < r_length < s_length:
            continue
        s = z[:s_length]
        r = z[s_length : s_length + r_length]
        if z != s + r + s:
            continue
        if len(r) > len(x) or x[-len(r) :] != r:
            continue
        if s[-len(r) :] != r:
            continue
        if exact_cn(s) != 1:
            continue
        records.append((s, r))
    return tuple(records)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-x", type=int, default=15)
    parser.add_argument("--examples", type=int, default=3)
    args = parser.parse_args()

    for x_length in range(2, args.max_x + 1):
        counts: dict[int, int] = {}
        first_types: dict[tuple[int, str], int] = {}
        theorem_types: dict[tuple[int, str, bool], int] = {}
        examples: dict[int, list[object]] = {}
        for x in itertools.product((2, 3), repeat=x_length):
            if x[0] != 3 or exact_cn(x) != 1:
                continue
            for a_length in range(1, x_length):
                a = x[-a_length:]
                if a[0] != 2:
                    continue
                z = a + x
                q = x + a + x + a + x
                if exact_cn(z) != 1 or exact_cn(q) != 2:
                    continue
                w = x + a + x
                branch = exact_cn(w)
                assert branch in (1, 2)
                decompositions = theorem_13_decompositions(a, x)
                if branch == 2:
                    assert decompositions
                roots = tuple(cube_roots(q, cut) for cut in range(len(q)))
                decomposition_kind = (
                    "none"
                    if not decompositions
                    else "+".join(
                        sorted(
                            {
                                "equal" if len(s) == len(a) else "gap"
                                for s, _ in decompositions
                            }
                        )
                    )
                )
                theorem_key = (
                    branch,
                    decomposition_kind,
                    bool(roots[len(x) + len(a)]),
                )
                theorem_types[theorem_key] = theorem_types.get(theorem_key, 0) + 1
                mismatches = tuple(
                    cut
                    for cut in range(len(q))
                    if (q[cut] == 3) != bool(roots[cut])
                )
                assert mismatches
                counts[branch] = counts.get(branch, 0) + 1

                def kind(cut: int) -> str:
                    boundaries = {
                        0: "origin",
                        x_length: "X|A1",
                        x_length + a_length: "A1|X2",
                        2 * x_length + a_length: "X2|A2",
                        2 * (x_length + a_length): "A2|X3",
                        len(q) - 1: "last",
                    }
                    if cut in boundaries:
                        return boundaries[cut]
                    if cut < x_length:
                        return "X1"
                    if cut < x_length + a_length:
                        return "A1"
                    if cut < 2 * x_length + a_length:
                        return "X2"
                    if cut < 2 * (x_length + a_length):
                        return "A2"
                    return "X3"

                key = (branch, kind(mismatches[0]))
                first_types[key] = first_types.get(key, 0) + 1
                branch_examples = examples.setdefault(branch, [])
                if len(branch_examples) < args.examples:
                    branch_examples.append(
                        (
                            "".join(map(str, x)),
                            "".join(map(str, a)),
                            "".join(map(str, q)),
                            tuple(
                                (
                                    "".join(map(str, s)),
                                    "".join(map(str, r)),
                                    "equal" if len(s) == len(a) else "gap",
                                )
                                for s, r in decompositions
                            ),
                            tuple((cut, kind(cut), roots[cut]) for cut in mismatches),
                        )
                    )
        if counts:
            print(
                f"|X|={x_length} branch_counts={counts} "
                f"first_mismatch_types={first_types} theorem_types={theorem_types}"
            )
            for branch, records in sorted(examples.items()):
                for record in records:
                    print(f"  branch={branch} {record!r}")


if __name__ == "__main__":
    main()
