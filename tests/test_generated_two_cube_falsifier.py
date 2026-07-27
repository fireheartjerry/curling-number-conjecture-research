from itertools import product

import pytest

from curling import curling_number, curling_number_reference
from research.generated_two_cube_falsifier import (
    canonical_witness,
    generated_states,
    synchronization_evaluation_states,
)


def test_canonical_witness_checks_every_block_length():
    assert canonical_witness((2, 3, 2, 3, 2)) == (2, 2)


def test_canonical_witness_uses_shortest_maximizing_period():
    assert canonical_witness((2, 2, 2, 2)) == (4, 1)


def test_canonical_witness_uses_whole_word_sentinel_for_exponent_one():
    assert canonical_witness((2, 3)) == (1, 2)


def test_canonical_witness_rejects_empty_word():
    with pytest.raises(
        ValueError, match="^canonical_witness requires a nonempty word$"
    ):
        canonical_witness(())


def test_canonical_witness_matches_reference_implementations_on_small_ternary_words():
    for length in range(1, 9):
        for word in product((-1, 0, 1), repeat=length):
            exponent, period = canonical_witness(word)
            assert exponent == curling_number(word)
            assert exponent == curling_number_reference(word)
            if exponent == 1:
                assert period == len(word)
                continue

            periods = []
            for candidate in range(1, len(word) // exponent + 1):
                block = word[-candidate:]
                if block * exponent == word[-candidate * exponent :]:
                    periods.append(candidate)
            assert period == min(periods)


def test_generated_states_include_start_and_terminal():
    states = generated_states((2, 2), (2,))
    assert states == ((2, 2), (2, 2, 2))


def test_generated_states_reject_wrong_requested_symbol():
    with pytest.raises(ValueError, match=r"^expected 2 but generated 1$"):
        generated_states((2, 3), (2,))


def test_generated_states_accept_empty_requested_block():
    assert generated_states((2, 3), ()) == ((2, 3),)


def test_generated_states_recomputes_witness_after_each_append():
    assert generated_states((2, 2), (2, 3)) == (
        (2, 2),
        (2, 2, 2),
        (2, 2, 2, 3),
    )


def test_generated_states_rejects_empty_start_word():
    with pytest.raises(
        ValueError, match=r"^generated_states requires a nonempty start word$"
    ):
        generated_states((), ())


def test_synchronization_evaluation_states_includes_g_and_excludes_h():
    early = ((1,), (1, 2))
    later = ((3,), (3, 2))
    assert synchronization_evaluation_states(early, later) == ((1,), (1, 2), (3,))


@pytest.mark.parametrize(
    ("early", "later", "message"),
    [
        (
            (),
            ((3,),),
            "synchronization_evaluation_states requires nonempty early_states",
        ),
        (
            ((1,),),
            (),
            "synchronization_evaluation_states requires nonempty later_states",
        ),
    ],
)
def test_synchronization_evaluation_states_rejects_empty_state_traces(
    early, later, message
):
    with pytest.raises(ValueError, match=f"^{message}$"):
        synchronization_evaluation_states(early, later)


def test_synchronization_evaluation_states_preserves_order_and_duplicate_states():
    repeated = (1,)
    early = (repeated, repeated)
    later = (repeated, repeated)
    assert synchronization_evaluation_states(early, later) == (
        repeated,
        repeated,
        repeated,
    )


def test_synchronization_evaluation_states_normalizes_mutable_inner_states():
    early = [[1], [1, 2]]
    later = [[3], [3, 2]]

    states = synchronization_evaluation_states(early, later)
    early[0].append(99)
    later[0].append(99)

    assert states == ((1,), (1, 2), (3,))
