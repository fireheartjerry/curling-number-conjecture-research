import Mathlib.Analysis.Convex.DoublyStochasticMatrix
import Mathlib.LinearAlgebra.Matrix.Permanent

open scoped BigOperators Matrix
open Matrix

namespace Foregger

abbrev RMat (n : ℕ) := Matrix (Fin n) (Fin n) ℝ

def IsDS {n : ℕ} (A : RMat n) : Prop :=
  A ∈ doublyStochastic ℝ (Fin n)

/-- Stronger eventual form of Foregger's conjecture. -/
def EventualPermanentDecrease (n : ℕ) : Prop :=
  ∃ K : ℕ, 2 ≤ K ∧ ∀ (A : RMat n), IsDS A →
    ∀ k : ℕ, K ≤ k → (A ^ k).permanent ≤ A.permanent

lemma isDS_nonneg {n : ℕ} {A : RMat n} (hA : IsDS A) (i j : Fin n) : 0 ≤ A i j := by
  exact nonneg_of_mem_doublyStochastic hA

lemma isDS_row_sum {n : ℕ} {A : RMat n} (hA : IsDS A) (i : Fin n) :
    ∑ j : Fin n, A i j = 1 := by
  exact sum_row_of_mem_doublyStochastic hA i

lemma isDS_col_sum {n : ℕ} {A : RMat n} (hA : IsDS A) (j : Fin n) :
    ∑ i : Fin n, A i j = 1 := by
  exact sum_col_of_mem_doublyStochastic hA j

lemma isDS_pow {n : ℕ} {A : RMat n} (hA : IsDS A) (k : ℕ) : IsDS (A ^ k) := by
  exact (doublyStochastic ℝ (Fin n)).pow_mem hA k

end Foregger
