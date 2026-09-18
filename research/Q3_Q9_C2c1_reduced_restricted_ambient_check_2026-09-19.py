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


def power(A, n):
    out = {(): 1}
    for _ in range(n):
        out = mul(out, A)
    return out


def vec(A, degree, generators):
    words = list(product(range(generators), repeat=degree))
    index = {w: i for i, w in enumerate(words)}
    v = np.zeros(generators ** degree, dtype=np.int64)
    for w, c in A.items():
        v[index[w]] = c % P
    return v


def rank3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    if A.ndim == 1:
        A = A[:, None]
    rows, cols = A.shape
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if A[i, c]), None)
        if pivot is None:
            continue
        A[[r, pivot]] = A[[pivot, r]]
        if A[r, c] == 2:
            A[r] = (2 * A[r]) % P
        for i in range(rows):
            if i != r and A[i, c]:
                A[i] = (A[i] - A[i, c] * A[r]) % P
        r += 1
        if r == rows:
            break
    return r


def independent(candidates, degree, generators):
    M = np.empty((generators ** degree, 0), dtype=np.int64)
    basis = []
    r = 0
    for a in candidates:
        v = vec(a, degree, generators)
        C = np.column_stack([M, v])
        rr = rank3(C)
        if rr > r:
            basis.append(a)
            M = C
            r = rr
    return basis, M


def lie_basis(generators, max_degree):
    X = [{(i,): 1} for i in range(generators)]
    basis = {1: X}
    for n in range(2, max_degree + 1):
        candidates = []
        for i in range(1, n):
            for a in basis[i]:
                for b in basis[n - i]:
                    candidates.append(bracket(a, b))
        basis[n], _ = independent(candidates, n, generators)
    return basis


# Check 1: the repository's four-generator degree-3 restricted convention.
X4 = [{(i,): 1} for i in range(4)]
L2_4 = [bracket(X4[i], X4[j]) for i in range(4) for j in range(i + 1, 4)]
L3_4_candidates = [bracket(a, x) for a in L2_4 for x in X4]
L3_4, _ = independent(L3_4_candidates, 3, 4)
restricted3_4 = np.column_stack(
    [vec(a, 3, 4) for a in L3_4 + [power(x, 3) for x in X4]]
)
assert len(L3_4) == 20
assert rank3(restricted3_4) == 24

# Check 2: reduced two-generator degree-9 model.
B = lie_basis(2, 9)
L9_2 = B[9]
p3_2 = [power(a, 3) for a in B[3]]
p9_2 = [power(a, 9) for a in B[1]]
ambient2 = np.column_stack(
    [vec(a, 9, 2) for a in L9_2 + p3_2 + p9_2]
)
rank2 = rank3(ambient2)

assert len(L9_2) == 56
assert len(B[3]) == 2
assert len(B[1]) == 2
assert rank2 == 60

print("C-2c-1 REDUCED RESTRICTED AMBIENT CHECK")
print("4-generator degree-3 restricted ambient rank =", rank3(restricted3_4))
print("expected degree-3 rank = 24")
print("2-generator degree-9 ordinary Lie rank =", len(L9_2))
print("2-generator degree-9 L3^[3] layer =", len(p3_2))
print("2-generator degree-9 L1^[9] layer =", len(p9_2))
print("2-generator degree-9 restricted ambient rank =", rank2)
print("expected reduced rank = 56 + 2 + 2 = 60")
print("RESULT: PASS")
