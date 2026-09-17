import importlib.util
import numpy as np

P = 3
SANITY_PATH = 'research/A3_4_10_BRACKET_PIPELINE_SANITY_2026-09-17.py'
spec = importlib.util.spec_from_file_location('ambient_sanity', SANITY_PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

rank3 = mod.rank3
WORDS4, INDEX4 = mod.WORDS4, mod.INDEX4
WORDS5, INDEX5 = mod.WORDS5, mod.INDEX5
W, Wd, gens = mod.W, mod.Wd, mod.gens
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
            if q is None: continue
            A[[r, q]] = A[[q, r]]
            if A[r, c] == 2: A[r] = (2 * A[r]) % P
            for i in range(m):
                if i != r and A[i, c]:
                    A[i] = (A[i] - A[i, c] * A[r]) % P
            piv.append(c); r += 1
        assert len(piv) == B.shape[1]
        for rr, c in enumerate(piv): out[c, j] = A[rr, -1]
    return out


def nullspace3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    m, n = A.shape; r = 0; piv = []
    for c in range(n):
        q = next((i for i in range(r, m) if A[i, c]), None)
        if q is None: continue
        A[[r, q]] = A[[q, r]]
        if A[r, c] == 2: A[r] = (2 * A[r]) % P
        for i in range(m):
            if i != r and A[i, c]: A[i] = (A[i] - A[i, c] * A[r]) % P
        piv.append(c); r += 1
        if r == m: break
    free = [c for c in range(n) if c not in piv]
    Z = np.zeros((n, len(free)), dtype=np.int64)
    for j, f in enumerate(free):
        Z[f, j] = 1
        for rr, c in enumerate(piv): Z[c, j] = (-A[rr, f]) % P
    return Z


def degree_action_matrix(g):
    G = np.zeros((256, 256), dtype=np.int64)
    for j, w in enumerate(WORDS4):
        out = apply_linear_map({w: 1}, g)
        for ww, c in out.items(): G[INDEX4[ww], j] = (G[INDEX4[ww], j] + int(c)) % P
    return G

A4 = [degree_action_matrix(g) for g in gens]
AW = [coords(W, (G @ W) % P) for G in A4]
AWd = [coords(Wd, (G @ Wd) % P) for G in A4]

# Independent recovery of the common 35-dimensional K.
Z = nullspace3(np.column_stack([W, (-Wd) % P]))
assert Z.shape[1] == 35
I_W = Z[:45, :] % P
K_Wd = Z[45:, :] % P
assert rank3(W @ I_W) == 35

# Solve the affine system defining tau: AWd * X = X * AW and X(I_W)=K_Wd.
n = 45
rows, rhs = [], []
idx = lambda r, c: r * n + c
for A, Ad in zip(AW, AWd):
    for r in range(n):
        for c in range(n):
            row = np.zeros(n*n, dtype=np.int64)
            for k in range(n):
                row[idx(k, c)] = (row[idx(k, c)] + Ad[r, k]) % P
                row[idx(r, k)] = (row[idx(r, k)] - A[k, c]) % P
            rows.append(row); rhs.append(0)
for r in range(n):
    for c in range(35):
        row = np.zeros(n*n, dtype=np.int64)
        for k in range(n): row[idx(r, k)] = (row[idx(r, k)] + I_W[k, c]) % P
        rows.append(row); rhs.append(int(K_Wd[r, c]))

M = np.array(rows, dtype=np.int64) % P
b = np.array(rhs, dtype=np.int64) % P


def solve3(A, b):
    R = np.column_stack([A.copy() % P, b.reshape(-1, 1) % P])
    m, naug = R.shape; nvar = naug - 1; r = 0; piv = []
    for c in range(nvar):
        q = next((i for i in range(r, m) if R[i, c]), None)
        if q is None: continue
        R[[r, q]] = R[[q, r]]
        if R[r, c] == 2: R[r] = (2 * R[r]) % P
        for i in range(m):
            if i != r and R[i, c]: R[i] = (R[i] - R[i, c] * R[r]) % P
        piv.append(c); r += 1
        if r == m: break
    assert not any(np.all(R[i, :nvar] == 0) and R[i, nvar] != 0 for i in range(r, m))
    x = np.zeros(nvar, dtype=np.int64)
    for rr, c in enumerate(piv): x[c] = R[rr, nvar]
    return len(piv), x, nvar - len(piv)

rank_system, sol, nullity = solve3(M, b)
tau = sol.reshape((45, 45)) % P

# Layer 1: tau is genuinely an H-intertwiner.
tau_intertwiner = all(np.array_equal((Ad @ tau) % P, (tau @ A) % P) for A, Ad in zip(AW, AWd))
# Layer 2: prescribed K identification is respected.
tau_K = np.array_equal((tau @ I_W) % P, K_Wd % P)
assert rank3(tau) == 45


def bracket_matrix(M, h):
    B = np.zeros((1024, 45), dtype=np.int64)
    for j in range(45):
        for k, coeff in enumerate(M[:, j]):
            c = int(coeff) % P
            if not c: continue
            w = WORDS4[k]
            B[INDEX5[w + (h,)], j] = (B[INDEX5[w + (h,)], j] + c) % P
            B[INDEX5[(h,) + w], j] = (B[INDEX5[(h,) + w], j] - c) % P
    return B

B_W = [bracket_matrix(W, h) for h in range(1, 5)]
B_Wd = [bracket_matrix(Wd, h) for h in range(1, 5)]
obstructions = [((B_Wd[h] @ tau) - B_W[h]) % P for h in range(4)]
stacked = np.vstack(obstructions)
obstruction_rank = rank3(stacked)
tau_bracket = obstruction_rank == 0

print('A3-4-10 TAU-SPECIFIC SANITY CHECK (STANDALONE)')
print('No Gate-0-A or old phase script imported/executed.')
print('dim W45 =', rank3(W), 'dim Wd =', rank3(Wd), 'dim K =', rank3(W @ I_W))
print('tau constrained-system rank =', rank_system, 'unknowns =', n*n, 'nullity =', nullity)
print('tau rank =', rank3(tau))
print('TAU_INTERTWINER =', tau_intertwiner)
print('TAU_FIXES_K =', tau_K)
print('TAU_BRACKET_COMPATIBLE_ALL_4 =', tau_bracket)
print('TAU_BRACKET_OBSTRUCTION_RANK =', obstruction_rank)
print('RESULT =', 'PASS' if tau_intertwiner and tau_K else 'FAIL')
print('NOTE: bracket compatibility is reported separately; this sanity does not assume it.')
