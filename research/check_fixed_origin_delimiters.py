"""Audit copied delimiters in nested fixed-origin cube prefixes."""

from __future__ import annotations

from dataclasses import dataclass


def curling_data(word: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    n = len(word)
    best = 1
    roots: list[int] = []
    for root in range(1, n // 2 + 1):
        block = word[-root:]
        exponent = 1
        while (
            (exponent + 1) * root <= n
            and word[
                n - (exponent + 1) * root : n - exponent * root
            ]
            == block
        ):
            exponent += 1
        if exponent > best:
            best = exponent
            roots = [root]
        elif exponent == best and exponent >= 2:
            roots.append(root)
    return best, tuple(roots) if best >= 2 else ()


def orbit(seed: tuple[int, ...], maximum_length: int) -> tuple[int, ...]:
    word = seed
    while len(word) < maximum_length:
        value, _ = curling_data(word)
        word += (value,)
    return word


def encode_fibonacci(word: str) -> tuple[int, ...]:
    return tuple(3 if symbol == "0" else 2 for symbol in word)


def fibonacci_roots(levels: int) -> tuple[str, ...]:
    a = "01001"
    b = "010"

    def h(word: str) -> str:
        return "".join(a if symbol == "0" else b for symbol in word)

    result = [b]
    for _ in range(levels):
        image = h(result[-1])
        assert image.startswith(a)
        result.append(image[len(a) :] + a)
    return tuple(result)


@dataclass(frozen=True)
class DelimiterAudit:
    cut: int
    symbol: int
    value: int
    roots: tuple[int, ...]


def q4_q21_audit() -> tuple[DelimiterAudit, ...]:
    q4 = tuple(map(int, "2232"))
    q21 = tuple(map(int, "223222322232322232223"))
    seed = tuple(map(int, "22322232"))
    word = orbit(seed, 66)
    assert word[: 3 * len(q4)] == q4 * 3
    assert word[: 3 * len(q21)] == q21 * 3
    assert word[63:66] == (3, 2, 1)

    delimiter = 3 * len(q4)
    assert word[delimiter] == 3
    assert word[delimiter] != q4[0]
    result = []
    for copy in range(3):
        cut = delimiter + copy * len(q21)
        value, roots = curling_data(word[:cut])
        result.append(DelimiterAudit(cut, word[cut], value, roots))
    assert result == [
        DelimiterAudit(12, 3, 3, (4,)),
        DelimiterAudit(33, 3, 3, (4,)),
        DelimiterAudit(54, 3, 3, (4,)),
    ]

    # At later weight-two phases the third Q21 copy acquires the global
    # root 21, but its exponent stays exactly two.
    for phase in (13, 14, 15, 17):
        first = curling_data(word[:phase])
        second = curling_data(word[: phase + 21])
        third = curling_data(word[: phase + 42])
        assert first[0] == second[0] == third[0] == word[phase] == 2
        assert 21 not in first[1] and 21 not in second[1]
        assert 21 in third[1]
    return tuple(result)


def power_roots(word: tuple[int, ...], cut: int, exponent: int) -> tuple[int, ...]:
    """All root lengths of an exponent-power ending at a linear cut."""
    return tuple(
        root
        for root in range(1, cut // exponent + 1)
        if all(
            word[cut - block * root + offset]
            == word[cut - root + offset]
            for block in range(2, exponent + 1)
            for offset in range(root)
        )
    )


def two_level_spike_audit() -> tuple[
    tuple[int, int, tuple[int, ...], tuple[int, ...], tuple[int, ...]], ...
]:
    """Enumerate every square, cube, and fourth root at the four spikes."""
    q = tuple(map(int, "2232"))
    r = tuple(map(int, "223222322232322232223"))
    word = r * 3 + (3,)
    cuts = (3 * len(q), len(r) + 3 * len(q),
            2 * len(r) + 3 * len(q), 3 * len(r))
    result = tuple(
        (
            cut,
            curling_data(word[:cut])[0],
            power_roots(word, cut, 2),
            power_roots(word, cut, 3),
            power_roots(word, cut, 4),
        )
        for cut in cuts
    )
    assert result == (
        (12, 3, (4,), (4,), ()),
        (33, 3, (4, 11), (4,), ()),
        (54, 3, (4, 11, 21), (4,), ()),
        (63, 3, (4, 10, 21), (21,), ()),
    )
    return result


def fibonacci_negative_control() -> tuple[tuple[int, int, int, int], ...]:
    roots = fibonacci_roots(6)
    limit = encode_fibonacci(roots[-1])
    result = []
    for level, root in enumerate(roots[:-1]):
        q = len(root)
        assert roots[level + 1].startswith(root * 3)
        state = limit[:q]
        mismatch = None
        for phase in range(min(200, len(limit) - q)):
            actual, _ = curling_data(state)
            wanted = limit[q + phase]
            if actual != wanted:
                mismatch = (level, q, phase, actual, wanted)
                break
            state += (actual,)
        assert mismatch is not None
        result.append(mismatch)
    return tuple(result)


def test_q4_q21_audit() -> None:
    q4_q21_audit()


def test_fibonacci_negative_control() -> None:
    fibonacci_negative_control()


def test_two_level_spike_audit() -> None:
    two_level_spike_audit()


if __name__ == "__main__":
    print("Q4_Q21=" + repr(q4_q21_audit()))
    print("TWO_LEVEL=" + repr(two_level_spike_audit()))
    print("FIBONACCI=" + repr(fibonacci_negative_control()))
