# Repository audit — 2026-07-27

## Package integrity

- All 20 source entries in the external `MANIFEST.json` match their declared
  byte lengths and SHA-256 hashes after accounting for the Windows
  case-collision rename.
- The standalone original prompt PDF is byte-for-byte identical to the
  packaged PDF.
- `PACKAGE_MANIFEST.sha256` contains a stale self-hash. A checksum file cannot
  reliably authenticate its own final bytes; do not use that line.

## Reproduced computations

Fresh runs reproduced:

- Python calibration and Part 3 examples: `5, 66, 142`.
- `audit_all_square_replay.cpp 18 500`:
  `squares=9722 tested=9722 fullmatch=9722 mismatch=0`.
- `audit_bridge_promotion.cpp 18 500`:
  `squares=9722 promotion=9722 non=0`.
- `replay_local_promo2.cpp`: `valid=2286 strict=1536 promotion=1536 non=0`.
- A bounded monotonicity run through binary seed length 18 found no
  counterexample and only the `6/4 -> 7/4` transition.

These are bounded observations. They do not prove synchronization, bridge
promotion, monotonicity, autonomous termination, or the conjecture.

## Computational caveats

1. Several C++ audits use `n-p >= seed_length`, which proves that the final
   copy begins after the seed. It does **not** prove an entirely generated
   square, which would require `n-2p >= seed_length`.
2. The `500`-step limit is silent; capped trajectories are not counted.
3. Several programs stop at any curling number outside `{2,3}`, not literally
   at the first `1`.
4. `curling_research_tools.total_length_before_first_one()` is misnamed: its
   trace stops outside `{2,3}` and fails on trajectories that first hit `4`.
5. Some verifiers print examples without asserting every printed property.
6. The preserved outputs do not include reproducible evidence for every large
   census claimed in prose, including the length-26 and million-random-seed
   searches.

## Mathematical caveats

1. Generated Two-Cube Synchronization is genuinely open.
2. Its current wording must exclude terminal `H` from “intermediate period at
   least `P`” or it becomes tautological.
3. The Border–conjugate short-period lemma survives an initial index audit,
   but no proof derives the required short period `t<b`.
4. The proposed Cell C split must be restated in exact interval coordinates;
   “contained in `Y` / crosses `Y|B` / crosses `B|T`” is ambiguous for a suffix
   cube ending after `BT`.
5. The old bounded-overhang theorem proves only a contexted episode
   `cn(LZ^2)=2 -> cn(LZ^3)=3`. It does not prove standalone bridge-root
   promotion and does not close Cells A–C.

