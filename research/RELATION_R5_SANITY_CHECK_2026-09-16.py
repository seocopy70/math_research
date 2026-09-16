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


def independent_basis(candidates, degree, target):
    chosen = []
    M = np.empty((4 ** degree, 0), dtype=np.int64)
    r = 0
    for a in candidates:
        c = vec(a, degree)
        C = np.column_stack([M, c])
        nr = rank3(C)
        if nr > r:
            chosen.append(a)
            M = C
            r = nr
            if r == target:
                break
    return chosen, M


# Independent reconstruction of the quadratic relator.
X = [{(i + 1,): 1} for i in range(4)]
L2 = [bracket(X[i], X[j]) for i in range(4) for j in range(i + 1, 4)]
R = add(L2[0], L2[5])

# First relation layer: exactly four degree-3 generators.
R3 = [bracket(x, R) for x in X]
assert len(R3) == 4
assert all(all(len(w) == 3 for w in a) for a in R3)
assert rank3(np.column_stack([vec(a, 3) for a in R3])) == 4

# True degree-4 relation space: generate only [L1,(R)_3], then extract 15 basis vectors.
R4_candidates = [bracket(x, r3) for x in X for r3 in R3]
assert len(R4_candidates) == 16
assert all(all(len(w) == 4 for w in a) for a in R4_candidates)
R4_basis, R4_basis_matrix = independent_basis(R4_candidates, 4, target=15)
assert len(R4_basis) == 15
assert rank3(R4_basis_matrix) == 15

# Critical input audit: R5 must use these 15 degree-4 basis vectors, not L4.
R5_candidates = [bracket(x, r4) for x in X for r4 in R4_basis]
assert len(R5_candidates) == 4 * len(R4_basis) == 60
assert all(all(len(w) == 5 for w in a) for a in R5_candidates)

# Independent degree-5 ambient check: Witt dimension for free Lie algebra L_5 on 4 generators is 204.
L3_candidates = [bracket(a, x) for a in L2 for x in X]
L3_basis, _ = independent_basis(L3_candidates, 3, target=20)
L4_candidates = [bracket(x, b) for x in L3_basis for b in X]
L4_basis, _ = independent_basis(L4_candidates, 4, target=60)
L5_candidates = [bracket(x, b) for x in L4_basis for b in X]
L5_basis, _ = independent_basis(L5_candidates, 5, target=204)
assert len(L5_basis) == 204

R5_matrix = np.column_stack([vec(a, 5) for a in R5_candidates])
dim_R5 = rank3(R5_matrix)

# Cross-check: all 60 local brackets are already the full generated column set;
# no hidden degree-4/L4 input is involved.
assert R5_matrix.shape == (4 ** 5, 60)
assert dim_R5 == 60

print("R5 INPUT + DEGREE SANITY CHECK — 2026-09-16")
print("=============================================")
print("len(R3 candidates) =", len(R3))
print("dim (R)_3 =", 4)
print("len((R)_4 raw candidates) =", len(R4_candidates))
print("len((R)_4 independent basis) =", len(R4_basis))
print("dim (R)_4 =", rank3(R4_basis_matrix))
print("R5 input basis dimension =", len(R4_basis))
print("len([L1,(R)_4] raw candidates) =", len(R5_candidates))
print("all R5 input vectors have degree =", sorted({len(w) for a in R4_basis for w in a}))
print("all R5 output vectors have degree =", sorted({len(w) for a in R5_candidates for w in a}))
print("L5 ambient independent dimension =", len(L5_basis))
print("R5 matrix shape =", R5_matrix.shape)
print("dim [L1,(R)_4] =", dim_R5)
print("RESULT: R5 uses exactly the 15-dimensional (R)_4 basis.")
print("RESULT: no L4 vectors are used as R5 inputs.")
print("RESULT: every R5 output is a genuine degree-5 associative word vector.")
print("RESULT: L5 ambient dimension is 204, and R5 has rank 60 inside it.")
print("ALL R5 SANITY CHECKS PASSED")
