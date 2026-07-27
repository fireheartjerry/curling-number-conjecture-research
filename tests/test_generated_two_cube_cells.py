from itertools import product


def _has_period(word: tuple[int, ...], period: int) -> bool:
    return word[:-period] == word[period:]


def test_cell_b_index_chain_forces_a_square_through_q_12():
    """Exhaust the binary index certificate; this is not the Cell B proof."""

    checked_cases = 0
    for q in range(3, 13):
        for c in range(q // 2 + 1, q):
            for b in range(c + 1, q):
                delta = b - c
                for root in product((2, 3), repeat=q):
                    if not _has_period(root, c):
                        continue

                    k = root[q - c : q]
                    suffix_b = root[q - b : q]
                    if suffix_b != k + root[0:delta]:
                        continue

                    checked_cases += 1
                    assert suffix_b[0:c] == suffix_b[delta:b]
                    assert _has_period(suffix_b, delta)
                    assert len(suffix_b) > 2 * delta
                    assert (
                        suffix_b[b - 2 * delta : b - delta]
                        == suffix_b[b - delta : b]
                    )

    # This pins the cap and prevents a vacuous certificate.
    assert checked_cases == 84
