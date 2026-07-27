"""Executed certificate for the exact origin-zero re-entry branch.

The model uses the known primitive replay word

    R = 223222322232322232223

and its prefix Q^3 3 with Q = 2232.  It checks every numerical curling
number with both implementations in ``curling.py``.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from curling import curling_number, curling_number_reference


def cn(word: tuple[int, ...]) -> int:
    """Evaluate with the two independent implementations."""
    fast = curling_number(word)
    slow = curling_number_reference(word)
    assert fast == slow
    return fast


def is_primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return all(
        n % p != 0 or word != word[:p] * (n // p)
        for p in range(1, n)
    )


def maximizing_roots(
    word: tuple[int, ...],
) -> list[tuple[int, int]]:
    """Return (primitive root length, power origin) for all maximizing roots."""
    exponent = cn(word)
    n = len(word)
    roots: list[tuple[int, int]] = []
    for p in range(1, n // exponent + 1):
        root = word[-p:]
        if word[-exponent * p :] == root * exponent and is_primitive(root):
            roots.append((p, n - exponent * p))
    return roots


def anchored_powers(
    word: tuple[int, ...],
) -> list[tuple[int, int]]:
    """Return all (exponent, root length) powers occupying the whole word."""
    n = len(word)
    result: list[tuple[int, int]] = []
    for exponent in range(2, n + 1):
        if n % exponent:
            continue
        p = n // exponent
        if word == word[:p] * exponent:
            result.append((exponent, p))
    return result


def main() -> None:
    q_word = tuple(map(int, "2232"))
    r_word = tuple(map(int, "223222322232322232223"))
    q = len(q_word)
    r = len(r_word)
    promoted = q_word * 3 + (3,)
    tower_prefix = r_word * 3

    assert is_primitive(q_word)
    assert is_primitive(r_word)
    assert r_word[: len(promoted)] == promoted

    # The post-promotion state has only one primitive maximizing root.  Its
    # complete square begins strictly to the right of coordinate zero.
    assert cn(promoted) == 2
    assert maximizing_roots(promoted) == [(2, 9)]

    # R is a full replay word through its third copy.
    for copies in (1, 2):
        for phase in range(r):
            state = r_word * copies + r_word[:phase]
            assert cn(state) == r_word[phase]
    assert cn(r_word * 2) == 2
    assert cn(r_word * 3) == 3

    # From just after Q^3 3 through R^3, the first complete power whose
    # origin is coordinate zero is exactly the square R^2.
    anchored: list[tuple[int, list[tuple[int, int]]]] = []
    for end in range(len(promoted), 3 * r + 1):
        powers = anchored_powers(tower_prefix[:end])
        if powers:
            anchored.append((end, powers))
    assert anchored == [(2 * r, [(2, r)]), (3 * r, [(3, r)])]

    # Minimum origins among maximizing roots fall 9 -> 5 -> 1 -> 0.
    record_origins: list[tuple[int, int]] = []
    best = len(promoted) + 1
    for end in range(len(promoted), 2 * r + 1):
        origin = min(origin for _, origin in maximizing_roots(tower_prefix[:end]))
        if origin < best:
            record_origins.append((end, origin))
            best = origin
    assert record_origins == [(13, 9), (17, 5), (21, 1), (42, 0)]

    # Adjacent-cut laminar branch.  The old state ends in 2^3 at origin 38;
    # appending its label 3 closes the much larger boundary square R^2.
    old_end = 2 * r - 1
    assert cn(tower_prefix[:old_end]) == 3
    assert maximizing_roots(tower_prefix[:old_end]) == [(1, 38)]
    assert tower_prefix[old_end] == 3
    assert cn(tower_prefix[: old_end + 1]) == 2
    assert maximizing_roots(tower_prefix[: old_end + 1]) == [
        (4, 34),
        (10, 22),
        (21, 0),
    ]
    assert 2 * r == 3 * 1 + 38 + 1

    # Root-episode coordinates.  The preceding 2-event is two cuts earlier,
    # so the length-r square is a crossing birth with R = F D.
    two_events = [
        end
        for end in range(1, 2 * r)
        if cn(tower_prefix[:end]) == 2
    ]
    previous_two_event = two_events[-1]
    d = 2 * r - previous_two_event
    f = r - d
    assert previous_two_event == 40
    assert d == 2 and f == 19
    assert cn(tower_prefix[:f]) == 2
    first = r_word[:f]
    second = r_word[f:]
    assert r_word * 2 == first + second + first + second

    # The subsequent cube is the fixed-origin, equal-root maturation.
    assert maximizing_roots(tower_prefix[: 3 * r]) == [(r, 0)]
    assert 2 * r - 2 * r == 3 * r - 3 * r == 0

    print(f"Q={''.join(map(str, q_word))} q={q}")
    print(f"R={''.join(map(str, r_word))} r={r}")
    print(
        "post_promotion="
        f"cn:{cn(promoted)} roots_origins:{maximizing_roots(promoted)}"
    )
    print(f"record_origins={record_origins}")
    print(
        "adjacent_reentry="
        f"old_end:{old_end} old_cn:3 old_root_origin:(1,38) "
        f"new_end:{2*r} new_cn:2 new_root_origin:(21,0)"
    )
    print(
        "root_episode="
        f"previous_2_event:{previous_two_event} gap:{d} "
        f"birth:crossing F_length:{f} D_length:{d}"
    )
    print("anchored_powers=" + repr(anchored))


if __name__ == "__main__":
    main()
