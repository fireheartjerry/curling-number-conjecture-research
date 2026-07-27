"""Exact check of the minimal length-30 interval-Hall obstruction.

The proper circular profile uses only root lengths strictly below the
word length.  Every displayed profile value and every cube-root claim is
computed by executed code.
"""

from __future__ import annotations

from check_run_length_grammar import (
    primitive,
    proper_profile,
    word_power_root_lengths,
)


Q30 = tuple(map(int, "222333233232223332332322233323"))
F30 = tuple(map(int, "322322322222223223222222232233"))


def cyclic_variation(word: tuple[int, ...]) -> int:
    return sum(
        word[i] != word[(i + 1) % len(word)]
        for i in range(len(word))
    )


def profile_three_components(
    profile: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    n = len(profile)
    components: list[tuple[int, ...]] = []
    for start in range(n):
        if profile[start] != 3 or profile[(start - 1) % n] == 3:
            continue
        component: list[int] = []
        cut = start
        while profile[cut] == 3:
            component.append(cut)
            cut = (cut + 1) % n
        components.append(tuple(component))
    return tuple(components)


def oriented_external_edges(
    word: tuple[int, ...],
    start: int,
    length: int,
    left_symbol: int,
) -> tuple[int, ...]:
    """External unequal edges of one orientation around a unary run."""
    n = len(word)
    edges = ((start - 1) % n, (start + length - 1) % n)
    return tuple(
        edge
        for edge in edges
        if word[edge] == left_symbol
        and word[(edge + 1) % n] != left_symbol
    )


def main() -> None:
    assert len(Q30) == 30
    assert primitive(Q30)

    profile = proper_profile(Q30)
    assert profile == F30
    assert all(value in (2, 3) for value in profile)
    assert all(
        word_power_root_lengths(Q30, cut, 2)
        for cut in range(len(Q30))
    )
    assert all(
        not word_power_root_lengths(Q30, cut, 4)
        for cut in range(len(Q30))
    )

    components = profile_three_components(profile)
    assert components == (
        (3,),
        (6,),
        (14,),
        (17,),
        (25,),
        (28, 29, 0),
    )

    # The two selected singleton components have no nonunary cubic
    # witness.  Their sole cubic roots have length one.
    roots_at_3 = word_power_root_lengths(Q30, 3, 3)
    roots_at_6 = word_power_root_lengths(Q30, 6, 3)
    assert roots_at_3 == (1,)
    assert roots_at_6 == (1,)

    # The corresponding maximal unary runs are adjacent 222 and 333.
    # For orientation 2->3, their unique external candidate is in both
    # cases edge 2, the shared boundary between those runs.
    assert Q30[0:3] == (2, 2, 2)
    assert Q30[3:6] == (3, 3, 3)
    assert Q30[-1] == 3 and Q30[6] == 2
    candidates_222 = oriented_external_edges(Q30, 0, 3, 2)
    candidates_333 = oriented_external_edges(Q30, 3, 3, 2)
    assert candidates_222 == (2,)
    assert candidates_333 == (2,)
    assert len(set(candidates_222) | set(candidates_333)) == 1 < 2

    assert cyclic_variation(Q30) == 16
    assert cyclic_variation(profile) == 12

    print("Q30 =", "".join(map(str, Q30)))
    print("F30 =", "".join(map(str, profile)))
    print("F=3 components:", components)
    print("cube roots at cuts 3 and 6:", roots_at_3, roots_at_6)
    print("2->3 candidates:", candidates_222, candidates_333)
    print("Hall deficit: union size 1 for 2 components")
    print("Var(Q30)=16, Var(F30)=12")


if __name__ == "__main__":
    main()
