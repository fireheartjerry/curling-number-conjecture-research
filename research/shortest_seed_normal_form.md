# Shortest-counterexample one-symbol deletion normal form

This note assumes a hypothetical counterexample and records an exact
normal form.  It does not prove termination.

Choose a counterexample seed `S=aU` of minimum length.  The shorter seed
`U` terminates.  Compare the two deterministic evolutions until their first
different output.  Immediately before that output the states have the form

`aH` and `H`,

because all earlier outputs agreed.  Suffix monotonicity makes the global
label `k` strictly larger than the local label `ell`.  A primitive
maximizing `k`-root of `aH` cannot fit in `H`; otherwise the local label
would be at least `k`.  Since the state lengths differ by one, its powered
length is exactly

`k*r=|H|+1`,

and the whole global state is a pure power

`aH=Y^k`, with `|Y|=r`.

Deleting the first symbol gives

`H=Y[1:r] Y^(k-1)`.

Thus `H` ends in `Y^(k-1)`, so `ell>=k-1`.  Since `ell<k`,

`ell=k-1`.

The first mismatch is therefore the exact whole-word maturation

`Y^k : k` versus `Y[1:r]Y^(k-1) : k-1`.

The primitive root `Y` does not automatically support induction on the
minimum seed length.  Put `n=|S|`.

* If `r>=n`, the prefix of the global orbit word of length `r` is exactly
  `Y`.  It is an earlier state on the hypothetical counterorbit, hence is
  itself nonterminating.  The normal form is a self-replication event of an
  earlier state, not a reduction to a terminating seed.
* If `r<n`, minimum seed length says that `Y` terminates, but `Y` is a
  prefix of the current pure power, not a suffix whose evolution stayed
  coupled to the global one.  Proving that termination transfers from
  `Y` to `Y^k` is precisely the context-masking/power-self-replication
  obstruction.

Executed examples from both implementations in `curling.py` calibrate the
two issues.

* `Y=23` has `cn(Y)=1`, while `Y^2=2323` has curling number two and tail
  length four.  A terminating root and its power need not have coupled
  first steps.
* For `S=223222323` and its one-symbol deletion `23222323`, the first
  outputs differ only after 54 common outputs.  At that point the global
  state is `Y^3`, its curling number is three, the deleted state has
  curling number two, and

  `Y=223222323222322232232`, `|Y|=21>|S|=9`.

  Executed reconstruction confirms that this `Y` is the earlier global
  orbit state at time 12.  The respective executed tail lengths of `S`,
  its deletion, and `Y` are 59, 58, and 47; the example is a finite
  calibration, not a counterexample.

Consequently the one-symbol normal form is rigorous and useful, but a
post-break theorem transferring termination through a primitive power is
still load-bearing.  Without such a theorem, this route repackages the
fixed-origin square/cube tower rather than closing it.
