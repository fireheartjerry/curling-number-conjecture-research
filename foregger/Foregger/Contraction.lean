import Mathlib.Analysis.Convex.Birkhoff
import Mathlib.Analysis.CStarAlgebra.Matrix
import Foregger

open scoped Matrix.Norms.L2Operator

namespace Foregger

/-- Every doubly stochastic real matrix is a Euclidean `ℓ₂` contraction. -/
theorem isDS_l2_opNorm_le_one {n : ℕ} {A : RMat n} (hA : IsDS A) : ‖A‖ ≤ 1 := by
  exact Matrix.l2_opNorm_le_one_of_mem_doublyStochastic hA

/-- Every power of a doubly stochastic real matrix is again an `ℓ₂` contraction. -/
theorem isDS_pow_l2_opNorm_le_one {n : ℕ} {A : RMat n} (hA : IsDS A) (k : ℕ) :
    ‖A ^ k‖ ≤ 1 := by
  exact isDS_l2_opNorm_le_one (isDS_pow hA k)

end Foregger
