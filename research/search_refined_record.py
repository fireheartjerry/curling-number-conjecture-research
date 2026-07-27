"""Parallel falsifier for the generated-record left-endpoint conjecture.

For each binary seed, build canonical nearest-parent vertices incrementally.
On every value-2 parent ray, a new record cube root is checked against the
previous record.  The candidate says that if the old cube began at or beyond
the seed boundary, the new record cube must begin strictly earlier.
"""

from __future__ import annotations

import argparse
import multiprocessing


def curl_and_shortest(sequence):
    sequence = tuple(sequence)
    length = len(sequence)
    best = 1
    shortest = 1
    for block_length in range(1, length + 1):
        block = sequence[length - block_length :]
        copies = 1
        cursor = length - 2 * block_length
        while cursor >= 0 and sequence[cursor : cursor + block_length] == block:
            copies += 1
            cursor -= block_length
        if copies > best:
            best = copies
            shortest = block_length
    return best, shortest


def decode_seed(length, bits):
    return tuple(2 + ((bits >> shift) & 1) for shift in range(length))


def first_failure(seed, step_limit):
    seed_length = len(seed)
    state = tuple(seed)
    previous_value = None
    # vertex -> (record cube span, its left endpoint); only value-2 vertices
    ray_record = {}
    trace = []

    for time in range(step_limit + 1):
        value, root = curl_and_shortest(state)
        if previous_value is not None:
            vertex = seed_length + time - 1
            if previous_value == 2 and value >= 2:
                parent = vertex - root
                old_span, old_left = ray_record.get(parent, (-1, None))
                new_span, new_left = old_span, old_left
                if value == 3 and root > old_span:
                    left = vertex - 3 * root + 1
                    if old_left is not None and old_left >= seed_length and left >= old_left:
                        return {
                            "seed": seed,
                            "time": time - 1,
                            "vertex": vertex,
                            "root": root,
                            "left": left,
                            "old_span": old_span,
                            "old_left": old_left,
                            "trace": tuple(trace),
                        }
                    new_span, new_left = root, left
                ray_record[vertex] = (new_span, new_left)
        if value == 1:
            return None
        trace.append(value)
        state += (value,)
        previous_value = value
    return None


def scan_interval(args):
    length, lower, upper, step_limit = args
    for bits in range(lower, upper):
        failure = first_failure(decode_seed(length, bits), step_limit)
        if failure is not None:
            return failure
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("--steps", type=int, default=220)
    parser.add_argument("--workers", type=int, default=min(8, multiprocessing.cpu_count()))
    args = parser.parse_args()

    case_count = 1 << args.length
    chunk_size = max(1, (case_count + args.workers * 8 - 1) // (args.workers * 8))
    jobs = [
        (args.length, lower, min(case_count, lower + chunk_size), args.steps)
        for lower in range(0, case_count, chunk_size)
    ]
    with multiprocessing.Pool(args.workers) as pool:
        for result in pool.imap_unordered(scan_interval, jobs):
            if result is not None:
                print(result)
                pool.terminate()
                return 1
    print({"length": args.length, "cases": case_count, "failure": None})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
