"""Definition-first finite checks for the Cell C double-``3`` row.

This module is intentionally independent of both production Cell C searches.
It constructs the two simultaneous-boundary normal forms directly and
recomputes canonical witnesses from the definition.  The scans are bounded
regressions, not the proof of the unbounded elimination.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Sequence
from dataclasses import dataclass
from itertools import product
from math import gcd


Word = tuple[int, ...]
Witness = tuple[int, int]


@dataclass(frozen=True)
class DoubleThreeScanSummary:
    """Exact counts for one bounded period branch."""

    branch: str
    max_q: int
    structured_assignments: int
    retained_z2_candidates: int
    z2_h0_candidates: int
    z2_h1_candidates: int
    z2_h0_f1_kappa_counts: tuple[tuple[int, int], ...]
    z2_h1_f1_kappa_counts: tuple[tuple[int, int], ...]
    seam_row_counts: tuple[tuple[str, int, int], ...]
    f1_label_three_candidates: int


@dataclass(frozen=True)
class Z1EndpointNearModel:
    """Endpoint-correct ``q=23`` sharpness model for the surviving row."""

    q: int
    r: int
    p: int
    P: int
    nu: int
    c: int
    B: Word
    Theta: Word
    D: Word
    Q: Word
    U: Word
    R: Word
    X: Word
    A: Word
    C: Word
    H0: Word
    z: int
    h: int
    matched_phases: int
    failure_phase: int
    early_pairs: tuple[Witness, ...]
    late_pairs: tuple[Witness, ...]


def definition_first_witness(sequence: Sequence[int]) -> Witness:
    """Return ``(kappa, pi)`` by literal suffix-block enumeration."""

    word = tuple(sequence)
    if not word:
        raise ValueError("definition_first_witness requires a nonempty word")

    length = len(word)
    best_exponent = 1
    best_period = length
    for period in range(1, length + 1):
        block = word[length - period :]
        exponent = 1
        cursor = length - 2 * period
        while cursor >= 0 and word[cursor : cursor + period] == block:
            exponent += 1
            cursor -= period
        if exponent > best_exponent or (
            exponent == best_exponent
            and exponent >= 2
            and period < best_period
        ):
            best_exponent = exponent
            best_period = period
    return best_exponent, best_period


def _terminal_three_run(word: Word) -> int:
    length = 0
    for symbol in reversed(word):
        if symbol != 3:
            break
        length += 1
    return length


def _first_mismatch(X: Word, U: Word) -> int | None:
    period = len(X)
    return next(
        (
            index
            for index, symbol in enumerate(U)
            if symbol != X[index % period]
        ),
        None,
    )


def _scan_candidate(
    *,
    q: int,
    r: int,
    p: int,
    B: Word,
    Q: Word,
    U: Word,
    R: Word,
    X: Word,
) -> tuple[int, int, int] | None:
    """Return ``(h, kappa(F1), rho(F1))`` for a retained ``z=2`` row."""

    if len(B) != r or len(R) != q or len(X) != p:
        raise AssertionError("model lengths do not match q, r, p")
    if R != B + Q + B or U != Q + B:
        raise AssertionError("model words do not match R=BQB, U=QB")

    if definition_first_witness(R * 2) != (2, q):
        return None
    if definition_first_witness(R * 2 + B)[0] != 2:
        return None
    if definition_first_witness(B + R + B * 2) != (3, r):
        return None
    if definition_first_witness(X * 3) != (3, p):
        return None

    F = X * 3 + U + B * 2
    if definition_first_witness(F) != (3, r):
        return None

    z = U.index(2)
    h = _first_mismatch(X, U)
    if (
        z != 2
        or h not in (0, 1)
        or _terminal_three_run(B) + z > 2
    ):
        return None

    kappa, rho = definition_first_witness(F + (3,))
    return h, kappa, rho


def _summary(
    *,
    branch: str,
    max_q: int,
    structured_assignments: int,
    retained_z2_candidates: int,
    row_counts: Counter[int],
    f1_counts: dict[int, Counter[int]],
    seam_counts: dict[str, Counter[int]],
) -> DoubleThreeScanSummary:
    return DoubleThreeScanSummary(
        branch=branch,
        max_q=max_q,
        structured_assignments=structured_assignments,
        retained_z2_candidates=retained_z2_candidates,
        z2_h0_candidates=row_counts[0],
        z2_h1_candidates=row_counts[1],
        z2_h0_f1_kappa_counts=tuple(sorted(f1_counts[0].items())),
        z2_h1_f1_kappa_counts=tuple(sorted(f1_counts[1].items())),
        seam_row_counts=tuple(
            (seam, counts[0], counts[1])
            for seam, counts in seam_counts.items()
        ),
        f1_label_three_candidates=f1_counts[0][3] + f1_counts[1][3],
    )


def scan_pgtq_double_three(*, max_q: int) -> DoubleThreeScanSummary:
    """Scan the exact ``p>q`` normal form through ``q=max_q``."""

    if max_q <= 0:
        raise ValueError("max_q must be positive")

    structured_assignments = 0
    retained_z2_candidates = 0
    row_counts: Counter[int] = Counter()
    f1_counts = {0: Counter(), 1: Counter()}

    for q in range(1, max_q + 1):
        for r in range(1, (q - 1) // 2 + 1):
            prefix_length = q - 2 * r
            for t in range(r // 2 + 1, r):
                if 2 * t <= r:
                    continue
                p = q + t
                for B_tail in product((2, 3), repeat=t - 1):
                    seed = (2,) + B_tail
                    B = tuple(seed[index % t] for index in range(r))
                    for Q_tail in product(
                        (2, 3), repeat=prefix_length - 1
                    ):
                        Q = (3,) + Q_tail
                        U = Q + B
                        R = B + Q + B
                        X = B[r - t :] + U + B
                        structured_assignments += 1

                        result = _scan_candidate(
                            q=q,
                            r=r,
                            p=p,
                            B=B,
                            Q=Q,
                            U=U,
                            R=R,
                            X=X,
                        )
                        if result is None:
                            continue
                        retained_z2_candidates += 1
                        h, kappa, _rho = result
                        row_counts[h] += 1
                        f1_counts[h][kappa] += 1

    return _summary(
        branch="p>q",
        max_q=max_q,
        structured_assignments=structured_assignments,
        retained_z2_candidates=retained_z2_candidates,
        row_counts=row_counts,
        f1_counts=f1_counts,
        seam_counts={},
    )


def scan_pltq_double_three(*, max_q: int) -> DoubleThreeScanSummary:
    """Scan both exact ``p<q`` seams through ``q=max_q``."""

    if max_q <= 0:
        raise ValueError("max_q must be positive")

    structured_assignments = 0
    retained_z2_candidates = 0
    row_counts: Counter[int] = Counter()
    f1_counts = {0: Counter(), 1: Counter()}
    seam_counts = {
        "D=JBTheta": Counter(),
        "D=B[c:]Theta": Counter(),
    }

    for r in range(1, (max_q - 1) // 4 + 1):
        for nu in range(1, max_q + 1):
            for sigma in range(nu + 1, max_q + 1):
                q = 4 * r + nu + sigma
                if q > max_q:
                    break
                p = 2 * r + sigma
                P = q + r
                if not (
                    r < p - gcd(p, q)
                    and p > r + gcd(p, r)
                ):
                    continue

                e = 2 * p - P
                for B_tail in product((2, 3), repeat=r - 1):
                    B = (2,) + B_tail
                    for Theta_tail in product(
                        (2, 3), repeat=nu - 1
                    ):
                        Theta = (3,) + Theta_tail

                        if e >= 0:
                            seams = (
                                (
                                    "D=JBTheta",
                                    J + B + Theta,
                                )
                                for J in product((2, 3), repeat=e)
                            )
                        else:
                            c = -e
                            if (
                                2 * c >= r
                                or B[:c] != B[-c:]
                            ):
                                continue
                            seams = (("D=B[c:]Theta", B[c:] + Theta),)

                        for seam, D in seams:
                            Q = Theta + B * 2 + D
                            U = Q + B
                            R = B + Q + B
                            X = D + B * 2
                            structured_assignments += 1

                            result = _scan_candidate(
                                q=q,
                                r=r,
                                p=p,
                                B=B,
                                Q=Q,
                                U=U,
                                R=R,
                                X=X,
                            )
                            if result is None:
                                continue
                            retained_z2_candidates += 1
                            h, kappa, _rho = result
                            row_counts[h] += 1
                            f1_counts[h][kappa] += 1
                            seam_counts[seam][h] += 1

    return _summary(
        branch="p<q",
        max_q=max_q,
        structured_assignments=structured_assignments,
        retained_z2_candidates=retained_z2_candidates,
        row_counts=row_counts,
        f1_counts=f1_counts,
        seam_counts=seam_counts,
    )


def q23_z1_endpoint_near_model() -> Z1EndpointNearModel:
    """Return the exact endpoint-correct model that first fails at phase 13."""

    q, r, p = 23, 4, 13
    P = q + r
    nu = q - p - 2 * r
    c = P - 2 * p
    B = tuple(map(int, "2232"))
    Theta = tuple(map(int, "32"))
    D = tuple(map(int, "23232"))
    Q = tuple(map(int, "322232223223232"))
    U = tuple(map(int, "3222322232232322232"))
    R = tuple(map(int, "22323222322232232322232"))
    X = tuple(map(int, "2323222322232"))
    A = B[c:]
    C = Theta + B * 2
    H0 = Theta + B

    early_start = X * 3
    late_start = early_start + U + B * 2
    early_pairs = tuple(
        definition_first_witness(early_start + U[:phase])
        for phase in range(len(U) + 1)
    )
    late_pairs = tuple(
        definition_first_witness(late_start + U[:phase])
        for phase in range(len(U) + 1)
    )
    early_failure = next(
        phase
        for phase, expected in enumerate(U)
        if early_pairs[phase][0] != expected
    )
    late_failure = next(
        phase
        for phase, expected in enumerate(U)
        if late_pairs[phase][0] != expected
    )
    if early_failure != late_failure:
        raise AssertionError("the pinned traces must fail together")

    return Z1EndpointNearModel(
        q=q,
        r=r,
        p=p,
        P=P,
        nu=nu,
        c=c,
        B=B,
        Theta=Theta,
        D=D,
        Q=Q,
        U=U,
        R=R,
        X=X,
        A=A,
        C=C,
        H0=H0,
        z=U.index(2),
        h=_first_mismatch(X, U),
        matched_phases=early_failure,
        failure_phase=early_failure,
        early_pairs=early_pairs,
        late_pairs=late_pairs,
    )
