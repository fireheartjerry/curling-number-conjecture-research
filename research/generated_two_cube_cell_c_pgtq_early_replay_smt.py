"""Exact bounded QF_BV audit for the Cell C ``p > q`` early replay wall."""

from __future__ import annotations

import argparse
import json
from collections.abc import Iterator, Sequence
from dataclasses import asdict, dataclass
from itertools import product

from z3 import (
    And,
    BitVec,
    BitVecRef,
    BitVecVal,
    Concat,
    Extract,
    If,
    Not,
    Or,
    SolverFor,
    sat,
    unknown,
)

Word = tuple[int, ...]
Witness = tuple[int, int]


@dataclass(frozen=True)
class PgtqParameters:
    """One admissible simultaneous-boundary parameter triple."""

    q: int
    r: int
    t: int

    def __post_init__(self) -> None:
        if not (self.q > 2 * self.r > 0 and self.r / 2 < self.t < self.r):
            raise ValueError(
                "parameters must satisfy q>2r>0 and r/2<t<r"
            )

    @property
    def p(self) -> int:
        return self.q + self.t

    @property
    def P(self) -> int:
        return self.q + self.r

    @property
    def q_prefix_length(self) -> int:
        return self.q - 2 * self.r

    @property
    def continuation_length(self) -> int:
        return self.q - self.r


def iter_parameter_triples(*, max_q: int) -> Iterator[PgtqParameters]:
    """Yield every integer triple in the exact ``p>q`` boundary domain."""
    if max_q <= 0:
        raise ValueError("max_q must be positive")

    for q in range(1, max_q + 1):
        for r in range(1, (q - 1) // 2 + 1):
            for t in range(r // 2 + 1, r):
                if 2 * t > r:
                    yield PgtqParameters(q=q, r=r, t=t)


@dataclass(frozen=True)
class PgtqWords:
    """One concrete structural assignment."""

    B: Word
    Q: Word
    U: Word
    R: Word
    X: Word


@dataclass(frozen=True)
class SolverResult:
    """One fixed-parameter QF_BV result."""

    parameters: PgtqParameters
    require_canonical_r2: bool
    status: str
    witness: PgtqWords | None
    reason_unknown: str | None


@dataclass(frozen=True)
class OracleMismatch:
    """A disagreement between solver existence and direct enumeration."""

    parameters: PgtqParameters
    solver_status: str
    direct_exists: bool


@dataclass(frozen=True)
class DirectOracleSummary:
    """Independent definition-first comparison over a small exact domain."""

    max_q: int
    parameter_triples: int
    structured_assignments: int
    direct_sat: int
    solver_sat: int
    solver_unsat: int
    solver_unknown: int
    mismatches: tuple[OracleMismatch, ...]


@dataclass(frozen=True)
class PerQSummary:
    """Status counts for one root length q."""

    q: int
    parameter_triples: int
    sat: int
    unsat: int
    unknown: int


@dataclass(frozen=True)
class ReplayScanSummary:
    """Exact QF_BV results over every triple through one q bound."""

    max_q: int
    timeout_ms: int
    parameter_triples: int
    sat: int
    unsat: int
    unknown: int
    per_q: tuple[PerQSummary, ...]


@dataclass(frozen=True)
class CollapseCertificate:
    """A positive early replay whose endpoint collapses below ``q``."""

    q: int
    r: int
    t: int
    B: Word
    Q: Word
    U: Word
    R: Word
    X: Word
    x3_witness: Witness
    r2_witness: Witness
    timeline: tuple[Witness, ...]


@dataclass(frozen=True)
class EndpointJumpCertificate:
    """The structural model showing that the final root push is feasible."""

    q: int
    r: int
    t: int
    B: Word
    Q: Word
    U: Word
    R: Word
    X: Word
    Y: Word
    x3_witness: Witness
    g_pre_witness: Witness
    g_witness: Witness
    h_pre_witness: Witness
    h_witness: Witness
    appended_symbol: int
    first_early_mismatch: tuple[int, int, Witness]


def definition_first_witness(sequence: Sequence[int]) -> Witness:
    """Compute ``(curling number, least maximizing root)`` literally."""
    word = tuple(sequence)
    if not word:
        raise ValueError("definition_first_witness requires a nonempty word")

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


def _build_words(
    parameters: PgtqParameters,
    period_seed: Word,
    q_tail: Word,
) -> PgtqWords:
    q, r, t = parameters.q, parameters.r, parameters.t
    if len(period_seed) != t:
        raise ValueError("period seed has the wrong length")
    if len(q_tail) != parameters.q_prefix_length - 1:
        raise ValueError("Q tail has the wrong length")

    B = tuple(period_seed[index % t] for index in range(r))
    Q = (3,) + q_tail
    U = Q + B
    R = B + U
    X = B[r - t :] + U + B
    return PgtqWords(B=B, Q=Q, U=U, R=R, X=X)


def _iter_direct_words(parameters: PgtqParameters) -> Iterator[PgtqWords]:
    """Enumerate concrete assignments without using any solver helper."""
    for seed_tail in product((2, 3), repeat=parameters.t - 1):
        period_seed = (2,) + seed_tail
        for q_tail in product(
            (2, 3),
            repeat=parameters.q_prefix_length - 1,
        ):
            yield _build_words(parameters, period_seed, q_tail)


def _emits_entire_continuation(words: PgtqWords) -> bool:
    state = words.X * 3
    for requested in words.U:
        if definition_first_witness(state)[0] != requested:
            return False
        state += (requested,)
    return True


def _direct_assignment_satisfies(
    parameters: PgtqParameters,
    words: PgtqWords,
    *,
    require_canonical_r2: bool,
) -> bool:
    if definition_first_witness(words.X * 3) != (3, parameters.p):
        return False
    if not _emits_entire_continuation(words):
        return False
    return (
        not require_canonical_r2
        or definition_first_witness(words.R * 2) == (2, parameters.q)
    )


def _canonical_timeline(start: Word, continuation: Word) -> tuple[Witness, ...]:
    state = start
    timeline: list[Witness] = []
    for symbol in continuation:
        timeline.append(definition_first_witness(state))
        state += (symbol,)
    timeline.append(definition_first_witness(state))
    return tuple(timeline)


def _collapse_certificate(
    q: int,
    r: int,
    t: int,
    B_text: str,
    Q_text: str,
) -> CollapseCertificate:
    parameters = PgtqParameters(q=q, r=r, t=t)
    B = tuple(map(int, B_text))
    Q = tuple(map(int, Q_text))
    U = Q + B
    R = B + U
    X = B[r - t :] + U + B
    return CollapseCertificate(
        q=q,
        r=r,
        t=t,
        B=B,
        Q=Q,
        U=U,
        R=R,
        X=X,
        x3_witness=definition_first_witness(X * 3),
        r2_witness=definition_first_witness(R * 2),
        timeline=_canonical_timeline(X * 3, U),
    )


def known_collapse_certificates() -> tuple[CollapseCertificate, ...]:
    """Return four historical collapses and one witness beyond q=25."""
    return (
        _collapse_certificate(10, 4, 3, "2232", "32"),
        _collapse_certificate(17, 4, 3, "2232", "322232223"),
        _collapse_certificate(17, 7, 4, "2322232", "322"),
        _collapse_certificate(19, 9, 8, "222322232", "3"),
        _collapse_certificate(27, 10, 7, "2322322232", "3222322"),
    )


def audit_collapse_certificate(certificate: CollapseCertificate) -> bool:
    """Recompute every structural and canonical claim in a collapse."""
    try:
        parameters = PgtqParameters(
            q=certificate.q,
            r=certificate.r,
            t=certificate.t,
        )
    except ValueError:
        return False

    if len(certificate.B) != certificate.r:
        return False
    if len(certificate.Q) != parameters.q_prefix_length:
        return False
    if certificate.B[0] != 2 or certificate.Q[0] != 3:
        return False
    if any(
        certificate.B[index] != certificate.B[index - certificate.t]
        for index in range(certificate.t, certificate.r)
    ):
        return False

    U = certificate.Q + certificate.B
    R = certificate.B + U
    X = certificate.B[certificate.r - certificate.t :] + U + certificate.B
    if (certificate.U, certificate.R, certificate.X) != (U, R, X):
        return False

    timeline = _canonical_timeline(X * 3, U)
    return (
        certificate.x3_witness == (3, parameters.p)
        and certificate.x3_witness == definition_first_witness(X * 3)
        and certificate.r2_witness == definition_first_witness(R * 2)
        and certificate.r2_witness != (2, certificate.q)
        and certificate.timeline == timeline
        and tuple(pair[0] for pair in timeline[:-1]) == U
    )


def endpoint_jump_certificate() -> EndpointJumpCertificate:
    """Return the minimal structural simultaneous endpoint-push model."""
    q, r, t = 9, 4, 3
    B = tuple(map(int, "2332"))
    Q = tuple(map(int, "3"))
    U = Q + B
    R = B + U
    X = B[r - t :] + U + B
    Y = B + B + U
    appended = R[-1]
    early_phase_one = definition_first_witness(X * 3 + U[:1])
    return EndpointJumpCertificate(
        q=q,
        r=r,
        t=t,
        B=B,
        Q=Q,
        U=U,
        R=R,
        X=X,
        Y=Y,
        x3_witness=definition_first_witness(X * 3),
        g_pre_witness=definition_first_witness((R * 2)[:-1]),
        g_witness=definition_first_witness(R * 2),
        h_pre_witness=definition_first_witness((Y * 2)[:-1]),
        h_witness=definition_first_witness(Y * 2),
        appended_symbol=appended,
        first_early_mismatch=(1, U[1], early_phase_one),
    )


def audit_endpoint_jump_certificate(
    certificate: EndpointJumpCertificate,
) -> bool:
    """Recompute the endpoint jumps and the earlier replay failure."""
    try:
        parameters = PgtqParameters(
            q=certificate.q,
            r=certificate.r,
            t=certificate.t,
        )
    except ValueError:
        return False

    U = certificate.Q + certificate.B
    R = certificate.B + U
    X = certificate.B[certificate.r - certificate.t :] + U + certificate.B
    Y = certificate.B + certificate.B + U
    if (certificate.U, certificate.R, certificate.X, certificate.Y) != (
        U,
        R,
        X,
        Y,
    ):
        return False
    if certificate.appended_symbol != R[-1] or R[-1] != Y[-1]:
        return False

    return (
        certificate.x3_witness
        == definition_first_witness(X * 3)
        == (3, parameters.p)
        and certificate.g_pre_witness
        == definition_first_witness((R * 2)[:-1])
        == (2, 1)
        and certificate.g_witness
        == definition_first_witness(R * 2)
        == (2, parameters.q)
        and certificate.h_pre_witness
        == definition_first_witness((Y * 2)[:-1])
        == (2, 1)
        and certificate.h_witness
        == definition_first_witness(Y * 2)
        == (2, parameters.P)
        and certificate.first_early_mismatch
        == (1, U[1], definition_first_witness(X * 3 + U[:1]))
        and certificate.first_early_mismatch[2][0] != U[1]
    )


def _concat_symbols(symbols: Sequence[BitVecRef]) -> BitVecRef:
    if not symbols:
        raise ValueError("cannot concatenate an empty symbol sequence")
    if len(symbols) == 1:
        return symbols[0]
    return Concat(*symbols)


def _bit_at(word: BitVecRef, length: int, index: int) -> BitVecRef:
    return Extract(length - 1 - index, length - 1 - index, word)


def _power_constraint(
    word: BitVecRef,
    *,
    exponent: int,
    period: int,
) -> object:
    base = Extract(period - 1, 0, word)
    return And(
        *(
            Extract(
                (block + 1) * period - 1,
                block * period,
                word,
            )
            == base
            for block in range(1, exponent)
        )
    )


def _some_power(
    word: BitVecRef,
    *,
    length: int,
    exponent: int,
) -> object:
    return Or(
        *(
            _power_constraint(
                word,
                exponent=exponent,
                period=period,
            )
            for period in range(1, length // exponent + 1)
        )
    )


def _no_power(
    word: BitVecRef,
    *,
    length: int,
    exponent: int,
    maximum_period: int,
) -> object:
    upper = min(maximum_period, length // exponent)
    return And(
        *(
            Not(
                _power_constraint(
                    word,
                    exponent=exponent,
                    period=period,
                )
            )
            for period in range(1, upper + 1)
        )
    )


def _decode_bitvector(
    value: int,
    *,
    width: int,
) -> tuple[int, ...]:
    return tuple(
        (value >> (width - 1 - index)) & 1 for index in range(width)
    )


def solve_parameter(
    parameters: PgtqParameters,
    *,
    require_canonical_r2: bool,
    timeout_ms: int,
) -> SolverResult:
    """Solve one fixed triple using only quantifier-free bit vectors."""
    if timeout_ms <= 0:
        raise ValueError("timeout_ms must be positive")

    q, r, t = parameters.q, parameters.r, parameters.t
    p = parameters.p
    q_prefix_length = parameters.q_prefix_length
    continuation_length = parameters.continuation_length

    b_seed = BitVec("b_seed", t)
    seed = tuple(_bit_at(b_seed, t, index) for index in range(t))
    B = tuple(seed[index % t] for index in range(r))

    if q_prefix_length == 1:
        q_tail_word = None
        q_tail: tuple[BitVecRef, ...] = ()
    else:
        q_tail_word = BitVec("q_tail", q_prefix_length - 1)
        q_tail = tuple(
            _bit_at(q_tail_word, q_prefix_length - 1, index)
            for index in range(q_prefix_length - 1)
        )

    Q = (BitVecVal(1, 1),) + q_tail
    U = Q + B
    R = B + U
    X = B[r - t :] + U + B
    x3 = _concat_symbols(X * 3)
    r2 = _concat_symbols(R * 2)

    solver = SolverFor("QF_BV")
    solver.set(timeout=timeout_ms)
    solver.add(seed[0] == BitVecVal(0, 1))
    solver.add(
        _no_power(
            x3,
            length=3 * p,
            exponent=3,
            maximum_period=p - 1,
        )
    )
    solver.add(
        _no_power(
            x3,
            length=3 * p,
            exponent=4,
            maximum_period=(3 * p) // 4,
        )
    )
    if require_canonical_r2:
        solver.add(
            _no_power(
                r2,
                length=2 * q,
                exponent=2,
                maximum_period=q - 1,
            )
        )

    state = x3
    for phase in range(1, continuation_length):
        state = Concat(state, U[phase - 1])
        length = 3 * p + phase
        has_square = _some_power(state, length=length, exponent=2)
        has_cube = _some_power(state, length=length, exponent=3)
        has_fourth = _some_power(state, length=length, exponent=4)
        solver.add(
            If(
                U[phase] == BitVecVal(0, 1),
                And(has_square, Not(has_cube)),
                And(has_cube, Not(has_fourth)),
            )
        )

    result = solver.check()
    if result == unknown:
        return SolverResult(
            parameters=parameters,
            require_canonical_r2=require_canonical_r2,
            status="unknown",
            witness=None,
            reason_unknown=solver.reason_unknown(),
        )
    if result != sat:
        return SolverResult(
            parameters=parameters,
            require_canonical_r2=require_canonical_r2,
            status="unsat",
            witness=None,
            reason_unknown=None,
        )

    model = solver.model()
    seed_bits = _decode_bitvector(
        model.eval(b_seed, model_completion=True).as_long(),
        width=t,
    )
    if q_tail_word is None:
        q_tail_bits: tuple[int, ...] = ()
    else:
        q_tail_bits = _decode_bitvector(
            model.eval(q_tail_word, model_completion=True).as_long(),
            width=q_prefix_length - 1,
        )
    words = _build_words(
        parameters,
        tuple(bit + 2 for bit in seed_bits),
        tuple(bit + 2 for bit in q_tail_bits),
    )
    if not _direct_assignment_satisfies(
        parameters,
        words,
        require_canonical_r2=require_canonical_r2,
    ):
        raise AssertionError("SMT witness failed the definition-first audit")
    return SolverResult(
        parameters=parameters,
        require_canonical_r2=require_canonical_r2,
        status="sat",
        witness=words,
        reason_unknown=None,
    )


def run_direct_oracle(
    *,
    max_q: int,
    timeout_ms: int,
) -> DirectOracleSummary:
    """Compare solver existence with literal concrete enumeration."""
    if max_q <= 0:
        raise ValueError("max_q must be positive")
    if timeout_ms <= 0:
        raise ValueError("timeout_ms must be positive")

    parameter_count = 0
    assignment_count = 0
    direct_sat = 0
    solver_sat = 0
    solver_unsat = 0
    solver_unknown = 0
    mismatches: list[OracleMismatch] = []

    for parameters in iter_parameter_triples(max_q=max_q):
        parameter_count += 1
        direct_exists = False
        for words in _iter_direct_words(parameters):
            assignment_count += 1
            if _direct_assignment_satisfies(
                parameters,
                words,
                require_canonical_r2=True,
            ):
                direct_exists = True
        if direct_exists:
            direct_sat += 1

        solver_result = solve_parameter(
            parameters,
            require_canonical_r2=True,
            timeout_ms=timeout_ms,
        )
        if solver_result.status == "sat":
            solver_sat += 1
        elif solver_result.status == "unsat":
            solver_unsat += 1
        else:
            solver_unknown += 1

        if (
            solver_result.status == "unknown"
            or (solver_result.status == "sat") != direct_exists
        ):
            mismatches.append(
                OracleMismatch(
                    parameters=parameters,
                    solver_status=solver_result.status,
                    direct_exists=direct_exists,
                )
            )

    return DirectOracleSummary(
        max_q=max_q,
        parameter_triples=parameter_count,
        structured_assignments=assignment_count,
        direct_sat=direct_sat,
        solver_sat=solver_sat,
        solver_unsat=solver_unsat,
        solver_unknown=solver_unknown,
        mismatches=tuple(mismatches),
    )


def scan_early_replay_wall(
    *,
    max_q: int,
    timeout_ms: int,
) -> ReplayScanSummary:
    """Check the necessary early-replay relaxation through ``max_q``."""
    if max_q <= 0:
        raise ValueError("max_q must be positive")
    if timeout_ms <= 0:
        raise ValueError("timeout_ms must be positive")

    rows: list[PerQSummary] = []
    total_parameters = 0
    total_sat = 0
    total_unsat = 0
    total_unknown = 0

    for q in range(1, max_q + 1):
        parameter_count = 0
        sat_count = 0
        unsat_count = 0
        unknown_count = 0
        for parameters in (
            item
            for item in iter_parameter_triples(max_q=q)
            if item.q == q
        ):
            parameter_count += 1
            result = solve_parameter(
                parameters,
                require_canonical_r2=True,
                timeout_ms=timeout_ms,
            )
            if result.status == "sat":
                sat_count += 1
            elif result.status == "unsat":
                unsat_count += 1
            else:
                unknown_count += 1

        if parameter_count:
            rows.append(
                PerQSummary(
                    q=q,
                    parameter_triples=parameter_count,
                    sat=sat_count,
                    unsat=unsat_count,
                    unknown=unknown_count,
                )
            )
        total_parameters += parameter_count
        total_sat += sat_count
        total_unsat += unsat_count
        total_unknown += unknown_count

    return ReplayScanSummary(
        max_q=max_q,
        timeout_ms=timeout_ms,
        parameter_triples=total_parameters,
        sat=total_sat,
        unsat=total_unsat,
        unknown=total_unknown,
        per_q=tuple(rows),
    )


def render_checkpoint(
    summary: ReplayScanSummary,
    oracle: DirectOracleSummary,
    collapses: tuple[CollapseCertificate, ...],
    endpoint_jump: EndpointJumpCertificate,
) -> str:
    """Render a deterministic evidence artifact with explicit scope."""
    if not all(audit_collapse_certificate(item) for item in collapses):
        raise ValueError("invalid collapse certificate")
    if not audit_endpoint_jump_certificate(endpoint_jump):
        raise ValueError("invalid endpoint-jump certificate")

    lines = [
        "label=bounded_binary_cell_C_p_gt_q_early_replay_qfbv",
        "status=COMPUTED",
        "solver_logic=QF_BV",
        "alphabet=2,3",
        "encoding=2->0,3->1,leftmost_symbol_is_MSB",
        "domain=q>2r>0,r/2<t<r,p=q+t",
        "audited_conjunction=canonical_X3_and_full_early_replay_and_canonical_R2",
        "necessary_relaxation=true",
        "omits=standalone_R2B,canonical_F_B3,later_replay,"
        "J_only_bridge_replay,canonical_H_pair_2_P,"
        "all_proper_period_caps",
        "uses_first_mismatch_trichotomy=false",
        f"max_q={summary.max_q}",
        f"timeout_ms={summary.timeout_ms}",
        f"parameter_triples={summary.parameter_triples}",
        f"sat={summary.sat}",
        f"unsat={summary.unsat}",
        f"unknown={summary.unknown}",
    ]
    for row in summary.per_q:
        lines.extend(
            (
                f"q_{row.q}_parameter_triples={row.parameter_triples}",
                f"q_{row.q}_sat={row.sat}",
                f"q_{row.q}_unsat={row.unsat}",
                f"q_{row.q}_unknown={row.unknown}",
            )
        )

    lines.extend(
        (
            f"oracle_max_q={oracle.max_q}",
            "oracle_method=definition_first_structured_enumeration",
            f"oracle_parameter_triples={oracle.parameter_triples}",
            f"oracle_structured_assignments={oracle.structured_assignments}",
            f"oracle_direct_sat={oracle.direct_sat}",
            f"oracle_solver_sat={oracle.solver_sat}",
            f"oracle_solver_unsat={oracle.solver_unsat}",
            f"oracle_solver_unknown={oracle.solver_unknown}",
            f"oracle_mismatch_count={len(oracle.mismatches)}",
            "oracle_mismatches="
            + json.dumps(
                [asdict(item) for item in oracle.mismatches],
                sort_keys=True,
                separators=(",", ":"),
            ),
            "historical_collapse_certificate_count=4",
            f"collapse_certificate_count={len(collapses)}",
        )
    )
    for index, certificate in enumerate(collapses, start=1):
        lines.append(
            f"collapse_certificate_{index}="
            + json.dumps(
                asdict(certificate),
                sort_keys=True,
                separators=(",", ":"),
            )
        )

    lines.extend(
        (
            f"endpoint_jump_q={endpoint_jump.q}",
            "endpoint_jump_certificate="
            + json.dumps(
                asdict(endpoint_jump),
                sort_keys=True,
                separators=(",", ":"),
            ),
            "NOT_A_PROOF: bounded QF_BV UNSAT is computed evidence only; "
            "the unbounded p>q wall and Cell C remain open.",
        )
    )
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit the Cell C p>q early-replay relaxation."
    )
    parser.add_argument("--max-q", type=int, default=40)
    parser.add_argument("--oracle-max-q", type=int, default=14)
    parser.add_argument("--timeout-ms", type=int, default=3000)
    args = parser.parse_args(argv)

    summary = scan_early_replay_wall(
        max_q=args.max_q,
        timeout_ms=args.timeout_ms,
    )
    oracle = run_direct_oracle(
        max_q=args.oracle_max_q,
        timeout_ms=args.timeout_ms,
    )
    print(
        render_checkpoint(
            summary,
            oracle,
            known_collapse_certificates(),
            endpoint_jump_certificate(),
        ),
        end="",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
