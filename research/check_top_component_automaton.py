"""Exact checks for the maximum-label top-component automaton.

For a parameter M, start with 0**M and append 1 precisely when the
current word has an M-th-power suffix; otherwise append 0.  The script
checks the valuation closed form through its first forced overflow and
checks the exact (M-1)-power criterion at every possible zero-phase exit.

All suffix-power tests enumerate every possible positive root length.
"""

from __future__ import annotations


def valuation(n: int, base: int) -> int:
    assert n >= 1 and base >= 2
    result = 0
    while n % base == 0:
        n //= base
        result += 1
    return result


def has_digit(n: int, base: int, digit: int) -> bool:
    assert n >= 1 and 0 <= digit < base
    while n:
        if n % base == digit:
            return True
        n //= base
    return False


def suffix_power_roots(word: bytes, exponent: int) -> tuple[int, ...]:
    """Every root length for which ``word`` ends in that exact power."""
    roots: list[int] = []
    length = len(word)
    for root in range(1, length // exponent + 1):
        block = word[-root:]
        if all(
            word[
                length - copy * root : length - (copy - 1) * root
            ]
            == block
            for copy in range(2, exponent + 1)
        ):
            roots.append(root)
    return tuple(roots)


def valuation_word(base: int, blocks: int) -> bytes:
    result = bytearray()
    for n in range(1, blocks + 1):
        result.extend(bytes([0]) * base)
        result.extend(bytes([1]) * (1 + valuation(n, base)))
    return bytes(result)


def block_end_positions(base: int, blocks: int) -> tuple[int, ...]:
    cursor = 0
    positions: list[int] = []
    for n in range(1, blocks + 1):
        cursor += base + 1 + valuation(n, base)
        positions.append(cursor)
    return tuple(positions)


def generated_prefix(base: int, final_length: int) -> bytes:
    word = bytearray(bytes([0]) * base)
    while len(word) < final_length:
        roots = suffix_power_roots(bytes(word), base)
        word.append(1 if roots else 0)
    return bytes(word)


def predicted_forced_zero_phase(
    base: int, block: int, zero_offset: int
) -> bool:
    """Whether an internal (M-1)-power forces the next zero label."""
    return (
        zero_offset == base - 1
        or has_digit(block, base, base - 1)
        or (
            zero_offset == 0
            and valuation(block, base) >= base - 2
        )
    )


def check_base(base: int) -> tuple[int, int, int]:
    threshold = base ** (base - 1)
    expected = valuation_word(base, threshold)

    # Independently run the suffix-power automaton through the complete
    # valuation prefix.  Its next decision must be one because the word
    # now ends in 1**M.
    generated = generated_prefix(base, len(expected))
    assert generated == expected
    final_roots = suffix_power_roots(expected, base)
    assert 1 in final_roots
    overflow = expected + bytes([1])
    assert overflow.endswith(bytes([1]) * (base + 1))

    # Check the closed-form decision at every pre-overflow prefix,
    # including every partial one-run.
    prefix = bytearray()
    prefix.extend(bytes([0]) * base)
    assert suffix_power_roots(bytes(prefix), base) == (1,)
    for n in range(1, threshold + 1):
        # The first one follows the unary zero power.
        assert suffix_power_roots(bytes(prefix), base)
        prefix.append(1)
        run = 1 + valuation(n, base)
        for visible_ones in range(1, run):
            roots = suffix_power_roots(bytes(prefix), base)
            assert roots
            assert visible_ones <= valuation(n, base)
            prefix.append(1)
        assert len(prefix) <= len(expected)
        if n < threshold:
            assert not suffix_power_roots(bytes(prefix), base)
            prefix.extend(bytes([0]) * base)
    assert bytes(prefix) == expected

    # At a zero phase after block n, zero_offset is the number of
    # already-present zeros in the next 0**M run.  Compare exact
    # root enumeration with the proposed arithmetic criterion.
    ends = block_end_positions(base, threshold)
    no_return_block = (base - 1) * base ** (base - 2)
    assert ends[no_return_block - 1] == base**base - 1
    candidates = 0
    forced = 0
    for n in range(1, threshold):
        for zero_offset in range(base):
            cut = ends[n - 1] + zero_offset
            current = expected[:cut]
            actual = bool(suffix_power_roots(current, base - 1))
            predicted = predicted_forced_zero_phase(
                base, n, zero_offset
            )
            assert actual == predicted
            if actual:
                forced += 1
            else:
                candidates += 1

    assert all(
        predicted_forced_zero_phase(base, n, zero_offset)
        for n in range(no_return_block, threshold)
        for zero_offset in range(base)
    )

    # Exit cuts do not synchronize return powers.  For every adjacent
    # pair of the immediate exit types (n,r)=(1,r), the shorter raw
    # return is a proper suffix of the longer one.  The resulting
    # (M-1)-power starts one symbol inside the longer return.
    high = base - 1
    marker = bytes([base - 2]) + bytes([high]) * base + bytes([base])
    returns = {
        zero_offset: bytes([high]) * zero_offset + marker
        for zero_offset in range(1, base - 1)
    }
    for zero_offset, raw_return in returns.items():
        assert not predicted_forced_zero_phase(
            base, 1, zero_offset
        )
        if zero_offset + 1 not in returns:
            continue
        longer = returns[zero_offset + 1]
        assert longer == bytes([high]) + raw_return
        pointed = longer + raw_return * (high - 1)
        assert pointed.endswith(raw_return * high)
    terminal = returns[base - 2]
    assert len(terminal) in suffix_power_roots(
        terminal * high, high
    )

    return len(expected), forced, candidates


def main() -> None:
    # The run-synchronization proof and the zero-phase criterion use
    # M>=4.  Check the first two values in that range completely.
    for base in (4, 5):
        length, forced, candidates = check_base(base)
        print(
            f"M={base}: valuation-prefix length={length}, "
            f"forced zero phases={forced}, "
            f"candidate exits={candidates}"
        )


if __name__ == "__main__":
    main()
