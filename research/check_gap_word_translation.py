"""Executed checks for the exact successive-2 gap translation."""

from __future__ import annotations

from itertools import product

from curling import curling_number, curling_number_reference


def encode(gaps: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x for d in gaps for x in (2,) + (3,) * (d - 1))


def maximizing_roots(word: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    value = curling_number(word)
    roots = tuple(
        p
        for p in range(1, len(word) // value + 1)
        if word[-value * p :] == word[-p:] * value
    )
    return value, roots


def decode_root(root: tuple[int, ...]):
    """Return (a,G,d), or None for a root containing no marker 2."""
    a = 0
    while a < len(root) and root[a] == 3:
        a += 1
    if a == len(root):
        return None
    assert root[a] == 2
    marked = root[a:]
    positions = [i for i, x in enumerate(marked) if x == 2] + [len(marked)]
    gaps = tuple(positions[i + 1] - positions[i] for i in range(len(positions) - 1))
    return a, gaps[:-1], gaps[-1]


def verify_translation(max_gap_length: int = 8) -> int:
    checked = 0
    for length in range(1, max_gap_length + 1):
        for gaps in product((1, 2, 3), repeat=length):
            raw = encode(gaps)
            assert curling_number(raw) == curling_number_reference(raw)
            for root_length in range(1, len(raw) // 2 + 1):
                root = raw[-root_length:]
                exponent = 1
                while (
                    (exponent + 1) * root_length <= len(raw)
                    and raw[-(exponent + 1) * root_length :] == root * (exponent + 1)
                ):
                    exponent += 1
                if exponent < 2 or 2 not in root:
                    continue
                a, G, d = decode_root(root)
                assert root == (3,) * a + encode(G + (d,))
                assert d + a <= 3
                pattern = (G + (d + a,)) * (exponent - 1) + G + (d,)
                if a == 0:
                    assert gaps[-len(pattern) :] == pattern
                else:
                    start = len(gaps) - len(pattern)
                    assert start >= 1
                    b = gaps[start - 1]
                    assert b >= a + 1
                    assert gaps[-(len(pattern) + 1) :] == (b,) + pattern
                checked += 1
    return checked


def orbit(seed: tuple[int, ...]) -> tuple[int, ...]:
    state = seed
    labels = []
    while True:
        value = curling_number(state)
        assert value == curling_number_reference(state)
        labels.append(value)
        if value == 1:
            return tuple(labels)
        state += (value,)


def pointed_birth_obstruction():
    seed = tuple(map(int, "23233223233223233"))
    labels = orbit(seed)
    assert labels == tuple(map(int, "2322231"))

    states = [seed]
    for value in labels[:-1]:
        states.append(states[-1] + (value,))

    values_and_roots = [maximizing_roots(state) for state in states]
    assert values_and_roots[0] == (2, (1, 6))
    assert values_and_roots[1][0] == 3
    assert values_and_roots[2] == (2, (3,))
    assert states[2][-6:] == tuple(map(int, "323323"))
    assert states[0][-4:] == tuple(map(int, "3233"))
    assert states[0][:-4][-1:] == (2,)  # not D=23

    assert values_and_roots[3] == (2, (2,))
    assert states[3][-4:] == tuple(map(int, "3232"))
    assert states[2][-3:] == tuple(map(int, "323"))
    assert states[2][:-3][-1:] == (3,)  # not D=2

    return labels, values_and_roots[:4]


def repeated_defects():
    seed = tuple(map(int, "23222323"))
    labels = orbit(seed)
    expected = tuple(
        map(int, "22232223223222322232322232223223222322232322232223223223321")
    )
    assert labels == expected
    pairs = ((13, 34), (17, 38), (22, 43), (26, 47), (30, 51))
    roots = {}
    for cut in {x for pair in pairs for x in pair}:
        state = seed + labels[:cut]
        value, lengths = maximizing_roots(state)
        assert value == 2
        pointed = []
        for p in lengths:
            if 2 * p > cut:
                continue
            root = labels[cut - p : cut]
            decoded = decode_root(root)
            if decoded is not None and decoded[0] > 0:
                pointed.append((p, root, decoded))
        roots[cut] = tuple(pointed)
    for left, right in pairs:
        assert roots[left] == roots[right]
    return tuple((left, right, roots[left]) for left, right in pairs)


if __name__ == "__main__":
    print("translated_powers", verify_translation())
    print("pointed_birth_obstruction", pointed_birth_obstruction())
    print("repeated_defects", repeated_defects())
