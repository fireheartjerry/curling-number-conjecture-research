"""Exhaust the necessary local graph when every relevant root is <= 5.

For a binary exact circular profile whose largest low-square root is at
most R, the cube-to-low-square bridge bounds every cube root by R.  A
length-4R suffix at each cut must therefore satisfy:

* at least one square of root 1..R ends there;
* the next displayed bit is 3 iff one of those cube roots exists;
* no fourth power of one of those roots exists.

The functional graph of these necessary suffix transitions is a
supergraph of every such circular profile.  This script checks R=5
exhaustively using integer suffix masks and a three-color DFS.
"""

from __future__ import annotations


ROOT_MAX = 5
WINDOW = 4 * ROOT_MAX
STATE_COUNT = 1 << WINDOW
STATE_MASK = STATE_COUNT - 1

REPEAT_MASK = {
    (root, exponent): sum(
        1 << (copy * root)
        for copy in range(exponent)
    )
    for root in range(1, ROOT_MAX + 1)
    for exponent in (2, 3, 4)
}


def ends_power(state: int, root: int, exponent: int) -> bool:
    block = state & ((1 << root) - 1)
    powered_suffix = state & ((1 << (root * exponent)) - 1)
    return powered_suffix == block * REPEAT_MASK[root, exponent]


def transition(state: int) -> int:
    has_square = any(
        ends_power(state, root, 2)
        for root in range(1, ROOT_MAX + 1)
    )
    has_fourth = any(
        ends_power(state, root, 4)
        for root in range(1, ROOT_MAX + 1)
    )
    if not has_square or has_fourth:
        return -1
    has_cube = any(
        ends_power(state, root, 3)
        for root in range(1, ROOT_MAX + 1)
    )
    output_bit = 1 if has_cube else 0
    return ((state << 1) & STATE_MASK) | output_bit


def main() -> None:
    successor = [transition(state) for state in range(STATE_COUNT)]
    locally_admissible = sum(next_state >= 0 for next_state in successor)
    retained_edges = sum(
        next_state >= 0 and successor[next_state] >= 0
        for next_state in successor
    )

    color = bytearray(STATE_COUNT)

    def visit(start: int) -> None:
        path: list[int] = []
        path_index: dict[int, int] = {}
        state = start
        while (
            state >= 0
            and successor[state] >= 0
            and color[state] == 0
            and state not in path_index
        ):
            path_index[state] = len(path)
            path.append(state)
            state = successor[state]
        if state in path_index:
            raise AssertionError(
                ("directed cycle", tuple(path[path_index[state] :]))
            )
        for member in path:
            color[member] = 2

    for state in range(STATE_COUNT):
        if color[state] == 0 and successor[state] >= 0:
            visit(state)

    assert STATE_COUNT == 1_048_576
    assert locally_admissible == 614_692
    assert retained_edges == 396_764

    print(
        {
            "root_max": ROOT_MAX,
            "window": WINDOW,
            "states": STATE_COUNT,
            "locally_admissible": locally_admissible,
            "retained_edges": retained_edges,
            "directed_cycles": 0,
        }
    )


if __name__ == "__main__":
    main()
