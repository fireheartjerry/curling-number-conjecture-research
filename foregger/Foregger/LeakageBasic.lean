import Foregger.BlockStochastic

open scoped BigOperators Matrix
open Matrix Finset

namespace Foregger.BlockSystem

variable {n : ℕ} {β : Type*} [Fintype β] [DecidableEq β]

/-- Wrong-block mass in one row. -/
noncomputable def rowLeakage (B : BlockSystem n β) (A : RMat n) (i : Fin n) : ℝ :=
  ∑ j : Fin n, if B.block j = B.perm (B.block i) then 0 else A i j

@[simp] theorem leakage_eq_sum_rowLeakage (B : BlockSystem n β) (A : RMat n) :
    B.leakage A = ∑ i : Fin n, B.rowLeakage A i := by
  rfl

theorem rowLeakage_nonneg (B : BlockSystem n β) {A : RMat n}
    (hA : ∀ i j, 0 ≤ A i j) (i : Fin n) : 0 ≤ B.rowLeakage A i := by
  classical
  unfold rowLeakage
  apply Finset.sum_nonneg
  intro j hj
  split <;> simp_all

theorem leakage_nonneg (B : BlockSystem n β) {A : RMat n}
    (hA : ∀ i j, 0 ≤ A i j) : 0 ≤ B.leakage A := by
  rw [B.leakage_eq_sum_rowLeakage]
  exact Finset.sum_nonneg fun i _ => B.rowLeakage_nonneg hA i

theorem leakage_isDS_nonneg (B : BlockSystem n β) {A : RMat n} (hA : IsDS A) :
    0 ≤ B.leakage A :=
  B.leakage_nonneg (fun i j => isDS_nonneg hA i j)

theorem rowLeakage_le_leakage (B : BlockSystem n β) {A : RMat n}
    (hA : ∀ i j, 0 ≤ A i j) (i : Fin n) : B.rowLeakage A i ≤ B.leakage A := by
  rw [B.leakage_eq_sum_rowLeakage]
  exact Finset.single_le_sum (fun j _ => B.rowLeakage_nonneg hA j) (Finset.mem_univ i)

theorem rowLeakage_isDS_le_one (B : BlockSystem n β) {A : RMat n}
    (hA : IsDS A) (i : Fin n) : B.rowLeakage A i ≤ 1 := by
  classical
  calc
    B.rowLeakage A i ≤ ∑ j : Fin n, A i j := by
      unfold rowLeakage
      gcongr with j
      split <;> simp [isDS_nonneg hA i j]
    _ = 1 := isDS_row_sum hA i

theorem leakage_isDS_le_card (B : BlockSystem n β) {A : RMat n} (hA : IsDS A) :
    B.leakage A ≤ n := by
  rw [B.leakage_eq_sum_rowLeakage]
  calc
    (∑ i : Fin n, B.rowLeakage A i) ≤ ∑ _i : Fin n, (1 : ℝ) := by
      gcongr with i
      exact B.rowLeakage_isDS_le_one hA i
    _ = n := by simp

theorem leakage_uniformTransition (B : BlockSystem n β) :
    B.leakage B.uniformTransition = 0 := by
  classical
  simp [leakage, uniformTransition]

theorem uniformTransition_pos_iff (B : BlockSystem n β) (i j : Fin n) :
    0 < B.uniformTransition i j ↔ B.block j = B.perm (B.block i) := by
  classical
  simp only [uniformTransition]
  split_ifs with h
  · simp [h, B.size_pos]
  · simp [h]

end Foregger.BlockSystem
