from itertools import product

import pytest

from curling import curling_number, curling_number_reference
from research.generated_two_cube_falsifier import canonical_witness


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
