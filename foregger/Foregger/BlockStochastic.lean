import Foregger.Blocks

open scoped BigOperators Matrix
open Matrix Finset

namespace Foregger.BlockSystem

variable {n : ℕ} {β : Type*} [Fintype β] [DecidableEq β]

private theorem sum_indicator_inv_card {α : Type*} [Fintype α]
    (p : α → Prop) [DecidablePred p]
    (hpos : 0 < (Finset.univ.filter p).card) :
    (∑ x : α, if p x then (((Finset.univ.filter p).card : ℝ)⁻¹) else 0) = 1 := by
  rw [← Finset.sum_filter]
  simp [hpos.ne']

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
  have hpos : 0 < (Finset.univ.filter fun j : Fin n => B.block j = B.block i).card := by
    simpa [size] using B.size_pos (B.block i)
  simpa [averaging, size] using
    (sum_indicator_inv_card (p := fun j : Fin n => B.block j = B.block i) hpos)

theorem averaging_col_sum (B : BlockSystem n β) (j : Fin n) :
    ∑ i : Fin n, B.averaging i j = 1 := by
  classical
  have hpos : 0 < (Finset.univ.filter fun i : Fin n => B.block i = B.block j).card := by
    simpa [size] using B.size_pos (B.block j)
  calc
    (∑ i : Fin n, B.averaging i j) =
        ∑ i : Fin n, if B.block i = B.block j then (B.size (B.block j) : ℝ)⁻¹ else 0 := by
      apply Finset.sum_congr rfl
      intro i hi
      rw [averaging]
      by_cases h : B.block i = B.block j
      · have h' : B.block j = B.block i := h.symm
        simp only [if_pos h, if_pos h']
        rw [h]
      · have h' : B.block j ≠ B.block i := fun e => h e.symm
        simp only [if_neg h, if_neg h']
    _ = 1 := by
      simpa [size] using
        (sum_indicator_inv_card (p := fun i : Fin n => B.block i = B.block j) hpos)

theorem averaging_isDS (B : BlockSystem n β) : IsDS B.averaging := by
  rw [IsDS, mem_doublyStochastic_iff_sum]
  exact ⟨B.averaging_nonneg, B.averaging_row_sum, B.averaging_col_sum⟩

theorem uniformTransition_row_sum (B : BlockSystem n β) (i : Fin n) :
    ∑ j : Fin n, B.uniformTransition i j = 1 := by
  classical
  have hpos :
      0 < (Finset.univ.filter fun j : Fin n => B.block j = B.perm (B.block i)).card := by
    simpa [size] using B.size_pos (B.perm (B.block i))
  have hcard :
      (Finset.univ.filter fun j : Fin n => B.block j = B.perm (B.block i)).card =
        B.size (B.block i) := by
    simpa [size] using B.size_perm (B.block i)
  have h := sum_indicator_inv_card
    (p := fun j : Fin n => B.block j = B.perm (B.block i)) hpos
  rw [hcard] at h
  simpa only [uniformTransition] using h

theorem uniformTransition_col_sum (B : BlockSystem n β) (j : Fin n) :
    ∑ i : Fin n, B.uniformTransition i j = 1 := by
  classical
  let a : β := B.perm.symm (B.block j)
  have ha : B.perm a = B.block j := by simp [a]
  have hpos : 0 < (Finset.univ.filter fun i : Fin n => B.block i = a).card := by
    simpa [size] using B.size_pos a
  calc
    (∑ i : Fin n, B.uniformTransition i j) =
        ∑ i : Fin n, if B.block i = a then (B.size a : ℝ)⁻¹ else 0 := by
      apply Finset.sum_congr rfl
      intro i hi
      rw [uniformTransition]
      by_cases h : B.block i = a
      · have ht : B.block j = B.perm (B.block i) := by simpa [h, ha]
        simp only [if_pos ht, if_pos h]
        rw [h]
      · have ht : B.block j ≠ B.perm (B.block i) := by
          intro e
          apply h
          apply B.perm.injective
          simpa [ha] using e.symm
        simp only [if_neg ht, if_neg h]
    _ = 1 := by
      simpa [size] using
        (sum_indicator_inv_card (p := fun i : Fin n => B.block i = a) hpos)

theorem uniformTransition_isDS (B : BlockSystem n β) : IsDS B.uniformTransition := by
  rw [IsDS, mem_doublyStochastic_iff_sum]
  exact ⟨B.uniformTransition_nonneg, B.uniformTransition_row_sum,
    B.uniformTransition_col_sum⟩

end Foregger.BlockSystem
