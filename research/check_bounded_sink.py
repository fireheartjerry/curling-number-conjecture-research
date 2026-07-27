"""Executed checks for research/bounded_sink_cascade.md."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference


def alternating_reset_words(level_count):
    words = [(2,)]
    for level in range(level_count):
        separator = 3 if level % 2 == 0 else 2
        previous = words[-1]
        words.append(previous + (separator,) + previous)
    return words


def proper_border_lengths(word):
    return tuple(
        length
        for length in range(1, len(word))
        if word[:length] == word[-length:]
    )


def main():
    words = alternating_reset_words(10)
    print("convention: cn is the maximum repeated-suffix exponent")
    for level, word in enumerate(words):
        fast = curling_number(word)
        reference = curling_number_reference(word)
        expected_borders = tuple(len(previous) for previous in words[:level])
        actual_borders = proper_border_lengths(word)
        assert fast == reference == 1
        assert word == word[::-1]
        assert actual_borders == expected_borders
        print(
            f"level={level} length={len(word)} cn={fast} "
            f"proper_borders={actual_borders}"
        )

    separators = tuple(3 if level % 2 == 0 else 2 for level in range(10))
    for depth in range(1, 10, 2):
        context = (2,) + words[depth] + (2,)
        context_cn = curling_number(context)
        assert context_cn == curling_number_reference(context) == 2
        sparse_values = tuple(
            curling_number(context + words[level])
            for level in range(depth + 1)
        )
        sparse_reference = tuple(
            curling_number_reference(context + words[level])
            for level in range(depth + 1)
        )
        expected = separators[: depth + 1]
        assert sparse_values == sparse_reference == expected
        print(
            f"depth={depth} context_length={len(context)} cn_context={context_cn} "
            f"exact_sparse_cut_cn={sparse_values}"
        )

    depth = 3
    context = (2,) + words[depth] + (2,)
    current = context
    emitted = []
    for _ in range(len(words[depth])):
        value = curling_number(current)
        assert value == curling_number_reference(current)
        emitted.append(value)
        if value == 1:
            break
        current += (value,)
    matching_prefix = 0
    for actual, expected in zip(emitted, words[depth]):
        if actual != expected:
            break
        matching_prefix += 1
    assert matching_prefix == 4
    failure_state = context + words[depth][:matching_prefix]
    failure_root = tuple(map(int, "2322"))
    assert failure_state[-3 * len(failure_root) :] == failure_root * 3
    assert curling_number(failure_state) == 3
    assert curling_number_reference(failure_state) == 3
    print(
        f"depth=3 attempted_full_orbit_matching_prefix={matching_prefix} "
        f"next_actual={emitted[matching_prefix]} "
        f"next_expected={words[depth][matching_prefix]} "
        f"failure_root=2322 failure_exponent=3"
    )

    context = tuple(map(int, "22322"))
    sparse_values = tuple(curling_number(context + word) for word in words[:4])
    sparse_reference = tuple(
        curling_number_reference(context + word) for word in words[:4]
    )
    assert sparse_values == sparse_reference == (3, 2, 3, 1)
    print(f"context=22322 sparse_cut_cn={sparse_values}")

    current = context
    emitted = []
    for _ in range(3):
        value = curling_number(current)
        assert value == curling_number_reference(current)
        emitted.append(value)
        if value == 1:
            break
        current += (value,)
    assert tuple(emitted) == (2, 3, 1)
    print(f"context=22322 actual_emitted_prefix={tuple(emitted)}")


if __name__ == "__main__":
    main()
