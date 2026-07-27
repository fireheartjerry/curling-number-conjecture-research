"""Finite regression checks for binary_compactness_escape.md."""


def tm(n: int) -> int:
    return n.bit_count() & 1


def limit_x(j: int) -> int:
    if j < 0:
        return tm(-j - 1)
    return 1 - tm(j)


def is_power(block: list[int], exponent: int) -> bool:
    if len(block) % exponent:
        return False
    p = len(block) // exponent
    return block == block[:p] * exponent


def main() -> None:
    # Exact centered-limit formula at finite powers of two.
    for m in range(2, 12):
        c = 1 << (2 * m)
        radius = min(1000, c)
        actual = [tm(c + j) for j in range(-radius, radius)]
        expected = [limit_x(j) for j in range(-radius, radius)]
        assert actual == expected

    # No square prefix, and equivalently no square ending at the limit cut.
    for bound in (64, 256, 1024, 4096):
        pref = [tm(i) for i in range(2 * bound)]
        roots = [
            p
            for p in range(1, bound + 1)
            if pref[:p] == pref[p : 2 * p]
        ]
        assert roots == []

        left = [limit_x(j) for j in range(-2 * bound, 0)]
        roots_at_cut = [
            p
            for p in range(1, bound + 1)
            if left[-2 * p : -p] == left[-p:]
        ]
        assert roots_at_cut == []
        print(f"root bound {bound}: no square prefix or center suffix")

    # Finite cube-free regression on centered windows.
    for radius in (128, 512, 2048):
        block = [limit_x(j) for j in range(-radius, radius)]
        cubes = []
        for end in range(1, len(block) + 1):
            for p in range(1, end // 3 + 1):
                if is_power(block[end - 3 * p : end], 3):
                    cubes.append((end, p))
        assert cubes == []
        print(f"radius {radius}: centered factor cube-free")


if __name__ == "__main__":
    main()
