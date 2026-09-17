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


def nullspace3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    m, n = A.shape
    R = A.copy()
    pivots = []
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
        pivots.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(n) if c not in pivots]
    Z = np.zeros((n, len(free)), dtype=np.int64)
    for j, f in enumerate(free):
        Z[f, j] = 1
        for rr, p in enumerate(pivots):
            Z[p, j] = (-R[rr, f]) % P
    return Z


def left_inverse(B):
    B = np.array(B, dtype=np.int64) % P
    k = B.shape[1]
    rows = []
    R = np.empty((0, k), dtype=np.int64)
    r = 0
    for i in range(B.shape[0]):
        T = np.vstack([R, B[i:i+1]])
        nr = rank3(T)
        if nr > r:
            rows.append(i)
            R = T
            r = nr
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


# Reuse the authoritative O1-0 computation. Its PASS is an explicit prerequisite.
ns0 = runpy.run_path(ROOT + 'O1-0_OBSTRUCTION_ANNIHILATES_I_2026-09-18.py')
N = np.array(ns0['N'], dtype=np.int64) % P
D_L5 = np.array(ns0['D_L5'], dtype=np.int64) % P
I_basis = np.array(ns0['I_basis'], dtype=np.int64) % P

assert N.shape == (45, 45)
assert D_L5.shape == (816, 45)
assert I_basis.shape == (45, 35)
assert rank3(N) == 10
assert rank3(I_basis) == 35
assert np.array_equal((N @ I_basis) % P, np.zeros((45, 35), dtype=np.int64))

# D_stack : W -> L5^4.  It is the full 816 x 45 stacked obstruction map.
D_stack = D_L5
assert D_stack.shape == (816, 45)

# Choose an explicit 10-dimensional complement C to I_W and form
# Q = [I_basis | C], a basis of W.  The quotient coordinates are the
# last 10 coordinates in this basis.
C_cols = []
current = I_basis.copy()
current_rank = 35
for j in range(45):
    e = np.zeros((45, 1), dtype=np.int64)
    e[j, 0] = 1
    T = np.column_stack([current, e])
    r = rank3(T)
    if r > current_rank:
        C_cols.append(j)
        current = T
        current_rank = r
        if current_rank == 45:
            break
assert len(C_cols) == 10
C = np.eye(45, dtype=np.int64)[:, C_cols]
Q = np.column_stack([I_basis, C]) % P
assert Q.shape == (45, 45)
assert rank3(Q) == 45

# LQ Q = I, so pi = last 10 rows of LQ is a concrete quotient-coordinate
# map pi: W -> F3^10 with ker(pi) = I_W.
LQ = left_inverse(Q)
assert np.array_equal((LQ @ Q) % P, np.eye(45, dtype=np.int64))
pi = LQ[35:, :]
assert pi.shape == (10, 45)
assert rank3(pi) == 10
assert np.array_equal((pi @ I_basis) % P, np.zeros((10, 35), dtype=np.int64))
assert np.array_equal((pi @ C) % P, np.eye(10, dtype=np.int64))

# The candidate factor map is barD_stack = D_stack C : F3^10 -> L5^4.
barD_stack = (D_stack @ C) % P
assert barD_stack.shape == (816, 10)

# Direct factorization identity: D_stack = barD_stack o pi.
reconstructed = (barD_stack @ pi) % P
factorization_exact = np.array_equal(reconstructed, D_stack)
assert factorization_exact

# Verify the same factorization generator-by-generator.
generator_factorization = []
for h in range(4):
    D_h = D_stack[h * 204:(h + 1) * 204, :]
    barD_h = (D_h @ C) % P
    ok = np.array_equal((barD_h @ pi) % P, D_h)
    generator_factorization.append(ok)
    assert ok

print('O1-1: QUOTIENT FACTORIZATION THROUGH W / I_W')
print('W dimension =', 45)
print('dim I_W =', I_basis.shape[1])
print('quotient dimension =', 45 - I_basis.shape[1])
print('D_stack shape =', D_stack.shape)
print('D_stack rank =', rank3(D_stack))
print('chosen complement columns =', C_cols)
print('Q = [I_W | C] rank =', rank3(Q))
print('quotient coordinate map pi shape =', pi.shape)
print('ker(pi) dimension =', 45 - rank3(pi))
print('pi(I_W) = 0 =', np.array_equal((pi @ I_basis) % P, np.zeros((10, 35), dtype=np.int64)))
print('pi(C) = I_10 =', np.array_equal((pi @ C) % P, np.eye(10, dtype=np.int64)))
print('barD_stack shape =', barD_stack.shape)
print('D_stack = barD_stack o pi =', factorization_exact)
print('generator-wise factorization (h=1..4) =', generator_factorization)

PASS = factorization_exact and all(generator_factorization)
print('O1-1 PASS =', PASS)
if not PASS:
    raise AssertionError('O1-1 FAIL: quotient factorization was not verified')

print('CONCLUSION: the stacked obstruction factors through W/I_W.')
print('Equivalently, there is a well-defined barD_stack: W/I_W -> L5^4.')
print('The same well-defined factorization holds for each generator obstruction D_h.')
