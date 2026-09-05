import Foregger.StableProjection

open scoped BigOperators Matrix
open Matrix

namespace Foregger.BlockSystem

variable {n : ℕ} {β : Type*} [Fintype β] [DecidableEq β]

/-- The transient remainder also annihilates the uniform block transition on the right. -/
theorem transient_mul_uniformTransition_eq_zero (B : BlockSystem n β) {A : RMat n}
    (hA : IsDS A) (hroute : B.ObeysRouting A) :
    B.transient A * B.uniformTransition = 0 := by
  rw [← B.averaging_mul_uniformTransition]
  rw [← Matrix.mul_assoc, B.transient_mul_averaging_eq_zero hA hroute]
  simp

/-- And on the left. -/
theorem uniformTransition_mul_transient_eq_zero (B : BlockSystem n β) {A : RMat n}
    (hA : IsDS A) (hroute : B.ObeysRouting A) :
    B.uniformTransition * B.transient A = 0 := by
  rw [← B.uniformTransition_mul_averaging]
  rw [Matrix.mul_assoc, B.averaging_mul_transient_eq_zero hA hroute]
  simp

/-- Recover `A` as stable transition plus transient remainder. -/
theorem uniformTransition_add_transient (B : BlockSystem n β) (A : RMat n) :
    B.uniformTransition + B.transient A = A := by
  unfold transient
  abel

/-- A positive power of the stable-plus-transient decomposition has no mixed words, since both
cross products vanish. -/
theorem pow_succ_eq_uniform_add_transient (B : BlockSystem n β) {A : RMat n}
    (hA : IsDS A) (hroute : B.ObeysRouting A) :
    ∀ m : ℕ,
      A ^ (m + 1) = B.uniformTransition ^ (m + 1) + B.transient A ^ (m + 1) := by
  intro m
  induction m with
  | zero =>
      simp [B.uniformTransition_add_transient A]
  | succ m ih =>
      rw [pow_succ, ih]
      rw [← B.uniformTransition_add_transient A]
      rw [add_mul, mul_add, mul_add]
      rw [B.transient_mul_uniformTransition_eq_zero hA hroute,
        B.uniformTransition_mul_transient_eq_zero hA hroute]
      simp [pow_succ]
      ac_rfl

end Foregger.BlockSystem

namespace Foregger

/-- The stable quotient gives a canonical exact decomposition of every positive power into a
periodic block-uniform term and a transient term. -/
theorem stable_power_decomposition {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k))
    (m : ℕ) :
    A ^ (m + 1) =
      (stableBlockSystem hA hplateau).uniformTransition ^ (m + 1) +
      (stableBlockSystem hA hplateau).transient A ^ (m + 1) :=
  (stableBlockSystem hA hplateau).pow_succ_eq_uniform_add_transient
    hA (stableBlockSystem_obeysRouting hA hplateau) m

end Foregger
