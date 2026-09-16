import runpy
import numpy as np

P = 3
ROOT = 'research/'


def rank3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    if A.ndim == 1: A = A[:, None]
    m, n = A.shape; r = 0
    for c in range(n):
        q = next((i for i in range(r, m) if A[i, c]), None)
        if q is None: continue
        A[[r, q]] = A[[q, r]]
        if A[r, c] == 2: A[r] = (2 * A[r]) % P
        for i in range(m):
            if i != r and A[i, c]: A[i] = (A[i] - A[i, c] * A[r]) % P
        r += 1
        if r == m: break
    return r


def null3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    m, n = A.shape; R = A.copy(); piv = []; r = 0
    for c in range(n):
        q = next((i for i in range(r, m) if R[i, c]), None)
        if q is None: continue
        R[[r, q]] = R[[q, r]]
        if R[r, c] == 2: R[r] = (2 * R[r]) % P
        for i in range(m):
            if i != r and R[i, c]: R[i] = (R[i] - R[i, c] * R[r]) % P
        piv.append(c); r += 1
        if r == m: break
    out = []
    for f in [j for j in range(n) if j not in piv]:
        x = np.zeros(n, dtype=np.int64); x[f] = 1
        for rr, c in enumerate(piv): x[c] = (-R[rr, f]) % P
        out.append(x)
    return out


def basis_columns(M, target):
    B = np.empty((M.shape[0], 0), dtype=np.int64); r = 0
    for j in range(M.shape[1]):
        C = np.column_stack([B, M[:, j]])
        q = rank3(C)
        if q > r:
            B = C; r = q
            if r == target: break
    assert r == target
    return B


def left_inverse(B):
    k = B.shape[1]; rows = []; R = np.empty((0, k), dtype=np.int64); r = 0
    for i in range(B.shape[0]):
        C = np.vstack([R, B[i:i+1]])
        q = rank3(C)
        if q > r:
            rows.append(i); R = C; r = q
            if r == k: break
    assert r == k
    E = np.column_stack([R, np.eye(k, dtype=np.int64)])
    for c in range(k):
        q = next(i for i in range(c, k) if E[i, c])
        E[[c, q]] = E[[q, c]]
        if E[c, c] == 2: E[c] = (2 * E[c]) % P
        for i in range(k):
            if i != c and E[i, c]: E[i] = (E[i] - E[i, c] * E[c]) % P
    return rows, E[:, k:]


def coords(B, V):
    rows, L = left_inverse(B)
    return (L @ V[rows]) % P


def intertwiner_data(A_src, A_tgt):
    n = A_src[0].shape[0]; cols = []
    for q in range(n * n):
        Q = np.zeros((n, n), dtype=np.int64); Q.flat[q] = 1
        blocks = [((Q @ a - b @ Q) % P).reshape(-1) for a, b in zip(A_src, A_tgt)]
        cols.append(np.concatenate(blocks))
    Sys = np.column_stack(cols); nb = null3(Sys); max_rank = 0; full = None
    for x in nb:
        Q = x.reshape((n, n)) % P; rr = rank3(Q); max_rank = max(max_rank, rr)
        if rr == n: full = Q; break
    return len(nb), max_rank, full


# Exact canonical infrastructure.
ns1 = runpy.run_path(ROOT + 'phase2_1_invariant_space_verification_2026-09-15.py')
ns3 = runpy.run_path(ROOT + 'phase2_3_endH_optimized_2026-09-15.py')
W_words = ns1['basis']; index4 = ns1['index4']; gens = ns1['gens']; apply_linear_map = ns1['apply_linear_map']
A_W = [np.array(a, dtype=np.int64) % P for a in ns1['action_matrices']]
N = np.array(ns3['N'], dtype=np.int64) % P


def vec4(A):
    v = np.zeros(256, dtype=np.int64)
    for w, c in A.items(): v[index4[w]] = c % P
    return v

W = np.column_stack([vec4(a) for a in W_words])
assert W.shape == (256, 45) and rank3(W) == 45
assert rank3(N) == 10 and np.array_equal((N @ N) % P, np.zeros_like(N))

# d and its full Sp4 orbit.
def add(A, B):
    C = dict(A)
    for w, a in B.items():
        C[w] = (C.get(w, 0) + a) % P
        if C[w] == 0: del C[w]
    return C

def mul(A, B):
    C = {}
    for wa, ca in A.items():
        for wb, cb in B.items():
            w = wa + wb; C[w] = (C.get(w, 0) + ca * cb) % P
            if C[w] == 0: del C[w]
    return C

def neg(A): return {w: (-c) % P for w, c in A.items() if c % P}
def bracket(A, B): return add(mul(A, B), neg(mul(B, A)))

d = bracket({(1, 1, 1): 1}, {(2,): 1})
queue = [d]; seen = {tuple(vec4(d).tolist())}
for a in queue:
    for g in gens:
        b = apply_linear_map(a, g); key = tuple(vec4(b).tolist())
        if key not in seen: seen.add(key); queue.append(b)
Wd = np.column_stack([vec4(a) for a in queue])
Wd_basis = basis_columns(Wd, 45)
assert len(queue) == 360 and rank3(Wd_basis) == 45
assert rank3(np.column_stack([W, Wd_basis])) == 55

# I = W45 intersect Wd. Use an independent 45-column basis of Wd, not all 360 orbit vectors.
S = np.column_stack([W, (-Wd_basis) % P]) % P
ker = null3(S)
assert len(ker) == 35
I_ambient = (W @ np.column_stack(ker)[:, :45]) % P
assert rank3(I_ambient) == 35
I_W = coords(W, I_ambient)
assert I_W.shape == (45, 35) and rank3(I_W) == 35

# K = ker(N) inside W-coordinate module.
K_coord = np.column_stack(null3(N))
assert K_coord.shape == (45, 35) and rank3(K_coord) == 35


def restricted_actions(Bcoord):
    acts = []
    for A in A_W:
        X = (A @ Bcoord) % P; C = coords(Bcoord, X)
        assert np.array_equal((Bcoord @ C) % P, X); acts.append(C)
    return acts

A_K = restricted_actions(K_coord)
A_I = restricted_actions(I_W)
hom_KI, maxrank_KI, P_KI = intertwiner_data(A_K, A_I)

# Quotient W/I, dimension 10.
B = I_W.copy(); Qcols = []; r = rank3(B)
for j in range(45):
    e = np.eye(45, dtype=np.int64)[:, j]; C = np.column_stack([B, e]); q = rank3(C)
    if q > r:
        Qcols.append(e); B = C; r = q
        if r == 45: break
Q = np.column_stack(Qcols); assert Q.shape == (45, 10)
S_WI = np.column_stack([I_W, Q]); assert rank3(S_WI) == 45
rows, Linv = left_inverse(S_WI)
A_WI = []
for A in A_W:
    AQ = (A @ Q) % P; C = (Linv @ AQ[rows]) % P
    assert np.array_equal((S_WI @ C) % P, AQ); A_WI.append(C[35:, :])
assert all(rank3(a) == 10 for a in A_WI)

# Sym^2(V) reference under the same five natural generators.
J = np.array([[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]], dtype=np.int64) % P
vecs = [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(1,0,1,0)]
G = [(np.eye(4, dtype=np.int64) + np.outer(np.array(v, dtype=np.int64), (J @ np.array(v, dtype=np.int64)) % P)) % P for v in vecs]
pairs = [(0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]; pi = {p:i for i,p in enumerate(pairs)}
def sym2_matrix(g):
    M = np.zeros((10,10), dtype=np.int64)
    for c,(i,j) in enumerate(pairs):
        for a in range(4):
            for b in range(4):
                z = int(g[a,i]) * int(g[b,j])
                if z:
                    p = (a,b) if a <= b else (b,a); M[pi[p],c] = (M[pi[p],c] + z) % P
    return M
A_Sym2 = [sym2_matrix(g) for g in G]
hom_Q, maxrank_Q, P_Q = intertwiner_data(A_WI, A_Sym2)

print('PHASE 2-18 / A3-4-5 INTERSECTION IDENTIFICATION')
print('dim W45 =', rank3(W)); print('dim Wd =', rank3(Wd_basis)); print('orbit size of d =', len(queue))
print('dim I = dim(W45 intersect Wd) =', rank3(I_W)); print('dim K = dim ker(N) =', rank3(K_coord)); print('rank([W45 | Wd]) =', rank3(np.column_stack([W, Wd_basis])))
print(); print('TEST 1: I ~= K'); print('dim Hom_H(K,I) =', hom_KI); print('maximum intertwiner rank =', maxrank_KI); print('FULL_RANK_INTERTWINER_FOUND =', P_KI is not None)
print(); print('TEST 2: W45/I ~= Sym^2(V)'); print('dim(W45/I) =', 10); print('dim Hom_H(W45/I, Sym^2(V)) =', hom_Q); print('maximum intertwiner rank =', maxrank_Q); print('FULL_RANK_INTERTWINER_FOUND =', P_Q is not None)
print(); print('CERTIFICATES'); print('I_EQUALS_K_UP_TO_H_MODULE_ISOMORPHISM =', P_KI is not None); print('W45_OVER_I_EQUALS_SYM2 =', P_Q is not None)
assert P_KI is not None
assert P_Q is not None
print('ALL A3-4-5 HYPOTHESIS TESTS PASSED')
