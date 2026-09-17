import json
import numpy as np
from itertools import product
from pathlib import Path

P = 3
D1 = 4
OUT = Path('artifacts/a3_4_data.npz')
META = Path('artifacts/a3_4_data_meta.json')
OUT.parent.mkdir(parents=True, exist_ok=True)

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


def vec4(A):
    v = np.zeros(256, dtype=np.int64)
    for w, c in A.items():
        v[INDEX4[w]] = c % P
    return v


def apply_linear_map(A, g):
    images = []
    for j in range(D1):
        image = {}
        for i in range(D1):
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


def basis_columns(M, target):
    B = np.empty((M.shape[0], 0), dtype=np.int64)
    r = 0
    for j in range(M.shape[1]):
        C = np.column_stack([B, M[:, j]])
        q = rank3(C)
        if q > r:
            B = C
            r = q
            if r == target:
                break
    assert r == target
    return B


def orbit_basis(seed, gens, target, modulo=None):
    basis = []
    combined = np.empty((256, 0), dtype=np.int64) if modulo is None else modulo.copy()
    queue = [seed]
    seen = set()
    while queue:
        a = queue.pop(0)
        key = tuple(vec4(a).tolist())
        if key in seen:
            continue
        seen.add(key)
        old_rank = rank3(combined)
        candidate = np.column_stack([combined, vec4(a)])
        new_rank = rank3(candidate)
        if new_rank > old_rank:
            basis.append(a)
            combined = candidate
            if len(basis) == target:
                break
        for g in gens:
            queue.append(apply_linear_map(a, g))
    assert len(basis) == target
    return basis


# Ambient degree-4 construction. No phase script is imported or executed.
X = [{(1,): 1}, {(2,): 1}, {(3,): 1}, {(4,): 1}]
L2 = [bracket(X[i], X[j]) for i in range(4) for j in range(i + 1, 4)]
R = add(L2[0], L2[5])
R3 = [bracket(x, R) for x in X]
R4 = [bracket(x, r3) for x in X for r3 in R3]
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
W_basis = orbit_basis(T, gens, 45, modulo=R4_matrix)
W = np.column_stack([vec4(a) for a in W_basis])
assert rank3(W) == 45
assert rank3(np.column_stack([R4_matrix, W])) == 60

orbit = [d]
seen = {tuple(vec4(d).tolist())}
for a in orbit:
    for g in gens:
        b = apply_linear_map(a, g)
        key = tuple(vec4(b).tolist())
        if key not in seen:
            seen.add(key)
            orbit.append(b)
assert len(orbit) == 360
Wd = basis_columns(np.column_stack([vec4(a) for a in orbit]), 45)
assert rank3(Wd) == 45

# Intersection I = W ∩ Wd, stored by ambient coordinates and by coordinates in W/Wd.
# Solve W*a = Wd*b over F_3.
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
        if r == m:
            break
    free = [c for c in range(n) if c not in piv]
    Z = np.zeros((n, len(free)), dtype=np.int64)
    for j, f in enumerate(free):
        Z[f, j] = 1
        for rr, c in enumerate(piv):
            Z[c, j] = (-A[rr, f]) % P
    return Z

Z = nullspace3(np.column_stack([W, (-Wd) % P]))
assert Z.shape[1] == 35
I_W = Z[:45, :] % P
I_Wd = Z[45:, :] % P
I_ambient = (W @ I_W) % P
assert rank3(I_ambient) == 35

np.savez_compressed(
    OUT,
    W=W.astype(np.int8),
    Wd=Wd.astype(np.int8),
    gens=np.stack(gens).astype(np.int8),
    R4=R4_matrix.astype(np.int8),
    I_W=I_W.astype(np.int8),
    I_Wd=I_Wd.astype(np.int8),
    I_ambient=I_ambient.astype(np.int8),
)
meta = {
    'schema': 'A3-4-data-v1',
    'field': 'F3',
    'W_shape': list(W.shape),
    'Wd_shape': list(Wd.shape),
    'R4_shape': list(R4_matrix.shape),
    'I_dimension': int(rank3(I_ambient)),
    'generator_count': len(gens),
    'source': 'research/A3_4_BUILD_DATA_2026-09-17.py',
    'policy': 'downstream jobs must read this artifact and must not import/execute phase scripts',
}
META.write_text(json.dumps(meta, indent=2) + '\n', encoding='utf-8')
print('A3-4 BUILD DATA')
print('No phase script imported or executed.')
print('dim W45 =', rank3(W))
print('dim Wd =', rank3(Wd))
print('dim I =', rank3(I_ambient))
print('artifact =', OUT)
print('schema =', meta['schema'])
