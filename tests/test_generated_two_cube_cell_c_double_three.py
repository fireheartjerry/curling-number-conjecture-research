"""Definition-first regressions for the Cell C double-``3`` row.

The bounded scans in this file deliberately do not import either production
Cell C search.  They check literal finite words and are evidence only; the
unbounded proof lives in ``research/generated_two_cube_cells.md``.
"""

from itertools import product

import pytest

from research.generated_two_cube_cell_c_double_three import (
    definition_first_witness,
    q23_z1_endpoint_near_model,
    scan_pgtq_double_three,
    scan_pltq_double_three,
)


Word = tuple[int, ...]


def _literal_reference_witness(word: Word) -> tuple[int, int]:
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


@pytest.fixture(scope="module")
def pgtq_q20():
    return scan_pgtq_double_three(max_q=20)


@pytest.fixture(scope="module")
def pltq_q20():
    return scan_pltq_double_three(max_q=20)


def test_definition_first_witness_matches_a_separate_literal_oracle():
    checked = 0
    for length in range(1, 10):
        for word in product((2, 3), repeat=length):
            assert definition_first_witness(word) == (
                _literal_reference_witness(word)
            )
            checked += 1
    assert checked == 1022


def test_pgtq_z2_rows_are_nonvacuous_but_f1_never_has_label_three(
    pgtq_q20,
):
    assert pgtq_q20.branch == "p>q"
    assert pgtq_q20.max_q == 20
    assert pgtq_q20.z2_h0_candidates == 1394
    assert pgtq_q20.z2_h1_candidates == 1447
    assert pgtq_q20.z2_h0_f1_kappa_counts == ((1, 399), (2, 995))
    assert pgtq_q20.z2_h1_f1_kappa_counts == ((1, 43), (2, 1404))
    assert pgtq_q20.f1_label_three_candidates == 0


def test_pltq_z2_rows_cover_both_exact_seams_and_have_no_f1_label_three(
    pltq_q20,
):
    assert pltq_q20.branch == "p<q"
    assert pltq_q20.max_q == 20
    assert pltq_q20.z2_h0_candidates == 1343
    assert pltq_q20.z2_h1_candidates == 673
    assert pltq_q20.z2_h0_f1_kappa_counts == ((1, 1090), (2, 253))
    assert pltq_q20.z2_h1_f1_kappa_counts == ((1, 547), (2, 126))
    assert pltq_q20.seam_row_counts == (
        ("D=JBTheta", 1343, 672),
        ("D=B[c:]Theta", 0, 1),
    )
    assert pltq_q20.f1_label_three_candidates == 0


def test_q23_z1_near_model_has_exact_endpoints_but_fails_at_phase_13():
    model = q23_z1_endpoint_near_model()

    assert (model.q, model.r, model.p, model.P) == (23, 4, 13, 27)
    assert (model.nu, model.c) == (2, 1)
    assert model.B == tuple(map(int, "2232"))
    assert model.Theta == tuple(map(int, "32"))
    assert model.D == tuple(map(int, "23232"))
    assert model.Q == tuple(map(int, "322232223223232"))
    assert model.U == tuple(map(int, "3222322232232322232"))
    assert model.R == tuple(map(int, "22323222322232232322232"))
    assert model.X == tuple(map(int, "2323222322232"))

    assert model.D == model.B[model.c :] + model.Theta
    assert model.B[: model.c] == model.B[-model.c :]
    assert model.X == model.A + model.C
    assert model.U == model.C + model.A + model.H0

    early_start = model.X * 3
    late_start = early_start + model.U + model.B * 2
    assert definition_first_witness(model.R * 2) == (2, model.q)
    assert definition_first_witness(model.R * 2 + model.B) == (2, model.r)
    assert definition_first_witness(model.B + model.R + model.B * 2) == (
        3,
        model.r,
    )
    assert definition_first_witness(early_start) == (3, model.p)
    assert definition_first_witness(early_start + model.U) == (2, model.q)
    assert definition_first_witness(late_start) == (3, model.r)
    assert definition_first_witness(late_start + model.U) == (2, model.P)

    assert (model.z, model.h) == (1, 0)
    assert model.matched_phases == 13
    assert model.failure_phase == 13
    assert model.U[model.failure_phase] == 3
    assert model.early_pairs[model.failure_phase] == (2, 3)
    assert model.late_pairs[model.failure_phase] == (2, 3)
    assert tuple(pair[0] for pair in model.early_pairs[:13]) == model.U[:13]
    assert tuple(pair[0] for pair in model.late_pairs[:13]) == model.U[:13]

    # The endpoint scales and a long synchronized prefix are exact, but the
    # internal replay still fails.  This is a sharpness model, not a survivor.
    assert model.failure_phase < len(model.U)
