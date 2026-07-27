"""Executable identity checks for ``ava_bordered_quotients.md``.

This is a bounded calibration of the displayed word equations, not a
substitute for their symbolic proofs.
"""

from __future__ import annotations

import itertools


Word = tuple[int, ...]


def is_power_at(word: Word, cut: int, root: int, exponent: int) -> bool:
    if cut - exponent * root < 0:
        return False
    block = word[cut - root : cut]
    return all(
        word[cut - multiple * root : cut - (multiple - 1) * root] == block
        for multiple in range(2, exponent + 1)
    )


def build(root: Word, remainder: int, quotient: int) -> tuple[Word, ...]:
    prefix = root[:remainder]
    tail = root[remainder:]
    rotation = tail + prefix
    bordered = root * quotient + prefix
    unit = root * (quotient + 1) + prefix
    block = rotation + unit + unit
    return prefix, tail, rotation, bordered, unit, block


def main() -> None:
    checked = {0: 0, 1: 0, 2: 0}
    for length in range(2, 11):
        for remainder in range(1, length):
            for root in itertools.product((2, 3), repeat=length):
                if root[remainder] != 2:
                    continue
                for quotient in range(3):
                    prefix, tail, rotation, bordered, unit, block = build(
                        root, remainder, quotient
                    )
                    assert unit == bordered + rotation
                    assert block == rotation + unit + unit
                    assert block[-len(bordered) :] == bordered

                    doubled = block + block
                    boundary = len(block)
                    if quotient == 2:
                        cut = boundary + len(tail)
                        assert is_power_at(doubled, cut, length, 4)
                    elif quotient == 1:
                        for offset in range(remainder):
                            cut = boundary + len(tail) + offset
                            assert is_power_at(doubled, cut, length, 3)
                        if remainder == 1 and prefix == (3,):
                            assert is_power_at(doubled, boundary, length, 2)
                            assert is_power_at(
                                doubled, boundary + length - 1, length, 3
                            )
                    else:
                        first_cut = length + remainder
                        second_cut = 2 * length + 2 * remainder
                        assert is_power_at(block, first_cut, remainder, 2)
                        assert is_power_at(block, second_cut, remainder, 2)
                        assert block[first_cut] == 2
                        assert block[second_cut] == 2
                    checked[quotient] += 1

    print("bounded symbolic-identity calibration:", checked)


if __name__ == "__main__":
    main()
