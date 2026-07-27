"""Audit the unary-external-source to gap-four-pair bridge.

Run the A094004 calibration first.  The symbolic lemma is proved in
``external_reset_chain_states.md``; this script recomputes its two Q21
realizations and the corresponding extended-ancestry edges.
"""

from __future__ import annotations

from check_extended_cap_ancestry_q21 import (
    Q21,
    extended_fitting_ancestry,
)
from check_run_length_grammar import (
    primitive,
    proper_profile,
    word_power_root_lengths,
)


PAIR = tuple(map(int, "222322232"))
MARKER = tuple(map(int, "22232"))


def circular_factor(
    word: tuple[int, ...], start: int, length: int
) -> tuple[int, ...]:
    return tuple(word[(start + offset) % len(word)] for offset in range(length))


def main() -> None:
    word = Q21
    size = len(word)
    assert primitive(word)
    assert proper_profile(word) == word

    _, edges = extended_fitting_ancestry(word)
    records: list[dict[str, object]] = []
    for source in ((9, 1), (19, 1)):
        outgoing = edges[source]
        assert len(outgoing) == 1
        child_cut, child_root, distance, high = outgoing[0]
        assert (child_root, distance) == (1, 3)
        assert circular_factor(word, high - 3, 9) == PAIR
        assert circular_factor(word, high - 3, 5) == MARKER
        assert circular_factor(word, high + 1, 5) == MARKER
        assert 1 in word_power_root_lengths(word, high, 3)
        assert 1 in word_power_root_lengths(word, high + 4, 3)

        child = (child_cut, child_root)
        next_records = edges[child]
        assert next_records
        # A second selected unary external edge would create three markers
        # four symbols apart.  In Q21 the deterministic fitting choice is
        # already the nonunary root-four reset.
        assert all(record[1] != 1 for record in next_records)
        assert tuple(record[1] for record in next_records) == (4,)

        records.append(
            {
                "source": source,
                "unary_external_edge": outgoing[0],
                "high": high,
                "pair_factor": "".join(
                    map(str, circular_factor(word, high - 3, 9))
                ),
                "marker_cube_endpoints": (high, (high + 4) % size),
                "next_selected_roots": tuple(
                    record[1] for record in next_records
                ),
            }
        )

    print(
        {
            "word": "".join(map(str, word)),
            "unary_external_pair_records": tuple(records),
        }
    )


if __name__ == "__main__":
    main()
