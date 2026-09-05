import Mathlib.Tactic

open scoped BigOperators
open Finset

namespace Foregger

/-- Finite weighted variance identity.  This is the algebraic equality case behind the
`ℓ₂` contraction of a stochastic row, and avoids an abstract strict-convexity dependency. -/
theorem weighted_variance_identity {α : Type*} [Fintype α]
    (w x : α → ℝ) (hw : ∑ i, w i = 1) :
    (∑ i, w i * x i ^ 2) - (∑ i, w i * x i) ^ 2 =
      ∑ i, w i * (x i - ∑ j, w j * x j) ^ 2 := by
  classical
  let μ : ℝ := ∑ i, w i * x i
  have hexpand (i : α) :
      w i * (x i - μ) ^ 2 =
        w i * x i ^ 2 - 2 * μ * (w i * x i) + μ ^ 2 * w i := by
    ring
  change (∑ i, w i * x i ^ 2) - μ ^ 2 = ∑ i, w i * (x i - μ) ^ 2
  simp_rw [hexpand, Finset.sum_add_distrib, Finset.sum_sub_distrib]
  rw [← Finset.mul_sum]
  rw [← Finset.mul_sum]
  rw [hw]
  ring

/-- Weighted Jensen for the square function, in the exact form needed later. -/
theorem sq_weighted_sum_le_weighted_sq_sum {α : Type*} [Fintype α]
    (w x : α → ℝ) (hw0 : ∀ i, 0 ≤ w i) (hw : ∑ i, w i = 1) :
    (∑ i, w i * x i) ^ 2 ≤ ∑ i, w i * x i ^ 2 := by
  rw [← sub_nonneg]
  rw [weighted_variance_identity w x hw]
  exact Finset.sum_nonneg (fun i _ => mul_nonneg (hw0 i) (sq_nonneg _))

/-- Equality in the weighted square inequality forces every positively weighted coordinate
to equal the weighted mean. -/
theorem eq_weighted_mean_of_sq_eq {α : Type*} [Fintype α]
    (w x : α → ℝ) (hw0 : ∀ i, 0 ≤ w i) (hw : ∑ i, w i = 1)
    (heq : (∑ i, w i * x i) ^ 2 = ∑ i, w i * x i ^ 2)
    {i : α} (hi : 0 < w i) :
    x i = ∑ j, w j * x j := by
  have hz : ∑ j, w j * (x j - ∑ t, w t * x t) ^ 2 = 0 := by
    rw [← weighted_variance_identity w x hw]
    linarith
  have hterm := (Finset.sum_eq_zero_iff_of_nonneg
      (fun j _ => mul_nonneg (hw0 j) (sq_nonneg _))).mp hz i (Finset.mem_univ i)
  have hsquare : (x i - ∑ j, w j * x j) ^ 2 = 0 := by
    exact (mul_eq_zero.mp hterm).resolve_left hi.ne'
  nlinarith

/-- Equality therefore identifies any two coordinates appearing with positive weight. -/
theorem eq_of_pos_weights_of_sq_eq {α : Type*} [Fintype α]
    (w x : α → ℝ) (hw0 : ∀ i, 0 ≤ w i) (hw : ∑ i, w i = 1)
    (heq : (∑ i, w i * x i) ^ 2 = ∑ i, w i * x i ^ 2)
    {i j : α} (hi : 0 < w i) (hj : 0 < w j) : x i = x j := by
  rw [eq_weighted_mean_of_sq_eq w x hw0 hw heq hi,
    eq_weighted_mean_of_sq_eq w x hw0 hw heq hj]

end Foregger
