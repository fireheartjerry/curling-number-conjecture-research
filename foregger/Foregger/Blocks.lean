import Foregger.Basic

open scoped BigOperators Matrix
open Matrix Finset

namespace Foregger

/-- A finite partition of the state space, together with a permutation of its blocks.
The size condition is exactly what is forced by double stochasticity on a deterministic
block transition. -/
structure BlockSystem (n : ℕ) (β : Type*) [Fintype β] [DecidableEq β] where
  block : Fin n → β
  onto : Function.Surjective block
  perm : Equiv.Perm β
  card_perm : ∀ a : β,
    (univ.filter fun i : Fin n => block i = a).card =
      (univ.filter fun i : Fin n => block i = perm a).card

namespace BlockSystem

variable {n : ℕ} {β : Type*} [Fintype β] [DecidableEq β]

/-- Number of states in a block. -/
def size (B : BlockSystem n β) (a : β) : ℕ :=
  (univ.filter fun i : Fin n => B.block i = a).card

theorem size_pos (B : BlockSystem n β) (a : β) : 0 < B.size a := by
  obtain ⟨i, hi⟩ := B.onto a
  rw [size, Finset.card_pos]
  exact ⟨i, by simp [hi]⟩

theorem size_ne_zero (B : BlockSystem n β) (a : β) : B.size a ≠ 0 :=
  Nat.ne_of_gt (B.size_pos a)

theorem size_perm (B : BlockSystem n β) (a : β) : B.size (B.perm a) = B.size a := by
  simpa [size] using (B.card_perm a).symm

/-- Block averaging projection. -/
noncomputable def averaging (B : BlockSystem n β) : RMat n := fun i j =>
  if B.block j = B.block i then (B.size (B.block i) : ℝ)⁻¹ else 0

/-- Uniform deterministic transition from each block to its permuted successor block. -/
noncomputable def uniformTransition (B : BlockSystem n β) : RMat n := fun i j =>
  if B.block j = B.perm (B.block i) then (B.size (B.block i) : ℝ)⁻¹ else 0

/-- Mass of transitions that violate the deterministic block permutation. -/
noncomputable def leakage (B : BlockSystem n β) (A : RMat n) : ℝ :=
  ∑ i : Fin n, ∑ j : Fin n,
    if B.block j = B.perm (B.block i) then 0 else A i j

end BlockSystem

end Foregger
