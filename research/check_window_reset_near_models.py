"""Executed near-models for the finite-window phase-reset problem.

Both words below satisfy every proper circular fixed-profile equation
except one.  Their post-promotion orbits survive a complete block.  They
show exactly where the missing fixed equation is used and, in the second
model, falsify the tempting claim that the autonomous-one root produced
by a first phase loss makes the ambient orbit terminate immediately.
"""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from curling import curling_number, curling_number_reference
from research.check_run_length_grammar import primitive, proper_profile


P_CLEAN = tuple(map(int, "23222323222322232"))
P_CHAIN = tuple(map(int, "23223222323222322"))


def cn(word: tuple[int, ...]) -> int:
    fast = curling_number(word)
    slow = curling_number_reference(word)
    assert fast == slow
    return fast


def roots(word: tuple[int, ...], exponent: int) -> tuple[int, ...]:
    if exponent == 1:
        return ()
    return tuple(
        root
        for root in range(1, len(word) // exponent + 1)
        if word[-exponent * root :] == word[-root:] * exponent
    )


def is_cyclic_factor(
    p_word: tuple[int, ...], candidate: tuple[int, ...]
) -> bool:
    p = len(p_word)
    return any(
        candidate
        == tuple(p_word[(start + i) % p] for i in range(len(candidate)))
        for start in range(p)
    )


def trace(p_word: tuple[int, ...]):
    p = len(p_word)
    state = p_word * 3 + (3,)
    d_word = (3,)
    records = []
    first_loss = None
    for e in range(1, p + 1):
        value = cn(state)
        spectrum = roots(state, value)
        assert value >= 2
        assert all(root < p for root in spectrum)
        records.append((e, d_word, value, spectrum))
        d_word += (value,)
        if first_loss is None and not is_cyclic_factor(p_word, d_word):
            first_loss = len(d_word)
        state += (value,)
    return d_word, tuple(records), first_loss


def audit_clean_final_loss():
    profile = proper_profile(P_CLEAN)
    mismatches = tuple(
        i for i, (left, right) in enumerate(zip(P_CLEAN, profile))
        if left != right
    )
    assert primitive(P_CLEAN)
    assert mismatches == (7,)
    assert (P_CLEAN[7], profile[7]) == (3, 2)

    d_word, records, first_loss = trace(P_CLEAN)
    assert first_loss == len(P_CLEAN) + 1
    assert is_cyclic_factor(P_CLEAN, d_word[:-1])
    assert not is_cyclic_factor(P_CLEAN, d_word)
    assert records[-1][2] == profile[7] == 2
    return {
        "P": "".join(map(str, P_CLEAN)),
        "profile": "".join(map(str, profile)),
        "mismatch": mismatches[0],
        "D": "".join(map(str, d_word)),
        "first nonfactor length": first_loss,
        "last cn": records[-1][2],
    }


def audit_nonmonotone_reset_chain():
    profile = proper_profile(P_CHAIN)
    mismatches = tuple(
        i for i, (left, right) in enumerate(zip(P_CHAIN, profile))
        if left != right
    )
    assert primitive(P_CHAIN)
    assert mismatches == (10,)
    assert (P_CHAIN[10], profile[10]) == (3, 2)

    d_word, records, first_loss = trace(P_CHAIN)
    assert first_loss == 11

    # U is the last factor prefix; appending k=3 loses every phase.
    u_word = records[9][1]
    k = records[9][2]
    assert len(u_word) == 10
    assert k == 3
    assert is_cyclic_factor(P_CHAIN, u_word)
    assert not is_cyclic_factor(P_CHAIN, u_word + (k,))

    # At B=P^3 U k the least maximizing root has q=2 and is Y=23.
    b_state = P_CHAIN * 3 + u_word + (k,)
    ell = cn(b_state)
    spectrum = roots(b_state, ell)
    q = min(spectrum)
    y_word = (u_word + (k,))[-q:]
    assert ell == 2
    assert spectrum == (2,)
    assert y_word == (2, 3)
    assert cn(y_word) == 1

    # Nevertheless the ambient orbit does not terminate after appending
    # ell.  The least maximizing-root lengths later jump from 1 to 6,
    # so neither root length nor (root length, exponent) descends.
    continued = []
    state = b_state
    for _ in range(7):
        value = cn(state)
        spectrum = roots(state, value)
        continued.append((value, spectrum))
        state += (value,)
    assert continued == [
        (2, (2,)),
        (2, (2,)),
        (2, (1,)),
        (3, (1,)),
        (2, (6,)),
        (2, (6,)),
        (2, (1, 4)),
    ]
    assert continued[1][0] == 2

    return {
        "P": "".join(map(str, P_CHAIN)),
        "profile": "".join(map(str, profile)),
        "mismatch": mismatches[0],
        "first nonfactor length": first_loss,
        "U": "".join(map(str, u_word)),
        "k": k,
        "ell": ell,
        "Y": "".join(map(str, y_word)),
        "cn(Y)": cn(y_word),
        "continued values and roots": continued,
    }


def main() -> None:
    print({"clean_final_loss": audit_clean_final_loss()})
    print({"nonmonotone_reset_chain": audit_nonmonotone_reset_chain()})


if __name__ == "__main__":
    main()
