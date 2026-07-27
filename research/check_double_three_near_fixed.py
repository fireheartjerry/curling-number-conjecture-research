"""Executed certificates for two globally near-fixed adjacent-33 models.

Both words are primitive and have proper circular profile in {2,3} at
every cut.  They isolate the two complementary global obligations:

* Q35 has every positive square/cube witness, but four 2-labelled cuts
  acquire forbidden cubes.
* Q41 has every square and no forbidden cube/fourth power, but four
  3-labelled cuts lack cubes.

All profile values and every displayed root set are recomputed by the
direct enumerator in ``check_run_length_grammar.py``.
"""

from __future__ import annotations

from math import gcd

from check_run_length_grammar import (
    primitive,
    proper_profile,
    word_power_root_lengths,
)


Word = tuple[int, ...]
Q35: Word = tuple(map(int, "33222322233222322232223322232223222"))
F35: Word = tuple(map(int, "33222333333222322233223322232223222"))
Q41: Word = tuple(
    map(int, "33222322232232223322232223223222332223222")
)
F41: Word = tuple(
    map(int, "33222322232222223222232223222222322223222")
)


def roots(word: Word, cut: int) -> tuple[
    tuple[int, ...], tuple[int, ...], tuple[int, ...]
]:
    return tuple(
        word_power_root_lengths(word, cut, exponent)
        for exponent in (2, 3, 4)
    )  # type: ignore[return-value]


def double_components(word: Word) -> tuple[int, ...]:
    n = len(word)
    return tuple(
        cut
        for cut in range(n)
        if (
            word[(cut - 1) % n],
            word[cut],
            word[(cut + 1) % n],
            word[(cut + 2) % n],
        )
        == (2, 3, 3, 2)
    )


def audit_q35() -> dict[str, object]:
    profile = proper_profile(Q35)
    assert primitive(Q35)
    assert profile == F35
    assert set(profile) == {2, 3}
    mismatches = tuple(
        (cut, Q35[cut], profile[cut])
        for cut in range(len(Q35))
        if Q35[cut] != profile[cut]
    )
    assert mismatches == (
        (6, 2, 3),
        (7, 2, 3),
        (8, 2, 3),
        (19, 2, 3),
    )

    # Every requested positive witness exists; no fourth power exists.
    assert all(word_power_root_lengths(Q35, cut, 2) for cut in range(35))
    assert all(
        word_power_root_lengths(Q35, cut, 3)
        for cut in range(35)
        if Q35[cut] == 3
    )
    assert all(
        not word_power_root_lengths(Q35, cut, 4)
        for cut in range(35)
    )

    components = double_components(Q35)
    assert components == (0, 9, 22)
    component_roots = tuple(
        (
            cut,
            word_power_root_lengths(Q35, cut, 3),
            word_power_root_lengths(Q35, cut + 1, 3),
        )
        for cut in components
    )
    assert component_roots == (
        (0, (1, 4), (4,)),
        (9, (1, 13), (13,)),
        (22, (1, 4), (4,)),
    )

    # The four cuts immediately around the normalized component.
    local = tuple(
        (cut % 35, Q35[cut % 35], profile[cut % 35], roots(Q35, cut))
        for cut in (-1, 0, 1, 2)
    )
    assert local == (
        (34, 2, 2, ((1, 4, 13), (), ())),
        (0, 3, 3, ((1, 4, 13), (1, 4), ())),
        (1, 3, 3, ((4, 13), (4,), ())),
        (2, 2, 2, ((1, 13), (), ())),
    )

    # The period-13 cube at the middle component is not left-tight:
    # it persists through the three preceding 2-labelled cuts.
    assert tuple(
        word_power_root_lengths(Q35, cut, 3)
        for cut in (5, 6, 7, 8, 9, 10)
    ) == (
        (1, 13),
        (13,),
        (13,),
        (13,),
        (1, 13),
        (13,),
    )

    # Wrapping-marker calibration.  The globally largest cube root 13
    # ending at cut 9 starts at cut 5.  In start-zero coordinates,
    # n=35=3*13-4 and the copied endpoint marker is at E=2*13+4.
    outer_root = 13
    cube_start = 5
    overlap = 3 * outer_root - len(Q35)
    outer_word = tuple(
        Q35[(cube_start + offset) % len(Q35)]
        for offset in range(outer_root)
    )
    internal_cut = (
        cube_start + 2 * outer_root + overlap
    ) % len(Q35)
    assert overlap == 4
    assert outer_word[:overlap] == outer_word[-overlap:]
    assert outer_word[overlap] == 3
    assert internal_cut == 0
    assert word_power_root_lengths(Q35, internal_cut, 3) == (1, 4)
    child_root = 4
    assert 2 * child_root + gcd(outer_root, child_root) < outer_root
    assert word_power_root_lengths(Q35, 19, 3) == (9,)

    return {
        "word": "".join(map(str, Q35)),
        "profile": "".join(map(str, profile)),
        "mismatches": mismatches,
        "component_roots": component_roots,
        "local": local,
        "wrapping_marker": (
            cube_start,
            outer_root,
            overlap,
            internal_cut,
            child_root,
        ),
        "regrown_cube": (19, 9),
    }


def audit_q41() -> dict[str, object]:
    profile = proper_profile(Q41)
    assert primitive(Q41)
    assert profile == F41
    assert set(profile) == {2, 3}
    mismatches = tuple(
        (cut, Q41[cut], profile[cut])
        for cut in range(len(Q41))
        if Q41[cut] != profile[cut]
    )
    assert mismatches == (
        (12, 3, 2),
        (17, 3, 2),
        (28, 3, 2),
        (33, 3, 2),
    )

    # Every cut is squareful, every 2-cut excludes cubes, and every cut
    # excludes fourth powers.  Only four requested cube witnesses are absent.
    assert all(word_power_root_lengths(Q41, cut, 2) for cut in range(41))
    assert all(
        not word_power_root_lengths(Q41, cut, 3)
        for cut in range(41)
        if Q41[cut] == 2
    )
    assert all(
        not word_power_root_lengths(Q41, cut, 4)
        for cut in range(41)
    )

    components = double_components(Q41)
    assert components == (0, 16, 32)
    component_roots = tuple(
        (
            cut,
            word_power_root_lengths(Q41, cut, 3),
            word_power_root_lengths(Q41, cut + 1, 3),
        )
        for cut in components
    )
    assert component_roots == (
        (0, (1,), (16,)),
        (16, (1,), ()),
        (32, (1,), ()),
    )

    local = tuple(
        (cut % 41, Q41[cut % 41], profile[cut % 41], roots(Q41, cut))
        for cut in (-1, 0, 1, 2)
    )
    assert local == (
        (40, 2, 2, ((1, 16), (), ())),
        (0, 3, 3, ((1, 4, 16), (1,), ())),
        (1, 3, 3, ((4, 16), (16,), ())),
        (2, 2, 2, ((1,), (), ())),
    )

    # Complementary wrapping-marker calibration.  The largest cube root
    # 16 ending at cut 1 starts at cut 35.  The forced copied marker is
    # exactly failed 3-cut 33: it has no cube in this near-model.
    outer_root = 16
    cube_start = 35
    overlap = 3 * outer_root - len(Q41)
    outer_word = tuple(
        Q41[(cube_start + offset) % len(Q41)]
        for offset in range(outer_root)
    )
    internal_cut = (
        cube_start + 2 * outer_root + overlap
    ) % len(Q41)
    assert overlap == 7
    assert outer_word[:overlap] == outer_word[-overlap:]
    assert outer_word[overlap] == 3
    assert internal_cut == 33
    assert Q41[internal_cut] == 3
    assert word_power_root_lengths(Q41, internal_cut, 3) == ()

    return {
        "word": "".join(map(str, Q41)),
        "profile": "".join(map(str, profile)),
        "mismatches": mismatches,
        "component_roots": component_roots,
        "local": local,
        "wrapping_marker": (
            cube_start,
            outer_root,
            overlap,
            internal_cut,
        ),
    }


def main() -> None:
    print("Q35=" + repr(audit_q35()))
    print("Q41=" + repr(audit_q41()))


if __name__ == "__main__":
    main()
