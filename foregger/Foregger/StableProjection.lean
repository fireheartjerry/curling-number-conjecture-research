import Foregger.StableBlockSystem
import Foregger.BlockProjection

namespace Foregger

/-- The stabilized block system obeys its routing exactly. -/
theorem stableBlockSystem_obeysRouting {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k)) :
    (stableBlockSystem hA hplateau).ObeysRouting A := by
  intro i j hnot
  exact entry_eq_zero_of_not_stable_target hA hplateau hnot

/-- Stable right projection. -/
theorem stable_mul_averaging_eq_uniformTransition {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k)) :
    A * (stableBlockSystem hA hplateau).averaging =
      (stableBlockSystem hA hplateau).uniformTransition :=
  (stableBlockSystem hA hplateau).mul_averaging_eq_uniformTransition hA
    (stableBlockSystem_obeysRouting hA hplateau)

/-- Stable left projection. -/
theorem stable_averaging_mul_eq_uniformTransition {n : ℕ} {A : RMat n} (hA : IsDS A) {k : ℕ}
    (hplateau : supportConstSubmodule (A ^ (k + 1)) = supportConstSubmodule (A ^ k)) :
    (stableBlockSystem hA hplateau).averaging * A =
      (stableBlockSystem hA hplateau).uniformTransition :=
  (stableBlockSystem hA hplateau).averaging_mul_eq_uniformTransition hA
    (stableBlockSystem_obeysRouting hA hplateau)

end Foregger
