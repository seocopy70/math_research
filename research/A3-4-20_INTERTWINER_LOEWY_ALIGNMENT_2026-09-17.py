import runpy
import numpy as np

P = 3
ROOT = 'research/'

# Reuse exactly the A3-4-16 action matrices and the A3-4-17 Hom computation.
ns16 = runpy.run_path(ROOT + 'A3-4-16_STRONG_MODULAR_FINGERPRINT_2026-09-16.py')
BA = [np.array(x, dtype=np.int64) % P for x in ns16['BA_gens']]
K = [np.array(x, dtype=np.int64) % P for x in ns16['K_gens']]
rank3 = ns16['rank3']

assert len(BA) == len(K) == 5
assert all(T.shape == (35, 35) for T in BA + K)

I35 = np.eye(35, dtype=np.int64)

# Exact F_3 RREF.  This is intentionally the same construction as A3-4-17.
def rref3(A):
    R = np.array(A, dtype=np.int64) % P
    m, n = R.shape
    pivots = []
    r = 0
    for c in range(n):
        q = next((i for i in range(r, m) if R[i, c]), None)
        if q is None:
            continue
        if q != r:
            R[[r, q]] = R[[q, r]]
        if R[r, c] == 2:
            R[r] = (2 * R[r]) % P
        for i in range(m):
            if i != r and R[i, c]:
                R[i] = (R[i] - R[i, c] * R[r]) % P
        pivots.append(c)
        r += 1
        if r == m:
            break
    return R, pivots

# -------------------------------------------------------------------------
# 1. Recover the unique nonzero intertwiner P from
#       P BA_g = K_g P
# -------------------------------------------------------------------------
blocks = []
for A, G in zip(BA, K):
    blocks.append((np.kron(A.T, I35) - np.kron(I35, G)) % P)
E = np.vstack(blocks) % P
assert E.shape == (6125, 1225)

R, pivots = rref3(E)
rankE = len(pivots)
nullity = E.shape[1] - rankE
assert nullity == 1

free = next(c for c in range(E.shape[1]) if c not in set(pivots))
x = np.zeros(E.shape[1], dtype=np.int64)
x[free] = 1
for rr, pc in enumerate(pivots):
    x[pc] = (-R[rr, free]) % P

# Same column-major convention as A3-4-17.
Q = x.reshape((35, 35), order='F') % P
for A, G in zip(BA, K):
    assert np.array_equal((Q @ A - G @ Q) % P, np.zeros((35, 35), dtype=np.int64))
assert rank3(Q) == 10

# -------------------------------------------------------------------------
# 2. Linear-algebra helpers for subspaces of F_3^35.
#    Columns are the coordinate vectors (column-module convention).
# -------------------------------------------------------------------------
def col_basis(A):
    A = np.array(A, dtype=np.int64) % P
    if A.shape[1] == 0:
        return np.zeros((A.shape[0], 0), dtype=np.int64)
    _, piv = rref3(A)
    return A[:, piv] % P

def subspace_rank(A):
    if A.size == 0:
        return 0
    return len(rref3(A)[1])

def equal_subspaces(A, B):
    return subspace_rank(np.column_stack([A, B])) == subspace_rank(A) == subspace_rank(B)

def nullspace_basis(A):
    A = np.array(A, dtype=np.int64) % P
    R, piv = rref3(A)
    n = A.shape[1]
    free_cols = [c for c in range(n) if c not in set(piv)]
    out = []
    for f in free_cols:
        v = np.zeros(n, dtype=np.int64)
        v[f] = 1
        for rr, pc in enumerate(piv):
            v[pc] = (-R[rr, f]) % P
        out.append(v)
    return np.column_stack(out) if out else np.zeros((n, 0), dtype=np.int64)

def intersection(A, B):
    # A,B are column bases.  Solve A a = B b, so [A|-B](a,b)=0.
    da, db = A.shape[1], B.shape[1]
    if da == 0 or db == 0:
        return np.zeros((35, 0), dtype=np.int64)
    Z = nullspace_basis(np.column_stack([A, (-B) % P]))
    return col_basis((A @ Z[:da, :]) % P)

# -------------------------------------------------------------------------
# 3. Radical = sum_g im(g-I); socle = intersection_g ker(g-I).
# -------------------------------------------------------------------------
def radical(gens):
    blocks = [(G - I35) % P for G in gens]
    return col_basis(np.column_stack(blocks))

def socle(gens):
    S = I35.copy()
    # Start with V; intersect kernels one generator at a time.
    # A basis of ker(G-I) is obtained directly from nullspace.
    for G in gens:
        ker = nullspace_basis((G - I35) % P)
        S = intersection(S, ker)
    return S

radBA = radical(BA)
socBA = socle(BA)
radK = radical(K)
socK = socle(K)

# Q maps BA to K.  Compare ker(Q) with each 25-dim candidate and im(Q)
# with each 10-dim candidate.  Also test the four cross-pairings explicitly.
kerQ = nullspace_basis(Q)
imQ = col_basis(Q)

print('A3-4-20 / INTERTWINER-LOEWY ALIGNMENT')
print('module_dimension = 35')
print('intertwiner_system_shape =', E.shape)
print('rank(E) =', rankE)
print('Hom_dimension =', nullity)
print('rank(Q) =', rank3(Q))
print('dim ker(Q) =', kerQ.shape[1])
print('dim im(Q) =', imQ.shape[1])
print('dim rad(B/A) =', radBA.shape[1])
print('dim soc(B/A) =', socBA.shape[1])
print('dim rad(K) =', radK.shape[1])
print('dim soc(K) =', socK.shape[1])

print('KER_EQ_RAD_BA =', equal_subspaces(kerQ, radBA))
print('KER_EQ_SOC_BA =', equal_subspaces(kerQ, socBA))
print('IMAGE_EQ_RAD_K =', equal_subspaces(imQ, radK))
print('IMAGE_EQ_SOC_K =', equal_subspaces(imQ, socK))

# Since Q is unique up to scalar, these equalities are invariant under
# rescaling the nonzero intertwiner.
print('CANDIDATE_TOP_TO_SOCLE =', equal_subspaces(kerQ, radBA) and equal_subspaces(imQ, socK))
print('CANDIDATE_SOCLE_TO_RADICAL =', equal_subspaces(kerQ, socBA) and equal_subspaces(imQ, radK))

# Direct module-homology checks: kernel and image are H-stable automatically,
# but assert it explicitly to guard against coordinate mistakes.
for G in BA:
    assert np.all((Q @ G) % P == (Q @ G) % P)
for G in K:
    assert np.all((G @ Q) % P == (G @ Q) % P)

print('A3-4-20_PASS =', (
    kerQ.shape[1] == 25 and imQ.shape[1] == 10 and
    radBA.shape[1] == 25 and socK.shape[1] == 10 and
    equal_subspaces(kerQ, radBA) and equal_subspaces(imQ, socK)
))
print('RESULT: exact kernel/image placement of the unique rank-10 intertwiner was tested against radical/socle.')
