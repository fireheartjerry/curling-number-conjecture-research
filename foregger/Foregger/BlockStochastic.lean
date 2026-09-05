import Foregger.Blocks

open scoped BigOperators Matrix
open Matrix Finset

namespace Foregger.BlockSystem

variable {n : ℕ} {β : Type*} [Fintype β] [DecidableEq β]

private theorem inv_nonneg_nat (m : ℕ) : 0 ≤ ((m : ℝ)⁻¹) := by positivity

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

end Foregger.BlockSystem
