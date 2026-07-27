"""Executed audits for the contained symbol-two completion fork.

Run the A094004 calibration before this script.  The symbolic proofs are
in ``contained_completion_fork.md``.  This file performs two independent
finite checks:

1. Exhaust arbitrary primitive binary roots beginning in ``2`` and reject
   a whole-power representation of ``(C^3)[1:] + (3,)``.
2. On every phase-two rotation of the exact Q21 profile, recompute every
   maximizing root of ``C^3 + (3,)``.  In the value-three rows, verify the
   exact length-``3p-1`` shadow and the incoming-cube scale alternative.
"""

from __future__ import annotations

import argparse
from itertools import product
from math import gcd

from check_extended_cap_ancestry_q21 import Q21
from check_run_length_grammar import (
    primitive,
    proper_profile,
    word_power_root_lengths,
)
from check_symbol_two_status_seam import exact_cn, maximizing_roots


Word = tuple[int, ...]


def exact_tail(word: Word, step_limit: int = 10_000) -> int:
    state = word
    for steps in range(step_limit + 1):
        value = exact_cn(state)
        if value == 1:
            return steps
        state += (value,)
    raise RuntimeError("tail limit reached")


def whole_power_roots(word: Word) -> tuple[int, ...]:
    return tuple(
        root
        for root in range(1, len(word))
        if len(word) % root == 0
        and word == word[:root] * (len(word) // root)
    )


def circular_factor(word: Word, start: int, length: int) -> Word:
    return tuple(word[(start + offset) % len(word)] for offset in range(length))


def exhaustive_nonpower(max_n: int) -> dict[str, int]:
    checked = 0
    for n in range(1, max_n + 1):
        for tail in product((2, 3), repeat=n - 1):
            root = (2,) + tail
            if not primitive(root):
                continue
            checked += 1
            shifted_wrong_completion = (root * 3)[1:] + (3,)
            assert not whole_power_roots(shifted_wrong_completion)
    return {
        "max_n": max_n,
        "primitive_binary_roots_beginning_2": checked,
        "whole_power_counterexamples": 0,
    }


def q21_shadow_audit() -> tuple[dict[str, object], ...]:
    word = Q21
    n = len(word)
    assert primitive(word)
    assert proper_profile(word) == word

    records: list[dict[str, object]] = []
    for phase, label in enumerate(word):
        if label != 2:
            continue
        root = word[phase:] + word[:phase]
        promoted = root * 3 + (3,)
        value = exact_cn(promoted)
        if value != 3:
            continue

        for period in maximizing_roots(promoted):
            assert period < n
            power_root = promoted[-period:]
            assert power_root[-1] == 3
            interior = power_root[:-1]
            conjugate = (3,) + interior
            expected_shadow = (
                (2,) + interior + conjugate + conjugate
            )
            assert circular_factor(root, -3 * period, 3 * period) == (
                expected_shadow
            )

            high_cut = (-period) % n
            assert root[high_cut] == 3
            incoming = word_power_root_lengths(root, high_cut, 3)
            assert incoming
            alternatives: list[tuple[int, str]] = []
            for incoming_root in incoming:
                assert incoming_root != period
                common = gcd(period, incoming_root)
                overlap = min(2 * period - 1, 3 * incoming_root)
                assert overlap < period + incoming_root - common
                if incoming_root < period:
                    assert 2 * incoming_root + common < period
                    alternatives.append((incoming_root, "strict_descent"))
                else:
                    assert incoming_root >= period + common
                    alternatives.append((incoming_root, "strict_ascent"))

            records.append(
                {
                    "phase": phase,
                    "completion_root": period,
                    "internal_high_cut": high_cut,
                    "incoming_cube_roots": incoming,
                    "scale_alternatives": tuple(alternatives),
                    "shadow": "".join(map(str, expected_shadow)),
                }
            )

    return tuple(records)


def q21_completion_tail_order_audit() -> dict[str, object]:
    """Refute either unconditional ordering of tau(D3) and tau(D2)."""
    word = Q21
    n = len(word)
    assert primitive(word)
    assert proper_profile(word) == word

    rows: list[dict[str, int]] = []
    for phase, label in enumerate(word):
        if label != 2:
            continue
        root = word[phase:] + word[:phase]
        deleted = (root * 3)[1:]
        terminal_two = deleted + (2,)
        completion_three = deleted + (3,)
        promoted = root * 3 + (3,)

        tau_two = exact_tail(terminal_two)
        tau_three = exact_tail(completion_three)
        rows.append(
            {
                "phase": phase,
                "cn_promoted": exact_cn(promoted),
                "tau_D2": tau_two,
                "tau_D3": tau_three,
                "tau_D3_minus_tau_D2": tau_three - tau_two,
            }
        )

    greater = tuple(row for row in rows if row["tau_D3"] > row["tau_D2"])
    smaller = tuple(row for row in rows if row["tau_D3"] < row["tau_D2"])
    assert greater
    assert smaller
    return {
        "rows": tuple(rows),
        "D3_greater_examples": greater,
        "D3_smaller_examples": smaller,
        "maximum_positive_gap": max(
            row["tau_D3_minus_tau_D2"] for row in rows
        ),
        "maximum_negative_gap": min(
            row["tau_D3_minus_tau_D2"] for row in rows
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=14)
    args = parser.parse_args()
    print(
        {
            "nonpower_audit": exhaustive_nonpower(args.max_n),
            "Q21_value_three_shadows": q21_shadow_audit(),
            "Q21_completion_tail_order": q21_completion_tail_order_audit(),
        }
    )


if __name__ == "__main__":
    main()
