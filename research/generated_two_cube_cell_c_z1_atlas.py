"""Definition-first transition atlas for the surviving Cell C ``z=1`` row.

The scanner constructs both simultaneous-boundary normal forms directly and
imports neither production Cell C search.  Every canonical witness is
recomputed from the suffix-power definition.  Its finite results are
``COMPUTED`` evidence, not a proof of the remaining word wall.
"""

from __future__ import annotations

import argparse
import json
import time
from collections import Counter
from collections.abc import Iterator, Sequence
from dataclasses import asdict, dataclass
from itertools import product
from math import gcd
from pathlib import Path


Word = tuple[int, ...]
Witness = tuple[int, int]
StringCounter = tuple[tuple[str, int], ...]


@dataclass(frozen=True)
class Z1Model:
    """One exact structural word in either period branch."""

    branch: str
    q: int
    r: int
    p: int
    P: int
    seam: str
    B: Word
    Theta: Word
    D: Word
    Q: Word
    U: Word
    R: Word
    X: Word


@dataclass(frozen=True)
class BranchAtlasSummary:
    """Deterministic counters for one bounded period branch."""

    branch: str
    max_q: int
    structured_assignments: int
    z1_structural_assignments: int
    static_candidates: int
    seam_structured_counts: StringCounter
    seam_static_counts: StringCounter
    phase_one_label_counts: StringCounter
    phase_one_pair_counts: tuple[
        tuple[Witness, Witness, int], ...
    ]
    phase_one_period_cap_candidates: int
    phase_one_equal_local: int
    phase_one_equal_crossing: int
    phase_one_different_crossing: int
    phase_one_unclassified: int
    early_failure_counts: StringCounter
    late_failure_counts: StringCounter
    joint_failure_counts: tuple[tuple[str, str, int], ...]
    first_divergence_counts: StringCounter
    divergence_relative_counts: StringCounter
    synchronized_failure_candidates: int
    desynchronized_failure_candidates: int
    early_endpoint_exact: int
    late_endpoint_exact: int
    both_endpoints_exact: int
    early_predecessor_label_matches: int
    late_predecessor_label_matches: int
    both_predecessor_labels_match: int
    r1_static_candidates: int
    r1_phase_one_both_label_two: int
    r1_late_endpoint_exact: int


@dataclass(frozen=True)
class Z1TransitionAtlas:
    """Complete two-branch atlas at one bound."""

    max_q: int
    pgtq: BranchAtlasSummary
    pltq: BranchAtlasSummary


@dataclass(frozen=True)
class TransitionCertificate:
    """Fully recomputable sharpness or countermodel certificate."""

    name: str
    branch: str
    q: int
    r: int
    p: int
    P: int
    seam: str
    B: Word
    Theta: Word
    D: Word
    Q: Word
    U: Word
    R: Word
    X: Word
    early_phase_one: Witness
    late_phase_one: Witness
    early_failure_phase: int | None
    late_failure_phase: int | None
    first_divergence_phase: int | None
    early_endpoint: Witness
    late_endpoint: Witness
    early_pairs: tuple[Witness, ...]
    late_pairs: tuple[Witness, ...]


def definition_first_witness(sequence: Sequence[int]) -> Witness:
    """Return maximal suffix exponent and its least maximizing period."""

    word = tuple(sequence)
    if not word:
        raise ValueError("definition_first_witness requires a nonempty word")

    length = len(word)
    best_exponent = 1
    best_period = length
    for period in range(1, length // 2 + 1):
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
    run = 0
    for symbol in reversed(word):
        if symbol != 3:
            break
        run += 1
    return run


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


def _iter_pgtq_models(max_q: int) -> Iterator[Z1Model]:
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
                        yield Z1Model(
                            branch="p>q",
                            q=q,
                            r=r,
                            p=p,
                            P=q + r,
                            seam="none",
                            B=B,
                            Theta=(),
                            D=(),
                            Q=Q,
                            U=U,
                            R=R,
                            X=X,
                        )


def _iter_pltq_models(max_q: int) -> Iterator[Z1Model]:
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
                            seams = (
                                ("D=B[c:]Theta", B[c:] + Theta),
                            )

                        for seam, D in seams:
                            Q = Theta + B * 2 + D
                            U = Q + B
                            R = B + Q + B
                            X = D + B * 2
                            yield Z1Model(
                                branch="p<q",
                                q=q,
                                r=r,
                                p=p,
                                P=P,
                                seam=seam,
                                B=B,
                                Theta=Theta,
                                D=D,
                                Q=Q,
                                U=U,
                                R=R,
                                X=X,
                            )


def _is_z1_structural(model: Z1Model) -> bool:
    return (
        model.U.index(2) == 1
        and _first_mismatch(model.X, model.U) == 0
        and _terminal_three_run(model.B) <= 1
    )


def _is_static_candidate(model: Z1Model) -> bool:
    witness = definition_first_witness
    if witness(model.R * 2) != (2, model.q):
        return False
    if witness(model.R * 2 + model.B)[0] != 2:
        return False
    if witness(model.B + model.R + model.B * 2) != (3, model.r):
        return False
    if witness(model.X * 3) != (3, model.p):
        return False
    F = model.X * 3 + model.U + model.B * 2
    return witness(F) == (3, model.r)


def iter_z1_branch_models(
    *,
    branch: str,
    max_q: int,
) -> Iterator[Z1Model]:
    """Yield every exact structural model in one D-034 period branch."""

    if type(max_q) is not int or max_q <= 0:
        raise ValueError("max_q must be a positive integer")
    if branch == "p>q":
        return _iter_pgtq_models(max_q)
    if branch == "p<q":
        return _iter_pltq_models(max_q)
    raise ValueError("branch must be 'p>q' or 'p<q'")


def _has_public_model_shape(model: object) -> bool:
    """Fail-closed shape guard for public downstream predicates."""

    if type(model) is not Z1Model:
        return False
    words = (
        model.B,
        model.Theta,
        model.D,
        model.Q,
        model.U,
        model.R,
        model.X,
    )
    return (
        type(model.branch) is str
        and model.branch in ("p>q", "p<q")
        and type(model.seam) is str
        and all(
            type(value) is int and value > 0
            for value in (model.q, model.r, model.p, model.P)
        )
        and model.q > 2 * model.r
        and model.P == model.q + model.r
        and all(
            type(word) is tuple
            and all(
                type(symbol) is int and symbol in (2, 3)
                for symbol in word
            )
            for word in words
        )
        and len(model.B) == model.r
        and len(model.Q) == model.q - 2 * model.r
        and len(model.U) == model.q - model.r
        and len(model.R) == model.q
        and len(model.X) == model.p
        and model.B[0] == 2
        and model.Q[0] == 3
        and model.U == model.Q + model.B
        and model.R == model.B + model.Q + model.B
    )


def is_z1_structural(model: object) -> bool:
    """Public exact-row predicate for downstream definition-first audits."""

    if not _has_public_model_shape(model):
        return False
    try:
        return _is_z1_structural(model)
    except (IndexError, TypeError, ValueError, ZeroDivisionError):
        return False


def is_z1_static_candidate(model: object) -> bool:
    """Public D-034 static predicate for downstream bridge enumeration."""

    if not _has_public_model_shape(model):
        return False
    try:
        return _is_static_candidate(model)
    except (IndexError, TypeError, ValueError, ZeroDivisionError):
        return False


def _counter_tuple(counter: Counter[str]) -> StringCounter:
    return tuple(sorted(counter.items()))


def _phase_key(phase: int | None) -> str:
    return "complete" if phase is None else str(phase)


def _scan_branch(
    *,
    branch: str,
    max_q: int,
    models: Iterator[Z1Model],
) -> BranchAtlasSummary:
    structured_assignments = 0
    z1_structural_assignments = 0
    static_candidates = 0
    seam_structured: Counter[str] = Counter()
    seam_static: Counter[str] = Counter()
    phase_one_labels: Counter[str] = Counter(
        {
            "both_2": 0,
            "early_2_only": 0,
            "late_2_only": 0,
            "neither_2": 0,
        }
    )
    phase_one_pairs: Counter[tuple[Witness, Witness]] = Counter()
    phase_one_period_cap_candidates = 0
    phase_one_equal_local = 0
    phase_one_equal_crossing = 0
    phase_one_different_crossing = 0
    phase_one_unclassified = 0
    early_failures: Counter[str] = Counter()
    late_failures: Counter[str] = Counter()
    joint_failures: Counter[tuple[str, str]] = Counter()
    first_divergences: Counter[str] = Counter()
    divergence_relative: Counter[str] = Counter()
    synchronized_failure_candidates = 0
    desynchronized_failure_candidates = 0
    early_endpoint_exact = 0
    late_endpoint_exact = 0
    both_endpoints_exact = 0
    early_predecessor_label_matches = 0
    late_predecessor_label_matches = 0
    both_predecessor_labels_match = 0
    r1_static_candidates = 0
    r1_phase_one_both_label_two = 0
    r1_late_endpoint_exact = 0
    witness = definition_first_witness

    for model in models:
        structured_assignments += 1
        seam_structured[model.seam] += 1
        if not _is_z1_structural(model):
            continue
        z1_structural_assignments += 1
        if not _is_static_candidate(model):
            continue

        static_candidates += 1
        seam_static[model.seam] += 1
        if model.r == 1:
            r1_static_candidates += 1

        early_start = model.X * 3
        late_start = early_start + model.U + model.B * 2
        early_phase_one = witness(early_start + (3,))
        late_phase_one = witness(late_start + (3,))
        phase_one_pairs[(early_phase_one, late_phase_one)] += 1

        early_is_two = early_phase_one[0] == 2
        late_is_two = late_phase_one[0] == 2
        if early_is_two and late_is_two:
            phase_one_labels["both_2"] += 1
            if (
                early_phase_one[1] < model.P
                and late_phase_one[1] < model.P
            ):
                phase_one_period_cap_candidates += 1
            if (
                early_phase_one == late_phase_one
                and early_phase_one[1] < model.r
            ):
                phase_one_equal_local += 1
            elif (
                early_phase_one == late_phase_one
                and early_phase_one[1] > model.r
            ):
                phase_one_equal_crossing += 1
            elif (
                early_phase_one != late_phase_one
                and early_phase_one[1] > model.r
                and late_phase_one[1] > model.r
            ):
                phase_one_different_crossing += 1
            else:
                phase_one_unclassified += 1
            if model.r == 1:
                r1_phase_one_both_label_two += 1
        elif early_is_two:
            phase_one_labels["early_2_only"] += 1
        elif late_is_two:
            phase_one_labels["late_2_only"] += 1
        else:
            phase_one_labels["neither_2"] += 1

        early_state = early_start + (3,)
        late_state = late_start + (3,)
        early_failure: int | None = None
        late_failure: int | None = None
        first_divergence: int | None = None
        cached_early: dict[int, Witness] = {1: early_phase_one}
        cached_late: dict[int, Witness] = {1: late_phase_one}

        for phase in range(1, len(model.U) + 1):
            early_pair = (
                early_phase_one
                if phase == 1
                else witness(early_state)
            )
            late_pair = (
                late_phase_one
                if phase == 1
                else witness(late_state)
            )
            cached_early[phase] = early_pair
            cached_late[phase] = late_pair
            if (
                first_divergence is None
                and early_pair != late_pair
            ):
                first_divergence = phase

            if phase < len(model.U):
                expected = model.U[phase]
                if (
                    early_failure is None
                    and early_pair[0] != expected
                ):
                    early_failure = phase
                if (
                    late_failure is None
                    and late_pair[0] != expected
                ):
                    late_failure = phase

            if (
                first_divergence is not None
                and early_failure is not None
                and late_failure is not None
            ):
                break
            if phase < len(model.U):
                early_state += (model.U[phase],)
                late_state += (model.U[phase],)

        early_key = _phase_key(early_failure)
        late_key = _phase_key(late_failure)
        divergence_key = _phase_key(first_divergence)
        early_failures[early_key] += 1
        late_failures[late_key] += 1
        joint_failures[(early_key, late_key)] += 1
        first_divergences[divergence_key] += 1
        if early_failure == late_failure:
            synchronized_failure_candidates += 1
        else:
            desynchronized_failure_candidates += 1

        failure_boundary = min(
            len(model.U) if early_failure is None else early_failure,
            len(model.U) if late_failure is None else late_failure,
        )
        if first_divergence is None:
            divergence_relative["none"] += 1
        elif first_divergence < failure_boundary:
            divergence_relative["before_first_failure"] += 1
        elif first_divergence == failure_boundary:
            divergence_relative["at_first_failure"] += 1
        else:
            divergence_relative["after_first_failure"] += 1

        endpoint_phase = len(model.U)
        predecessor_phase = endpoint_phase - 1
        early_endpoint = cached_early.get(endpoint_phase)
        if early_endpoint is None:
            early_endpoint = witness(early_start + model.U)
        late_endpoint = cached_late.get(endpoint_phase)
        if late_endpoint is None:
            late_endpoint = witness(late_start + model.U)
        early_predecessor = cached_early.get(predecessor_phase)
        if early_predecessor is None:
            early_predecessor = witness(
                early_start + model.U[:-1]
            )
        late_predecessor = cached_late.get(predecessor_phase)
        if late_predecessor is None:
            late_predecessor = witness(
                late_start + model.U[:-1]
            )

        early_exact = early_endpoint == (2, model.q)
        late_exact = late_endpoint == (2, model.P)
        early_endpoint_exact += early_exact
        late_endpoint_exact += late_exact
        both_endpoints_exact += early_exact and late_exact
        if model.r == 1:
            r1_late_endpoint_exact += late_exact

        last_symbol = model.U[-1]
        early_pre_matches = early_predecessor[0] == last_symbol
        late_pre_matches = late_predecessor[0] == last_symbol
        early_predecessor_label_matches += early_pre_matches
        late_predecessor_label_matches += late_pre_matches
        both_predecessor_labels_match += (
            early_pre_matches and late_pre_matches
        )

    return BranchAtlasSummary(
        branch=branch,
        max_q=max_q,
        structured_assignments=structured_assignments,
        z1_structural_assignments=z1_structural_assignments,
        static_candidates=static_candidates,
        seam_structured_counts=_counter_tuple(seam_structured),
        seam_static_counts=_counter_tuple(seam_static),
        phase_one_label_counts=_counter_tuple(phase_one_labels),
        phase_one_pair_counts=tuple(
            (early, late, count)
            for (early, late), count in sorted(
                phase_one_pairs.items()
            )
        ),
        phase_one_period_cap_candidates=(
            phase_one_period_cap_candidates
        ),
        phase_one_equal_local=phase_one_equal_local,
        phase_one_equal_crossing=phase_one_equal_crossing,
        phase_one_different_crossing=phase_one_different_crossing,
        phase_one_unclassified=phase_one_unclassified,
        early_failure_counts=_counter_tuple(early_failures),
        late_failure_counts=_counter_tuple(late_failures),
        joint_failure_counts=tuple(
            (early, late, count)
            for (early, late), count in sorted(
                joint_failures.items()
            )
        ),
        first_divergence_counts=_counter_tuple(first_divergences),
        divergence_relative_counts=_counter_tuple(
            divergence_relative
        ),
        synchronized_failure_candidates=(
            synchronized_failure_candidates
        ),
        desynchronized_failure_candidates=(
            desynchronized_failure_candidates
        ),
        early_endpoint_exact=early_endpoint_exact,
        late_endpoint_exact=late_endpoint_exact,
        both_endpoints_exact=both_endpoints_exact,
        early_predecessor_label_matches=(
            early_predecessor_label_matches
        ),
        late_predecessor_label_matches=(
            late_predecessor_label_matches
        ),
        both_predecessor_labels_match=(
            both_predecessor_labels_match
        ),
        r1_static_candidates=r1_static_candidates,
        r1_phase_one_both_label_two=(
            r1_phase_one_both_label_two
        ),
        r1_late_endpoint_exact=r1_late_endpoint_exact,
    )


def scan_z1_transition_atlas(*, max_q: int) -> Z1TransitionAtlas:
    """Scan both exact simultaneous-boundary branches."""

    if max_q <= 0:
        raise ValueError("max_q must be positive")
    return Z1TransitionAtlas(
        max_q=max_q,
        pgtq=_scan_branch(
            branch="p>q",
            max_q=max_q,
            models=_iter_pgtq_models(max_q),
        ),
        pltq=_scan_branch(
            branch="p<q",
            max_q=max_q,
            models=_iter_pltq_models(max_q),
        ),
    )


def _failure_phase(
    pairs: Sequence[Witness],
    continuation: Word,
) -> int | None:
    return next(
        (
            phase
            for phase, expected in enumerate(continuation)
            if pairs[phase][0] != expected
        ),
        None,
    )


def _make_certificate(
    *,
    name: str,
    q: int,
    r: int,
    p: int,
    seam: str,
    B: str,
    Theta: str,
    D: str,
    Q: str,
    U: str,
    R: str,
    X: str,
) -> TransitionCertificate:
    words = {
        key: tuple(map(int, value))
        for key, value in {
            "B": B,
            "Theta": Theta,
            "D": D,
            "Q": Q,
            "U": U,
            "R": R,
            "X": X,
        }.items()
    }
    early_start = words["X"] * 3
    late_start = early_start + words["U"] + words["B"] * 2
    early_pairs = tuple(
        definition_first_witness(early_start + words["U"][:phase])
        for phase in range(len(words["U"]) + 1)
    )
    late_pairs = tuple(
        definition_first_witness(late_start + words["U"][:phase])
        for phase in range(len(words["U"]) + 1)
    )
    first_divergence = next(
        (
            phase
            for phase in range(1, len(words["U"]) + 1)
            if early_pairs[phase] != late_pairs[phase]
        ),
        None,
    )
    return TransitionCertificate(
        name=name,
        branch="p<q",
        q=q,
        r=r,
        p=p,
        P=q + r,
        seam=seam,
        B=words["B"],
        Theta=words["Theta"],
        D=words["D"],
        Q=words["Q"],
        U=words["U"],
        R=words["R"],
        X=words["X"],
        early_phase_one=early_pairs[1],
        late_phase_one=late_pairs[1],
        early_failure_phase=_failure_phase(
            early_pairs, words["U"]
        ),
        late_failure_phase=_failure_phase(
            late_pairs, words["U"]
        ),
        first_divergence_phase=first_divergence,
        early_endpoint=early_pairs[-1],
        late_endpoint=late_pairs[-1],
        early_pairs=early_pairs,
        late_pairs=late_pairs,
    )


def known_transition_certificates() -> tuple[TransitionCertificate, ...]:
    """Return the six audited sharpness and countermodel words."""

    return (
        _make_certificate(
            name="q8_r1_high_endpoint_failure",
            q=8,
            r=1,
            p=5,
            seam="D=JBTheta",
            B="2",
            Theta="3",
            D="223",
            Q="322223",
            U="3222232",
            R="23222232",
            X="22322",
        ),
        _make_certificate(
            name="q9_r1_high_endpoint_correct",
            q=9,
            r=1,
            p=6,
            seam="D=JBTheta",
            B="2",
            Theta="3",
            D="2223",
            Q="3222223",
            U="32222232",
            R="232222232",
            X="222322",
        ),
        _make_certificate(
            name="q11_r1_desynchronized_failure",
            q=11,
            r=1,
            p=8,
            seam="D=JBTheta",
            B="2",
            Theta="3",
            D="233223",
            Q="322233223",
            U="3222332232",
            R="23222332232",
            X="23322322",
        ),
        _make_certificate(
            name="q16_r2_root_divergence",
            q=16,
            r=2,
            p=10,
            seam="D=JBTheta",
            B="23",
            Theta="32",
            D="232332",
            Q="322323232332",
            U="32232323233223",
            R="2332232323233223",
            X="2323322323",
        ),
        _make_certificate(
            name="q23_overlap_long_replay",
            q=23,
            r=4,
            p=13,
            seam="D=B[c:]Theta",
            B="2232",
            Theta="32",
            D="23232",
            Q="322232223223232",
            U="3222322232232322232",
            R="22323222322232232322232",
            X="2323222322232",
        ),
        _make_certificate(
            name="q29_r4_high_static",
            q=29,
            r=4,
            p=20,
            seam="D=JBTheta",
            B="2332",
            Theta="3",
            D="233233223323",
            Q="323322332233233223323",
            U="3233223322332332233232332",
            R="23323233223322332332233232332",
            X="23323322332323322332",
        ),
    )


def audit_transition_certificate(
    certificate: TransitionCertificate,
) -> bool:
    """Recompute every word identity, static pair, and stored trace."""

    B = certificate.B
    Theta = certificate.Theta
    D = certificate.D
    Q = certificate.Q
    U = certificate.U
    R = certificate.R
    X = certificate.X
    q = certificate.q
    r = certificate.r
    p = certificate.p
    P = certificate.P
    if (
        certificate.branch != "p<q"
        or P != q + r
        or not q > 4 * r
        or not p > 2 * r
        or not q - p == 2 * r + len(Theta)
        or not len(D) == p - 2 * r
        or not len(D) > len(Theta)
        or not r < p - gcd(p, q)
        or not p > r + gcd(p, r)
        or len(B) != r
        or len(R) != q
        or len(X) != p
        or U != Q + B
        or R != B + Q + B
        or Q != Theta + B * 2 + D
        or X != D + B * 2
        or B[0] != 2
        or Theta[0] != 3
        or U.index(2) != 1
        or _first_mismatch(X, U) != 0
        or _terminal_three_run(B) > 1
    ):
        return False

    e = 2 * p - P
    if certificate.seam == "D=JBTheta":
        if e < 0 or D[e:] != B + Theta:
            return False
    elif certificate.seam == "D=B[c:]Theta":
        c = -e
        if (
            e >= 0
            or not 0 < 2 * c < r
            or B[:c] != B[-c:]
            or D != B[c:] + Theta
        ):
            return False
    else:
        return False

    witness = definition_first_witness
    early_start = X * 3
    late_start = early_start + U + B * 2
    early_pairs = tuple(
        witness(early_start + U[:phase])
        for phase in range(len(U) + 1)
    )
    late_pairs = tuple(
        witness(late_start + U[:phase])
        for phase in range(len(U) + 1)
    )
    first_divergence = next(
        (
            phase
            for phase in range(1, len(U) + 1)
            if early_pairs[phase] != late_pairs[phase]
        ),
        None,
    )
    return (
        witness(R * 2) == (2, q)
        and witness(R * 2 + B)[0] == 2
        and witness(B + R + B * 2) == (3, r)
        and witness(early_start) == (3, p)
        and witness(late_start) == (3, r)
        and certificate.early_phase_one == early_pairs[1]
        and certificate.late_phase_one == late_pairs[1]
        and certificate.early_failure_phase
        == _failure_phase(early_pairs, U)
        and certificate.late_failure_phase
        == _failure_phase(late_pairs, U)
        and certificate.first_divergence_phase
        == first_divergence
        and certificate.early_endpoint == early_pairs[-1]
        and certificate.late_endpoint == late_pairs[-1]
        and certificate.early_pairs == early_pairs
        and certificate.late_pairs == late_pairs
    )


def _json(value) -> str:
    return json.dumps(
        value,
        separators=(",", ":"),
        sort_keys=True,
    )


def _render_branch(summary: BranchAtlasSummary) -> list[str]:
    prefix = "pgtq" if summary.branch == "p>q" else "pltq"
    fields = (
        "structured_assignments",
        "z1_structural_assignments",
        "static_candidates",
        "phase_one_period_cap_candidates",
        "phase_one_equal_local",
        "phase_one_equal_crossing",
        "phase_one_different_crossing",
        "phase_one_unclassified",
        "synchronized_failure_candidates",
        "desynchronized_failure_candidates",
        "early_endpoint_exact",
        "late_endpoint_exact",
        "both_endpoints_exact",
        "early_predecessor_label_matches",
        "late_predecessor_label_matches",
        "both_predecessor_labels_match",
        "r1_static_candidates",
        "r1_phase_one_both_label_two",
        "r1_late_endpoint_exact",
    )
    lines = [
        f"{prefix}.branch={summary.branch}",
        *(f"{prefix}.{field}={getattr(summary, field)}" for field in fields),
        f"{prefix}.seam_structured_counts="
        + _json(dict(summary.seam_structured_counts)),
        f"{prefix}.seam_static_counts="
        + _json(dict(summary.seam_static_counts)),
        f"{prefix}.phase_one_label_counts="
        + _json(dict(summary.phase_one_label_counts)),
        f"{prefix}.phase_one_pair_counts="
        + _json(summary.phase_one_pair_counts),
        f"{prefix}.early_failure_counts="
        + _json(dict(summary.early_failure_counts)),
        f"{prefix}.late_failure_counts="
        + _json(dict(summary.late_failure_counts)),
        f"{prefix}.joint_failure_counts="
        + _json(summary.joint_failure_counts),
        f"{prefix}.first_divergence_counts="
        + _json(dict(summary.first_divergence_counts)),
        f"{prefix}.divergence_relative_counts="
        + _json(dict(summary.divergence_relative_counts)),
    ]
    return lines


def render_atlas(
    atlas: Z1TransitionAtlas,
    certificates: Sequence[TransitionCertificate],
) -> str:
    """Render a byte-stable checkpoint with explicit scope labels."""

    if any(
        not audit_transition_certificate(certificate)
        for certificate in certificates
    ):
        raise ValueError("invalid transition certificate")
    lines = [
        "label=bounded_binary_cell_C_z1_transition_atlas",
        f"max_q={atlas.max_q}",
        "alphabet=2,3",
        "status=COMPUTED",
        "row=z1_h0",
        "target_scope=sampled_E_and_F_windows_only",
        "bridge_scope=not_enumerated",
        "Cell_C=OPEN",
        *_render_branch(atlas.pgtq),
        *_render_branch(atlas.pltq),
        f"certificate_count={len(certificates)}",
    ]
    lines.extend(
        "certificate="
        + _json(asdict(certificate))
        for certificate in certificates
    )
    lines.append(
        "NOT_A_PROOF: bounded binary z1 transition atlas; "
        "zero bounded replays does not close either word wall or Cell C."
    )
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build the exact bounded Cell C z=1 transition atlas."
    )
    parser.add_argument("--max-q", type=int, default=25)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args(argv)

    started = time.perf_counter()
    atlas = scan_z1_transition_atlas(max_q=arguments.max_q)
    certificates = known_transition_certificates()
    rendered = render_atlas(atlas, certificates)
    if arguments.output is None:
        print(rendered, end="")
    else:
        arguments.output.write_bytes(rendered.encode("utf-8"))
    elapsed = time.perf_counter() - started
    print(f"scan_seconds={elapsed:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
