"""Explore finite termination ranks across one-symbol prefix deletion.

This is diagnostic only.  Curling numbers are computed by exhaustive suffix
power enumeration and cross-checked against the independent reference
implementation on every enumerated starting word.
"""

from __future__ import annotations

import argparse
import itertools

from curling import curling_number, curling_number_reference, tail_length


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return not any(
        n % d == 0 and word == word[:d] * (n // d)
        for d in range(1, n)
    )


def render(word: tuple[int, ...]) -> str:
    return "".join(map(str, word))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-length", type=int, default=16)
    args = parser.parse_args()

    records: list[tuple[int, int, tuple[int, ...], int, int]] = []
    by_low: dict[int, tuple[int, tuple[int, ...], int]] = {}
    no_later_lower_tail: list[
        tuple[int, int, tuple[int, ...], int]
    ] = []
    lower_witnesses: list[
        tuple[int, int, int, int, tuple[int, ...], int]
    ] = []
    reset_towers: list[
        tuple[int, tuple[int, ...], tuple[tuple[int, int, int], ...]]
    ] = []

    for n in range(2, args.max_length + 1):
        for word in itertools.product((2, 3), repeat=n):
            high_cn = curling_number(word)
            low_cn = curling_number(word[1:])
            assert high_cn == curling_number_reference(word)
            assert low_cn == curling_number_reference(word[1:])
            if high_cn != low_cn + 1:
                continue
            if n % high_cn:
                continue
            root = word[: n // high_cn]
            if word != root * high_cn or not primitive(root):
                continue
            high_tau = tail_length(word, step_limit=10000)
            low_tau = tail_length(word[1:], step_limit=10000)
            records.append((high_tau - low_tau, high_tau, word, low_tau, high_cn))
            old = by_low.get(low_tau)
            if old is None or high_tau > old[0]:
                by_low[low_tau] = (high_tau, word, high_cn)
            if low_tau > 0:
                state = word
                best_later = low_tau
                witness_step = -1
                for step in range(high_tau):
                    value = curling_number(state)
                    state += (value,)
                    candidate = tail_length(state[1:], step_limit=10000)
                    if candidate < best_later:
                        best_later = candidate
                        witness_step = step + 1
                        lower_witnesses.append(
                            (
                                witness_step,
                                low_tau,
                                candidate,
                                high_tau,
                                word,
                                high_cn,
                            )
                        )
                        break
                if witness_step < 0:
                    no_later_lower_tail.append(
                        (low_tau, high_tau, word, high_cn)
                    )
            state = word
            resets: list[tuple[int, int, int]] = []
            for step in range(high_tau):
                high_value = curling_number(state)
                deleted_value = curling_number(state[1:])
                assert high_value in (deleted_value, deleted_value + 1)
                if high_value == deleted_value + 1:
                    assert len(state) % high_value == 0
                    root_length = len(state) // high_value
                    assert state == state[:root_length] * high_value
                    resets.append((step, root_length, high_value))
                state += (high_value,)
            reset_towers.append((len(resets), word, tuple(resets)))

    print("convention: tau is steps before first current cn=1")
    print(f"enumerated_binary_lengths=2..{args.max_length}")
    print(f"strict_pure_power_boundaries={len(records)}")
    print("largest_high_minus_low")
    for gap, high_tau, word, low_tau, high_cn in sorted(records, reverse=True)[:20]:
        print(
            f"A={render(word)} k={high_cn} tau(A)={high_tau} "
            f"tau(A.tail)={low_tau} gap={gap}"
        )
    print("max_high_tau_by_low_tau")
    for low_tau in sorted(by_low)[:30]:
        high_tau, word, high_cn = by_low[low_tau]
        print(
            f"low_tau={low_tau} max_high_tau={high_tau} "
            f"A={render(word)} k={high_cn}"
        )
    print("no_later_high_state_with_lower_deleted_tau")
    print(f"count={len(no_later_lower_tail)}")
    for low_tau, high_tau, word, high_cn in no_later_lower_tail[:30]:
        print(
            f"A={render(word)} k={high_cn} tau(A)={high_tau} "
            f"tau(A.tail)={low_tau}"
        )
    print("largest_steps_to_lower_deleted_tau")
    for step, low_tau, candidate, high_tau, word, high_cn in sorted(
        lower_witnesses, reverse=True
    )[:30]:
        print(
            f"step={step} low_tau={low_tau}->{candidate} "
            f"tau(A)={high_tau} A={render(word)} k={high_cn}"
        )
    print("largest_driven_deletion_reset_towers")
    for count, word, resets in sorted(reset_towers, reverse=True)[:20]:
        print(f"count={count} A={render(word)} resets={resets}")


if __name__ == "__main__":
    main()
