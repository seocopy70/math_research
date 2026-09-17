import numpy as np
from itertools import product

P = 3
D4 = 256
WORDS4 = list(product(range(1, 5), repeat=4))
INDEX4 = {w: i for i, w in enumerate(WORDS4)}


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


def vec4(A):
    v = np.zeros(D4, dtype=np.int64)
    for w, c in A.items():
        v[INDEX4[w]] = c % P
    return v


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
    r = 0
    piv = []
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
        piv.append(c)
        r += 1
    free = [c for c in range(n) if c not in piv]
    Z = np.zeros((n, len(free)), dtype=np.int64)
    for j, f in enumerate(free):
        Z[f, j] = 1
        for rr, c in enumerate(piv):
            Z[c, j] = (-A[rr, f]) % P
    return Z


def apply_linear_map(A, g):
    images = []
    for j in range(4):
        image = {}
        for i in range(4):
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


def transvection(v):
    J = np.array([[0, 1, 0, 0], [-1, 0, 0, 0],
                  [0, 0, 0, 1], [0, 0, -1, 0]], dtype=np.int64) % P
    v = np.array(v, dtype=np.int64) % P
    return (np.eye(4, dtype=np.int64) + np.outer(v, (J @ v) % P)) % P


def independent_columns(M, target):
    B = np.empty((M.shape[0], 0), dtype=np.int64)
    r = 0
    for j in range(M.shape[1]):
        C = np.column_stack([B, M[:, j]])
        q = rank3(C)
        if q > r:
            B, r = C, q
            if r == target:
                break
    assert r == target
    return B


def orbit_basis(seed, gens, target, modulo):
    basis = []
    combined = modulo.copy()
    queue = [seed]
    seen = set()
    while queue:
        a = queue.pop(0)
        key = tuple(vec4(a).tolist())
        if key in seen:
            continue
        seen.add(key)
        old = rank3(combined)
        cand = np.column_stack([combined, vec4(a)])
        new = rank3(cand)
        if new > old:
            basis.append(a)
            combined = cand
            if len(basis) == target:
                break
        for g in gens:
            queue.append(apply_linear_map(a, g))
    assert len(basis) == target
    return basis

# Build the same TRUE Q4 data independently.
X = [{(1,): 1}, {(2,): 1}, {(3,): 1}, {(4,): 1}]
L2 = [bracket(X[i], X[j]) for i in range(4) for j in range(i + 1, 4)]
R = add(L2[0], L2[5])
R3 = [bracket(x, R) for x in X]
R4 = [bracket(x, r) for x in R3 for r in X]
# Order above is immaterial for the span; retain rank check.
R4_matrix = np.column_stack([vec4(a) for a in R4])
assert rank3(R4_matrix) == 15

J = np.array([[0, 1, 0, 0], [-1, 0, 0, 0],
              [0, 0, 0, 1], [0, 0, -1, 0]], dtype=np.int64) % P
generating_vectors = [(1, 0, 0, 0), (0, 1, 0, 0),
                      (0, 0, 1, 0), (0, 0, 0, 1), (1, 0, 1, 0)]
gens = [transvection(v) for v in generating_vectors]
assert all(np.array_equal((g.T @ J @ g) % P, J) for g in gens)

T = bracket(bracket(bracket(X[2], X[3]), X[0]), X[0])
d = bracket({(1, 1, 1): 1}, {(2,): 1})
W_basis = orbit_basis(T, gens, 45, R4_matrix)
W = np.column_stack([vec4(a) for a in W_basis])
assert rank3(W) == 45
assert rank3(np.column_stack([R4_matrix, W])) == 60

# W is a quotient subspace modulo R4, not necessarily an invariant complement.
# Therefore the action must be computed in [R4 | W] coordinates and projected to Q4.
R4_ind = independent_columns(R4_matrix, 15)
Qbasis = np.column_stack([R4_ind, W])
assert rank3(Qbasis) == 60

# Select 60 pivot rows once and invert that square coordinate system.
rows = []
RM = np.empty((0, 60), dtype=np.int64)
rr = 0
for i in range(256):
    cand = np.vstack([RM, Qbasis[i:i+1, :]])
    nr = rank3(cand)
    if nr > rr:
        rows.append(i)
        RM, rr = cand, nr
        if rr == 60:
            break
assert len(rows) == 60

def inverse3(A):
    A = np.array(A, dtype=np.int64) % P
    n = A.shape[0]
    M = np.concatenate([A, np.eye(n, dtype=np.int64)], axis=1)
    for c in range(n):
        q = next((i for i in range(c, n) if M[i, c]), None)
        assert q is not None
        M[[c, q]] = M[[q, c]]
        if M[c, c] == 2:
            M[c] = (2 * M[c]) % P
        for i in range(n):
            if i != c and M[i, c]:
                M[i] = (M[i] - M[i, c] * M[c]) % P
    return M[:, n:]

Qinv = inverse3(Qbasis[rows, :])

def qcoords(v):
    return (Qinv @ (v[rows] % P)) % P

AW = []
for g in gens:
    cols = []
    for j in range(45):
        v = vec4(apply_linear_map({w: int(c) for w, c in zip(WORDS4, W[:, j]) if int(c) % P}, g))
        full = qcoords(v)
        cols.append(full[15:])
    A = np.column_stack(cols) % P
    assert A.shape == (45, 45)
    AW.append(A)
AW = np.stack(AW)

# Independent convention check: Wd is not needed here. First verify quotient action is closed.
# Reproduce Phase 2-3's cyclic test exactly.
B = (AW[1] + AW[2] + AW[3] + AW[4]) % P
powers = []
cur = np.eye(45, dtype=np.int64)
for _ in range(45):
    powers.append(cur.copy())
    cur = (cur @ B) % P
Krylov = np.column_stack([X.reshape(-1) for X in powers]) % P
krylov_rank = rank3(Krylov)

# If cyclicity is restored, independently recover End_H(W) and the square-zero rank-10 N.
end_dim = None
N = None
N_rank = None
N_kernel = None
if krylov_rank == 45:
    Ecols = []
    for Pk in powers:
        pieces = [((Pk @ A - A @ Pk) % P).reshape(-1) for A in AW]
        Ecols.append(np.concatenate(pieces))
    E = np.column_stack(Ecols) % P
    Z = nullspace3(E)
    end_dim = Z.shape[1]
    end_basis = []
    for j in range(end_dim):
        Xj = np.zeros((45, 45), dtype=np.int64)
        for t in range(45):
            Xj = (Xj + int(Z[t, j]) * powers[t]) % P
        end_basis.append(Xj)
    for a in range(3):
        for b in range(3):
            if a == 0 and b == 0:
                continue
            Xab = (a * end_basis[0] + b * end_basis[1]) % P if end_dim == 2 else None
            if Xab is not None and rank3(Xab) == 10 and np.array_equal((Xab @ Xab) % P, np.zeros((45,45), dtype=np.int64)):
                N = Xab
                break
        if N is not None:
            break
    if N is not None:
        N_rank = rank3(N)
        N_kernel = 45 - N_rank

print('A3-4 N RECON DIAGNOSTIC')
print('W dimension =', rank3(W))
print('Q4 dimension =', 45)
print('action construction = quotient projection from [R4 | W]')
print('Krylov rank =', krylov_rank)
print('End_H(W) dimension =', end_dim)
print('rank N =', N_rank)
print('dim ker N =', N_kernel)
print('N^2 = 0 =', N is not None)
print('DIAGNOSTIC PASS =', krylov_rank == 45 and end_dim == 2 and N is not None and N_rank == 10 and N_kernel == 35)
