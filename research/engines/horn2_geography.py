from math import gcd

# tau  = reversed known tail of E2 (t1..t10), tau' = of F2 (t1..t14)
TAU = [2, 3, 2, 3, 2, 2, 2, 3, 2, 2]
TAUP = [2, 3, 2, 3, 2, 2, 2, 3, 2, 2, 2, 3, 2, 2]


def compatible_shifts(A, B, lo=-30, hi=30):
    """Shifts s (start(B) - start(A)) where A,B agree on overlap."""
    ok = set()
    for s in range(lo, hi + 1):
        good = True
        for j in range(len(B)):
            i = j + s
            if 0 <= i < len(A) and A[i] != B[j]:
                good = False
                break
        if good:
            ok.add(s)
    return ok


print("tau  vs tau :", sorted(compatible_shifts(TAU, TAU)))
print("tau  vs tau':", sorted(compatible_shifts(TAU, TAUP)))
print("tau' vs tau':", sorted(compatible_shifts(TAUP, TAUP)))

# Full Case-A pin propagation: Q infinite to the left (pure deep-Q case).
# Early cube root L: relations t_i = t_{i+L}, i=1..2L, on E2 tail
#   (t1..t10 known, t_{10+k} = Q[-k]).
# Later cube root Lp: same with t1..t14 known (t11..t14 = final B of R^2
#   reversed = 2,3,2,2), t_{14+k} = Q[-k].
E_KNOWN = {i + 1: v for i, v in enumerate(TAU)}
F_KNOWN = {i + 1: v for i, v in enumerate(TAUP)}


def pins_from_cube(known, off, root):
    """Return dict depth->letter forced in Q, or None if inconsistent.
    off = number of known state letters before Q starts (10 or 14).
    Uses union-find over state positions 1..3*root with known letters."""
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for i in range(1, 2 * root + 1):
        union(i, i + root)
    value = {}
    for pos in set(parent) | set(known) | set(range(1, 3 * root + 1)):
        r = find(pos)
        v = known.get(pos)
        if v is not None:
            if r in value and value[r] != v:
                return None
            value[r] = v
    out = {}
    for pos in range(off + 1, 3 * root + 1):
        r = find(pos)
        if r in value:
            out[pos - off] = value[r]
    return out


def joint_ok(L, Lp):
    pe = pins_from_cube(E_KNOWN, 10, L)
    pf = pins_from_cube(F_KNOWN, 14, Lp)
    if pe is None or pf is None:
        return False
    for d, v in pe.items():
        if d in pf and pf[d] != v:
            return False
    return True


def fw_kill(L, Lp):
    g = gcd(L, Lp)
    M = min(3 * L - 10, 3 * Lp - 14)
    return M >= L + Lp - g


surv = []
for L in range(10, 161):
    for Lp in range(14, 161):
        if joint_ok(L, Lp) and not fw_kill(L, Lp):
            surv.append((L, Lp))
print("survivors (full pin sim + FW), count:", len(surv))
# classify against the analytic family
fam = []
oddballs = []
for L, Lp in surv:
    if Lp == 2 * L + 4 or Lp >= 2 * L + 13 or L == 2 * Lp - 4 or L >= 2 * Lp + 9:
        fam.append((L, Lp))
    else:
        oddballs.append((L, Lp))
print("in analytic family:", len(fam), " outside:", len(oddballs))
print("outside examples:", oddballs[:40])
lo = [p for p in surv if p[0] <= 30 and p[1] <= 70]
print("small survivors:", lo)
