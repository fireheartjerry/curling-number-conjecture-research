"""Exact Q21 audit for the residual short external symbol-two seam.

This checks every rotation beginning in two and every admissible split.  It
records the overlap/next-label equations and then checks the full replay
profile consequences proved in ``symbol_two_status_seam.md``.  Curling
values used for orbit diagnostics are evaluated by both implementations.

Run the A094004 total-orbit-length calibration before using this output.
"""

from __future__ import annotations

from math import gcd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference
from check_general_rotation_status import primitive, proper_circular_profile


Word = tuple[int, ...]


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def exact_tail(word: Word, limit: int = 10000) -> int | None:
    current = word
    for step in range(limit + 1):
        value = exact_cn(current)
        if value == 1:
            return step
        current += (value,)
    return None


def main() -> None:
    q21 = tuple(map(int, "223222322232322232223"))
    assert primitive(q21)
    assert proper_circular_profile(q21) == q21
    n = len(q21)
    rows = []
    for rotation in range(n):
        p = q21[rotation:] + q21[:rotation]
        if p[0] != 2:
            continue
        assert proper_circular_profile(p) == p
        for split in range(2, n):
            hidden = n + 1 - split
            if split <= gcd(n, split):
                continue
            if p[:hidden] != p[split:] + (2,):
                continue
            if p[hidden] != 3:
                continue

            y = p * 2 + p[:split]
            profile = proper_circular_profile(y)
            holes = tuple(
                phase
                for phase in range(hidden)
                if y[phase] == 2 and profile[phase] == 1
            )
            replay_compatible = (
                all(profile[phase] <= y[phase] for phase in range(len(y)))
                and all(
                    profile[phase] == y[phase]
                    for phase in range(hidden, len(y))
                )
                and all(
                    profile[phase] == y[phase]
                    for phase in range(hidden)
                    if y[phase] >= 3
                )
            )

            remainder = n - split
            quotient, u_length = divmod(remainder, split)
            u = p[:u_length]
            v = p[u_length:split]
            assert quotient in (0, 1)
            assert u and v
            assert p == (u + v) * (quotient + 1) + u
            assert v + u == p[remainder:]

            h_word = p * 3 + (3,)
            e_word = p * 3 + (2,)
            b_word = (p[1:] + p[:1]) * 3
            assert exact_cn(e_word) == exact_cn(b_word) == 3
            rows.append(
                {
                    "rotation": rotation,
                    "P": "".join(map(str, p)),
                    "split": split,
                    "hidden": hidden,
                    "quotient": quotient,
                    "U": "".join(map(str, u)),
                    "V": "".join(map(str, v)),
                    "holes": holes,
                    "replay_compatible": replay_compatible,
                    "first_profile_mismatches": tuple(
                        (phase, y[phase], profile[phase])
                        for phase in range(len(y))
                        if y[phase] != profile[phase]
                    )[:8],
                    "cn_H": exact_cn(h_word),
                    "tau_H": exact_tail(h_word),
                    "tau_E": exact_tail(e_word),
                    "tau_B": exact_tail(b_word),
                }
            )

    print(
        {
            "rows": rows,
            "overlap_rows": len(rows),
            "replay_compatible_rows": sum(row["replay_compatible"] for row in rows),
        }
    )


if __name__ == "__main__":
    main()
