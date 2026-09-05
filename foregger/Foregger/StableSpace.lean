import Foregger.SupportRelation
import Mathlib.LinearAlgebra.FiniteDimensional.Basic

open scoped BigOperators Matrix
open Matrix Finset

namespace Foregger

/-- Vectors constant on every generated positive-support class. -/
def supportConstSubmodule {n : ℕ} (A : RMat n) : Submodule ℝ (Fin n → ℝ) where
  carrier := {x | ∀ ⦃i j : Fin n⦄, SupportEqv A i j → x i = x j}
  zero_mem' := by
    intro i j hij
    rfl
  add_mem' := by
    intro x y hx hy i j hij
    simp only [Pi.add_apply]
    rw [hx hij, hy hij]
  smul_mem' := by
    intro c x hx i j hij
    simp only [Pi.smul_apply, smul_eq_mul]
    rw [hx hij]

@[simp] theorem mem_supportConstSubmodule {n : ℕ} {A : RMat n} {x : Fin n → ℝ} :
    x ∈ supportConstSubmodule A ↔
      ∀ ⦃i j : Fin n⦄, SupportEqv A i j → x i = x j :=
  Iff.rfl

private theorem exists_pos_in_row {n : ℕ} {A : RMat n} (hA : IsDS A) (i : Fin n) :
    ∃ j : Fin n, 0 < A i j := by
  by_contra h
  push_neg at h
  have hz : ∀ j : Fin n, A i j = 0 := by
    intro j
    exact le_antisymm (h j) (isDS_nonneg hA i j)
  have hs := isDS_row_sum hA i
  have : (0 : ℝ) = 1 := by simpa [hz] using hs
  norm_num at this

/-- On a support-constant vector, each stochastic row literally evaluates to the common value on
its positive support. -/
theorem row_mean_eq_of_mem_supportConst {n : ℕ} {A : RMat n} (hA : IsDS A)
    {x : Fin n → ℝ} (hx : x ∈ supportConstSubmodule A) (r : Fin n)
    {j₀ : Fin n} (hj₀ : 0 < A r j₀) :
    ∑ j, A r j * x j = x j₀ := by
  classical
  calc
    (∑ j, A r j * x j) = ∑ j, A r j * x j₀ := by
      apply Finset.sum_congr rfl
      intro j hj
      by_cases hp : 0 < A r j
      · have hrel : SupportEqv A j j₀ :=
          Relation.EqvGen.rel _ _ ⟨r, hp, hj₀⟩
        rw [(mem_supportConstSubmodule.mp hx) hrel]
      · have hz : A r j = 0 :=
          le_antisymm (not_lt.mp hp) (isDS_nonneg hA r j)
        simp [hz]
    _ = x j₀ := by
      rw [← Finset.sum_mul, isDS_row_sum hA r]
      simp

/-- The corresponding weighted second moment is the square of that same common value. -/
theorem row_second_eq_of_mem_supportConst {n : ℕ} {A : RMat n} (hA : IsDS A)
    {x : Fin n → ℝ} (hx : x ∈ supportConstSubmodule A) (r : Fin n)
    {j₀ : Fin n} (hj₀ : 0 < A r j₀) :
    ∑ j, A r j * x j ^ 2 = x j₀ ^ 2 := by
  classical
  calc
    (∑ j, A r j * x j ^ 2) = ∑ j, A r j * x j₀ ^ 2 := by
      apply Finset.sum_congr rfl
      intro j hj
      by_cases hp : 0 < A r j
      · have hrel : SupportEqv A j j₀ :=
          Relation.EqvGen.rel _ _ ⟨r, hp, hj₀⟩
        rw [(mem_supportConstSubmodule.mp hx) hrel]
      · have hz : A r j = 0 :=
          le_antisymm (not_lt.mp hp) (isDS_nonneg hA r j)
        simp [hz]
    _ = x j₀ ^ 2 := by
      rw [← Finset.sum_mul, isDS_row_sum hA r]
      simp

/-- Every support-constant vector attains equality in every rowwise square inequality. -/
theorem row_sq_eq_of_mem_supportConst {n : ℕ} {A : RMat n} (hA : IsDS A)
    {x : Fin n → ℝ} (hx : x ∈ supportConstSubmodule A) (r : Fin n) :
    (A *ᵥ x) r ^ 2 = ∑ j, A r j * x j ^ 2 := by
  obtain ⟨j₀, hj₀⟩ := exists_pos_in_row hA r
  rw [Matrix.mulVec_apply_eq_sum,
    row_mean_eq_of_mem_supportConst hA hx r hj₀,
    row_second_eq_of_mem_supportConst hA hx r hj₀]

/-- Support-constant vectors are precisely norm-preserving vectors for a doubly stochastic
matrix.  This gives a genuine linear subspace model for the equality locus. -/
theorem sqMass_eq_of_mem_supportConst {n : ℕ} {A : RMat n} (hA : IsDS A)
    {x : Fin n → ℝ} (hx : x ∈ supportConstSubmodule A) :
    sqMass (A *ᵥ x) = sqMass x := by
  unfold sqMass
  calc
    (∑ r, (A *ᵥ x) r ^ 2) = ∑ r, ∑ j, A r j * x j ^ 2 := by
      apply Finset.sum_congr rfl
      intro r hr
      exact row_sq_eq_of_mem_supportConst hA hx r
    _ = sqMass x := isDS_sum_weighted_sq hA x

/-- Exact characterization of the global equality locus. -/
theorem sqMass_mulVec_eq_iff_mem_supportConst {n : ℕ} {A : RMat n} (hA : IsDS A)
    (x : Fin n → ℝ) :
    sqMass (A *ᵥ x) = sqMass x ↔ x ∈ supportConstSubmodule A := by
  constructor
  · intro heq
    rw [mem_supportConstSubmodule]
    intro i j hij
    exact eq_of_supportEqv_of_sqMass_eq hA x heq hij
  · intro hx
    exact sqMass_eq_of_mem_supportConst hA hx

/-- The norm-preserving subspaces of successive powers form a descending chain. -/
theorem supportConst_pow_succ_le {n : ℕ} {A : RMat n} (hA : IsDS A) (k : ℕ) :
    supportConstSubmodule (A ^ (k + 1)) ≤ supportConstSubmodule (A ^ k) := by
  intro x hx
  rw [mem_supportConstSubmodule] at hx ⊢
  intro i j hij
  exact hx (supportEqv_pow_mono hA k hij)

end Foregger
