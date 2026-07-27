"""Audit the translated-square fill of short symbol-two profile holes.

Run the A094004 calibration first.  The proof is symbolic; this script
checks every overlap candidate in every symbol-two rotation of Q21 and
recomputes all proper circular square roots on both sides of the
translation.
"""

from __future__ import annotations

from check_extended_cap_ancestry_q21 import Q21
from check_run_length_grammar import (
    primitive,
    proper_profile,
    word_power_root_lengths,
)


def rotations(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(word[shift:] + word[:shift] for shift in range(len(word)))


def main() -> None:
    assert primitive(Q21)
    assert proper_profile(Q21) == Q21

    records: list[dict[str, object]] = []
    translated_low_phases = 0
    for shift, p in enumerate(rotations(Q21)):
        n = len(p)
        if p[0] != 2:
            continue
        for s in range(2, n):
            h = n + 1 - s
            if p[:h] != p[s:] + (2,):
                continue
            if p[h - 1] != 2 or p[h] != max(3, p[1]):
                continue

            y = p * 2 + p[:s]
            assert primitive(y)
            assert p[: n - s] == p[s:]
            assert n < 3 * s
            assert n != 2 * s

            phase_records: list[dict[str, object]] = []
            for t in range(h):
                assert y[t] == p[t]
                if p[t] != 2:
                    continue
                translated = s + t
                assert translated <= n
                assert y + p[:t] == p * 2 + p[:translated]

                p_phase = translated % n
                p_roots = tuple(
                    root
                    for root in word_power_root_lengths(p, p_phase, 2)
                    if root < n
                )
                y_roots = tuple(
                    root
                    for root in word_power_root_lengths(y, t, 2)
                    if root < len(y)
                )
                y_root_set = set(y_roots)
                common = tuple(root for root in p_roots if root in y_root_set)
                assert p_roots
                assert common
                translated_low_phases += 1
                phase_records.append(
                    {
                        "phase": t,
                        "translated_P_phase": p_phase,
                        "P_square_roots": p_roots,
                        "Y_square_roots": y_roots,
                        "common_roots": common,
                    }
                )

            records.append(
                {
                    "rotation": shift,
                    "s": s,
                    "h": h,
                    "n": n,
                    "r": len(y),
                    "early_low_translations": tuple(phase_records),
                }
            )

    assert records
    assert translated_low_phases
    print(
        {
            "Q21_overlap_candidates": len(records),
            "translated_early_low_phases": translated_low_phases,
            "records": tuple(records),
        }
    )


if __name__ == "__main__":
    main()
