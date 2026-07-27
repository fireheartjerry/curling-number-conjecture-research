"""Executable checks for the external-reset sibling-tail rank.

The displayed length-21 word is a complete critical replay root, not an
arbitrary common-prefix example.  It shows that proper-circular fixedness
and all finite replay/fitting equations do not imply the proposed sibling
inequality.  A literal earlier ``P^3 3`` marker is therefore load-bearing.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from curling import (  # noqa: E402
    curling_number,
    curling_number_reference,
    tail_length,
)
from research.check_critical_seed_induction import (  # noqa: E402
    maximizing_roots,
    primitive,
    proper_circular_maximizing_roots,
    proper_circular_profile,
)


Word = tuple[int, ...]


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def outputs_to_one(word: Word, limit: int = 1000) -> Word:
    outputs: list[int] = []
    for _ in range(limit):
        value = exact_cn(word)
        outputs.append(value)
        if value == 1:
            return tuple(outputs)
        word += (value,)
    raise RuntimeError("trace limit reached")


def literal_parent_lengths(word: Word) -> tuple[int, ...]:
    return tuple(
        p
        for p in range(1, (len(word) - 1) // 3 + 1)
        if word[: 3 * p] == word[:p] * 3 and word[3 * p] == 3
    )


def main() -> None:
    root = tuple(map(int, "223222322322232223232"))
    n = len(root)
    assert primitive(root)
    assert root[0] == 2
    assert proper_circular_profile(root) == root

    # This directly checks every finite synchronization/fitting equation:
    # from U, the orbit emits U twice and reaches U^3.
    replay_state = root
    replay_outputs: list[int] = []
    for _ in range(2 * n):
        value = exact_cn(replay_state)
        replay_outputs.append(value)
        replay_state += (value,)
    assert tuple(replay_outputs) == root * 2
    assert replay_state == root * 3
    assert exact_cn(replay_state) == 3

    deleted = replay_state[1:]
    assert exact_cn(deleted) == 2
    low_sibling = deleted + (2,)
    high_sibling = deleted + (3,)
    low_outputs = outputs_to_one(low_sibling)
    high_outputs = outputs_to_one(high_sibling)
    tau2 = tail_length(low_sibling, step_limit=1000)
    tau3 = tail_length(high_sibling, step_limit=1000)
    assert low_outputs == (3, 1)
    assert high_outputs == (3, 2, 1)
    assert (tau2, tau3) == (1, 2)
    assert tau3 > tau2

    parents = literal_parent_lengths(root)
    assert parents == ()

    # A partial nested SAT model demonstrates why every actual-prefix
    # equation matters.  It was constrained only through circular/replay
    # cut 64.  Its sibling order fails, but the first omitted cut 65 is
    # already incompatible with both the circular profile and the actual
    # finite orbit prefix.
    q21 = "223222322232322232223"
    near_text = (
        "2232223222323222322232232223222323222322232232223222323222322233"
        "2323333323333223322223322223322322232322232223323233333233332233"
        "222233222233"
    )
    near = tuple(map(int, near_text))
    assert len(near) == 140
    assert near_text.startswith(q21 * 3 + "3")
    near_profile = proper_circular_profile(near)
    assert near[65] == 3
    assert near_profile[65] == 1
    assert exact_cn(near[:65]) == 1
    near_deleted = (near * 3)[1:]
    near_tau2 = tail_length(near_deleted + (2,), step_limit=1000)
    near_tau3 = tail_length(near_deleted + (3,), step_limit=1000)
    assert (near_tau2, near_tau3) == (1, 2)

    # Actual parent-orbit ancestry without child criticality is also
    # insufficient.  This parent is an exact critical Q21 rotation.  Its
    # high and deleted post-promotion states emit the same 16-symbol word.
    parent = tuple(map(int, "223232223222322322232"))
    assert primitive(parent)
    assert proper_circular_profile(parent) == parent
    parent_state = parent
    for _ in range(2 * len(parent)):
        value = exact_cn(parent_state)
        assert value == parent[len(parent_state) % len(parent)]
        parent_state += (value,)
    assert parent_state == parent * 3
    assert exact_cn(parent_state) == 3
    parent_high = parent_state + (3,)
    parent_low = parent_state[1:] + (3,)
    actual_extension: list[int] = []
    for _ in range(16):
        high_value = exact_cn(parent_high)
        low_value = exact_cn(parent_low)
        assert high_value == low_value
        actual_extension.append(high_value)
        parent_high += (high_value,)
        parent_low += (low_value,)
    extension = tuple(actual_extension)
    assert extension == tuple(map(int, "2223222322322232"))

    ancestry_near = parent * 3 + (3,) + extension
    assert len(ancestry_near) == 80
    assert primitive(ancestry_near)
    assert exact_cn(ancestry_near * 3) == 3
    ancestry_deleted = (ancestry_near * 3)[1:]
    assert exact_cn(ancestry_deleted) == 2
    ancestry_tau2 = tail_length(
        ancestry_deleted + (2,), step_limit=1000
    )
    ancestry_tau3 = tail_length(
        ancestry_deleted + (3,), step_limit=1000
    )
    assert (ancestry_tau2, ancestry_tau3) == (7, 10)
    assert exact_cn(ancestry_deleted + (3, 2)) == 2

    ancestry_profile = proper_circular_profile(ancestry_near)
    first_bad_phase = next(
        phase
        for phase, (symbol, profile_value) in enumerate(
            zip(ancestry_near, ancestry_profile)
        )
        if symbol != profile_value
    )
    assert first_bad_phase == 38
    assert (
        ancestry_near[first_bad_phase],
        ancestry_profile[first_bad_phase],
    ) == (2, 3)
    assert proper_circular_maximizing_roots(
        ancestry_near, first_bad_phase
    ) == (len(parent),)

    replay_near = ancestry_near
    first_replay_failure = None
    for step in range(2 * len(ancestry_near)):
        value = exact_cn(replay_near)
        target = ancestry_near[step % len(ancestry_near)]
        if value != target:
            first_replay_failure = (step, target, value)
            break
        replay_near += (value,)
    assert first_replay_failure == (38, 2, 3)

    pointed = ancestry_deleted + (3, 2)
    assert maximizing_roots(pointed, exact_cn(pointed)) == (2, 17)
    pointed_records = tuple(
        (
            root_length,
            len(ancestry_near) - root_length,
            proper_circular_maximizing_roots(
                ancestry_near,
                len(ancestry_near) - root_length,
            ),
        )
        for root_length in (2, 17)
    )
    assert pointed_records == ((2, 78, (1,)), (17, 63, (21,)))

    print(f"critical_root={''.join(map(str, root))}")
    print(
        f"length={n} circular_profile_exact=true "
        f"replay_outputs={''.join(map(str, replay_outputs))}"
    )
    print(
        "sibling_order=(tau(D2),tau(D3)) "
        f"values=({tau2},{tau3}) "
        f"outputs2={''.join(map(str, low_outputs))} "
        f"outputs3={''.join(map(str, high_outputs))}"
    )
    print(f"literal_parent_lengths={parents}")
    print(
        "partial_nested_near_model="
        f"length={len(near)} first_omitted_cut=65 "
        f"symbol={near[65]} circular_value={near_profile[65]} "
        f"finite_prefix_value={exact_cn(near[:65])} "
        f"sibling_order=({near_tau2},{near_tau3})"
    )
    print(
        "actual_ancestry_near_model="
        f"parent_length={len(parent)} child_length={len(ancestry_near)} "
        f"extension={''.join(map(str, extension))} "
        f"sibling_order=({ancestry_tau2},{ancestry_tau3}) "
        f"first_child_failure={first_replay_failure} "
        f"pointed_roots={pointed_records}"
    )


if __name__ == "__main__":
    main()
