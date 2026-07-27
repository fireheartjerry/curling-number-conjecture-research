"""Exact arithmetic audit for repeated affine peak crossings.

This does not construct a word and does not evaluate a curling number.
It checks that the complete integer inequalities currently proved for
the crossing branch admit an infinite self-similar parameter family.
Consequently those inequalities alone cannot provide a rank over
successive peaks.
"""

from __future__ import annotations

from math import gcd


def audit(stages: int = 64) -> list[dict[str, int]]:
    # Repeated defect pattern 1 < 5 > 1 < 5 > ...
    a = e = 1
    d = 5
    delta = 2 * d - e

    # At each peak p = 4r-12 and x = 2r-7.  Both strict inequalities
    # are saturated with integer slack one.  Two reset transitions send
    # p to 9p-3a-d = 9p-8, preserving this form:
    # r -> 9r-26.
    #
    # Choosing r == 5 (mod 7) makes gcd(r, x)=1 at every stage, since
    # 9r-26 == 2r+2 == 5 (mod 7) whenever r == 5 (mod 7).
    r = 12
    rows: list[dict[str, int]] = []

    for stage in range(stages):
        p = 4 * r - 12
        x = 2 * r - 7
        gp = gcd(p, x)
        gr = gcd(r, x)
        ge = gcd(e, x)

        assert a < d and e < d
        assert d < r < p / 2
        assert r > delta

        # Proper ambient-root/Fine--Wilf bound.
        assert x < p
        assert 2 * x + gp < p

        # Co-terminal G^2/Q^3 large-root branch.
        assert x > e + ge

        # Sole outer-overlap affine crossing branch.
        assert x > 2 * (r - d) + e + gr
        assert x > r

        # Exact gcd identities used by the closed-form family.
        assert gp == gr == ge == 1

        rows.append(
            {
                "stage": stage,
                "p": p,
                "r": r,
                "x": x,
                "ambient_slack": p - (2 * x + gp),
                "crossing_slack": (
                    x - (2 * (r - d) + e + gr)
                ),
            }
        )

        p_next = 9 * p - 3 * a - d
        r_next = 9 * r - 26
        assert r_next % 7 == 5
        assert p_next == 4 * r_next - 12
        r = r_next

    return rows


def main() -> None:
    rows = audit()
    print(f"stages={len(rows)}")
    print(f"first={rows[0]}")
    print(f"last={rows[-1]}")


if __name__ == "__main__":
    main()
