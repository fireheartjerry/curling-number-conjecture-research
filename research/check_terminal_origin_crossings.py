"""Exhaust the local terminal factors that can cross one code origin.

For a fitting edge, a span-one factor crosses the origin only when its
canonical endpoint is 0,1,2; a span-six factor crosses only for endpoints
0,...,17.  There are 2*3 + 8*18 = 150 oriented candidates.  Compatibility
means equality at every overlapping lifted code position.
"""

from __future__ import annotations

from dataclasses import dataclass

from check_terminal_q21_overlaps import oriented_roots


@dataclass(frozen=True)
class Candidate:
    span: int
    endpoint: int
    orientation: str
    assignments: tuple[tuple[int, int], ...]


def terminal_long_factors() -> tuple[tuple[str, tuple[int, ...]], ...]:
    out = []
    for shift, period, alpha, beta, _ in oriented_roots():
        if period[-1] != 3:
            continue
        c = period[:-1]
        factor = (alpha,) + c + (3,) + c + (3,) + c + (beta,)
        out.append((f"shift={shift},a={alpha},b={beta}", factor))
    assert len(out) == 8
    return tuple(out)


def candidates() -> tuple[Candidate, ...]:
    out = []
    for endpoint in range(3):
        for alpha, beta in ((1, 2), (2, 1)):
            factor = (alpha, 3, 3, beta)
            out.append(
                Candidate(
                    1,
                    endpoint,
                    f"a={alpha},b={beta}",
                    tuple((endpoint - 3 + j, value) for j, value in enumerate(factor)),
                )
            )
    for endpoint in range(18):
        for label, factor in terminal_long_factors():
            out.append(
                Candidate(
                    6,
                    endpoint,
                    label,
                    tuple((endpoint - 18 + j, value) for j, value in enumerate(factor)),
                )
            )
    assert len(out) == 150
    return tuple(out)


def compatible(left: Candidate, right: Candidate) -> bool:
    a = dict(left.assignments)
    b = dict(right.assignments)
    return all(position not in b or b[position] == value for position, value in a.items())


def main() -> None:
    all_candidates = candidates()
    compatible_pairs = tuple(
        (i, j)
        for i in range(len(all_candidates))
        for j in range(i + 1, len(all_candidates))
        if compatible(all_candidates[i], all_candidates[j])
    )
    compatible_triples = tuple(
        (i, j, k)
        for i, j in compatible_pairs
        for k in range(j + 1, len(all_candidates))
        if compatible(all_candidates[i], all_candidates[k])
        and compatible(all_candidates[j], all_candidates[k])
    )
    assert compatible_pairs
    assert compatible_triples == ()

    maximum_example = next(
        (all_candidates[i], all_candidates[j])
        for i, j in compatible_pairs
    )
    print(f"candidates={len(all_candidates)}")
    print(f"compatible_pairs={len(compatible_pairs)}")
    print("compatible_triples=0")
    print(f"example_pair={maximum_example}")


if __name__ == "__main__":
    main()
