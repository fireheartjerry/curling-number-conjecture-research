"""Exhaustive diagnostics for codes A=(b_j,3,3)."""

from __future__ import annotations

from itertools import product

from check_run_length_grammar import binary_word, primitive, proper_profile
from explore_gadget_cycles import (
    defect_graph,
    exact_negative_constraints,
    perfect_matchings,
    wsq_holes,
)


def expand(b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x for value in b for x in (value, 3, 3))


def main(max_b: int = 10) -> None:
    for length in range(1, max_b + 1):
        covered = 0
        negative = 0
        exact = 0
        examples = []
        for b in product((1, 2, 3), repeat=length):
            a = expand(b)
            if not primitive(a):
                continue
            assert not wsq_holes(a)
            graph = defect_graph(a)
            if not graph or any(not edges for edges in graph.values()):
                continue
            covered += 1
            if not exact_negative_constraints(a):
                continue
            negative += 1
            q = binary_word(a)
            if proper_profile(q) == q:
                exact += 1
            if len(examples) < 10:
                examples.append(
                    (
                        "".join(map(str, b)),
                        len(perfect_matchings(a)),
                        graph,
                    )
                )
        print(
            f"|b|={length}: covered={covered} negative={negative} "
            f"exact={exact} examples={examples}"
        )


if __name__ == "__main__":
    main()
