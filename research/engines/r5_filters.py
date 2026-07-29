from itertools import product

MAXR = 16


def has_period(w, d):
    return all(w[i] == w[i + d] for i in range(len(w) - d))


def is_primitive(w):
    L = len(w)
    return not any(L % d == 0 and has_period(w, d) for d in range(1, L))


def terminal_run3(w):
    c = 0
    for x in reversed(w):
        if x != 3:
            break
        c += 1
    return c


def catalogue(r):
    out = []
    for t in range(r // 2 + 1, r):
        a = r - t
        for w in product((2, 3), repeat=r):
            if w[0] != 2:
                continue
            if not has_period(w, t):
                continue
            if w[a] != 2:
                continue
            if not is_primitive(w):
                continue
            if any(has_period(w, d) for d in range(1, r // 2 + 1)):
                continue
            if terminal_run3(w) > 1:
                continue
            out.append((t, w))
    return out


def ends_in_power(word, rho, k):
    """word (tuple) ends in a k-power of root rho?"""
    if k * rho > len(word):
        return False
    block = word[len(word) - rho :]
    return word[len(word) - k * rho :] == block * k


def filters(r, t, B):
    lam = terminal_run3(B)
    # S8: no terminal square of B with root <= r/2 (visible in G, pi(G)=q)
    for rho in range(1, r // 2 + 1):
        if ends_in_power(B, rho, 2):
            return "S8-rho%d" % rho
    # S7: B^3 has no suffix cube of root < r (pi(F) = r exactly)
    B3 = B * 3
    for rho in range(1, r):
        if ends_in_power(B3, rho, 3):
            return "S7-rho%d" % rho
    # bridge cuts h = 1..2r-1; visible B-periodic suffix V_h of length r+h
    Binf = B * 4
    for h in range(1, 2 * r):
        lab = B[h % r]
        V = Binf[: r + h] if False else None
        # suffix of B^inf ending at cut position h, length r+h:
        # cut position h corresponds to ...B B B[0:h]; build directly
        V = (B * 3)[: 2 * r + h][-(r + h) :] if h <= r else (B * 3)[: r + h]
        # simpler: V = last r+h letters of B*2 + B[0:h]
        V = tuple((B + B + B)[: 2 * r + h][h:]) if False else None
        W = tuple(B + B + B[:h] if h <= r else B + B + B + B[: h - r])
        W = tuple((B * 3 + B)[: 3 * r + (h % r)]) if False else W
        # W = B^k B[0:h mod r] with enough left context; take last r+h letters
        full = tuple(B * 4)[: 4 * r]
        # word ending at cut h: B-periodic word ending with B[0:h mod r] after
        # (h // r) whole B's plus the R-final B. Total visible length r + h.
        # Its letters: (B^inf) suffix aligned so the end is at position h mod r.
        end_phase = h % r
        big = tuple(B * 6)
        # position of end: choose index j with j % r == end_phase, j large
        j = 4 * r + end_phase
        vis = big[j - (r + h) : j]
        if lab == 2:
            for rho in range(1, (r + h) // 3 + 1):
                if ends_in_power(vis, rho, 3):
                    return "S11-h%d-rho%d" % (h, rho)
        else:
            if h > r:
                i = h - r
                if i == r - 1 and lam == 1:
                    continue  # full-root seam exception
                okc = False
                for rho in range(1, r):
                    if 3 * rho <= 2 * r + i and ends_in_power(vis, rho, 3):
                        okc = True
                        break
                if not okc:
                    return "S12-i%d" % i
    return None


print("r : total | killed-per-filter | SURVIVORS")
for r in range(5, MAXR + 1):
    cat = catalogue(r)
    surv = []
    kills = {}
    seen = set()
    for t, B in cat:
        if B in seen:
            continue
        seen.add(B)
        why = filters(r, t, B)
        if why is None:
            surv.append("".join(map(str, B)))
        else:
            kills[why.split("-")[0]] = kills.get(why.split("-")[0], 0) + 1
    print(r, ":", len(seen), "|", kills, "| survivors:", len(surv), surv[:12])
