"""Direct certificate for two same-color minimal-square midpoint cycles."""

from __future__ import annotations


W = tuple(map(int, "3323223323232233232322"))

EXPECTED_ROOTS = (
    (1, 8),
    (8,),
    (1, 8),
    (8,),
    (8,),
    (2, 8),
    (1,),
    (6,),
    (1, 6),
    (6,),
    (6,),
    (2, 6),
    (2,),
    (2,),
    (1,),
    (14,),
    (1, 14),
    (8, 14),
    (8, 14),
    (2, 8, 14),
    (2, 8),
    (2, 8),
)

EXPECTED_PROFILE = tuple(map(int, "2223332222222322222223"))


def square_at_cut(cut: int, root: int) -> bool:
    n = len(W)
    return all(
        W[(cut - 2 * root + offset) % n]
        == W[(cut - root + offset) % n]
        for offset in range(root)
    )


def all_proper_square_roots() -> tuple[tuple[int, ...], ...]:
    n = len(W)
    return tuple(
        tuple(root for root in range(1, n) if square_at_cut(cut, root))
        for cut in range(n)
    )


def is_primitive() -> bool:
    n = len(W)
    return all(
        n % period != 0
        or W != W[:period] * (n // period)
        for period in range(1, n)
    )


def proper_circular_profile() -> tuple[int, ...]:
    n = len(W)
    values = []
    for cut in range(n):
        best = 1
        for root in range(1, n):
            terminal = tuple(
                W[(cut - root + offset) % n]
                for offset in range(root)
            )
            copies = 1
            while copies <= n:
                earlier = tuple(
                    W[(cut - (copies + 1) * root + offset) % n]
                    for offset in range(root)
                )
                if earlier != terminal:
                    break
                copies += 1
            if copies > n:
                raise AssertionError(("improper periodic root", root))
            best = max(best, copies)
        values.append(best)
    return tuple(values)


def directed_cycles(parent: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    n = len(parent)
    done = [False] * n
    result = []
    for start in range(n):
        if done[start]:
            continue
        path = []
        index = {}
        cut = start
        while not done[cut] and cut not in index:
            index[cut] = len(path)
            path.append(cut)
            cut = parent[cut]
        if cut in index:
            result.append(tuple(path[index[cut] :]))
        for cut in path:
            done[cut] = True
    return tuple(result)


def main() -> None:
    roots = all_proper_square_roots()
    assert roots == EXPECTED_ROOTS
    assert is_primitive()
    profile = proper_circular_profile()
    assert profile == EXPECTED_PROFILE
    assert set(profile) == {2, 3}
    mu = tuple(candidates[0] for candidates in roots)
    n = len(W)
    parent = tuple((cut - mu[cut]) % n for cut in range(n))
    cycles = directed_cycles(parent)
    assert cycles == ((17, 9, 3), (1, 15), (4, 18, 10))
    for cycle in cycles:
        cycle_roots = tuple(mu[cut] for cut in cycle)
        colors = tuple(W[(cut - 1) % n] for cut in cycle)
        assert sum(cycle_roots) == n
        print(
            f"cycle={cycle} roots={cycle_roots} "
            f"winding={sum(cycle_roots) // n} colors={colors}"
        )
    color_three_cycles = tuple(
        cycle
        for cycle in cycles
        if W[(cycle[0] - 1) % n] == 3
    )
    assert color_three_cycles == ((1, 15), (4, 18, 10))
    print(f"word={''.join(map(str, W))} primitive={is_primitive()}")
    print(f"profile={''.join(map(str, profile))} admissible=True")
    print(f"roots={roots}")
    print(f"mu={mu}")
    print(f"parent={parent}")


if __name__ == "__main__":
    main()
