import runpy
import numpy as np

P = 3
ROOT = 'research/'

# Import A3-4-16 itself so B/A and K are exactly the same 35x35 action
# matrices used in the strong modular fingerprint experiment.
ns = runpy.run_path(ROOT + 'A3-4-16_STRONG_MODULAR_FINGERPRINT_2026-09-16.py')
BA = [np.array(x, dtype=np.int64) % P for x in ns['BA_gens']]
K = [np.array(x, dtype=np.int64) % P for x in ns['K_gens']]
rank3 = ns['rank3']

assert len(BA) == len(K) == 5
assert all(T.shape == (35, 35) for T in BA + K)

# P*BA_g = K_g*P.  With column-major vectorization:
# (BA_g^T kron I - I kron K_g) vec(P) = 0.
I = np.eye(35, dtype=np.int64)
blocks = []
for A, G in zip(BA, K):
    blocks.append((np.kron(A.T, I) - np.kron(I, G)) % P)
E = np.vstack(blocks) % P
assert E.shape == (6125, 1225)

# Exact Gaussian elimination over F_3.
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

R, pivots = rref3(E)
rankE = len(pivots)
nullity = E.shape[1] - rankE
print('A3-4-17 / HOM RECHECK IN IDENTICAL A3-4-16 SETTING')
print('BA dimensions =', [T.shape for T in BA])
print('K dimensions  =', [T.shape for T in K])
print('intertwiner system shape =', E.shape)
print('rank(E) =', rankE)
print('nullity(E) =', nullity)

free_set = set(range(E.shape[1])) - set(pivots)
basis = []
for f in sorted(free_set):
    x = np.zeros(E.shape[1], dtype=np.int64)
    x[f] = 1
    for rr, pc in enumerate(pivots):
        x[pc] = (-R[rr, f]) % P
    basis.append(x)
assert len(basis) == nullity

intertwiner_ranks = []
for idx, x in enumerate(basis, 1):
    M = x.reshape((35, 35), order='F') % P
    for A, G in zip(BA, K):
        assert np.array_equal((M @ A - G @ M) % P,
                              np.zeros((35, 35), dtype=np.int64))
    rM = rank3(M)
    intertwiner_ranks.append(rM)
    print('intertwiner', idx, 'rank =', rM)

max_rank = max(intertwiner_ranks) if intertwiner_ranks else 0
print('dim Hom_H(B/A,K) =', nullity)
print('MAX_INTERTWINER_RANK =', max_rank)

# If Hom has dimension 1, every nonzero intertwiner is a scalar multiple of
# the same map, so rank < 35 is a complete non-isomorphism certificate.
if nullity == 1:
    assert max_rank < 35
    print('NONISOMORPHISM_CERTIFICATE = True')
else:
    print('NOTE: Hom dimension is not 1; maximum-rank certification needs a separate search.')

print('SAME_ACTION_MATRICES_AS_A3-4-16 = True')
print('RESULT: Hom-space recheck completed in the identical A3-4-16 representation setting.')
print('ALL A3-4-17 CHECKS COMPLETED')
