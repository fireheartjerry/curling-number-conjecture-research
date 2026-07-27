"""Enumerate exact oriented Q21 terminal gadget roots and overlaps."""

from __future__ import annotations

from check_run_length_grammar import primitive


BASE = tuple(map(int, "133233"))


def rotations(word: tuple[int, ...]):
    return tuple(word[k:] + word[:k] for k in range(len(word)))


def oriented_roots():
    out = []
    for shift, period_code in enumerate(rotations(BASE)):
        g = period_code[-1]
        splits = ((1, 1),) if g == 2 else ((1, 2), (2, 1))
        if g not in (2, 3):
            continue
        c = period_code[:-1]
        for alpha, beta in splits:
            root = [2] * alpha + [3]
            for run in c:
                root.extend([2] * run)
                root.append(3)
            root.extend([2] * beta)
            root = tuple(root)
            assert len(root) == 21 and primitive(root)
            out.append((shift, period_code, alpha, beta, root))
    return tuple(out)


def main() -> None:
    roots = oriented_roots()
    assert len(roots) == 9
    current = next(x for x in roots if x[1][-1] == 2)
    current_word = current[4]
    print(
        "current g2 root:",
        f"shift={current[0]} P={''.join(map(str, current[1]))}",
        f"U={''.join(map(str, current_word))}",
    )
    for overlap in range(1, 22):
        matches = tuple(
            x for x in roots if x[4][-overlap:] == current_word[:overlap]
        )
        if matches:
            print(
                f"overlap={overlap}:",
                tuple(
                    (
                        x[0],
                        "".join(map(str, x[1])),
                        x[2],
                        x[3],
                    )
                    for x in matches
                ),
            )
    matches11 = tuple(
        x for x in roots if x[4][-11:] == current_word[:11]
    )
    assert tuple(
        (x[0], x[1], x[2], x[3]) for x in matches11
    ) == ((4, tuple(map(int, "331332")), 1, 1),)


if __name__ == "__main__":
    main()
