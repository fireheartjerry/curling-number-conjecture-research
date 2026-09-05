import Foregger.RelationRecovery
import Foregger.Stabilization

open scoped BigOperators Matrix
open Matrix Finset

namespace Foregger

/-- Every row of a doubly stochastic matrix has a positive entry. -/
theorem exists_pos_in_row_isDS {n : ℕ} {A : RMat n} (hA : IsDS A) (i : Fin n) :
    ∃ j : Fin n, 0 < A i j := by
  by_contra h
  push_neg at h
  have hz : ∀ j : Fin n, A i j = 0 := by
    intro j
    exact le_antisymm (h j) (isDS_nonneg hA i j)
  have hs := isDS_row_sum hA i
  have : (0 : ℝ) = 1 := by simpa [hz] using hs
  norm_num at this

/-- At a plateau `U_{k+1}=U_k`, every two positive columns in a row of `A` belong to the same
support class of `A^k`.  Thus each row routes all of its mass into one stable class. -/
theorem positive_cols_same_stable_class {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k))
    {r i j : Fin n} (hi : 0 < A r i) (hj : 0 < A r j) :
    SupportEqv (A ^ k) i j := by
  rw [supportEqv_iff_forall_const_eq]
  intro x hx
  have hx' : x ∈ supportConstSubmodule (A ^ (k + 1)) := by
    rw [hplateau]
    exact hx
  have hfirst : sqMass (A *ᵥ x) = sqMass x :=
    first_step_sqMass_eq_of_mem_pow_succ hA k hx'
  exact eq_of_common_positive_row_of_sqMass_eq hA x hfirst hi hj

/-- Under the same plateau, two rows that lie in one stable class must route to the same stable
class.  This is the finite deterministic block map promised by the hand proof. -/
theorem stable_equiv_rows_target_same_class {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k))
    {r s i j : Fin n} (hrs : SupportEqv (A ^ k) r s)
    (hri : 0 < A r i) (hsj : 0 < A s j) :
    SupportEqv (A ^ k) i j := by
  rw [supportEqv_iff_forall_const_eq]
  intro x hx
  have hx' : x ∈ supportConstSubmodule (A ^ (k + 1)) := by
    rw [hplateau]
    exact hx
  have hfirst : sqMass (A *ᵥ x) = sqMass x :=
    first_step_sqMass_eq_of_mem_pow_succ hA k hx'
  have hxA : x ∈ supportConstSubmodule A :=
    (sqMass_mulVec_eq_iff_mem_supportConst hA x).mp hfirst
  have hAx : A *ᵥ x ∈ supportConstSubmodule (A ^ k) :=
    mulVec_mem_supportConst_pow hA k hx'
  have hout : (A *ᵥ x) r = (A *ᵥ x) s :=
    (mem_supportConstSubmodule.mp hAx) hrs
  have hri' : (A *ᵥ x) r = x i := by
    simpa only [Matrix.mulVec_apply_eq_sum] using
      row_mean_eq_of_mem_supportConst hA hxA r hri
  have hsj' : (A *ᵥ x) s = x j := by
    simpa only [Matrix.mulVec_apply_eq_sum] using
      row_mean_eq_of_mem_supportConst hA hxA s hsj
  linarith

/-- Each row has a well-defined stable target class: any two positive witnesses are equivalent. -/
theorem stable_target_class_well_defined {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k))
    (r : Fin n) :
    ∃ i : Fin n, 0 < A r i ∧
      ∀ j : Fin n, 0 < A r j → SupportEqv (A ^ k) i j := by
  obtain ⟨i, hi⟩ := exists_pos_in_row_isDS hA r
  refine ⟨i, hi, ?_⟩
  intro j hj
  exact positive_cols_same_stable_class hA hplateau hi hj

end Foregger
