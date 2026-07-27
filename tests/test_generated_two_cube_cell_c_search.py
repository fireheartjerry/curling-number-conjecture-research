import json
from itertools import product
from pathlib import Path

import pytest

from research.generated_two_cube_cell_c_search import (
    cell_c_precompletion_times,
    exact_canonical_witness,
    iter_cell_c_parameters,
    iter_equality_roots,
    render_scan,
    scan_bounded_cell_c,
)


def _independent_canonical_witness(
    word: tuple[int, ...],
) -> tuple[int, int]:
    """Definition-first oracle, deliberately unlike the production loop."""
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


def _displays_required_cell_c_cube(
    root: tuple[int, ...],
    *,
    b: int,
    j: int,
    r: int,
) -> bool:
    B = root[-b:]
    T = root[:j]
    ybt = B + root + B + T
    cube = ybt[-3 * r :]
    return len(cube) == 3 * r and cube == cube[:r] * 3


def test_exact_canonical_witness_matches_independent_binary_oracle_through_10():
    checked = 0
    for length in range(1, 11):
        for word in product((2, 3), repeat=length):
            assert exact_canonical_witness(word) == _independent_canonical_witness(
                word
            )
            checked += 1

    assert checked == 2046


def test_equality_first_roots_match_bruteforce_through_q_8():
    parameters = tuple(iter_cell_c_parameters(max_q=8))
    assert len(parameters) == 197
    assert any(parameter.j == 0 for parameter in parameters)

    equality_assignments = 0
    for parameter in parameters:
        generated = set(iter_equality_roots(parameter))
        brute = {
            root
            for root in product((2, 3), repeat=parameter.q)
            if root[parameter.j] == 3
            and _displays_required_cell_c_cube(
                root,
                b=parameter.b,
                j=parameter.j,
                r=parameter.r,
            )
        }
        assert generated == brute
        equality_assignments += len(generated)

    assert equality_assignments == 1036


def test_positive_certificate_has_exact_orbit_and_cell_c_coordinates():
    summary = scan_bounded_cell_c(max_start_length=12)
    certificate = summary.positive_certificate

    assert certificate is not None
    assert certificate.L == tuple(map(int, "23222322"))
    assert certificate.R == tuple(map(int, "232"))
    assert certificate.B == (2,)
    assert certificate.T == (2,)
    assert certificate.U == (3, 2)
    assert certificate.E == tuple(map(int, "232223222322"))
    assert certificate.requested == tuple(map(int, "322232"))
    assert (certificate.q, certificate.P, certificate.r) == (3, 4, 1)
    assert (certificate.b, certificate.j, certificate.s) == (1, 1, 2)
    assert certificate.ybt_start == 10
    assert certificate.cube_start == 13
    assert certificate.cube_start >= certificate.ybt_start
    assert certificate.standalone_witness == (2, 1)
    assert tuple(
        (event.exponent, event.period) for event in certificate.events
    ) == (
        (3, 4),
        (2, 3),
        (2, 3),
        (2, 1),
        (3, 1),
        (2, 7),
        (2, 4),
    )
    assert certificate.I_times == (0, 1, 2, 4, 5)
    assert certificate.J_times == (0, 1, 2, 3, 4, 5)
    assert certificate.J_only_times == (3,)
    assert certificate.max_period_over_I == 7
    assert certificate.max_period_over_J == 7


def test_precompletion_times_distinguish_i_from_the_bridge():
    times = cell_c_precompletion_times(q=3, b=1, j=1)

    assert times.I == (0, 1, 2, 4, 5)
    assert times.J == (0, 1, 2, 3, 4, 5)
    assert times.J_only == (3,)


def test_length_12_integration_counts_are_exact_and_nonvacuous():
    summary = scan_bounded_cell_c(max_start_length=12)

    assert summary.max_start_length == 12
    assert summary.parameter_tuples == 428
    assert summary.equality_assignments == 10567
    assert summary.standalone_no_cube_assignments == 3444
    assert summary.bounded_contexts == 22840
    assert summary.actual_generation_traces == 1
    assert summary.g2cs_antecedents == 1
    assert summary.I_witnesses == 1
    assert summary.I_survivors == 0
    assert summary.J_witnesses == 1
    assert summary.J_survivors == 0
    assert summary.J_only_witnesses == 0
    assert summary.root_parameter_families == (
        ((2, 3, 2), 1, 1, 1),
    )
    assert summary.boundary_s_eq_2r_j_eq_r_antecedents == 1
    assert summary.survivor_certificates == ()


def test_render_scan_is_deterministic_and_serializes_full_certificate():
    summary = scan_bounded_cell_c(max_start_length=12)

    first = render_scan(summary)
    second = render_scan(summary)

    assert first == second
    assert first.startswith("label=bounded_binary_record_free_cell_C_residual\n")
    assert "max_start_length=12\n" in first
    assert "I_survivors=0\n" in first
    assert "J_survivors=0\n" in first
    assert first.endswith(
        "NOT_A_PROOF: bounded record-free Cell C residual scan; "
        "zero bounded survivors is not a proof.\n"
    )

    certificate_line = next(
        line
        for line in first.splitlines()
        if line.startswith("positive_certificate=")
    )
    serialized = json.loads(certificate_line.split("=", 1)[1])
    assert serialized["E"] == list(map(int, "232223222322"))
    assert serialized["events"][0]["exponent"] == 3
    assert serialized["events"][-1]["period"] == 4


def test_preserved_length_18_scan_pins_simultaneous_boundary_count():
    output_path = (
        Path(__file__).parents[1]
        / "research"
        / "outputs"
        / "generated_two_cube_cell_c_scan_2026-07-27.txt"
    )
    output = output_path.read_text(encoding="utf-8")

    assert "g2cs_antecedents=120\n" in output
    assert "I_survivors=0\n" in output
    assert "J_survivors=0\n" in output
    assert (
        "boundary_s_eq_2r_j_eq_r_antecedents=120\n" in output
    )
    assert (
        'root_parameter_family={"R":[2,3,2],"b":1,"j":1,"r":1}\n'
        in output
    )


@pytest.mark.parametrize("bound", [0, -1])
def test_invalid_scan_and_parameter_bounds_fail_closed(bound):
    with pytest.raises(
        ValueError, match=r"^max_start_length must be positive$"
    ):
        scan_bounded_cell_c(max_start_length=bound)

    with pytest.raises(ValueError, match=r"^max_q must be positive$"):
        tuple(iter_cell_c_parameters(max_q=bound))
