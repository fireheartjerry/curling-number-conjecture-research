"""Stress-test recursive g=2 predecessor chains in one-residue codes.

The ambient run code is A=(b_j,3,3), with b cyclic, binary, primitive,
and containing no ``22``.  A compressed g=2 gadget ending at ``v`` has

    b[u:v+1] = [1,C,2,C,2,C,1],  u=v-3h,

on the periodic lift, and primitive root code ``(C,2)``.

For a nonterminal gadget, this script selects the leftmost ``11`` in
its third copy of C and enumerates every compressed g=2 gadget ending
at the second 1.  It reports the exact lift displacement and searches
for counterexamples to proposed lexicographic descent ranks.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
import sys

from check_run_length_grammar import primitive
from explore_gadget_cycles import exact_negative_constraints
from explore_one_residue_codes import expand


@dataclass(frozen=True)
class G2:
    """A compressed g=2 gadget on a specified integer lift."""

    end: int
    span: int

    @property
    def start(self) -> int:
        return self.end - 3 * self.span


def at(b: tuple[int, ...], j: int) -> int:
    return b[j % len(b)]


def g2_at(b: tuple[int, ...], end: int, h: int) -> G2 | None:
    """Return the exact-leading compressed gadget, if present."""
    m = len(b)
    if not (1 <= h < m):
        return None
    u = end - 3 * h
    if at(b, u) != 1 or at(b, end) != 1:
        return None
    if at(b, u + h) != 2 or at(b, u + 2 * h) != 2:
        return None
    c = tuple(at(b, u + j) for j in range(1, h))
    if any(
        at(b, u + j) != at(b, u + h + j)
        or at(b, u + j) != at(b, u + 2 * h + j)
        for j in range(1, h)
    ):
        return None
    if not primitive(c + (2,)):
        return None
    return G2(end, h)


def all_g2_at(b: tuple[int, ...], end: int) -> tuple[G2, ...]:
    return tuple(
        gadget
        for h in range(1, len(b))
        if (gadget := g2_at(b, end, h)) is not None
    )


def first_internal_11(b: tuple[int, ...], gadget: G2) -> tuple[int, int] | None:
    """Return (second-index lift, number of preceding 12 pairs)."""
    u, h = gadget.start, gadget.span
    for t in range(1, h - 1):
        if at(b, u + t) == at(b, u + t + 1) == 1:
            # Transport the occurrence into the third copy of C.
            return u + 2 * h + t + 1, (t - 1) // 2
    return None


def cyclic_binary_words(m: int):
    for b in product((1, 2), repeat=m):
        if not primitive(b):
            continue
        if any(b[j] == b[(j + 1) % m] == 2 for j in range(m)):
            continue
        yield b


def covered(b: tuple[int, ...]) -> bool:
    """Every second 1 in an 11 pair has a compressed g=2 gadget."""
    return all(
        not (at(b, v - 1) == at(b, v) == 1) or all_g2_at(b, v)
        for v in range(len(b))
    )


def analyze(max_m: int, require_negative: bool) -> None:
    total_words = total_parents = total_transitions = 0
    crossing_examples: list[tuple] = []
    same_or_larger_examples: list[tuple] = []
    rank_failures: list[tuple] = []

    for m in range(1, max_m + 1):
        words_m = parents_m = transitions_m = 0
        for b in cyclic_binary_words(m):
            if not covered(b):
                continue
            if require_negative and not exact_negative_constraints(expand(b)):
                continue
            words_m += 1
            for end in range(m):
                for parent in all_g2_at(b, end):
                    selected = first_internal_11(b, parent)
                    if selected is None:
                        continue
                    parents_m += 1
                    child_end, parent_alt = selected
                    for next_gadget in all_g2_at(b, child_end):
                        transitions_m += 1
                        # Use the unique lift ending at child_end.
                        crossing = next_gadget.start < parent.start
                        if crossing and len(crossing_examples) < 20:
                            crossing_examples.append(
                                (
                                    "".join(map(str, b)),
                                    parent,
                                    parent_alt,
                                    child_end,
                                    next_gadget,
                                )
                            )
                        if (
                            next_gadget.span >= parent.span
                            and len(same_or_larger_examples) < 20
                        ):
                            same_or_larger_examples.append(
                                (
                                    "".join(map(str, b)),
                                    parent,
                                    parent_alt,
                                    child_end,
                                    next_gadget,
                                )
                            )

                        child_selected = first_internal_11(b, next_gadget)
                        if child_selected is None:
                            child_rank = (-1, next_gadget.span)
                        else:
                            child_rank = (
                                child_selected[1],
                                next_gadget.span,
                            )
                        parent_rank = (parent_alt, parent.span)
                        if (
                            child_rank >= parent_rank
                            and len(rank_failures) < 20
                        ):
                            rank_failures.append(
                                (
                                    "".join(map(str, b)),
                                    parent,
                                    parent_rank,
                                    next_gadget,
                                    child_rank,
                                )
                            )
        total_words += words_m
        total_parents += parents_m
        total_transitions += transitions_m
        print(
            f"m={m}: words={words_m} nonterminal={parents_m} "
            f"transitions={transitions_m}"
        )

    print(
        f"TOTAL words={total_words} nonterminal={total_parents} "
        f"transitions={total_transitions}"
    )
    print("CROSSING", crossing_examples)
    print("SAME_OR_LARGER", same_or_larger_examples)
    print("RANK_FAILURES", rank_failures)


if __name__ == "__main__":
    upper = int(sys.argv[1]) if len(sys.argv) > 1 else 18
    negative = "--negative" in sys.argv[2:]
    analyze(upper, negative)
