"""Independent checks for research/pgtq_boundary_small_r.md.

The catalogue is re-derived here with a deliberately different
implementation style (string words, border-based period test) so the
enumeration script and this test cannot share a bug shape.
"""

import os
from itertools import product
from math import gcd


def periods(word):
    """All periods delta in [1, len(word)] via the border definition."""
    length = len(word)
    return {
        delta
        for delta in range(1, length + 1)
        if word[: length - delta] == word[delta:]
    }


def catalogue(r):
    """All (t, B) strings over {2, 3} meeting (S1)-(S6)."""
    found = []
    for word_tuple in product("23", repeat=r):
        word = "".join(word_tuple)
        word_periods = periods(word)
        if word[0] != "2":  # (S1)
            continue
        if any(2 * delta <= r for delta in word_periods):  # (S5)
            continue
        if any(delta < r and r % delta == 0 for delta in word_periods):
            continue  # (S4)
        run = len(word) - len(word.rstrip("3"))
        if run > 1:  # (S6)
            continue
        for t in word_periods:
            if not r / 2 < t < r:  # (S2) range
                continue
            if word[r - t] != "2":  # (S3)
                continue
            found.append((t, word))
    return sorted(found)


def test_pb1_pb3_small_r_void():
    for r in range(1, 4):
        assert catalogue(r) == []


def test_pb4_r4_unique():
    assert catalogue(4) == [(3, "2232")]


def test_pb5_r5_catalogue():
    assert catalogue(5) == [
        (3, "23223"),
        (4, "22232"),
        (4, "22322"),
        (4, "22332"),
    ]


def test_pb2_transfer_and_lambda_one():
    for r in range(3, 13):
        for t, word in catalogue(r):
            a = r - t
            assert word[r - 1] == word[a - 1]  # PB.2a
            run = len(word) - len(word.rstrip("3"))
            if a == 1:
                assert run == 0  # PB.2 item 1
            if run == 1:
                assert a >= 2 and r >= 5  # PB.2b
                assert word[a - 2 : a + 1] == "232"  # PB.2 item 2


def test_pb7b_fine_wilf_gap_between_large_periods():
    for r in range(3, 13):
        rows = catalogue(r)
        words = {word for _, word in rows}
        for word in words:
            large = sorted(delta for delta in periods(word) if r / 2 < delta < r)
            for i, t in enumerate(large):
                for u in large[i + 1 :]:
                    assert t + u - gcd(t, u) > r  # PB.7b


def suffix_root_exponent(word, root):
    """Exact exponent of the length-root suffix block."""
    block = word[len(word) - root :]
    copies = 0
    cursor = len(word)
    while cursor >= root and word[cursor - root : cursor] == block:
        copies += 1
        cursor -= root
    return copies


def test_pb6_r4_bridge_cut_atlas():
    """PB.6 checks the L-independent content only.

    The kappa values in PB.6 come from actual-orbit generation
    (kappa(K_h) = B[h mod r]); artificial L and Q samples can inflate
    the raw curling number, so this test verifies the suffix-square
    facts that make the table exact once those labels are given.
    """
    bridge = "2232"
    for q_word in ("3", "32", "3223", "32232232"):
        rec = bridge + q_word + bridge  # R = BQB
        for left in ("", "23", "2232232"):
            base = left + rec + rec  # LR^2, left context varied
            cuts = {
                "G1": base + bridge[:1],
                "G2": base + bridge[:2],
                "G3": base + bridge[:3],
                "M0": base + bridge,
                "M1": base + bridge + bridge[:1],
                "M2": base + bridge + bridge[:2],
                "M3": base + bridge + bridge[:3],
            }
            # Root-1 exponents are exact and context-free.
            assert suffix_root_exponent(cuts["G1"], 1) == 2
            assert suffix_root_exponent(cuts["M1"], 1) == 2
            assert suffix_root_exponent(cuts["G2"], 1) == 3
            assert suffix_root_exponent(cuts["M2"], 1) == 3
            # M0 and M3: roots 1-3 fail, root 4 is a suffix square.
            for name in ("M0", "M3"):
                word = cuts[name]
                for root in (1, 2, 3):
                    assert suffix_root_exponent(word, root) < 2
                assert suffix_root_exponent(word, 4) >= 2
            assert cuts["M3"].endswith("2223" * 2)
            # G3: roots 1-3 fail; root 4 squares iff Q ends in 2.
            for root in (1, 2, 3):
                assert suffix_root_exponent(cuts["G3"], root) < 2
            has_root4 = suffix_root_exponent(cuts["G3"], 4) >= 2
            assert has_root4 == (q_word[-1] == "2")


def test_pb8_r4_x_prefix_coordinates():
    bridge = "2232"
    for q_word in ("3", "32", "322322"):
        x_word = bridge[1:] + q_word + bridge + bridge
        assert x_word[0] == "2"
        assert x_word[1] == "3"
        assert x_word[2] == "2"  # alpha = p - 2 excluded
        assert x_word[3] == q_word[0] == "3"  # alpha = p - 3 allowed


def test_r4_circular_cubes_of_bridge():
    bridge = "2232"
    doubled = bridge * 3
    cubes = set()
    for root in range(1, 4):
        for start in range(len(bridge)):
            window = doubled[start : start + 3 * root]
            if len(window) == 3 * root and window == window[:root] * 3:
                cubes.add(window)
    assert cubes == {"222"}  # unique proper circular cube


def test_script_artifact_matches_enumeration():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(
        root, "research", "outputs", "pgtq_small_r_catalogue_2026-07-28.txt"
    )
    assert os.path.exists(path)
    with open(path, newline="") as handle:
        text = handle.read()
    assert "assertions=PASS" in text
    assert "NOT_A_PROOF" in text
    for r in range(1, 13):
        expected = len(catalogue(r))
        assert "r=%d count=%d" % (r, expected) in text
