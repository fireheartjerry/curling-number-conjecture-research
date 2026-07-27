"""Bounded search for the Cell C simultaneous-boundary branch ``p > q``.

This module searches the exact finite-word residual derived in
``generated_two_cube_cells.md``.  It enumerates binary words only after
applying the structural period equations, then checks every canonical
curling witness exactly.  A separate definition-first raw-root oracle audits
the small bound.  Neither zero survivors nor agreement of the two bounded
engines is a proof of Cell C.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Iterator, Sequence
from dataclasses import asdict, dataclass
from itertools import product

if __package__:
    from research.generated_two_cube_cell_c_search import (
        exact_canonical_witness,
    )
else:
    from generated_two_cube_cell_c_search import exact_canonical_witness

Word = tuple[int, ...]
Witness = tuple[int, int]


@dataclass(frozen=True)
class PgtqParameters:
    q: int
    r: int
    t: int

    @property
    def P(self) -> int:
        return self.q + self.r

    @property
    def p(self) -> int:
        return self.q + self.t

    @property
    def prefix_length(self) -> int:
        return self.q - 2 * self.r


@dataclass(frozen=True)
class PgtqModel:
    parameters: PgtqParameters
    B: Word
    C: Word
    U: Word
    R: Word
    X: Word


@dataclass(frozen=True)
class PgtqCertificate:
    q: int
    r: int
    t: int
    P: int
    p: int
    B: Word
    C: Word
    U: Word
    R: Word
    X: Word
    Y: Word
    rotated_Y: Word
    r2_witness: Witness
    standalone_witness: Witness
    x3_witness: Witness
    late_witnesses: tuple[Witness, ...]
    h_witness: Witness
    early_witnesses: tuple[Witness, ...]
    first_early_mismatch: tuple[int, int, Witness] | None
    shadow_predecessor: int
    shadow_last_symbol: int
    has_shifted_P_square: bool


@dataclass(frozen=True)
class PgtqScanSummary:
    max_q: int
    parameter_triples: int
    raw_root_parameter_pairs: int
    structured_assignments: int
    canonical_r2: int
    standalone_exponent_two: int
    canonical_x3: int
    late_exponent_replays: int
    exact_late_window_replays: int
    late_period_cap_survivors: int
    terminal_h_canonical: int
    early_after_exact_late_replays: int
    full_continuation_replays: int
    I_window_survivors: int
    J_window_survivors: int
    shifted_P_square_witnesses: int
    rotation_plus_B_factorizations: int
    first_mismatch_trichotomy_candidates: int
    trichotomy_z1_h0: int
    trichotomy_z2_h0: int
    trichotomy_z2_h1: int
    trichotomy_early_failure_phase_0: int
    trichotomy_early_failure_phase_1: int
    trichotomy_early_failure_phase_2: int
    trichotomy_early_failure_phase_other: int
    trichotomy_early_endpoint_failures: int
    trichotomy_exact_early_windows: int
    late_replay_certificate: PgtqCertificate | None


@dataclass(frozen=True)
class DefinitionFirstOracleSummary:
    max_q: int
    parameter_triples: int
    raw_root_parameter_pairs: int
    structured_assignments: int
    canonical_r2: int
    standalone_exponent_two: int
    canonical_x3: int
    late_exponent_replays: int
    exact_late_window_replays: int
    late_period_cap_survivors: int
    terminal_h_canonical: int
    early_after_exact_late_replays: int
    full_continuation_replays: int
    I_window_survivors: int
    J_window_survivors: int


def definition_first_witness(sequence: Sequence[int]) -> Witness:
    """Return ``(kappa, pi)`` by literal exponent/period enumeration."""
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


def iter_pgtq_parameters(*, max_q: int) -> Iterator[PgtqParameters]:
    """Yield every integer triple with ``q>2r`` and ``r/2<t<r``."""
    if max_q <= 0:
        raise ValueError("max_q must be positive")

    for q in range(1, max_q + 1):
        for r in range(1, (q - 1) // 2 + 1):
            for t in range(r // 2 + 1, r):
                if 2 * t > r:
                    yield PgtqParameters(q=q, r=r, t=t)


def raw_root_parameter_pairs(*, max_q: int) -> int:
    """Count the raw binary ``R`` words before structural pruning."""
    return sum(
        2**parameters.q
        for parameters in iter_pgtq_parameters(max_q=max_q)
    )


def iter_structured_models(
    parameters: PgtqParameters,
) -> Iterator[PgtqModel]:
    """Enumerate each structural ``(q,r,t,B,U)`` tuple exactly once."""
    q, r, t = parameters.q, parameters.r, parameters.t
    if not (q > 2 * r > 0 and r / 2 < t < r):
        raise ValueError("parameters must satisfy q>2r>0 and r/2<t<r")

    prefix_length = parameters.prefix_length
    for B_tail in product((2, 3), repeat=t - 1):
        period_seed = (2,) + B_tail
        B = tuple(period_seed[index % t] for index in range(r))
        for C_tail in product((2, 3), repeat=prefix_length - 1):
            C = (3,) + C_tail
            U = C + B
            R = B + U
            X = B[r - t :] + U + B
            yield PgtqModel(
                parameters=parameters,
                B=B,
                C=C,
                U=U,
                R=R,
                X=X,
            )


def _trace(
    start: Word,
    requested: Word,
    witness,
) -> tuple[tuple[Witness, ...], bool]:
    current = start
    events: list[Witness] = []
    matched = True
    for expected in requested:
        actual = witness(current)
        events.append(actual)
        if actual[0] != expected:
            matched = False
            break
        current += (expected,)
    if matched:
        events.append(witness(current))
    return tuple(events), matched


def _all_proper_periods_below(
    events: tuple[Witness, ...], P: int
) -> bool:
    return all(period < P for _, period in events[:-1])


def _make_certificate(
    model: PgtqModel,
    *,
    r2_witness: Witness,
    standalone_witness: Witness,
    x3_witness: Witness,
    late_witnesses: tuple[Witness, ...],
) -> PgtqCertificate:
    parameters = model.parameters
    P = parameters.P
    Y = model.B + model.B + model.U
    rotated_Y = (Y[-1],) + Y[:-1]
    late_start = model.X * 3 + model.U + model.B * 2
    pre_h = late_start + model.U[:-1]
    early_witnesses = tuple(
        exact_canonical_witness(model.X * 3 + model.U[:phase])
        for phase in range(len(model.U) + 1)
    )
    first_early_mismatch = next(
        (
            (phase, expected, early_witnesses[phase])
            for phase, expected in enumerate(model.U)
            if early_witnesses[phase][0] != expected
        ),
        None,
    )
    return PgtqCertificate(
        q=parameters.q,
        r=parameters.r,
        t=parameters.t,
        P=P,
        p=parameters.p,
        B=model.B,
        C=model.C,
        U=model.U,
        R=model.R,
        X=model.X,
        Y=Y,
        rotated_Y=rotated_Y,
        r2_witness=r2_witness,
        standalone_witness=standalone_witness,
        x3_witness=x3_witness,
        late_witnesses=late_witnesses[:-1],
        h_witness=late_witnesses[-1],
        early_witnesses=early_witnesses,
        first_early_mismatch=first_early_mismatch,
        shadow_predecessor=model.C[-1],
        shadow_last_symbol=model.B[-1],
        has_shifted_P_square=pre_h[-2 * P :] == rotated_Y * 2,
    )


def _first_two_and_mismatch(model: PgtqModel) -> tuple[int, int | None]:
    first_two = model.U.index(2)
    first_mismatch = next(
        (
            index
            for index, (left, right) in enumerate(zip(model.X, model.U))
            if left != right
        ),
        None,
    )
    return first_two, first_mismatch


def _terminal_three_run(B: Word) -> int:
    length = 0
    for symbol in reversed(B):
        if symbol != 3:
            break
        length += 1
    return length


def _scan_structured_models(max_q: int) -> PgtqScanSummary:
    parameter_triples = 0
    structured_assignments = 0
    canonical_r2 = 0
    standalone_exponent_two = 0
    canonical_x3 = 0
    late_exponent_replays = 0
    exact_late_window_replays = 0
    late_period_cap_survivors = 0
    terminal_h_canonical = 0
    early_after_exact_late_replays = 0
    full_continuation_replays = 0
    I_window_survivors = 0
    J_window_survivors = 0
    shifted_P_square_witnesses = 0
    rotation_plus_B_factorizations = 0
    first_mismatch_trichotomy_candidates = 0
    trichotomy_counts = {
        (1, 0): 0,
        (2, 0): 0,
        (2, 1): 0,
    }
    trichotomy_early_failures = {
        "phase_0": 0,
        "phase_1": 0,
        "phase_2": 0,
        "phase_other": 0,
    }
    trichotomy_early_endpoint_failures = 0
    trichotomy_exact_early_windows = 0
    certificate: PgtqCertificate | None = None

    for parameters in iter_pgtq_parameters(max_q=max_q):
        parameter_triples += 1
        P = parameters.P
        for model in iter_structured_models(parameters):
            structured_assignments += 1
            r2_witness = exact_canonical_witness(model.R * 2)
            if r2_witness != (2, parameters.q):
                continue
            canonical_r2 += 1

            standalone_witness = exact_canonical_witness(
                model.R * 2 + model.B
            )
            if standalone_witness[0] != 2:
                continue
            standalone_exponent_two += 1

            x3_witness = exact_canonical_witness(model.X * 3)
            if x3_witness != (3, parameters.p):
                continue
            canonical_x3 += 1

            first_two, first_mismatch = _first_two_and_mismatch(model)
            trichotomy_key = (first_two, first_mismatch)
            if (
                trichotomy_key in trichotomy_counts
                and _terminal_three_run(model.B) + first_two <= 2
            ):
                first_mismatch_trichotomy_candidates += 1
                trichotomy_counts[trichotomy_key] += 1
                early_state = model.X * 3
                for phase, expected in enumerate(model.U):
                    actual = (
                        x3_witness
                        if phase == 0
                        else exact_canonical_witness(early_state)
                    )
                    if actual[0] != expected:
                        if phase in (0, 1, 2):
                            trichotomy_early_failures[f"phase_{phase}"] += 1
                        else:
                            trichotomy_early_failures["phase_other"] += 1
                        break
                    early_state += (expected,)
                else:
                    if exact_canonical_witness(early_state) == (
                        2,
                        parameters.q,
                    ):
                        trichotomy_exact_early_windows += 1
                    else:
                        trichotomy_early_endpoint_failures += 1

            late_start = model.X * 3 + model.U + model.B * 2
            late_events, late_matched = _trace(
                late_start, model.U, exact_canonical_witness
            )
            if not late_matched:
                continue
            late_exponent_replays += 1
            if late_events[0] != (3, parameters.r):
                continue
            exact_late_window_replays += 1

            if _all_proper_periods_below(late_events, P):
                late_period_cap_survivors += 1
            h_canonical = late_events[-1] == (2, P)
            if h_canonical:
                terminal_h_canonical += 1

            early_events, early_matched = _trace(
                model.X * 3, model.U, exact_canonical_witness
            )
            early_exact = (
                early_matched
                and early_events[-1] == (2, parameters.q)
            )
            if early_exact:
                early_after_exact_late_replays += 1

            continuation = model.U + model.B * 2 + model.U
            full_events, full_matched = _trace(
                model.X * 3,
                continuation,
                exact_canonical_witness,
            )
            full_exact = full_matched and full_events[-1] == (2, P)
            if full_exact:
                full_continuation_replays += 1

            late_period_cap = _all_proper_periods_below(late_events, P)
            early_period_cap = (
                early_exact
                and _all_proper_periods_below(early_events, P)
            )
            if (
                late_period_cap
                and early_period_cap
                and h_canonical
            ):
                I_window_survivors += 1
            if (
                full_exact
                and _all_proper_periods_below(full_events, P)
            ):
                J_window_survivors += 1

            candidate = _make_certificate(
                model,
                r2_witness=r2_witness,
                standalone_witness=standalone_witness,
                x3_witness=x3_witness,
                late_witnesses=late_events,
            )
            if candidate.has_shifted_P_square:
                shifted_P_square_witnesses += 1
            if model.U == model.B[1:] + model.B[:1] + model.B:
                rotation_plus_B_factorizations += 1
            if certificate is None:
                certificate = candidate

    return PgtqScanSummary(
        max_q=max_q,
        parameter_triples=parameter_triples,
        raw_root_parameter_pairs=raw_root_parameter_pairs(max_q=max_q),
        structured_assignments=structured_assignments,
        canonical_r2=canonical_r2,
        standalone_exponent_two=standalone_exponent_two,
        canonical_x3=canonical_x3,
        late_exponent_replays=late_exponent_replays,
        exact_late_window_replays=exact_late_window_replays,
        late_period_cap_survivors=late_period_cap_survivors,
        terminal_h_canonical=terminal_h_canonical,
        early_after_exact_late_replays=early_after_exact_late_replays,
        full_continuation_replays=full_continuation_replays,
        I_window_survivors=I_window_survivors,
        J_window_survivors=J_window_survivors,
        shifted_P_square_witnesses=shifted_P_square_witnesses,
        rotation_plus_B_factorizations=rotation_plus_B_factorizations,
        first_mismatch_trichotomy_candidates=(
            first_mismatch_trichotomy_candidates
        ),
        trichotomy_z1_h0=trichotomy_counts[(1, 0)],
        trichotomy_z2_h0=trichotomy_counts[(2, 0)],
        trichotomy_z2_h1=trichotomy_counts[(2, 1)],
        trichotomy_early_failure_phase_0=trichotomy_early_failures[
            "phase_0"
        ],
        trichotomy_early_failure_phase_1=trichotomy_early_failures[
            "phase_1"
        ],
        trichotomy_early_failure_phase_2=trichotomy_early_failures[
            "phase_2"
        ],
        trichotomy_early_failure_phase_other=trichotomy_early_failures[
            "phase_other"
        ],
        trichotomy_early_endpoint_failures=(
            trichotomy_early_endpoint_failures
        ),
        trichotomy_exact_early_windows=trichotomy_exact_early_windows,
        late_replay_certificate=certificate,
    )


def scan_pgtq_boundary(*, max_q: int) -> PgtqScanSummary:
    """Run the equality-first production search through ``q=max_q``."""
    if max_q <= 0:
        raise ValueError("max_q must be positive")
    return _scan_structured_models(max_q)


def _model_from_raw_root(
    parameters: PgtqParameters, R: Word
) -> PgtqModel | None:
    r, t = parameters.r, parameters.t
    B = R[:r]
    U = R[r:]
    if B[0] != 2 or U[0] != 3 or U[-r:] != B:
        return None
    if any(B[index] != B[index - t] for index in range(t, r)):
        return None
    C = U[:-r]
    X = B[r - t :] + U + B
    return PgtqModel(
        parameters=parameters,
        B=B,
        C=C,
        U=U,
        R=R,
        X=X,
    )


def run_definition_first_oracle(
    *, max_q: int
) -> DefinitionFirstOracleSummary:
    """Raw-root small oracle using a definition-first canonical witness."""
    if max_q <= 0:
        raise ValueError("max_q must be positive")

    parameter_triples = 0
    raw_pairs = 0
    structured_assignments = 0
    canonical_r2 = 0
    standalone_exponent_two = 0
    canonical_x3 = 0
    late_exponent_replays = 0
    exact_late_window_replays = 0
    late_period_cap_survivors = 0
    terminal_h_canonical = 0
    early_after_exact_late_replays = 0
    full_continuation_replays = 0
    I_window_survivors = 0
    J_window_survivors = 0

    for parameters in iter_pgtq_parameters(max_q=max_q):
        parameter_triples += 1
        P = parameters.P
        for R in product((2, 3), repeat=parameters.q):
            raw_pairs += 1
            model = _model_from_raw_root(parameters, R)
            if model is None:
                continue
            structured_assignments += 1

            if definition_first_witness(model.R * 2) != (
                2,
                parameters.q,
            ):
                continue
            canonical_r2 += 1

            if definition_first_witness(model.R * 2 + model.B)[0] != 2:
                continue
            standalone_exponent_two += 1

            if definition_first_witness(model.X * 3) != (
                3,
                parameters.p,
            ):
                continue
            canonical_x3 += 1

            late_events, late_matched = _trace(
                model.X * 3 + model.U + model.B * 2,
                model.U,
                definition_first_witness,
            )
            if not late_matched:
                continue
            late_exponent_replays += 1
            if late_events[0] != (3, parameters.r):
                continue
            exact_late_window_replays += 1
            late_period_cap = _all_proper_periods_below(late_events, P)
            if late_period_cap:
                late_period_cap_survivors += 1
            h_canonical = late_events[-1] == (2, P)
            if h_canonical:
                terminal_h_canonical += 1

            early_events, early_matched = _trace(
                model.X * 3,
                model.U,
                definition_first_witness,
            )
            early_exact = (
                early_matched
                and early_events[-1] == (2, parameters.q)
            )
            if early_exact:
                early_after_exact_late_replays += 1

            continuation = model.U + model.B * 2 + model.U
            full_events, full_matched = _trace(
                model.X * 3,
                continuation,
                definition_first_witness,
            )
            full_exact = full_matched and full_events[-1] == (2, P)
            if full_exact:
                full_continuation_replays += 1

            if (
                late_period_cap
                and early_exact
                and _all_proper_periods_below(early_events, P)
                and h_canonical
            ):
                I_window_survivors += 1
            if (
                full_exact
                and _all_proper_periods_below(full_events, P)
            ):
                J_window_survivors += 1

    return DefinitionFirstOracleSummary(
        max_q=max_q,
        parameter_triples=parameter_triples,
        raw_root_parameter_pairs=raw_pairs,
        structured_assignments=structured_assignments,
        canonical_r2=canonical_r2,
        standalone_exponent_two=standalone_exponent_two,
        canonical_x3=canonical_x3,
        late_exponent_replays=late_exponent_replays,
        exact_late_window_replays=exact_late_window_replays,
        late_period_cap_survivors=late_period_cap_survivors,
        terminal_h_canonical=terminal_h_canonical,
        early_after_exact_late_replays=early_after_exact_late_replays,
        full_continuation_replays=full_continuation_replays,
        I_window_survivors=I_window_survivors,
        J_window_survivors=J_window_survivors,
    )


def render_scan(
    summary: PgtqScanSummary,
    oracle: DefinitionFirstOracleSummary,
) -> str:
    """Render deterministic evidence without machine-time fields."""
    lines = [
        "label=bounded_binary_cell_C_p_gt_q_boundary",
        f"max_q={summary.max_q}",
        "alphabet=2,3",
        "domain=q>2r>0,r/2<t<r,P=q+r,p=q+t",
        "dedup_key=q,r,t,B,U",
    ]
    for field in (
        "parameter_triples",
        "raw_root_parameter_pairs",
        "structured_assignments",
        "canonical_r2",
        "standalone_exponent_two",
        "canonical_x3",
        "late_exponent_replays",
        "exact_late_window_replays",
        "late_period_cap_survivors",
        "terminal_h_canonical",
        "early_after_exact_late_replays",
        "full_continuation_replays",
        "I_window_survivors",
        "J_window_survivors",
        "shifted_P_square_witnesses",
        "rotation_plus_B_factorizations",
        "first_mismatch_trichotomy_candidates",
        "trichotomy_z1_h0",
        "trichotomy_z2_h0",
        "trichotomy_z2_h1",
        "trichotomy_early_failure_phase_0",
        "trichotomy_early_failure_phase_1",
        "trichotomy_early_failure_phase_2",
        "trichotomy_early_failure_phase_other",
        "trichotomy_early_endpoint_failures",
        "trichotomy_exact_early_windows",
    ):
        lines.append(f"{field}={getattr(summary, field)}")

    if summary.late_replay_certificate is None:
        lines.append("late_replay_certificate=null")
    else:
        lines.append(
            "late_replay_certificate="
            + json.dumps(
                asdict(summary.late_replay_certificate),
                sort_keys=True,
                separators=(",", ":"),
            )
        )

    lines.extend(
        (
            f"oracle_max_q={oracle.max_q}",
            "oracle_method=raw_binary_R_definition_first_witness",
        )
    )
    for field in (
        "parameter_triples",
        "raw_root_parameter_pairs",
        "structured_assignments",
        "canonical_r2",
        "standalone_exponent_two",
        "canonical_x3",
        "late_exponent_replays",
        "exact_late_window_replays",
        "late_period_cap_survivors",
        "terminal_h_canonical",
        "early_after_exact_late_replays",
        "full_continuation_replays",
        "I_window_survivors",
        "J_window_survivors",
    ):
        lines.append(f"oracle_{field}={getattr(oracle, field)}")

    lines.extend(
        (
            "I_scope=exact early and late sampled windows plus endpoint scales",
            "J_scope=exact full proper continuation plus endpoint scale",
            "NOT_A_PROOF: bounded binary p>q boundary search; "
            "zero bounded survivors does not prove Cell C.",
        )
    )
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Search the Cell C p>q simultaneous boundary."
    )
    parser.add_argument("--max-q", type=int, default=25)
    parser.add_argument("--oracle-max-q", type=int, default=10)
    args = parser.parse_args(argv)

    summary = scan_pgtq_boundary(max_q=args.max_q)
    oracle = run_definition_first_oracle(max_q=args.oracle_max_q)
    print(render_scan(summary, oracle), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
