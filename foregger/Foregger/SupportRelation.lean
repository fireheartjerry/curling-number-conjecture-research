import Foregger.DSEquality
import Mathlib.Logic.Relation

open scoped BigOperators Matrix
open Matrix Finset

namespace Foregger

/-- Two input coordinates are directly linked when some row puts positive mass on both. -/
def CommonRowSupport {n : ℕ} (A : RMat n) (i j : Fin n) : Prop :=
  ∃ r : Fin n, 0 < A r i ∧ 0 < A r j

/-- The equivalence closure of common positive row support.  Norm-preserving vectors are constant
on these classes. -/
def SupportEqv {n : ℕ} (A : RMat n) : Fin n → Fin n → Prop :=
  Relation.EqvGen (CommonRowSupport A)

theorem supportEqv_refl {n : ℕ} (A : RMat n) (i : Fin n) : SupportEqv A i i :=
  Relation.EqvGen.refl _

theorem supportEqv_symm {n : ℕ} {A : RMat n} {i j : Fin n}
    (h : SupportEqv A i j) : SupportEqv A j i :=
  Relation.EqvGen.symm h

theorem supportEqv_trans {n : ℕ} {A : RMat n} {i j k : Fin n}
    (hij : SupportEqv A i j) (hjk : SupportEqv A j k) : SupportEqv A i k :=
  Relation.EqvGen.trans hij hjk

/-- Global norm equality propagates along the whole support equivalence closure. -/
theorem eq_of_supportEqv_of_sqMass_eq {n : ℕ} {A : RMat n} (hA : IsDS A)
    (x : Fin n → ℝ) (heq : sqMass (A *ᵥ x) = sqMass x)
    {i j : Fin n} (hij : SupportEqv A i j) : x i = x j := by
  induction hij with
  | rel a b hab =>
      rcases hab with ⟨r, har, hbr⟩
      exact eq_of_common_positive_row_of_sqMass_eq hA x heq har hbr
  | refl a => rfl
  | symm a b hab ih => exact ih.symm
  | trans a b c hab hbc ihab ihbc => exact ihab.trans ihbc

/-- Every column of a doubly stochastic matrix contains a positive entry. -/
theorem exists_pos_in_col {n : ℕ} {A : RMat n} (hA : IsDS A) (j : Fin n) :
    ∃ i : Fin n, 0 < A i j := by
  by_contra h
  push_neg at h
  have hz : ∀ i : Fin n, A i j = 0 := by
    intro i
    exact le_antisymm (h i) (isDS_nonneg hA i j)
  have hs := isDS_col_sum hA j
  have : (0 : ℝ) = 1 := by simpa [hz] using hs
  norm_num at this

/-- A positive summand makes an entry of a product positive when both factors are nonnegative. -/
theorem mul_apply_pos_of_pos {n : ℕ} {A B : RMat n}
    (hA0 : ∀ i j, 0 ≤ A i j) (hB0 : ∀ i j, 0 ≤ B i j)
    {s r i : Fin n} (hAr : 0 < A s r) (hBi : 0 < B r i) :
    0 < (A * B) s i := by
  classical
  rw [Matrix.mul_apply]
  refine Finset.sum_pos' (fun k _ => mul_nonneg (hA0 s k) (hB0 k i)) ?_
  exact ⟨r, Finset.mem_univ r, mul_pos hAr hBi⟩

/-- Left multiplication by a doubly stochastic matrix cannot split an existing common-support
connection. -/
theorem commonRowSupport_mul_left {n : ℕ} {A B : RMat n}
    (hA : IsDS A) (hB : IsDS B) {i j : Fin n}
    (hij : CommonRowSupport B i j) : CommonRowSupport (A * B) i j := by
  rcases hij with ⟨r, hri, hrj⟩
  obtain ⟨s, hsr⟩ := exists_pos_in_col hA r
  refine ⟨s, ?_, ?_⟩
  · exact mul_apply_pos_of_pos
      (fun a b => isDS_nonneg hA a b) (fun a b => isDS_nonneg hB a b) hsr hri
  · exact mul_apply_pos_of_pos
      (fun a b => isDS_nonneg hA a b) (fun a b => isDS_nonneg hB a b) hsr hrj

/-- Consequently the generated support equivalence only coarsens under left stochastic
multiplication. -/
theorem supportEqv_mul_left {n : ℕ} {A B : RMat n}
    (hA : IsDS A) (hB : IsDS B) {i j : Fin n}
    (hij : SupportEqv B i j) : SupportEqv (A * B) i j := by
  induction hij with
  | rel a b hab =>
      exact Relation.EqvGen.rel _ _ (commonRowSupport_mul_left hA hB hab)
  | refl a => exact Relation.EqvGen.refl _
  | symm a b hab ih => exact Relation.EqvGen.symm ih
  | trans a b c hab hbc ihab ihbc => exact Relation.EqvGen.trans ihab ihbc

/-- The support equivalence of successive powers is monotone: classes can merge, never split. -/
theorem supportEqv_pow_mono {n : ℕ} {A : RMat n} (hA : IsDS A) (k : ℕ)
    {i j : Fin n} (hij : SupportEqv (A ^ k) i j) :
    SupportEqv (A ^ (k + 1)) i j := by
  have h := supportEqv_mul_left hA (isDS_pow hA k) hij
  simpa only [pow_succ'] using h

end Foregger
