"""Audit the first steps after a whole-word maturation Y^k versus delete(Y^k).

Every curling number and root set printed by this program is obtained by
direct exhaustive suffix-power enumeration.
"""

from __future__ import annotations

import argparse
import itertools


def is_primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return not any(
        n % period == 0
        and all(word[i] == word[i % period] for i in range(period, n))
        for period in range(1, n)
    )


def curling_data(
    word: tuple[int, ...],
) -> tuple[int, tuple[int, ...]]:
    n = len(word)
    best = 1
    roots: list[int] = []
    for root in range(1, n // 2 + 1):
        block = word[n - root :]
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
        elif exponent == best:
            roots.append(root)
    return best, tuple(roots) if best >= 2 else ()


def orbit_trace(
    seed: tuple[int, ...],
    steps: int,
) -> tuple[tuple[int, tuple[int, ...]], ...]:
    word = seed
    result = []
    for _ in range(steps):
        value, roots = curling_data(word)
        result.append((value, roots))
        if value == 1:
            break
        word += (value,)
    return tuple(result)


def render(word: tuple[int, ...]) -> str:
    return "".join(map(str, word))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-root-length", type=int, default=14)
    parser.add_argument("--trace-steps", type=int, default=30)
    args = parser.parse_args()

    strict_drop = None
    regrowth = None
    unequal_first = None
    equal_first = None

    for length in range(1, args.max_root_length + 1):
        for letters in itertools.product((2, 3), repeat=length):
            y = tuple(letters)
            if not is_primitive(y):
                continue
            for exponent in range(2, 5):
                high = y * exponent
                local = high[1:]
                high_value, _ = curling_data(high)
                local_value, _ = curling_data(local)
                if high_value != exponent or local_value != exponent - 1:
                    continue
                post = high + (exponent,)
                post_value, post_roots = curling_data(post)
                if post_value == 1:
                    continue
                record = (
                    y,
                    exponent,
                    post_value,
                    post_roots,
                    orbit_trace(post, args.trace_steps),
                )
                if y[0] == exponent and equal_first is None:
                    equal_first = record
                if y[0] != exponent and unequal_first is None:
                    unequal_first = record
                if min(post_roots) < length and strict_drop is None:
                    strict_drop = record
                trace = record[-1]
                if min(post_roots) < length and any(
                    roots and max(roots) > length
                    for _, roots in trace[1:]
                ):
                    regrowth = record
                    break
            if regrowth is not None:
                break
        if regrowth is not None:
            break

    for name, record in (
        ("equal_first_symbol", equal_first),
        ("unequal_first_symbol", unequal_first),
        ("strict_root_drop", strict_drop),
        ("later_regrowth", regrowth),
    ):
        print(name)
        if record is None:
            print("none")
            continue
        y, exponent, post_value, post_roots, trace = record
        high = y * exponent
        local = high[1:]
        print(
            f"Y={render(y)} r={len(y)} k={exponent} "
            f"cn(Y^k)={curling_data(high)[0]} "
            f"cn(delete(Y^k))={curling_data(local)[0]}"
        )
        print(
            f"cn(Y^k.k)={post_value} maximizing_roots={post_roots}"
        )
        print("post_trace=" + repr(trace))


def test_postbreak_root_bound() -> None:
    """Exhaustive calibration of the p<=|Y| lemma in a finite range."""
    for length in range(1, 11):
        for y in itertools.product((2, 3), repeat=length):
            if not is_primitive(y):
                continue
            for exponent in range(2, 5):
                high = y * exponent
                if curling_data(high)[0] != exponent:
                    continue
                if curling_data(high[1:])[0] != exponent - 1:
                    continue
                value, roots = curling_data(high + (exponent,))
                if value >= 2:
                    assert all(root <= length for root in roots)
                    if length in roots:
                        assert y[0] == exponent


def test_equal_root_exponent_rise() -> None:
    word = tuple(map(int, "32323"))
    assert curling_data(word) == (2, (2,))
    assert curling_data(word + (2,)) == (3, (2,))


if __name__ == "__main__":
    main()
