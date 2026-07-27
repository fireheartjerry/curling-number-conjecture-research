"""Executed audits for the external-child midpoint reduction.

Run the A094004 total-orbit-length calibration before accepting this
output.  Every finite curling number below is evaluated by both
implementations in ``curling.py``.
"""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "research"))

from curling import curling_number, curling_number_reference  # noqa: E402
from check_cross_rank_tower_audit import (  # noqa: E402
    full_first_copy_fitting,
)
from check_critical_seed_induction import (  # noqa: E402
    primitive,
    proper_circular_profile,
)


Word = tuple[int, ...]


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def circular_power(
    word: Word,
    cut: int,
    root: int,
    exponent: int,
) -> bool:
    n = len(word)
    return all(
        word[(cut - block * root + offset) % n]
        == word[(cut - root + offset) % n]
        for block in range(2, exponent + 1)
        for offset in range(root)
    )


def shortest_square_root(word: Word, cut: int) -> int:
    return min(
        root
        for root in range(1, len(word))
        if circular_power(word, cut, root, 2)
    )


def minimal_suffix_at_least(word: Word, threshold: int) -> Word:
    for length in range(1, len(word) + 1):
        suffix = word[-length:]
        if exact_cn(suffix) >= threshold:
            return suffix
    raise AssertionError("the complete word meets the threshold")


def replay_to_second_copy(word: Word) -> None:
    state = word
    for phase, target in enumerate(word):
        value = exact_cn(state)
        assert value == target, (phase, value, target)
        state += (value,)
    assert state == word * 2


def phase_zero_carrier_audit(
    text: str,
    expected_square_root: int,
    expected_target: int,
    expected_carriers: tuple[tuple[int, int, str, str], ...],
) -> tuple[object, ...]:
    """Check the autonomous-one root and its matching reset carriers."""
    word = tuple(map(int, text))
    n = len(word)
    assert primitive(word)
    assert proper_circular_profile(word) == word
    assert full_first_copy_fitting(word)
    replay_to_second_copy(word)

    square_root = shortest_square_root(word, 0)
    assert square_root == expected_square_root
    root = word[-square_root:]
    assert exact_cn(root) == 1

    # This lifted midpoint is an actual state on the replay from ``word``.
    midpoint = (word * 2)[:-square_root]
    assert exact_cn(midpoint) == expected_target == root[0]

    observed = []
    for (
        threshold,
        expected_length,
        expected_text,
        expected_outputs,
    ) in expected_carriers:
        carrier = minimal_suffix_at_least(midpoint, threshold)
        assert len(carrier) == expected_length
        assert "".join(map(str, carrier)) == expected_text
        assert exact_cn(carrier) == threshold
        assert exact_cn(carrier[1:]) == threshold - 1
        assert carrier == carrier[: expected_length // threshold] * threshold

        state = carrier
        outputs = []
        for target in root:
            value = exact_cn(state)
            outputs.append(value)
            if value != target:
                break
            state += (value,)
        assert "".join(map(str, outputs)) == expected_outputs
        observed.append(
            (
                threshold,
                len(carrier),
                len(carrier) - square_root,
                "".join(map(str, outputs)),
            )
        )

    return (
        n,
        square_root,
        "".join(map(str, root)),
        tuple(observed),
    )


def q21_midpoint_cycle_audit() -> tuple[object, ...]:
    """Recompute the exact cycle and test proposed one-edge ranks."""
    word = tuple(map(int, "223222322232322232223"))
    n = len(word)
    assert proper_circular_profile(word) == word

    roots = tuple(shortest_square_root(word, cut) for cut in range(n))
    assert roots == (
        4, 4, 1, 3, 3, 1, 1, 7, 4, 1, 1,
        4, 4, 2, 2, 1, 1, 6, 6, 1, 1,
    )
    cycle = (0, 17, 11, 7)
    cycle_roots = tuple(roots[cut] for cut in cycle)
    assert cycle_roots == (4, 6, 4, 7)
    assert sum(cycle_roots) == n

    next_roots = cycle_roots[1:] + cycle_roots[:1]
    deficits = tuple(
        2 * next_root - root
        for root, next_root in zip(cycle_roots, next_roots)
    )
    assert deficits == (8, 2, 10, 1)
    assert all(deficit > 0 for deficit in deficits)

    # The root at each edge is an autonomous-one word, as required by
    # the shortest-square carrier lemma.
    root_values = []
    for cut, root_length in zip(cycle, cycle_roots):
        root_word = tuple(
            word[(cut - root_length + offset) % n]
            for offset in range(root_length)
        )
        root_values.append(exact_cn(root_word))
    assert tuple(root_values) == (1, 1, 1, 1)

    return cycle, cycle_roots, deficits, sum(cycle_roots) // n


def main() -> None:
    q21 = phase_zero_carrier_audit(
        "223222322232322232223",
        expected_square_root=4,
        expected_target=2,
        expected_carriers=((2, 12, "232223232223", "2223"),),
    )
    adjacent_model = phase_zero_carrier_audit(
        "223222322322232223232",
        expected_square_root=2,
        expected_target=3,
        expected_carriers=(
            (2, 8, "22322232", "2"),
            (3, 12, "223222322232", "32"),
        ),
    )
    midpoint_cycle = q21_midpoint_cycle_audit()

    print("Q21_PHASE_ZERO_CARRIER=" + repr(q21))
    print("ADJACENT_PHASE_ZERO_CARRIERS=" + repr(adjacent_model))
    print("Q21_MIDPOINT_CYCLE=" + repr(midpoint_cycle))


if __name__ == "__main__":
    main()
