import runpy
import numpy as np
from itertools import product
from collections import deque

P = 3
ROOT = 'research/'

# Reuse the already verified A3-4-14 construction of B/A and K actions.
ns = runpy.run_path(ROOT + 'A3-4-14_BA_MODULE_FINGERPRINT_2026-09-16.py')
rank3 = ns['rank3']
W = np.array(ns['W'], dtype=np.int64) % P
K_coord = np.array(ns['K_coord'], dtype=np.int64) % P
gens = ns['gens']
apply_linear_map = ns['apply_linear_map']
index4 = ns['index4']
words4 = list(index4.keys())
words5 = list(product((1, 2, 3, 4), repeat=5))
index5 = {w: i for i, w in enumerate(words5)}

# Reconstruct the exact B/A and K representation matrices using the
# A3-4-14 code path.  This keeps the coordinate conventions identical.
# A3-4-14 itself computes these local matrices; we deliberately recompute
# them below from its verified ambient data rather than relying on globals.
D_tau = np.array(ns['D_tau'], dtype=np.int64) % P
B_W = ns['B_W']
D_u = np.vstack([((np.array(B, dtype=np.int64) @ np.array(ns['N'], dtype=np.int64)) % P) for B in B_W])

assert W.shape == (256, 45)
assert K_coord.shape == (45, 35)
assert rank3(W) == 45 and rank3(K_coord) == 35
assert rank3(D_tau) == 45 and rank3(D_u) == 10

# ---------- Exact F_3 linear solver ----------
def solve(A, b):
    A = np.array(A, dtype=np.int64) % P
    b = np.array(b, dtype=np.int64).reshape(-1) % P
    R = np.column_stack([A, b])
    m, n1 = R.shape
    n = n1 - 1
    r = 0
    piv = []
    for c in range(n):
        q = next((i for i in range(r, m) if R[i, c]), None)
        if q is None:
            continue
        R[[r, q]] = R[[q, r]]
        if R[r, c] == 2:
            R[r] = (2 * R[r]) % P
        for i in range(m):
            if i != r and R[i, c]:
                R[i] = (R[i] - R[i, c] * R[r]) % P
        piv.append(c)
        r += 1
        if r == m:
            break
    for i in range(r, m):
        if np.all(R[i, :n] == 0) and R[i, n] != 0:
            return None
    x = np.zeros(n, dtype=np.int64)
    for rr, c in enumerate(piv):
        x[c] = R[rr, n]
    return x % P

# ---------- Build the degree-4 action on W ----------
def gen_matrix(g):
    M = np.zeros((4, 4), dtype=np.int64)
    for j in range(1, 5):
        out = apply_linear_map({(j,): 1}, g)
        for ww, c in out.items():
            if len(ww) == 1:
                M[ww[0] - 1, j - 1] = (M[ww[0] - 1, j - 1] + c) % P
    return M % P

Mgens = [gen_matrix(g) for g in gens]

A_W_coord = []
for Gmat in Mgens:
    G = np.zeros((256, 256), dtype=np.int64)
    for j, w in enumerate(words4):
        out = apply_linear_map({w: 1}, gens[Mgens.index(Gmat)] if False else None)
    # Rebuild directly from Gmat on tensor words: the generator matrices
    # act letterwise on degree-4 words.
    for j, w in enumerate(words4):
        partial = {(): 1}
        for letter in w:
            nxt = {}
            for pref, coef in partial.items():
                for out_letter in range(4):
                    a = int(Gmat[out_letter, letter - 1]) % P
                    if a:
                        key = pref + (out_letter + 1,)
                        nxt[key] = (nxt.get(key, 0) + coef * a) % P
            partial = nxt
        for ww, c in partial.items():
            G[index4[ww], j] = c % P
    cols = []
    for j in range(45):
        z = solve(W, (G @ W[:, j]) % P)
        assert z is not None
        cols.append(z)
    A_W_coord.append(np.array(cols, dtype=np.int64).T % P)

# ---------- Rebuild B/A representation ----------
A_basis = np.empty((4096, 0), dtype=np.int64)
for j in range(D_u.shape[1]):
    c = D_u[:, j:j+1]
    if rank3(np.column_stack([A_basis, c])) > rank3(A_basis):
        A_basis = np.column_stack([A_basis, c])
assert A_basis.shape == (4096, 10)
Q_cols = []
cur = A_basis
for j in range(D_tau.shape[1]):
    c = D_tau[:, j:j+1]
    if rank3(np.column_stack([cur, c])) > rank3(cur):
        Q_cols.append(D_tau[:, j])
        cur = np.column_stack([cur, c])
    if len(Q_cols) == 35:
        break
Q_basis = np.array(Q_cols, dtype=np.int64).T % P
C = np.column_stack([A_basis, Q_basis]) % P
assert C.shape == (4096, 45) and rank3(C) == 45

# Actual Hom(V,T^5) action.
def tensor5(M):
    T = np.zeros((1024, 1024), dtype=np.int64)
    for j, w in enumerate(words5):
        partial = {(): 1}
        for letter in w:
            nxt = {}
            for pref, coef in partial.items():
                for out_letter in range(4):
                    a = int(M[out_letter, letter - 1]) % P
                    if a:
                        key = pref + (out_letter + 1,)
                        nxt[key] = (nxt.get(key, 0) + coef * a) % P
            partial = nxt
        for ww, c in partial.items():
            T[index5[ww], j] = c % P
    return T % P

def hom_action(h, M, T):
    Minv = np.column_stack([solve(M, np.eye(4, dtype=np.int64)[:, j]) for j in range(4)]) % P
    blocks = [h[j*1024:(j+1)*1024] % P for j in range(4)]
    out = []
    for j in range(4):
        v = np.zeros(1024, dtype=np.int64)
        for k in range(4):
            v = (v + int(Minv[k, j]) * blocks[k]) % P
        out.append((T @ v) % P)
    return np.concatenate(out) % P

T5gens = [tensor5(M) for M in Mgens]
BA_gens = []
for M, T in zip(Mgens, T5gens):
    cols = []
    for j in range(35):
        z = solve(C, hom_action(Q_basis[:, j], M, T))
        assert z is not None
        cols.append(z[10:])
    BA_gens.append(np.array(cols, dtype=np.int64).T % P)

K_gens = []
for A in A_W_coord:
    cols = []
    for j in range(35):
        z = solve(K_coord, (A @ K_coord[:, j]) % P)
        assert z is not None
        cols.append(z)
    K_gens.append(np.array(cols, dtype=np.int64).T % P)

# ---------- Enumerate H = Sp_4(F_3) from the five generators ----------
def key(M):
    return tuple(int(x) for x in M.reshape(-1))

def mat_from_key(k):
    return np.array(k, dtype=np.int64).reshape(4, 4)

def mm(A, B):
    return (A @ B) % P

I4 = np.eye(4, dtype=np.int64)
Gmap = {key(I4): 0}
group = [I4]
parent = [-1]
parent_gen = [-1]
q = deque([0])
while q:
    i = q.popleft()
    A = group[i]
    for gi, G in enumerate(Mgens):
        Hm = mm(A, G)
        k = key(Hm)
        if k not in Gmap:
            idx = len(group)
            Gmap[k] = idx
            group.append(Hm)
            parent.append(i)
            parent_gen.append(gi)
            q.append(idx)

print('A3-4-15 / CLASS-LEVEL MODULE COMPARISON')
print('Enumerated group size =', len(group))
assert len(group) == 51840

# Generator inverses, verified by multiplication.
Ginv = []
for G in Mgens:
    inv = np.column_stack([solve(G, I4[:, j]) for j in range(4)]) % P
    assert np.array_equal(mm(G, inv), I4)
    Ginv.append(inv)

# Conjugacy classes are connected components under conjugation by the
# generators and their inverses.
adj = [[] for _ in range(len(group))]
for i, A in enumerate(group):
    for G, Gi in zip(Mgens, Ginv):
        for Cg in (G, Gi):
            conj = mm(mm(Cg, A), np.column_stack([solve(Cg, I4[:, j]) for j in range(4)]) % P)
            adj[i].append(Gmap[key(conj)])

seen = np.zeros(len(group), dtype=bool)
classes = []
for start in range(len(group)):
    if seen[start]:
        continue
    dq = [start]
    seen[start] = True
    cls = []
    while dq:
        i = dq.pop()
        cls.append(i)
        for j in adj[i]:
            if not seen[j]:
                seen[j] = True
                dq.append(j)
    classes.append(cls)

print('Conjugacy class count =', len(classes))

# Recover a generator word for every class representative.
def word_for(idx):
    w = []
    while parent[idx] != -1:
        w.append(parent_gen[idx])
        idx = parent[idx]
    return list(reversed(w))

# Representation action of a group element from its generator word.
def rep_from_word(word, mats):
    R = np.eye(35, dtype=np.int64)
    for gi in word:
        R = (R @ mats[gi]) % P
    return R

def mat_order(T, max_order=200):
    R = np.eye(T.shape[0], dtype=np.int64)
    for k in range(1, max_order + 1):
        R = (R @ T) % P
        if np.array_equal(R, np.eye(T.shape[0], dtype=np.int64)):
            return k
    return None

def ranks_powers(T, max_power=8):
    D = (T - np.eye(35, dtype=np.int64)) % P
    out = []
    R = D.copy()
    for _ in range(max_power):
        r = rank3(R)
        out.append(r)
        if r == 0:
            break
        R = (R @ D) % P
    return out

def fingerprint(T):
    D = (T - np.eye(35, dtype=np.int64)) % P
    return {
        'trace_F3': int(np.trace(T) % P),
        'order': mat_order(T),
        'fixed_dim': 35 - rank3(D),
        'rank(T-I)': rank3(D),
        'ranks_powers': ranks_powers(T),
    }

rows = []
for ci, cls in enumerate(classes, 1):
    rep_idx = min(cls)
    word = word_for(rep_idx)
    rep = group[rep_idx]
    Tb = rep_from_word(word, BA_gens)
    Tk = rep_from_word(word, K_gens)
    fb = fingerprint(Tb)
    fk = fingerprint(Tk)
    rows.append((ci, len(cls), rep, word, fb, fk))

print('class | size | group_order | word_length | BA trace/order/fix/rank | K trace/order/fix/rank | equal')
for ci, size, rep, word, fb, fk in rows:
    eq = fb == fk
    print(ci, '|', size, '|', mat_order(rep), '|', len(word), '|',
          fb['trace_F3'], fb['order'], fb['fixed_dim'], fb['rank(T-I)'], '|',
          fk['trace_F3'], fk['order'], fk['fixed_dim'], fk['rank(T-I)'], '|', eq)

# Identify precisely which classes separate the two modules under these
# modular fingerprints.
diff = [r for r in rows if r[4] != r[5]]
print()
print('DISTINGUISHING_CLASS_COUNT =', len(diff))
for ci, size, rep, word, fb, fk in diff:
    print('DISTINGUISHING CLASS', ci,
          'size=', size,
          'group_order=', mat_order(rep),
          'word=', word)
    print('  B/A =', fb)
    print('  K   =', fk)

# Explicitly report the five original generators' class membership.
for gi, G in enumerate(Mgens, 1):
    idx = Gmap[key(G)]
    ci = next(c+1 for c, cls in enumerate(classes) if idx in cls)
    print('ORIGINAL_GENERATOR_CLASS', gi, '=', ci, 'order=', mat_order(G))

assert sum(len(c) for c in classes) == 51840
print('RESULT: class-level comparison completed.')
print('NOTE: traces are reported in F_3; this is not being promoted to an ordinary-character classification in defining characteristic.')
print('ALL A3-4-15 CHECKS COMPLETED')
