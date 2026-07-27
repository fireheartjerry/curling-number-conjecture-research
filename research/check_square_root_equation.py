"""Exact checks for square-root equations in a periodic circular word.

For a rotation R of a primitive word Q, this script tests:

1. whether the greedy factorization of R^2 into shortest square prefixes
   closes exactly at length 2|R|; and
2. every composition |R| = |X_1| + ... + |X_m| satisfying

       R^2 = X_1^2 ... X_m^2
       R   = X_1   ... X_m.

The second test is a finite dynamic program over cut positions in R.
"""

from __future__ import annotations

from dataclasses import dataclass


Q = tuple(map(int, "223222322232322232223"))


def rotate(word: tuple[int, ...], shift: int) -> tuple[int, ...]:
    return word[shift:] + word[:shift]


def periodic_factor(
    word: tuple[int, ...], start: int, length: int
) -> tuple[int, ...]:
    n = len(word)
    return tuple(word[(start + i) % n] for i in range(length))


def square_roots_at(
    word: tuple[int, ...], start: int
) -> tuple[int, ...]:
    """All proper circular root lengths producing a forward square."""
    roots = []
    for root in range(1, len(word)):
        block = periodic_factor(word, start, root)
        if periodic_factor(word, start, 2 * root) == block * 2:
            roots.append(root)
    return tuple(roots)


def is_primitive(word: tuple[int, ...]) -> bool:
    """Test every possible proper power length."""
    n = len(word)
    return all(
        n % period != 0
        or word != word[:period] * (n // period)
        for period in range(1, n)
    )


def proper_circular_curl_at(
    word: tuple[int, ...], cut: int
) -> int:
    """Exact maximum exponent at a cut, restricting root length below |word|."""
    n = len(word)
    best = 1
    for root_length in range(1, n):
        terminal = periodic_factor(word, cut - root_length, root_length)
        copies = 1
        while copies <= n:
            previous = periodic_factor(
                word,
                cut - (copies + 1) * root_length,
                root_length,
            )
            if previous != terminal:
                break
            copies += 1
        if copies > n:
            raise AssertionError(
                ("proper root repeats around full period", root_length)
            )
        best = max(best, copies)
    return best


def proper_circular_profile(
    word: tuple[int, ...],
) -> tuple[int, ...]:
    return tuple(
        proper_circular_curl_at(word, cut)
        for cut in range(len(word))
    )


@dataclass(frozen=True)
class GreedyResult:
    roots: tuple[tuple[int, ...], ...]
    lengths: tuple[int, ...]
    consumed: int


def greedy_shortest_square_factorization(
    word: tuple[int, ...],
) -> GreedyResult:
    """Greedily factor from phase zero until reaching or passing 2|word|."""
    target = 2 * len(word)
    position = 0
    roots = []
    lengths = []
    while position < target:
        candidates = square_roots_at(word, position)
        if not candidates:
            raise AssertionError(("not circular-squareful", position))
        root_length = candidates[0]
        roots.append(periodic_factor(word, position, root_length))
        lengths.append(root_length)
        position += 2 * root_length
    return GreedyResult(tuple(roots), tuple(lengths), position)


def all_square_root_equation_compositions(
    word: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    """Enumerate all root-length compositions witnessing the equation."""
    n = len(word)
    doubled = word * 2
    paths: list[list[tuple[int, ...]]] = [[] for _ in range(n + 1)]
    paths[0] = [()]
    for root_sum in range(n):
        for path in paths[root_sum]:
            for root_length in range(1, n - root_sum + 1):
                root = word[root_sum : root_sum + root_length]
                square_start = 2 * root_sum
                square_end = square_start + 2 * root_length
                if doubled[square_start:square_end] == root * 2:
                    paths[root_sum + root_length].append(
                        path + (root_length,)
                    )
    return tuple(paths[n])


def materialize_roots(
    word: tuple[int, ...], lengths: tuple[int, ...]
) -> tuple[tuple[int, ...], ...]:
    roots = []
    cursor = 0
    for length in lengths:
        roots.append(word[cursor : cursor + length])
        cursor += length
    assert cursor == len(word)
    return tuple(roots)


def verify_equation(
    word: tuple[int, ...], lengths: tuple[int, ...]
) -> None:
    roots = materialize_roots(word, lengths)
    left = sum((root * 2 for root in roots), ())
    right_root = sum(roots, ())
    assert left == word * 2
    assert right_root == word
    assert left == right_root * 2


def optimal_square_roots(
    a: int, b: int
) -> frozenset[tuple[int, ...]]:
    """The six roots S_1,...,S_6 in Peltomäki--Saarela notation."""
    if a < 1 or b < 0:
        raise ValueError((a, b))
    zero = (0,)
    one = (1,)
    block = one + zero * a
    return frozenset(
        (
            zero,
            zero + one + zero * (a - 1),
            zero + one + zero * a,
            block,
            one + zero * (a + 1) + block * b,
            one + zero * (a + 1) + block * (b + 1),
        )
    )


def optimal_family_parameters(
    roots: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, int, int], ...]:
    """Find (letter_swap,a,b) placing every root in one six-root family."""
    if not roots:
        return ()
    max_length = max(map(len, roots))
    matches = []
    for letter_swap in (0, 1):
        binary_roots = tuple(
            tuple(((letter - 2) ^ letter_swap) for letter in root)
            for root in roots
        )
        for a in range(1, max_length + 1):
            for b in range(max_length + 1):
                family = optimal_square_roots(a, b)
                if all(root in family for root in binary_roots):
                    matches.append((letter_swap, a, b))
    return tuple(matches)


def minimality_flags(
    word: tuple[int, ...], lengths: tuple[int, ...]
) -> tuple[bool, ...]:
    """Say whether each selected square has the shortest root at its start."""
    flags = []
    root_sum = 0
    for root_length in lengths:
        minimum = square_roots_at(word, 2 * root_sum)[0]
        flags.append(root_length == minimum)
        root_sum += root_length
    return tuple(flags)


def main() -> None:
    assert len(Q) == 21
    assert is_primitive(Q)
    profile = proper_circular_profile(Q)
    assert profile == Q
    print(
        "word="
        + "".join(map(str, Q))
        + " primitive=True proper_circular_profile="
        + "".join(map(str, profile))
    )
    total_equations = 0
    nontrivial_equations = []
    any_greedy_equation = False
    for shift in range(len(Q)):
        word = rotate(Q, shift)
        greedy = greedy_shortest_square_factorization(word)
        equations = all_square_root_equation_compositions(word)
        for lengths in equations:
            verify_equation(word, lengths)
        total_equations += len(equations)
        greedy_closes = greedy.consumed == 2 * len(word)
        greedy_root = sum(greedy.roots, ())
        rotation_match = None
        if len(greedy_root) == len(word):
            for candidate_shift in range(len(Q)):
                if greedy_root == rotate(Q, candidate_shift):
                    rotation_match = candidate_shift
                    break
        greedy_equation = (
            greedy_closes
            and len(greedy_root) == len(word)
            and greedy_root == word
        )
        first_mismatch = None
        if greedy_closes and greedy_root != word:
            first_mismatch = next(
                index
                for index, (actual, wanted) in enumerate(
                    zip(greedy_root, word)
                )
                if actual != wanted
            )
        any_greedy_equation |= greedy_equation
        for lengths in equations:
            if lengths != (len(Q),):
                roots = materialize_roots(word, lengths)
                parameters = optimal_family_parameters(roots)
                flags = minimality_flags(word, lengths)
                nontrivial_equations.append(
                    (shift, lengths, flags, parameters)
                )
        print(
            f"shift={shift:2d} greedy_lengths={greedy.lengths} "
            f"consumed={greedy.consumed} "
            f"greedy_equation={greedy_equation} "
            f"greedy_root={''.join(map(str, greedy_root))} "
            f"rotation_match={rotation_match} "
            f"first_mismatch={first_mismatch} "
            f"equation_compositions={equations}"
        )
    assert not any_greedy_equation
    assert nontrivial_equations == [
        (1, (10, 1, 10), (False, True, False), ()),
        (
            1,
            (4, 2, 4, 1, 10),
            (True, True, False, True, False),
            (),
        ),
        (
            1,
            (10, 1, 4, 2, 4),
            (False, True, True, True, False),
            (),
        ),
        (
            1,
            (4, 2, 4, 1, 4, 2, 4),
            (True, True, False, True, True, True, False),
            (),
        ),
    ]
    print(f"rotations={len(Q)} total_equations={total_equations}")
    print(f"nontrivial_equations={nontrivial_equations}")

    # The suffix-square profile naturally becomes a prefix-square problem
    # after reversal, so audit that orientation separately rather than
    # assuming that greedy minimality is reversal-invariant.
    reverse_nontrivial = []
    reverse_any_greedy_equation = False
    reversed_q = Q[::-1]
    for shift in range(len(reversed_q)):
        word = rotate(reversed_q, shift)
        greedy = greedy_shortest_square_factorization(word)
        greedy_root = sum(greedy.roots, ())
        reverse_any_greedy_equation |= (
            greedy.consumed == 2 * len(word)
            and len(greedy_root) == len(word)
            and greedy_root == word
        )
        for lengths in all_square_root_equation_compositions(word):
            if lengths == (len(word),):
                continue
            roots = materialize_roots(word, lengths)
            reverse_nontrivial.append(
                (
                    shift,
                    lengths,
                    minimality_flags(word, lengths),
                    optimal_family_parameters(roots),
                )
            )
    assert not reverse_any_greedy_equation
    assert reverse_nontrivial == [
        (20, (10, 1, 10), (False, True, False), ()),
        (
            20,
            (4, 2, 4, 1, 10),
            (True, True, False, True, False),
            (),
        ),
        (
            20,
            (10, 1, 4, 2, 4),
            (False, True, True, True, False),
            (),
        ),
        (
            20,
            (4, 2, 4, 1, 4, 2, 4),
            (True, True, False, True, True, True, False),
            (),
        ),
    ]
    print(
        "reversed_rotations=21 reverse_greedy_equations=0 "
        f"reverse_nontrivial_equations={reverse_nontrivial}"
    )


if __name__ == "__main__":
    main()
