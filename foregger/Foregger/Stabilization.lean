import Foregger.StableSpace
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas

open scoped BigOperators Matrix
open Matrix Finset Module

namespace Foregger

/-- Any antitone sequence of natural numbers plateaus no later than its initial value. -/
theorem nat_antitone_has_plateau_aux (d : ℕ) (f : ℕ → ℕ)
    (h0 : f 0 ≤ d) (hmono : ∀ k, f (k + 1) ≤ f k) :
    ∃ k, k ≤ d ∧ f (k + 1) = f k := by
  induction d generalizing f with
  | zero =>
      refine ⟨0, le_rfl, ?_⟩
      have hle := hmono 0
      omega
  | succ d ih =>
      by_cases heq : f 1 = f 0
      · exact ⟨0, Nat.zero_le _, by simpa using heq⟩
      · have hlt : f 1 < f 0 := lt_of_le_of_ne (by simpa using hmono 0) heq
        have h1d : f 1 ≤ d := by omega
        let g : ℕ → ℕ := fun k => f (k + 1)
        have hgmono : ∀ k, g (k + 1) ≤ g k := by
          intro k
          simpa [g, Nat.add_assoc] using hmono (k + 1)
        obtain ⟨k, hk, hkg⟩ := ih g h1d hgmono
        refine ⟨k + 1, Nat.succ_le_succ hk, ?_⟩
        simpa [g, Nat.add_assoc] using hkg

theorem nat_antitone_has_plateau (f : ℕ → ℕ)
    (hmono : ∀ k, f (k + 1) ≤ f k) :
    ∃ k, k ≤ f 0 ∧ f (k + 1) = f k :=
  nat_antitone_has_plateau_aux (f 0) f le_rfl hmono

/-- The exact norm-preserving subspaces of the powers of a doubly stochastic `n × n` matrix
plateau by step `n`. -/
theorem exists_supportConst_plateau {n : ℕ} {A : RMat n} (hA : IsDS A) :
    ∃ k, k ≤ n ∧
      supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k) := by
  let f : ℕ → ℕ := fun k => Module.finrank ℝ (supportConstSubmodule (A ^ k))
  have hmono : ∀ k, f (k + 1) ≤ f k := by
    intro k
    exact Submodule.finrank_mono (supportConst_pow_succ_le hA k)
  have hbound : f 0 ≤ n := by
    calc
      f 0 ≤ Module.finrank ℝ (Fin n → ℝ) := Submodule.finrank_le _
      _ = n := by simp
  obtain ⟨k, hk, hdim⟩ := nat_antitone_has_plateau f hmono
  refine ⟨k, hk.trans hbound, ?_⟩
  apply Submodule.eq_of_le_of_finrank_le (supportConst_pow_succ_le hA k)
  simpa [f] using hdim.ge

/-- If `x` preserves norm through `k+1` steps, then already the first application of `A`
preserves its norm. -/
theorem first_step_sqMass_eq_of_mem_pow_succ {n : ℕ} {A : RMat n} (hA : IsDS A)
    (k : ℕ) {x : Fin n → ℝ}
    (hx : x ∈ supportConstSubmodule (A ^ (k + 1))) :
    sqMass (A *ᵥ x) = sqMass x := by
  have hend : sqMass ((A ^ (k + 1)) *ᵥ x) = sqMass x :=
    sqMass_eq_of_mem_supportConst (isDS_pow hA (k + 1)) hx
  have hfirst : sqMass (A *ᵥ x) ≤ sqMass x := isDS_sqMass_mulVec_le hA x
  have htail0 := isDS_sqMass_mulVec_le (isDS_pow hA k) (A *ᵥ x)
  have htail : sqMass ((A ^ (k + 1)) *ᵥ x) ≤ sqMass (A *ᵥ x) := by
    simpa only [Matrix.mulVec_mulVec, pow_succ] using htail0
  linarith

/-- The first image of a vector in the `(k+1)`-step equality space belongs to the `k`-step
equality space. -/
theorem mulVec_mem_supportConst_pow {n : ℕ} {A : RMat n} (hA : IsDS A)
    (k : ℕ) {x : Fin n → ℝ}
    (hx : x ∈ supportConstSubmodule (A ^ (k + 1))) :
    A *ᵥ x ∈ supportConstSubmodule (A ^ k) := by
  apply (sqMass_mulVec_eq_iff_mem_supportConst (isDS_pow hA k) (A *ᵥ x)).mp
  have hend : sqMass ((A ^ (k + 1)) *ᵥ x) = sqMass x :=
    sqMass_eq_of_mem_supportConst (isDS_pow hA (k + 1)) hx
  have hfirst := first_step_sqMass_eq_of_mem_pow_succ hA k hx
  calc
    sqMass ((A ^ k) *ᵥ (A *ᵥ x)) = sqMass ((A ^ (k + 1)) *ᵥ x) := by
      simp only [Matrix.mulVec_mulVec, pow_succ]
    _ = sqMass x := hend
    _ = sqMass (A *ᵥ x) := hfirst.symm

/-- Once two consecutive equality spaces coincide, the next pair also coincides.  So a plateau is
a true fixed point of the chain, not a temporary pause. -/
theorem supportConst_plateau_succ {n : ℕ} {A : RMat n} (hA : IsDS A) (k : ℕ)
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k)) :
    supportConstSubmodule (A ^ (k + 2)) = supportConstSubmodule (A ^ (k + 1)) := by
  apply le_antisymm
  · simpa [Nat.add_assoc] using supportConst_pow_succ_le hA (k + 1)
  · intro x hx
    have hAx_k : A *ᵥ x ∈ supportConstSubmodule (A ^ k) :=
      mulVec_mem_supportConst_pow hA k hx
    have hAx_k1 : A *ᵥ x ∈ supportConstSubmodule (A ^ (k + 1)) := by
      rw [hplateau]
      exact hAx_k
    apply (sqMass_mulVec_eq_iff_mem_supportConst (isDS_pow hA (k + 2)) x).mp
    have hfirst := first_step_sqMass_eq_of_mem_pow_succ hA k hx
    have hAxEq : sqMass ((A ^ (k + 1)) *ᵥ (A *ᵥ x)) = sqMass (A *ᵥ x) :=
      sqMass_eq_of_mem_supportConst (isDS_pow hA (k + 1)) hAx_k1
    calc
      sqMass ((A ^ (k + 2)) *ᵥ x) = sqMass ((A ^ (k + 1)) *ᵥ (A *ᵥ x)) := by
        simp only [Matrix.mulVec_mulVec, pow_succ]
      _ = sqMass (A *ᵥ x) := hAxEq
      _ = sqMass x := hfirst

/-- A plateau propagates forever. -/
theorem supportConst_plateau_add {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k)) :
    ∀ t : ℕ,
      supportConstSubmodule (A ^ (k + t + 1)) = supportConstSubmodule (A ^ (k + t)) := by
  intro t
  induction t with
  | zero => simpa using hplateau
  | succ t ih =>
      have hs := supportConst_plateau_succ hA (k + t) ih
      simpa [Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using hs

end Foregger
