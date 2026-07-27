"""Finite-state certificate excluding a binary replay with fitting roots <= 4.

For a binary fixed profile with full first-copy fitting, if every fitting
square root has length at most four, the next symbol is determined by the
last sixteen symbols:

* some square of root length 1..4 must end at the cut;
* the next symbol is 3 exactly when a cube of root length 1..4 ends there;
* no fourth power of root length 1..4 may end there.

The functional graph on all 2^16 suffixes is checked exhaustively.
"""

from __future__ import annotations

from itertools import product


Word = tuple[int, ...]
WINDOW = 16
ROOT_MAX = 4


def ends_power(word: Word, root: int, exponent: int) -> bool:
    span = root * exponent
    if span > len(word):
        return False
    block = word[-root:]
    return word[-span:] == block * exponent


def transition(state: Word) -> Word | None:
    has_square = any(
        ends_power(state, root, 2)
        for root in range(1, ROOT_MAX + 1)
    )
    has_cube = any(
        ends_power(state, root, 3)
        for root in range(1, ROOT_MAX + 1)
    )
    has_fourth = any(
        ends_power(state, root, 4)
        for root in range(1, ROOT_MAX + 1)
    )
    if not has_square or has_fourth:
        return None
    output = 3 if has_cube else 2
    return state[1:] + (output,)


states = tuple(product((2, 3), repeat=WINDOW))
successor = {
    state: next_state
    for state in states
    if (next_state := transition(state)) is not None
}
edges = {
    state: next_state
    for state, next_state in successor.items()
    if next_state in successor
}

# A three-color DFS is an independent cycle check; encountering gray would
# be an explicit directed cycle and refute the certificate.
color: dict[Word, int] = {}


def visit(state: Word) -> None:
    status = color.get(state, 0)
    if status == 1:
        raise AssertionError(("directed cycle", state))
    if status == 2:
        return
    color[state] = 1
    if state in edges:
        visit(edges[state])
    color[state] = 2


for state in edges:
    visit(state)

# Compute the exact longest surviving path after acyclicity is certified.
rank: dict[Word, int] = {}


def path_length(state: Word) -> int:
    if state not in edges:
        return 0
    if state not in rank:
        rank[state] = 1 + path_length(edges[state])
    return rank[state]


maximum_path = max(path_length(state) for state in successor)
assert len(states) == 65_536
assert len(successor) == 37_780
assert len(edges) == 23_904
assert maximum_path == 8

print(
    {
        "states": len(states),
        "locally_admissible": len(successor),
        "admissible_edges": len(edges),
        "directed_cycles": 0,
        "maximum_path": maximum_path,
    }
)
