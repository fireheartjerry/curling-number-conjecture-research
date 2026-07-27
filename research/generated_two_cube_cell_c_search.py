"""Equality-first bounded search for the internal Generated Two-Cube cell.

The search is record-free: it takes the early state ``E = L R T`` as a
bounded binary local start, verifies the complete forward orbit segment
through ``H`` with an exact canonical oracle, and evaluates both the original
two-window family I and the bridge-inclusive family J.  The integer and
equality filters are necessary Cell C residual conditions, not proof rules.
Zero bounded survivors is explicitly not a proof.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Iterator, Sequence
from dataclasses import asdict, dataclass
from itertools import product
from math import gcd

Word = tuple[int, ...]
RootParameterFamily = tuple[Word, int, int, int]


@dataclass(frozen=True)
class CellCParameters:
    """Integer residual parameters for an internal later cube."""

    q: int
    b: int
    j: int
    r: int

    @property
    def P(self) -> int:
        return self.q + self.b

    @property
    def s(self) -> int:
        return self.b + self.j

    @property
    def m(self) -> int:
        return self.q - self.j

    @property
    def N(self) -> int:
        """Length of V = YBT = BRBT."""
        return self.P + self.s

    @property
    def alpha(self) -> int:
        """Start of the suffix r-cube relative to V = YBT."""
        return self.N - 3 * self.r


@dataclass(frozen=True)
class PrecompletionTimes:
    """Chronological relative indices for the two target families."""

    I: tuple[int, ...]
    J: tuple[int, ...]
    J_only: tuple[int, ...]


@dataclass(frozen=True)
class CellCEvent:
    time: int
    word: Word
    exponent: int
    period: int


@dataclass(frozen=True)
class CellCCertificate:
    """Complete exact local trace for one retained Cell C antecedent."""

    L: Word
    R: Word
    B: Word
    T: Word
    U: Word
    E: Word
    requested: Word
    q: int
    b: int
    j: int
    r: int
    P: int
    s: int
    alpha: int
    ybt_start: int
    cube_start: int
    standalone_witness: tuple[int, int]
    events: tuple[CellCEvent, ...]
    I_times: tuple[int, ...]
    J_times: tuple[int, ...]
    J_only_times: tuple[int, ...]
    max_period_over_I: int
    max_period_over_J: int
    I_witness: bool
    J_witness: bool


@dataclass(frozen=True)
class CellCScanSummary:
    max_start_length: int
    parameter_tuples: int
    equality_assignments: int
    standalone_no_cube_assignments: int
    bounded_contexts: int
    actual_generation_traces: int
    g2cs_antecedents: int
    I_witnesses: int
    I_survivors: int
    J_witnesses: int
    J_survivors: int
    J_only_witnesses: int
    root_parameter_families: tuple[RootParameterFamily, ...]
    boundary_s_eq_2r_j_eq_r_antecedents: int
    positive_certificate: CellCCertificate | None
    survivor_certificates: tuple[CellCCertificate, ...]


class _UnionFind:
    def __init__(self, size: int) -> None:
        self._parent = list(range(size))

    def find(self, item: int) -> int:
        parent = self._parent[item]
        if parent != item:
            self._parent[item] = self.find(parent)
        return self._parent[item]

    def union(self, left: int, right: int) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root == right_root:
            return
        smaller, larger = sorted((left_root, right_root))
        self._parent[larger] = smaller


def exact_canonical_witness(sequence: Sequence[int]) -> tuple[int, int]:
    """Return maximal suffix exponent and its shortest maximizing period."""
    word = tuple(sequence)
    if not word:
        raise ValueError("exact_canonical_witness requires a nonempty word")

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


def iter_cell_c_parameters(
    *, max_q: int, max_start_length: int | None = None
) -> Iterator[CellCParameters]:
    """Yield Cell C integer residuals in deterministic lexical order.

    With ``max_start_length`` supplied, ``q+j <= max_start_length`` is the
    exact condition that at least the empty-left-context start ``E=RT`` fits
    under the local-start cap.
    """
    if max_q <= 0:
        raise ValueError("max_q must be positive")
    if max_start_length is not None and max_start_length <= 0:
        raise ValueError("max_start_length must be positive")

    for q in range(1, max_q + 1):
        for b in range(1, q):
            P = q + b
            for j in range(q):
                if (
                    max_start_length is not None
                    and q + j > max_start_length
                ):
                    continue
                s = b + j
                N = P + s
                for r in range(1, P):
                    alpha = N - 3 * r
                    if alpha < 0:
                        continue
                    if not r < s < 3 * r:
                        continue
                    if not 2 * r <= P - gcd(r, P) - 1:
                        continue
                    yield CellCParameters(q=q, b=b, j=j, r=r)


def _root_coordinate(parameter: CellCParameters, position: int) -> int:
    """Map a coordinate of V=BRBT back to its source coordinate in R."""
    q, b, P, N = (
        parameter.q,
        parameter.b,
        parameter.P,
        parameter.N,
    )
    if not 0 <= position < N:
        raise ValueError("V coordinate outside the half-open interval [0,N)")
    if position < b:
        return q - b + position
    if position < P:
        return position - b
    if position < P + b:
        return q - b + position - P
    return position - P - b


def iter_equality_roots(parameter: CellCParameters) -> Iterator[Word]:
    """Yield exactly the binary roots displaying the required suffix r-cube."""
    classes = _UnionFind(parameter.q)
    for position in range(parameter.alpha, parameter.N - parameter.r):
        classes.union(
            _root_coordinate(parameter, position),
            _root_coordinate(parameter, position + parameter.r),
        )

    representatives = sorted(
        {classes.find(position) for position in range(parameter.q)}
    )
    forced = classes.find(parameter.j)
    free = tuple(
        representative
        for representative in representatives
        if representative != forced
    )

    for values in product((2, 3), repeat=len(free)):
        assignment = dict(zip(free, values))
        assignment[forced] = 3
        yield tuple(
            assignment[classes.find(position)]
            for position in range(parameter.q)
        )


def cell_c_precompletion_times(*, q: int, b: int, j: int) -> PrecompletionTimes:
    """Return relative state times for I, J, and the bridge-only difference."""
    if not 0 < b < q:
        raise ValueError("requires 0 < b < q")
    if not 0 <= j < q:
        raise ValueError("requires 0 <= j < q")

    m = q - j
    P = q + b
    I = tuple(range(m + 1)) + tuple(range(P, P + m))
    J = tuple(range(P + m))
    J_only = tuple(range(m + 1, P))
    return PrecompletionTimes(I=I, J=J, J_only=J_only)


def _generated_trace(
    start: Word, requested: Word
) -> tuple[CellCEvent, ...] | None:
    current = start
    events: list[CellCEvent] = []
    for time, expected in enumerate(requested):
        exponent, period = exact_canonical_witness(current)
        if exponent != expected:
            return None
        events.append(
            CellCEvent(
                time=time,
                word=current,
                exponent=exponent,
                period=period,
            )
        )
        current += (exponent,)

    exponent, period = exact_canonical_witness(current)
    events.append(
        CellCEvent(
            time=len(requested),
            word=current,
            exponent=exponent,
            period=period,
        )
    )
    return tuple(events)


def _is_complete_g2cs_cell_c_antecedent(
    parameter: CellCParameters,
    standalone_witness: tuple[int, int],
    events: tuple[CellCEvent, ...],
) -> bool:
    m = parameter.m
    terminal_time = parameter.P + m
    return (
        standalone_witness[0] == 2
        and events[0].exponent == 3
        and (events[m].exponent, events[m].period) == (2, parameter.q)
        and (
            events[parameter.P].exponent,
            events[parameter.P].period,
        )
        == (3, parameter.r)
        and (
            events[terminal_time].exponent,
            events[terminal_time].period,
        )
        == (2, parameter.P)
    )


def _make_certificate(
    *,
    L: Word,
    R: Word,
    parameter: CellCParameters,
    requested: Word,
    standalone_witness: tuple[int, int],
    events: tuple[CellCEvent, ...],
) -> CellCCertificate:
    B = R[-parameter.b :]
    T = R[: parameter.j]
    U = R[parameter.j :]
    E = L + R + T
    times = cell_c_precompletion_times(
        q=parameter.q, b=parameter.b, j=parameter.j
    )
    max_I = max(events[time].period for time in times.I)
    max_J = max(events[time].period for time in times.J)
    ybt_start = len(L) + parameter.q - parameter.b
    return CellCCertificate(
        L=L,
        R=R,
        B=B,
        T=T,
        U=U,
        E=E,
        requested=requested,
        q=parameter.q,
        b=parameter.b,
        j=parameter.j,
        r=parameter.r,
        P=parameter.P,
        s=parameter.s,
        alpha=parameter.alpha,
        ybt_start=ybt_start,
        cube_start=ybt_start + parameter.alpha,
        standalone_witness=standalone_witness,
        events=events,
        I_times=times.I,
        J_times=times.J,
        J_only_times=times.J_only,
        max_period_over_I=max_I,
        max_period_over_J=max_J,
        I_witness=max_I >= parameter.P,
        J_witness=max_J >= parameter.P,
    )


def scan_bounded_cell_c(*, max_start_length: int) -> CellCScanSummary:
    """Exhaust the binary Cell C residual with ``1 <= |E| <=`` the cap."""
    if max_start_length <= 0:
        raise ValueError("max_start_length must be positive")

    parameter_tuples = 0
    equality_assignments = 0
    standalone_no_cube_assignments = 0
    bounded_contexts = 0
    actual_generation_traces = 0
    g2cs_antecedents = 0
    I_witnesses = 0
    I_survivors = 0
    J_witnesses = 0
    J_survivors = 0
    J_only_witnesses = 0
    boundary_s_eq_2r_j_eq_r_antecedents = 0
    families: set[RootParameterFamily] = set()
    seen_actual: set[tuple[Word, Word, int, int, int]] = set()
    seen_antecedents: set[tuple[Word, Word, int, int, int]] = set()
    positive_certificate: CellCCertificate | None = None
    survivor_certificates: list[CellCCertificate] = []

    parameters = iter_cell_c_parameters(
        max_q=max_start_length,
        max_start_length=max_start_length,
    )
    for parameter in parameters:
        parameter_tuples += 1
        for R in iter_equality_roots(parameter):
            equality_assignments += 1
            T = R[: parameter.j]
            standalone_witness = exact_canonical_witness(R + R + T)
            if standalone_witness[0] != 2:
                continue
            standalone_no_cube_assignments += 1

            B = R[-parameter.b :]
            U = R[parameter.j :]
            requested = U + B + T + U
            maximum_left_length = (
                max_start_length - parameter.q - parameter.j
            )
            for left_length in range(maximum_left_length + 1):
                for L in product((2, 3), repeat=left_length):
                    bounded_contexts += 1
                    E = L + R + T
                    events = _generated_trace(E, requested)
                    if events is None:
                        continue

                    structural_key = (
                        L,
                        R,
                        parameter.b,
                        parameter.j,
                        parameter.r,
                    )
                    if structural_key in seen_actual:
                        continue
                    seen_actual.add(structural_key)
                    actual_generation_traces += 1

                    if not _is_complete_g2cs_cell_c_antecedent(
                        parameter, standalone_witness, events
                    ):
                        continue
                    if structural_key in seen_antecedents:
                        continue
                    seen_antecedents.add(structural_key)
                    g2cs_antecedents += 1

                    certificate = _make_certificate(
                        L=L,
                        R=R,
                        parameter=parameter,
                        requested=requested,
                        standalone_witness=standalone_witness,
                        events=events,
                    )
                    if positive_certificate is None:
                        positive_certificate = certificate
                    families.add(
                        (R, parameter.b, parameter.j, parameter.r)
                    )
                    if (
                        parameter.s == 2 * parameter.r
                        and parameter.j == parameter.r
                    ):
                        boundary_s_eq_2r_j_eq_r_antecedents += 1

                    if certificate.I_witness:
                        I_witnesses += 1
                    else:
                        I_survivors += 1
                        survivor_certificates.append(certificate)

                    if certificate.J_witness:
                        J_witnesses += 1
                    else:
                        J_survivors += 1

                    if (
                        not certificate.I_witness
                        and certificate.J_witness
                    ):
                        J_only_witnesses += 1

    return CellCScanSummary(
        max_start_length=max_start_length,
        parameter_tuples=parameter_tuples,
        equality_assignments=equality_assignments,
        standalone_no_cube_assignments=standalone_no_cube_assignments,
        bounded_contexts=bounded_contexts,
        actual_generation_traces=actual_generation_traces,
        g2cs_antecedents=g2cs_antecedents,
        I_witnesses=I_witnesses,
        I_survivors=I_survivors,
        J_witnesses=J_witnesses,
        J_survivors=J_survivors,
        J_only_witnesses=J_only_witnesses,
        root_parameter_families=tuple(sorted(families)),
        boundary_s_eq_2r_j_eq_r_antecedents=(
            boundary_s_eq_2r_j_eq_r_antecedents
        ),
        positive_certificate=positive_certificate,
        survivor_certificates=tuple(survivor_certificates),
    )


def _serialize_certificate(certificate: CellCCertificate) -> str:
    return json.dumps(
        asdict(certificate), sort_keys=True, separators=(",", ":")
    )


def render_scan(summary: CellCScanSummary) -> str:
    """Serialize a scan deterministically, without machine-time fields."""
    lines = [
        "label=bounded_binary_record_free_cell_C_residual",
        f"max_start_length={summary.max_start_length}",
        "alphabet=2,3",
        "bound=1<=|E=LRT|<=max_start_length",
    ]
    for field in (
        "parameter_tuples",
        "equality_assignments",
        "standalone_no_cube_assignments",
        "bounded_contexts",
        "actual_generation_traces",
        "g2cs_antecedents",
        "I_witnesses",
        "I_survivors",
        "J_witnesses",
        "J_survivors",
        "J_only_witnesses",
    ):
        lines.append(f"{field}={getattr(summary, field)}")

    lines.append(
        f"root_parameter_families={len(summary.root_parameter_families)}"
    )
    for R, b, j, r in summary.root_parameter_families:
        lines.append(
            "root_parameter_family="
            + json.dumps(
                {"R": R, "b": b, "j": j, "r": r},
                sort_keys=True,
                separators=(",", ":"),
            )
        )
    lines.append(
        "boundary_s_eq_2r_j_eq_r_antecedents="
        f"{summary.boundary_s_eq_2r_j_eq_r_antecedents}"
    )
    if summary.positive_certificate is None:
        lines.append("positive_certificate=null")
    else:
        lines.append(
            "positive_certificate="
            + _serialize_certificate(summary.positive_certificate)
        )
    lines.append(
        f"survivor_certificates={len(summary.survivor_certificates)}"
    )
    for certificate in summary.survivor_certificates:
        lines.append(
            "survivor_certificate=" + _serialize_certificate(certificate)
        )
    lines.append(
        "NOT_A_PROOF: bounded record-free Cell C residual scan; "
        "zero bounded survivors is not a proof."
    )
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Equality-first bounded search for G2CS Cell C."
    )
    parser.add_argument("--max-start-length", type=int, default=18)
    args = parser.parse_args(argv)
    summary = scan_bounded_cell_c(
        max_start_length=args.max_start_length
    )
    print(render_scan(summary), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
