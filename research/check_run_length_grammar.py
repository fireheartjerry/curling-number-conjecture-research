"""Exact checks for the singleton-3 run-length grammar.

This script is deliberately self-contained.  It verifies:

* the binary proper profile induced by a cyclic run code A;
* the clipped run-code criterion for a square at a 2-cut;
* primitive cubic defect gadgets [alpha,C,g,C,g,C,beta]; and
* the two failed 2-cuts in the length-33 near-model.

Conventions
-----------
``A[i]`` is the length of the i-th 2-run in

    Q(A) = product_i 2**A[i] 3.

At offset ``r`` in run ``i``, ``r=0`` is the cut before its first 2.
All indices in ``A`` are cyclic.  A proper root has physical length
strictly smaller than ``len(Q)``.
"""

from __future__ import annotations

from dataclasses import dataclass


A33 = tuple(map(int, "133233133233133213323313323313323"))
A9 = tuple(map(int, "133233233"))
A8 = tuple(map(int, "12112121"))
A18 = tuple(map(int, "133133233133233133"))


def primitive(word: tuple[int, ...]) -> bool:
    """Return whether ``word`` has no shorter integral period."""
    n = len(word)
    return all(
        any(word[j] != word[j % p] for j in range(p, n))
        for p in range(1, n)
        if n % p == 0
    )


def binary_word(a: tuple[int, ...]) -> tuple[int, ...]:
    """Expand the cyclic run code once."""
    out: list[int] = []
    for run in a:
        out.extend([2] * run)
        out.append(3)
    return tuple(out)


def proper_profile(q: tuple[int, ...]) -> tuple[int, ...]:
    """Compute the exact proper circular curling profile of ``q``."""
    n = len(q)
    profile: list[int] = []
    for cut in range(n):
        best = 1
        for root in range(1, n):
            exponent = 1
            while all(
                q[(cut - (exponent + 1) * root + j) % n]
                == q[(cut - root + j) % n]
                for j in range(root)
            ):
                exponent += 1
            best = max(best, exponent)
        profile.append(best)
    return tuple(profile)


def run_starts(a: tuple[int, ...]) -> tuple[int, ...]:
    starts: list[int] = []
    cursor = 0
    for run in a:
        starts.append(cursor)
        cursor += run + 1
    return tuple(starts)


def square_code_condition(
    a: tuple[int, ...], i: int, r: int, h: int
) -> bool:
    """The clipped run-code equation for a square with h threes/root."""
    m = len(a)
    if not (0 <= r < a[i] and 1 <= h < m):
        return False
    # The second copy begins r symbols into run i-h.  That cut must
    # still lie inside that run.
    if r > a[(i - h) % m]:
        return False
    internal = all(
        a[(i - 2 * h + j) % m] == a[(i - h + j) % m]
        for j in range(1, h)
    )
    capacity = a[(i - 2 * h) % m] >= a[(i - h) % m] - r
    return internal and capacity


def code_square_witnesses(
    a: tuple[int, ...], i: int, r: int
) -> tuple[int, ...]:
    return tuple(
        h
        for h in range(1, len(a))
        if square_code_condition(a, i, r, h)
    )


def direct_square_root_lengths(
    a: tuple[int, ...], i: int, r: int
) -> tuple[int, ...]:
    """Enumerate proper binary square-root lengths at a specified 2-cut."""
    q = binary_word(a)
    cut = run_starts(a)[i] + r
    n = len(q)
    return tuple(
        p
        for p in range(1, n)
        if all(
            q[(cut - 2 * p + j) % n] == q[(cut - p + j) % n]
            for j in range(p)
        )
    )


def direct_power_root_lengths(
    a: tuple[int, ...], i: int, r: int, exponent: int
) -> tuple[int, ...]:
    """Enumerate proper root lengths giving the requested power."""
    q = binary_word(a)
    cut = run_starts(a)[i] + r
    n = len(q)
    return tuple(
        p
        for p in range(1, n)
        if all(
            q[(cut - block * p + j) % n]
            == q[(cut - p + j) % n]
            for block in range(2, exponent + 1)
            for j in range(p)
        )
    )


def word_power_root_lengths(
    word: tuple[int, ...], cut: int, exponent: int
) -> tuple[int, ...]:
    """Proper circular power roots for an arbitrary primitive word."""
    n = len(word)
    return tuple(
        p
        for p in range(1, n)
        if all(
            word[(cut - block * p + j) % n]
            == word[(cut - p + j) % n]
            for block in range(2, exponent + 1)
            for j in range(p)
        )
    )


def power_code_condition(
    a: tuple[int, ...],
    i: int,
    r: int,
    h: int,
    exponent: int,
) -> bool:
    """Run-code equation for a nonunary ``exponent``-th power.

    The root contains exactly ``h`` symbols 3.  ``r=a[i]`` is allowed
    and denotes the cut immediately before the terminating 3.
    """
    m = len(a)
    if not (
        0 <= r <= a[i]
        and 1 <= h < m
        and exponent >= 2
        and r <= a[(i - h) % m]
    ):
        return False
    base = a[(i - h) % m]
    if a[(i - exponent * h) % m] < base - r:
        return False
    if any(
        a[(i - block * h) % m] != base
        for block in range(2, exponent)
    ):
        return False
    return all(
        a[(i - block * h + j) % m] == a[(i - h + j) % m]
        for block in range(2, exponent + 1)
        for j in range(1, h)
    )


def code_power_root_lengths(
    a: tuple[int, ...], i: int, r: int, exponent: int
) -> tuple[int, ...]:
    return tuple(
        h_root_length(a, i, r, h)
        for h in range(1, len(a))
        if power_code_condition(a, i, r, h, exponent)
    )


def h_root_length(a: tuple[int, ...], i: int, r: int, h: int) -> int:
    """Physical root length determined by a code witness."""
    # Moving the cut r symbols into a 2-run moves both ends by r, so r
    # cancels from the root length.
    del r
    return sum(a[(i - h + j) % len(a)] + 1 for j in range(h))


@dataclass(frozen=True)
class Gadget:
    end: int
    span: int
    alpha: int
    beta: int
    period_code: tuple[int, ...]


def defect_gadget(a: tuple[int, ...], i: int, s: int) -> Gadget | None:
    """Recognize a clipped [alpha,C,g,C,g,C,beta] cube gadget.

    The first displayed ``alpha`` may be only a suffix of the ambient
    run ``a[i-3s]``.  This leading-capacity inequality is essential.
    """
    m = len(a)
    if not (1 <= s < m):
        return None
    start = i - 3 * s
    beta = a[i % m]
    if beta not in (1, 2):
        return None
    g = a[(start + s) % m]
    if a[(start + 2 * s) % m] != g:
        return None
    alpha = g - beta
    if alpha < 1 or a[start % m] < alpha:
        return None
    c = tuple(a[(start + j) % m] for j in range(1, s))
    if any(
        a[(start + j) % m]
        != a[(start + s + j) % m]
        or a[(start + j) % m] != a[(start + 2 * s + j) % m]
        for j in range(1, s)
    ):
        return None
    p = c + (g,)
    if not primitive(p):
        return None
    if sum(x + 1 for x in p) >= len(binary_word(a)):
        return None
    return Gadget(i % m, s, alpha, beta, p)


def first_internal_mismatch(
    a: tuple[int, ...], i: int, h: int
) -> int | None:
    """First j in the internal equation that fails, or None."""
    m = len(a)
    return next(
        (
            j
            for j in range(1, h)
            if a[(i - 2 * h + j) % m] != a[(i - h + j) % m]
        ),
        None,
    )


def main() -> None:
    a = A33
    q = binary_word(a)
    f = proper_profile(q)
    assert len(a) == 33 and primitive(a)
    assert len(q) == 114 and primitive(q)

    starts = run_starts(a)
    failures = tuple(
        (i, r, starts[i] + r)
        for i, run in enumerate(a)
        for r in range(run)
        if not direct_square_root_lengths(a, i, r)
    )
    assert failures == ((18, 0, 61), (18, 1, 62))
    assert tuple(j for j, (x, y) in enumerate(zip(q, f)) if x != y) == (
        61,
        62,
    )
    assert f[61] == f[62] == 1 and q[61] == q[62] == 2

    # Calibrate the code equation against direct binary enumeration at
    # every 2-cut in this model.
    for i, run in enumerate(a):
        for r in range(run):
            nonunary_code_lengths = tuple(
                h_root_length(a, i, r, h)
                for h in code_square_witnesses(a, i, r)
            )
            code_lengths = tuple(
                sorted(set(nonunary_code_lengths + ((1,) if r >= 2 else ())))
            )
            assert code_lengths == direct_square_root_lengths(a, i, r)

    # Calibrate the general power equation at every cut after r twos,
    # including the cut r=a_i immediately before the following 3.
    for i, run in enumerate(a):
        for r in range(run + 1):
            cut = starts[i] + r
            for exponent in (2, 3, 4):
                direct_nonunary = tuple(
                    p
                    for p in direct_power_root_lengths(
                        a, i, r, exponent
                    )
                    if 3 in tuple(
                        q[(cut - p + j) % len(q)] for j in range(p)
                    )
                )
                assert code_power_root_lengths(
                    a, i, r, exponent
                ) == direct_nonunary

    g0 = defect_gadget(a, 0, 6)
    g16 = defect_gadget(a, 16, 6)
    assert g0 == Gadget(0, 6, 2, 1, tuple(map(int, "133233")))
    assert g16 == Gadget(16, 6, 2, 1, tuple(map(int, "313323")))

    # Physical hierarchy inside the period-21 root of the first s=6
    # gadget.  The third copy's six 3-cuts have child cube periods
    # 1,4,1,1,4,1, all strictly below 21/2.
    root_start = run_starts(a)[15]
    u21 = tuple(q[(root_start + j) % len(q)] for j in range(21))
    assert u21 == tuple(map(int, "223232223222322322232"))
    child_data = tuple(
        (
            offset,
            word_power_root_lengths(
                q, (root_start + 2 * len(u21) + offset) % len(q), 3
            ),
        )
        for offset, symbol in enumerate(u21)
        if symbol == 3
    )
    assert child_data == (
        (2, (1,)),
        (4, (4,)),
        (8, (1,)),
        (12, (1,)),
        (15, (4,)),
        (19, (1,)),
    )

    # In the circular root U itself, these are the 2-cuts for which no
    # square is wholly contained in the linear prefix U[0:cut].
    holes = tuple(
        cut
        for cut, symbol in enumerate(u21)
        if symbol == 2
        and not any(
            2 * p <= cut
            for p in word_power_root_lengths(u21, cut, 2)
        )
    )
    assert holes == (0, 1, 3, 9, 10)

    # At the failed run i=18, h=1 has no internal comparison but fails
    # capacity for both offsets:
    #     a_16 = 1 < a_17-r = 3-r,  r in {0,1}.
    assert a[16] == 1 and a[17] == 3
    for r in (0, 1):
        assert not (a[16] >= a[17] - r)

    # Every remaining possible proper h has a displayed internal mismatch.
    certificate = tuple(
        (h, first_internal_mismatch(a, 18, h))
        for h in range(2, len(a))
    )
    assert all(j is not None for _, j in certificate)

    # A local falsifier: one primitive nontrivial gadget and squareful
    # 2-cuts do not imply a fixed profile.
    a8 = A8
    q8 = binary_word(a8)
    f8 = proper_profile(q8)
    assert primitive(a8) and primitive(q8)
    assert max(f8) == 3
    assert defect_gadget(a8, 0, 2) == Gadget(
        0, 2, 1, 1, (1, 2)
    )
    assert all(
        direct_square_root_lengths(a8, i, r)
        for i, run in enumerate(a8)
        for r in range(run)
    )

    # A sharper falsifier: squarefulness plus global cube coverage is
    # still insufficient if leading capacity is allowed to be strict.
    a9 = A9
    q9 = binary_word(a9)
    f9 = proper_profile(q9)
    assert primitive(a9) and primitive(q9) and max(f9) == 3
    assert tuple(
        j for j, (x, y) in enumerate(zip(q9, f9)) if x != y
    ) == (22,)
    assert q9[22] == 2 and f9[22] == 3
    assert all(
        any(defect_gadget(a9, i, s) for s in range(1, len(a9)))
        for i, run in enumerate(a9)
        if run <= 2
    )
    assert defect_gadget(a9, 0, 3) == Gadget(
        0, 3, 1, 1, (3, 3, 2)
    )
    strict = defect_gadget(a9, 6, 1)
    assert strict == Gadget(6, 1, 1, 2, (3,))
    assert a9[(6 - 3) % len(a9)] == 2 > strict.alpha
    assert 4 in direct_power_root_lengths(a9, 6, 1, 3)

    # An essential short-border wrapping gadget need not have a smaller
    # masking cube at its own endpoint.  This model instead creates
    # unwanted period-ten powers later along the phase stream.
    a18 = A18
    q18 = binary_word(a18)
    f18 = proper_profile(q18)
    assert primitive(a18) and primitive(q18) and len(q18) == 62
    assert defect_gadget(a18, 0, 6) == Gadget(
        0, 6, 1, 1, tuple(map(int, "331332"))
    )
    assert word_power_root_lengths(q18, 1, 3) == (21,)
    assert word_power_root_lengths(q18, 1, 4) == ()
    assert tuple(
        j for j, (x, y) in enumerate(zip(q18, f18)) if x != y
    ) == (10, 12, 13, 14, 16, 17, 18, 20, 21)
    u18 = q18[:21]
    u18_periods = tuple(
        p
        for p in range(1, len(u18))
        if all(u18[j] == u18[j - p] for j in range(p, len(u18)))
    )
    assert u18_periods == (10, 14, 18, 20)

    print(f"A={''.join(map(str, a))}")
    print(f"|A|={len(a)}, |Q(A)|={len(q)}, primitive(A)=primitive(Q)=true")
    print(f"s=6 gadgets: end=0 P={''.join(map(str, g0.period_code))}; "
          f"end=16 P={''.join(map(str, g16.period_code))}")
    print("failed 2-cuts: (run,offset,Q-cut) =", failures)
    print("h=1: a_16=1 < a_17-r=3-r for r=0,1")
    print(
        "h=2..32 first internal mismatch j: "
        + " ".join(f"{h}:{j}" for h, j in certificate)
    )
    print(
        "local falsifier A8=12112121: s=2 gadget, all 2-cuts "
        "squareful, max(F)=3, but F!=Q"
    )
    print(
        "capacity falsifier A9=133233233: all defects cube-covered "
        "and all 2-cuts squareful; strict capacity at endpoint 6 "
        "shifts a period-4 cube to 2-cut 22"
    )
    print(
        "U21 child cube periods at third-copy 3-cuts: "
        + " ".join(f"{offset}:{roots[0]}" for offset, roots in child_data)
    )
    print("U21 linear-prefix square holes:", holes)
    print(
        "essential wrap falsifier A18: n=62 p=21 t=20 b=1, "
        "least period(U)=10; unwanted cuts "
        "10,12-18,20-21"
    )


if __name__ == "__main__":
    main()
