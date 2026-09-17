import importlib.util
import numpy as np

P = 3
SANITY_PATH = 'research/A3_4_10_BRACKET_PIPELINE_SANITY_2026-09-17.py'

# Reuse ONLY the verified standalone ambient/bracket pipeline.
# No Gate-0-A or any phase script is imported.
spec = importlib.util.spec_from_file_location('a3410_sanity', SANITY_PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

rank3 = mod.rank3
WORDS4 = mod.WORDS4
WORDS5 = mod.WORDS5
INDEX4 = mod.INDEX4
INDEX5 = mod.INDEX5
W = mod.W
Wd = mod.Wd
gens = mod.gens
apply_linear_map = mod.apply_linear_map


def coords(B, Y):
    B = np.array(B, dtype=np.int64) % P
    Y = np.array(Y, dtype=np.int64) % P
    out = np.zeros((B.shape[1], Y.shape[1]), dtype=np.int64)
    for j in range(Y.shape[1]):
        A = np.column_stack([B, Y[:, j]]) % P
        m, naug = A.shape
        r = 0
        piv = []
        for c in range(naug - 1):
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
        assert len(piv) == B.shape[1]
        for rr, c in enumerate(piv):
            out[c, j] = A[rr, -1]
    return out


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


def degree_action_matrix(g, words, index):
    dim = len(words)
    G = np.zeros((dim, dim), dtype=np.int64)
    for j, w in enumerate(words):
        out = apply_linear_map({w: 1}, g)
        for ww, c in out.items():
            G[index[ww], j] = (G[index[ww], j] + int(c)) % P
    return G


A4_ambient = [degree_action_matrix(g, WORDS4, INDEX4) for g in gens]
A_W = [coords(W, (G @ W) % P) for G in A4_ambient]
A_Wd = [coords(Wd, (G @ Wd) % P) for G in A4_ambient]

# Recover W45 ∩ Wd independently.
Z = nullspace3(np.column_stack([W, (-Wd) % P]))
assert Z.shape[1] == 35
I_W = Z[:45, :] % P
K_Wd = Z[45:, :] % P
K_ambient = (W @ I_W) % P
assert rank3(K_ambient) == 35
assert np.array_equal(K_ambient, (Wd @ K_Wd) % P)

# Reconstruct the unique A3-4-9 intertwiner fixed by K.
n = 45
Nvar = n * n
rows = []
rhs = []


def vi(r, c):
    return r * n + c


for A, Ad in zip(A_W, A_Wd):
    for r in range(n):
        for c in range(n):
            row = np.zeros(Nvar, dtype=np.int64)
            for k in range(n):
                row[vi(k, c)] = (row[vi(k, c)] + Ad[r, k]) % P
                row[vi(r, k)] = (row[vi(r, k)] - A[k, c]) % P
            rows.append(row)
            rhs.append(0)

for r in range(n):
    for c in range(35):
        row = np.zeros(Nvar, dtype=np.int64)
        for k in range(n):
            row[vi(r, k)] = (row[vi(r, k)] + I_W[k, c]) % P
        rows.append(row)
        rhs.append(int(K_Wd[r, c]))

M = np.array(rows, dtype=np.int64) % P
b = np.array(rhs, dtype=np.int64) % P


def rref_solve(A, b):
    R = np.column_stack([A.copy() % P, b.reshape(-1, 1) % P])
    m, naug = R.shape
    n = naug - 1
    r = 0
    piv = []
    for c in range(n):
        q = next((i for i in range(r, m) if R[i, c]), None)
        if q is None:
            continue
        R[[r, q]] = R[[q, r]]
        if R[r, c] == 2:
            R[r] = (2 * R[r]) % P
        for i in range(m):
            if i != r and R[i, c]:
                R[i] = (R[i] - R[i, c] * R[r]) % P
        piv.append(c)
        r += 1
        if r == m:
            break
    bad = any(np.all(R[i, :n] % P == 0) and R[i, n] % P != 0 for i in range(r, m))
    if bad:
        return len(piv), None, n - len(piv)
    x = np.zeros(n, dtype=np.int64)
    for rr, c in enumerate(piv):
        x[c] = R[rr, n]
    return len(piv), x, n - len(piv)


rank_system, sol, nullity_system = rref_solve(M, b)
assert sol is not None
X_intertwiner = sol.reshape((n, n)) % P
assert rank3(X_intertwiner) == 45
assert np.array_equal((X_intertwiner @ I_W) % P, K_Wd % P)
assert all(np.array_equal((Ad @ X_intertwiner) % P, (X_intertwiner @ A) % P)
           for A, Ad in zip(A_W, A_Wd))


def column_bracket_with_generator(v_col, gen):
    out = np.zeros(1024, dtype=np.int64)
    for j, coeff in enumerate(v_col):
        c = int(coeff) % P
        if not c:
            continue
        w = WORDS4[j]
        out[INDEX5[w + (gen,)]] = (out[INDEX5[w + (gen,)]] + c) % P
        out[INDEX5[(gen,) + w]] = (out[INDEX5[(gen,) + w]] - c) % P
    return out


B_W = [np.column_stack([column_bracket_with_generator(W[:, j], g) for j in range(45)]) % P
       for g in range(1, 5)]
B_Wd = [np.column_stack([column_bracket_with_generator(Wd[:, j], g) for j in range(45)]) % P
        for g in range(1, 5)]

diffs = [((B_Wd[g] @ X_intertwiner) - B_W[g]) % P for g in range(4)]
D = np.vstack(diffs)
BRACKET_COMPATIBLE = rank3(D) == 0
OBSTRUCTION_RANK = rank3(D)

print('PHASE 2-23 / A3-4-10 AMBIENT BRACKET COMPATIBILITY (CORRECTED)')
print('Gate-0-A imported/executed = NO')
print('dim W45 =', rank3(W))
print('dim Wd =', rank3(Wd))
print('dim common K =', rank3(K_ambient))
print('system rows =', M.shape[0])
print('system unknowns =', M.shape[1])
print('rank of constrained system =', rank_system)
print('solution nullity =', nullity_system)
print('A3-4-9 intertwiner rank =', rank3(X_intertwiner))
print('A3-4-9 intertwiner fixes K =', np.array_equal((X_intertwiner @ I_W) % P, K_Wd % P))
print('degree-5 ambient associative word dimension =', 1024)
print('BRACKET_COMPATIBLE_FOR_ALL_4_GENERATORS =', BRACKET_COMPATIBLE)
print('STACKED_BRACKET_OBSTRUCTION_RANK =', OBSTRUCTION_RANK)
print('RESULT =', 'PASS' if BRACKET_COMPATIBLE else 'FAIL')
print('ALL A3-4-10 CHECKS COMPLETED')
