import runpy
import numpy as np

P = 3
ROOT = 'research/'

# Reuse the verified A3-4-5 construction.
# It exposes W45, Wd_basis, I_W, K_coord and generator action machinery.
ns = runpy.run_path(ROOT + 'phase2_18_A3_4_5_intersection_K_and_Sym2_2026-09-16.py')
rank3 = ns['rank3']
W = np.array(ns['W'], dtype=np.int64) % P
Wd = np.array(ns['Wd_basis'], dtype=np.int64) % P
I_W = np.array(ns['I_W'], dtype=np.int64) % P
K_coord = np.array(ns['K_coord'], dtype=np.int64) % P

# Recover generator action matrices from the same verified construction.
# The script stores the five generator actions on W and Wd through A_list / Ad_list
# when available.  If names differ, fail loudly rather than silently changing the test.
A_list = ns.get('A_list')
Ad_list = ns.get('Ad_list')
if A_list is None or Ad_list is None:
    raise RuntimeError('A3-4-5 script must expose A_list and Ad_list for A3-4-9.')
A_list = [np.array(A, dtype=np.int64) % P for A in A_list]
Ad_list = [np.array(A, dtype=np.int64) % P for A in Ad_list]

assert W.shape == (256, 45)
assert Wd.shape == (256, 45)
assert I_W.shape == (45, 35)
assert K_coord.shape == (45, 35)
assert len(A_list) == len(Ad_list) == 5

# Because A3-4-8 established I = K as actual ambient subspaces, express the
# common 35-dimensional subspace in Wd coordinates.
K_ambient = (W @ K_coord) % P
# Solve Wd * K_Wd = K_ambient over F3, column by column.
def solve_full_col(A, b):
    A = A.copy() % P
    b = b.copy() % P
    M = np.column_stack([A, b])
    m, n = A.shape
    row = 0
    pivots = []
    for col in range(n):
        piv = next((r for r in range(row, m) if M[r, col] % P != 0), None)
        if piv is None:
            continue
        M[[row, piv]] = M[[piv, row]]
        inv = pow(int(M[row, col]), -1, P)
        M[row] = (M[row] * inv) % P
        for r in range(m):
            if r != row and M[r, col] % P != 0:
                M[r] = (M[r] - M[r, col] * M[row]) % P
        pivots.append(col)
        row += 1
        if row == m:
            break
    if len(pivots) < n:
        raise RuntimeError('Coordinate solve failed: Wd basis rank is not 45.')
    if np.any(M[:, n] != 0):
        raise RuntimeError('Common K basis is not contained in Wd.')
    x = np.zeros(n, dtype=np.int64)
    for r, c in enumerate(pivots):
        x[c] = M[r, n]
    return x

K_Wd = np.column_stack([solve_full_col(Wd, K_ambient[:, j]) for j in range(35)]) % P
assert rank3((Wd @ K_Wd) % P - K_ambient) == 0

# A3-4-9 asks whether the two exact sequences are equivalent with the
# common submodule K fixed pointwise.  Seek Pmap: W45 -> Wd such that
#   Ad_i Pmap = Pmap A_i   for all generators,
#   Pmap I_W = K_Wd       (identity on the actual common K).
# This is a linear system over F3 in 45^2 unknowns.

n = 45
num_unknowns = n * n
rows = []
rhs = []

def var_index(r, c):
    return r * n + c

# Kronecker-free equation construction: each scalar equation is generated
# directly from (Ad_i X - X A_i)_{r,c}=0.
for A, Ad in zip(A_list, Ad_list):
    for r in range(n):
        for c in range(n):
            row_vec = np.zeros(num_unknowns, dtype=np.int64)
            # (Ad X)_{r,c} = sum_k Ad[r,k] X[k,c]
            for k in range(n):
                coeff = int(Ad[r, k]) % P
                if coeff:
                    row_vec[var_index(k, c)] = (row_vec[var_index(k, c)] + coeff) % P
            # -(X A)_{r,c} = -sum_k X[r,k] A[k,c]
            for k in range(n):
                coeff = int(A[k, c]) % P
                if coeff:
                    row_vec[var_index(r, k)] = (row_vec[var_index(r, k)] - coeff) % P
            rows.append(row_vec)
            rhs.append(0)

# Restriction-to-K equations: X I_W = K_Wd.
for r in range(n):
    for c in range(35):
        row_vec = np.zeros(num_unknowns, dtype=np.int64)
        for k in range(n):
            coeff = int(I_W[k, c]) % P
            if coeff:
                row_vec[var_index(r, k)] = (row_vec[var_index(r, k)] + coeff) % P
        rows.append(row_vec)
        rhs.append(int(K_Wd[r, c]) % P)

M = np.array(rows, dtype=np.int64) % P
b = np.array(rhs, dtype=np.int64) % P

# Gaussian elimination over F3, returning rank and one solution if consistent.
def rref_solve(A, b):
    M = np.column_stack([A % P, b.reshape(-1, 1) % P])
    m, n_aug = M.shape
    n = n_aug - 1
    row = 0
    pivots = []
    for col in range(n):
        piv = next((r for r in range(row, m) if M[r, col] % P != 0), None)
        if piv is None:
            continue
        M[[row, piv]] = M[[piv, row]]
        inv = pow(int(M[row, col]), -1, P)
        M[row] = (M[row] * inv) % P
        for r in range(m):
            if r != row and M[r, col] % P != 0:
                M[r] = (M[r] - M[r, col] * M[row]) % P
        pivots.append(col)
        row += 1
        if row == m:
            break
    inconsistent = any(np.all(M[r, :n] % P == 0) and M[r, n] % P != 0 for r in range(row, m))
    if inconsistent:
        return len(pivots), None, n - len(pivots)
    x = np.zeros(n, dtype=np.int64)
    for rr, cc in enumerate(pivots):
        x[cc] = M[rr, n]
    return len(pivots), x, n - len(pivots)

rank_system, sol, nullity_system = rref_solve(M, b)

print('PHASE 2-22 / A3-4-9 EXTENSION EQUIVALENCE')
print('dim W45 =', rank3(W))
print('dim Wd =', rank3(Wd))
print('dim common K =', rank3(K_ambient))
print('system rows =', M.shape[0])
print('system unknowns =', M.shape[1])
print('rank of homogeneous/equivalence system =', rank_system)
print('solution nullity =', nullity_system)
print('EXTENSION_ISOMORPHISM_FIXING_K_EXISTS =', sol is not None)

if sol is not None:
    X = sol.reshape((n, n)) % P
    print('rank(extension intertwiner) =', rank3(X))
    print('RESTRICTION_TO_K_CHECK =', np.array_equal((X @ I_W) % P, K_Wd % P))
    for A, Ad in zip(A_list, Ad_list):
        print('GENERATOR_INTERTWINING_CHECK =', np.array_equal((Ad @ X) % P, (X @ A) % P))
    assert rank3(X) == 45
    assert np.array_equal((X @ I_W) % P, K_Wd % P)
    assert all(np.array_equal((Ad @ X) % P, (X @ A) % P) for A, Ad in zip(A_list, Ad_list))
    print('RESULT: the two extensions are equivalent via an H-isomorphism fixing K pointwise.')
else:
    print('RESULT: no H-isomorphism W45 -> Wd fixing the common K pointwise exists.')

print('ALL A3-4-9 CHECKS COMPLETED')
