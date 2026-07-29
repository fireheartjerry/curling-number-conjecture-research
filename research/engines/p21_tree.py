import sys

sys.path.insert(0, r"C:\Users\fireh\OneDrive\Documents\Curling Problem")
from curling import curling_number

B = [2, 2, 3, 2]


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


def word_kappa(K):
    """curling number of the known word K plus branch opportunities.
    Returns (kappa, ext_branches, cross_roots):
      ext_branches: roots rho whose (e+1)-th copy would cross the left edge
                    and whose visible part matches (deep letters could extend)
      cross_roots:  periods s2 of K with 3*s2 > len(K) (wholly-crossing cube
                    possible, root already consistent with K)"""
    L = len(K)
    best = 1
    ext = []
    for rho in range(1, L // 2 + 1):
        c = 1
        while (c + 1) * rho <= L:
            if K[L - (c + 1) * rho : L - c * rho] != K[L - rho :] and K[
                L - (c + 1) * rho : L - c * rho
            ] != tuple(K[L - rho :]):
                break
            c += 1
        # visible-part check for the (c+1)-th copy crossing the left edge
        vis = L - c * rho  # letters of the next copy visible (from left edge)
        if (c + 1) * rho > L and vis > 0:
            if K[:vis] == K[L - rho :][rho - vis :]:
                ext.append((rho, c))
        elif (c + 1) * rho > L and vis == 0:
            ext.append((rho, c))
        best = max(best, c)
    crosses = []
    for s2 in range(1, L):
        if 3 * s2 > L and all(K[i] == K[i + s2] for i in range(L - s2)):
            crosses.append(s2)
    return best, ext, crosses


def explore(K, depth, hist, log, maxdepth=400, maxnodes=200000, counter=[0]):
    """DFS over the forced continuation. K = tuple of known letters (suffix of
    the state, left edge = deepest known). Returns True if every branch dies."""
    counter[0] += 1
    if counter[0] > maxnodes:
        log.append(("NODES-CAP", depth))
        return False
    if depth > maxdepth:
        log.append(("DEPTH-CAP", depth))
        return False
    kappa, ext, crosses = word_kappa(K)
    # hard death: word kappa >= 4 (state kappa >= word kappa > 3)
    if kappa >= 4:
        return True
    # possible state kappas at this phase:
    outcomes = set()
    if kappa >= 1:
        outcomes.add(kappa)  # no-crossing value
    branch_pins = []  # (new_kappa, pinned-extension description -> new K)
    for rho, c in ext:
        # extension: deep letters complete the (c+1)-th copy: kappa -> c+1
        newk = c + 1
        if newk > 3:
            continue  # would exceed 3: extension is impossible in an orbit
        # pin the missing left part of that copy
        miss = (c + 1) * rho - len(K)
        newK = tuple(K[len(K) - rho :][:miss]) + tuple(K)
        branch_pins.append((newk, newK, ("ext", rho, c)))
    for s2 in crosses:
        miss = 3 * s2 - len(K)
        if miss <= 0:
            continue
        # pin periodic extension for the crossing cube
        pref = []
        for i in range(miss):
            pref.append(K[(len(K) - s2) + ((i - miss) % s2)])
        idx0 = len(K) % s2
        newK = tuple(K[j % s2 + (len(K) - s2)] for j in range(0, 0)) + tuple(K)
        # simpler: extend leftward by periodicity
        left = []
        for i in range(miss, 0, -1):
            left.append(K[len(K) - s2 + ((-i) % s2)])
        newK = tuple(left) + tuple(K)
        if curling_number(newK) >= 4:
            continue
        branch_pins.append((3, newK, ("cross", s2)))
    # the generated symbol must equal the state kappa; state kappa is the
    # no-branch value, or a branch value. Explore each.
    all_dead = True
    # no-branch: state kappa = word kappa; symbol = kappa; must be 2 or 3
    if kappa in (2, 3):
        if not explore(
            K + (kappa,), depth + 1, hist + [kappa], log, maxdepth, maxnodes, counter
        ):
            all_dead = False
    elif kappa == 1:
        pass  # cannot emit 1; only branches survive
    for nk, newK, tag in branch_pins:
        if nk in (2, 3):
            if not explore(
                newK + (nk,), depth + 1, hist + [nk], log, maxdepth, maxnodes, counter
            ):
                all_dead = False
    return all_dead


for lstar in (52, 54):
    T = tuple(B + B + forced[:lstar])
    n = len(T)
    miss = 63 - n
    pin = tuple(T[n - 21 + ((-i) % 21)] for i in range(miss, 0, -1))
    K0 = pin + T + (3,)
    log = []
    counter = [0]
    ok = explore(K0, 0, [], log, maxdepth=400, maxnodes=500000, counter=counter)
    print(
        "family (%d,21): all branches dead: %s  nodes=%d  log=%s"
        % (lstar, ok, counter[0], log[:5])
    )
    sys.stdout.flush()
