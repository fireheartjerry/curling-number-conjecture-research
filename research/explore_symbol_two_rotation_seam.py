"""Calibrated finite exploration of the remaining symbol-two seam.

Run the A094004 calibration before accepting this output.  This script is
hypothesis generation only: it enumerates primitive words with minimum two
and proper circular profile value two at phase zero, then audits the exact
cube/deletion/completion identities used in ``symbol_two_rotation_seam.md``.
Every curling number is evaluated by both implementations in ``curling.py``.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import product
from math import gcd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference
from check_general_rotation_status import (
    primitive,
    proper_circular_profile,
)


Word = tuple[int, ...]


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def maximizing_roots(word: Word) -> tuple[int, tuple[int, ...]]:
    value = exact_cn(word)
    roots = tuple(
        root
        for root in range(1, len(word) // value + 1)
        if word[-value * root :]
        == word[-root:] * value
    )
    assert roots
    return value, roots


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=9)
    args = parser.parse_args()

    counts: Counter[tuple[int, int, int]] = Counter()
    examples: dict[tuple[int, int, int], Word] = {}
    long_promoted: list[tuple[Word, Word, int, tuple[int, ...]]] = []
    tested = 0
    full_profiles = 0
    squareful_profiles = 0
    squareful_patterns: Counter[tuple[int, int, int]] = Counter()

    for n in range(2, args.max_n + 1):
        for tail in product((2, 3, 4), repeat=n - 1):
            period = (2,) + tail
            if min(period) != 2 or not primitive(period):
                continue
            profile = proper_circular_profile(period)
            if profile[0] != 2:
                continue
            tested += 1
            full_profiles += profile == period

            rotation = period[1:] + (2,)
            cube = period * 3
            deleted = cube[1:]
            promoted = cube + (3,)
            wrong = cube + (2,)
            next_cube = rotation * 3

            # Universal symbol-two identities.
            assert exact_cn(cube) == 3
            assert exact_cn(deleted) == 2
            assert deleted + (2,) == next_cube
            assert exact_cn(next_cube) == max(3, profile[1])
            assert exact_cn(wrong) == exact_cn(next_cube)

            promoted_value, promoted_roots = maximizing_roots(promoted)
            assert promoted_value <= 3
            if promoted_value >= 2 and max(promoted_roots) >= n:
                long_promoted.append(
                    (period, profile, promoted_value, promoted_roots)
                )

            key = (profile[1], promoted_value, exact_cn(wrong))
            counts[key] += 1
            examples.setdefault(key, period)
            if min(profile) >= 2:
                squareful_profiles += 1
                squareful_patterns[key] += 1

    print(
        {
            "tested_local_phase_zero": tested,
            "full_fixed_profiles": full_profiles,
            "squareful_profiles": squareful_profiles,
            "squareful_patterns": dict(sorted(squareful_patterns.items())),
            "patterns": dict(sorted(counts.items())),
            "long_promoted_roots": len(long_promoted),
        }
    )
    for key in sorted(examples):
        print(key, "P=" + "".join(map(str, examples[key])))
    for period, profile, value, roots in long_promoted[:20]:
        print(
            "long",
            "P=" + "".join(map(str, period)),
            "profile=" + "".join(map(str, profile)),
            f"cn={value}",
            f"roots={roots}",
        )

    q21 = tuple(map(int, "223222322232322232223"))
    assert proper_circular_profile(q21) == q21
    q21_rows = []
    for phase, label in enumerate(q21):
        if label != 2:
            continue
        period = q21[phase:] + q21[:phase]
        rotation = period[1:] + period[:1]
        cube = period * 3
        promoted_value, promoted_roots = maximizing_roots(cube + (3,))
        wrong_value, wrong_roots = maximizing_roots(cube + (2,))
        assert wrong_value == exact_cn(rotation * 3) == 3
        q21_rows.append(
            (phase, q21[(phase + 1) % len(q21)], promoted_value,
             promoted_roots, wrong_value, wrong_roots)
        )
    print("q21_symbol_two_rows", q21_rows)

    # Enumerate the exact word/profile equations left by the short external
    # prefix seam.  This does not assert that a status mismatch exists.
    short_counts: Counter[str] = Counter()
    short_examples: dict[str, tuple[Word, int, int, Word, Word]] = {}
    for n in range(3, min(args.max_n, 14) + 1):
        for tail in product((2, 3), repeat=n - 1):
            c = (2,) + tail
            if not primitive(c):
                continue
            c_profile = proper_circular_profile(c)
            if c_profile != c:
                continue
            for split in range(2, n):
                if split <= gcd(n, split):
                    continue
                hidden = n + 1 - split
                if c[:hidden] != c[split:] + (2,):
                    continue
                if c[hidden] != max(3, c[1]):
                    continue
                short_counts["fixed_overlap"] += 1
                y = c * 2 + c[:split]
                y_profile = proper_circular_profile(y)
                holes = tuple(
                    phase
                    for phase in range(hidden)
                    if y[phase] == 2 and y_profile[phase] == 1
                )
                replay_compatible = (
                    all(y_profile[phase] <= y[phase] for phase in range(len(y)))
                    and all(
                        y_profile[phase] == y[phase]
                        for phase in range(hidden, len(y))
                    )
                    and all(
                        y_profile[phase] == y[phase]
                        for phase in range(hidden)
                        if y[phase] >= 3
                    )
                )
                if not replay_compatible:
                    short_counts["profile_incompatible"] += 1
                    short_examples.setdefault(
                        "profile_incompatible", (c, split, hidden, y, holes)
                    )
                elif holes:
                    short_counts["compatible_with_low_holes"] += 1
                    short_examples.setdefault(
                        "compatible_with_low_holes", (c, split, hidden, y, holes)
                    )
                else:
                    short_counts["complete_fixed_child"] += 1
                    short_examples.setdefault(
                        "complete_fixed_child", (c, split, hidden, y, holes)
                    )
    print("short_external_fixed_parent", dict(short_counts))
    for kind, (c, split, hidden, y, holes) in short_examples.items():
        print(
            kind,
            "C=" + "".join(map(str, c)),
            f"split={split}",
            f"h={hidden}",
            "Y=" + "".join(map(str, y)),
            f"holes={holes}",
        )


if __name__ == "__main__":
    main()
