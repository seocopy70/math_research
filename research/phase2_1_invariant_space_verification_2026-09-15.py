import numpy as np
from itertools import product

P = 3

# ---------- F_3 associative algebra ----------
def add(A, B):
    C = dict(A)
    for w, c in B.items():
        C[w] = (C.get(w, 0) + c) % P
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
L2 = [bracket(X[i], X[j]) for i in range(4) for j in range(i + 1, 4)]

# ---------- Quadratic relation ----------
R = add(L2[0], L2[5])

# ---------- Coordinate helpers ----------
def make_index(degree):
    words = list(product(range(1, 5), repeat=degree))
    return words, {w: i for i, w in enumerate(words)}

words4, index4 = make_index(4)

def vec4(A):
    v = np.zeros(256, dtype=int)
    for w, c in A.items():
        v[index4[w]] = c % P
    return v

def rank3(A):
    A = np.array(A, dtype=int, copy=True) % P
    if A.ndim == 1:
        A = A.reshape(-1, 1)
    m, n = A.shape
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i, c]), None)
        if pivot is None:
            continue
        A[[r, pivot]] = A[[pivot, r]]
        if A[r, c] == 2:
            A[r] = (2 * A[r]) % P
        for i in range(m):
            if i != r and A[i, c]:
                A[i] = (A[i] - A[i, c] * A[r]) % P
        r += 1
        if r == m:
            break
    return r

def rref3(A):
    A = np.array(A, dtype=int, copy=True) % P
    if A.ndim == 1:
        A = A.reshape(-1, 1)
    m, n = A.shape
    r = 0
    pivots = []
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i, c]), None)
        if pivot is None:
            continue
        A[[r, pivot]] = A[[pivot, r]]
        if A[r, c] == 2:
            A[r] = (2 * A[r]) % P
        for i in range(m):
            if i != r and A[i, c]:
                A[i] = (A[i] - A[i, c] * A[r]) % P
        pivots.append(c)
        r += 1
        if r == m:
            break
    return A, pivots

def inverse3(A):
    A = np.array(A, dtype=int) % P
    n = A.shape[0]
    aug = np.concatenate([A, np.eye(n, dtype=int)], axis=1)
    for c in range(n):
        pivot = next((i for i in range(c, n) if aug[i, c]), None)
        if pivot is None:
            raise ValueError('singular matrix over F_3')
        aug[[c, pivot]] = aug[[pivot, c]]
        if aug[c, c] == 2:
            aug[c] = (2 * aug[c]) % P
        for i in range(n):
            if i != c and aug[i, c]:
                aug[i] = (aug[i] - aug[i, c] * aug[c]) % P
    return aug[:, n:]

def independent_columns(M):
    M = np.array(M, dtype=int) % P
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

# ---------- Lie degree 3 and 4 ----------
L3_candidates = [bracket(a, x) for a in L2 for x in X]
L3_matrix = np.column_stack([{w: c for w, c in a.items()} and np.array([]) for a in []]) if False else None

# Degree-4 candidates via all brackets of degrees (1,3),(2,2),(3,1).
L4_candidates = []
for a in X:
    for b in L3_candidates:
        L4_candidates.append(bracket(a, b))
for a in L2:
    for b in L2:
        L4_candidates.append(bracket(a, b))
for a in L3_candidates:
    for b in X:
        L4_candidates.append(bracket(a, b))
L4_matrix = np.column_stack([vec4(a) for a in L4_candidates])
dimL4 = rank3(L4_matrix)
assert dimL4 == 60

# ---------- TRUE recursive relation component ----------
# (R)_3 = [L_1,R], then (R)_4 = [L_1,(R)_3].
R3 = [bracket(x, R) for x in X]
words3, index3 = make_index(3)

def vec3(A):
    v = np.zeros(64, dtype=int)
    for w, c in A.items():
        v[index3[w]] = c % P
    return v

R3_matrix = np.column_stack([vec3(a) for a in R3])
dimR3 = rank3(R3_matrix)
assert dimR3 == 4

R4 = [bracket(x, r3) for x in X for r3 in R3]
R4_matrix = np.column_stack([vec4(a) for a in R4])
dimR4 = rank3(R4_matrix)
assert dimR4 == 15
dimQ4 = dimL4 - dimR4
assert dimQ4 == 45

# ---------- Symplectic matrix ----------
J = np.array([[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]]) % 3

# ---------- Target T ----------
T = bracket(bracket(bracket(X3, X4), X1), X1)

g0 = np.array([[1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) % 3
phase1_symp = np.array_equal((g0.T @ J @ g0) % 3, J)
Y1 = add(X1, X2)
g0T = bracket(bracket(bracket(X3, X4), Y1), Y1)
d0 = add(g0T, neg(T))
R4_aug = np.column_stack([R4_matrix, vec4(d0)])
r1 = rank3(R4_matrix)
r2 = rank3(R4_aug)

# ---------- Symplectic action ----------
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

nonzero_vectors = [np.array(v, dtype=int) for v in product(range(3), repeat=4) if any(v)]
transvection_dict = {matrix_key(transvection(v)): transvection(v) for v in nonzero_vectors}
transvections = list(transvection_dict.values())
assert len(transvections) == 40
assert all(np.array_equal((g.T @ J @ g) % 3, J) for g in transvections)

generating_vectors = [(1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1), (1,0,1,0)]
gens = [transvection(v) for v in generating_vectors]
group_order = generated_group_size(gens)
assert group_order == 51840

# ---------- Orbit span W in the TRUE Q4 ----------
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

dimW = len(basis)
combined_rank = rank3(combined)
assert dimW == 45
assert combined_rank == 60

# Coordinate system on (R)_4 + W = L4.
r4_indices, R4_ind = independent_columns(R4_matrix)
assert len(r4_indices) == 15
B = np.column_stack([R4_ind] + [vec4(a) for a in basis])
assert B.shape == (256, 60)
assert rank3(B) == 60

selected_rows = []
row_matrix = np.empty((0, 60), dtype=int)
row_rank = 0
for i in range(256):
    candidate = np.vstack([row_matrix, B[i:i+1, :]])
    new_rank = rank3(candidate)
    if new_rank > row_rank:
        selected_rows.append(i)
        row_matrix = candidate
        row_rank = new_rank
        if row_rank == 60:
            break
assert len(selected_rows) == 60
B_inv = inverse3(B[selected_rows, :])

def coordinates(v):
    return (B_inv @ (v[selected_rows] % 3)) % 3

# ---------- W action and invariant-space calculation ----------
action_matrices = []
for g in gens:
    C = np.column_stack([coordinates(vec4(apply_linear_map(a, g))) for a in basis])
    A = C[15:, :]
    assert A.shape == (45, 45)
    action_matrices.append(A)
M = np.vstack([(A - np.eye(45, dtype=int)) % 3 for A in action_matrices])
rank_M = rank3(M)
dim_invariants = 45 - rank_M
assert rank_M == 45
assert dim_invariants == 0

print('PHASE 1 / TRUE RECURSIVE RELATION')
print('dim L4 =', dimL4)
print('dim (R)_3 =', dimR3)
print('dim (R)_4 =', dimR4)
print('dim Q4 =', dimQ4)
print('g0 symplectic =', phase1_symp)
print('rank(R4) =', r1)
print('rank([R4 | gT-T]) =', r2)
print()
print('PHASE 2-1 / TRUE Q4')
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
print('ALL PHASE 2-1 TRUE-RELATION CHECKS PASSED')
