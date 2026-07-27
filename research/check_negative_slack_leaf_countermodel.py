"""Local exact countermodel to a pointed-slack ancestry rank.

The primitive circular word has the required exact profile values at the
three distinguished cuts, a nonfitting root-five parent square, and an
immediate root-one leaf.  It is not a complete fixed profile; the checker
prints every profile mismatch.
"""

from __future__ import annotations

from check_run_length_grammar import (
    primitive,
    proper_profile,
    word_power_root_lengths,
)


def main() -> None:
    word = tuple(map(int, "222332223"))
    size = len(word)
    profile = proper_profile(word)
    assert size == 9
    assert primitive(word)

    parent_cut = 0
    parent_root = 5
    high_cut = -1
    child_root = 1
    child_cut = -2
    distance = 1

    assert word[parent_cut] == profile[parent_cut] == 2
    assert parent_root in word_power_root_lengths(word, parent_cut, 2)
    assert word[high_cut % size] == profile[high_cut % size] == 3
    assert child_root in word_power_root_lengths(
        word,
        high_cut % size,
        3,
    )
    assert word[child_cut % size] == profile[child_cut % size] == 2
    assert child_root in word_power_root_lengths(
        word,
        child_cut % size,
        2,
    )

    parent_slack = size + parent_cut - 1 - 2 * parent_root
    child_slack = size + child_cut - 1 - 2 * child_root
    assert parent_slack == -2
    assert child_slack == 4
    assert (
        child_slack - parent_slack
        == 2 * parent_root - 3 * child_root - distance
    )

    # The root-one square is "22", so its one-symbol root has no high
    # coordinate and the ancestry path terminates.
    assert word[(child_cut - 1) % size] == 2

    mismatches = tuple(
        index
        for index, (symbol, value) in enumerate(zip(word, profile))
        if symbol != value
    )
    assert mismatches == (1, 4, 6)

    print(
        {
            "word": "".join(map(str, word)),
            "primitive": True,
            "proper_profile": profile,
            "profile_mismatches": mismatches,
            "parent": {
                "cut": parent_cut,
                "root": parent_root,
                "slack": parent_slack,
                "exact_profile_value": profile[parent_cut],
            },
            "edge": {
                "distance": distance,
                "high_cut": high_cut,
                "cube_root": child_root,
                "exact_profile_value": profile[high_cut % size],
            },
            "leaf": {
                "cut": child_cut,
                "root": child_root,
                "slack": child_slack,
                "exact_profile_value": profile[child_cut % size],
            },
        }
    )


if __name__ == "__main__":
    main()
