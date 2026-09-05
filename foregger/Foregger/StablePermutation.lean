import Foregger.StableQuotient
import Mathlib.Data.Fintype.Card

open scoped BigOperators Matrix
open Matrix Finset

namespace Foregger

/-- A deterministic positive target chosen in each row. -/
noncomputable def rowTargetIndex {n : ℕ} {A : RMat n} (hA : IsDS A) (r : Fin n) : Fin n :=
  Classical.choose (exists_pos_in_row_isDS hA r)

theorem rowTargetIndex_pos {n : ℕ} {A : RMat n} (hA : IsDS A) (r : Fin n) :
    0 < A r (rowTargetIndex hA r) :=
  Classical.choose_spec (exists_pos_in_row_isDS hA r)

/-- The deterministic row routing descends to the quotient of stable support classes. -/
noncomputable def stableClassMap {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k)) :
    SupportClass (A ^ k) → SupportClass (A ^ k) := fun c =>
  Quotient.liftOn' c
    (fun r => supportClassMk (A ^ k) (rowTargetIndex hA r))
    (by
      intro r s hrs
      apply (supportClassMk_eq_iff (A ^ k) _ _).2
      exact stable_equiv_rows_target_same_class hA hplateau hrs
        (rowTargetIndex_pos hA r) (rowTargetIndex_pos hA s))

@[simp] theorem stableClassMap_mk {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k))
    (r : Fin n) :
    stableClassMap hA hplateau (supportClassMk (A ^ k) r) =
      supportClassMk (A ^ k) (rowTargetIndex hA r) :=
  rfl

/-- Every positive entry of `A` lands in the class selected by the stable class map. -/
theorem positive_entry_target_class {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k))
    {r j : Fin n} (hrj : 0 < A r j) :
    stableClassMap hA hplateau (supportClassMk (A ^ k) r) =
      supportClassMk (A ^ k) j := by
  rw [stableClassMap_mk]
  apply (supportClassMk_eq_iff (A ^ k) _ _).2
  exact positive_cols_same_stable_class hA hplateau (rowTargetIndex_pos hA r) hrj

/-- Column stochasticity makes the stable class map surjective: every class contains a column,
and that column has positive incoming mass from some row class. -/
theorem stableClassMap_surjective {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k)) :
    Function.Surjective (stableClassMap hA hplateau) := by
  intro c
  induction c using Quotient.inductionOn' with
  | _ j =>
      obtain ⟨r, hrj⟩ := exists_pos_in_col hA j
      refine ⟨supportClassMk (A ^ k) r, ?_⟩
      exact positive_entry_target_class hA hplateau hrj

/-- On the finite stable quotient, deterministic routing is therefore a permutation. -/
noncomputable def stableClassPerm {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k)) :
    Equiv.Perm (SupportClass (A ^ k)) :=
  Equiv.ofBijective (stableClassMap hA hplateau)
    ⟨Finite.injective_iff_surjective.mpr (stableClassMap_surjective hA hplateau),
      stableClassMap_surjective hA hplateau⟩

@[simp] theorem stableClassPerm_apply {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k))
    (c : SupportClass (A ^ k)) :
    stableClassPerm hA hplateau c = stableClassMap hA hplateau c :=
  rfl

/-- The indicator of the target class is sent exactly to the indicator of its predecessor class. -/
theorem mulVec_target_indicator {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k))
    (c : SupportClass (A ^ k)) :
    A *ᵥ supportClassIndicator (A ^ k) (stableClassPerm hA hplateau c) =
      supportClassIndicator (A ^ k) c := by
  funext r
  let x := supportClassIndicator (A ^ k) (stableClassPerm hA hplateau c)
  have hxk : x ∈ supportConstSubmodule (A ^ k) :=
    supportClassIndicator_mem (A ^ k) (stableClassPerm hA hplateau c)
  have hxk1 : x ∈ supportConstSubmodule (A ^ (k + 1)) := by
    rw [hplateau]
    exact hxk
  have hfirst : sqMass (A *ᵥ x) = sqMass x :=
    first_step_sqMass_eq_of_mem_pow_succ hA k hxk1
  have hxA : x ∈ supportConstSubmodule A :=
    (sqMass_mulVec_eq_iff_mem_supportConst hA x).mp hfirst
  have hrow : (A *ᵥ x) r = x (rowTargetIndex hA r) := by
    simpa only [Matrix.mulVec_apply_eq_sum] using
      row_mean_eq_of_mem_supportConst hA hxA r (rowTargetIndex_pos hA r)
  have hroute :
      supportClassMk (A ^ k) (rowTargetIndex hA r) =
        stableClassPerm hA hplateau (supportClassMk (A ^ k) r) := by
    rw [stableClassPerm_apply, stableClassMap_mk]
  rw [hrow]
  simp only [x, supportClassIndicator]
  rw [hroute]
  simp

/-- Norm preservation of class indicators proves that the stable permutation preserves the exact
cardinality of every block. -/
theorem stableClassPerm_size {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k))
    (c : SupportClass (A ^ k)) :
    supportClassSize (A ^ k) (stableClassPerm hA hplateau c) =
      supportClassSize (A ^ k) c := by
  let x := supportClassIndicator (A ^ k) (stableClassPerm hA hplateau c)
  have hxk : x ∈ supportConstSubmodule (A ^ k) :=
    supportClassIndicator_mem (A ^ k) (stableClassPerm hA hplateau c)
  have hxk1 : x ∈ supportConstSubmodule (A ^ (k + 1)) := by
    rw [hplateau]
    exact hxk
  have hfirst : sqMass (A *ᵥ x) = sqMass x :=
    first_step_sqMass_eq_of_mem_pow_succ hA k hxk1
  have hmap := mulVec_target_indicator hA hplateau c
  have hreal :
      (supportClassSize (A ^ k) c : ℝ) =
        supportClassSize (A ^ k) (stableClassPerm hA hplateau c) := by
    calc
      (supportClassSize (A ^ k) c : ℝ) =
          sqMass (supportClassIndicator (A ^ k) c) :=
        (sqMass_supportClassIndicator (A ^ k) c).symm
      _ = sqMass (A *ᵥ x) := by simpa [x, hmap]
      _ = sqMass x := hfirst
      _ = (supportClassSize (A ^ k) (stableClassPerm hA hplateau c) : ℝ) :=
        sqMass_supportClassIndicator (A ^ k) (stableClassPerm hA hplateau c)
  exact_mod_cast hreal.symm

end Foregger
