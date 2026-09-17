import json
import os
import numpy as np
from itertools import product
from pathlib import Path

P = 3
D1 = 4
D4 = 256
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


def vec4(A):
    v = np.zeros(D4, dtype=np.int64)
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
    combined = np.empty((D4, 0), dtype=np.int64) if modulo is None else modulo.copy()
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


def independent_columns(M, target):
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

# Correct quotient action: W lives in Q4 = L4/(R4), so gW is only
# determined modulo R4. Use [R4 | W] coordinates and project away R4.
R4_ind = independent_columns(R4_matrix, 15)
Qbasis = np.column_stack([R4_ind, W])
assert rank3(Qbasis) == 60
rows = []
RM = np.empty((0, 60), dtype=np.int64)
rr = 0
for i in range(D4):
    cand = np.vstack([RM, Qbasis[i:i+1, :]])
    nr = rank3(cand)
    if nr > rr:
        rows.append(i)
        RM = cand
        rr = nr
        if rr == 60:
            break
assert len(rows) == 60
Qinv = inverse3(Qbasis[rows, :])

def qcoords(v):
    return (Qinv @ (v[rows] % P)) % P


def action_matrix(B, g):
    # B is a 45-column representative matrix in ambient L4 coordinates.
    # The first 15 quotient coordinates are R4; the last 45 are W.
    Qbasis_local = Qbasis if B is W else np.column_stack([R4_ind, B])
    rows_local = rows if B is W else None
    if B is W:
        inv_local = Qinv
    else:
        rows2 = []
        RM2 = np.empty((0, 60), dtype=np.int64)
        rr2 = 0
        for i in range(D4):
            cand2 = np.vstack([RM2, Qbasis_local[i:i+1, :]])
            nr2 = rank3(cand2)
            if nr2 > rr2:
                rows2.append(i)
                RM2 = cand2
                rr2 = nr2
                if rr2 == 60:
                    break
        assert len(rows2) == 60
        inv_local = inverse3(Qbasis_local[rows2, :])
        rows_local = rows2
    cols = []
    for j in range(B.shape[1]):
        v = vec4(apply_linear_map(
            {w: int(c) for w, c in zip(WORDS4, B[:, j]) if int(c) % P}, g))
        full = (inv_local @ (v[rows_local] % P)) % P
        cols.append(full[15:])
    return np.column_stack(cols) % P

AW = np.stack([action_matrix(W, g) for g in gens]).astype(np.int64)
AWd = np.stack([action_matrix(Wd, g) for g in gens]).astype(np.int64)

# Historical Phase-2-3 N construction, reproduced independently.
Bcomm = (AW[1] + AW[2] + AW[3] + AW[4]) % P
powers = []
cur = np.eye(45, dtype=np.int64)
for _ in range(45):
    powers.append(cur.copy())
    cur = (cur @ Bcomm) % P
Krylov = np.column_stack([p.reshape(-1) for p in powers]) % P
assert rank3(Krylov) == 45

comm_blocks = []
for A in AW:
    cols = [((Xp @ A - A @ Xp) % P).reshape(-1) for Xp in powers]
    comm_blocks.append(np.column_stack(cols))
C = np.vstack(comm_blocks) % P
Zcomm = nullspace3(C)
assert Zcomm.shape[1] == 2
end_basis = []
for j in range(2):
    Xj = np.zeros((45, 45), dtype=np.int64)
    for t in range(45):
        Xj = (Xj + int(Zcomm[t, j]) * powers[t]) % P
    end_basis.append(Xj)
I45 = np.eye(45, dtype=np.int64) % P
assert any(np.array_equal(Xj, I45) for Xj in end_basis)

N = None
for a in range(3):
    for b in range(3):
        if a == 0 and b == 0:
            continue
        Xab = (a * end_basis[0] + b * end_basis[1]) % P
        if rank3(Xab) == 10 and np.array_equal((Xab @ Xab) % P,
                                                np.zeros((45, 45), dtype=np.int64)):
            N = Xab
            break
    if N is not None:
        break
assert N is not None
assert all(np.array_equal((N @ A - A @ N) % P,
                          np.zeros((45, 45), dtype=np.int64)) for A in AW)
assert np.array_equal((N @ N) % P, np.zeros((45, 45), dtype=np.int64))
assert rank3(N) == 10
K_N = nullspace3(N)
assert K_N.shape == (45, 35)
assert rank3(K_N) == 35

# Intersection I = W ∩ Wd.
Z = nullspace3(np.column_stack([W, (-Wd) % P]))
assert Z.shape[1] == 35
I_W = Z[:45, :] % P
I_Wd = Z[45:, :] % P
I_ambient = (W @ I_W) % P
assert rank3(I_ambient) == 35
K_I_rank = rank3(np.column_stack([K_N, I_W]))
K_EQUALS_I = (K_I_rank == 35)

np.savez_compressed(
    OUT,
    W=W.astype(np.int8),
    Wd=Wd.astype(np.int8),
    gens=np.stack(gens).astype(np.int8),
    R4=R4_matrix.astype(np.int8),
    I_W=I_W.astype(np.int8),
    I_Wd=I_Wd.astype(np.int8),
    I_ambient=I_ambient.astype(np.int8),
    AW=AW.astype(np.int8),
    AWd=AWd.astype(np.int8),
    N=N.astype(np.int8),
    K_N=K_N.astype(np.int8),
)
meta = {
    'schema': 'A3-4-data-v2',
    'field': 'F3',
    'W_shape': list(W.shape),
    'Wd_shape': list(Wd.shape),
    'R4_shape': list(R4_matrix.shape),
    'I_dimension': int(rank3(I_ambient)),
    'generator_count': len(gens),
    'End_H_W_dimension': 2,
    'N_rank': int(rank3(N)),
    'N_kernel_dimension': int(K_N.shape[1]),
    'N_square_zero': True,
    'K_I_augmented_rank': int(K_I_rank),
    'K_N_equals_I': bool(K_EQUALS_I),
    'source': 'research/A3_4_BUILD_DATA_2026-09-17.py',
    'policy': 'downstream jobs must read this artifact and must not import/execute phase scripts',
    'action_coordinate_method': 'quotient projection from [R4_ind | W] in ambient degree-4 coordinates',
}
META.write_text(json.dumps(meta, indent=2) + '\n', encoding='utf-8')
print('A3-4 BUILD DATA v2')
print('No phase script imported or executed.')
print('GITHUB_SHA =', os.environ.get('GITHUB_SHA', 'UNKNOWN'))
print('dim W45 =', rank3(W))
print('dim Wd =', rank3(Wd))
print('dim I =', rank3(I_ambient))
print('dim End_H(W) =', 2)
print('N^2 = 0 =', True)
print('rank N =', rank3(N))
print('dim ker N =', K_N.shape[1])
print('rank [K_N | I] =', K_I_rank)
print('K_N = I =', K_EQUALS_I)
print('action coordinate method = quotient projection [R4 | W]')
print('artifact =', OUT)
print('schema =', meta['schema'])
