"""Finite checks for the Cell C boundary branch ``p < q``.

The exhaustive part is deliberately definition-first and independent of the
production Cell C searches.  These are bounded index checks and sharpness
certificates, not proofs of any unbounded statement.
"""

from itertools import product
from math import gcd


Word = tuple[int, ...]
StaticModel = tuple[int, int, int, Word]


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
    assert 0 < period < len(word)
    return word[:-period] == word[period:]


def _terminal_run(word: Word, symbol: int) -> int:
    length = 0
    for value in reversed(word):
        if value != symbol:
            break
        length += 1
    return length


def _static_models_through_14() -> tuple[StaticModel, ...]:
    """Return every exact static ``p<q`` boundary tuple through ``q=14``."""

    retained: list[StaticModel] = []
    for q in range(1, 15):
        for r in range(1, (q - 1) // 2 + 1):
            P = q + r
            for R in product((2, 3), repeat=q):
                B = R[:r]
                Q = R[r : q - r]
                if R[-r:] != B:
                    continue
                if B[0] != 2 or not Q or Q[0] != 3:
                    continue
                if _canonical_witness(R * 2) != (2, q):
                    continue
                if _canonical_witness(R * 2 + B)[0] != 2:
                    continue
                if _canonical_witness(B + R + B * 2) != (3, r):
                    continue

                W = R + B
                for p in range(1, q):
                    if 3 * p <= P or not _has_period(W, p):
                        continue
                    X = W[-p:]
                    if _canonical_witness(X * 3) != (3, p):
                        continue
                    retained.append((q, r, p, R))
    return tuple(retained)


def test_p_less_q_normal_form_through_q_14():
    """The strengthened overlap normal form is nonvacuous and exact."""

    retained = _static_models_through_14()
    assert len(retained) == 141

    for q, r, p, R in retained:
        P = q + r
        d = q - p
        a = d - r
        nu = d - 2 * r
        B = R[:r]
        Q = R[r : q - r]
        U = Q + B
        W = R + B
        X = W[-p:]
        Z = R[:p]
        A = Q[:a]
        C = Q[-a:]
        Theta = Q[:nu]

        assert p > q / 2
        assert R == Z + Z[:d]
        assert R[d : d + r] == B == R[:r] == R[-r:]

        assert d > 2 * r
        assert q > 4 * r
        assert p > 2 * r
        assert p < len(U)
        assert 2 * a < len(Q)

        assert B + A == C + B
        assert A == Theta + B
        assert C == B + Theta
        assert Q[: nu + 2 * r] == Theta + B * 2
        assert Q[-(r + nu) :] == B + Theta
        assert X == Q[d:] + B * 2

        assert r < p - gcd(p, q)
        assert p > r + gcd(p, r)
        assert (X * 3)[3 * p - P :] == W


def test_p_less_q_crossing_root_localization_slots_through_q_14():
    """No bounded static model admits a crossing root below ``P``."""

    slots = 0
    candidates = 0
    for q, r, p, R in _static_models_through_14():
        P = q + r
        X = (R + R[:r])[-p:]
        X3 = X * 3

        for phase in range(2 * q):
            local_length = 3 * p + phase
            for exponent in (2, 3):
                for period in range(1, P):
                    if exponent * period <= local_length:
                        continue
                    slots += 1
                    if _has_period(X3, period):
                        candidates += 1

    assert slots == 3753
    assert candidates == 0


def test_p_less_q_first_mismatch_uses_periodic_extension():
    """The three mismatch rows survive the corrected ``X^omega`` indexing."""

    row_counts = {(1, 0): 0, (2, 0): 0, (2, 1): 0}
    qualified = 0

    for q, r, p, R in _static_models_through_14():
        B = R[:r]
        U = R[r:]
        X = (R + B)[-p:]
        assert p < len(U)

        z = U.index(2)
        h = next(
            index
            for index, value in enumerate(U)
            if value != X[index % p]
        )
        terminal_threes = _terminal_run(B, 3)
        if not (h < z and terminal_threes + z <= 2):
            continue

        qualified += 1
        row_counts[(z, h)] += 1
        assert U[: h + 1] == (3,) * (h + 1)
        assert X[h] == 2

        if (z, h) == (1, 0):
            assert X[0] == 2
            assert terminal_threes <= 1
        elif (z, h) == (2, 0):
            assert X[0] == 2
            assert B[-1] == 2
        else:
            assert (z, h) == (2, 1)
            assert X[:2] == (3, 2)
            assert B[-1] == 2

    assert qualified == 74
    assert row_counts == {(1, 0): 41, (2, 0): 21, (2, 1): 12}


def test_p_less_q_shifted_suffix_sharpness_model():
    """The ``2p<P`` suffix geometry is real but does not replay."""

    q, r, p = 20, 3, 11
    d = q - p
    P = q + r
    c = P - 2 * p
    nu = d - 2 * r
    B = tuple(map(int, "232"))
    Q = tuple(map(int, "33223223232332"))
    U = tuple(map(int, "33223223232332232"))
    R = tuple(map(int, "23233223223232332232"))
    X = tuple(map(int, "32332232232"))
    Theta = Q[:nu]
    W = R + B

    assert R == B + Q + B
    assert U == Q + B
    assert d > 2 * r
    assert Q[: nu + 2 * r] == Theta + B * 2
    assert Q[-(r + nu) :] == B + Theta
    assert X == Q[d:] + B * 2

    assert c == 1
    assert 0 < c < r / 2
    assert W == X[-c:] + X * 2
    assert B[:c] == B[-c:]
    assert _has_period(B, r - c)

    assert _canonical_witness(R * 2) == (2, q)
    assert _canonical_witness(R * 2 + B) == (2, r)
    assert _canonical_witness(B + R + B * 2) == (3, r)
    assert _canonical_witness(X * 3) == (3, p)
    assert _canonical_witness(X * 3 + U) == (2, q)
    assert _canonical_witness(X * 3 + U + B * 2) == (3, r)
    assert _canonical_witness(X * 3 + U + B * 2 + U) == (2, P)

    z = U.index(2)
    h = next(
        index
        for index, value in enumerate(U)
        if value != X[index % p]
    )
    assert (z, h) == (2, 1)
    assert X[:2] == (3, 2)
    assert B[-1] == 2

    # Static endpoint geometry and the mismatch trichotomy are insufficient:
    # the later replay already fails at phase one.
    assert U[1] == 3
    assert _canonical_witness(X * 3 + U + B * 2 + U[:1]) == (2, 2)
