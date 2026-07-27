"""Verify the length-38 counterexample to profile variation and Hall."""

from __future__ import annotations

from check_run_length_grammar import (
    primitive,
    proper_profile,
    word_power_root_lengths,
)


Q38 = tuple(
    map(int, "22233323332333222333233322233323332333")
)
F38 = tuple(
    map(int, "33232232223222332322333333232232223222")
)


def cyclic_variation(word: tuple[int, ...]) -> int:
    return sum(
        word[i] != word[(i + 1) % len(word)]
        for i in range(len(word))
    )


def profile_three_components(
    profile: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    n = len(profile)
    components = []
    for start in range(n):
        if profile[start] != 3 or profile[(start - 1) % n] == 3:
            continue
        component = []
        cut = start
        while profile[cut] == 3:
            component.append(cut)
            cut = (cut + 1) % n
        components.append(tuple(component))
    return tuple(components)


def main() -> None:
    assert len(Q38) == 38
    assert primitive(Q38)
    profile = proper_profile(Q38)
    assert profile == F38
    assert all(value in (2, 3) for value in profile)
    assert cyclic_variation(Q38) == 16
    assert cyclic_variation(profile) == 20
    assert profile_three_components(profile) == (
        (0, 1),
        (3,),
        (6,),
        (10,),
        (14, 15),
        (17,),
        (20, 21, 22, 23, 24, 25),
        (27,),
        (30,),
        (34,),
    )

    # The singleton components at cuts 3 and 6 have only unary cube
    # roots.  Their unary runs are 222 at positions 0..2 and 333 at
    # positions 3..5.  For orientation 2->3, both therefore have the
    # same sole external candidate, the boundary after position 2.
    assert word_power_root_lengths(Q38, 3, 3) == (1,)
    assert word_power_root_lengths(Q38, 6, 3) == (1,)
    assert Q38[2:4] == (2, 3)

    print("Q38 =", "".join(map(str, Q38)))
    print("F38 =", "".join(map(str, profile)))
    print("Var(Q38)=16, Var(F38)=20")
    print("2->3 Hall obstruction: components {3}, {6} share edge 2")


if __name__ == "__main__":
    main()
