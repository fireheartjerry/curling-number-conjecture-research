from itertools import product

import pytest

from research.generated_two_cube_falsifier import (
    bridge_inclusive_precompletion_states,
)


def _has_period(word: tuple[int, ...], period: int) -> bool:
    return word[:-period] == word[period:]


def _has_square_suffix(word: tuple[int, ...]) -> bool:
    return any(
        word[-2 * period : -period] == word[-period:]
        for period in range(1, len(word) // 2 + 1)
    )


def _border_conjugate_audit(
    alphabet: tuple[int, ...], max_root_length: int
) -> tuple[int, int]:
    retained = 0
    failures = 0
    for root_length in range(1, max_root_length + 1):
        for root in product(alphabet, repeat=root_length):
            for border_length in range(1, (root_length - 1) // 2 + 1):
                if root[:border_length] != root[-border_length:]:
                    continue
                for cut in range(root_length - border_length):
                    conjugate = root[cut:] + root[:cut]
                    for period in range(1, border_length):
                        if not _has_period(conjugate, period):
                            continue
                        retained += 1
                        if not _has_square_suffix(root):
                            failures += 1
    return retained, failures


@pytest.mark.parametrize(
    ("alphabet", "max_root_length", "expected_retained"),
    [
        ((2, 3), 15, 1776),
        ((1, 2, 3), 11, 690),
    ],
)
def test_border_conjugate_lemma_exhaustive_oracle(
    alphabet, max_root_length, expected_retained
):
    retained, failures = _border_conjugate_audit(alphabet, max_root_length)

    # The asserted caps and survivor counts prevent a silently weakened or
    # vacuous certificate. The proof itself remains the argument in the ledger.
    assert retained == expected_retained
    assert failures == 0


def test_bridge_inclusive_precompletion_decomposes_j_and_excludes_h():
    early = [[1], [1, 2]]
    bridge = [[1, 2], [1, 2, 3], [1, 2, 3, 2]]
    later = [[1, 2, 3, 2], [1, 2, 3, 2, 3], [1, 2, 3, 2, 3, 2]]

    states = bridge_inclusive_precompletion_states(early, bridge, later)

    assert states == (
        (1,),
        (1, 2),  # G, included once.
        (1, 2, 3),  # A proper bridge state K_h.
        (1, 2, 3, 2),  # F, included once.
        (1, 2, 3, 2, 3),  # A proper later state.
    )
    assert tuple(later[-1]) not in states  # H is excluded.

    early[0].append(99)
    bridge[1].append(99)
    later[1].append(99)
    assert states[0] == (1,)
    assert states[2] == (1, 2, 3)
    assert states[-1] == (1, 2, 3, 2, 3)


def test_bridge_inclusive_precompletion_j_zero_still_includes_nonempty_bridge():
    # When j=0, s=b+j=b>0: G and F are still distinct consecutive endpoints.
    early = ((2,), (2, 3))
    bridge = ((2, 3), (2, 3, 2))
    later = ((2, 3, 2), (2, 3, 2, 3))

    assert bridge_inclusive_precompletion_states(early, bridge, later) == (
        (2,),
        (2, 3),
        (2, 3, 2),
    )


@pytest.mark.parametrize(
    ("early", "bridge", "later", "message"),
    [
        (
            ((1,), (1, 2)),
            ((9,), (9, 3)),
            ((9, 3), (9, 3, 2)),
            "bridge start must equal the early terminal state G",
        ),
        (
            ((1,), (1, 2)),
            ((1, 2), (1, 2, 3)),
            ((9,), (9, 2)),
            "later start must equal the bridge terminal state F",
        ),
    ],
)
def test_bridge_inclusive_precompletion_rejects_endpoint_mismatch(
    early, bridge, later, message
):
    with pytest.raises(ValueError, match=f"^{message}$"):
        bridge_inclusive_precompletion_states(early, bridge, later)


@pytest.mark.parametrize(
    ("early", "bridge", "later", "message"),
    [
        (
            ((1,),),
            ((1,), (1, 2)),
            ((1, 2), (1, 2, 3)),
            "early_states must contain E through G",
        ),
        (
            ((1,), (1, 2)),
            ((1, 2),),
            ((1, 2), (1, 2, 3)),
            "bridge_states must contain G through F",
        ),
        (
            ((1,), (1, 2)),
            ((1, 2), (1, 2, 3)),
            ((1, 2, 3),),
            "later_states must contain F through H",
        ),
        (
            ((1,), ()),
            ((), (2,)),
            ((2,), (2, 3)),
            "state traces must contain only nonempty states",
        ),
    ],
)
def test_bridge_inclusive_precompletion_rejects_degenerate_traces(
    early, bridge, later, message
):
    with pytest.raises(ValueError, match=f"^{message}$"):
        bridge_inclusive_precompletion_states(early, bridge, later)
