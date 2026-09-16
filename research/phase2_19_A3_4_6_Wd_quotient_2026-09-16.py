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


def intertwiner_data(A_src, A_tgt):
    n = A_src[0].shape[0]
    cols = []
    for q in range(n*n):
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


# Reuse the already verified A3-4-5 construction.
ns = runpy.run_path(ROOT + 'phase2_18_A3_4_5_intersection_K_and_Sym2_2026-09-16.py')
W = ns['W']
Wd_basis = ns['Wd_basis']
I_W = ns['I_W']
A_W = ns['A_W']
A_WI = ns['A_WI']
A_Sym2 = ns['A_Sym2']

assert W.shape == (256, 45)
assert Wd_basis.shape == (256, 45)
assert I_W.shape == (45, 35)
assert rank3(W) == rank3(Wd_basis) == 45
assert rank3(I_W) == 35

# Build a 10-dimensional quotient basis Wd/I, entirely inside Wd-coordinates.
# First change Wd's 45-coordinate basis so that the first 35 columns span I.
I_ambient = (W @ I_W) % P
I_in_Wd = coords(Wd_basis, I_ambient)
assert I_in_Wd.shape == (45, 35) and rank3(I_in_Wd) == 35

B = I_in_Wd.copy()
Qcols = []
r = rank3(B)
for j in range(45):
    e = np.eye(45, dtype=np.int64)[:, j]
    C = np.column_stack([B, e])
    q = rank3(C)
    if q > r:
        Qcols.append(e)
        B = C
        r = q
        if r == 45:
            break
Q = np.column_stack(Qcols)
assert Q.shape == (45, 10)
S = np.column_stack([I_in_Wd, Q])
assert rank3(S) == 45

# Full Wd action in Wd coordinates.
A_Wd = []
for A in A_W:
    X = (A @ Wd_basis) % P
    C = coords(Wd_basis, X)
    assert np.array_equal((Wd_basis @ C) % P, X)
    A_Wd.append(C)

# Induced quotient action on Wd/I.
rows, Linv = left_inverse(S)
A_WdI = []
for A in A_Wd:
    AQ = (A @ Q) % P
    C = (Linv @ AQ[rows]) % P
    assert np.array_equal((S @ C) % P, AQ)
    A_WdI.append(C[35:, :])
assert all(rank3(a) == 10 for a in A_WdI)

hom_d, maxrank_d, P_d = intertwiner_data(A_WdI, A_Sym2)
hom_cross, maxrank_cross, P_cross = intertwiner_data(A_WdI, A_WI)

print('PHASE 2-19 / A3-4-6 Wd/I QUOTIENT IDENTIFICATION')
print('dim W45 =', rank3(W))
print('dim Wd =', rank3(Wd_basis))
print('dim I =', rank3(I_W))
print('dim(Wd/I) =', 10)
print()
print('TEST 1: Wd/I ~= Sym^2(V)')
print('dim Hom_H(Wd/I, Sym^2(V)) =', hom_d)
print('maximum intertwiner rank =', maxrank_d)
print('FULL_RANK_INTERTWINER_FOUND =', P_d is not None)
print()
print('TEST 2: Wd/I ~= W45/I')
print('dim Hom_H(Wd/I, W45/I) =', hom_cross)
print('maximum intertwiner rank =', maxrank_cross)
print('FULL_RANK_INTERTWINER_FOUND =', P_cross is not None)
print()
print('CERTIFICATES')
print('WD_OVER_I_EQUALS_SYM2 =', P_d is not None)
print('WD_OVER_I_EQUALS_W45_OVER_I =', P_cross is not None)

assert P_d is not None
assert P_cross is not None
print('ALL A3-4-6 TESTS PASSED')
