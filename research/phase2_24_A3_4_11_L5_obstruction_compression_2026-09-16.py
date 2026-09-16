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
    E = np.column_stack([R, np.eye(k, dtype=np.int64)])
    for c in range(k):
        q = next(i for i in range(k) if E[i, c])
        E[[c, q]] = E[[q, c]]
        if E[c, c] == 2:
            E[c] = (2 * E[c]) % P
        for i in range(k):
            if i != c and E[i, c]:
                E[i] = (E[i] - E[i, c] * E[c]) % P
    return rows, E[:, k:]


def coords(B, V):
    rows, L = left_inverse(B)
    C = (L @ np.array(V, dtype=np.int64)[rows]) % P
    assert np.array_equal((B @ C) % P, np.array(V, dtype=np.int64) % P)
    return C


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

def bracket_column_with_generator(v_col, gen):
    out = np.zeros(1024, dtype=np.int64)
    for j, coeff in enumerate(v_col):
        coeff = int(coeff) % P
        if coeff == 0:
            continue
        w = words4[j]
        out[sum((4 ** k) * (a - 1) for k, a in enumerate(w + (gen,)))] = 0
        # The direct index expression above is only a placeholder; use the
        # canonical tuple dictionary below for correctness.
    return out

# Canonical tuple-indexed degree-5 associative coordinates.
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

# vec4(L4 element) columns -> [L4, X_i] candidates.
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

# -------------------------------------------------------------------------
# 2. Project each A3-4-10 discrepancy component to actual L_5 coordinates.
# -------------------------------------------------------------------------
D_components = [D[g * 1024:(g + 1) * 1024, :] for g in range(4)]
D_L5 = np.column_stack([coords(L5_basis, C) for C in D_components])
# D_L5 has 204*4 rows and 45 columns.
assert D_L5.shape == (816, 45)
rank_D_associative = rank3(D)
rank_D_L5 = rank3(D_L5)
assert rank_D_associative == rank_D_L5

# The projection is lossless here: every discrepancy is already a Lie element.
RECONSTRUCTION_OK = all(
    np.array_equal((L5_basis @ D_L5[g * 204:(g + 1) * 204, :]) % P, D_components[g])
    for g in range(4)
)
assert RECONSTRUCTION_OK

# -------------------------------------------------------------------------
# 3. Verify that the obstruction map is H-equivariant as a map
#       W45 -> Hom(V, L5),
#    where H acts on Hom(V,L5) by h.F = h o F o h^{-1}.
#    This is the natural representation-theoretic packaging of the four
#    bracket discrepancy components.
# -------------------------------------------------------------------------

# Build action of each symplectic generator on L5 coordinates by applying
# the generator substitution to each L5 basis vector in the tensor algebra.
# Convert an associative vector to a word dictionary, apply the existing
# substitution routine, then return its degree-5 vector.
def dict_from_vec5(v):
    return {w: int(c) % P for w, c in zip(words5, v) if int(c) % P}

def vec5_from_dict(a):
    v = np.zeros(1024, dtype=np.int64)
    for w, c in a.items():
        v[index5[w]] = int(c) % P
    return v

A_L5 = []
for gmat in gens:
    cols = []
    for j in range(dim_L5):
        v = (L5_basis[:, j]) % P
        out = apply_linear_map(dict_from_vec5(v), gmat)
        cols.append(coords(L5_basis, vec5_from_dict(out)))
    A_L5.append(np.column_stack(cols) % P)
assert all(a.shape == (204, 204) and rank3(a) == 204 for a in A_L5)

# D as a 204 x 4 x 45 tensor: D[w][input]. Under h,
# (h.D)(e_i) = h(D(h^{-1} e_i)).
# The generator matrix has columns h(e_i).
# Hence output component i is sum_j (h^{-1})[j,i] * h(D_j).
def transform_D(Dcoords, A5, h):
    # Dcoords shape (816,45), split into 4 L5 blocks.
    blocks = [Dcoords[g * 204:(g + 1) * 204, :] for g in range(4)]
    hinv = None
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

A_W = ns10['A_W']
A_W = [np.array(a, dtype=np.int64) % P for a in A_W]
EQUIVARIANT = True
EQUIVARIANCE_RANKS = []
for A5, h, A in zip(A_L5, gens, A_W):
    lhs = transform_D(D_L5, A5, h)
    rhs = (D_L5 @ A) % P
    diff = (lhs - rhs) % P
    rr = rank3(diff)
    EQUIVARIANCE_RANKS.append(rr)
    if rr != 0:
        EQUIVARIANT = False
assert EQUIVARIANT

# Since rank(D)=45 and D is H-equivariant, the obstruction image is an
# H-module isomorphic to W45. We verify this directly by rank/injectivity.
IMAGE_IS_W45 = (rank_D_L5 == 45)
assert IMAGE_IS_W45

# -------------------------------------------------------------------------
# 4. Degree-5 relation span generated by the verified degree-4 relation
#    ideal: [ (R)_4, X_i ]. This is a conservative local test only; it does
#    not assert that this span is the full degree-5 ideal in every graded
#    presentation.
# -------------------------------------------------------------------------
R4_ind = L5_matrix[:, :0]
r = 0
for j in range(R4_matrix.shape[1]):
    C = np.column_stack([R4_ind, R4_matrix[:, j]])
    q = rank3(C)
    if q > r:
        R4_ind = C
        r = q
assert r == 5

R5_candidates = []
for j in range(R4_ind.shape[1]):
    for g in range(1, 5):
        R5_candidates.append(bracket_col(R4_ind[:, j], g))
R5_matrix = np.column_stack(R5_candidates) % P
R5_L5 = np.column_stack([coords(L5_basis, R5_matrix[:, j]) for j in range(R5_matrix.shape[1])])
dim_R5_local = rank3(R5_L5)

# Intersections of obstruction image with the local degree-5 relation span.
# The image is represented by columns of D_L5; relation span by R5_L5.
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
print('RESULT: the degree-5 obstruction is already an actual L5-valued obstruction; compression to L5 loses no rank.')
print('RESULT: the obstruction map is H-equivariant and injective, so its image is an H-module isomorphic to W45.')
print('CAUTION: the relation-span test uses only [ (R)_4, X_i ]; it is not claimed to be the full degree-5 relation ideal.')
print('ALL A3-4-11 CHECKS COMPLETED')
