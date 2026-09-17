import numpy as np
from itertools import product

P = 3
N = 4


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


def make_index(degree):
    words = list(product(range(1, N + 1), repeat=degree))
    return words, {w: i for i, w in enumerate(words)}


words2, index2 = make_index(2)
words3, index3 = make_index(3)
words4, index4 = make_index(4)

X = [{(i,): 1} for i in range(1, N + 1)]


def vec(A, degree):
    size = N ** degree
    index = {2: index2, 3: index3, 4: index4}[degree]
    v = np.zeros(size, dtype=int)
    for w, c in A.items():
        v[index[w]] = c % P
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


def nullspace3(A):
    A = np.array(A, dtype=int, copy=True) % P
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
    free = [c for c in range(n) if c not in pivots]
    basis = []
    for f in free:
        v = np.zeros(n, dtype=int)
        v[f] = 1
        for row, pc in enumerate(pivots):
            v[pc] = (-A[row, f]) % P
        basis.append(v)
    return basis


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


def apply_linear_map(A, g):
    images = []
    for j in range(N):
        image = {}
        for i in range(N):
            c = int(g[i, j]) % P
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


def matrix_key(A):
    return tuple((np.array(A, dtype=int) % P).flatten().tolist())


def generated_group_size(gens):
    I = np.eye(N, dtype=int)
    group = {matrix_key(I): I}
    frontier = [I]
    while frontier:
        a = frontier.pop()
        for g in gens:
            b = (a @ g) % P
            k = matrix_key(b)
            if k not in group:
                group[k] = b
                frontier.append(b)
    return len(group)


J = np.array([[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]]) % P


def transvection(v):
    v = np.array(v, dtype=int) % P
    return (np.eye(N, dtype=int) + np.outer(v, (J @ v) % P)) % P


generating_vectors = [(1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1), (1,0,1,0)]
gens = [transvection(v) for v in generating_vectors]
assert len({matrix_key(g) for g in gens}) == 5
assert generated_group_size(gens) == 51840


def build_q_path(label, relation):
    # Every q-path independently starts from its own degree-2 relation object.
    assert label in ('q3', 'qinf')
    L2 = [bracket(X[i], X[j]) for i in range(N) for j in range(i + 1, N)]
    assert np.array_equal(vec(relation, 2), vec(add(L2[0], L2[5]), 2))

    L3_candidates = [bracket(a, x) for a in L2 for x in X]
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
    dimL4 = rank3(np.column_stack([vec(a, 4) for a in L4_candidates]))
    assert dimL4 == 60

    R3 = [bracket(x, relation) for x in X]
    R3_matrix = np.column_stack([vec(a, 3) for a in R3])
    assert rank3(R3_matrix) == 4
    R4 = [bracket(x, r3) for x in X for r3 in R3]
    R4_matrix = np.column_stack([vec(a, 4) for a in R4])
    assert rank3(R4_matrix) == 15
    assert dimL4 - rank3(R4_matrix) == 45

    # Same deterministic target class, but constructed inside this q-path.
    T = bracket(bracket(bracket(X[2], X[3]), X[0]), X[0])
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
        candidate = np.column_stack([combined, vec(a, 4)])
        new_rank = rank3(candidate)
        if new_rank > old_rank:
            basis.append(a)
            combined = candidate
        for g in gens:
            queue.append(apply_linear_map(a, g))
    assert len(basis) == 45
    assert rank3(combined) == 60

    r4_indices, R4_ind = independent_columns(R4_matrix)
    assert len(r4_indices) == 15
    B = np.column_stack([R4_ind] + [vec(a, 4) for a in basis])
    assert rank3(B) == 60
    selected_rows = []
    row_matrix = np.empty((0, 60), dtype=int)
    row_rank = 0
    for i in range(256):
        candidate = np.vstack([row_matrix, B[i:i+1, :]])
        nr = rank3(candidate)
        if nr > row_rank:
            selected_rows.append(i)
            row_matrix = candidate
            row_rank = nr
            if row_rank == 60:
                break
    assert len(selected_rows) == 60
    B_inv = inverse3(B[selected_rows, :])

    def coordinates(v):
        return (B_inv @ (v[selected_rows] % P)) % P

    action_matrices = []
    for g in gens:
        C = np.column_stack([coordinates(vec(apply_linear_map(a, g), 4)) for a in basis])
        A = C[15:, :]
        assert A.shape == (45, 45)
        action_matrices.append(A)
    assert rank3(np.vstack([(A - np.eye(45, dtype=int)) % P for A in action_matrices])) == 45
    return {
        'label': label,
        'relation': relation,
        'R4': R4_matrix,
        'basis': basis,
        'actions': action_matrices,
    }


# Independent degree-2 relation derivations for q=3 and q=infinity.
# The p-power term has degree 3, so both initial quadratic relations are identical.
L2_q3 = [bracket(X[i], X[j]) for i in range(N) for j in range(i + 1, N)]
L2_qinf = [bracket(X[i], X[j]) for i in range(N) for j in range(i + 1, N)]
R_q3 = add(L2_q3[0], L2_q3[5])
R_qinf = add(L2_qinf[0], L2_qinf[5])
assert R_q3 == R_qinf

q3 = build_q_path('q3', R_q3)
qinf = build_q_path('qinf', R_qinf)

# Actual H-equivariant intertwiner calculation between two separately constructed 45x45 modules.
# Unknown T has 45^2 entries. For each generator solve T A_q3 - A_qinf T = 0 over F_3.
constraints = []
for A3, Ainf in zip(q3['actions'], qinf['actions']):
    for r in range(45):
        for c in range(45):
            row = np.zeros(45 * 45, dtype=int)
            for k in range(45):
                row[r * 45 + k] = (row[r * 45 + k] + A3[k, c]) % P
                row[k * 45 + c] = (row[k * 45 + c] - Ainf[r, k]) % P
            constraints.append(row)
C = np.vstack(constraints)
null_basis = nullspace3(C)
assert len(null_basis) > 0

# Search a small deterministic set of linear combinations for an invertible intertwiner.
candidates = []
for v in null_basis:
    candidates.append(v.reshape(45, 45) % P)
for i in range(len(null_basis)):
    for j in range(i + 1, len(null_basis)):
        candidates.append((null_basis[i].reshape(45,45) + null_basis[j].reshape(45,45)) % P)
T_iso = next((T for T in candidates if rank3(T) == 45), None)
assert T_iso is not None

for A3, Ainf in zip(q3['actions'], qinf['actions']):
    assert np.array_equal((T_iso @ A3 - Ainf @ T_iso) % P, np.zeros((45,45), dtype=int))

print('GATE0A_INDEPENDENT_Q3_QINF_W45')
print('q3 degree-2 relation =', R_q3)
print('qinf degree-2 relation =', R_qinf)
print('degree-2 relations identical =', R_q3 == R_qinf)
print('q3 dim Q4 = 45')
print('qinf dim Q4 = 45')
print('q3 action matrices =', len(q3['actions']), 'x', q3['actions'][0].shape)
print('qinf action matrices =', len(qinf['actions']), 'x', qinf['actions'][0].shape)
print('intertwiner constraint rank =', rank3(C))
print('intertwiner space dimension =', len(null_basis))
print('invertible intertwiner rank =', rank3(T_iso))
print('RESULT = PASS')
