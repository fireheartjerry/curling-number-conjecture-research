"""Finite index checks for the symbolic Cell C reduction.

This file deliberately uses a definition-first canonical-witness routine and
does not import the production Cell C search.  The checks are bounded index
certificates, not proofs of any unbounded statement.
"""

from itertools import product
from math import gcd


Word = tuple[int, ...]


def _canonical_witness(word: Word) -> tuple[int, int]:
    feasible: dict[int, list[int]] = {}
    for exponent in range(2, len(word) + 1):
        for period in range(1, len(word) // exponent + 1):
            suffix = word[-exponent * period :]
            if suffix == suffix[:period] * exponent:
                feasible.setdefault(exponent, []).append(period)
    if not feasible:
        return 1, len(word)
    exponent = max(feasible)
    return exponent, min(feasible[exponent])


def _has_period(word: Word, period: int) -> bool:
    return word[:-period] == word[period:]


def _retained_cell_c_roots_through_10():
    equality_assignments = 0
    canonical_g = 0
    standalone_no_cube = 0
    retained: list[tuple[int, int, int, int, Word]] = []

    for q in range(1, 11):
        for b in range(1, q):
            P = q + b
            for j in range(q):
                s = b + j
                N = P + s
                for r in range(1, P):
                    if N - 3 * r < 0:
                        continue
                    if not r < s < 3 * r:
                        continue
                    if not 2 * r <= P - gcd(r, P) - 1:
                        continue

                    for root in product((2, 3), repeat=q):
                        if root[j] != 3:
                            continue
                        B = root[-b:]
                        T = root[:j]
                        V = B + root + B + T
                        if V[-3 * r :] != V[-r:] * 3:
                            continue

                        equality_assignments += 1
                        if _canonical_witness(root * 2) != (2, q):
                            continue
                        canonical_g += 1
                        if _canonical_witness(root * 2 + T)[0] != 2:
                            continue
                        standalone_no_cube += 1
                        if _canonical_witness(V) != (3, r):
                            continue
                        retained.append((q, b, j, r, root))

    return (
        equality_assignments,
        canonical_g,
        standalone_no_cube,
        tuple(retained),
    )


def test_cell_c_reduction_coordinate_certificate_through_q_10():
    (
        equality_assignments,
        canonical_g,
        standalone_no_cube,
        retained,
    ) = _retained_cell_c_roots_through_10()

    assert equality_assignments == 4958
    assert canonical_g == 538
    assert standalone_no_cube == 489
    assert len(retained) == 489
    assert all(b < 2 * r and j > 0 for q, b, j, r, root in retained)

    boundary = [
        item for item in retained if item[1] + item[2] == 2 * item[3]
        and item[2] == item[3]
    ]
    assert len(boundary) == 257

    generation_compatible = [
        item for item in boundary if item[4][-item[1]] == 2
    ]
    assert len(generation_compatible) == 130

    possible_early_periods = 0
    greater_branch = 0
    lesser_branch = 0
    for q, b, j, r, root in generation_compatible:
        B = root[-b:]
        T = root[:j]
        middle = root[r : q - r]
        U = root[r:]
        P = q + r
        W = root + B

        assert b == j == r
        assert T == B
        assert q > 2 * r
        assert B[0] == 2
        assert middle and middle[0] == 3
        assert (B + root + B + T)[-3 * r :] == B * 3

        for p in range(1, P):
            if 3 * p <= P or p == q or not _has_period(W, p):
                continue

            possible_early_periods += 1
            e = gcd(p, q)
            g = gcd(p, r)
            X = W[-p:]
            frontier = 3 * p - P

            assert r < p - e
            assert p > r + g
            assert frontier > 0
            assert (X * 3)[frontier:] == W

            if p > q:
                greater_branch += 1
                t = p - q
                assert r / 2 < t < r
                assert _has_period(B, t)
                assert X == B[r - t :] + U + B
                assert 3 * p > 2 * P
            else:
                lesser_branch += 1
                d = q - p
                nu = d - 2 * r
                Z = root[:p]
                assert p > q / 2
                assert root == Z + Z[:d]
                assert root[d : d + r] == B == root[:r] == root[-r:]
                assert d > 2 * r
                assert q > 4 * r
                assert p > 2 * r
                assert middle[: nu + 2 * r] == middle[:nu] + B * 2
                assert middle[-(r + nu) :] == B + middle[:nu]
                assert X == middle[d:] + B * 2

    assert possible_early_periods == 13
    assert greater_branch == 7
    assert lesser_branch == 6


def test_p_greater_q_local_replay_model_needs_the_period_cap():
    """The local replay conclusion is false if ``pi < P`` is omitted."""

    B = tuple(map(int, "232"))
    U = tuple(map(int, "322232"))
    R = B + U
    X = tuple(map(int, "32322232232"))
    q, r, p = 9, 3, 11
    P = q + r
    t = p - q

    assert P - p == r - t == 1
    assert X == B[r - t :] + U + B
    assert _has_period(R + B, p)
    assert (X * 3)[3 * p - P :] == R + B
    assert _canonical_witness(X * 3) == (3, p)
    assert _canonical_witness(R * 2) == (2, q)
    assert _canonical_witness(R * 2 + B)[0] == 2
    assert _canonical_witness(B + R + B + B) == (3, r)
    assert _canonical_witness(B + R + B + B + U) == (2, P)

    local_f_witnesses = tuple(
        _canonical_witness(X * 3 + U + B * 2 + U[:ell])
        for ell in range(len(U))
    )
    assert tuple(exponent for exponent, period in local_f_witnesses) == U
    assert local_f_witnesses == (
        (3, 3),
        (2, 2),
        (2, 2),
        (2, 1),
        (3, 1),
        (2, P),
    )
    assert _canonical_witness(X * 3 + U + B * 2 + U) == (2, P)

    # This is not a full G2CS antecedent: the early local replay already
    # disagrees at ell=1.
    assert _canonical_witness(X * 3 + U[:1]) == (3, p)
    assert U[1] == 2


def test_first_mismatch_near_model_needs_the_endpoint_scales():
    """Both sampled windows can replay while the endpoint periods are wrong."""

    B = tuple(map(int, "2232"))
    Q = tuple(map(int, "32"))
    U = Q + B
    R = B + Q + B
    q, r, t = 10, 4, 3
    p = q + t
    P = q + r
    a = r - t
    X = B[a:] + U + B
    continuation = U + B * 2 + U

    assert U == tuple(map(int, "322232"))
    assert X == tuple(map(int, "2323222322232"))
    assert U.index(2) == 1
    assert X[0] == B[a] == 2

    early_pairs = tuple(
        _canonical_witness(X * 3 + U[:ell])
        for ell in range(len(U))
    )
    later_pairs = tuple(
        _canonical_witness(X * 3 + continuation[: P + ell])
        for ell in range(len(U))
    )

    assert tuple(exponent for exponent, period in early_pairs) == U
    assert tuple(exponent for exponent, period in later_pairs) == U
    assert early_pairs == (
        (3, p),
        (2, 2),
        (2, 2),
        (2, 1),
        (3, 1),
        (2, 6),
    )
    assert later_pairs == (
        (3, r),
        (2, 2),
        (2, 2),
        (2, 1),
        (3, 1),
        (2, 6),
    )
    assert all(period < P for exponent, period in early_pairs + later_pairs)
    assert _canonical_witness(R * 2 + B) == (2, r)
    assert later_pairs[0] == (3, r)

    # It is not a G2CS survivor: the local endpoint scales are 6 rather than
    # the required q=10 and P=14.
    assert _canonical_witness(R * 2) == (2, 6)
    assert _canonical_witness(X * 3 + continuation) == (2, 6)
