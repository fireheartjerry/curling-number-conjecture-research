"""Exhaustive binary search for two consecutive external cubic resets.

The enumeration convention matches ``tests/test_curling.py``: a length-n
binary seed is decoded little-endian from an integer, with bit zero giving
the first term.  Every curling number is evaluated by ``curling.py``.
"""

from __future__ import annotations

import argparse
import multiprocessing

from curling import curling_number


Word = tuple[int, ...]


def primitive(word: Word) -> bool:
    n = len(word)
    return not any(
        n % period == 0 and word == word[:period] * (n // period)
        for period in range(1, n)
    )


def decode(bits: int, length: int) -> Word:
    return tuple(2 + ((bits >> shift) & 1) for shift in range(length))


def reset_roots(seed: Word, step_limit: int) -> tuple[tuple[int, Word], ...]:
    state = seed
    roots: list[tuple[int, Word]] = []
    for _ in range(step_limit + 1):
        value = curling_number(state)
        if value == 1:
            return tuple(roots)
        if value == 3 and len(state) % 3 == 0:
            root_length = len(state) // 3
            root = state[:root_length]
            if (
                state == root * 3
                and primitive(root)
                and curling_number(state[1:]) == 2
            ):
                roots.append((root_length, root))
        state += (value,)
    raise RuntimeError(("step limit", seed, step_limit))


def search_interval(
    job: tuple[int, int, int, int],
) -> tuple[int, tuple[tuple[Word, tuple[int, ...]], ...]]:
    length, lower, upper, step_limit = job
    hits: list[tuple[Word, tuple[int, ...]]] = []
    examined = 0
    for bits in range(lower, upper):
        seed = decode(bits, length)
        roots = reset_roots(seed, step_limit)
        examined += 1
        for index in range(len(roots) - 2):
            p = roots[index][0]
            q = roots[index + 1][0]
            r = roots[index + 2][0]
            if q > 3 * p and r > 3 * q:
                hits.append((seed, (p, q, r)))
                break
    return examined, tuple(hits)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("minimum", type=int)
    parser.add_argument("maximum", type=int)
    parser.add_argument("--step-limit", type=int, default=500)
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()

    jobs = []
    for length in range(args.minimum, args.maximum + 1):
        total = 1 << length
        chunk = (total + args.workers - 1) // args.workers
        jobs.extend(
            (
                length,
                lower,
                min(total, lower + chunk),
                args.step_limit,
            )
            for lower in range(0, total, chunk)
        )

    with multiprocessing.Pool(args.workers) as pool:
        results = pool.map(search_interval, jobs)

    examined = sum(count for count, _ in results)
    hits = [hit for _, chunk in results for hit in chunk]
    print(
        "convention: cubic reset means exact high/deleted values 3/2 "
        "at a primitive whole cube"
    )
    print(
        f"lengths={args.minimum}..{args.maximum} "
        f"examined={examined} hits={len(hits)}"
    )
    for seed, lengths in hits:
        print("seed=" + "".join(map(str, seed)), "roots=" + repr(lengths))


if __name__ == "__main__":
    main()
