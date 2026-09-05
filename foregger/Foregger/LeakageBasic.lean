import Foregger.BlockStochastic

open scoped BigOperators Matrix
open Matrix Finset

namespace Foregger.BlockSystem

variable {n : ℕ} {β : Type*} [Fintype β] [DecidableEq β]

theorem leakage_nonneg (B : BlockSystem n β) {A : RMat n}
    (hA : ∀ i j, 0 ≤ A i j) : 0 ≤ B.leakage A := by
  classical
  unfold leakage
  apply Finset.sum_nonneg
  intro i hi
  apply Finset.sum_nonneg
  intro j hj
  split <;> simp_all

theorem leakage_isDS_nonneg (B : BlockSystem n β) {A : RMat n} (hA : IsDS A) :
    0 ≤ B.leakage A :=
  B.leakage_nonneg (fun i j => isDS_nonneg hA i j)

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
