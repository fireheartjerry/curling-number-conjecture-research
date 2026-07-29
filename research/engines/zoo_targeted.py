import sys
from math import gcd

sys.path.insert(0, r"C:\Users\fireh\OneDrive\Documents\Curling Problem")
from curling import curling_number

B = [2, 2, 3, 2]
NEG = -1000000


def canon(t):
    k = curling_number(t)
    if k == 1:
        return 1, None
    for s in range(1, len(t) // k + 1):
        if tuple(t[len(t) - k * s :]) == tuple(t[len(t) - s :]) * k:
            return k, s


tail = tuple(B + B + [3])
forced = [3]
pairs = {}
for ph in range(1, 60):
    k, s0 = canon(tail)
    pairs[ph] = (k, s0)
    forced.append(k)
    tail += (k,)
exits_all = [ph for ph in range(1, 60) if pairs[ph][0] == 2] + [60]


def periods(w):
    n = len(w)
    return [d for d in range(1, n) if all(w[i] == w[i + d] for i in range(n - d))]


def feasible(lstar, q):
    Ql = q - 8
    if Ql < 2:
        return False
    for j in range(min(lstar, Ql), lstar):
        if forced[j] != B[j - Ql]:
            return False
    if lstar >= Ql and (lstar - Ql > 3 or B[lstar - Ql] != 3):
        return False
    return True


REV232 = (2, 3, 2)
REVB2 = (2, 3, 2, 2, 2, 3, 2, 2)


def zone(pos, lstar, q):
    p = q + 3
    if pos <= lstar:
        return ("k", forced[lstar - pos])
    r = pos - lstar
    blk = (r - 1) // p
    off = (r - 1) % p + 1
    if blk >= 3:
        return ("k", None)
    if off <= 8:
        return ("k", REVB2[off - 1])
    if off <= q:
        return ("Q", off - 8)
    return ("k", REV232[off - q - 1])


def consistency(lstar, q, s, expo):
    """Union-find over cube relations; returns None (conflict) or Q-template."""
    Ql = q - 8
    L = 3 * (q + 3) + lstar
    win = min(expo * s, L)
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        r = x
        while parent[r] != r:
            r = parent[r]
        while parent[x] != r:
            parent[x], x = r, parent[x]
        return r

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for i in range(1, (expo - 1) * s + 1):
        if i + s <= win:
            union(("p", i), ("p", i + s))
    for pos in range(1, win + 1):
        z = zone(pos, lstar, q)
        if z[0] == "Q":
            union(("p", pos), ("Qv", z[1]))
    pin = {}
    for j in range(min(lstar, Ql)):
        pin[("Qv", Ql - j)] = forced[j]
    if lstar < Ql:
        pin[("Qv", Ql - lstar)] = 3
    val = {}
    ok = True
    for _ in range(3):
        for pos in range(1, win + 1):
            z = zone(pos, lstar, q)
            if z[0] == "k" and z[1] is not None:
                r = find(("p", pos))
                if r in val and val[r] != z[1]:
                    ok = False
                val[r] = z[1]
        for key, v in pin.items():
            r = find(key)
            if r in val and val[r] != v:
                ok = False
            val[r] = v
    if not ok:
        return None
    Q = []
    for j in range(Ql):
        r = find(("Qv", Ql - j))
        v = val.get(r)
        Q.append(v if v is not None else NEG - j)
    return Q


def kappa_or_wild(seq):
    L = len(seq)
    best = 1
    for rho in range(1, L // 2 + 1):
        c = 1
        while (c + 1) * rho <= L:
            good = True
            wild = None
            for i in range(rho):
                a = seq[L - (c + 1) * rho + i]
                b = seq[L - rho + i]
                if a == b:
                    continue
                if a < 0 or b < 0:
                    wild = a if a < 0 else b
                    continue
                good = False
                break
            if not good:
                break
            if wild is not None:
                return None, NEG - wild
            c += 1
        best = max(best, c)
    return best, None


def simulate(lstar, q, Q0, cap=400000):
    Ql = q - 8
    m = q - 4
    P = q + 4
    stack = [(Q0, 0, lstar)]
    nodes = 0
    while stack:
        nodes += 1
        if nodes > cap:
            return "CAP"
        Q, stage, j = stack.pop()
        X = B[1:] + Q + B + B
        U = Q + B
        if stage == 0:
            seq = X * 3 + U[:j]
            if any(x < 0 for x in U[:j]):
                continue
        elif stage == 1:
            seq = X * 3 + U + B[:j]
        else:
            seq = X * 3 + U + B + B + U[:j]
        if stage >= 1 and any(x < 0 for x in Q):
            qi = next(i for i, x in enumerate(Q) if x < 0)
            for v in (2, 3):
                Q2 = list(Q)
                Q2[qi] = v
                stack.append((Q2, stage, j))
            continue
        kap, wild = kappa_or_wild(seq)
        if wild is not None:
            for v in (2, 3):
                Q2 = list(Q)
                Q2[wild] = v
                stack.append((Q2, stage, j))
            continue
        if stage == 0:
            if j == m:
                if any(x < 0 for x in Q):
                    qi = next(i for i, x in enumerate(Q) if x < 0)
                    for v in (2, 3):
                        Q2 = list(Q)
                        Q2[qi] = v
                        stack.append((Q2, stage, j))
                    continue
                if canon(tuple(seq)) == (2, q):
                    stack.append((Q, 1, 0))
                continue
            need = Q[j] if j < Ql else B[j - Ql]
            if need < 0:
                if kap in (2, 3):
                    Q2 = list(Q)
                    Q2[j] = kap
                    stack.append((Q2, 0, j + 1))
                continue
            if kap == need:
                stack.append((Q, 0, j + 1))
            continue
        if stage == 1:
            if j == 4:
                stack.append((Q, 2, 0))
            elif kap == B[j]:
                stack.append((Q, 1, j + 1))
            continue
        if j == m:
            if canon(tuple(seq)) == (2, P):
                return ("ALIVE", Q)
            continue
        if kap == U[j]:
            stack.append((Q, 2, j + 1))
    return "DEAD"


out = []
checked = 0
sims = 0
for lstar in exits_all:
    for q in range(max(10, lstar + 5), 2 * lstar + 31):
        if lstar > min(q - 5, 60):
            continue
        if not feasible(lstar, q):
            continue
        p = q + 3
        T = B + B + forced[:lstar]
        n = len(T)
        cands = set()
        for s in periods(T):
            if 3 * s > n and s <= lstar + 7:
                cands.add((s, 3))
        for s in range(max(n // 3 + 1, (q - 4) // 2 + 1), (p + lstar) // 2 + 1):
            g = gcd(s, p)
            if 2 * s < p + lstar - g and s != p:
                cands.add((s, 3))
        if lstar == 60:
            for s in range(n // 2 + 1, q + 4):
                cands.add((s, 2))
        for s, expo in sorted(cands):
            if s >= q + 4:
                continue
            checked += 1
            Q0 = consistency(lstar, q, s, expo)
            if Q0 is None:
                continue
            sims += 1
            r = simulate(lstar, q, Q0)
            if r != "DEAD":
                out.append((lstar, q, s, expo, r if r == "CAP" else "ALIVE"))
                print("SURV", lstar, q, s, expo, r if r == "CAP" else r[0])
                sys.stdout.flush()
print("checked", checked, "simulated", sims)
print("FINAL:", out if out else "ZOO EMPTY")
