import runpy
import numpy as np
from itertools import product

P = 3
ROOT = 'research/'

ns = runpy.run_path(ROOT + 'phase2_18_A3_4_5_intersection_K_and_Sym2_2026-09-16.py')
rank3 = ns['rank3']
coords = ns['coords']
W = np.array(ns['W'], dtype=np.int64) % P
Wd = np.array(ns['Wd_basis'], dtype=np.int64) % P
I_W = np.array(ns['I_W'], dtype=np.int64) % P
K_coord = np.array(ns['K_coord'], dtype=np.int64) % P
A_W = [np.array(a, dtype=np.int64) % P for a in ns['A_W']]

ns1 = runpy.run_path(ROOT + 'phase2_1_invariant_space_verification_2026-09-15.py')
index4 = ns1['index4']
gens = ns1['gens']
apply_linear_map = ns1['apply_linear_map']
words4 = list(index4.keys())

A4_ambient = []
for g in gens:
    G = np.zeros((256, 256), dtype=np.int64)
    for j, w in enumerate(words4):
        out = apply_linear_map({w: 1}, g)
        for ww, c in out.items():
            G[index4[ww], j] = (G[index4[ww], j] + c) % P
    A4_ambient.append(G)

assert W.shape == (256, 45)
assert Wd.shape == (256, 45)
assert len(A_W) == len(A4_ambient) == 5

# Existing degree-4 words are tuples of generator labels.  The A3-4-5
# construction is authoritative, so preserve that exact word convention.
# Degree-5 associative words are represented by tuples as well.
words5 = list(product((1, 2, 3, 4), repeat=5))
index5 = {w: i for i, w in enumerate(words5)}

def column_bracket_with_generator(v_col, gen):
    """Associative expansion of [v, X_gen] = v X_gen - X_gen v."""
    out = np.zeros(1024, dtype=np.int64)
    for j, coeff in enumerate(v_col):
        coeff = int(coeff) % P
        if coeff == 0:
            continue
        w = words4[j]
        wg = w + (gen,)
        gw = (gen,) + w
        out[index5[wg]] = (out[index5[wg]] + coeff) % P
        out[index5[gw]] = (out[index5[gw]] - coeff) % P
    return out

B_W = []
B_Wd = []
for g in range(1, 5):
    B_W.append(np.column_stack([
        column_bracket_with_generator(W[:, j], g) for j in range(45)
    ]) % P)
    B_Wd.append(np.column_stack([
        column_bracket_with_generator(Wd[:, j], g) for j in range(45)
    ]) % P)

# Reconstruct the A3-4-9 intertwiner X: W45 -> Wd, fixing K pointwise.
n = 45
Nvar = n * n
rows = []

def vi(r, c):
    return r * n + c

A_Wd = []
for G in A4_ambient:
    Y = (G @ Wd) % P
    C = coords(Wd, Y)
    assert np.array_equal((Wd @ C) % P, Y)
    A_Wd.append(C)

K_ambient = (W @ K_coord) % P
K_Wd = coords(Wd, K_ambient)
assert np.array_equal((Wd @ K_Wd) % P, K_ambient)
assert rank3(K_Wd) == 35

for A, Ad in zip(A_W, A_Wd):
    for r in range(n):
        for c in range(n):
            row = np.zeros(Nvar, dtype=np.int64)
            for k in range(n):
                row[vi(k, c)] = (row[vi(k, c)] + Ad[r, k]) % P
                row[vi(r, k)] = (row[vi(r, k)] - A[k, c]) % P
            rows.append(row)

# X|K = identity, expressed as X I_W = K_Wd.
for r in range(n):
    for c in range(35):
        row = np.zeros(Nvar, dtype=np.int64)
        for k in range(n):
            row[vi(r, k)] = (row[vi(r, k)] + I_W[k, c]) % P
        rows.append(row)

M = np.array(rows, dtype=np.int64) % P

def rref_nullspace(A):
    R = A.copy() % P
    m, n = R.shape
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
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        z = np.zeros(n, dtype=np.int64)
        z[f] = 1
        for rr, c in enumerate(piv):
            z[c] = (-R[rr, f]) % P
        basis.append(z)
    return len(piv), basis

rank_system, null_basis = rref_nullspace(M)
assert len(null_basis) == 1
X_intertwiner = null_basis[0].reshape((45, 45)) % P
assert rank3(X_intertwiner) == 45
assert np.array_equal((X_intertwiner @ I_W) % P, K_Wd % P)
assert all(
    np.array_equal((Ad @ X_intertwiner) % P, (X_intertwiner @ A) % P)
    for A, Ad in zip(A_W, A_Wd)
)

# IMPORTANT: B_W[g] maps W45 -> degree-5 ambient space, while B_Wd[g]
# maps Wd -> degree-5 ambient space. Therefore the correct compatibility
# equation is B_Wd[g] @ X = B_W[g].
diffs = [((B_Wd[g] @ X_intertwiner) - B_W[g]) % P for g in range(4)]
D = np.vstack(diffs)
BRACKET_COMPATIBLE = all(np.count_nonzero(D[g * 1024:(g + 1) * 1024, :]) == 0 for g in range(4))
OBSTRUCTION_RANK = rank3(D)

print('PHASE 2-23 / A3-4-10 AMBIENT BRACKET COMPATIBILITY')
print('dim W45 =', rank3(W))
print('dim Wd =', rank3(Wd))
print('dim common K =', rank3(K_ambient))
print('A3-4-9 intertwiner rank =', rank3(X_intertwiner))
print('A3-4-9 intertwiner fixes K =', np.array_equal((X_intertwiner @ I_W) % P, K_Wd % P))
print('degree-5 ambient associative word dimension =', 1024)
print('BRACKET_COMPATIBLE_FOR_ALL_4_GENERATORS =', BRACKET_COMPATIBLE)
print('STACKED_BRACKET_OBSTRUCTION_RANK =', OBSTRUCTION_RANK)

if BRACKET_COMPATIBLE:
    print('RESULT: the verified W45~Wd intertwiner is compatible with the ambient degree-5 Lie bracket against every generator.')
else:
    print('RESULT: the verified module/extension intertwiner is NOT compatible with the ambient degree-5 Lie bracket.')

print('ALL A3-4-10 CHECKS COMPLETED')
