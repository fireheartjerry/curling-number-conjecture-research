"""Exhaustively maximize the second square root at a low-root 2-state."""

from __future__ import annotations

import argparse
import multiprocessing

from research.search_refined_record import decode_seed


def curl_and_roots(sequence):
    sequence = tuple(sequence)
    length = len(sequence)
    best = 1
    roots = [1]
    for block_length in range(1, length + 1):
        block = sequence[length - block_length :]
        copies = 1
        cursor = length - 2 * block_length
        while cursor >= 0 and sequence[cursor : cursor + block_length] == block:
            copies += 1
            cursor -= block_length
        if copies > best:
            best = copies
            roots = [block_length]
        elif copies == best:
            roots.append(block_length)
    return best, tuple(roots)


def scan_interval(args):
    length, lower, upper, step_limit = args
    champion = (-1, None)
    for bits in range(lower, upper):
        seed = decode_seed(length, bits)
        state = seed
        for time in range(step_limit):
            value, roots = curl_and_roots(state)
            if value == 1:
                break
            if value == 2 and roots[0] <= 2 and len(roots) >= 2:
                candidate = roots[1]
                if candidate > champion[0]:
                    champion = (
                        candidate,
                        {
                            "seed": seed,
                            "time": time,
                            "state_length": len(state),
                            "roots": roots,
                        },
                    )
            state += (value,)
    return champion


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("--steps", type=int, default=220)
    parser.add_argument("--workers", type=int, default=min(8, multiprocessing.cpu_count()))
    args = parser.parse_args()
    count = 1 << args.length
    chunk = max(1, (count + args.workers * 8 - 1) // (args.workers * 8))
    jobs = [
        (args.length, lower, min(count, lower + chunk), args.steps)
        for lower in range(0, count, chunk)
    ]
    with multiprocessing.Pool(args.workers) as pool:
        champion = max(pool.map(scan_interval, jobs), key=lambda item: item[0])
    value, data = champion
    if data is not None:
        data = dict(data)
        data["seed"] = "".join(map(str, data["seed"]))
    print({"length": args.length, "second_root": value, "witness": data})


if __name__ == "__main__":
    main()
