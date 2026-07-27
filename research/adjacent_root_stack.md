# Consecutive maximizing roots: exact push/pop geometry

This note gives the strongest interval statement that follows from two
neighboring orbit transitions.  It also records why these intervals do
not form a global laminar stack.

Let `T[0:n]` be an orbit state with exact value

```
k=cn(T[0:n])>=2,
```

and let `p` be the length of a primitive maximizing root.  After appending
`k`, put

```
l=cn(T[0:n+1])>=2
```

and choose a primitive maximizing root of length `q`.  Define the complete
powered intervals

```
I=[n-kp,n),
J=[n+1-lq,n+1).
```

The known one-step bound gives `l<=k+1`.

## Adjacent separation lemma

Exactly one of the following occurs.

1. `q=p`.  The old `p`-periodic suffix extends through the appended
   symbol, and `l` is `k` or `k+1`.
2. `q>p`.  The new powered interval contains the whole old one together
   with the appended site:

   ```
   n+1-lq <= n-kp,
   q>(k-1)p+gcd(p,q).
   ```

3. `q<p`.  After deleting the appended site, the new periodic shadow is
   contained in the old powered interval:

   ```
   n+1-lq > n-kp,
   p>=(l-1)q+gcd(p,q).
   ```

To prove this, the overlap of `I` with `J` after deleting the final site
has length

```
O=min(kp,lq-1)
```

and has periods `p` and `q`.  If `p!=q`, Fine--Wilf and primitivity give

```
O<p+q-gcd(p,q).                                  (1)
```

If `kp<=lq-1`, equation (1) gives

```
q>(k-1)p+gcd(p,q).                               (2)
```

In particular `q>p`.  Conversely, if `lq-1<kp`, equation (1), with
integer rounding, gives

```
p>=(l-1)q+gcd(p,q),                              (3)
```

and therefore `p>q`.  Thus the comparison of the two powered lengths
cannot have the orientation opposite to the comparison of the roots.
The endpoint inequalities in cases 2--3 are the same powered-length
comparison rewritten as interval starts.

When `p=q`, existence of `J` says that the appended symbol is the next
letter in the old `p`-periodic continuation.  Hence the last `kp`
symbols after the append are `k` copies of a rotation of the old root,
so `l>=k`.  Together with `l<=k+1`, this gives case 1.

Thus adjacent changes really are a push to a larger enclosing period or a
pop to a smaller internal period.  For `k>=3`, every push more than
doubles the root.  For `l>=3`, every pop decreases the root by more than
a factor two.  The weak transitions are exactly those incident to value
two.

## Why there is no global interval stack

Powered intervals from nonconsecutive episodes can cross.  The exact
orbit from the seed

```
22322232
```

has the following least-maximizing-root data:

```
cut  8: value 2, root 4, powered interval [0,8)
cut 12: value 3, root 4, powered interval [0,12)
cut 17: value 2, root 6, powered interval [5,17)
cut 18: value 2, root 6, powered interval [6,18)
```

The maximal period-four run is `[0,12)`, while the later maximal
period-six run is `[5,18)`.  They overlap on `[5,12)`, but neither
contains the other.  All intervening transitions are genuine orbit
transitions and obey the adjacent lemma.

Consequently, pushing and popping only the currently selected root does
not leave a LIFO family of ancestral intervals: a retired period can be
crossed by a later run.  Replacing complete powers by maximal periodic
runs does not repair laminarity, as the two displayed maximal runs show.

The executable `check_adjacent_root_stack.py` independently enumerates
all maximizing roots on the orbit episode, checks the adjacent
inequalities at every nonterminal transition, and verifies the crossing
run coordinates above.
