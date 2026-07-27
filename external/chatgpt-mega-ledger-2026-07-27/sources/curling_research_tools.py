"""Exact tools used in the Curling Number Conjecture research ledger.

Convention: an orbit stops at the first prefix whose curling number is not in
{2, 3}; for calibration examples this is the first 1. All suffix block lengths
are checked via the Z-function of the reversed word.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Sequence


def z_function(s: Sequence[int]) -> list[int]:
    n = len(s)
    z = [0] * n
    left = right = 0
    for i in range(1, n):
        if i < right:
            z[i] = min(right - i, z[i - left])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


def curling_number_and_shortest_period(seq: Sequence[int]) -> tuple[int, int]:
    """Return (curling number, shortest period attaining it)."""
    if not seq:
        raise ValueError("The curling number is defined only for nonempty sequences")
    n = len(seq)
    rev = list(reversed(seq))
    z = z_function(rev)
    best_k = 1
    best_p = n
    for p in range(1, n):
        k = 1 + z[p] // p
        if k > best_k or (k == best_k and p < best_p):
            best_k, best_p = k, p
    return best_k, best_p


@dataclass(frozen=True)
class Event:
    length: int
    exponent: int
    period: int
    edge: int
    strict_period_record: bool


def trace_binary_orbit(seed: Sequence[int], max_steps: int = 100_000) -> list[Event]:
    """Trace until the first curling number outside {2,3}, or max_steps."""
    if not seed:
        raise ValueError("seed must be nonempty")
    s = list(seed)
    max_period = 0
    events: list[Event] = []
    for _ in range(max_steps + 1):
        k, p = curling_number_and_shortest_period(s)
        record = p > max_period
        if record:
            max_period = p
        events.append(Event(len(s), k, p, len(s) - k * p, record))
        if k not in (2, 3):
            break
        s.append(k)
    return events


def total_length_before_first_one(seed: Sequence[int], max_steps: int = 100_000) -> int:
    events = trace_binary_orbit(seed, max_steps=max_steps)
    if events[-1].exponent != 1:
        raise RuntimeError("No 1 reached within max_steps")
    return events[-1].length


def digits(text: str) -> list[int]:
    return [int(ch) for ch in text.strip()]


def calibrate() -> None:
    cases = {
        "322": 5,
        "23222323": 66,
        "2322322323222323223223": 142,
    }
    for seed_text, expected in cases.items():
        actual = total_length_before_first_one(digits(seed_text))
        if actual != expected:
            raise AssertionError((seed_text, expected, actual))
    print("Calibration passed: total lengths 5, 66, 142")


if __name__ == "__main__":
    calibrate()
