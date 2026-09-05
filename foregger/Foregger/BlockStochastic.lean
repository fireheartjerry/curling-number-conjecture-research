import Foregger.Blocks

open scoped BigOperators Matrix
open Matrix Finset

namespace Foregger.BlockSystem

variable {n : ℕ} {β : Type*} [Fintype β] [DecidableEq β]

theorem averaging_nonneg (B : BlockSystem n β) (i j : Fin n) :
    0 ≤ B.averaging i j := by
  classical
  simp only [averaging]
  split <;> positivity

theorem uniformTransition_nonneg (B : BlockSystem n β) (i j : Fin n) :
    0 ≤ B.uniformTransition i j := by
  classical
  simp only [uniformTransition]
  split <;> positivity

theorem averaging_row_sum (B : BlockSystem n β) (i : Fin n) :
    ∑ j : Fin n, B.averaging i j = 1 := by
  classical
  simp [averaging, size, B.size_ne_zero]

theorem averaging_col_sum (B : BlockSystem n β) (j : Fin n) :
    ∑ i : Fin n, B.averaging i j = 1 := by
  classical
  simp [averaging, size, eq_comm, B.size_ne_zero]

theorem averaging_isDS (B : BlockSystem n β) : IsDS B.averaging := by
  rw [IsDS, mem_doublyStochastic_iff]
  exact ⟨B.averaging_nonneg, B.averaging_row_sum, B.averaging_col_sum⟩

theorem uniformTransition_row_sum (B : BlockSystem n β) (i : Fin n) :
    ∑ j : Fin n, B.uniformTransition i j = 1 := by
  classical
  have hs : B.size (B.perm (B.block i)) = B.size (B.block i) := B.size_perm _
  simp [uniformTransition, size] at hs ⊢
  rw [hs]
  field_simp [B.size_ne_zero (B.block i)]

theorem uniformTransition_col_sum (B : BlockSystem n β) (j : Fin n) :
    ∑ i : Fin n, B.uniformTransition i j = 1 := by
  classical
  let a : β := B.perm.symm (B.block j)
  have ha : B.perm a = B.block j := by simp [a]
  have hs : B.size a = B.size (B.block j) := by
    rw [← ha, B.size_perm]
  have hiff (i : Fin n) : B.block j = B.perm (B.block i) ↔ B.block i = a := by
    constructor
    · intro h
      apply B.perm.injective
      simpa [ha] using h.symm
    · intro h
      simpa [h, ha]
  simp only [uniformTransition]
  simp_rw [if_congr (hiff _) rfl rfl]
  simp [a, size, hs, B.size_ne_zero]

theorem uniformTransition_isDS (B : BlockSystem n β) : IsDS B.uniformTransition := by
  rw [IsDS, mem_doublyStochastic_iff]
  exact ⟨B.uniformTransition_nonneg, B.uniformTransition_row_sum,
    B.uniformTransition_col_sum⟩

end Foregger.BlockSystem
