import runpy
import numpy as np
from itertools import product

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


def independent_columns(M):
    M = np.array(M, dtype=np.int64) % P
    selected = []
    C = np.empty((M.shape[0], 0), dtype=np.int64)
    r = 0
    for j in range(M.shape[1]):
        T = np.column_stack([C, M[:, j]])
        nr = rank3(T)
        if nr > r:
            selected.append(j)
            C = T
            r = nr
    return selected, C


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
    return rows, E[:, k:]


# Authoritative frozen W and nilpotent N.
ns_end = runpy.run_path(ROOT + 'phase2_3_endH_optimized_2026-09-15.py')
N = np.array(ns_end['N'], dtype=np.int64) % P
assert N.shape == (45, 45)
assert rank3(N) == 10
assert np.array_equal((N @ N) % P, np.zeros((45, 45), dtype=np.int64))

# Reconstruct the corrected A3-4-10 obstruction D directly.
# This deliberately does NOT import A3-4-11, whose independent rank_D==45
# assertion is unrelated to the O1-0 question.
ns10 = runpy.run_path(ROOT + 'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
D = np.array(ns10['D'], dtype=np.int64) % P
assert D.shape == (4096, 45)

# Build the actual degree-5 Lie target L5 and coordinates in F3^204.
ns1 = runpy.run_path(ROOT + 'phase2_1_invariant_space_verification_2026-09-15.py')
words4 = ns1['words4']
L4_candidates = ns1['L4_candidates']
vec4 = ns1['vec4']

words5 = list(product((1, 2, 3, 4), repeat=5))
index5 = {w: i for i, w in enumerate(words5)}

def bracket_col(v_col, gen):
    out = np.zeros(1024, dtype=np.int64)
    for j, coeff in enumerate(v_col):
        c = int(coeff) % P
        if c:
            w = words4[j]
            out[index5[w + (gen,)]] = (out[index5[w + (gen,)]] + c) % P
            out[index5[(gen,) + w]] = (out[index5[(gen,) + w]] - c) % P
    return out

L5_candidates = []
for a in L4_candidates:
    va = vec4(a)
    for g in range(1, 5):
        L5_candidates.append(bracket_col(va, g))
L5_matrix = np.column_stack(L5_candidates) % P
assert rank3(L5_matrix) == 204
L5_basis = np.empty((1024, 0), dtype=np.int64)
r = 0
for j in range(L5_matrix.shape[1]):
    T = np.column_stack([L5_basis, L5_matrix[:, j]])
    nr = rank3(T)
    if nr > r:
        L5_basis = T
        r = nr
        if r == 204:
            break
assert L5_basis.shape == (1024, 204)
rows, L5_left = left_inverse(L5_basis)

def coords(V):
    V = np.array(V, dtype=np.int64) % P
    if V.ndim == 1:
        V = V[:, None]
    C = (L5_left @ V[rows, :]) % P
    assert np.array_equal((L5_basis @ C) % P, V)
    return C

# D consists of four 1024-row ambient blocks; compress each to L5 coordinates.
D_blocks = [D[h * 1024:(h + 1) * 1024, :] for h in range(4)]
D_L5 = np.vstack([coords(B) for B in D_blocks])
assert D_L5.shape == (816, 45)

# I_W = ker(N), in the same frozen W coordinates.
I_basis = nullspace3(N)
assert I_basis.shape == (45, 35)
assert rank3(I_basis) == 35
assert np.array_equal((N @ I_basis) % P, np.zeros((45, 35), dtype=np.int64))

# Four generator discrepancies D_h: W -> L5.
ranks = []
max_abs = []
for h in range(4):
    D_h = D_L5[h * 204:(h + 1) * 204, :]
    M = (D_h @ I_basis) % P
    ranks.append(rank3(M))
    max_abs.append(int(np.max(np.abs(M))))
    assert M.shape == (204, 35)

print('O1-0: DOES THE OBSTRUCTION ANNIHILATE I_W = ker(N)?')
print('W dimension =', 45)
print('rank(N) =', rank3(N))
print('dim I_W = dim ker(N) =', I_basis.shape[1])
print('D_L5 shape =', D_L5.shape)
print('D_h I_W ranks (h=1..4) =', ranks)
print('D_h I_W max absolute entries (h=1..4) =', max_abs)
print('D_h I_W zero matrices =', [r == 0 and m == 0 for r, m in zip(ranks, max_abs)])

PASS = all(r == 0 and m == 0 for r, m in zip(ranks, max_abs))
print('O1-0 PASS =', PASS)
if not PASS:
    raise AssertionError('O1-0 FAIL: at least one D_h does not annihilate I_W')

print('CONCLUSION: D_h(I_W)=0 for all four generators.')
print('This establishes I_W subset ker(D_h); quotient factorization may now be tested.')
