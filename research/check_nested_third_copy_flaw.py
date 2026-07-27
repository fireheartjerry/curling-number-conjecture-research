"""Exact falsifier for iterating the third-copy maximal-child lemma.

A child cube contained in U^3 need not have its own third copy contained
in the third copy of U.  The displayed word also shows that the
straddling branch is compatible with an exact square/no-cube label at
the crossed U-boundary.
"""

from __future__ import annotations

from check_run_length_grammar import (
    primitive,
    word_power_root_lengths,
)


def main() -> None:
    u = tuple(map(int, "2332323"))
    p = len(u)
    offset = 1
    child = 2
    cube = u * 3
    endpoint = 2 * p + offset
    child_left = endpoint - 3 * child
    child_third_left = endpoint - child
    parent_third_left = 2 * p

    assert primitive(u)
    assert word_power_root_lengths(u, offset, 3) == (child,)
    assert word_power_root_lengths(u, offset, 4) == ()
    assert child < p / 2
    assert cube[child_left:endpoint] == tuple(map(int, "323232"))
    assert 0 <= child_left < endpoint <= 3 * p

    # The child cube is contained in U^3, but its third copy straddles
    # the boundary between the second and third copies of U.
    assert child_third_left < parent_third_left < endpoint
    assert cube[child_third_left:endpoint] == (3, 2)

    # At the crossed U-boundary, the same child period supplies a
    # square but not a cube.  Thus the straddling case is compatible
    # with the required value 2 there.
    assert u[0] == 2
    assert child in word_power_root_lengths(u, 0, 2)
    assert child not in word_power_root_lengths(u, 0, 3)

    print(
        "U=2332323 p=7; cut offset=1 has primitive cube root 2; "
        "child third copy [13,15) straddles parent boundary 14"
    )
    print("at boundary phase 0: root 2 is a square and not a cube")


if __name__ == "__main__":
    main()
