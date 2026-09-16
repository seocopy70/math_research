import runpy
import time
import numpy as np

P = 3
ROOT = 'research/'
T0 = time.perf_counter()


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
    return rows, E[:, k:]


# A3-4-10 supplies the corrected degree-5 discrepancy Delta in L5^4.
ns10 = runpy.run_path(ROOT + 'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
ns1 = runpy.run_path(ROOT + 'phase2_1_invariant_space_verification_2026-09-15.py')

D = np.array(ns10['D'], dtype=np.int64) % P
W = np.array(ns10['W'], dtype=np.int64) % P
Wd = np.array(ns10['Wd'], dtype=np.int64) % P
assert D.shape == (4 * 1024, 45)
assert W.shape == (256, 45) and Wd.shape == (256, 45)

words4 = ns1['words4']
L4_candidates = ns1['L4_candidates']
vec4 = ns1['vec4']
apply_linear_map = ns1['apply_linear_map']
gens = ns1['gens']
R4_matrix = np.array(ns1['R4_matrix'], dtype=np.int64) % P

from itertools import product
words5 = list(product((1, 2, 3, 4), repeat=5))
index5 = {w: i for i, w in enumerate(words5)}


def bracket_col(v_col, gen):
    out = np.zeros(1024, dtype=np.int64)
    for j, coeff in enumerate(v_col):
        coeff = int(coeff) % P
        if coeff:
            w = words4[j]
            out[index5[w + (gen,)]] = (out[index5[w + (gen,)]] + coeff) % P
            out[index5[(gen,) + w]] = (out[index5[(gen,) + w]] - coeff) % P
    return out

# Build the actual Lie L5 and a coordinate extractor L5 -> F3^204.
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
    C = np.column_stack([L5_basis, L5_matrix[:, j]])
    nr = rank3(C)
    if nr > r:
        L5_basis = C
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

# Compress Delta from the associative degree-5 tensor algebra to L5^4.
D_blocks = [D[g * 1024:(g + 1) * 1024, :] for g in range(4)]
D_L5 = np.vstack([coords(B) for B in D_blocks])
assert D_L5.shape == (816, 45)
rank_D = rank3(D_L5)
assert rank_D == 45

# TRUE (R)_5 = [L1,(R)_4].  R4_matrix has rank 15; retain all 15 independent
# columns, not the six displayed quadratic-derived candidates.
r4_idx, R4_ind = independent_columns(R4_matrix)
assert len(r4_idx) == 15
assert rank3(R4_ind) == 15

R5_candidates = []
for j in range(15):
    for g in range(1, 5):
        R5_candidates.append(bracket_col(R4_ind[:, j], g))
R5_matrix = np.column_stack(R5_candidates) % P
R5_L5 = coords(R5_matrix)
rank_R5 = rank3(R5_L5)
assert rank_R5 == 60

# The relation-valued target is Hom(V,(R)_5) inside Hom(V,L5) = L5^4.
# Therefore it is the full 4-fold block space over a 60-dimensional R5 basis:
# dimension 4*60 = 240.  This is the correct (R)_5^4/Hom(V,R5) subspace,
# rather than the old 20-column diagonal construction.
r5_idx, R5_basis = independent_columns(R5_L5)
assert len(r5_idx) == 60
assert R5_basis.shape == (204, 60)

R5_4 = np.zeros((4 * 204, 4 * 60), dtype=np.int64)
for g in range(4):
    R5_4[g * 204:(g + 1) * 204, g * 60:(g + 1) * 60] = R5_basis

rank_R5_4 = rank3(R5_4)
assert rank_R5_4 == 240

combined = rank3(np.column_stack([D_L5, R5_4]))
intersection_dim = rank_D + rank_R5_4 - combined
assert 0 <= intersection_dim <= min(rank_D, rank_R5_4)

# H-invariance sanity: R5 itself must be H-stable because R4 is generated by
# the H-stable relation ideal and the Lie bracket is natural.  Verify directly
# on a generating set by checking transformed R5_basis lies in R5.
def dict_from_vec5(v):
    return {w: int(c) % P for w, c in zip(words5, v) if int(c) % P}


def vec5_from_dict(a):
    v = np.zeros(1024, dtype=np.int64)
    for w, c in a.items():
        v[index5[w]] = int(c) % P
    return v

A5 = []
R5_STABILITY_RANKS = []
for gmat in gens:
    transformed = []
    for j in range(204):
        out = apply_linear_map(dict_from_vec5(L5_basis[:, j]), gmat)
        transformed.append(vec5_from_dict(out))
    T5 = coords(np.column_stack(transformed))
    A5.append(T5)
    # Every transformed R5 basis vector must remain in span(R5_basis).
    R = rank3(R5_basis)
    rr = rank3(np.column_stack([R5_basis, (T5 @ R5_basis) % P]))
    R5_STABILITY_RANKS.append(rr - R)
assert R5_STABILITY_RANKS == [0, 0, 0, 0, 0]

print('PHASE A3-4-11 / TRUE R5 INTERSECTION')
print('dim L5 =', 204)
print('dim (R)_4 =', rank3(R4_ind))
print('dim TRUE (R)_5 =', rank_R5)
print('A3-4-10 obstruction rank in L5^4 =', rank_D)
print('dim Hom(V,(R)_5) =', rank_R5_4)
print('rank(obstruction + Hom(V,R5)) =', combined)
print('dim(Im(Delta) intersect Hom(V,R5)) =', intersection_dim)
print('R5 H-stability defects =', R5_STABILITY_RANKS)
print('EXPECTED_W45_SUBMODULE_DIMENSION_SANITY =', intersection_dim in {0, 10, 35, 45})
print('TOTAL_ELAPSED_SECONDS =', round(time.perf_counter() - T0, 3))
assert intersection_dim in {0, 10, 35, 45}
print('SANITY CHECK PASSED: intersection dimension is compatible with the known W45 submodule dimensions.')
print('ALL A3-4-11 TRUE-R5 CHECKS PASSED')
