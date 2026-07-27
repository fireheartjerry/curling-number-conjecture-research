"""Executable audits for the post-promotion root bound.

Notation
--------
Let ``P`` have length ``p`` and ``P[0] == 2``.  A post-promotion
state is

    A_h = P^3 D,       D = (3,) + H,       len(H) = h < p,

where every symbol of ``H`` was produced by the curling-number orbit.

The proof in ``post_promotion_escape.md`` shows that no primitive
maximizing root at ``A_h`` can have length at least ``p``.  This file
checks:

* the exact square equations used in the proof;
* the local sharpness example ``P=233, D=323``;
* every ternary ``P`` with ``P[0]=2`` through length nine, following
  its actual post-promotion orbit while ``h<p``; and
* every rotation beginning in 2 of the length-21 circular replay word.

Every curling number used here is evaluated by the two independent
implementations in ``curling.py``.
"""

from __future__ import annotations

from itertools import product
from math import gcd
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from curling import curling_number, curling_number_reference
from research.check_run_length_grammar import primitive, proper_profile


REPLAY_21 = tuple(map(int, "223222322232322232223"))


def cn(word: tuple[int, ...]) -> int:
    """Compute a curling number with two independent implementations."""
    fast = curling_number(word)
    slow = curling_number_reference(word)
    assert fast == slow
    return fast


def maximizing_roots(word: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    """Return ``cn(word)`` and all root lengths attaining it.

    Root lengths are meaningful only when the returned exponent is at
    least two.  For exponent one the spectrum is returned as empty.
    """
    exponent = cn(word)
    if exponent == 1:
        return exponent, ()
    roots = tuple(
        root
        for root in range(1, len(word) // exponent + 1)
        if word[-exponent * root :] == word[-root:] * exponent
    )
    assert roots
    return exponent, roots


def cyclic_slice(
    word: tuple[int, ...], start: int, length: int
) -> tuple[int, ...]:
    """Read ``length`` symbols from the bi-infinite periodic word."""
    return tuple(word[(start + offset) % len(word)] for offset in range(length))


def assert_escape_equations(
    p_word: tuple[int, ...],
    d_word: tuple[int, ...],
    root: int,
) -> None:
    """Check the indexed equations forced by a crossing square.

    Preconditions are that ``(P^3 D)`` ends in a square with root
    length ``root=p+s>p`` and that ``len(D)<=p``.  No orbit assumption
    is used by this routine.
    """
    p = len(p_word)
    e = len(d_word)
    s = root - p
    whole = p_word * 3 + d_word
    assert 0 < s < e <= p
    assert whole[-2 * root :] == whole[-root:] * 2

    # The tail of the second root is the cyclic P-factor beginning
    # s positions before phase zero.
    expected_d = cyclic_slice(p_word, -s, e)
    assert d_word == expected_d

    # The initial overlap of the two roots lies wholly in P^3.
    overlap = p + s - e
    assert overlap > 0
    for j in range(overlap):
        assert (
            p_word[(e - 2 * s + j) % p]
            == p_word[e - s + j]
        )

    # Put delta=e-s.  The same equalities state that the lifted
    # P-factor [delta-s,p) has period s.
    delta = e - s
    factor = cyclic_slice(p_word, delta - s, p - delta + s)
    assert all(factor[j] == factor[j - s] for j in range(s, len(factor)))


def audit_local_square_equations(max_p: int = 7) -> int:
    """Exhaustively audit every small ternary crossing square."""
    checked = 0
    alphabet = (1, 2, 3)
    for p in range(2, max_p + 1):
        for tail in product(alphabet, repeat=p - 1):
            p_word = (2,) + tail
            for e in range(1, p + 1):
                for d_tail in product(alphabet, repeat=e - 1):
                    d_word = (3,) + d_tail
                    whole = p_word * 3 + d_word
                    for root in range(p + 1, len(whole) // 2 + 1):
                        if whole[-2 * root :] != whole[-root:] * 2:
                            continue
                        s = root - p
                        # The post-promotion proof first obtains
                        # s<e from its Fine--Wilf inequality.
                        if s >= e:
                            continue
                        assert_escape_equations(p_word, d_word, root)
                        checked += 1
    return checked


def audit_actual_orbits(max_p: int = 9) -> tuple[int, int]:
    """Exhaustively rule out crossing maximizing roots on small starts.

    The enumeration is over all words ``P=(2,...)`` on ``{1,2,3}``.
    It does not assume primitivity or ``pc(P)=P``, so it checks a
    strictly broader class than the theorem's application.
    """
    starts = 0
    states = 0
    for p in range(1, max_p + 1):
        for tail in product((1, 2, 3), repeat=p - 1):
            starts += 1
            p_word = (2,) + tail
            state = p_word * 3 + (3,)
            for _h in range(p):
                exponent, roots = maximizing_roots(state)
                states += 1
                assert not any(root >= p for root in roots)
                if exponent == 1:
                    break
                state += (exponent,)
    return starts, states


def audit_first_step_fixed_profiles(max_p: int = 9) -> int:
    """Check the arbitrary-alphabet first-step bounds on small models."""
    checked = 0
    for p in range(1, max_p + 1):
        for tail in product((1, 2, 3), repeat=p - 1):
            p_word = (2,) + tail
            if not primitive(p_word) or proper_profile(p_word) != p_word:
                continue
            exponent, roots = maximizing_roots(p_word * 3 + (3,))
            checked += 1
            if exponent == 1:
                continue
            assert exponent <= 3
            for root in roots:
                assert root < p
                assert (exponent - 1) * root + gcd(p, root) <= p
                if exponent == 3:
                    assert 2 * root + gcd(p, root) <= p
                    assert 2 * root < p
    return checked


def audit_replay_rotations() -> tuple[int, int]:
    """Check every phase-zero normalization of the length-21 replay."""
    p = len(REPLAY_21)
    assert primitive(REPLAY_21)
    assert proper_profile(REPLAY_21) == REPLAY_21
    rotations = 0
    states = 0
    for shift in range(p):
        p_word = REPLAY_21[shift:] + REPLAY_21[:shift]
        if p_word[0] != 2:
            continue
        assert proper_profile(p_word) == p_word
        rotations += 1
        state = p_word * 3 + (3,)
        for _h in range(p):
            exponent, roots = maximizing_roots(state)
            states += 1
            assert not any(root >= p for root in roots)
            if exponent == 1:
                break
            state += (exponent,)
    return rotations, states


def audit_local_sharpness() -> dict[str, object]:
    """Recompute the exact non-orbit crossing-square example."""
    p_word = (2, 3, 3)
    d_word = (3, 2, 3)
    whole = p_word * 3 + d_word
    exponent, roots = maximizing_roots(whole)
    assert exponent == 2
    assert roots == (4,)
    assert_escape_equations(p_word, d_word, roots[0])

    first_state = p_word * 3 + (3,)
    first_value = cn(first_state)
    assert first_value == 3
    assert d_word[1] == p_word[0] == 2
    assert first_value != d_word[1]
    return {
        "P": "".join(map(str, p_word)),
        "D": "".join(map(str, d_word)),
        "word": "".join(map(str, whole)),
        "cn(word)": exponent,
        "maximizing roots": roots,
        "cn(P^3 3)": first_value,
        "required next symbol": d_word[1],
    }


def main() -> None:
    equation_cases = audit_local_square_equations()
    starts, orbit_states = audit_actual_orbits()
    fixed_profiles = audit_first_step_fixed_profiles()
    rotations, replay_states = audit_replay_rotations()
    sharpness = audit_local_sharpness()
    print(f"crossing-square equation cases checked: {equation_cases}")
    print(
        "actual ternary post-promotion orbits checked: "
        f"{starts} starts, {orbit_states} states"
    )
    print(f"small pc-fixed profiles checked: {fixed_profiles}")
    print(
        "length-21 replay rotations checked: "
        f"{rotations} rotations, {replay_states} states"
    )
    print(f"local sharpness certificate: {sharpness}")


if __name__ == "__main__":
    main()
