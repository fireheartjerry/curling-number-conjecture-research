"""Finite falsifier for increasingly strong external-ancestry hypotheses.

For a binary word ``U`` beginning ``P^3 3``, put

    D_U = (U^3)[1:],  A_U = D_U 2,  E_U = D_U 3,
    B_P = (P^3)[1:] 3.

The key coupling hypothesis says that the autonomous orbit from ``B_P``
generates exactly the remaining symbols of ``A_U``.  This is the deleted
side of a pair of consecutive external cubic resets.  Optional checks
also require that the undeleted high side follows the displayed word and
that ``P`` itself has the complete critical replay profile.
"""

from __future__ import annotations

import argparse
import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from curling import curling_number, tail_length  # noqa: E402


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return all(
        word != word[:period] * (n // period)
        for period in range(1, n)
        if n % period == 0
    )


def generates(start: tuple[int, ...], target: tuple[int, ...]) -> bool:
    if target[: len(start)] != start:
        return False
    current = start
    for symbol in target[len(start) :]:
        if curling_number(current) != symbol:
            return False
        current += (symbol,)
    return True


def critical_replay(word: tuple[int, ...]) -> bool:
    """The finite synchronization equations from ``word`` through its cube."""
    return primitive(word) and generates(word, word * 3)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("max_root_length", type=int)
    parser.add_argument("--min-root-length", type=int, default=1)
    parser.add_argument("--tail-limit", type=int, default=2000)
    parser.add_argument("--show-coupled", action="store_true")
    args = parser.parse_args()

    tested = coupled = high_coupled = critical_parent = terminating = 0
    violations = []
    for q in range(args.min_root_length, args.max_root_length + 1):
        for p in range(1, (q - 1) // 3 + 1):
            for parent_tail in itertools.product((2, 3), repeat=p - 1):
                parent = (2,) + parent_tail
                if not primitive(parent):
                    continue
                fixed_prefix = parent * 3 + (3,)
                remaining = q - len(fixed_prefix)
                if remaining < 0:
                    continue
                for suffix in itertools.product((2, 3), repeat=remaining):
                    tested += 1
                    root = fixed_prefix + suffix
                    if not primitive(root):
                        continue
                    deleted = (root * 3)[1:]
                    if (
                        curling_number(root * 3) != 3
                        or curling_number(deleted) != 2
                    ):
                        continue
                    low = deleted + (2,)
                    wrong = deleted + (3,)
                    parent_wrong = (parent * 3)[1:] + (3,)
                    if not generates(parent_wrong, low):
                        continue
                    coupled += 1

                    high_ok = generates(parent * 3, root * 3)
                    if high_ok:
                        high_coupled += 1
                    parent_ok = critical_replay(parent)
                    if parent_ok:
                        critical_parent += 1
                    try:
                        tau2 = tail_length(low, step_limit=args.tail_limit)
                        tau3 = tail_length(wrong, step_limit=args.tail_limit)
                    except RuntimeError:
                        continue
                    terminating += 1
                    if args.show_coupled:
                        print(
                            "COUPLED "
                            f"q={q} p={p} U={''.join(map(str, root))} "
                            f"tau2={tau2} tau3={tau3} "
                            f"high_coupled={high_ok} "
                            f"critical_parent={parent_ok}"
                        )
                    if tau3 > tau2:
                        record = (
                            q,
                            p,
                            "".join(map(str, root)),
                            tau2,
                            tau3,
                            high_ok,
                            parent_ok,
                        )
                        violations.append(record)
                        print(
                            "VIOLATION "
                            f"q={q} p={p} U={record[2]} "
                            f"tau2={tau2} tau3={tau3} "
                            f"high_coupled={high_ok} "
                            f"critical_parent={parent_ok}"
                        )
    print(
        f"max_q={args.max_root_length} tested={tested} coupled={coupled} "
        f"high_coupled={high_coupled} critical_parent={critical_parent} "
        f"terminating={terminating} violations={len(violations)}"
    )


if __name__ == "__main__":
    main()
