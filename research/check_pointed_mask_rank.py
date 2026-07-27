"""Falsify naive pointed first-loss ranks on the exact Q64 bridge model.

The model satisfies all no-cube/no-fourth constraints and has fitting
period-21 roots at its unique double component.  It fails three positive
profile requirements, so it is not a fixed profile; its role is to show
that first-loss coordinates alone do not descend.
"""

from __future__ import annotations

from check_run_length_grammar import (
    binary_word,
    primitive,
    proper_profile,
    word_power_root_lengths,
)


def main() -> None:
    q21 = binary_word(tuple(map(int, "133233")))
    bridge_root = q21[16:] + q21[:16]
    q64 = bridge_root * 3 + (3,)
    word = q64[1:] + q64[:1]
    profile = proper_profile(word)
    n = len(word)
    assert n == 64 and primitive(word)
    assert word[0] == 2
    assert word_power_root_lengths(word, 62, 3) == (1, 21)
    assert word_power_root_lengths(word, 63, 3) == (21,)
    assert 3 * 21 <= n + 62 - 1
    assert 3 * 21 <= n + 63 - 1
    assert tuple(
        (i, word[i], profile[i])
        for i in range(n)
        if word[i] != profile[i]
    ) == ((1, 2, 1), (5, 3, 1), (10, 2, 1))

    # Equal-root bridge predecessor: c -> c-(3p+1).
    p = 21
    lifted_components = [62]
    for _ in range(4):
        lifted_components.append(lifted_components[-1] - (3 * p + 1))
    assert lifted_components == [62, -2, -66, -130, -194]
    assert all(c % n == 62 for c in lifted_components)

    # At every negative re-entry t=-2-64k, the canonical fitting root is
    # still p=21.  Lemma-10 overshoot is delta=2 and repeats exactly.
    first_losses = lifted_components[1:]
    ranks = []
    for generation, absolute_t in enumerate(first_losses):
        shifted_origin = -generation * n
        t = absolute_t - shifted_origin
        assert t == -2
        canonical = t + n
        assert canonical == 62
        distance = n + t - 1
        delta = 3 * p - distance
        ranks.append((distance, delta, p))
    assert ranks == [(61, 2, 21)] * len(first_losses)

    print(f"components={tuple(lifted_components)}")
    print(f"(canonical_distance,overshoot,period)={tuple(ranks)}")
    print(
        "positive-profile failures="
        + repr(tuple(
            (i, word[i], profile[i])
            for i in range(n)
            if word[i] != profile[i]
        ))
    )


if __name__ == "__main__":
    main()
