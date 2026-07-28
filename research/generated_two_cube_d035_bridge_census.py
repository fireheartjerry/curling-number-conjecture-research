"""Definition-first bounded census for the D-035 two-half bridge.

Every numerical result produced here is finite ``COMPUTED`` evidence. It is
not an unbounded proof of a bridge theorem, Cell C, either G2CS target, or
the Curling Number Conjecture.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from collections.abc import Sequence
from dataclasses import asdict, dataclass
from math import gcd
from pathlib import Path

from research.generated_two_cube_cell_c_z1_atlas import (
    Witness,
    Z1Model,
    _is_static_candidate as _is_trusted_static_candidate,
    _is_z1_structural as _is_trusted_z1_structural,
    definition_first_witness,
    iter_z1_branch_models,
)

StringCounter = tuple[tuple[str, int], ...]

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


@dataclass(frozen=True)
class BridgeCut:
    """One directly recomputed proper bridge cut."""

    phase: int
    half: str
    index: int
    requested: int
    witness: Witness
    visible_context_length: int
    full_fourth_power_roots: tuple[int, ...]
    visible_proper_fourth_roots: tuple[int, ...]


@dataclass(frozen=True)
class BridgeTrace:
    """A local replay stopped at its first nonmatching requested symbol."""

    cuts: tuple[BridgeCut, ...]
    first_failure_phase: int | None
    endpoint: Witness | None


@dataclass(frozen=True)
class BranchBridgeSummary:
    """Deterministic bounded counts for one exact period branch."""

    branch: str
    max_q: int
    structured_assignments: int
    z1_structural_assignments: int
    static_candidates: int
    first_failure_phase_counts: StringCounter
    local_bridge_replays: int
    all_proper_periods_below_P_local_replays: int
    local_endpoint_exact_replays: int
    local_r_counts: StringCounter
    local_B_counts: StringCounter
    local_seam_counts: StringCounter
    proper_cut_count: int
    cut_relation_counts: StringCounter
    period_P_relation_counts: StringCounter
    second_half_three_seam_cross_counts: StringCounter
    full_fourth_power_root_occurrences: int
    full_fourth_power_cut_count: int
    visible_proper_fourth_root_occurrences: int
    visible_proper_fourth_cut_count: int
    theorem_opportunity_counts: StringCounter
    theorem_violation_counts: StringCounter


@dataclass(frozen=True)
class BridgeCensus:
    """Complete two-branch D-035 census at one finite bound."""

    max_q: int
    pgtq: BranchBridgeSummary
    pltq: BranchBridgeSummary


@dataclass(frozen=True)
class BridgeCertificate:
    """A fixed sharp model with independently auditable bridge data."""

    name: str
    branch: str
    q: int
    r: int
    p: int
    P: int
    seam: str
    B: tuple[int, ...]
    Theta: tuple[int, ...]
    D: tuple[int, ...]
    Q: tuple[int, ...]
    U: tuple[int, ...]
    R: tuple[int, ...]
    X: tuple[int, ...]
    all_proper_periods_below_P: bool
    expected_cut_pairs: tuple[Witness, ...]
    second_half_three_rows: tuple[
        tuple[int, Witness, bool], ...
    ]
    endpoint: Witness
    full_fourth_power_root_occurrences: int
    full_fourth_power_cut_count: int
    visible_proper_fourth_root_occurrences: int
    visible_proper_fourth_cut_count: int


def _fourth_power_roots(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        root
        for root in range(1, len(word) // 4 + 1)
        if word[-4 * root :] == word[-4 * root : -3 * root] * 4
    )


def _proper_fourth_roots(
    word: tuple[int, ...],
    *,
    ambient_period: int,
) -> tuple[int, ...]:
    return tuple(
        root
        for root in _fourth_power_roots(word)
        if root < ambient_period
    )


def _visible_context(model: Z1Model, phase: int) -> tuple[int, ...]:
    index = phase % model.r
    if phase < model.r:
        return model.R * 2 + model.B[:index]
    return model.B * 2 + model.B[:index]


def _ends_power(
    word: tuple[int, ...],
    *,
    root: int,
    exponent: int,
) -> bool:
    if root <= 0 or exponent * root > len(word):
        return False
    suffix = word[-exponent * root :]
    return suffix == suffix[:root] * exponent


def _terminal_three_run(word: tuple[int, ...]) -> int:
    run = 0
    for symbol in reversed(word):
        if symbol != 3:
            break
        run += 1
    return run


def _counter_tuple(counter: Counter[str]) -> StringCounter:
    return tuple(sorted(counter.items()))


def _zero_counter(keys: tuple[str, ...]) -> Counter[str]:
    return Counter({key: 0 for key in keys})


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


def _has_valid_certificate_shape(certificate: object) -> bool:
    if type(certificate) is not BridgeCertificate:
        return False
    if not (
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
            _is_binary_word(word)
            for word in (
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
    ):
        return False
    return True


def _validate_trace_model(model: Z1Model) -> None:
    words = (
        model.B,
        model.Theta,
        model.D,
        model.Q,
        model.U,
        model.R,
        model.X,
    )
    if not (
        all(
            _is_positive_integer(value)
            for value in (model.q, model.r, model.p, model.P)
        )
        and model.branch in ("p>q", "p<q")
        and model.q > 2 * model.r
        and model.P == model.q + model.r
        and len(model.B) == model.r
        and len(model.Q) == model.q - 2 * model.r
        and len(model.U) == model.q - model.r
        and len(model.R) == model.q
        and len(model.X) == model.p
        and model.U == model.Q + model.B
        and model.R == model.B + model.Q + model.B
        and all(
            symbol in (2, 3)
            for word in words
            for symbol in word
        )
    ):
        raise ValueError("trace_bridge requires a valid D-035 model")


def _literal_witness(word: tuple[int, ...]) -> Witness:
    """Independent exponent-first oracle used only by certificate audits."""

    feasible: dict[int, list[int]] = {}
    for exponent in range(2, len(word) + 1):
        for period in range(1, len(word) // exponent + 1):
            suffix = word[-exponent * period :]
            if suffix == suffix[:period] * exponent:
                feasible.setdefault(exponent, []).append(period)
    if not feasible:
        return 1, len(word)
    exponent = max(feasible)
    return exponent, min(feasible[exponent])


def trace_bridge(model: Z1Model) -> BridgeTrace:
    """Recompute a standalone ``G_loc`` replay from literal suffix powers."""

    _validate_trace_model(model)

    continuation = model.B * 2
    state = model.X * 3 + model.U
    cuts: list[BridgeCut] = []

    for phase, requested in enumerate(continuation):
        index = phase % model.r
        if phase < model.r:
            half = "first"
            visible = model.R * 2 + model.B[:index]
            ambient_period = model.q
        else:
            half = "second"
            visible = model.B * 2 + model.B[:index]
            ambient_period = model.r

        if state[-len(visible) :] != visible:
            raise ValueError(
                "model violates the literal bridge suffix identity"
            )
        witness = definition_first_witness(state)
        cuts.append(
            BridgeCut(
                phase=phase,
                half=half,
                index=index,
                requested=requested,
                witness=witness,
                visible_context_length=len(visible),
                full_fourth_power_roots=_fourth_power_roots(state),
                visible_proper_fourth_roots=_proper_fourth_roots(
                    visible,
                    ambient_period=ambient_period,
                ),
            )
        )
        if witness[0] != requested:
            return BridgeTrace(
                cuts=tuple(cuts),
                first_failure_phase=phase,
                endpoint=None,
            )
        state += (requested,)

    return BridgeTrace(
        cuts=tuple(cuts),
        first_failure_phase=None,
        endpoint=definition_first_witness(state),
    )


def _relation_key(cut: BridgeCut, model: Z1Model) -> str:
    if cut.half == "first":
        bound = model.q
        scale = "q"
    else:
        bound = model.r
        scale = "r"
    period = cut.witness[1]
    relation = "<" if period < bound else "=" if period == bound else ">"
    return f"{cut.half}:{cut.requested}:{relation}{scale}"


def _scan_branch(*, branch: str, max_q: int) -> BranchBridgeSummary:
    structured_assignments = 0
    z1_structural_assignments = 0
    static_candidates = 0
    failures: Counter[str] = Counter()
    local_bridge_replays = 0
    all_proper_periods_below_P_local_replays = 0
    local_endpoint_exact_replays = 0
    local_r: Counter[str] = Counter()
    local_B: Counter[str] = Counter()
    local_seams: Counter[str] = Counter()
    proper_cut_count = 0
    cut_relations: Counter[str] = Counter()
    period_P_relations = _zero_counter(PERIOD_P_KEYS)
    second_half_three_seams = _zero_counter(SEAM_CROSS_KEYS)
    full_fourth_root_occurrences = 0
    full_fourth_cut_count = 0
    visible_fourth_root_occurrences = 0
    visible_fourth_cut_count = 0
    opportunities = _zero_counter(THEOREM_KEYS)
    violations = _zero_counter(THEOREM_KEYS)

    for model in iter_z1_branch_models(
        branch=branch,
        max_q=max_q,
    ):
        structured_assignments += 1
        if not _is_trusted_z1_structural(model):
            continue
        z1_structural_assignments += 1
        if not _is_trusted_static_candidate(model):
            continue
        static_candidates += 1

        trace = trace_bridge(model)
        if trace.first_failure_phase is not None:
            failures[str(trace.first_failure_phase)] += 1
            continue

        local_bridge_replays += 1
        local_r[str(model.r)] += 1
        local_B["".join(map(str, model.B))] += 1
        local_seams[model.seam] += 1

        endpoint_exact = trace.endpoint == (3, model.r)
        local_endpoint_exact_replays += endpoint_exact
        opportunities["endpoint_pair"] += 1
        if not endpoint_exact:
            violations["endpoint_pair"] += 1

        if all(cut.witness[1] < model.P for cut in trace.cuts):
            all_proper_periods_below_P_local_replays += 1

        for cut in trace.cuts:
            proper_cut_count += 1
            cut_relations[_relation_key(cut, model)] += 1
            period = cut.witness[1]
            P_relation = (
                "<"
                if period < model.P
                else "="
                if period == model.P
                else ">"
            )
            period_P_relations[
                f"{cut.half}:{cut.requested}:{P_relation}P"
            ] += 1

            full_fourth_root_occurrences += len(
                cut.full_fourth_power_roots
            )
            full_fourth_cut_count += bool(
                cut.full_fourth_power_roots
            )
            visible_fourth_root_occurrences += len(
                cut.visible_proper_fourth_roots
            )
            visible_fourth_cut_count += bool(
                cut.visible_proper_fourth_roots
            )
            opportunities["full_fourth_power"] += 1
            opportunities["visible_fourth_power"] += 1
            if cut.full_fourth_power_roots:
                violations["full_fourth_power"] += 1
            if cut.visible_proper_fourth_roots:
                violations["visible_fourth_power"] += 1

            visible = _visible_context(model, cut.phase)
            if cut.requested == 2:
                key = f"{cut.half}_2_cap"
                bound = (
                    model.q
                    if cut.half == "first"
                    else model.r
                )
                opportunities[key] += 1
                if period > bound:
                    violations[key] += 1
                continue

            seam_holds: bool | None = None
            if cut.half == "second":
                suffix_length = model.r - cut.index
                seam_holds = (
                    (model.B + model.Q)[-suffix_length:]
                    == model.B[cut.index:]
                )
                root_relation = (
                    "lt_r"
                    if period < model.r
                    else "eq_r"
                    if period == model.r
                    else "gt_r"
                )
                second_half_three_seams[
                    f"{root_relation}:"
                    f"seam_{str(seam_holds).lower()}"
                ] += 1

            if period >= model.P:
                continue
            if cut.half == "first":
                opportunities["first_3_bound"] += 1
                opportunities["first_3_visibility"] += 1
                if period >= model.q:
                    violations["first_3_bound"] += 1
                if not _ends_power(
                    visible,
                    root=period,
                    exponent=3,
                ):
                    violations["first_3_visibility"] += 1
                continue

            opportunities["second_3_bound"] += 1
            if period > model.r:
                violations["second_3_bound"] += 1
            if period < model.r:
                opportunities["second_3_visibility"] += 1
                if not _ends_power(
                    visible,
                    root=period,
                    exponent=3,
                ):
                    violations["second_3_visibility"] += 1
                continue
            if period != model.r:
                continue

            for key in (
                "full_root_seam",
                "full_root_suffix",
                "full_root_terminal",
            ):
                opportunities[key] += 1
            if not seam_holds:
                violations["full_root_seam"] += 1
            suffix_length = model.r - cut.index
            if model.B[cut.index:] != (3,) * suffix_length:
                violations["full_root_suffix"] += 1
            if cut.index != model.r - 1:
                violations["full_root_terminal"] += 1

    return BranchBridgeSummary(
        branch=branch,
        max_q=max_q,
        structured_assignments=structured_assignments,
        z1_structural_assignments=z1_structural_assignments,
        static_candidates=static_candidates,
        first_failure_phase_counts=_counter_tuple(failures),
        local_bridge_replays=local_bridge_replays,
        all_proper_periods_below_P_local_replays=(
            all_proper_periods_below_P_local_replays
        ),
        local_endpoint_exact_replays=local_endpoint_exact_replays,
        local_r_counts=_counter_tuple(local_r),
        local_B_counts=_counter_tuple(local_B),
        local_seam_counts=_counter_tuple(local_seams),
        proper_cut_count=proper_cut_count,
        cut_relation_counts=_counter_tuple(cut_relations),
        period_P_relation_counts=_counter_tuple(period_P_relations),
        second_half_three_seam_cross_counts=_counter_tuple(
            second_half_three_seams
        ),
        full_fourth_power_root_occurrences=(
            full_fourth_root_occurrences
        ),
        full_fourth_power_cut_count=full_fourth_cut_count,
        visible_proper_fourth_root_occurrences=(
            visible_fourth_root_occurrences
        ),
        visible_proper_fourth_cut_count=visible_fourth_cut_count,
        theorem_opportunity_counts=_counter_tuple(opportunities),
        theorem_violation_counts=_counter_tuple(violations),
    )


def scan_bridge_census(*, max_q: int) -> BridgeCensus:
    """Scan both exact D-035 bridge branches through ``q=max_q``."""

    if not _is_positive_integer(max_q):
        raise ValueError("max_q must be a positive integer")
    return BridgeCensus(
        max_q=max_q,
        pgtq=_scan_branch(branch="p>q", max_q=max_q),
        pltq=_scan_branch(branch="p<q", max_q=max_q),
    )


def _word(text: str) -> tuple[int, ...]:
    return tuple(map(int, text))


def _certificate(
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
    all_proper_periods_below_P: bool,
    expected_cut_pairs: tuple[Witness, ...],
    second_half_three_rows: tuple[
        tuple[int, Witness, bool], ...
    ],
    endpoint: Witness,
    full_fourth_power_root_occurrences: int,
    full_fourth_power_cut_count: int,
    visible_proper_fourth_root_occurrences: int,
    visible_proper_fourth_cut_count: int,
) -> BridgeCertificate:
    return BridgeCertificate(
        name=name,
        branch=branch,
        q=q,
        r=r,
        p=p,
        P=q + r,
        seam=seam,
        B=_word(B),
        Theta=_word(Theta),
        D=_word(D),
        Q=_word(Q),
        U=_word(U),
        R=_word(R),
        X=_word(X),
        all_proper_periods_below_P=all_proper_periods_below_P,
        expected_cut_pairs=expected_cut_pairs,
        second_half_three_rows=second_half_three_rows,
        endpoint=endpoint,
        full_fourth_power_root_occurrences=(
            full_fourth_power_root_occurrences
        ),
        full_fourth_power_cut_count=full_fourth_power_cut_count,
        visible_proper_fourth_root_occurrences=(
            visible_proper_fourth_root_occurrences
        ),
        visible_proper_fourth_cut_count=(
            visible_proper_fourth_cut_count
        ),
    )


def known_bridge_certificates() -> tuple[BridgeCertificate, ...]:
    """Return the six fixed sharp bridge models through ``q<=25``."""

    pgtq_trace = (
        (2, 12),
        (2, 1),
        (3, 1),
        (2, 12),
        (2, 4),
        (2, 1),
        (3, 1),
        (2, 4),
    )
    return (
        _certificate(
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
            all_proper_periods_below_P=True,
            expected_cut_pairs=pgtq_trace,
            second_half_three_rows=((2, (3, 1), False),),
            endpoint=(3, 4),
            full_fourth_power_root_occurrences=0,
            full_fourth_power_cut_count=0,
            visible_proper_fourth_root_occurrences=0,
            visible_proper_fourth_cut_count=0,
        ),
        _certificate(
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
            all_proper_periods_below_P=True,
            expected_cut_pairs=((2, 8), (2, 1)),
            second_half_three_rows=(),
            endpoint=(3, 1),
            full_fourth_power_root_occurrences=0,
            full_fourth_power_cut_count=0,
            visible_proper_fourth_root_occurrences=0,
            visible_proper_fourth_cut_count=0,
        ),
        _certificate(
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
            all_proper_periods_below_P=True,
            expected_cut_pairs=(
                (2, 23),
                (2, 23),
                (2, 1),
                (3, 1),
                (2, 4),
                (2, 4),
                (2, 1),
                (3, 1),
            ),
            second_half_three_rows=((3, (3, 1), True),),
            endpoint=(3, 4),
            full_fourth_power_root_occurrences=0,
            full_fourth_power_cut_count=0,
            visible_proper_fourth_root_occurrences=0,
            visible_proper_fourth_cut_count=0,
        ),
        _certificate(
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
            all_proper_periods_below_P=True,
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
            full_fourth_power_root_occurrences=0,
            full_fourth_power_cut_count=0,
            visible_proper_fourth_root_occurrences=0,
            visible_proper_fourth_cut_count=0,
        ),
        _certificate(
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
            all_proper_periods_below_P=True,
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
            full_fourth_power_root_occurrences=0,
            full_fourth_power_cut_count=0,
            visible_proper_fourth_root_occurrences=0,
            visible_proper_fourth_cut_count=0,
        ),
        _certificate(
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
            all_proper_periods_below_P=True,
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
            full_fourth_power_root_occurrences=0,
            full_fourth_power_cut_count=0,
            visible_proper_fourth_root_occurrences=0,
            visible_proper_fourth_cut_count=0,
        ),
    )


def _branch_normal_form_holds(certificate: BridgeCertificate) -> bool:
    q = certificate.q
    r = certificate.r
    p = certificate.p
    P = certificate.P
    B = certificate.B
    Theta = certificate.Theta
    D = certificate.D
    Q = certificate.Q
    U = certificate.U
    R = certificate.R
    X = certificate.X

    if (
        P != q + r
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
            and all(B[index] == B[index - t]
                    for index in range(t, r))
            and X == B[r - t :] + U + B
        )

    if certificate.branch != "p<q":
        return False
    nu = len(Theta)
    sigma = p - 2 * r
    e = 2 * p - P
    if (
        not nu > 0
        or not sigma > nu
        or q != 4 * r + nu + sigma
        or not r < p - gcd(p, q)
        or not p > r + gcd(p, r)
        or Theta[0] != 3
        or Q != Theta + B * 2 + D
        or X != D + B * 2
    ):
        return False
    if certificate.seam == "D=JBTheta":
        return e >= 0 and D[e:] == B + Theta
    if certificate.seam == "D=B[c:]Theta":
        c = -e
        return (
            e < 0
            and 0 < 2 * c < r
            and B[:c] == B[-c:]
            and D == B[c:] + Theta
        )
    return False


def audit_bridge_certificate(certificate: object) -> bool:
    """Recompute every literal certificate field with exact suffix loops."""

    if not _has_valid_certificate_shape(certificate):
        return False
    if not _branch_normal_form_holds(certificate):
        return False

    witness = _literal_witness
    if not (
        certificate.U.index(2) == 1
        and next(
            (
                index
                for index, symbol in enumerate(certificate.U)
                if symbol != certificate.X[index % certificate.p]
            ),
            None,
        )
        == 0
        and _terminal_three_run(certificate.B) <= 1
        and witness(certificate.R * 2) == (2, certificate.q)
        and witness(certificate.R * 2 + certificate.B)[0] == 2
        and witness(
            certificate.B + certificate.R + certificate.B * 2
        )
        == (3, certificate.r)
        and witness(certificate.X * 3) == (3, certificate.p)
        and witness(
            certificate.X * 3
            + certificate.U
            + certificate.B * 2
        )
        == (3, certificate.r)
    ):
        return False

    state = certificate.X * 3 + certificate.U
    independent_pairs: list[Witness] = []
    second_half_three_rows: list[
        tuple[int, Witness, bool]
    ] = []
    full_fourth_root_occurrences = 0
    full_fourth_cut_count = 0
    visible_fourth_root_occurrences = 0
    visible_fourth_cut_count = 0
    for phase, expected in enumerate(certificate.B * 2):
        pair = witness(state)
        independent_pairs.append(pair)
        if pair[0] != expected:
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
        full_roots = _fourth_power_roots(state)
        visible_roots = _proper_fourth_roots(
            visible,
            ambient_period=(
                certificate.q if first_half else certificate.r
            ),
        )
        full_fourth_root_occurrences += len(full_roots)
        full_fourth_cut_count += bool(full_roots)
        visible_fourth_root_occurrences += len(visible_roots)
        visible_fourth_cut_count += bool(visible_roots)
        if not first_half and expected == 3:
            suffix_length = certificate.r - index
            seam_holds = (
                (certificate.B + certificate.Q)[-suffix_length:]
                == certificate.B[index:]
            )
            second_half_three_rows.append(
                (index, pair, seam_holds)
            )
        state += (expected,)
    if (
        tuple(independent_pairs) != certificate.expected_cut_pairs
        or (
            all(
                period < certificate.P
                for _, period in independent_pairs
            )
            != certificate.all_proper_periods_below_P
        )
        or tuple(second_half_three_rows)
        != certificate.second_half_three_rows
        or witness(state) != certificate.endpoint
        or full_fourth_root_occurrences
        != certificate.full_fourth_power_root_occurrences
        or full_fourth_cut_count
        != certificate.full_fourth_power_cut_count
        or visible_fourth_root_occurrences
        != certificate.visible_proper_fourth_root_occurrences
        or visible_fourth_cut_count
        != certificate.visible_proper_fourth_cut_count
    ):
        return False

    model = Z1Model(
        branch=certificate.branch,
        q=certificate.q,
        r=certificate.r,
        p=certificate.p,
        P=certificate.P,
        seam=certificate.seam,
        B=certificate.B,
        Theta=certificate.Theta,
        D=certificate.D,
        Q=certificate.Q,
        U=certificate.U,
        R=certificate.R,
        X=certificate.X,
    )
    trace = trace_bridge(model)
    return (
        trace.first_failure_phase is None
        and tuple(cut.witness for cut in trace.cuts)
        == certificate.expected_cut_pairs
        and sum(
            len(cut.full_fourth_power_roots)
            for cut in trace.cuts
        )
        == certificate.full_fourth_power_root_occurrences
        and sum(
            bool(cut.full_fourth_power_roots)
            for cut in trace.cuts
        )
        == certificate.full_fourth_power_cut_count
        and sum(
            len(cut.visible_proper_fourth_roots)
            for cut in trace.cuts
        )
        == certificate.visible_proper_fourth_root_occurrences
        and sum(
            bool(cut.visible_proper_fourth_roots)
            for cut in trace.cuts
        )
        == certificate.visible_proper_fourth_cut_count
        and trace.endpoint == certificate.endpoint
    )


def _json(value) -> str:
    return json.dumps(
        value,
        separators=(",", ":"),
        sort_keys=True,
    )


def _render_branch(summary: BranchBridgeSummary) -> list[str]:
    if (
        type(summary) is not BranchBridgeSummary
        or summary.branch not in ("p>q", "p<q")
    ):
        raise ValueError("invalid branch summary")
    prefix = "pgtq" if summary.branch == "p>q" else "pltq"
    scalar_fields = (
        "structured_assignments",
        "z1_structural_assignments",
        "static_candidates",
        "local_bridge_replays",
        "all_proper_periods_below_P_local_replays",
        "local_endpoint_exact_replays",
        "proper_cut_count",
        "full_fourth_power_root_occurrences",
        "full_fourth_power_cut_count",
        "visible_proper_fourth_root_occurrences",
        "visible_proper_fourth_cut_count",
    )
    counter_fields = (
        "first_failure_phase_counts",
        "local_r_counts",
        "local_B_counts",
        "local_seam_counts",
        "cut_relation_counts",
        "period_P_relation_counts",
        "second_half_three_seam_cross_counts",
        "theorem_opportunity_counts",
        "theorem_violation_counts",
    )
    lines = [
        f"{prefix}.branch={summary.branch}",
        *(
            f"{prefix}.{field}={getattr(summary, field)}"
            for field in scalar_fields
        ),
    ]
    lines.extend(
        f"{prefix}.{field}={_json(dict(getattr(summary, field)))}"
        for field in counter_fields
    )
    return lines


def _has_coherent_census_metadata(census: object) -> bool:
    if type(census) is not BridgeCensus:
        return False
    if not _is_positive_integer(census.max_q):
        return False
    return (
        type(census.pgtq) is BranchBridgeSummary
        and type(census.pltq) is BranchBridgeSummary
        and census.pgtq.branch == "p>q"
        and census.pltq.branch == "p<q"
        and type(census.pgtq.max_q) is int
        and type(census.pltq.max_q) is int
        and census.pgtq.max_q == census.max_q
        and census.pltq.max_q == census.max_q
    )


def render_census(
    census: BridgeCensus,
    certificates: Sequence[BridgeCertificate],
) -> str:
    """Render a byte-stable artifact with explicit finite-evidence scope."""

    if not _has_coherent_census_metadata(census):
        raise ValueError("invalid bridge census metadata")
    if len(certificates) != 6:
        raise ValueError("expected exactly six bridge certificates")
    if any(
        not audit_bridge_certificate(certificate)
        for certificate in certificates
    ):
        raise ValueError("invalid bridge certificate")

    lines = [
        "label=bounded_binary_D035_two_half_local_bridge_census",
        f"max_q={census.max_q}",
        "alphabet=2,3",
        "status=COMPUTED",
        "row=z1_h0",
        "mismatch_index=0",
        "scope=standalone_local_two_half_bridge_only",
        "orbit_scope=standalone_G_loc_seed",
        "target_assumption=none",
        "full_context_not_enumerated=true",
        "I_bridge_membership=K0_and_K2r_only",
        "J_bridge_membership=all_K0_through_K2r",
        "two_cut_cap=target_independent",
        "interior_three_cut_I_cap=not_automatic",
        "proper_bridge_J_cap=under_J_negation",
        "structural_source=D034_exact_two_branch_generators",
        "witness_method=definition_first_suffix_power",
        (
            "local_replay_condition="
            "direct_kappa_match_at_all_2r_proper_cuts"
        ),
        (
            "counter_universe.structured_assignments="
            "all_exact_normal_form_assignments"
        ),
        (
            "counter_universe.z1_structural_assignments="
            "structured_assignments_with_z1_mismatch0_lambda_at_most1"
        ),
        (
            "counter_universe.static_candidates="
            "z1_structural_assignments_passing_exact_static_filters"
        ),
        (
            "counter_universe.first_failure_phase_counts="
            "failed_local_prefixes_of_static_candidates"
        ),
        (
            "counter_universe.local_bridge_replays="
            "static_candidates_matching_all_2r_requested_labels"
        ),
        (
            "counter_universe.local_replay_model_counters="
            "complete_local_bridge_replays"
        ),
        (
            "counter_universe.proper_cut_counters="
            "proper_cuts_of_complete_local_bridge_replays"
        ),
        (
            "counter_universe.theorem_opportunity_counts="
            "eligible_conclusions_after_complete_local_replay"
        ),
        (
            "counter_universe.theorem_violation_counts="
            "matching_theorem_opportunities_only"
        ),
        (
            "counter_definition.first_failure_phase_counts="
            "one_first_mismatch_phase_per_failed_static_candidate"
        ),
        (
            "counter_definition.proper_cut_count="
            "sum_2r_over_complete_local_bridge_replays"
        ),
        (
            "counter_definition.full_fourth_power_root_occurrences="
            "sum_full_state_fourth_suffix_roots_over_proper_cuts"
        ),
        (
            "counter_definition.full_fourth_power_cut_count="
            "proper_cuts_with_a_full_state_fourth_suffix_root"
        ),
        (
            "counter_definition.visible_proper_fourth_root_occurrences="
            "sum_visible_proper_fourth_suffix_roots_over_proper_cuts"
        ),
        (
            "counter_definition.visible_proper_fourth_cut_count="
            "proper_cuts_with_a_visible_proper_fourth_suffix_root"
        ),
        (
            "counter_definition.period_P_relation_counts="
            "proper_cuts_by_half_label_and_canonical_period_vs_P"
        ),
        (
            "counter_definition.second_half_three_seam_cross_counts="
            "second_half_3_cuts_by_period_vs_r_and_independent_seam"
        ),
        (
            "counter_definition.theorem_opportunity_counts="
            "theorem_specific_eligible_instances"
        ),
        (
            "counter_definition.theorem_violation_counts="
            "failed_conclusions_within_matching_opportunities"
        ),
        "Cell_C=OPEN",
        *_render_branch(census.pgtq),
        *_render_branch(census.pltq),
        f"certificate_count={len(certificates)}",
    ]
    lines.extend(
        "certificate=" + _json(asdict(certificate))
        for certificate in certificates
    )
    lines.append(
        "NOT_A_PROOF: bounded standalone-local D-035 bridge census; "
        "no arbitrary left context was enumerated, and zero violations "
        "prove neither bridge theorem, boundary wall, nor Cell C."
    )
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build the bounded D-035 two-half bridge census."
    )
    parser.add_argument("--max-q", type=int, default=25)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args(argv)

    started = time.perf_counter()
    census = scan_bridge_census(max_q=arguments.max_q)
    rendered = render_census(census, known_bridge_certificates())
    if arguments.output is None:
        print(rendered, end="")
    else:
        arguments.output.write_bytes(rendered.encode("utf-8"))
    elapsed = time.perf_counter() - started
    print(f"scan_seconds={elapsed:.3f}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
