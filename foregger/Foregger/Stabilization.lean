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

end Foregger
