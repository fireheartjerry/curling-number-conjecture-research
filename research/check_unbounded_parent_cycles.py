"""Executed audit of an unbounded family of cycle-local parent models.

For L >= 2 put

    A_r = 2^(r-2) 3 2,             3 <= r <= L+2,
    Q_L = A_3 A_4 ... A_(L+2).

The cuts immediately after the arcs A_r form a winding-one cycle for the
least-maximizing-proper-root parent map.  This script computes every
proper cyclic exponent directly; it does not infer maximality from the
displayed squares.

The construction is deliberately only a model of the equations *on that
cycle*.  It is not a proper-cyclic-profile fixed point at all other cuts.
"""

from __future__ import annotations


Word = tuple[int, ...]
SEED_BOUND = 8


def arc(root: int) -> Word:
    assert root >= 3
    return (2,) * (root - 2) + (3, 2)


def family(length: int) -> tuple[Word, tuple[tuple[int, int], ...]]:
    """Return Q_L and its (endpoint cut, intended root) pairs."""
    assert length >= 2
    word: Word = ()
    endpoints: list[tuple[int, int]] = []
    for root in range(3, length + 3):
        word += arc(root)
        endpoints.append((len(word), root))
    q = len(word)
    return word, tuple((cut % q, root) for cut, root in endpoints)


def cyclic_block(word: Word, end: int, size: int) -> Word:
    """Length-size block ending at the circular cut end."""
    q = len(word)
    return tuple(word[index % q] for index in range(end - size, end))


def exponent_at_proper_root(word: Word, cut: int, root: int) -> int:
    """Exact exponent at one root 1 <= root < |word|.

    Consecutive root blocks are compared backwards.  More than |word|
    identical blocks would make the bi-infinite periodic word invariant
    under a nonzero shift smaller than |word|, contrary to primitivity.
    The explicit guard makes such an error fail loudly.
    """
    q = len(word)
    assert 1 <= root < q
    final = cyclic_block(word, cut, root)
    exponent = 1
    for copy in range(1, q + 1):
        if cyclic_block(word, cut - copy * root, root) != final:
            return exponent
        exponent += 1
    raise AssertionError("proper root repeated forever; word is not primitive")


def proper_cyclic_profile_at(
    word: Word, cut: int
) -> tuple[int, tuple[int, ...]]:
    """Return the exact proper cyclic CN and all maximizing roots."""
    by_root = tuple(
        exponent_at_proper_root(word, cut, root)
        for root in range(1, len(word))
    )
    value = max(by_root)
    roots = tuple(
        root
        for root, exponent in enumerate(by_root, start=1)
        if exponent == value
    )
    return value, roots


def is_primitive(word: Word) -> bool:
    q = len(word)
    return all(
        q % period != 0 or word != word[:period] * (q // period)
        for period in range(1, q)
    )


def audit_member(length: int) -> dict[str, object]:
    word, endpoints = family(length)
    q = len(word)
    assert q == length * (length + 5) // 2
    assert set(word) == {2, 3}
    assert is_primitive(word)
    assert len(endpoints) == length
    assert sum(root for _, root in endpoints) == q

    endpoint_records = []
    wrap_count = 0
    endpoint_set = {cut for cut, _ in endpoints}
    for cut, intended_root in endpoints:
        value, roots = proper_cyclic_profile_at(word, cut)

        # Exact maximality and uniqueness, not merely a square witness.
        assert value == 2
        assert roots == (intended_root,)

        # The two copied blocks and the two relevant self-label colors.
        copied = cyclic_block(word, cut, intended_root)
        source = cyclic_block(word, cut - intended_root, intended_root)
        assert copied == source == arc(intended_root)
        assert word[cut] == value == 2
        assert word[(cut - 1) % q] == 2

        parent = (cut - intended_root) % q
        assert parent in endpoint_set
        if cut - intended_root < 0:
            wrap_count += 1

        # This is the extra finite-prefix containment consequence in Lemma 8.
        # The three exceptional cuts 0, 3, 7 are all inside the fixed seed.
        if cut >= SEED_BOUND:
            assert 2 * intended_root <= cut

        endpoint_records.append(
            (cut, intended_root, value, roots, parent)
        )

    assert wrap_count == 1
    assert any(cut < SEED_BOUND for cut, _ in endpoints)

    # Following parents from any endpoint visits the whole endpoint set once.
    current = endpoints[-1][0]
    visited = []
    root_at = dict(endpoints)
    for _ in range(length):
        assert current not in visited
        visited.append(current)
        current = (current - root_at[current]) % q
    assert current == endpoints[-1][0]
    assert set(visited) == endpoint_set

    return {
        "L": length,
        "q": q,
        "cycle_length": len(visited),
        "winding": wrap_count,
        "spans": tuple(root for _, root in endpoints),
        "cuts": tuple(cut for cut, _ in endpoints),
        "records": tuple(endpoint_records),
    }


def audit_off_cycle_caveat() -> dict[str, object]:
    """Exhibit the missing global fixed-profile equations by computation."""
    word, endpoints = family(5)
    endpoint_set = {cut for cut, _ in endpoints}
    mismatches = []
    for cut in range(len(word)):
        value, roots = proper_cyclic_profile_at(word, cut)
        if value != word[cut]:
            mismatches.append((cut, word[cut], value, roots))
    assert mismatches
    assert any(cut not in endpoint_set for cut, _, _, _ in mismatches)
    assert all(
        proper_cyclic_profile_at(word, cut)[0] == word[cut]
        for cut in endpoint_set
    )
    return {
        "L": 5,
        "q": len(word),
        "word": "".join(map(str, word)),
        "mismatches": tuple(mismatches),
    }


def main() -> None:
    records = tuple(audit_member(length) for length in range(2, 31))
    caveat = audit_off_cycle_caveat()
    for record in records:
        print(
            "L={L} q={q} cycle={cycle_length} winding={winding} "
            "spans={spans} cuts={cuts}".format(**record)
        )
    print("off_cycle_caveat=" + repr(caveat))


if __name__ == "__main__":
    main()
