import Foregger.BlockAlgebra
import Mathlib.GroupTheory.OrderOfElement

open scoped BigOperators Matrix
open Matrix Finset

namespace Foregger.BlockSystem

variable {n : ℕ} {β : Type*} [Fintype β] [DecidableEq β]

theorem size_perm_pow (B : BlockSystem n β) (k : ℕ) (a : β) :
    B.size ((B.perm ^ k) a) = B.size a := by
  induction k with
  | zero => simp
  | succ k ih =>
      rw [pow_succ]
      simp only [Equiv.mul_apply]
      rw [B.size_perm, ih]

/-- The block-uniform matrix associated with the `k`-fold block permutation.
At `k = 0` this is the averaging projection, rather than the identity matrix. -/
noncomputable def uniformPower (B : BlockSystem n β) (k : ℕ) : RMat n := fun i j =>
  if B.block j = (B.perm ^ k) (B.block i) then (B.size (B.block i) : ℝ)⁻¹ else 0

@[simp] theorem uniformPower_zero (B : BlockSystem n β) : B.uniformPower 0 = B.averaging := by
  classical
  ext i j
  simp [uniformPower, averaging]

@[simp] theorem uniformPower_one (B : BlockSystem n β) : B.uniformPower 1 = B.uniformTransition := by
  classical
  ext i j
  simp [uniformPower, uniformTransition]

theorem uniformPower_nonneg (B : BlockSystem n β) (k : ℕ) (i j : Fin n) :
    0 ≤ B.uniformPower k i j := by
  classical
  simp only [uniformPower]
  split <;> positivity

theorem uniformPower_row_sum (B : BlockSystem n β) (k : ℕ) (i : Fin n) :
    ∑ j : Fin n, B.uniformPower k i j = 1 := by
  classical
  have hs : B.size ((B.perm ^ k) (B.block i)) = B.size (B.block i) :=
    B.size_perm_pow k _
  simp [uniformPower, size] at hs ⊢
  rw [hs]
  field_simp [B.size_ne_zero (B.block i)]

theorem uniformPower_col_sum (B : BlockSystem n β) (k : ℕ) (j : Fin n) :
    ∑ i : Fin n, B.uniformPower k i j = 1 := by
  classical
  let p : Equiv.Perm β := B.perm ^ k
  let a : β := p.symm (B.block j)
  have ha : p a = B.block j := by simp [a]
  have hpSize : B.size (p a) = B.size a := by
    simpa [p] using B.size_perm_pow k a
  have hiff (i : Fin n) : B.block j = p (B.block i) ↔ B.block i = a := by
    constructor
    · intro h
      apply p.injective
      simpa [ha] using h.symm
    · intro h
      simpa [h, ha]
  simp only [uniformPower, p]
  simp_rw [show (B.block j = (B.perm ^ k) (B.block ·)) =
      (fun i : Fin n => B.block i = a) by funext i; exact propext (hiff i)]
  simp [size, p, a, hpSize, B.size_ne_zero]

theorem uniformPower_isDS (B : BlockSystem n β) (k : ℕ) : IsDS (B.uniformPower k) := by
  rw [IsDS, mem_doublyStochastic_iff]
  exact ⟨B.uniformPower_nonneg k, B.uniformPower_row_sum k, B.uniformPower_col_sum k⟩

theorem uniformPower_mul (B : BlockSystem n β) (a b : ℕ) :
    B.uniformPower a * B.uniformPower b = B.uniformPower (a + b) := by
  classical
  ext i j
  by_cases h : B.block j = (B.perm ^ (a + b)) (B.block i)
  · have hs : B.size ((B.perm ^ a) (B.block i)) = B.size (B.block i) :=
      B.size_perm_pow a _
    simp [Matrix.mul_apply, uniformPower, h, pow_add, size, hs, B.size_ne_zero]
  · have hk (x : Fin n) :
        ¬ (B.block x = (B.perm ^ a) (B.block i) ∧
            B.block j = (B.perm ^ b) (B.block x)) := by
      rintro ⟨hxi, hjx⟩
      apply h
      simpa [pow_add, hxi] using hjx
    simp [Matrix.mul_apply, uniformPower, h, hk]

theorem uniformTransition_pow_succ (B : BlockSystem n β) (k : ℕ) :
    B.uniformTransition ^ (k + 1) = B.uniformPower (k + 1) := by
  induction k with
  | zero => simp
  | succ k ih =>
      rw [pow_succ, ih]
      rw [← B.uniformPower_one]
      rw [B.uniformPower_mul]
      congr
      omega

theorem uniformTransition_pow_orderOf (B : BlockSystem n β) :
    B.uniformTransition ^ orderOf B.perm = B.averaging := by
  have ho : 0 < orderOf B.perm := orderOf_pos B.perm
  obtain ⟨k, hk⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt ho)
  subst hk
  rw [B.uniformTransition_pow_succ]
  ext i j
  simp [uniformPower, averaging, pow_orderOf_eq_one]

end Foregger.BlockSystem
