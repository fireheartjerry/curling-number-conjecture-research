"""Independent audit of mixed weighted-profile counterexamples."""

from __future__ import annotations

from collections import Counter


MODELS = (
    ("0020010010100100020010010100100020010", (2, 2, 3)),
    ("0101101000211011010110100021101000211011", (2, 2, 3)),
)


def is_power(word: str, cut: int, root: int, exponent: int) -> bool:
    n = len(word)
    return all(
        word[(cut - block * root + offset) % n]
        == word[(cut - root + offset) % n]
        for block in range(2, exponent + 1)
        for offset in range(root)
    )


def proper_profile(word: str) -> tuple[int, ...]:
    n = len(word)
    result = []
    for cut in range(n):
        best = 1
        for root in range(1, n):
            exponent = 2
            while is_power(word, cut, root, exponent):
                best = max(best, exponent)
                exponent += 1
                if exponent > 4:
                    break
        result.append(best)
    return tuple(result)


def full_proper_profile(word: str) -> tuple[int, ...]:
    """Compute every exponent, with no cutoff at four.

    The caller first checks that ``word`` has no proper circular period.  Thus
    no proper root can repeat forever in the bi-infinite circular word.
    """

    assert not proper_periods(word)
    n = len(word)
    result = []
    for cut in range(n):
        best = 1
        for root in range(1, n):
            exponent = 2
            while is_power(word, cut, root, exponent):
                best = max(best, exponent)
                exponent += 1
        result.append(best)
    return tuple(result)


def proper_periods(word: str) -> tuple[int, ...]:
    n = len(word)
    return tuple(
        period
        for period in range(1, n)
        if all(word[i] == word[(i + period) % n] for i in range(n))
    )


def root_sets(
    word: str,
    exponent: int,
) -> tuple[tuple[int, ...], ...]:
    n = len(word)
    return tuple(
        tuple(
            root
            for root in range(1, n)
            if is_power(word, cut, root, exponent)
        )
        for cut in range(n)
    )


def audit(word: str, weights: tuple[int, ...]) -> None:
    profile = proper_profile(word)
    wanted = tuple(weights[int(token)] for token in word)
    squares = root_sets(word, 2)
    cubes = root_sets(word, 3)
    fourths = root_sets(word, 4)
    assert profile == wanted
    assert not proper_periods(word)
    assert all(squares)
    assert all(not roots for roots in fourths)
    assert len(set(word)) == 3
    assert len(set(weights)) == 2
    assert len(weights) > len(set(weights))

    projected = "".join(str(weights[int(token)]) for token in word)
    projected_profile = full_proper_profile(projected)
    projected_symbols = tuple(map(int, projected))
    assert projected_profile != projected_symbols

    print(f"word={word}")
    print(f"length={len(word)} counts={dict(Counter(word))}")
    print("profile=" + "".join(map(str, profile)))
    print(f"proper_periods={proper_periods(word)}")
    print(
        "cube_cuts="
        + repr(
            tuple(
                (cut, roots)
                for cut, roots in enumerate(cubes)
                if roots
            )
        )
    )
    print(
        "least_square_roots="
        + repr(tuple(roots[0] for roots in squares))
    )
    print(f"weight_projection={projected}")
    print(f"weight_projection_profile={projected_profile}")
    print(
        "weight_projection_mismatches="
        + repr(
            tuple(
                (cut, symbol, value)
                for cut, (symbol, value) in enumerate(
                    zip(projected_symbols, projected_profile)
                )
                if symbol != value
            )
        )
    )


def test_models() -> None:
    for word, weights in MODELS:
        audit(word, weights)


if __name__ == "__main__":
    test_models()
