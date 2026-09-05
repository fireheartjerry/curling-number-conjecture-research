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

theorem uniformPower_mul (B : BlockSystem n β) (a b : ℕ) :
    B.uniformPower a * B.uniformPower b = B.uniformPower (a + b) := by
  classical
  ext i j
  by_cases h : B.block j = (B.perm ^ (a + b)) (B.block i)
  · have hs : B.size ((B.perm ^ a) (B.block i)) = B.size (B.block i) :=
      B.size_perm_pow a _
    simp [Matrix.mul_apply, uniformPower, h, pow_add, size, hs, B.size_ne_zero]
  · have hk (k : Fin n) :
        ¬ (B.block k = (B.perm ^ a) (B.block i) ∧
            B.block j = (B.perm ^ b) (B.block k)) := by
      rintro ⟨hki, hjk⟩
      apply h
      simpa [pow_add, hki] using hjk
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
