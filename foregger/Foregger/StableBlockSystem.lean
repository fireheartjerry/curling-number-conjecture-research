import Foregger.StablePermutation
import Foregger.Blocks

namespace Foregger

/-- The support classes at a stabilized power, equipped with the deterministic size-preserving
permutation induced by `A`. -/
noncomputable def stableBlockSystem {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k)) :
    BlockSystem n (SupportClass (A ^ k)) where
  block := supportClassMk (A ^ k)
  onto := supportClassMk_surjective (A ^ k)
  perm := stableClassPerm hA hplateau
  card_perm := by
    intro c
    change supportClassSize (A ^ k) c =
      supportClassSize (A ^ k) (stableClassPerm hA hplateau c)
    exact (stableClassPerm_size hA hplateau c).symm

@[simp] theorem stableBlockSystem_block {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k))
    (i : Fin n) :
    (stableBlockSystem hA hplateau).block i = supportClassMk (A ^ k) i :=
  rfl

@[simp] theorem stableBlockSystem_perm {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k))
    (c : SupportClass (A ^ k)) :
    (stableBlockSystem hA hplateau).perm c = stableClassPerm hA hplateau c :=
  rfl

/-- Every positive entry of `A` follows the canonical block permutation of the stabilized block
system. -/
theorem positive_entry_follows_stableBlockSystem {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k))
    {i j : Fin n} (hij : 0 < A i j) :
    (stableBlockSystem hA hplateau).block j =
      (stableBlockSystem hA hplateau).perm ((stableBlockSystem hA hplateau).block i) := by
  change supportClassMk (A ^ k) j =
    stableClassPerm hA hplateau (supportClassMk (A ^ k) i)
  exact (positive_entry_target_class hA hplateau hij).symm

/-- Entries outside the canonical routed block vanish exactly. -/
theorem entry_eq_zero_of_not_stable_target {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k))
    {i j : Fin n}
    (hnot : (stableBlockSystem hA hplateau).block j ≠
      (stableBlockSystem hA hplateau).perm ((stableBlockSystem hA hplateau).block i)) :
    A i j = 0 := by
  apply le_antisymm
  · apply not_lt.mp
    intro hpos
    exact hnot (positive_entry_follows_stableBlockSystem hA hplateau hpos)
  · exact isDS_nonneg hA i j

end Foregger
