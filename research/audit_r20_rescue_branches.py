"""Symbolic finite audit of the R20 phase-5/phase-7 rescue branches.

This script uses only the two selected cube equations and the fixed suffix
R^3.  It enumerates the genuinely free prefix Z in the selected cube root
and asks whether the forced suffix already contains a forbidden cube at a
later phase labelled 2, or a forbidden fourth power at a phase labelled 3.
Such a conflict is independent of every symbol further to the left.
"""
from __future__ import annotations

from itertools import product


R = tuple(map(int, "22322323222322232232"))
B7 = R[:7]
D7 = tuple(map(int, "2322232"))
GLOBAL_MAX = 21


def power_roots(word, exponent, bound=GLOBAL_MAX):
    roots = []
    for root in range(1, min(bound, len(word) // exponent) + 1):
        if word[-exponent * root :] == word[-root:] * exponent:
            roots.append(root)
    return tuple(roots)


def bits(length):
    return product((2, 3), repeat=length)


def forced_conflicts(context):
    word = context + R * 3
    conflicts = []
    for phase in range(3 * len(R)):
        prefix = word[: len(context) + phase]
        label = R[phase % len(R)]
        cube_roots = power_roots(prefix, 3)
        fourth_roots = power_roots(prefix, 4)
        if label == 2 and cube_roots:
            conflicts.append((phase, "cube_at_2", cube_roots))
        if label == 3 and fourth_roots:
            conflicts.append((phase, "fourth_at_3", fourth_roots))
    return tuple(conflicts)


def q5_4_q7_contexts(q7):
    """Return all minimal suffixes forced by roots q5=4 and q7."""
    if q7 < 7:
        return ()
    if q7 == 13:
        # Here A has length six and the final seven context symbols are
        # B7[-1] A.  Equating this with D7 determines A.
        if D7[0] != B7[-1]:
            return ()
        candidates = (D7[1:],)
    elif q7 >= 14:
        # The phase-5 root 4 fixes context[-7:] = D7.  Since |A|>=7,
        # A=Z D7 and |Z|=q7-14.
        candidates = tuple(z + D7 for z in bits(q7 - 14))
    else:
        # q7=7..12 can be checked directly by enumerating A.
        candidates = tuple(bits(q7 - 7))

    contexts = []
    for a in candidates:
        v = a + B7
        context = v + v + a
        test = context + R[:7]
        if 4 in power_roots(context + R[:5], 3):
            if q7 in power_roots(test, 3):
                contexts.append(context)
    return tuple(contexts)


def q5_21_q7_7_contexts():
    """Return the four possible minimal suffixes for roots (21, 7)."""
    contexts = []
    for z in bits(2):
        a = z + B7 + B7
        v = a + R[:5]
        context = v + v + a
        if 21 in power_roots(context + R[:5], 3):
            if 7 in power_roots(context + R[:7], 3):
                contexts.append(context)
    return tuple(contexts)


def summarize(name, contexts):
    print(f"{name}: contexts={len(contexts)}")
    no_forced_conflict = []
    histogram = {}
    for context in contexts:
        conflicts = forced_conflicts(context)
        if not conflicts:
            no_forced_conflict.append(context)
            continue
        first = conflicts[0]
        histogram[first] = histogram.get(first, 0) + 1
    for key in sorted(histogram):
        print(f"  first_conflict={key} count={histogram[key]}")
    print(f"  survivors_without_forced_conflict={len(no_forced_conflict)}")
    for context in no_forced_conflict:
        print("   " + "".join(map(str, context)))


def main():
    print("R=" + "".join(map(str, R)))
    print("B7=" + "".join(map(str, B7)))
    print("D7=" + "".join(map(str, D7)))
    for q7 in range(7, GLOBAL_MAX + 1):
        contexts = q5_4_q7_contexts(q7)
        if contexts:
            summarize(f"(q5,q7)=(4,{q7})", contexts)
    summarize("(q5,q7)=(21,7)", q5_21_q7_7_contexts())


if __name__ == "__main__":
    main()
