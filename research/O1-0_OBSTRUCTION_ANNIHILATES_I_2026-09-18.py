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
    basis = []
    for f in free:
        x = np.zeros(n, dtype=np.int64)
        x[f] = 1
        for rr, p in enumerate(pivots):
            x[p] = (-R[rr, f]) % P
        basis.append(x)
    return basis


# Frozen W representation and authoritative nilpotent N.
ns_end = runpy.run_path(ROOT + 'phase2_3_endH_optimized_2026-09-15.py')
N = np.array(ns_end['N'], dtype=np.int64) % P
assert N.shape == (45, 45)
assert rank3(N) == 10
assert np.array_equal((N @ N) % P, np.zeros((45, 45), dtype=np.int64))

# Corrected A3-4-11 artifact: Delta in L5^4.
ns = runpy.run_path(ROOT + 'A3-4-11_TRUE_R5_INTERSECTION_2026-09-16.py')
D_L5 = np.array(ns['D_L5'], dtype=np.int64) % P
assert D_L5.shape == (816, 45)
assert rank3(D_L5) == 45

# I_W = ker(N), in the same frozen W coordinates.
I_basis = np.column_stack(nullspace3(N)) % P
assert I_basis.shape == (45, 35)
assert rank3(I_basis) == 35
assert np.array_equal((N @ I_basis) % P, np.zeros((45, 35), dtype=np.int64))

# Four generator discrepancies D_h: W -> L5.
D_blocks = [D_L5[h * 204:(h + 1) * 204, :] for h in range(4)]
assert all(B.shape == (204, 45) for B in D_blocks)

ranks = []
max_abs = []
for h, D_h in enumerate(D_blocks, start=1):
    M = (D_h @ I_basis) % P
    ranks.append(rank3(M))
    max_abs.append(int(np.max(np.abs(M))))
    assert M.shape == (204, 35)

print('O1-0: DOES THE OBSTRUCTION ANNIHILATE I_W = ker(N)?')
print('W dimension =', 45)
print('rank(N) =', rank3(N))
print('dim I_W = dim ker(N) =', 35)
print('I_basis shape =', I_basis.shape)
print('D_h I_W ranks (h=1..4) =', ranks)
print('D_h I_W max absolute entries (h=1..4) =', max_abs)
print('D_h I_W zero matrices =', [r == 0 and m == 0 for r, m in zip(ranks, max_abs)])

PASS = all(r == 0 and m == 0 for r, m in zip(ranks, max_abs))
print('O1-0 PASS =', PASS)

if not PASS:
    raise AssertionError('O1-0 FAIL: at least one D_h does not annihilate I_W')

print('CONCLUSION: D_h(I_W)=0 for all four generators.')
print('This establishes I_W subset ker(D_h); quotient factorization may now be tested.')
