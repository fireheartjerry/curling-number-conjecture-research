"""Audit the H_3-component quotient of the exact critical Q21 profile.

The word Q21 satisfies both its proper circular fixed-profile equations
and the first-copy deletion equations.  Boundaries are placed immediately
after each isolated ``32`` component/exit marker.  The script compares:

* exact return-token identities;
* their successor weights in Q21;
* the proper circular profiles of the identity and weight words; and
* alignment of every raw maximizing root with marker boundaries.

Every finite curling number is evaluated by the two independent
implementations in ``curling.py``.
"""

from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from curling import curling_number, curling_number_reference

from check_run_length_grammar import (
    primitive,
    proper_profile,
    word_power_root_lengths,
)


Word = tuple[int, ...]
Q21: Word = tuple(map(int, "223222322232322232223"))


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def circular_arc(word: Word, start: int, end: int) -> Word:
    result: list[int] = []
    cursor = start
    while cursor != end:
        result.append(word[cursor])
        cursor = (cursor + 1) % len(word)
    return tuple(result)


def quotient_words(word: Word, boundaries: tuple[int, ...]):
    returns = tuple(
        circular_arc(
            word,
            boundaries[index],
            boundaries[(index + 1) % len(boundaries)],
        )
        for index in range(len(boundaries))
    )
    identity_of: dict[Word, int] = {}
    token_identities: list[int] = []
    for return_word in returns:
        if return_word not in identity_of:
            identity_of[return_word] = len(identity_of)
        token_identities.append(identity_of[return_word])
    tokens = tuple(token_identities)
    weights = tuple(word[cut] for cut in boundaries)
    return returns, tokens, weights


def main() -> None:
    word = Q21
    n = len(word)
    assert primitive(word)
    assert proper_profile(word) == word

    # Directly recompute the complete critical synchronization equations
    # H_(a,j) and D_(a,j), for both copies used in the equivalence theorem.
    for copies in (1, 2):
        for phase, target in enumerate(word):
            high = word * copies + word[:phase]
            deleted = word[1:] + word * (copies - 1) + word[:phase]
            assert exact_cn(high) == target
            assert exact_cn(deleted) == target

    marker_boundaries = tuple(
        cut
        for cut in range(n)
        if word[(cut - 2) % n : cut] == (3, 2)
    )
    # The nonwrapping slice misses the marker ending at cut one.
    marker_boundaries = tuple(
        sorted(
            set(marker_boundaries)
            | {
                cut
                for cut in range(n)
                if (
                    word[(cut - 2) % n] == 3
                    and word[(cut - 1) % n] == 2
                )
            }
        )
    )
    assert marker_boundaries == (1, 4, 8, 12, 14, 18)

    returns, tokens, weights = quotient_words(
        word,
        marker_boundaries,
    )

    assert returns == (
        (2, 3, 2),
        (2, 2, 3, 2),
        (2, 2, 3, 2),
        (3, 2),
        (2, 2, 3, 2),
        (2, 2, 3, 2),
    )
    assert tokens == (0, 1, 1, 2, 1, 1)
    assert weights == (2, 2, 2, 3, 2, 2)
    assert primitive(tokens)
    assert primitive(weights)

    token_profile = proper_profile(tokens)
    weight_profile = proper_profile(weights)
    assert token_profile == (2, 1, 1, 2, 1, 1)
    assert weight_profile == (2, 3, 4, 5, 1, 1)

    records = []
    boundary_set = set(marker_boundaries)
    for token_cut, raw_cut in enumerate(marker_boundaries):
        target = word[raw_cut]
        raw_roots = word_power_root_lengths(word, raw_cut, target)
        assert raw_roots
        root_records = []
        for root in raw_roots:
            aligned = 0
            for copy in range(1, target + 1):
                if (raw_cut - copy * root) % n not in boundary_set:
                    break
                aligned = copy
            root_records.append(
                {
                    "root": root,
                    "aligned_predecessor_boundaries": aligned,
                    "earliest_power_start_is_boundary": (
                        (raw_cut - target * root) % n in boundary_set
                    ),
                }
            )
        records.append(
            {
                "token_cut": token_cut,
                "raw_cut": raw_cut,
                "weight": target,
                "raw_roots": raw_roots,
                "root_alignment": tuple(root_records),
                "token_profile": token_profile[token_cut],
                "weight_profile": weight_profile[token_cut],
            }
        )

    assert records[1]["root_alignment"] == (
        {
            "root": 3,
            "aligned_predecessor_boundaries": 1,
            "earliest_power_start_is_boundary": False,
        },
    )
    assert records[3]["root_alignment"] == (
        {
            "root": 4,
            "aligned_predecessor_boundaries": 2,
            "earliest_power_start_is_boundary": False,
        },
    )

    # A finer quotient places a boundary after every symbol below the
    # threshold.  Its two exact token identities have distinct weights,
    # so no information is lost by numerical relabeling.  It still fails
    # fixedness because the earliest copies of the raw powers are not
    # boundary aligned.
    separator_boundaries = tuple(
        cut for cut in range(n) if word[(cut - 1) % n] < 3
    )
    (
        separator_returns,
        separator_tokens,
        separator_weights,
    ) = quotient_words(word, separator_boundaries)
    separator_profile = proper_profile(separator_tokens)
    separator_weight_profile = proper_profile(separator_weights)
    assert set(separator_returns) == {(2,), (3, 2)}
    assert separator_tokens == (
        0,
        1,
        0,
        0,
        1,
        0,
        0,
        1,
        1,
        0,
        0,
        1,
        0,
        0,
        1,
    )
    assert separator_weights == (
        2,
        3,
        2,
        2,
        3,
        2,
        2,
        3,
        3,
        2,
        2,
        3,
        2,
        2,
        3,
    )
    assert separator_profile == separator_weight_profile
    assert separator_profile == (
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        1,
        2,
        2,
        1,
        2,
    )
    assert all(
        (left == right)
        == (separator_weights[left_index] == separator_weights[right_index])
        for left_index, left in enumerate(separator_tokens)
        for right_index, right in enumerate(separator_tokens)
    )

    print(
        {
            "word": "".join(map(str, word)),
            "proper_profile_exact": True,
            "critical_synchronization_exact": True,
            "marker_boundaries": marker_boundaries,
            "returns": returns,
            "token_identities": tokens,
            "weights": weights,
            "token_profile": token_profile,
            "weight_profile": weight_profile,
            "records": tuple(records),
            "separator_quotient": {
                "boundaries": separator_boundaries,
                "returns": separator_returns,
                "token_identities": separator_tokens,
                "weights": separator_weights,
                "weight_map_injective": True,
                "token_profile": separator_profile,
            },
        }
    )


if __name__ == "__main__":
    main()
