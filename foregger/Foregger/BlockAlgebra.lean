import Foregger.BlockStochastic

open scoped BigOperators Matrix
open Matrix Finset

namespace Foregger.BlockSystem

variable {n : ℕ} {β : Type*} [Fintype β] [DecidableEq β]

theorem averaging_transpose (B : BlockSystem n β) : B.averaging.transpose = B.averaging := by
  classical
  ext i j
  by_cases h : B.block j = B.block i
  · simp [averaging, h, h.symm]
  · have h' : B.block i ≠ B.block j := fun e => h e.symm
    simp [averaging, h, h']

theorem averaging_mul_self (B : BlockSystem n β) : B.averaging * B.averaging = B.averaging := by
  classical
  ext i j
  by_cases h : B.block j = B.block i
  · simp [Matrix.mul_apply, averaging, h, size, B.size_ne_zero]
  · have hk (k : Fin n) :
        ¬ (B.block k = B.block i ∧ B.block j = B.block k) := by
      rintro ⟨hki, hjk⟩
      exact h (hjk.trans hki)
    simp [Matrix.mul_apply, averaging, h, hk]

theorem uniformTransition_mul_averaging (B : BlockSystem n β) :
    B.uniformTransition * B.averaging = B.uniformTransition := by
  classical
  ext i j
  by_cases h : B.block j = B.perm (B.block i)
  · have hs := B.size_perm (B.block i)
    simp [Matrix.mul_apply, uniformTransition, averaging, h, size, hs,
      B.size_ne_zero]
  · have hk (k : Fin n) :
        ¬ (B.block k = B.perm (B.block i) ∧ B.block j = B.block k) := by
      rintro ⟨hki, hjk⟩
      exact h (hjk.trans hki)
    simp [Matrix.mul_apply, uniformTransition, averaging, h, hk]

theorem averaging_mul_uniformTransition (B : BlockSystem n β) :
    B.averaging * B.uniformTransition = B.uniformTransition := by
  classical
  ext i j
  by_cases h : B.block j = B.perm (B.block i)
  · simp [Matrix.mul_apply, averaging, uniformTransition, h, size,
      B.size_ne_zero]
  · have hk (k : Fin n) :
        ¬ (B.block k = B.block i ∧ B.block j = B.perm (B.block k)) := by
      rintro ⟨hki, hjk⟩
      exact h (hjk.trans (congrArg B.perm hki))
    simp [Matrix.mul_apply, averaging, uniformTransition, h, hk]

end Foregger.BlockSystem
