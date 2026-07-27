"""Executed certificates for the four terminal cube-root markers.

Every curling number is evaluated by both implementations in
``curling.py``.  The script also checks all proper borders, the forced
short rescue, its first standalone loss, and the four marker-parent
periods in the length-21 fixed profile.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference
from check_run_length_grammar import (
    binary_word,
    primitive,
    proper_profile,
    word_power_root_lengths,
)


TERMINAL_ROOTS = (
    (2,),
    (2, 3),
    (2, 2, 3),
    (2, 2, 2, 3),
)


def exact_cn(word: tuple[int, ...]) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def borders(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        length
        for length in range(1, len(word))
        if word[:length] == word[-length:]
    )


def maximizing_roots(word: tuple[int, ...]) -> tuple[int, ...]:
    """All root lengths attaining the (nontrivial) curling number."""
    value = exact_cn(word)
    assert value >= 2
    return tuple(
        root
        for root in range(1, len(word) // value + 1)
        if word[-value * root :] == word[-root:] * value
    )


def guaranteed_unary_leaf_offsets_in_cube(
    root: tuple[int, ...],
    cube_end_offset: int,
) -> tuple[int, ...]:
    """Terminal 22232 leaf endpoints wholly certified inside root^3."""
    q = len(root)
    cube_start = cube_end_offset - 3 * q
    marker = tuple(map(int, "22232"))
    out: list[int] = []
    for copy in range(3):
        for phase in range(q):
            if tuple(
                root[(phase + offset) % q] for offset in range(-3, 2)
            ) != marker:
                continue
            leaf = cube_start + copy * q + phase
            if leaf - 3 >= cube_start and leaf + 2 <= cube_end_offset:
                out.append(leaf)
    return tuple(sorted(out))


def internal_profile_violations(
    root: tuple[int, ...],
) -> tuple[tuple[int, int, int], ...]:
    """Cuts of root^3 where its internal suffix power exceeds the label."""
    cube = root * 3
    out = []
    for cut in range(1, len(cube)):
        value = exact_cn(cube[:cut])
        if value > cube[cut]:
            out.append((cut, value, cube[cut]))
    return tuple(out)


def advance_until_loss_or_larger_cube(
    word: tuple[int, ...],
    parent_root_length: int,
) -> tuple[str, tuple[int, ...], tuple[int, ...]]:
    """Execute locally until cn=1 or a cube root exceeds the parent."""
    appended: list[int] = []
    while True:
        value = exact_cn(word)
        if value == 1:
            return "loss", tuple(appended), word
        assert value in (2, 3)
        if value == 3 and any(
            root > parent_root_length for root in maximizing_roots(word)
        ):
            return "larger-cube", tuple(appended), word
        appended.append(value)
        word += (value,)


def first_loss_from_short_rescue(
    marker: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Return (appended labels, first state whose curling number is 1)."""
    root = marker[1:]
    state = root * 2
    appended: list[int] = []
    while True:
        value = exact_cn(state)
        if value == 1:
            return tuple(appended), state
        appended.append(value)
        state += (value,)


def main() -> None:
    markers: list[tuple[int, ...]] = []
    for root in TERMINAL_ROOTS:
        marker = root * 3 + (3, 2)
        markers.append(marker)
        assert marker[0] == marker[-1] == 2
        assert borders(marker) == (1,)
        assert exact_cn(marker) == 1

        short_root = marker[1:]
        assert (short_root * 2)[-len(marker):] == marker
        assert exact_cn(short_root * 2) == 2

        appended, loss = first_loss_from_short_rescue(marker)
        print(
            f"U={''.join(map(str, root))} "
            f"T={''.join(map(str, marker))} |T|={len(marker)} "
            f"short={len(short_root)} "
            f"short-appended={''.join(map(str, appended)) or '-'} "
            f"loss-length={len(loss)} loss-borders={borders(loss)}"
        )

    assert tuple(len(marker) for marker in markers) == (5, 8, 11, 14)
    assert tuple(
        first_loss_from_short_rescue(marker)[0] for marker in markers
    ) == (
        tuple(map(int, "223232223222322322232223232223222322322232223232223222332")),
        tuple(map(int, "223")),
        tuple(map(int, "223")),
        tuple(map(int, "22322232223323")),
    )
    assert tuple(
        borders(first_loss_from_short_rescue(marker)[1])
        for marker in markers
    ) == ((1,), (1,), (2,), ())

    # The length-21 fixed profile realizes all four long marker-parent
    # periods for T=22232, together with the forced short root four.
    q21 = binary_word(tuple(map(int, "133233")))
    t = markers[0]
    data = tuple(
        (cut, word_power_root_lengths(q21, cut, 2))
        for cut in range(len(q21))
        if tuple(
            q21[(cut - len(t) + offset) % len(q21)]
            for offset in range(len(t))
        )
        == t
    )
    assert data == (
        (1, (4, 11)),
        (7, (6,)),
        (11, (4, 10)),
        (18, (4, 7)),
    )
    print(f"Q21 T-marker square roots={data}")
    assert proper_profile(q21) == q21

    # Contextual terminal transition table.  If p is globally maximal,
    # every state here has length greater than 3p.  Consequently an
    # ambient raise from its standalone value 2 to 3 would itself require
    # a cube root longer than p.  The only unresolved standalone losses
    # are therefore the two explicitly rescued by their proper borders.
    expected_first = {
        (2,): ("larger-cube", "2232", 12, (4,)),
        (2, 3): ("loss", "223", 17, ()),
        (2, 2, 3): ("loss", "223", 23, ()),
        (2, 2, 2, 3): (
            "larger-cube",
            "2232223222332",
            39,
            (13,),
        ),
    }
    loss_rescues = {
        (2, 3): (1, 16, "2223222", 39, (1, 4)),
        (2, 2, 3): (2, 21, "2223222", 49, (1, 4)),
    }
    exposed_roots = {
        (2,): tuple(map(int, "2232")),
        (2, 3): tuple(map(int, "3222")),
        (2, 2, 3): tuple(map(int, "3222")),
        (2, 2, 2, 3): tuple(map(int, "2232223222332")),
    }
    exposed_unary_phases = {
        (2,): 2,
        (2, 3): 0,
        (2, 2, 3): 0,
        (2, 2, 2, 3): 2,
    }
    exposed_cube_end_offsets = {
        (2,): 6,
        (2, 3): 12,
        (2, 2, 3): 12,
        (2, 2, 2, 3): 15,
    }
    exposed_guaranteed_leaves = {
        (2,): (0, 4),
        (2, 3): (4, 8),
        (2, 2, 3): (4, 8),
        (2, 2, 2, 3): (-18, -9, -5, 4, 8),
    }
    for root, marker in zip(TERMINAL_ROOTS, markers):
        p = len(root)
        short_square = marker[1:] * 2
        assert len(short_square) > 3 * p
        outcome, appended, state = advance_until_loss_or_larger_cube(
            short_square, p
        )
        expected_outcome, expected_appended, expected_length, expected_roots = (
            expected_first[root]
        )
        assert outcome == expected_outcome
        assert appended == tuple(map(int, expected_appended))
        assert len(state) == expected_length
        if outcome == "larger-cube":
            assert maximizing_roots(state) == expected_roots
            exposed = exposed_roots[root]
            assert state[-3 * len(exposed) :] == exposed * 3
            # The certified phase of the exposed root's third copy is
            # a unary terminal cube, with its complete 22232 marker.
            phase = exposed_unary_phases[root]
            assert tuple(
                exposed[(phase + offset) % len(exposed)]
                for offset in range(-3, 2)
            ) == tuple(map(int, "22232"))
            assert guaranteed_unary_leaf_offsets_in_cube(
                exposed, exposed_cube_end_offsets[root]
            ) == exposed_guaranteed_leaves[root]
            print(
                f"terminal-transition U={''.join(map(str, root))} "
                f"short-square -> append {expected_appended} -> "
                f"larger cube roots {expected_roots} -> "
                f"unary terminal child at exposed phase {phase}"
            )
            continue

        assert exact_cn(state) == 1
        border, rescue_root, expected_appended, expected_length, expected_roots = (
            loss_rescues[root]
        )
        assert borders(state) == (border,)
        assert rescue_root == len(state) - border
        rescued_square = state[border:] * 2
        assert len(rescued_square) > 3 * p
        outcome, appended, final_state = advance_until_loss_or_larger_cube(
            rescued_square, p
        )
        assert outcome == "larger-cube"
        assert appended == tuple(map(int, expected_appended))
        assert len(final_state) == expected_length
        assert maximizing_roots(final_state) == expected_roots
        exposed = exposed_roots[root]
        assert final_state[-3 * len(exposed) :] == exposed * 3
        phase = exposed_unary_phases[root]
        assert tuple(
            exposed[(phase + offset) % len(exposed)]
            for offset in range(-3, 2)
        ) == tuple(map(int, "22232"))
        assert guaranteed_unary_leaf_offsets_in_cube(
            exposed, exposed_cube_end_offsets[root]
        ) == exposed_guaranteed_leaves[root]
        print(
            f"terminal-transition U={''.join(map(str, root))} "
            f"short-square -> loss borders={(border,)} -> "
            f"root {rescue_root} square -> append {expected_appended} -> "
            f"larger cube roots {expected_roots} -> "
            f"unary terminal child at exposed phase {phase}"
        )

    # Exhaust every proper-border cube interruption of the unary short
    # branch.  ``offset`` is the terminal unary child's endpoint minus
    # the source leaf endpoint.
    unary_root = tuple(map(int, "2232"))
    unary_outputs = tuple(map(int, "2232"))
    interruption_table = {}
    for step in (0, 1, 3):
        state = unary_root * 2 + unary_outputs[:step]
        assert exact_cn(state) == 2
        entries = []
        for border in borders(state):
            root_length = len(state) - border
            if 3 * root_length <= len(state):
                continue
            cube_root = state[-root_length:]
            # A nonprimitive cube root would expose exponent at least
            # six at a binary-profile cut, so it is not an admissible
            # maximizing interruption.
            if not primitive(cube_root):
                continue
            phases = tuple(
                phase
                for phase in range(root_length)
                if phase + 1 < root_length
                if tuple(
                    cube_root[(phase + offset) % root_length]
                    for offset in range(-3, 2)
                )
                == tuple(map(int, "22232"))
            )
            endpoint_offsets = tuple(
                2 + step - root_length + phase for phase in phases
            )
            boundary_double_offsets = tuple(
                2 + step - root_length + phase
                for phase in range(root_length)
                if phase + 1 == root_length
                and tuple(
                    cube_root[(phase + offset) % root_length]
                    for offset in range(-3, 1)
                )
                == tuple(map(int, "2223"))
            )
            entries.append(
                (
                    root_length,
                    "".join(map(str, cube_root)),
                    phases,
                    endpoint_offsets,
                    boundary_double_offsets,
                )
            )
        interruption_table[step] = tuple(entries)
    assert interruption_table == {
        0: (
            (7, "2322232", (5,), (0,), ()),
            (4, "2232", (2,), (0,), ()),
        ),
        1: (
            (7, "3222322", (4,), (0,), ()),
            (4, "2322", (1,), (0,), ()),
        ),
        3: (
            (4, "2223", (), (), (4,)),
        ),
    }
    assert {
        (0, 7): guaranteed_unary_leaf_offsets_in_cube(
            tuple(map(int, "2322232")), 2
        ),
        (0, 4): guaranteed_unary_leaf_offsets_in_cube(
            tuple(map(int, "2232")), 2
        ),
        (1, 7): guaranteed_unary_leaf_offsets_in_cube(
            tuple(map(int, "3222322")), 3
        ),
        (1, 4): guaranteed_unary_leaf_offsets_in_cube(
            tuple(map(int, "2322")), 3
        ),
        (3, 4): guaranteed_unary_leaf_offsets_in_cube(
            tuple(map(int, "2223")), 5
        ),
    } == {
        (0, 7): (-14, -7, 0),
        (0, 4): (-4, 0),
        (1, 7): (-14, -7, 0),
        (1, 4): (-4, 0),
        (3, 4): (-4, 0),
    }
    completed = unary_root * 2 + unary_outputs
    assert exact_cn(completed) == 3
    assert maximizing_roots(completed) == (4,)
    assert completed[-12:] == unary_root * 3
    print(f"unary-short-branch cube interruptions={interruption_table}")

    # Exact Q21 realization of the unary endpoint graph.
    unary_leaves = tuple(
        cut
        for cut in range(len(q21))
        if tuple(
            q21[(cut + offset) % len(q21)]
            for offset in range(-3, 2)
        )
        == tuple(map(int, "22232"))
    )
    assert unary_leaves == (5, 9, 16, 20)
    q21_graph = {
        5: ("long-square", 6, 20),
        9: ("step-1-cube-return", 4, 9),
        16: ("completed-short", 4, 20),
        20: ("marker-cube-return", 4, 20),
    }
    assert word_power_root_lengths(q21, 7, 2) == (6,)
    assert word_power_root_lengths(q21, 11, 2) == (4, 10)
    assert word_power_root_lengths(q21, 12, 3) == (4,)
    assert tuple(q21[(18 + step) % len(q21)] for step in range(4)) == (
        2,
        2,
        3,
        2,
    )
    assert word_power_root_lengths(q21, 1, 3) == (4,)
    print(f"Q21 unary endpoint graph={q21_graph}")

    # Three unary markers four positions apart force a cube at the
    # following 2-labelled cut.
    gap_four_triple = tuple(map(int, "2223")) * 3
    assert exact_cn(gap_four_triple) == 3
    assert tuple(
        cut
        for cut in range(3, len(gap_four_triple))
        if gap_four_triple[cut - 3 : cut] == (2, 2, 2)
        and gap_four_triple[cut] == 3
    ) == (3, 7, 11)
    assert gap_four_triple + (2,) == tuple(map(int, "2223222322232"))
    print("gap-four triple forces root-4 cube before appended label 2")

    # Exact overlap geometry for one marker and for an atomic gap-four
    # pair.  Shifts one through three would require a nonexistent marker
    # border; shift four is the sole permitted overlap.
    unary_marker = tuple(map(int, "22232"))
    assert borders(unary_marker) == (1,)
    assert tuple(
        shift
        for shift in range(1, len(unary_marker))
        if unary_marker[shift:] == unary_marker[:-shift]
    ) == (4,)
    gap_four_pair = tuple(map(int, "222322232"))
    assert (
        gap_four_pair[: len(unary_marker)] == unary_marker
        and gap_four_pair[-len(unary_marker) :] == unary_marker
    )
    assert gap_four_pair + tuple(map(int, "2232")) == (
        gap_four_triple + (2,)
    )

    # From a pair {c-4,c}, a marker-parent displacement q=5,6,7
    # creates a forbidden endpoint distance q-4 in {1,2,3}; q=8
    # creates the forbidden triple {c-8,c-4,c}.  Every q>=9 contains
    # the complete nine-symbol pair in the last root block.
    assert tuple(q - 4 for q in range(5, 8)) == (1, 2, 3)
    assert tuple(-q for q in (8,)) + (-4, 0) == (-8, -4, 0)
    assert len(gap_four_pair) == 9
    assert gap_four_pair[:-1] == tuple(map(int, "2223")) * 2
    assert exact_cn(gap_four_pair[:-1]) == 2
    assert maximizing_roots(gap_four_pair[:-1]) == (4,)
    assert tuple(
        (
            length,
            exact_cn(gap_four_pair[-length:]),
            borders(gap_four_pair[-length:]),
        )
        for length in range(1, len(gap_four_pair) + 1)
    ) == (
        (1, 1, ()),
        (2, 1, ()),
        (3, 1, (1,)),
        (4, 1, (1,)),
        (5, 1, (1,)),
        (6, 1, (2,)),
        (7, 1, (1, 3)),
        (8, 2, (1, 4)),
        (9, 2, (1, 5)),
    )

    # The q=4 branch based at the right endpoint cannot use a q=7
    # interruption: its companion at offset -7 lies three positions
    # from the existing left endpoint -4.  A q=4 interruption returns
    # exactly to that pair, while completion would create a third
    # gap-four leaf.
    assert (-7) - (-4) == -3
    assert (-4, 0) == guaranteed_unary_leaf_offsets_in_cube(
        tuple(map(int, "2232")), 2
    )
    assert (-4, 0, 4) == tuple(range(-4, 5, 4))

    # Exhaust the roots which can interrupt the three value-two states.
    # A root shorter than the state is determined by a proper border.
    # The length-eight candidates are nonprimitive squares.
    branch_states = {
        step: unary_root * 2 + unary_outputs[:step]
        for step in (0, 1, 3)
    }
    assert {
        step: borders(state) for step, state in branch_states.items()
    } == {
        0: (1, 4),
        1: (1, 2, 5),
        3: (3, 7),
    }
    assert branch_states[0] == tuple(map(int, "22322232"))
    assert branch_states[1] == tuple(map(int, "223222322"))
    assert branch_states[3] == tuple(map(int, "22322232223"))
    assert not primitive(branch_states[0])
    assert not primitive(branch_states[1][-8:])
    assert not primitive(branch_states[3][-8:])

    # The only one-letter external cube masks which fail to copy the
    # complete gap-four pair are locally incompatible with the exact
    # 2/3 profile.
    assert internal_profile_violations(tuple(map(int, "223222322"))) == (
        (10, 3, 2),
        (11, 4, 3),
        (19, 3, 2),
        (20, 4, 3),
    )
    assert internal_profile_violations(tuple(map(int, "22322232223"))) == (
        (12, 3, 2),
        (23, 3, 2),
    )
    assert internal_profile_violations(tuple(map(int, "222322232"))) == (
        (11, 3, 2),
        (12, 4, 3),
        (20, 3, 2),
        (21, 4, 3),
    )
    # Coordinate audit.  With right source endpoint c, A_1 ends at
    # c+3 and its q=9 cube begins at c-24, so violation cut 20 is c-4.
    # A_3 ends at c+5 and its q=11 cube begins at c-28, so cut 23 is
    # c-5.  The full-pair q=9 cube at A_0 begins at c-25, making cut
    # 21 the existing left endpoint c-4.
    c = 100
    assert (c + 3 - 3 * 9) + 20 == c - 4
    assert (c + 5 - 3 * 11) + 23 == c - 5
    assert (c + 2 - 3 * 9) + 21 == c - 4
    print("gap-four one-letter cube masks have internal profile violations")

    # Q64 is the exact obstruction to treating every square root longer
    # than the global cube scale as a pair-parent edge at its endpoint.
    # Its long squares transport complete internal pairs with unchanged
    # continuation labels; they do not end at a pair.  The three missing
    # positive profile equations are therefore load-bearing.
    bridge_root = q21[16:] + q21[:16]
    q64 = bridge_root * 3 + (3,)
    q64_profile = proper_profile(q64)
    assert tuple(
        cut
        for cut, (label, value) in enumerate(zip(q64, q64_profile))
        if label != value
    ) == (2, 6, 11)
    assert max(
        root
        for cut in range(len(q64))
        for root in word_power_root_lengths(q64, cut, 3)
    ) == 21
    pair_word = tuple(map(int, "222322232"))
    q64_pairs = tuple(
        endpoint
        for endpoint in range(len(q64))
        if tuple(
            q64[(endpoint - len(pair_word) + offset) % len(q64)]
            for offset in range(len(pair_word))
        )
        == pair_word
    )
    assert q64_pairs == (16, 27, 37, 48, 58)
    long_exact_two_squares = tuple(
        (cut, word_power_root_lengths(q64, cut, 2))
        for cut in range(len(q64))
        if q64[cut] == q64_profile[cut] == 2
        and any(
            root > 21
            for root in word_power_root_lengths(q64, cut, 2)
        )
    )
    assert long_exact_two_squares == (
        (22, (7, 22)),
        (43, (7, 21, 43)),
    )
    transported_pairs = {
        (22, 22): ((16, 58),),
        (43, 43): ((16, 37), (27, 48), (37, 58)),
    }
    for (cut, root), mappings in transported_pairs.items():
        for source, target in mappings:
            assert cut - root < source <= cut
            assert (source - root) % len(q64) == target
            assert source in q64_pairs and target in q64_pairs
            assert q64[source] == q64[target]
    assert all(cut not in q64_pairs for cut, _ in long_exact_two_squares)
    print(
        "Q64 long-square internal pair transport obstruction="
        f"{long_exact_two_squares}"
    )


if __name__ == "__main__":
    main()
