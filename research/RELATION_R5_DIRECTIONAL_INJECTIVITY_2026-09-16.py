from itertools import product
import numpy as np

P = 3


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


def vec(A, degree):
    words = list(product(range(1, 5), repeat=degree))
    index = {w: i for i, w in enumerate(words)}
    v = np.zeros(4 ** degree, dtype=np.int64)
    for w, c in A.items():
        if len(w) != degree:
            raise AssertionError(f"wrong word degree: expected {degree}, got {len(w)}")
        v[index[w]] = c % P
    return v


def rank3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    if A.ndim == 1:
        A = A[:, None]
    m, n = A.shape
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i, c]), None)
        if piv is None:
            continue
        if piv != r:
            A[[r, piv]] = A[[piv, r]]
        if A[r, c] == 2:
            A[r] = (2 * A[r]) % P
        for i in range(m):
            if i != r and A[i, c]:
                A[i] = (A[i] - A[i, c] * A[r]) % P
        r += 1
        if r == m:
            break
    return r


# Independent reconstruction of R = [X1,X2] + [X3,X4].
X = [{(i + 1,): 1} for i in range(4)]
L2 = [bracket(X[i], X[j]) for i in range(4) for j in range(i + 1, 4)]
R = add(L2[0], L2[5])

# Recursive relation layers.
R3 = [bracket(x, R) for x in X]
assert rank3(np.column_stack([vec(a, 3) for a in R3])) == 4

R4_candidates = [bracket(x, r3) for x in X for r3 in R3]
R4_matrix = np.column_stack([vec(a, 4) for a in R4_candidates])

# Extract an explicit 15-dimensional basis of (R)_4 by incremental rank.
R4_basis = []
M = np.empty((4 ** 4, 0), dtype=np.int64)
r = 0
for a in R4_candidates:
    c = vec(a, 4)
    C = np.column_stack([M, c])
    nr = rank3(C)
    if nr > r:
        R4_basis.append(a)
        M = C
        r = nr
assert len(R4_basis) == 15
assert r == 15

# Directional maps ad(X_i): (R)_4 -> L_5.
directional = []
for i, x in enumerate(X, start=1):
    cols = [vec(bracket(x, r4), 5) for r4 in R4_basis]
    Mi = np.column_stack(cols)
    ri = rank3(Mi)
    ki = len(R4_basis) - ri
    assert Mi.shape == (4 ** 5, 15)
    directional.append(Mi)
    print(f"rank ad(X{i})|_(R4) = {ri}")
    print(f"kernel dimension = {ki}")

# The global R5 space is the span of all four directional images.
combined = np.column_stack(directional)
combined_rank = rank3(combined)
print("combined rank =", combined_rank)
print("sum of individual ranks =", sum(rank3(Mi) for Mi in directional))
print("number of directional columns =", combined.shape[1])

# Fundamental consistency checks.
assert combined.shape == (4 ** 5, 60)
assert combined_rank == 60

print("ALL DIRECTIONAL R5 INJECTIVITY / COMBINED-RANK CHECKS PASSED")
