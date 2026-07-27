"""A primitive child with an internal cube that is not first-copy fitting.

This checks the precise distinction used in
``child_profile_inheritance_audit.md``.  The root-4 cube is a proper
circular witness at phase zero of the primitive length-11 word, and the
proper profile there is exactly three.  Its span is twelve, exceeding
the length-ten deleted first-copy suffix available at that phase.
"""

from __future__ import annotations

from check_run_length_grammar import (
    primitive,
    proper_profile,
    word_power_root_lengths,
)


V = tuple(map(int, "32223222322"))
PHASE = 0
ROOT = 4
EXPONENT = 3


def circular_suffix(word: tuple[int, ...], cut: int, length: int) -> tuple[int, ...]:
    return tuple(word[(cut - length + offset) % len(word)] for offset in range(length))


def main() -> None:
    q = len(V)
    roots = word_power_root_lengths(V, PHASE, EXPONENT)
    suffix = circular_suffix(V, PHASE, EXPONENT * ROOT)
    root_word = suffix[:ROOT]

    assert q == 11
    assert primitive(V)
    assert roots == (ROOT,)
    assert suffix == root_word * EXPONENT
    assert proper_profile(V)[PHASE] == EXPONENT
    assert EXPONENT * ROOT == 12
    assert q + PHASE - 1 == 10
    assert EXPONENT * ROOT > q + PHASE - 1

    print(
        {
            "V": "".join(map(str, V)),
            "length": q,
            "primitive": True,
            "phase": PHASE,
            "proper_profile_at_phase": proper_profile(V)[PHASE],
            "cube_roots": roots,
            "cube_root_word": "".join(map(str, root_word)),
            "cube_suffix": "".join(map(str, suffix)),
            "powered_span": EXPONENT * ROOT,
            "deleted_first_copy_capacity": q + PHASE - 1,
            "first_copy_fitting": False,
        }
    )


if __name__ == "__main__":
    main()
