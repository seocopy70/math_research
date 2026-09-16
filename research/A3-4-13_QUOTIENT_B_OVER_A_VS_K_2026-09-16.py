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
    R = A.copy(); piv = []; r = 0
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
        piv.append(c); r += 1
        if r == m:
            break
    out = []
    for f in [j for j in range(n) if j not in piv]:
        x = np.zeros(n, dtype=np.int64); x[f] = 1
        for rr, c in enumerate(piv):
            x[c] = (-R[rr, f]) % P
        out.append(x)
    return out


def left_inverse(B):
    B = np.array(B, dtype=np.int64) % P
    k = B.shape[1]
    rows = []; R = np.empty((0, k), dtype=np.int64); r = 0
    for i in range(B.shape[0]):
        C = np.vstack([R, B[i:i+1]])
        q = rank3(C)
        if q > r:
            rows.append(i); R = C; r = q
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
    return (L @ np.array(V, dtype=np.int64)[rows]) % P


def independent_columns(M, target=None):
    M = np.array(M, dtype=np.int64) % P
    B = np.empty((M.shape[0], 0), dtype=np.int64); r = 0; idx = []
    for j in range(M.shape[1]):
        C = np.column_stack([B, M[:, j]])
        q = rank3(C)
        if q > r:
            B = C; r = q; idx.append(j)
            if target is not None and r == target:
                break
    if target is not None:
        assert r == target
    return idx, B


def intertwiner_data(A_src, A_tgt):
    n = A_src[0].shape[0]
    cols = []
    for q in range(n*n):
        Q = np.zeros((n, n), dtype=np.int64); Q.flat[q] = 1
        blocks = [((Q @ a - b @ Q) % P).reshape(-1)
                  for a, b in zip(A_src, A_tgt)]
        cols.append(np.concatenate(blocks))
    Sys = np.column_stack(cols)
    nb = null3(Sys)
    max_rank = 0; full = None
    for x in nb:
        Q = x.reshape((n, n)) % P
        rr = rank3(Q); max_rank = max(max_rank, rr)
        if rr == n:
            full = Q; break
    return len(nb), max_rank, full


# Verified A3-4-10 infrastructure: W, I=K data, H-action, Delta_tau.
ns = runpy.run_path(ROOT + 'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
W = np.array(ns['W'], dtype=np.int64) % P
I_W = np.array(ns['I_W'], dtype=np.int64) % P
K_coord = np.array(ns['K_coord'], dtype=np.int64) % P
A_W = [np.array(a, dtype=np.int64) % P for a in ns['A_W']]
D_tau = np.vstack([np.array(d, dtype=np.int64) % P for d in ns['diffs']])

# Verified A3-4-12 control map Delta_u.
ns12 = runpy.run_path(ROOT + 'A3-4-12_IMAGE_INTERSECTION_DELTA_U_DELTA_TAU_2026-09-16.py')
D_u = np.array(ns12['D_u'], dtype=np.int64) % P

assert W.shape == (256, 45)
assert I_W.shape == (45, 35)
assert K_coord.shape == (45, 35)
assert D_tau.shape == (4096, 45)
assert D_u.shape == (4096, 45)
assert rank3(D_tau) == 45
assert rank3(D_u) == 10
assert rank3(np.column_stack([D_tau, D_u])) == 45

# ------------------------------------------------------------------
# Step 1: construct B/A explicitly.
# A = Im Delta_u, B = Im Delta_tau.
# ------------------------------------------------------------------
idxA, A_basis = independent_columns(D_u, 10)
Q_idx = []
C = A_basis.copy(); r = 10
for j in range(45):
    T = np.column_stack([C, D_tau[:, j]])
    rr = rank3(T)
    if rr > r:
        C = T; r = rr; Q_idx.append(j)
        if r == 45:
            break
assert len(Q_idx) == 35
B_over_A_basis = D_tau[:, Q_idx]
assert rank3(np.column_stack([A_basis, B_over_A_basis])) == 45

C_rows, C_L = left_inverse(C)

def quotient_coords(V):
    V = np.array(V, dtype=np.int64) % P
    full = (C_L @ V[C_rows]) % P
    # first 10 coordinates are the A-component; last 35 are B/A coordinates
    return full[10:]

# ------------------------------------------------------------------
# Step 2: induce the H-action on B/A directly from Delta_tau.
# Since X is H-equivariant, Delta_tau is H-equivariant. Thus
# Delta_tau(gw) = rho(g) Delta_tau(w), and D_tau @ A_g gives the
# transformed obstruction vectors without constructing a 4096x4096
# ambient Hom(V,L5) action matrix.
# ------------------------------------------------------------------
A_Bquot = []
for Ag in A_W:
    Y = (D_tau @ Ag[:, Q_idx]) % P
    Zfull = (C_L @ Y[C_rows]) % P
    recon = (C @ Zfull) % P
    assert np.array_equal(recon, Y)
    A_Bquot.append(Zfull[10:, :] % P)
assert all(a.shape == (35, 35) and rank3(a) == 35 for a in A_Bquot)

# ------------------------------------------------------------------
# Step 3: H-action on K=I. A3-4-12.5b established I=K as actual
# ambient subspaces, so K_coord is an ambient basis for the same space.
# ------------------------------------------------------------------
A_K = []
for A in A_W:
    Y = (A @ K_coord) % P
    c = coords(K_coord, Y)
    assert np.array_equal((K_coord @ c) % P, Y)
    A_K.append(c)
assert all(a.shape == (35, 35) and rank3(a) == 35 for a in A_K)

# ------------------------------------------------------------------
# Step 4: actual H-module comparison B/A versus K.
# This is an abstract module isomorphism test; B/A lives in the
# quotient of Hom(V,L5), whereas K lies inside W45.
# ------------------------------------------------------------------
hom_dim, max_rank, P_BA_K = intertwiner_data(A_Bquot, A_K)
FULL_RANK_INTERTWINER = P_BA_K is not None and rank3(P_BA_K) == 35

# Independent ambient equality check I=K.
assert rank3(I_W) == 35 and rank3(K_coord) == 35
assert rank3(np.column_stack([I_W, K_coord])) == 35

print('A3-4-13 / B/A VS K H-MODULE COMPARISON')
print('ambient Hom(V,L5) dimension =', 4096)
print('dim B = rank Delta_tau =', rank3(D_tau))
print('dim A = rank Delta_u =', rank3(D_u))
print('dim(B+A) =', rank3(np.column_stack([D_tau, D_u])))
print('dim(B/A) =', len(Q_idx))
print('dim K =', rank3(K_coord))
print('I = K ambient check =', rank3(np.column_stack([I_W, K_coord])) == 35)
print('number of B/A quotient representatives =', len(Q_idx))
print('dim Hom_H(B/A,K) =', hom_dim)
print('maximum intertwiner rank =', max_rank)
print('FULL_RANK_INTERTWINER_FOUND =', FULL_RANK_INTERTWINER)

if FULL_RANK_INTERTWINER:
    print('RESULT: B/A is H-isomorphic to K=I.')
else:
    print('RESULT: B/A is NOT H-isomorphic to K by the computed intertwiner test.')

assert len(Q_idx) == 35
assert FULL_RANK_INTERTWINER
print('ALL A3-4-13 CHECKS COMPLETED')
