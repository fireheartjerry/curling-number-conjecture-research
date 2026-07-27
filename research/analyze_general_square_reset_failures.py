"""Explore the residual k=2 square-reset replay from general_rotation_status.

This is finite hypothesis generation, not a proof.  It enumerates primitive
words C over {2,3,4}, the exact overlap equation of Theorem 6, and then tests
the required common replay to Y^2.  Every curling number is evaluated by both
independent implementations.  Run the A094004 calibration first.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import product
from math import gcd

from check_general_rotation_status import exact_cn, primitive


Word = tuple[int, ...]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=12)
    args = parser.parse_args()

    stages: Counter[str] = Counter()
    first_failures: Counter[tuple[str, int, int]] = Counter()
    examples: dict[tuple[str, int, int], tuple[Word, int, int, int, int]] = {}
    reset_failures: Counter[tuple[int, int]] = Counter()
    reset_examples: dict[tuple[int, int], tuple[Word, int, int]] = {}

    for n in range(3, args.max_n + 1):
        for c in product((2, 3, 4), repeat=n):
            a = c[0]
            if a < 3 or 2 not in c or not primitive(c):
                continue
            for s in range(2, n):
                if s <= gcd(n, s):
                    continue
                h = n + 1 - s
                if c[:h] != c[s:] + (a,):
                    continue
                stages["overlap"] += 1

                y = c * 2 + c[:s]
                whole = y * 2
                deleted = whole[1:]
                whole_cn = exact_cn(whole)
                deleted_cn = exact_cn(deleted)
                if whole_cn != 2 or deleted_cn != 1:
                    stages["reset_exactness_failed"] += 1
                    reset_failures[(whole_cn, deleted_cn)] += 1
                    reset_examples.setdefault(
                        (whole_cn, deleted_cn), (c, s, h)
                    )
                    continue
                stages["exact_reset"] += 1

                # The actual common output begins at t=h and must spell Y.
                initial = y + y[:h]
                expected_initial = max(3, c[1])
                if exact_cn(initial) != expected_initial or y[h] != expected_initial:
                    stages["initial_coupling_failed"] += 1
                    continue
                stages["initial_coupling"] += 1

                failure = None
                for t in range(h, len(y)):
                    value = exact_cn(y + y[:t])
                    if value != y[t]:
                        kind = "overflow" if value > y[t] else "mask"
                        failure = (kind, t // n, t % n)
                        examples.setdefault(
                            failure,
                            (c, s, h, value, y[t]),
                        )
                        break
                if failure is None:
                    stages["complete_replay"] += 1
                else:
                    first_failures[failure] += 1

    print(
        {
            "stages": dict(stages),
            "reset_failures": dict(reset_failures),
            "first_failures": dict(first_failures),
        }
    )
    for key in sorted(reset_examples):
        c, s, h = reset_examples[key]
        print(
            "reset",
            key,
            "C=" + "".join(map(str, c)),
            f"s={s}",
            f"h={h}",
        )
    for key in sorted(examples):
        c, s, h, value, wanted = examples[key]
        print(
            key,
            "C=" + "".join(map(str, c)),
            f"s={s}",
            f"h={h}",
            f"value={value}",
            f"wanted={wanted}",
        )


if __name__ == "__main__":
    main()
