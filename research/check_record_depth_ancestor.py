"""Executed checks for record_depth_ancestor_audit.md."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference


def orbit(seed):
    word = tuple(seed)
    while True:
        value = curling_number(word)
        assert value == curling_number_reference(word)
        if value == 1:
            return word
        word += (value,)


def vertex_data(word, vertex):
    prefix = word[: vertex + 1]
    exponent = curling_number(prefix)
    assert exponent == curling_number_reference(prefix)
    roots = tuple(
        p
        for p in range(1, len(prefix) // exponent + 1)
        if prefix[-exponent * p :] == prefix[-p:] * exponent
    )
    p = min(roots)
    parent = vertex - p
    left = vertex + 1 - exponent * p
    return exponent, p, parent, left, exponent * p, roots


def main():
    word = orbit(map(int, "22322232"))
    first = vertex_data(word, 11)
    second = vertex_data(word, 17)
    assert word[11] == word[17] == 2
    assert first[:5] == (3, 4, 7, 0, 12)
    assert second[:5] == (2, 6, 11, 6, 12)
    assert second[1] > first[1] and second[3] > first[3]
    print("root record: (p,L)=(4,0)->(6,6)")

    word = orbit(map(int, "23222322"))
    vertices = (10, 13, 17, 21)
    rows = tuple(vertex_data(word, v)[:5] for v in vertices)
    assert all(word[v] == 2 for v in vertices)
    assert rows == (
        (2, 4, 6, 3, 8),
        (2, 3, 10, 8, 6),
        (2, 4, 13, 10, 8),
        (3, 4, 17, 10, 12),
    )
    assert rows[-1][4] > max(row[4] for row in rows[:-1])
    assert rows[-1][3] > rows[0][3]
    print("depth record: (D,L)=((8,3),...)->(12,10)")


if __name__ == "__main__":
    main()
