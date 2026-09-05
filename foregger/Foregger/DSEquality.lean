import Foregger.Basic
import Foregger.Variance
import Mathlib.Data.Matrix.Mul

open scoped BigOperators Matrix
open Matrix Finset

namespace Foregger

/-- The squared Euclidean mass of a real coordinate vector, written without the `WithLp`
wrapper so the equality case reduces to finite-sum algebra. -/
def sqMass {n : ℕ} (x : Fin n → ℝ) : ℝ := ∑ i, x i ^ 2

/-- Rowwise Jensen for a doubly stochastic matrix. -/
theorem isDS_row_sq_le {n : ℕ} {A : RMat n} (hA : IsDS A)
    (x : Fin n → ℝ) (i : Fin n) :
    (A *ᵥ x) i ^ 2 ≤ ∑ j, A i j * x j ^ 2 := by
  have h := sq_weighted_sum_le_weighted_sq_sum
    (w := fun j : Fin n => A i j) x
    (fun j => isDS_nonneg hA i j) (isDS_row_sum hA i)
  simpa only [Matrix.mulVec_apply_eq_sum] using h

/-- Column stochasticity collapses the sum of the rowwise second moments. -/
theorem isDS_sum_weighted_sq {n : ℕ} {A : RMat n} (hA : IsDS A)
    (x : Fin n → ℝ) :
    (∑ i, ∑ j, A i j * x j ^ 2) = sqMass x := by
  classical
  rw [Finset.sum_comm]
  unfold sqMass
  apply Finset.sum_congr rfl
  intro j hj
  rw [← Finset.sum_mul]
  rw [isDS_col_sum hA j]
  simp

/-- Doubly stochastic matrices contract squared Euclidean mass. -/
theorem isDS_sqMass_mulVec_le {n : ℕ} {A : RMat n} (hA : IsDS A)
    (x : Fin n → ℝ) : sqMass (A *ᵥ x) ≤ sqMass x := by
  unfold sqMass
  calc
    (∑ i, (A *ᵥ x) i ^ 2) ≤ ∑ i, ∑ j, A i j * x j ^ 2 :=
      Finset.sum_le_sum (fun i _ => isDS_row_sq_le hA x i)
    _ = sqMass x := isDS_sum_weighted_sq hA x

/-- The nonnegative loss in the square inequality at one row. -/
def rowDeficit {n : ℕ} (A : RMat n) (x : Fin n → ℝ) (i : Fin n) : ℝ :=
  (∑ j, A i j * x j ^ 2) - (A *ᵥ x) i ^ 2

theorem rowDeficit_nonneg {n : ℕ} {A : RMat n} (hA : IsDS A)
    (x : Fin n → ℝ) (i : Fin n) : 0 ≤ rowDeficit A x i := by
  unfold rowDeficit
  linarith [isDS_row_sq_le hA x i]

/-- The total row deficit is exactly the global loss of squared Euclidean mass. -/
theorem sum_rowDeficit {n : ℕ} {A : RMat n} (hA : IsDS A)
    (x : Fin n → ℝ) :
    ∑ i, rowDeficit A x i = sqMass x - sqMass (A *ᵥ x) := by
  classical
  unfold rowDeficit
  rw [Finset.sum_sub_distrib]
  rw [isDS_sum_weighted_sq hA x]

/-- If a doubly stochastic matrix preserves squared mass on `x`, every individual row attains
its Jensen equality case. -/
theorem row_sq_eq_of_sqMass_eq {n : ℕ} {A : RMat n} (hA : IsDS A)
    (x : Fin n → ℝ) (heq : sqMass (A *ᵥ x) = sqMass x) (i : Fin n) :
    (A *ᵥ x) i ^ 2 = ∑ j, A i j * x j ^ 2 := by
  have hsum : ∑ r, rowDeficit A x r = 0 := by
    rw [sum_rowDeficit hA x, heq]
    ring
  have hi : rowDeficit A x i = 0 :=
    (Finset.sum_eq_zero_iff_of_nonneg
      (fun r _ => rowDeficit_nonneg hA x r)).mp hsum i (Finset.mem_univ i)
  unfold rowDeficit at hi
  linarith

/-- Equality in the global `ℓ₂` contraction forces coordinates that occur with positive weight
in a common row to agree.  This is the key combinatorial equality statement used to recover the
stable block partition. -/
theorem eq_of_common_positive_row_of_sqMass_eq {n : ℕ} {A : RMat n} (hA : IsDS A)
    (x : Fin n → ℝ) (heq : sqMass (A *ᵥ x) = sqMass x)
    {r i j : Fin n} (hi : 0 < A r i) (hj : 0 < A r j) : x i = x j := by
  have hrow := row_sq_eq_of_sqMass_eq hA x heq r
  have hrow' :
      (∑ t, A r t * x t) ^ 2 = ∑ t, A r t * x t ^ 2 := by
    simpa only [Matrix.mulVec_apply_eq_sum] using hrow
  exact eq_of_pos_weights_of_sq_eq
    (w := fun t : Fin n => A r t) x
    (fun t => isDS_nonneg hA r t) (isDS_row_sum hA r) hrow' hi hj

end Foregger
