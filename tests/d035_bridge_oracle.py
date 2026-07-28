"""Production-independent literal oracle for the D-035 bridge census.

This module intentionally imports no D-034 generator, structural/static
predicate, production witness, bridge tracer, or certificate selector.
Both normal forms and every suffix-power witness are reconstructed directly
from their defining equations.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import product
from math import gcd


Word = tuple[int, ...]
Witness = tuple[int, int]

THEOREM_KEYS = (
    "endpoint_pair",
    "first_2_cap",
    "second_2_cap",
    "first_3_bound",
    "first_3_visibility",
    "second_3_bound",
    "second_3_visibility",
    "full_root_seam",
    "full_root_suffix",
    "full_root_terminal",
    "full_fourth_power",
    "visible_fourth_power",
)

PERIOD_P_KEYS = tuple(
    f"{half}:{requested}:{relation}P"
    for half in ("first", "second")
    for requested in (2, 3)
    for relation in ("<", "=", ">")
)

SEAM_CROSS_KEYS = tuple(
    f"{relation}:seam_{str(seam).lower()}"
    for relation in ("lt_r", "eq_r", "gt_r")
    for seam in (False, True)
)


def word(text: str) -> Word:
    return tuple(map(int, text))


def literal_witness(sequence: Word) -> Witness:
    """Return the largest literal suffix exponent and least such period."""

    feasible: dict[int, list[int]] = {}
    for exponent in range(2, len(sequence) + 1):
        for period in range(1, len(sequence) // exponent + 1):
            suffix = sequence[-exponent * period :]
            if suffix == suffix[:period] * exponent:
                feasible.setdefault(exponent, []).append(period)
    if not feasible:
        return 1, len(sequence)
    exponent = max(feasible)
    return exponent, min(feasible[exponent])


def fourth_power_roots(sequence: Word) -> tuple[int, ...]:
    return tuple(
        root
        for root in range(1, len(sequence) // 4 + 1)
        if sequence[-4 * root :] == sequence[-4 * root : -3 * root] * 4
    )


def visible_proper_fourth_roots(
    sequence: Word,
    *,
    ambient_period: int,
) -> tuple[int, ...]:
    return tuple(
        root
        for root in fourth_power_roots(sequence)
        if root < ambient_period
    )


def terminal_three_run(sequence: Word) -> int:
    run = 0
    for symbol in reversed(sequence):
        if symbol != 3:
            break
        run += 1
    return run


def ends_power(sequence: Word, *, root: int, exponent: int) -> bool:
    if root <= 0 or exponent * root > len(sequence):
        return False
    suffix = sequence[-exponent * root :]
    return suffix == suffix[:root] * exponent


def _zero_counter(keys: tuple[str, ...]) -> Counter[str]:
    return Counter({key: 0 for key in keys})


def raw_reference(max_q: int) -> dict[str, dict[str, object]]:
    """Enumerate both normal forms through ``max_q`` from literal equations."""

    summaries = {
        branch: {
            "structured_assignments": 0,
            "z1_structural_assignments": 0,
            "static_candidates": 0,
            "first_failure_phase_counts": Counter(),
            "local_bridge_replays": 0,
            "all_proper_periods_below_P_local_replays": 0,
            "local_endpoint_exact_replays": 0,
            "local_r_counts": Counter(),
            "local_B_counts": Counter(),
            "local_seam_counts": Counter(),
            "proper_cut_count": 0,
            "cut_relation_counts": Counter(),
            "period_P_relation_counts": _zero_counter(PERIOD_P_KEYS),
            "second_half_three_seam_cross_counts": _zero_counter(
                SEAM_CROSS_KEYS
            ),
            "full_fourth_power_root_occurrences": 0,
            "full_fourth_power_cut_count": 0,
            "visible_proper_fourth_root_occurrences": 0,
            "visible_proper_fourth_cut_count": 0,
            "theorem_opportunity_counts": _zero_counter(THEOREM_KEYS),
            "theorem_violation_counts": _zero_counter(THEOREM_KEYS),
        }
        for branch in ("p>q", "p<q")
    }

    def record(
        *,
        branch: str,
        q: int,
        r: int,
        p: int,
        seam: str,
        B: Word,
        Q: Word,
        U: Word,
        R: Word,
        X: Word,
    ) -> None:
        summary = summaries[branch]
        summary["structured_assignments"] += 1
        mismatch_index = next(
            (
                index
                for index, symbol in enumerate(U)
                if symbol != X[index % p]
            ),
            None,
        )
        if (
            U.index(2) != 1
            or mismatch_index != 0
            or terminal_three_run(B) > 1
        ):
            return
        summary["z1_structural_assignments"] += 1

        if not (
            literal_witness(R * 2) == (2, q)
            and literal_witness(R * 2 + B)[0] == 2
            and literal_witness(B + R + B * 2) == (3, r)
            and literal_witness(X * 3) == (3, p)
            and literal_witness(X * 3 + U + B * 2) == (3, r)
        ):
            return
        summary["static_candidates"] += 1

        P = q + r
        state = X * 3 + U
        cuts: list[
            tuple[
                str,
                int,
                int,
                Witness,
                Word,
                tuple[int, ...],
                tuple[int, ...],
                bool | None,
            ]
        ] = []
        for phase, requested in enumerate(B * 2):
            pair = literal_witness(state)
            if pair[0] != requested:
                summary["first_failure_phase_counts"][str(phase)] += 1
                return

            index = phase % r
            first_half = phase < r
            half = "first" if first_half else "second"
            bound = q if first_half else r
            visible = (
                R * 2 + B[:index]
                if first_half
                else B * 2 + B[:index]
            )
            assert state[-len(visible) :] == visible
            full_roots = fourth_power_roots(state)
            visible_roots = visible_proper_fourth_roots(
                visible,
                ambient_period=bound,
            )
            seam_holds = (
                None
                if first_half or requested != 3
                else (B + Q)[-(r - index) :] == B[index:]
            )
            cuts.append(
                (
                    half,
                    index,
                    requested,
                    pair,
                    visible,
                    full_roots,
                    visible_roots,
                    seam_holds,
                )
            )
            state += (requested,)

        summary["local_bridge_replays"] += 1
        summary["all_proper_periods_below_P_local_replays"] += all(
            pair[1] < P for _, _, _, pair, *_ in cuts
        )
        endpoint = literal_witness(state)
        summary["local_endpoint_exact_replays"] += endpoint == (3, r)
        summary["local_r_counts"][str(r)] += 1
        summary["local_B_counts"]["".join(map(str, B))] += 1
        summary["local_seam_counts"][seam] += 1

        opportunities = summary["theorem_opportunity_counts"]
        violations = summary["theorem_violation_counts"]
        opportunities["endpoint_pair"] += 1
        if endpoint != (3, r):
            violations["endpoint_pair"] += 1

        for (
            half,
            index,
            requested,
            pair,
            visible,
            full_roots,
            visible_roots,
            seam_holds,
        ) in cuts:
            summary["proper_cut_count"] += 1
            period = pair[1]
            bound = q if half == "first" else r
            scale = "q" if half == "first" else "r"
            relation = "<" if period < bound else "=" if period == bound else ">"
            summary["cut_relation_counts"][
                f"{half}:{requested}:{relation}{scale}"
            ] += 1
            P_relation = "<" if period < P else "=" if period == P else ">"
            summary["period_P_relation_counts"][
                f"{half}:{requested}:{P_relation}P"
            ] += 1

            summary["full_fourth_power_root_occurrences"] += len(full_roots)
            summary["full_fourth_power_cut_count"] += bool(full_roots)
            summary["visible_proper_fourth_root_occurrences"] += len(
                visible_roots
            )
            summary["visible_proper_fourth_cut_count"] += bool(visible_roots)
            opportunities["full_fourth_power"] += 1
            opportunities["visible_fourth_power"] += 1
            if full_roots:
                violations["full_fourth_power"] += 1
            if visible_roots:
                violations["visible_fourth_power"] += 1

            if requested == 2:
                key = f"{half}_2_cap"
                opportunities[key] += 1
                if period > bound:
                    violations[key] += 1
                continue

            if half == "second":
                root_relation = (
                    "lt_r"
                    if period < r
                    else "eq_r"
                    if period == r
                    else "gt_r"
                )
                summary["second_half_three_seam_cross_counts"][
                    f"{root_relation}:seam_{str(seam_holds).lower()}"
                ] += 1

            if period >= P:
                continue
            if half == "first":
                opportunities["first_3_bound"] += 1
                opportunities["first_3_visibility"] += 1
                if period >= q:
                    violations["first_3_bound"] += 1
                if not ends_power(visible, root=period, exponent=3):
                    violations["first_3_visibility"] += 1
                continue

            opportunities["second_3_bound"] += 1
            if period > r:
                violations["second_3_bound"] += 1
            if period < r:
                opportunities["second_3_visibility"] += 1
                if not ends_power(visible, root=period, exponent=3):
                    violations["second_3_visibility"] += 1
                continue
            if period != r:
                continue

            for key in (
                "full_root_seam",
                "full_root_suffix",
                "full_root_terminal",
            ):
                opportunities[key] += 1
            if not seam_holds:
                violations["full_root_seam"] += 1
            suffix_length = r - index
            if B[index:] != (3,) * suffix_length:
                violations["full_root_suffix"] += 1
            if index != r - 1:
                violations["full_root_terminal"] += 1

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
                        (2, 3),
                        repeat=prefix_length - 1,
                    ):
                        Q = (3,) + Q_tail
                        U = Q + B
                        R = B + Q + B
                        X = B[r - t :] + U + B
                        record(
                            branch="p>q",
                            q=q,
                            r=r,
                            p=p,
                            seam="none",
                            B=B,
                            Q=Q,
                            U=U,
                            R=R,
                            X=X,
                        )

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
                        (2, 3),
                        repeat=nu - 1,
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
                            record(
                                branch="p<q",
                                q=q,
                                r=r,
                                p=p,
                                seam=seam,
                                B=B,
                                Q=Q,
                                U=U,
                                R=R,
                                X=X,
                            )

    return summaries


@dataclass(frozen=True)
class LiteralCertificate:
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
    all_proper_periods_below_P: bool
    expected_cut_pairs: tuple[Witness, ...]
    second_half_three_rows: tuple[tuple[int, Witness, bool], ...]
    endpoint: Witness
    full_fourth_power_root_occurrences: int
    full_fourth_power_cut_count: int
    visible_proper_fourth_root_occurrences: int
    visible_proper_fourth_cut_count: int


def _is_positive_integer(value: object) -> bool:
    return type(value) is int and value > 0


def _is_nonnegative_integer(value: object) -> bool:
    return type(value) is int and value >= 0


def _is_binary_word(value: object) -> bool:
    return type(value) is tuple and all(
        type(symbol) is int and symbol in (2, 3)
        for symbol in value
    )


def _is_witness_shape(value: object) -> bool:
    return (
        type(value) is tuple
        and len(value) == 2
        and all(_is_positive_integer(entry) for entry in value)
    )


def _has_valid_literal_certificate_shape(certificate: object) -> bool:
    if type(certificate) is not LiteralCertificate:
        return False
    return (
        type(certificate.name) is str
        and bool(certificate.name)
        and type(certificate.branch) is str
        and certificate.branch in ("p>q", "p<q")
        and type(certificate.seam) is str
        and all(
            _is_positive_integer(value)
            for value in (
                certificate.q,
                certificate.r,
                certificate.p,
                certificate.P,
            )
        )
        and certificate.q > 2 * certificate.r
        and all(
            _is_binary_word(value)
            for value in (
                certificate.B,
                certificate.Theta,
                certificate.D,
                certificate.Q,
                certificate.U,
                certificate.R,
                certificate.X,
            )
        )
        and type(certificate.all_proper_periods_below_P) is bool
        and type(certificate.expected_cut_pairs) is tuple
        and len(certificate.expected_cut_pairs)
        == 2 * certificate.r
        and all(
            _is_witness_shape(witness)
            for witness in certificate.expected_cut_pairs
        )
        and type(certificate.second_half_three_rows) is tuple
        and all(
            type(row) is tuple
            and len(row) == 3
            and _is_nonnegative_integer(row[0])
            and row[0] < certificate.r
            and _is_witness_shape(row[1])
            and type(row[2]) is bool
            for row in certificate.second_half_three_rows
        )
        and _is_witness_shape(certificate.endpoint)
        and all(
            _is_nonnegative_integer(count)
            for count in (
                certificate.full_fourth_power_root_occurrences,
                certificate.full_fourth_power_cut_count,
                certificate.visible_proper_fourth_root_occurrences,
                certificate.visible_proper_fourth_cut_count,
            )
        )
    )


def _literal_certificate(
    *,
    name: str,
    branch: str,
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
    expected_cut_pairs: tuple[Witness, ...],
    second_half_three_rows: tuple[tuple[int, Witness, bool], ...],
    endpoint: Witness,
) -> LiteralCertificate:
    return LiteralCertificate(
        name=name,
        branch=branch,
        q=q,
        r=r,
        p=p,
        P=q + r,
        seam=seam,
        B=word(B),
        Theta=word(Theta),
        D=word(D),
        Q=word(Q),
        U=word(U),
        R=word(R),
        X=word(X),
        all_proper_periods_below_P=True,
        expected_cut_pairs=expected_cut_pairs,
        second_half_three_rows=second_half_three_rows,
        endpoint=endpoint,
        full_fourth_power_root_occurrences=0,
        full_fourth_power_cut_count=0,
        visible_proper_fourth_root_occurrences=0,
        visible_proper_fourth_cut_count=0,
    )


_PGTQ_CUTS = (
    (2, 12),
    (2, 1),
    (3, 1),
    (2, 12),
    (2, 4),
    (2, 1),
    (3, 1),
    (2, 4),
)

_PLTQ_R4_CUTS = (
    (2, 23),
    (2, 23),
    (2, 1),
    (3, 1),
    (2, 4),
    (2, 4),
    (2, 1),
    (3, 1),
)

LITERAL_CERTIFICATES = (
    _literal_certificate(
        name="pgtq_q12_r4_minimal_local_replay",
        branch="p>q",
        q=12,
        r=4,
        p=15,
        seam="none",
        B="2232",
        Theta="",
        D="",
        Q="3233",
        U="32332232",
        R="223232332232",
        X="232323322322232",
        expected_cut_pairs=_PGTQ_CUTS,
        second_half_three_rows=((2, (3, 1), False),),
        endpoint=(3, 4),
    ),
    _literal_certificate(
        name="pltq_q8_r1_minimal_local_replay",
        branch="p<q",
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
        expected_cut_pairs=((2, 8), (2, 1)),
        second_half_three_rows=(),
        endpoint=(3, 1),
    ),
    _literal_certificate(
        name="pltq_q23_r4_first_nontrivial_local_replay",
        branch="p<q",
        q=23,
        r=4,
        p=14,
        seam="D=JBTheta",
        B="2223",
        Theta="3",
        D="222233",
        Q="322232223222233",
        U="3222322232222332223",
        R="22233222322232222332223",
        X="22223322232223",
        expected_cut_pairs=_PLTQ_R4_CUTS,
        second_half_three_rows=((3, (3, 1), True),),
        endpoint=(3, 4),
    ),
    _literal_certificate(
        name="pltq_q24_r4_local_replay",
        branch="p<q",
        q=24,
        r=4,
        p=15,
        seam="D=JBTheta",
        B="2223",
        Theta="3",
        D="2222233",
        Q="3222322232222233",
        U="32223222322222332223",
        R="222332223222322222332223",
        X="222223322232223",
        expected_cut_pairs=(
            (2, 24),
            (2, 24),
            (2, 1),
            (3, 1),
            (2, 4),
            (2, 4),
            (2, 1),
            (3, 1),
        ),
        second_half_three_rows=((3, (3, 1), True),),
        endpoint=(3, 4),
    ),
    _literal_certificate(
        name="pltq_q25_r4_first_local_replay",
        branch="p<q",
        q=25,
        r=4,
        p=16,
        seam="D=JBTheta",
        B="2223",
        Theta="3",
        D="22222233",
        Q="32223222322222233",
        U="322232223222222332223",
        R="2223322232223222222332223",
        X="2222223322232223",
        expected_cut_pairs=(
            (2, 25),
            (2, 25),
            (2, 1),
            (3, 1),
            (2, 4),
            (2, 4),
            (2, 1),
            (3, 1),
        ),
        second_half_three_rows=((3, (3, 1), True),),
        endpoint=(3, 4),
    ),
    _literal_certificate(
        name="pltq_q25_r4_second_local_replay",
        branch="p<q",
        q=25,
        r=4,
        p=16,
        seam="D=JBTheta",
        B="2223",
        Theta="3",
        D="23222233",
        Q="32223222323222233",
        U="322232223232222332223",
        R="2223322232223232222332223",
        X="2322223322232223",
        expected_cut_pairs=(
            (2, 25),
            (2, 25),
            (2, 1),
            (3, 1),
            (2, 4),
            (2, 4),
            (2, 1),
            (3, 1),
        ),
        second_half_three_rows=((3, (3, 1), True),),
        endpoint=(3, 4),
    ),
)


def _normal_form_holds(certificate: LiteralCertificate) -> bool:
    q = certificate.q
    r = certificate.r
    p = certificate.p
    B = certificate.B
    Theta = certificate.Theta
    D = certificate.D
    Q = certificate.Q
    U = certificate.U
    R = certificate.R
    X = certificate.X
    if (
        certificate.P != q + r
        or len(B) != r
        or len(Q) != q - 2 * r
        or len(U) != q - r
        or len(R) != q
        or len(X) != p
        or B[0] != 2
        or Q[0] != 3
        or U != Q + B
        or R != B + Q + B
    ):
        return False
    if certificate.branch == "p>q":
        t = p - q
        return (
            certificate.seam == "none"
            and not Theta
            and not D
            and q > 2 * r > 0
            and 2 * t > r
            and t < r
            and all(
                B[index] == B[index - t]
                for index in range(t, r)
            )
            and X == B[r - t :] + U + B
        )
    if certificate.branch != "p<q":
        return False
    nu = len(Theta)
    sigma = p - 2 * r
    e = 2 * p - certificate.P
    if not (
        nu > 0
        and sigma > nu
        and q == 4 * r + nu + sigma
        and r < p - gcd(p, q)
        and p > r + gcd(p, r)
        and Theta[0] == 3
        and Q == Theta + B * 2 + D
        and X == D + B * 2
    ):
        return False
    if certificate.seam == "D=JBTheta":
        return e >= 0 and D[e:] == B + Theta
    if certificate.seam != "D=B[c:]Theta":
        return False
    c = -e
    return (
        e < 0
        and 0 < 2 * c < r
        and B[:c] == B[-c:]
        and D == B[c:] + Theta
    )


def audit_literal_certificate(certificate: object) -> bool:
    """Recompute every literal certificate field without production code."""

    if not _has_valid_literal_certificate_shape(certificate):
        return False
    if not _normal_form_holds(certificate):
        return False
    mismatch_index = next(
        (
            index
            for index, symbol in enumerate(certificate.U)
            if symbol != certificate.X[index % certificate.p]
        ),
        None,
    )
    if not (
        certificate.U.index(2) == 1
        and mismatch_index == 0
        and terminal_three_run(certificate.B) <= 1
        and literal_witness(certificate.R * 2)
        == (2, certificate.q)
        and literal_witness(certificate.R * 2 + certificate.B)[0] == 2
        and literal_witness(
            certificate.B + certificate.R + certificate.B * 2
        )
        == (3, certificate.r)
        and literal_witness(certificate.X * 3)
        == (3, certificate.p)
        and literal_witness(
            certificate.X * 3
            + certificate.U
            + certificate.B * 2
        )
        == (3, certificate.r)
    ):
        return False

    state = certificate.X * 3 + certificate.U
    cut_pairs: list[Witness] = []
    second_half_three_rows: list[tuple[int, Witness, bool]] = []
    full_occurrences = 0
    full_cuts = 0
    visible_occurrences = 0
    visible_cuts = 0
    for phase, requested in enumerate(certificate.B * 2):
        pair = literal_witness(state)
        cut_pairs.append(pair)
        if pair[0] != requested:
            return False
        index = phase % certificate.r
        first_half = phase < certificate.r
        visible = (
            certificate.R * 2 + certificate.B[:index]
            if first_half
            else certificate.B * 2 + certificate.B[:index]
        )
        if state[-len(visible) :] != visible:
            return False
        full_roots = fourth_power_roots(state)
        visible_roots = visible_proper_fourth_roots(
            visible,
            ambient_period=(
                certificate.q if first_half else certificate.r
            ),
        )
        full_occurrences += len(full_roots)
        full_cuts += bool(full_roots)
        visible_occurrences += len(visible_roots)
        visible_cuts += bool(visible_roots)
        if not first_half and requested == 3:
            seam_holds = (
                certificate.B + certificate.Q
            )[-(certificate.r - index) :] == certificate.B[index:]
            second_half_three_rows.append((index, pair, seam_holds))
        state += (requested,)

    return (
        tuple(cut_pairs) == certificate.expected_cut_pairs
        and all(
            period < certificate.P
            for _, period in cut_pairs
        )
        == certificate.all_proper_periods_below_P
        and tuple(second_half_three_rows)
        == certificate.second_half_three_rows
        and literal_witness(state) == certificate.endpoint
        and full_occurrences
        == certificate.full_fourth_power_root_occurrences
        and full_cuts == certificate.full_fourth_power_cut_count
        and visible_occurrences
        == certificate.visible_proper_fourth_root_occurrences
        and visible_cuts
        == certificate.visible_proper_fourth_cut_count
    )
