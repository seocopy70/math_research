import runpy
import numpy as np

P = 3
ROOT = 'research/'


def rank3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    if A.ndim == 1:
        A = A[:, None]
    m, n = A.shape
    r = 0
    for c in range(n):
        q = next((i for i in range(r, m) if A[i, c]), None)
        if q is None:
            continue
        A[[r, q]] = A[[q, r]]
        if A[r, c] == 2:
            A[r] = (2 * A[r]) % P
        for i in range(m):
            if i != r and A[i, c]:
                A[i] = (A[i] - A[i, c] * A[r]) % P
        r += 1
        if r == m:
            break
    return r


def null3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    m, n = A.shape
    R = A.copy()
    piv = []
    r = 0
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
    out = []
    for f in [j for j in range(n) if j not in piv]:
        x = np.zeros(n, dtype=np.int64)
        x[f] = 1
        for rr, c in enumerate(piv):
            x[c] = (-R[rr, f]) % P
        out.append(x)
    return out


def basis_columns(M, target):
    B = np.empty((M.shape[0], 0), dtype=np.int64)
    r = 0
    for j in range(M.shape[1]):
        C = np.column_stack([B, M[:, j]])
        q = rank3(C)
        if q > r:
            B = C
            r = q
            if r == target:
                break
    assert r == target
    return B


def left_inverse(B):
    k = B.shape[1]
    rows = []
    R = np.empty((0, k), dtype=np.int64)
    r = 0
    for i in range(B.shape[0]):
        C = np.vstack([R, B[i:i+1]])
        q = rank3(C)
        if q > r:
            rows.append(i)
            R = C
            r = q
            if r == k:
                break
    assert r == k
    E = np.column_stack([R, np.eye(k, dtype=np.int64)])
    for c in range(k):
        q = next(i for i in range(c, k) if E[i, c])
        E[[c, q]] = E[[q, c]]
        if E[c, c] == 2:
            E[c] = (2 * E[c]) % P
        for i in range(k):
            if i != c and E[i, c]:
                E[i] = (E[i] - E[i, c] * E[c]) % P
    return rows, E[:, k:]


def coords(B, V):
    rows, L = left_inverse(B)
    return (L @ V[rows]) % P


def inv3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    n = A.shape[0]
    assert A.shape == (n, n)
    E = np.column_stack([A, np.eye(n, dtype=np.int64)]) % P
    for c in range(n):
        q = next((i for i in range(c, n) if E[i, c]), None)
        assert q is not None
        E[[c, q]] = E[[q, c]]
        if E[c, c] == 2:
            E[c] = (2 * E[c]) % P
        for i in range(n):
            if i != c and E[i, c]:
                E[i] = (E[i] - E[i, c] * E[c]) % P
    return E[:, n:]


def intertwiner_data(A_src, A_tgt):
    n = A_src[0].shape[0]
    cols = []
    for q in range(n * n):
        Q = np.zeros((n, n), dtype=np.int64)
        Q.flat[q] = 1
        blocks = [((Q @ a - b @ Q) % P).reshape(-1) for a, b in zip(A_src, A_tgt)]
        cols.append(np.concatenate(blocks))
    Sys = np.column_stack(cols)
    nb = null3(Sys)
    max_rank = 0
    full = None
    for x in nb:
        Q = x.reshape((n, n)) % P
        rr = rank3(Q)
        max_rank = max(max_rank, rr)
        if rr == n:
            full = Q
            break
    return len(nb), max_rank, full


def add(A, B):
    C = dict(A)
    for w, a in B.items():
        C[w] = (C.get(w, 0) + a) % P
        if C[w] == 0:
            del C[w]
    return C


def mul(A, B):
    C = {}
    for wa, ca in A.items():
        for wb, cb in B.items():
            w = wa + wb
            C[w] = (C.get(w, 0) + ca * cb) % P
            if C[w] == 0:
                del C[w]
    return C


def neg(A):
    return {w: (-c) % P for w, c in A.items() if c % P}


def bracket(A, B):
    return add(mul(A, B), neg(mul(B, A)))


# Canonical corrected W45 and group action.
ns1 = runpy.run_path(ROOT + 'phase2_1_invariant_space_verification_2026-09-15.py')
ns3 = runpy.run_path(ROOT + 'phase2_3_endH_optimized_2026-09-15.py')
W_words = ns1['basis']
index4 = ns1['index4']
gens = ns1['gens']
apply_linear_map = ns1['apply_linear_map']
A_W = [np.array(a, dtype=np.int64) % P for a in ns1['action_matrices']]
N = np.array(ns3['N'], dtype=np.int64) % P


def vec4(A):
    v = np.zeros(256, dtype=np.int64)
    for w, c in A.items():
        v[index4[w]] = c % P
    return v

W45 = np.column_stack([vec4(a) for a in W_words])
assert W45.shape == (256, 45) and rank3(W45) == 45
assert rank3(N) == 10 and np.array_equal((N @ N) % P, np.zeros_like(N))

# Reconstruct W_d from d and the same Sp4 generators, independently of the old quotient.
d = bracket({(1, 1, 1): 1}, {(2,): 1})
queue = [d]
seen = {tuple(vec4(d).tolist())}
for a in queue:
    for g in gens:
        b = apply_linear_map(a, g)
        key = tuple(vec4(b).tolist())
        if key not in seen:
            seen.add(key)
            queue.append(b)

Wd_raw = np.column_stack([vec4(a) for a in queue])
Wd = basis_columns(Wd_raw, 45)
assert rank3(Wd) == 45

# Ambient intersection I = W45 intersect Wd via the kernel of [W45 | -Wd].
S = np.column_stack([W45, (-Wd) % P]) % P
ker = null3(S)
assert len(ker) == 35
KERNEL = np.column_stack(ker)
I_ambient = (W45 @ KERNEL[:45, :]) % P
assert rank3(I_ambient) == 35
I_coord = coords(W45, I_ambient)
assert I_coord.shape == (45, 35) and rank3(I_coord) == 35

# K is reconstructed as ker(N), then embedded in the same ambient W45 coordinates.
K_coord = np.column_stack(null3(N))
assert K_coord.shape == (45, 35) and rank3(K_coord) == 35
K_ambient = (W45 @ K_coord) % P
assert rank3(K_ambient) == 35

# First test: actual equality of the embedded subspaces I and K.
actual_combined_rank = rank3(np.column_stack([I_ambient, K_ambient]))
actual_equal = actual_combined_rank == 35

# Quotient-level tau: pi|W45 and pi|Wd are isomorphisms onto Q4_true.
# Build an arbitrary but fixed quotient coordinate map by extending the 15D R4 basis
# to a 60D basis of L4.  The last 45 coordinates then give Q4 coordinates.
R3 = [bracket({(i,): 1}, {(1, 2): 1, (2, 1): 2, (3, 4): 1, (4, 3): 2}) for i in range(1, 5)]
R4_raw = [bracket({(i,): 1}, r) for i in range(1, 5) for r in R3]
R4 = basis_columns(np.column_stack([vec4(a) for a in R4_raw]), 15)
L4_std = np.eye(256, dtype=np.int64)
ambient_basis = basis_columns(np.column_stack([R4, L4_std]), 60)
assert ambient_basis.shape == (256, 60) and rank3(ambient_basis) == 60
rows60, L60 = left_inverse(ambient_basis)
# In these coordinates, the first 15 are R4 and the final 45 are quotient coordinates.
C_W45 = (L60 @ W45[rows60]) % P
C_Wd = (L60 @ Wd[rows60]) % P
Q_W45 = C_W45[15:, :]
Q_Wd = C_Wd[15:, :]
assert rank3(Q_W45) == 45
assert rank3(Q_Wd) == 45

tau_coord = (inv3(Q_Wd) @ Q_W45) % P
I_in_W45 = I_coord
I_image_in_Wd = (tau_coord @ I_in_W45) % P
I_fixed_residual = (Wd @ I_image_in_Wd - I_ambient) % P

tau_fixed = np.array_equal(I_fixed_residual, np.zeros_like(I_fixed_residual))
print('tau: Q4 coordinate matrix ranks =', rank3(Q_W45), rank3(Q_Wd))
print('tau|I identity residual rank =', rank3(I_fixed_residual))
print('TAU_RESTRICTED_TO_I_IS_IDENTITY =', tau_fixed)

# Second test: H-module isomorphism I ~= K, allowing different embeddings.
def restricted_actions(Bcoord):
    acts = []
    for A in A_W:
        X = (A @ Bcoord) % P
        C = coords(Bcoord, X)
        assert np.array_equal((Bcoord @ C) % P, X)
        acts.append(C)
    return acts

A_I = restricted_actions(I_coord)
A_K = restricted_actions(K_coord)
hom_dim, max_rank, full_intertwiner = intertwiner_data(A_I, A_K)

print('A3-4 REVALIDATION: I = W45 intersect Wd, with TRUE Wd')
print('orbit size of d =', len(queue))
print('dim W45 =', rank3(W45))
print('dim Wd =', rank3(Wd))
print('rank([W45 | Wd]) =', rank3(np.column_stack([W45, Wd])))
print('dim I =', rank3(I_ambient))
print('dim K =', rank3(K_ambient))
print('rank([I | K]) =', actual_combined_rank)
print('I_EQUALS_K_AS_ACTUAL_AMBIENT_SUBSPACES =', actual_equal)
print('dim Hom_H(I,K) =', hom_dim)
print('maximum intertwiner rank =', max_rank)
print('FULL_RANK_H_MODULE_INTERTWINER_FOUND =', full_intertwiner is not None)

assert rank3(Wd) == 45
assert rank3(np.column_stack([W45, Wd])) == 55
assert rank3(I_ambient) == 35
assert rank3(K_ambient) == 35
assert actual_equal
assert tau_fixed
assert full_intertwiner is not None

print('RESULT: I = K as actual 35-dimensional ambient subspaces.')
print('RESULT: I is also H-module isomorphic to K under the reconstructed TRUE Wd.')
print('RESULT: tau|_I = id_I for the quotient-induced canonical correspondence.')
print('ALL I/K TRUE-Wd + TAU REVALIDATION CHECKS PASSED')
