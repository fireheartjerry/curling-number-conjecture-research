"""Finite audits for one_sided_threshold_ancestry.md.

The unbounded component and marker lemmas are proved symbolically in the
note.  This script checks the Fibonacci suffix-duplication adversary and
recomputes every reported endpoint curling number with both independent
implementations.
"""

from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference


def fibonacci_words(max_index: int) -> list[str]:
    words = ["0", "01"]
    for _ in range(2, max_index + 1):
        words.append(words[-1] + words[-2])
    return words


def encode(word: str, maximum: int) -> tuple[int, ...]:
    high_block = (maximum - 1,) * maximum + (maximum,)
    output: tuple[int, ...] = ()
    for symbol in word:
        output += high_block if symbol == "0" else (2,)
    return output


def high_components(word: tuple[int, ...]) -> list[tuple[int, ...]]:
    components: list[tuple[int, ...]] = []
    index = 0
    while index < len(word):
        if word[index] < 3:
            index += 1
            continue
        end = index + 1
        while end < len(word) and word[end] >= 3:
            end += 1
        components.append(word[index:end])
        index = end
    return components


def has_suffix(word: tuple[int, ...], suffix: tuple[int, ...]) -> bool:
    return len(word) >= len(suffix) and word[-len(suffix) :] == suffix


def checked_curling_number(word: tuple[int, ...]) -> int:
    fast = curling_number(word)
    slow = curling_number_reference(word)
    assert fast == slow
    return fast


def main() -> None:
    words = fibonacci_words(11)
    checked_endpoints = 0
    largest_endpoint = 0

    for maximum in (4, 5, 6):
        high_block = (maximum - 1,) * maximum + (maximum,)
        marker = high_block + high_block + (2,)

        for index in (3, 5, 7, 9):
            current = words[index]
            missing_suffix = words[index - 3] + words[index - 2]

            assert current.endswith(missing_suffix)
            assert words[index + 2] == current * 2 + missing_suffix

            raw_current = encode(current, maximum)
            raw_double = raw_current * 2
            raw_suffix = encode(missing_suffix, maximum)
            raw_next = raw_double + raw_suffix

            assert raw_next == encode(words[index + 2], maximum)
            assert raw_double[-2 * len(raw_current) :] == raw_current * 2
            assert raw_next[-2 * len(raw_suffix) :] == raw_suffix * 2
            assert has_suffix(raw_current, marker)
            assert has_suffix(raw_double, marker)
            assert has_suffix(raw_next, marker)

            components = high_components(raw_next)
            assert components
            assert max(map(len, components)) <= 2 * len(high_block)

            assert checked_curling_number(raw_double) == 2
            assert checked_curling_number(raw_next) == 2
            checked_endpoints += 2
            largest_endpoint = max(largest_endpoint, len(raw_next))

    print("fibonacci_suffix_duplication_endpoints_checked", checked_endpoints)
    print("largest_raw_endpoint_length", largest_endpoint)
    print("maximum_values_checked", (4, 5, 6))
    print("odd_fibonacci_indices_checked", (3, 5, 7, 9))


if __name__ == "__main__":
    main()
