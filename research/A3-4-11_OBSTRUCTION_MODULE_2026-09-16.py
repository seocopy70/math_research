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


def independent_columns(M):
    M = np.array(M, dtype=np.int64) % P
    selected = []
    current = np.empty((M.shape[0], 0), dtype=np.int64)
    r = 0
    for j in range(M.shape[1]):
        C = np.column_stack([current, M[:, j]])
        nr = rank3(C)
        if nr > r:
            selected.append(j)
            current = C
            r = nr
    return selected, current


def left_inverse(B):
    B = np.array(B, dtype=np.int64) % P
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
    E = np.concatenate([R.copy(), np.eye(k, dtype=np.int64)], axis=1) % P
    for c in range(k):
        q = next(i for i in range(c, k) if E[i, c])
        E[[c, q]] = E[[q, c]]
        if E[c, c] == 2:
            E[c] = (2 * E[c]) % P
        for i in range(k):
            if i != c and E[i, c]:
                E[i] = (E[i] - E[i, c] * E[c]) % P
    assert np.array_equal(E[:, :k], np.eye(k, dtype=np.int64))
    return E[:, k:]


# Corrected A3-4-11 provides the true R5 basis, the L5 basis, Delta in
# Hom(V,L5), and the degree-5 action on L5.
ns = runpy.run_path(ROOT + 'A3-4-11_TRUE_R5_INTERSECTION_2026-09-16.py')
D_L5 = np.array(ns['D_L5'], dtype=np.int64) % P
R5_basis = np.array(ns['R5_basis'], dtype=np.int64) % P
A5 = [np.array(A, dtype=np.int64) % P for A in ns['A5']]
gens = [np.array(g, dtype=np.int64) % P for g in ns['gens']]

assert D_L5.shape == (816, 45)
assert R5_basis.shape == (204, 60)
assert all(A.shape == (204, 204) for A in A5)
assert all(g.shape == (4, 4) for g in gens)

# H acts on Hom(V,L5) by conjugation:
#       h.f = rho_5(h) f rho_V(h)^(-1).
# With stacked blocks f(e_1),...,f(e_4), the matrix is
#       rho_V(h)^(-T) \otimes rho_5(h).
# This is the correct action; it is NOT merely I_4 \otimes rho_5(h).
I4 = np.eye(4, dtype=np.int64)
A_Hom = []
for G, A in zip(gens, A5):
    # Inverse over F3; for a symplectic matrix G^{-T} = J G J^{-1},
    # but use Gauss-Jordan directly to avoid assuming a coordinate identity.
    M = np.concatenate([G.copy(), I4], axis=1) % P
    r = 0
    for c in range(4):
        q = next(i for i in range(r, 4) if M[i, c])
        M[[r, q]] = M[[q, r]]
        if M[r, c] == 2:
            M[r] = (2 * M[r]) % P
        for i in range(4):
            if i != r and M[i, c]:
                M[i] = (M[i] - M[i, c] * M[r]) % P
        r += 1
    Ginv = M[:, 4:] % P
    A_Hom.append(np.kron(Ginv.T, A) % P)

# True Hom(V,R5), dimension 4*60 = 240.
R5_4 = np.zeros((816, 240), dtype=np.int64)
for i in range(4):
    R5_4[i*204:(i+1)*204, i*60:(i+1)*60] = R5_basis
assert rank3(R5_4) == 240

# Extend the relation space to an ambient basis.  The quotient coordinates
# are the final 576 coordinates in this basis.
_, R5_rows_left = left_inverse(R5_4)
# Build a complement by greedily adjoining standard basis vectors.
_, Eextra = independent_columns(np.column_stack([R5_4, np.eye(816, dtype=np.int64)]))
# independent_columns returns a basis but not its indices, so reconstruct the
# complement explicitly by scanning standard basis columns.
Qcols = []
current = R5_4.copy()
r = 240
for j in range(816):
    e = np.eye(816, dtype=np.int64)[:, j:j+1]
    nr = rank3(np.column_stack([current, e]))
    if nr > r:
        Qcols.append(j)
        current = np.column_stack([current, e])
        r = nr
        if r == 816:
            break
assert len(Qcols) == 576
Qbasis = np.eye(816, dtype=np.int64)[:, Qcols]
E = np.column_stack([R5_4, Qbasis]) % P
assert rank3(E) == 816
E_inv = left_inverse(E)
assert np.array_equal((E_inv @ E) % P, np.eye(816, dtype=np.int64))

# Quotient action and projected obstruction.
Q_actions = []
for AH in A_Hom:
    M = (E_inv @ AH @ E) % P
    # R5 is H-stable, so the quotient is represented by the lower-right block.
    Q_actions.append(M[240:, 240:] % P)

D_Q = (E_inv[240:, :] @ D_L5) % P
assert D_Q.shape == (576, 45)
assert rank3(D_Q) == 45

# The obstruction image O is H-stable in Q5^4.
_, O_basis = independent_columns(D_Q)
assert O_basis.shape == (576, 45)
O_left = left_inverse(O_basis)
O_actions = []
O_defects = []
for AQ in Q_actions:
    Y = (AQ @ O_basis) % P
    assert rank3(np.column_stack([O_basis, Y])) == 45
    AO = (O_left @ Y) % P
    assert np.array_equal((O_basis @ AO) % P, Y)
    O_actions.append(AO)
    O_defects.append(0)

# End_H(O).  This independently checks the module type seen by the
# obstruction, rather than assuming it from Delta's construction.
I45 = np.eye(45, dtype=np.int64)
EQ = []
for AO in O_actions:
    EQ.append((np.kron(I45, AO) - np.kron(AO.T, I45)) % P)
EQ = np.vstack(EQ) % P
rank_End = rank3(EQ)
null_End = 2025 - rank_End
assert null_End == 2

# Recover a non-scalar square-zero endomorphism N in End_H(O) and record its
# radical dimensions.  We find it by taking any non-identity element in the
# 2D nullspace through RREF and testing the two affine combinations.
def rref_nullspace(A):
    R = np.array(A, dtype=np.int64, copy=True) % P
    m, n = R.shape
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
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        x = np.zeros(n, dtype=np.int64)
        x[f] = 1
        for rr, c in enumerate(piv):
            x[c] = (-R[rr, f]) % P
        basis.append(x)
    return basis

null_basis = rref_nullspace(EQ)
assert len(null_basis) == 2
Ivec = I45.reshape(-1)
# Choose a null vector independent of identity; then normalize by trying it and
# its two affine shifts.  It is enough to test square-zero and nonzero rank.
N = None
for v in null_basis:
    X = v.reshape((45, 45)) % P
    if np.array_equal(X, I45):
        continue
    for a in (1, 2):
        Y = (X - a * I45) % P
        if rank3(Y) < 45 and np.array_equal((Y @ Y) % P, np.zeros((45,45), dtype=np.int64)):
            N = Y
            break
    if N is not None:
        break
assert N is not None
rank_N = rank3(N)
null_N = 45 - rank_N
assert rank_N == 10 and null_N == 35

print('PHASE A3-4-11 / OBSTRUCTION MODULE IN TRUE Q5')
print('dim Hom(V,L5) =', 816)
print('dim Hom(V,(R)_5) =', 240)
print('dim Hom(V,L5/(R)_5) =', 576)
print('obstruction rank in quotient =', rank3(D_Q))
print('obstruction H-stability defects =', O_defects)
print('dim End_H(obstruction) =', null_End)
print('non-scalar square-zero N rank =', rank_N)
print('dim ker(N) =', null_N)
print('N^2 =', np.array_equal((N @ N) % P, np.zeros((45,45), dtype=np.int64)))
print('RESULT: obstruction is a 45-dimensional H-submodule of Q5^4 with the same verified End_H/N structure as W45.')
print('ALL A3-4-11 OBSTRUCTION MODULE CHECKS PASSED')
