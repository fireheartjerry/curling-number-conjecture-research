from __future__ import annotations

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


def cn(seq: Sequence[int]) -> tuple[int, int]:
    if not seq:
        raise ValueError("empty word")
    n = len(seq)
    z = z_function(list(reversed(seq)))
    best_k, best_p = 1, n
    for p in range(1, n):
        k = 1 + z[p] // p
        if k > best_k or (k == best_k and p < best_p):
            best_k, best_p = k, p
    return best_k, best_p


def digits(s: str) -> list[int]:
    return [int(c) for c in s.strip()]


def continuation(seed: str, steps: int) -> list[tuple[int, int]]:
    s = digits(seed)
    out: list[tuple[int, int]] = []
    for _ in range(steps):
        k, p = cn(s)
        out.append((k, p))
        s.append(k)
    return out


def total_before_one(seed: str, cap: int = 100_000) -> int:
    s = digits(seed)
    for _ in range(cap):
        k, _ = cn(s)
        if k == 1:
            return len(s)
        s.append(k)
    raise RuntimeError("cap exceeded")


def show(label: str, word: str) -> None:
    print(f"{label}: word={word} cn/period={cn(digits(word))}")


def main() -> None:
    calibration = {
        "322": 5,
        "23222323": 66,
        "2322322323222323223223": 142,
    }
    for seed, expected in calibration.items():
        actual = total_before_one(seed)
        assert actual == expected, (seed, expected, actual)
    print("CALIBRATION PASSED: 5, 66, 142")

    D = "223222"
    R = "322232"
    full = continuation(D + R, len(R))
    stand = continuation(R + R, len(R))
    print("\nGENERATED-R^2 IMPOSTOR")
    print("D=", D, "R=", R)
    print("from DR generated symbols/periods:", full)
    print("generated symbols:", "".join(str(k) for k, _ in full))
    show("completed DR^2", D + R + "".join(str(k) for k, _ in full))
    print("from standalone R^2 symbols/periods:", stand)
    print("standalone symbols:", "".join(str(k) for k, _ in stand))

    R = "233323"
    B = "23"
    j = 1
    T = R[:j]
    L = "23332322333232"
    E = L + R + T
    G = L + R + R
    F = L + R + R + B + T
    H = L + R + R + B + R
    standalone = R + R + T
    print("\nSTATIC TWO-CUBE IMPOSTOR")
    print(f"L={L} R={R} B={B} j={j} T={T} P={len(R)+len(B)}")
    for label, word in [("E=LRT", E), ("G=LR^2", G), ("F=LR^2BT", F),
                        ("H=LR^2BR", H), ("R^2T", standalone)]:
        show(label, word)
    generated = continuation(L + R, len(R))
    print("actual symbols/periods from LR:", generated)
    print("actual generated block:", "".join(str(k) for k, _ in generated))
    print("desired second R:", R)
    assert "".join(str(k) for k, _ in generated) != R


if __name__ == "__main__":
    main()
