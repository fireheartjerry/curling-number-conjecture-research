"""Finite audits for ``internal_k3_hidden_audit.md``.

The proof in the note is symbolic.  This program only:

* checks the forced five-block cube over a range of block lengths;
* exhausts period blocks over {2,3,4} through length ten;
* audits every internal child of every rotation of the binary Q21 word.

Run the repository's A094004 unit calibration before relying on this output:

    python -m unittest \
      tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration
"""

from __future__ import annotations

import itertools
from math import gcd


Word = tuple[int, ...]


def power(word: Word, cut: int, root: int, exponent: int) -> bool:
    n = len(word)
    return all(
        word[(cut - block * root + offset) % n]
        == word[(cut - root + offset) % n]
        for block in range(2, exponent + 1)
        for offset in range(root)
    )


def primitive(word: Word) -> bool:
    n = len(word)
    return not any(
        n % period == 0
        and word == word[:period] * (n // period)
        for period in range(1, n)
    )


def fixed(word: Word) -> bool:
    """Test ``pc_word=cut label`` when labels lie in {2,3,4}."""
    if not primitive(word):
        return False
    n = len(word)
    for cut, label in enumerate(word):
        assert 2 <= label <= 4
        if not any(power(word, cut, root, label) for root in range(1, n)):
            return False
        if any(power(word, cut, root, label + 1) for root in range(1, n)):
            return False
    return True


def periods(word: Word) -> tuple[int, ...]:
    return tuple(
        shift
        for shift in range(1, len(word))
        if word[shift:] == word[:-shift]
    )


def check_five_block_cube() -> int:
    checked = 0
    for a in range(1, 21):
        for b in range(1, 21):
            # Pairwise distinct formal symbols ensure that the assertion is
            # a word identity, rather than an accidental binary equality.
            block_a = tuple(("A", index) for index in range(a))
            block_b = tuple(("B", index) for index in range(b))
            c = block_a + block_b
            u = c * 2 + block_a
            v = u * 2 + c
            h = len(c)
            assert power(v, 2 * h, h, 3)
            assert v[2 * h] == block_a[0]
            checked += 1
    return checked


def exhaust_small_period_blocks() -> tuple[int, int, tuple[str, ...]]:
    checked = 0
    fixed_roots: list[str] = []
    fixed_pairs = 0
    for h in range(2, 11):
        for c in itertools.product((2, 3, 4), repeat=h):
            if c[0] != 2:
                continue
            for quotient in (1, 2):
                for remainder in range(1, h):
                    u = c * quotient + c[:remainder]
                    p = len(u)
                    defect = p - h
                    if u[defect] != 3:
                        continue
                    checked += 1
                    if not fixed(u):
                        continue
                    fixed_roots.append("".join(map(str, u)))
                    v = u * 2 + c
                    if fixed(v):
                        fixed_pairs += 1
    return checked, fixed_pairs, tuple(sorted(set(fixed_roots)))


def audit_q21_rotations() -> tuple[int, int]:
    q21 = tuple(map(int, "223222322232322232223"))
    candidates = 0
    fixed_children = 0
    for shift in range(len(q21)):
        u = q21[shift:] + q21[:shift]
        p = len(u)
        assert fixed(u)
        for h in periods(u):
            if 3 * h <= p or u[p - h] != 3:
                continue
            candidates += 1
            v = u * 2 + u[:h]
            if fixed(v):
                fixed_children += 1
    return candidates, fixed_children


def audit_root_scale_dichotomy() -> int:
    checked = 0
    for p in range(3, 17):
        for a in range(1, (p + 1) // 2):
            h = p - a
            for c in itertools.product((2, 3), repeat=h):
                if c[0] != 2:
                    continue
                u = c + c[:a]
                if u[a] != 3 or not primitive(u):
                    continue
                v = u * 2 + c
                if not primitive(v):
                    continue
                q = len(v)
                for d in range(1, h):
                    if (
                        d == a
                        or c[:d] != c[-d:]
                        or c[d] != 3
                    ):
                        continue
                    for root in range(1, q):
                        if not power(v, d, root, 3):
                            continue
                        checked += 1
                        common = gcd(p, root)
                        if d < a:
                            assert root == p or 2 * root + common < p
                        else:
                            assert root < p
                            assert 2 * root + common < p + d - a
    return checked


def main() -> None:
    identities = check_five_block_cube()
    checked, pairs, roots = exhaust_small_period_blocks()
    q21_candidates, q21_children = audit_q21_rotations()
    scale_cases = audit_root_scale_dichotomy()
    assert identities == 400
    assert pairs == 0
    assert roots == ("232223222323222322232",)
    assert q21_candidates == 10
    assert q21_children == 0
    assert scale_cases == 5190
    print(
        "five_block_identities=400 "
        f"period_candidates={checked} "
        f"fixed_roots={len(roots)} fixed_pairs={pairs} "
        f"q21_candidates={q21_candidates} "
        f"q21_fixed_children={q21_children} "
        f"root_scale_cases={scale_cases}"
    )


if __name__ == "__main__":
    main()
