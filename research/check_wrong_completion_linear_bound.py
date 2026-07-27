"""Falsify linear tail-delay bounds for the 2/3 completion siblings.

Diagnostic only.  For every binary word D of the requested lengths with
cn(D)=2, compute terminating tails of D, D2, and D3.  Curling numbers on
every orbit step are cross-checked against the independent reference
implementation.
"""

from __future__ import annotations

import argparse
import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from curling import curling_number, curling_number_reference


def checked_tau(word: tuple[int, ...], step_limit: int) -> int | None:
    state = word
    for step in range(step_limit + 1):
        fast = curling_number(state)
        reference = curling_number_reference(state)
        if fast != reference:
            raise AssertionError((state, fast, reference))
        if fast == 1:
            return step
        state += (fast,)
    return None


def render(word: tuple[int, ...]) -> str:
    return "".join(map(str, word))


def maximizing_roots(word: tuple[int, ...]) -> tuple[int, ...]:
    value = curling_number(word)
    roots: list[int] = []
    for root_length in range(1, len(word) // value + 1):
        suffix = word[-value * root_length :]
        if suffix == suffix[:root_length] * value:
            roots.append(root_length)
    return tuple(roots)


def first_prefix_mismatch(
    high: tuple[int, ...], low: tuple[int, ...], step_limit: int
) -> tuple[int, int, int, int, tuple[int, ...], tuple[int, ...]] | None:
    if high[1:] != low:
        raise AssertionError((high, low))
    high_state = high
    low_state = low
    for step in range(step_limit + 1):
        high_value = curling_number(high_state)
        low_value = curling_number(low_state)
        if high_value != curling_number_reference(high_state):
            raise AssertionError(high_state)
        if low_value != curling_number_reference(low_state):
            raise AssertionError(low_state)
        if high_value != low_value:
            return (
                step,
                high_value,
                low_value,
                len(high_state),
                maximizing_roots(high_state),
                maximizing_roots(low_state),
            )
        high_state += (high_value,)
        low_state += (low_value,)
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-length", type=int, default=16)
    parser.add_argument("--step-limit", type=int, default=2000)
    args = parser.parse_args()

    tested = eligible = terminating = 0
    maximum: tuple[int, tuple[int, ...], int, int, int] | None = None
    violations: list[tuple[int, tuple[int, ...], int, int, int]] = []

    for n in range(1, args.max_length + 1):
        for word in itertools.product((2, 3), repeat=n):
            tested += 1
            fast = curling_number(word)
            reference = curling_number_reference(word)
            if fast != reference:
                raise AssertionError((word, fast, reference))
            if fast != 2:
                continue
            eligible += 1
            tau_d = checked_tau(word, args.step_limit)
            tau_2 = checked_tau(word + (2,), args.step_limit)
            tau_3 = checked_tau(word + (3,), args.step_limit)
            if tau_d is None or tau_2 is None or tau_3 is None:
                continue
            terminating += 1
            delay = tau_3 - tau_d
            row = (delay, word, tau_d, tau_2, tau_3)
            if maximum is None or row[0] > maximum[0]:
                maximum = row
            if delay > n:
                violations.append(row)

    print("convention: tau is steps before first current cn=1")
    print(
        f"lengths=1..{args.max_length} tested={tested} eligible_cn2={eligible} "
        f"all_three_terminated={terminating}"
    )
    if maximum is not None:
        delay, word, tau_d, tau_2, tau_3 = maximum
        print(
            f"maximum_delay={delay} length={len(word)} D={render(word)} "
            f"tau_D={tau_d} tau_D2={tau_2} tau_D3={tau_3}"
        )
        tau_h = checked_tau((2,) + word + (3,), args.step_limit)
        mismatch = first_prefix_mismatch(
            (2,) + word + (3,), word + (3,), args.step_limit
        )
        print(f"maximum_example_tau_2D3={tau_h} H_F_first_mismatch={mismatch}")
    print(f"violations_of_tau_D3_minus_tau_D_le_length={len(violations)}")
    for delay, word, tau_d, tau_2, tau_3 in sorted(
        violations, reverse=True
    )[:20]:
        print(
            f"delay={delay} length={len(word)} D={render(word)} "
            f"tau_D={tau_d} tau_D2={tau_2} tau_D3={tau_3}"
        )


if __name__ == "__main__":
    main()
