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


def left_inverse(B):
    """Return row indices and a true left inverse over F_3."""
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
    assert r == k, f'B does not have full column rank: {r} < {k}'

    E = np.concatenate([R.copy(), np.eye(k, dtype=np.int64)], axis=1) % P
    for c in range(k):
        q = next((i for i in range(c, k) if E[i, c]), None)
        assert q is not None, f'no pivot in column {c}'
        E[[c, q]] = E[[q, c]]
        if E[c, c] == 2:
            E[c] = (2 * E[c]) % P
        for i in range(k):
            if i != c and E[i, c]:
                E[i] = (E[i] - E[i, c] * E[c]) % P

    assert np.array_equal(E[:, :k] % P, np.eye(k, dtype=np.int64))
    return rows, E[:, k:]


# A3-4-10 already contains the independently verified affine intertwiner X
# and the degree-5 ambient bracket discrepancy D. Reuse it, then compress
# from the 1024-dimensional associative tensor realization to L_5.
ns10 = runpy.run_path(ROOT + 'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
ns1 = runpy.run_path(ROOT + 'phase2_1_invariant_space_verification_2026-09-15.py')

words4 = ns1['words4']
L4_candidates = ns1['L4_candidates']
R4_matrix = np.array(ns1['R4_matrix'], dtype=np.int64) % P
vec4 = ns1['vec4']
apply_linear_map = ns1['apply_linear_map']
gens = ns1['gens']

W = np.array(ns10['W'], dtype=np.int64) % P
Wd = np.array(ns10['Wd'], dtype=np.int64) % P
X_intertwiner = np.array(ns10['X_intertwiner'], dtype=np.int64) % P
D = np.array(ns10['D'], dtype=np.int64) % P
B_W = ns10['B_W']
B_Wd = ns10['B_Wd']

assert W.shape == (256, 45)
assert Wd.shape == (256, 45)
assert X_intertwiner.shape == (45, 45)
assert D.shape == (4 * 1024, 45)

# -------------------------------------------------------------------------
# 1. Construct the actual free Lie space L_5 inside the degree-5 tensor
#    algebra. Brackets [L_4, X_i] span L_5.
# -------------------------------------------------------------------------
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

L5_candidates = []
for a in L4_candidates:
    va = vec4(a)
    for g in range(1, 5):
        L5_candidates.append(bracket_col(va, g))
L5_matrix = np.column_stack(L5_candidates) % P

dim_L5 = rank3(L5_matrix)
assert dim_L5 == 204, f'expected dim L5=204, got {dim_L5}'
L5_basis = L5_matrix[:, :0]
r = 0
for j in range(L5_matrix.shape[1]):
    C = np.column_stack([L5_basis, L5_matrix[:, j]])
    q = rank3(C)
    if q > r:
        L5_basis = C
        r = q
        if r == dim_L5:
            break
assert rank3(L5_basis) == 204
print('CHECKPOINT: L5 basis constructed; dim L5 =', dim_L5, 'elapsed =', round(time.perf_counter() - T0, 3), 's')

# IMPORTANT PERFORMANCE FIX:
# Build the L5 coordinate extractor exactly once. The previous version
# recomputed a 204x204 Gauss-Jordan inverse for every obstruction column,
# which made A3-4-11 unnecessarily slow.
INV_T0 = time.perf_counter()
L5_rows, L5_left_inv = left_inverse(L5_basis)
print('CHECKPOINT: L5 left inverse built once; elapsed =', round(time.perf_counter() - INV_T0, 3), 's')


def coords_many(V):
    """Convert one or many ambient vectors to L5 coordinates using cached inverse."""
    V = np.array(V, dtype=np.int64) % P
    if V.ndim == 1:
        V = V[:, None]
    C = (L5_left_inv @ V[L5_rows, :]) % P
    assert np.array_equal((L5_basis @ C) % P, V)
    return C


# -------------------------------------------------------------------------
# 2. Project each A3-4-10 discrepancy component to actual L_5 coordinates.
# -------------------------------------------------------------------------
D_components = [D[g * 1024:(g + 1) * 1024, :] for g in range(4)]
D_L5 = np.vstack([coords_many(C) for C in D_components])
assert D_L5.shape == (816, 45)
rank_D_associative = rank3(D)
rank_D_L5 = rank3(D_L5)
assert rank_D_associative == rank_D_L5

RECONSTRUCTION_OK = all(
    np.array_equal((L5_basis @ D_L5[g * 204:(g + 1) * 204, :]) % P, D_components[g])
    for g in range(4)
)
assert RECONSTRUCTION_OK
print('CHECKPOINT: obstruction compressed to L5; rank =', rank_D_L5, 'elapsed =', round(time.perf_counter() - T0, 3), 's')

# -------------------------------------------------------------------------
# 3. Verify that the obstruction map is H-equivariant as a map
#       W45 -> Hom(V, L5).
# -------------------------------------------------------------------------
def dict_from_vec5(v):
    return {w: int(c) % P for w, c in zip(words5, v) if int(c) % P}


def vec5_from_dict(a):
    v = np.zeros(1024, dtype=np.int64)
    for w, c in a.items():
        v[index5[w]] = int(c) % P
    return v

A_L5 = []
for gmat in gens:
    transformed = []
    for j in range(dim_L5):
        v = L5_basis[:, j] % P
        out = apply_linear_map(dict_from_vec5(v), gmat)
        transformed.append(vec5_from_dict(out))
    transformed_matrix = np.column_stack(transformed) % P
    A_L5.append(coords_many(transformed_matrix))
assert all(a.shape == (204, 204) and rank3(a) == 204 for a in A_L5)
print('CHECKPOINT: L5 action matrices built for', len(A_L5), 'generators; elapsed =', round(time.perf_counter() - T0, 3), 's')


def transform_D(Dcoords, A5, h):
    blocks = [Dcoords[g * 204:(g + 1) * 204, :] for g in range(4)]
    aug = np.concatenate([h.copy() % P, np.eye(4, dtype=np.int64)], axis=1)
    for c in range(4):
        q = next(i for i in range(c, 4) if aug[i, c])
        aug[[c, q]] = aug[[q, c]]
        if aug[c, c] == 2:
            aug[c] = (2 * aug[c]) % P
        for i in range(4):
            if i != c and aug[i, c]:
                aug[i] = (aug[i] - aug[i, c] * aug[c]) % P
    hinv = aug[:, 4:]
    h_blocks = [(A5 @ B) % P for B in blocks]
    out = []
    for i in range(4):
        C = np.zeros((204, 45), dtype=np.int64)
        for j in range(4):
            C = (C + hinv[j, i] * h_blocks[j]) % P
        out.append(C)
    return np.vstack(out) % P


A_W = [np.array(a, dtype=np.int64) % P for a in ns10['A_W']]
EQUIVARIANT = True
EQUIVARIANCE_RANKS = []
for A5, h, A in zip(A_L5, gens, A_W):
    lhs = transform_D(D_L5, A5, h)
    rhs = (D_L5 @ A) % P
    rr = rank3((lhs - rhs) % P)
    EQUIVARIANCE_RANKS.append(rr)
    if rr != 0:
        EQUIVARIANT = False
assert EQUIVARIANT

IMAGE_IS_W45 = (rank_D_L5 == 45)
assert IMAGE_IS_W45

# -------------------------------------------------------------------------
# 4. Local degree-5 relation span generated by [ (R)_4, X_i ].
# -------------------------------------------------------------------------
# R4_matrix is the actual degree-4 relation span in the 256-dimensional
# associative-word coordinates: 5 independent columns inside L4 (dim 60).
# The previous assertion incorrectly expected 60 rows, confusing ambient
# coordinates with the intrinsic dimension of L4.
R4_ind = R4_matrix
assert R4_ind.shape[0] == 256 and R4_ind.shape[1] == 5 and rank3(R4_ind) == 5

R5_candidates = []
for j in range(R4_ind.shape[1]):
    v = R4_ind[:, j]
    R5_candidates.extend(bracket_col(v, g) for g in range(1, 5))
R5_matrix = np.column_stack(R5_candidates) % P
R5_L5 = coords_many(R5_matrix)
dim_R5_local = rank3(R5_L5)

combined_rank = rank3(np.column_stack([D_L5, R5_L5]))
intersection_dim = rank_D_L5 + dim_R5_local - combined_rank

print('PHASE 2-24 / A3-4-11 DEGREE-5 LIE OBSTRUCTION COMPRESSION')
print('dim L5 =', dim_L5)
print('L5 basis ambient dimension =', 1024)
print('dim local degree-5 relation span <[(R)_4, X_i]> =', dim_R5_local)
print('A3-4-10 obstruction rank in associative degree-5 space =', rank_D_associative)
print('A3-4-10 obstruction rank after projection to L5 =', rank_D_L5)
print('LOSSLESS_LIE_PROJECTION =', RECONSTRUCTION_OK)
print('H-equivariance ranks for 5 generators =', EQUIVARIANCE_RANKS)
print('OBSTRUCTION_MAP_H_EQUIVARIANT =', EQUIVARIANT)
print('OBSTRUCTION_IMAGE_ISOMORPHIC_TO_W45_BY_INJECTIVITY =', IMAGE_IS_W45)
print('intersection dim(obstruction image, local relation span) =', intersection_dim)
print('rank(obstruction + local relation span) =', combined_rank)
print('TOTAL_ELAPSED_SECONDS =', round(time.perf_counter() - T0, 3))
print('RESULT: the degree-5 obstruction is already an actual L5-valued obstruction; compression to L5 loses no rank.')
print('RESULT: the obstruction map is H-equivariant and injective, so its image is an H-module isomorphic to W45.')
print('CAUTION: the relation-span test uses only [ (R)_4, X_i ]; it is not claimed to be the full degree-5 relation ideal.')
print('ALL A3-4-11 CHECKS COMPLETED')
