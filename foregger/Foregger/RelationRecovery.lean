import Foregger.StableSpace

open scoped BigOperators Matrix
open Matrix Finset

namespace Foregger

/-- An equivalence relation is completely determined by the subspace of functions constant on its
classes.  Specialized here to the support relation so the stable linear subspace recovers a finite
combinatorial partition. -/
theorem supportEqv_iff_forall_const_eq {n : ℕ} (A : RMat n) (i j : Fin n) :
    SupportEqv A i j ↔
      ∀ x : Fin n → ℝ, x ∈ supportConstSubmodule A → x i = x j := by
  constructor
  · intro hij x hx
    exact (mem_supportConstSubmodule.mp hx) hij
  · intro h
    classical
    let x : Fin n → ℝ := fun t => if SupportEqv A i t then 1 else 0
    have hx : x ∈ supportConstSubmodule A := by
      rw [mem_supportConstSubmodule]
      intro a b hab
      have hiff : SupportEqv A i a ↔ SupportEqv A i b := by
        constructor
        · intro hia
          exact supportEqv_trans hia hab
        · intro hib
          exact supportEqv_trans hib (supportEqv_symm hab)
      simp only [x]
      by_cases hia : SupportEqv A i a
      · have hib := hiff.mp hia
        simp [hia, hib]
      · have hib : ¬ SupportEqv A i b := by
          intro hib
          exact hia (hiff.mpr hib)
        simp [hia, hib]
    have hijx := h x hx
    have hii : SupportEqv A i i := supportEqv_refl A i
    simp only [x, if_pos hii] at hijx
    by_contra hn
    simp only [x, if_neg hn] at hijx
    norm_num at hijx

/-- Equality of the constant-function subspaces forces equality of the generated support
relations, pointwise. -/
theorem supportEqv_iff_of_supportConst_eq {n : ℕ} {A B : RMat n}
    (hsub : supportConstSubmodule A = supportConstSubmodule B) (i j : Fin n) :
    SupportEqv A i j ↔ SupportEqv B i j := by
  rw [supportEqv_iff_forall_const_eq A i j,
    supportEqv_iff_forall_const_eq B i j]
  constructor
  · intro h x hx
    exact h x (by simpa [hsub] using hx)
  · intro h x hx
    exact h x (by simpa [hsub] using hx)

/-- At a plateau of the equality-space chain, the support partition of two consecutive powers is
literally unchanged. -/
theorem supportEqv_pow_plateau {n : ℕ} {A : RMat n} {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k))
    (i j : Fin n) :
    SupportEqv (A ^ (k + 1)) i j ↔ SupportEqv (A ^ k) i j :=
  supportEqv_iff_of_supportConst_eq hplateau i j

end Foregger
