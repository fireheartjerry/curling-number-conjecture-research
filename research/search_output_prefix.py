"""Find binary starts whose generated labels match a requested prefix."""

from __future__ import annotations

import argparse
import multiprocessing

from curling import curling_number
from research.search_refined_record import decode_seed


def match_length(seed, target):
    state = tuple(seed)
    for index, expected in enumerate(target):
        value = curling_number(state)
        if value != expected:
            return index
        state += (value,)
    return len(target)


def scan_interval(args):
    length, lower, upper, target = args
    best = (-1, None)
    for bits in range(lower, upper):
        seed = decode_seed(length, bits)
        matched = match_length(seed, target)
        if matched > best[0]:
            best = (matched, seed)
            if matched == len(target):
                break
    return best


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("target")
    parser.add_argument("--workers", type=int, default=min(8, multiprocessing.cpu_count()))
    args = parser.parse_args()
    target = tuple(map(int, args.target))
    count = 1 << args.length
    chunk = max(1, (count + args.workers * 8 - 1) // (args.workers * 8))
    jobs = [
        (args.length, lower, min(count, lower + chunk), target)
        for lower in range(0, count, chunk)
    ]
    with multiprocessing.Pool(args.workers) as pool:
        results = pool.map(scan_interval, jobs)
    matched, seed = max(results, key=lambda item: item[0])
    print(
        {
            "length": args.length,
            "matched": matched,
            "target_length": len(target),
            "seed": "".join(map(str, seed)) if seed else None,
        }
    )


if __name__ == "__main__":
    main()
