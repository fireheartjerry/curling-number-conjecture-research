"""Exact checks for two consecutive 3-labelled circular cuts.

The setting is a primitive binary circular word Q with proper circular
profile F.  We normalize a double 3-run as

    Q[0:3] = 3,3,2

and study primitive cube roots ending at cuts 0 and 1.
"""

from __future__ import annotations

from itertools import product
from math import gcd

from check_run_length_grammar import (
    binary_word,
    primitive,
    proper_profile,
    word_power_root_lengths,
)


Q7 = tuple(map(int, "3323232"))
Q12 = tuple(map(int, "332323323232"))
Q34 = tuple(map(int, "3322232233222332223223322232233222"))


def normalized_candidates(n: int):
    for tail in product((2, 3), repeat=n - 3):
        q = (3, 3, 2) + tail
        if primitive(q):
            yield q


def local_double_ok(q: tuple[int, ...]) -> bool:
    f = proper_profile(q)
    return max(f) <= 3 and f[:3] == (3, 3, 2)


def admissible_double_ok(q: tuple[int, ...]) -> bool:
    f = proper_profile(q)
    return all(x in (2, 3) for x in f) and f[:3] == (3, 3, 2)


def primitive_cube_roots(q: tuple[int, ...], cut: int) -> tuple[int, ...]:
    """Cube roots are primitive whenever no fourth power ends here."""
    assert not word_power_root_lengths(q, cut, 4)
    return word_power_root_lengths(q, cut, 3)


def audit_scale_separation(max_n: int) -> int:
    """Exhaustively audit the two-root Fine--Wilf alternatives."""
    checked_pairs = 0
    for n in range(3, max_n + 1):
        for q in normalized_candidates(n):
            f = proper_profile(q)
            if max(f) > 3 or f[:2] != (3, 3):
                continue
            left = primitive_cube_roots(q, 0)
            right = primitive_cube_roots(q, 1)
            for p in left:
                for r in right:
                    checked_pairs += 1
                    if p == r:
                        # The adjacent p-cubes merge into a period-p
                        # interval of length at least 3p+1.
                        segment = tuple(
                            q[(-3 * p + j) % n]
                            for j in range(3 * p + 1)
                        )
                        assert all(
                            segment[j] == segment[j - p]
                            for j in range(p, len(segment))
                        )
                    elif r > p:
                        assert r > 2 * p + gcd(p, r)
                    else:
                        assert p >= 2 * r + gcd(p, r)
    return checked_pairs


def main() -> None:
    f7 = proper_profile(Q7)
    assert primitive(Q7)
    assert f7 == tuple(map(int, "3321222"))
    assert word_power_root_lengths(Q7, 0, 3) == (2,)
    assert word_power_root_lengths(Q7, 1, 3) == (2,)
    assert word_power_root_lengths(Q7, 2, 3) == ()
    assert word_power_root_lengths(Q7, 2, 2) == (1,)
    # U=32 transports across the intervening appended 3:
    # U^3 3 = 3 (23)^3.
    u = (3, 2)
    assert u * 3 + (3,) == (3,) + (2, 3) * 3

    # Q7 is the smallest primitive local countermodel.
    assert all(
        not any(local_double_ok(q) for q in normalized_candidates(n))
        for n in range(3, 7)
    )

    f12 = proper_profile(Q12)
    assert primitive(Q12)
    assert f12 == tuple(map(int, "332222222223"))
    assert all(x in (2, 3) for x in f12)
    # It is the smallest countermodel that is squareful at every cut.
    assert all(
        not any(
            admissible_double_ok(q) for q in normalized_candidates(n)
        )
        for n in range(3, 12)
    )

    # Global squarefulness and exclusion of fourth powers do not force
    # the adjacent cube-root sets to meet.
    f34 = proper_profile(Q34)
    assert primitive(Q34)
    assert f34 == tuple(
        map(int, "3322232222222322223222223333222222")
    )
    assert all(x in (2, 3) for x in f34)
    assert word_power_root_lengths(Q34, 0, 3) == (1,)
    assert word_power_root_lengths(Q34, 1, 3) == (8,)

    # A period-21 bridge made from the known singleton fixed word.  It
    # gets the double 3 and its following 2 exactly right; only three
    # first-copy square holes remain.
    q21 = binary_word(tuple(map(int, "133233")))
    bridge_root = q21[16:] + q21[:16]
    q64 = bridge_root * 3 + (3,)
    f64 = proper_profile(q64)
    assert primitive(q64) and max(f64) == 3
    assert tuple(
        i for i, (x, y) in enumerate(zip(q64, f64)) if x != y
    ) == (2, 6, 11)
    assert q64[-1:] + q64[:2] == (3, 3, 2)
    assert f64[-1:] + f64[:2] == (3, 3, 2)

    # Distinguished-origin lift audit.  Rotating by one symbol puts a
    # 2 at phase zero and moves the unique double component to phases
    # 62,63.  Its period-21 bridge is fitting at both canonical cuts,
    # but its predecessor is the same component translated by -64.
    critical_q64 = q64[1:] + q64[:1]
    critical_f64 = proper_profile(critical_q64)
    assert critical_q64[0] == 2
    assert tuple(
        cut
        for cut in range(len(critical_q64))
        if (
            critical_q64[(cut - 1) % len(critical_q64)],
            critical_q64[cut],
            critical_q64[(cut + 1) % len(critical_q64)],
            critical_q64[(cut + 2) % len(critical_q64)],
        )
        == (2, 3, 3, 2)
    ) == (62,)
    assert word_power_root_lengths(critical_q64, 62, 3) == (1, 21)
    assert word_power_root_lengths(critical_q64, 63, 3) == (21,)
    assert 3 * 21 <= 64 + 62 - 1
    assert 3 * 21 <= 64 + 63 - 1
    assert 62 - (3 * 21 + 1) == -2
    assert all(
        not word_power_root_lengths(critical_q64, cut, 3)
        for cut, value in enumerate(critical_q64)
        if value == 2
    )
    assert all(
        not word_power_root_lengths(critical_q64, cut, 4)
        for cut in range(len(critical_q64))
    )
    assert tuple(
        (cut, value, critical_f64[cut])
        for cut, value in enumerate(critical_q64)
        if value != critical_f64[cut]
    ) == ((1, 2, 1), (5, 3, 1), (10, 2, 1))

    pairs = audit_scale_separation(14)
    print("Q7 =", "".join(map(str, Q7)))
    print("F7 =", "".join(map(str, f7)))
    print("Q12=", "".join(map(str, Q12)))
    print("F12=", "".join(map(str, f12)))
    print("Q34 disjoint roots: (1,) versus (8,)")
    print("Q64 bridge mismatches: 2,6,11")
    print(
        "critical Q64: component 62, p=21, predecessor lift -2; "
        "mismatches (1,2,1),(5,3,1),(10,2,1)"
    )
    print(f"audited primitive two-root pairs through n=14: {pairs}")


if __name__ == "__main__":
    main()
