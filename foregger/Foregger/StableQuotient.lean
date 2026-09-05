import Foregger.PlateauRouting
import Mathlib.Data.Fintype.Basic

namespace Foregger

/-- The generated support relation as an actual setoid. -/
def supportSetoid {n : ℕ} (A : RMat n) : Setoid (Fin n) where
  r := SupportEqv A
  iseqv := ⟨supportEqv_refl A,
    fun _ _ h => supportEqv_symm h,
    fun _ _ _ h₁ h₂ => supportEqv_trans h₁ h₂⟩

/-- Finite set of support classes. -/
abbrev SupportClass {n : ℕ} (A : RMat n) := Quotient (supportSetoid A)

noncomputable instance supportClassFintype {n : ℕ} (A : RMat n) : Fintype (SupportClass A) := by
  classical
  exact Quotient.fintype (supportSetoid A)

noncomputable instance supportClassDecidableEq {n : ℕ} (A : RMat n) :
    DecidableEq (SupportClass A) := by
  classical
  exact Quotient.decidableEq

/-- Canonical projection from coordinates to their support class. -/
def supportClassMk {n : ℕ} (A : RMat n) (i : Fin n) : SupportClass A :=
  Quotient.mk'' i

theorem supportClassMk_surjective {n : ℕ} (A : RMat n) :
    Function.Surjective (supportClassMk A) := by
  intro q
  induction q using Quotient.inductionOn' with
  | _ i => exact ⟨i, rfl⟩

@[simp] theorem supportClassMk_eq_iff {n : ℕ} (A : RMat n) (i j : Fin n) :
    supportClassMk A i = supportClassMk A j ↔ SupportEqv A i j := by
  exact Quotient.eq''

/-- Size of a finite support class. -/
def supportClassSize {n : ℕ} (A : RMat n) (c : SupportClass A) : ℕ :=
  (Finset.univ.filter fun i : Fin n => supportClassMk A i = c).card

theorem supportClassSize_pos {n : ℕ} (A : RMat n) (c : SupportClass A) :
    0 < supportClassSize A c := by
  obtain ⟨i, rfl⟩ := supportClassMk_surjective A c
  unfold supportClassSize
  exact Finset.card_pos.mpr ⟨i, by simp⟩

end Foregger
