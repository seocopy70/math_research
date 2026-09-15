import numpy as np
from itertools import product

P = 3

# ---------- F_3 associative algebra ----------

def add(A, B):
    C = dict(A)
    for w in B:
        C[w] = (C.get(w, 0) + B[w]) % P
        if C[w] == 0:
            del C[w]
    return C

def neg(A):
    return {w: (-c) % P for w, c in A.items() if c % P}

def mul(A, B):
    C = {}
    for wa, ca in A.items():
        for wb, cb in B.items():
            w = wa + wb
            C[w] = (C.get(w, 0) + ca * cb) % P
            if C[w] == 0:
                del C[w]
    return C

def bracket(A, B):
    return add(mul(A, B), neg(mul(B, A)))

# ---------- Generators ----------

X1 = {(1,): 1}
X2 = {(2,): 1}
X3 = {(3,): 1}
X4 = {(4,): 1}
X = [X1, X2, X3, X4]

# ---------- Degree 2 ----------

L2 = []
for i in range(4):
    for j in range(i + 1, 4):
        L2.append(bracket(X[i], X[j]))

# ---------- Quadratic relation ----------

R = add(L2[0], L2[5])

# ---------- Degree 4 Lie elements ----------

L4_candidates = []
for i in range(1, 4):
    j = 4 - i

    if i == 1:
        A_list = X
    elif i == 2:
        A_list = L2
    else:
        A_list = []
        for a in X:
            for b in L2:
                A_list.append(bracket(a, b))

    if j == 1:
        B_list = X
    elif j == 2:
        B_list = L2
    else:
        B_list = []

    for A in A_list:
        for B in B_list:
            L4_candidates.append(bracket(A, B))

# ---------- Degree 4 word basis ----------

words4 = list(product(range(1, 5), repeat=4))
index4 = {w: i for i, w in enumerate(words4)}

def vec4(A):
    v = np.zeros(256, dtype=int)
    for w in A:
        v[index4[w]] = A[w] % P
    return v

# ---------- Rank over F_3 ----------

def rank3(A):
    A = np.array(A, dtype=int) % 3
    if A.ndim == 1:
        A = A.reshape(-1, 1)

    m, n = A.shape
    r = 0

    for c in range(n):
        pivot = None
        for i in range(r, m):
            if A[i, c] != 0:
                pivot = i
                break
        if pivot is None:
            continue

        A[[r, pivot]] = A[[pivot, r]]
        inv = 1 if A[r, c] == 1 else 2
        A[r] = (A[r] * inv) % 3

        for i in range(m):
            if i != r and A[i, c] != 0:
                A[i] = (A[i] - A[i, c] * A[r]) % 3
        r += 1

    return r

# ---------- Phase 1 dimensions ----------

L4_matrix = np.column_stack([vec4(A) for A in L4_candidates])
dimL4 = rank3(L4_matrix)

R4 = []
for B in L2:
    R4.append(bracket(R, B))
R4_matrix = np.column_stack([vec4(A) for A in R4])
dimR4 = rank3(R4_matrix)
dimQ4 = dimL4 - dimR4

# ---------- Symplectic matrix ----------

J = np.array([
    [0, 1, 0, 0],
    [-1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, -1, 0]
]) % 3

# ---------- Target T ----------

T = bracket(
    bracket(
        bracket(X3, X4),
        X1
    ),
    X1
)

# ---------- Exact Phase-1 transvection ----------

g0 = np.array([
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]) % 3

phase1_symp = np.array_equal((g0.T @ J @ g0) % 3, J)
Y1 = add(X1, X2)
g0T = bracket(bracket(bracket(X3, X4), Y1), Y1)
d0 = add(g0T, neg(T))
R4_aug = np.column_stack([R4_matrix, vec4(d0)])
r1 = rank3(R4_matrix)
r2 = rank3(R4_aug)

# ---------- Phase 2 helpers ----------

def rref3(A):
    A = np.array(A, dtype=int) % 3
    if A.ndim == 1:
        A = A.reshape(-1, 1)
    m, n = A.shape
    r = 0
    pivots = []
    for c in range(n):
        pivot = None
        for i in range(r, m):
            if A[i, c] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        A[[r, pivot]] = A[[pivot, r]]
        inv = 1 if A[r, c] == 1 else 2
        A[r] = (A[r] * inv) % 3
        for i in range(m):
            if i != r and A[i, c] != 0:
                A[i] = (A[i] - A[i, c] * A[r]) % 3
        pivots.append(c)
        r += 1
        if r == m:
            break
    return A, pivots


def transvection(v):
    v = np.array(v, dtype=int) % 3
    return (np.eye(4, dtype=int) + np.outer(v, (J @ v) % 3)) % 3


def matrix_key(A):
    return tuple((np.array(A, dtype=int) % 3).flatten().tolist())


def generated_group_size(gens):
    I = np.eye(4, dtype=int)
    group = {matrix_key(I): I}
    frontier = [I]
    while frontier:
        a = frontier.pop()
        for g in gens:
            b = (a @ g) % 3
            k = matrix_key(b)
            if k not in group:
                group[k] = b
                frontier.append(b)
    return len(group)


def apply_linear_map(A, g):
    # Column j of g is the image of X_j.
    images = []
    for j in range(4):
        image = {}
        for i in range(4):
            c = int(g[i, j]) % 3
            if c:
                image[(i + 1,)] = c
        images.append(image)

    out = {}
    for word, coeff in A.items():
        cur = {(): coeff}
        for letter in word:
            cur = mul(cur, images[letter - 1])
        out = add(out, cur)
    return out


def inverse3(A):
    A = np.array(A, dtype=int) % 3
    n = A.shape[0]
    aug = np.concatenate([A, np.eye(n, dtype=int)], axis=1)
    for c in range(n):
        pivot = None
        for i in range(c, n):
            if aug[i, c] != 0:
                pivot = i
                break
        if pivot is None:
            raise ValueError('singular matrix over F_3')
        aug[[c, pivot]] = aug[[pivot, c]]
        inv = 1 if aug[c, c] == 1 else 2
        aug[c] = (aug[c] * inv) % 3
        for i in range(n):
            if i != c and aug[i, c] != 0:
                aug[i] = (aug[i] - aug[i, c] * aug[c]) % 3
    return aug[:, n:]


def independent_columns(M):
    selected = []
    current = np.empty((M.shape[0], 0), dtype=int)
    r = 0
    for j in range(M.shape[1]):
        candidate = np.column_stack([current, M[:, j:j+1]])
        nr = rank3(candidate)
        if nr > r:
            selected.append(j)
            current = candidate
            r = nr
    return selected, current

# ---------- All 40 distinct symplectic transvections ----------

nonzero_vectors = [np.array(v, dtype=int) for v in product(range(3), repeat=4) if any(v)]
transvection_dict = {}
for v in nonzero_vectors:
    g = transvection(v)
    transvection_dict[matrix_key(g)] = g

transvections = list(transvection_dict.values())
assert len(transvections) == 40
assert all(np.array_equal((g.T @ J @ g) % 3, J) for g in transvections)

# ---------- Five generators for Sp_4(F_3) ----------

generating_vectors = [
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
    (1, 0, 1, 0),
]
gens = [transvection(v) for v in generating_vectors]
assert all(np.array_equal((g.T @ J @ g) % 3, J) for g in gens)
group_order = generated_group_size(gens)
assert group_order == 51840

# ---------- Orbit span W in Q4 ----------

# Start with T. Whenever a new orbit element increases the span modulo R4,
# append it to the W basis. Continue until the orbit under the generators closes.
basis = []
combined = R4_matrix.copy()
queue = [T]
seen = set()

while queue:
    a = queue.pop(0)
    k = tuple(sorted(a.items()))
    if k in seen:
        continue
    seen.add(k)

    old_rank = rank3(combined)
    candidate = np.column_stack([combined, vec4(a)])
    new_rank = rank3(candidate)
    if new_rank > old_rank:
        basis.append(a)
        combined = candidate

    for g in gens:
        queue.append(apply_linear_map(a, g))

# The quotient W has dimension equal to the number of independent orbit vectors.
dimW = len(basis)
combined_rank = rank3(combined)
assert dimW == 45
assert combined_rank == 50

# ---------- Coordinate system on R4 + W ----------

# R4 has 6 displayed generators but rank 5. Select an independent R4 basis.
r4_indices, R4_ind = independent_columns(R4_matrix)
assert len(r4_indices) == 5

B = np.column_stack([R4_ind] + [vec4(a) for a in basis])
assert B.shape == (256, 50)
assert rank3(B) == 50

# Select 50 independent rows so that the restricted 50x50 matrix is invertible.
selected_rows = []
row_matrix = np.empty((0, 50), dtype=int)
row_rank = 0
for i in range(256):
    candidate = np.vstack([row_matrix, B[i:i+1, :]])
    new_rank = rank3(candidate)
    if new_rank > row_rank:
        selected_rows.append(i)
        row_matrix = candidate
        row_rank = new_rank
        if row_rank == 50:
            break
assert len(selected_rows) == 50

B_inv = inverse3(B[selected_rows, :])

def coordinates(v):
    return (B_inv @ (v[selected_rows] % 3)) % 3

# ---------- W action matrices ----------

# For each generator and each W basis vector, recover coordinates in R4 + W.
# The first 5 coordinates are the R4 part; the last 45 are W coordinates.
action_matrices = []
for g in gens:
    C = np.column_stack([
        coordinates(vec4(apply_linear_map(a, g)))
        for a in basis
    ])
    A = C[5:, :]
    assert A.shape == (45, 45)
    action_matrices.append(A)

# ---------- Invariant-space calculation ----------

# w is invariant iff (A_i - I) w = 0 for every generator.
M = np.vstack([
    (A - np.eye(45, dtype=int)) % 3
    for A in action_matrices
])
rank_M = rank3(M)
dim_invariants = 45 - rank_M

assert rank_M == 45
assert dim_invariants == 0

# ---------- Output ----------

print('PHASE 1')
print('dim L4 =', dimL4)
print('dim (R)_4 =', dimR4)
print('dim Q4 =', dimQ4)
print('g0 symplectic =', phase1_symp)
print('rank(R4) =', r1)
print('rank([R4 | gT-T]) =', r2)
print()
print('PHASE 2-1')
print('distinct transvections =', len(transvections))
print('generator count =', len(gens))
print('generated group order =', group_order)
print('dim W =', dimW)
print('rank([R4_ind | W_basis]) =', combined_rank)
print('independent R4 columns =', r4_indices)
print('selected coordinate rows =', len(selected_rows))
print('action matrix shape =', action_matrices[0].shape)
print('rank of stacked (A_i-I) =', rank_M)
print('dim W^Sp4(F3) =', dim_invariants)
print()
print('ALL PHASE 2-1 CHECKS PASSED')
