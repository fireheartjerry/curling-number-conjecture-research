import sys

sys.path.insert(0, r"C:\Users\fireh\OneDrive\Documents\Curling Problem")
from curling import curling_number

NEG = -1000000


def canon(t):
    k = curling_number(t)
    if k == 1:
        return 1, None
    for s in range(1, len(t) // k + 1):
        if tuple(t[len(t) - k * s :]) == tuple(t[len(t) - s :]) * k:
            return k, s


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


def close_q(B, t, q, cap=2000000):
    r = len(B)
    a = r - t
    Ql = q - 2 * r
    m = q - r
    P = q + r
    Q0 = [NEG - i for i in range(Ql)]
    Q0[0] = 3
    if Ql >= 2:
        Q0[1] = 2
    stack = [(Q0, 0, 0)]
    nodes = 0
    alive = []
    while stack:
        nodes += 1
        if nodes > cap:
            return "CAP", nodes
        Q, stage, j = stack.pop()
        X = list(B[a:]) + Q + list(B) + list(B)
        U = Q + list(B)
        if stage == 0:
            seq = X * 3 + U[:j]
            if any(x < 0 for x in U[:j]):
                continue
        elif stage == 1:
            seq = X * 3 + U + list(B[:j])
        else:
            seq = X * 3 + U + list(B) + list(B) + U[:j]
        if stage >= 1 and any(x < 0 for x in Q):
            qi = next(i for i, x in enumerate(Q) if x < 0)
            for v in (2, 3):
                Q2 = list(Q)
                Q2[qi] = v
                stack.append((Q2, stage, j))
            continue
        kap, wild = kappa_or_wild(seq)
        if wild is not None:
            qi = wild
            if not (0 <= qi < Ql):
                continue
            for v in (2, 3):
                Q2 = list(Q)
                Q2[qi] = v
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
            if j == r:
                stack.append((Q, 2, 0))
            elif kap == B[j]:
                stack.append((Q, 1, j + 1))
            continue
        if j == m:
            if canon(tuple(seq)) == (2, P):
                alive.append(list(Q))
            continue
        if kap == U[j]:
            stack.append((Q, 2, j + 1))
    return alive, nodes


WORDS = [
    ("B1", tuple(int(c) for c in "2232223322232"), 9),
    ("B2", tuple(int(c) for c in "2232223222332"), 12),
]

for name, B, t in WORDS:
    r = len(B)
    bad = []
    for q in range(2 * r + 1, 161):
        res, nodes = close_q(B, t, q)
        if res == "CAP":
            bad.append((q, "CAP"))
            print(name, "q", q, "CAP", nodes)
        elif res:
            bad.append((q, len(res)))
            print(name, "q", q, "ALIVE", len(res), res[0])
        sys.stdout.flush()
    print(name, "small-q result:", bad if bad else "ALL DEAD q<=160")
    sys.stdout.flush()
