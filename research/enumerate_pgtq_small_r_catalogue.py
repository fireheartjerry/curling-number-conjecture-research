"""Enumerate the exact p>q boundary bridge-word catalogue for small r.

Scope: Cell C simultaneous boundary, branch p>q, surviving row
(z, h) = (1, 0). The constraint set (S1)-(S6) from
research/pgtq_boundary_small_r.md is necessary for every q, so for each
fixed r the enumeration is a complete classification valid for all q.
Membership is necessary, not sufficient; no realizability is claimed.

Deterministic output; run from the repository root:

    python research/enumerate_pgtq_small_r_catalogue.py
"""

from itertools import product

MAX_R = 12
OUTPUT_PATH = "research/outputs/pgtq_small_r_catalogue_2026-07-28.txt"


def has_period(word, delta):
    """True when word[i] == word[i + delta] for every valid i."""
    return all(word[i] == word[i + delta] for i in range(len(word) - delta))


def is_primitive(word):
    """True when word is not a proper integer power."""
    length = len(word)
    for delta in range(1, length):
        if length % delta == 0 and has_period(word, delta):
            return False
    return True


def terminal_three_run(word):
    """Length of the terminal run of 3's."""
    run = 0
    for symbol in reversed(word):
        if symbol != 3:
            break
        run += 1
    return run


def admissible_pairs(r):
    """All (t, B) meeting (S1)-(S6) at bridge length r, sorted."""
    pairs = []
    for t in range(r // 2 + 1, r):
        if not r / 2 < t < r:
            continue
        a = r - t
        for word in product((2, 3), repeat=r):
            if word[0] != 2:  # (S1)
                continue
            if not has_period(word, t):  # (S2)
                continue
            if word[a] != 2:  # (S3)
                continue
            if not is_primitive(word):  # (S4)
                continue
            if any(has_period(word, d) for d in range(1, r // 2 + 1)):
                continue  # (S5)
            if terminal_three_run(word) > 1:  # (S6)
                continue
            pairs.append((t, word))
    return pairs


def render(word):
    return "".join(str(symbol) for symbol in word)


def main():
    lines = [
        "label=pgtq_boundary_small_r_catalogue",
        "constraints=S1,S2,S3,S4,S5,S6",
        "scope=necessary_conditions_only_valid_for_every_q",
        "max_r=%d" % MAX_R,
    ]
    counts = {}
    for r in range(1, MAX_R + 1):
        pairs = admissible_pairs(r)
        counts[r] = len(pairs)
        lines.append("r=%d count=%d" % (r, len(pairs)))
        for t, word in pairs:
            a = r - t
            lines.append(
                "entry r=%d t=%d a=%d lambda=%d B=%s"
                % (r, t, a, terminal_three_run(word), render(word))
            )

    # PB.1 / PB.3: r <= 3 is void.
    assert counts[1] == counts[2] == counts[3] == 0
    # PB.4: r = 4 is uniquely (t, B) = (3, 2232).
    assert admissible_pairs(4) == [(3, (2, 2, 3, 2))]
    # PB.5: the complete r = 5 catalogue.
    assert sorted(render(word) for _, word in admissible_pairs(5)) == [
        "22232",
        "22322",
        "22332",
        "23223",
    ]
    # PB.2b: every lambda = 1 entry has a >= 2, hence r >= 5.
    for r in range(1, MAX_R + 1):
        for t, word in admissible_pairs(r):
            if terminal_three_run(word) == 1:
                assert r - t >= 2 and r >= 5
            # PB.2a: terminal-run transfer through the border.
            assert word[r - 1] == word[r - t - 1]
    lines.append("assertions=PASS")
    lines.append(
        "NOT_A_PROOF: per-r classification of necessary bridge-word "
        "conditions; the unbounded p>q word wall remains open."
    )

    text = "\n".join(lines) + "\n"
    with open(OUTPUT_PATH, "w", newline="\n") as handle:
        handle.write(text)
    print(text, end="")


if __name__ == "__main__":
    main()
