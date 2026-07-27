"""Copy-parent graph helpers for curling-number orbit experiments.

Positions are zero based.  If the seed has length ``n``, the symbol appended
at orbit time ``t`` occupies position ``n + t`` in the infinite orbit word.
For an orbit that has not reached curling number one, the prefix ending at
that position has a powered suffix.  Its shortest maximizing root determines
the canonical parent of the appended position.
"""

from dataclasses import dataclass

from curling import curling_number


def shortest_maximizing_root_length(sequence):
    """Return the least root length attaining ``curling_number(sequence)``."""
    sequence = tuple(sequence)
    exponent = curling_number(sequence)
    for root_length in range(1, len(sequence) // exponent + 1):
        root = sequence[-root_length:]
        if sequence[-exponent * root_length :] == root * exponent:
            return root_length
    raise AssertionError("the final term always supplies an exponent-one root")


def maximizing_root_lengths(sequence):
    """Return every root length attaining the curling number."""
    sequence = tuple(sequence)
    exponent = curling_number(sequence)
    return tuple(
        root_length
        for root_length in range(1, len(sequence) // exponent + 1)
        if sequence[-exponent * root_length :]
        == sequence[-root_length:] * exponent
    )


@dataclass(frozen=True)
class AppendedVertex:
    time: int
    position: int
    value: int
    next_exponent: int
    parent: int
    span: int


def finite_orbit_prefix(seed, step_limit):
    """Return states and appended values, stopping before the first one."""
    state = tuple(seed)
    states = []
    values = []
    for _ in range(step_limit):
        value = curling_number(state)
        states.append(state)
        if value == 1:
            break
        values.append(value)
        state += (value,)
    return states, tuple(values)


def canonical_vertices(seed, step_limit):
    """Build every canonical parent whose following state still has cn >= 2."""
    seed = tuple(seed)
    states, values = finite_orbit_prefix(seed, step_limit + 1)
    vertices = []
    for time in range(min(len(values), len(states) - 1)):
        following_state = states[time + 1]
        next_exponent = curling_number(following_state)
        if next_exponent == 1:
            break
        span = shortest_maximizing_root_length(following_state)
        position = len(seed) + time
        vertices.append(
            AppendedVertex(
                time=time,
                position=position,
                value=values[time],
                next_exponent=next_exponent,
                parent=position - span,
                span=span,
            )
        )
    return tuple(vertices)
