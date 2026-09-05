import Foregger.BlockAlgebra

open scoped BigOperators Matrix
open Matrix Finset

namespace Foregger.BlockSystem

variable {n : ℕ} {β : Type*} [Fintype β] [DecidableEq β]

/-- A matrix obeys the deterministic routing encoded by a block system when every entry outside
its designated target block is zero. -/
def ObeysRouting (B : BlockSystem n β) (A : RMat n) : Prop :=
  ∀ i j, B.block j ≠ B.perm (B.block i) → A i j = 0

theorem row_target_mass_eq_one (B : BlockSystem n β) {A : RMat n}
    (hA : IsDS A) (hroute : B.ObeysRouting A) (i : Fin n) :
    (∑ j, if B.block j = B.perm (B.block i) then A i j else 0) = 1 := by
  calc
    (∑ j, if B.block j = B.perm (B.block i) then A i j else 0) = ∑ j, A i j := by
      apply Finset.sum_congr rfl
      intro j hj
      by_cases h : B.block j = B.perm (B.block i)
      · simp [h]
      · simp [h, hroute i j h]
    _ = 1 := isDS_row_sum hA i

theorem col_predecessor_mass_eq_one (B : BlockSystem n β) {A : RMat n}
    (hA : IsDS A) (hroute : B.ObeysRouting A) {i j : Fin n}
    (hij : B.block j = B.perm (B.block i)) :
    (∑ x, if B.block x = B.block i then A x j else 0) = 1 := by
  calc
    (∑ x, if B.block x = B.block i then A x j else 0) = ∑ x, A x j := by
      apply Finset.sum_congr rfl
      intro x hx
      by_cases h : B.block x = B.block i
      · simp [h]
      · have hout : B.block j ≠ B.perm (B.block x) := by
          intro e
          apply h
          apply B.perm.injective
          rw [← hij, ← e]
        simp [h, hroute x j hout]
    _ = 1 := isDS_col_sum hA j

/-- Right block averaging turns any routed doubly stochastic matrix into the canonical uniform
transition. -/
theorem mul_averaging_eq_uniformTransition (B : BlockSystem n β) {A : RMat n}
    (hA : IsDS A) (hroute : B.ObeysRouting A) :
    A * B.averaging = B.uniformTransition := by
  classical
  ext i j
  rw [Matrix.mul_apply]
  by_cases htarget : B.block j = B.perm (B.block i)
  · have hs : B.size (B.block j) = B.size (B.block i) := by
      rw [htarget, B.size_perm]
    calc
      (∑ x, A i x * B.averaging x j) =
          (B.size (B.block i) : ℝ)⁻¹ *
            (∑ x, if B.block x = B.perm (B.block i) then A i x else 0) := by
        apply Finset.sum_congr rfl
        intro x hx
        by_cases hbx : B.block x = B.perm (B.block i)
        · have hjx : B.block j = B.block x := htarget.trans hbx.symm
          simp [averaging, hjx, hbx, hs, mul_comm, mul_left_comm, mul_assoc]
        · have hAx : A i x = 0 := hroute i x hbx
          simp [hAx]
      _ = (B.size (B.block i) : ℝ)⁻¹ := by rw [B.row_target_mass_eq_one hA hroute i, mul_one]
      _ = B.uniformTransition i j := by simp [uniformTransition, htarget]
  · have hzero (x : Fin n) : A i x * B.averaging x j = 0 := by
      by_cases hjx : B.block j = B.block x
      · have hbx : B.block x ≠ B.perm (B.block i) := by
          intro e
          exact htarget (hjx.trans e)
        rw [hroute i x hbx]
        simp
      · simp [averaging, hjx]
    simp [hzero, uniformTransition, htarget]

/-- Left block averaging gives the same canonical transition. -/
theorem averaging_mul_eq_uniformTransition (B : BlockSystem n β) {A : RMat n}
    (hA : IsDS A) (hroute : B.ObeysRouting A) :
    B.averaging * A = B.uniformTransition := by
  classical
  ext i j
  rw [Matrix.mul_apply]
  by_cases htarget : B.block j = B.perm (B.block i)
  · calc
      (∑ x, B.averaging i x * A x j) =
          (B.size (B.block i) : ℝ)⁻¹ *
            (∑ x, if B.block x = B.block i then A x j else 0) := by
        apply Finset.sum_congr rfl
        intro x hx
        by_cases hbx : B.block x = B.block i
        · have hix : B.block x = B.block i := hbx
          simp [averaging, hbx, hbx.symm, mul_comm, mul_left_comm, mul_assoc]
        · have hix : B.block i ≠ B.block x := fun e => hbx e.symm
          simp [averaging, hbx, hix]
      _ = (B.size (B.block i) : ℝ)⁻¹ := by
        rw [B.col_predecessor_mass_eq_one hA hroute htarget, mul_one]
      _ = B.uniformTransition i j := by simp [uniformTransition, htarget]
  · have hzero (x : Fin n) : B.averaging i x * A x j = 0 := by
      by_cases hbx : B.block x = B.block i
      · have hout : B.block j ≠ B.perm (B.block x) := by simpa [hbx] using htarget
        rw [hroute x j hout]
        simp
      · have hix : B.block i ≠ B.block x := fun e => hbx e.symm
        simp [averaging, hbx, hix]
    simp [hzero, uniformTransition, htarget]

/-- Transient remainder after removing the canonical block transition. -/
def transient (B : BlockSystem n β) (A : RMat n) : RMat n := A - B.uniformTransition

/-- The transient remainder annihilates block averages on the right. -/
theorem transient_mul_averaging_eq_zero (B : BlockSystem n β) {A : RMat n}
    (hA : IsDS A) (hroute : B.ObeysRouting A) :
    B.transient A * B.averaging = 0 := by
  rw [transient, sub_mul, B.mul_averaging_eq_uniformTransition hA hroute,
    B.uniformTransition_mul_averaging]
  simp

/-- The transient remainder annihilates block averages on the left. -/
theorem averaging_mul_transient_eq_zero (B : BlockSystem n β) {A : RMat n}
    (hA : IsDS A) (hroute : B.ObeysRouting A) :
    B.averaging * B.transient A = 0 := by
  rw [transient, mul_sub, B.averaging_mul_eq_uniformTransition hA hroute,
    B.averaging_mul_uniformTransition]
  simp

end Foregger.BlockSystem
