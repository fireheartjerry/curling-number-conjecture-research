import sys

sys.path.insert(0, r"C:\Users\fireh\OneDrive\Documents\Curling Problem")
from curling import curling_number

B = [2, 2, 3, 2]
NEG = -1000000  # q-variable token base: token NEG-idx means Q[idx] unknown


def canon(t):
    k = curling_number(t)
    if k == 1:
        return 1, None
    for s in range(1, len(t) // k + 1):
        if tuple(t[len(t) - k * s :]) == tuple(t[len(t) - s :]) * k:
            return k, s


def kappa_or_wild(seq):
    """seq entries: 2/3 concrete, or negative token (unknown variable).
    Same token = equal letters. Return (kappa, None) or (None, var_idx)."""
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
                return None, NEG - wild  # decode: var idx = NEG - token
            c += 1
        best = max(best, c)
    return best, None


def close_q(q, cap=1500000):
    Ql = q - 8
    m = q - 4
    P = q + 4
    Q0 = [NEG - i for i in range(Ql)]  # token for Q[i] is NEG-i
    Q0[0] = 3
    Q0[1] = 2
    stack = [(Q0, 0, 0)]
    nodes = 0
    alive = []
    while stack:
        nodes += 1
        if nodes > cap:
            return "CAP", nodes
        Q, stage, j = stack.pop()
        X = Q[:0] + B[1:] + Q + B + B
        U = Q + B
        if stage == 0:
            seq = X * 3 + U[:j]
        elif stage == 1:
            seq = X * 3 + U + B[:j]
        else:
            seq = X * 3 + U + B + B + U[:j]
        kap, wild = kappa_or_wild(seq)
        if wild is not None:
            qi = wild
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
            if j == 4:
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


total_alive = []
for q in range(10, 151):
    r, nodes = close_q(q)
    if r == "CAP":
        total_alive.append((q, "CAP"))
        print("q", q, "CAP after", nodes)
    elif r:
        total_alive.append((q, len(r)))
        print("q", q, "ALIVE", len(r), r[0])
    else:
        print("q", q, "dead  nodes", nodes)
    sys.stdout.flush()
print("DONE:", [t for t in total_alive] or "ZOO EMPTY")
