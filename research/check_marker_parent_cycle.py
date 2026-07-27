"""Exact marker-parent-cycle counterexample."""

from __future__ import annotations

from research.check_critical_seed_induction import primitive


E = tuple(map(int, "233334"))
TOKENS = tuple(map(int, "0010200100101001020010200100101"))
RETURNS = tuple(
    tuple(map(int, prefix)) + E
    for prefix in ("2", "22323223323", "2233")
)


def proper_cut(word: tuple[int, ...], cut: int):
    n = len(word)
    best = 1
    roots: list[int] = []
    for root in range(1, n):
        matched = 0
        while (
            matched < n
            and word[(cut - 1 - matched) % n]
            == word[(cut - 1 - matched - root) % n]
        ):
            matched += 1
        value = 1 + matched // root
        if value > best:
            best = value
            roots = [root]
        elif value == best:
            roots.append(root)
    return best, tuple(roots)


def build():
    word: tuple[int, ...] = ()
    cuts = []
    for token in TOKENS:
        word += RETURNS[token]
        cuts.append(len(word))
    cuts = tuple(cut % len(word) for cut in cuts)
    return word, cuts


def audit():
    word, cuts = build()
    assert len(word) == 316
    assert primitive(word)
    assert sum(value == 4 for value in word) == len(cuts) == 31
    assert all(
        tuple(word[(cut - len(E) + i) % len(word)] for i in range(len(E)))
        == E
        for cut in cuts
    )
    assert all(word[cut] == 2 for cut in cuts)

    cut_index = {cut: index for index, cut in enumerate(cuts)}
    parents = []
    records = []
    for index, cut in enumerate(cuts):
        value, roots = proper_cut(word, cut)
        assert value == 2
        root = min(roots)
        parent_cut = (cut - root) % len(word)
        left_cut = (cut - 2 * root) % len(word)
        assert parent_cut in cut_index
        assert left_cut in cut_index
        parent = cut_index[parent_cut]
        parents.append(parent)
        records.append((index, root, parent, cut_index[left_cut]))

    assert parents[21] == 8
    assert parents[8] == 21
    assert records[21] == (21, 134, 8, 26)
    assert records[8] == (8, 182, 21, 3)
    return records


if __name__ == "__main__":
    print("marker_records", audit())
