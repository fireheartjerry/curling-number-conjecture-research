# Verify the r=4 tame forced-replay table.
# Tail T_l = B^2 + U[0:l]; local pair = canonical pair among suffix powers
# whose window fits inside the tail; also check whether the
# exponent-limiting mismatch lies inside the tail (Q-independent).

B = [2, 2, 3, 2]


def local_pair(t):
    """(kappa_loc, canonical root, limit_inside) using only tail letters."""
    n = len(t)
    best_k, best_s = 1, None
    for s in range(1, n + 1):
        block = t[n - s :]
        k = 1
        while (k + 1) * s <= n and t[n - (k + 1) * s : n - k * s] == block:
            k += 1
        # k = exponent visible inside the tail
        if k > best_k:
            best_k, best_s = k, s
    if best_k == 1:
        return 1, None, True
    # canonical root: least s achieving best_k
    for s in range(1, n // best_k + 1):
        block = t[n - s :]
        if t[n - best_k * s :] == block * best_k:
            # limit inside tail iff the (k+1)-th copy window fits
            limit_inside = (best_k + 1) * s <= n
            return best_k, s, limit_inside
    raise AssertionError


tail = B + B + [3]  # U[0] = 3 is given, not tame-computed
forced = [3]
rows = [(0, 3, "given", "-", 9)]
for phase in range(1, 16):
    k, s, lim = local_pair(tail)
    rows.append((phase, k, s, lim, len(tail)))
    forced.append(k)
    tail = tail + [k]

print("phase | kappa_loc root limit_inside |T|")
for r in rows:
    print(r)
print("forced U[0:16]:", "".join(map(str, forced)))

# check: no local square at phase 15
assert rows[15][1] == 1
# occurrences of B inside forced word (tame-consistent q)
F = forced
hits = [i for i in range(len(F) - 3) if F[i : i + 4] == [2, 2, 3, 2]]
print(
    "B=2232 occurs in forced word at positions:", hits, "-> q =", [h + 8 for h in hits]
)
# endpoint pairs for those q: pair_loc at phase m = q-4
for h in hits:
    m = h + 4
    t = B + B + F[:m]
    print(
        "q =",
        h + 8,
        " endpoint local pair:",
        local_pair(t)[:2],
        " required (2,",
        h + 8,
        ")",
    )
