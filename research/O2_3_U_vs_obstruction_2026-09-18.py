import runpy
import numpy as np

P = 3


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


def inverse3(A):
    A = np.array(A, dtype=np.int64) % P
    n = A.shape[0]
    R = np.concatenate([A, np.eye(n, dtype=np.int64)], axis=1) % P
    for c in range(n):
        q = next((i for i in range(c, n) if R[i, c]), None)
        assert q is not None
        R[[c, q]] = R[[q, c]]
        if R[c, c] == 2:
            R[c] = (2 * R[c]) % P
        for i in range(n):
            if i != c and R[i, c]:
                R[i] = (R[i] - R[i, c] * R[c]) % P
    return R[:, n:]


def left_inverse(B):
    """Return L with L B = I for a full-column-rank matrix B."""
    B = np.array(B, dtype=np.int64) % P
    m, k = B.shape
    selected_rows = []
    R = np.empty((0, k), dtype=np.int64)
    r = 0
    for i in range(m):
        C = np.vstack([R, B[i:i+1]])
        q = rank3(C)
        if q > r:
            selected_rows.append(i)
            R = C
            r = q
            if r == k:
                break
    assert r == k
    R_inv = inverse3(R)
    L = np.zeros((k, m), dtype=np.int64)
    L[:, selected_rows] = R_inv
    assert np.array_equal((L @ B) % P, np.eye(k, dtype=np.int64))
    return L


def independent_columns(M):
    M = np.array(M, dtype=np.int64) % P
    selected = []
    B = np.empty((M.shape[0], 0), dtype=np.int64)
    r = 0
    for j in range(M.shape[1]):
        C = np.column_stack([B, M[:, j]])
        q = rank3(C)
        if q > r:
            selected.append(j)
            B = C
            r = q
    return selected, B


def nullspace3(A):
    R = np.array(A, dtype=np.int64, copy=True) % P
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
    out = []
    for f in free:
        x = np.zeros(n, dtype=np.int64)
        x[f] = 1
        for rr, c in enumerate(piv):
            x[c] = (-R[rr, f]) % P
        out.append(x)
    return out


def degree_action_matrix(g, words, index):
    dim = len(words)
    G = np.zeros((dim, dim), dtype=np.int64)
    for j, w in enumerate(words):
        out = apply_linear_map({w: 1}, g)
        for ww, c in out.items():
            G[index[ww], j] = (G[index[ww], j] + int(c)) % P
    return G


# ------------------------------------------------------------
# Consume the corrected, verified O2-2 artifact and the authoritative N.
# ------------------------------------------------------------
ns_D = runpy.run_path('research/phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
ns_N = runpy.run_path('research/phase2_3_endH_optimized_2026-09-15.py')

D = np.array(ns_D['D'], dtype=np.int64) % P
A_W = [np.array(A, dtype=np.int64) % P for A in ns_D['A_W']]
I_W = np.array(ns_D['I_W'], dtype=np.int64) % P
gens = [np.array(g, dtype=np.int64) % P for g in ns_D['gens']]
N = np.array(ns_N['N'], dtype=np.int64) % P

assert D.shape[1] == 45
assert I_W.shape == (45, 35)
assert N.shape == (45, 45)
assert all(A.shape == (45, 45) for A in A_W)
assert all(g.shape == (4, 4) for g in gens)
assert rank3(N) == 10
assert np.array_equal((N @ N) % P, np.zeros((45, 45), dtype=np.int64))
assert np.array_equal((N @ I_W) % P, np.zeros((45, 35), dtype=np.int64))

# ------------------------------------------------------------
# O2-3A: kernel/dimension precheck.
# ------------------------------------------------------------
rank_D = rank3(D)
D_on_I = (D @ I_W) % P
kernel_contains_I = np.array_equal(D_on_I, np.zeros_like(D_on_I))
ker_dim = 45 - rank_D
kernel_equals_I = kernel_contains_I and ker_dim == 35

# ------------------------------------------------------------
# Build O and U bases with exact left inverses.
# ------------------------------------------------------------
_, O_basis = independent_columns(D)
assert O_basis.shape[1] == rank_D
O_left = left_inverse(O_basis) if rank_D else None

_, U_basis = independent_columns(N)
assert U_basis.shape == (45, 10)
U_left = left_inverse(U_basis)

# ------------------------------------------------------------
# O2-3B: character/trace precheck.
# ------------------------------------------------------------
# O is the image of the stacked obstruction. Its H-action is the verified
# rho_T(g) tensor A5(g), with T_g = g^{-T}; this is already 4*1024 = 4096
# dimensional because T_g acts on the four stacked discrepancy blocks.
apply_linear_map = ns_D['apply_linear_map']
WORDS5 = ns_D['WORDS5']
INDEX5 = ns_D['INDEX5']

A_U = []
A_O = []
trace_U = []
trace_O = []

for g, AW in zip(gens, A_W):
    AU = (U_left @ AW @ U_basis) % P
    A_U.append(AU)
    trace_U.append(int(np.trace(AU) % P))

    if rank_D == 10:
        A5 = degree_action_matrix(g, WORDS5, INDEX5)
        Ginv = inverse3(g)
        T_g = Ginv.T % P
        rho_stack = np.kron(T_g, A5) % P
        assert rho_stack.shape == (4096, 4096)
        AO = (O_left @ rho_stack @ O_basis) % P
        A_O.append(AO)
        trace_O.append(int(np.trace(AO) % P))

trace_match = rank_D == 10 and trace_U == trace_O

# ------------------------------------------------------------
# O2-3C: induced W/I -> O and comparison with U = im(N).
# ------------------------------------------------------------
# All matrices below use W-coordinates. I_W is 45x35, D is 4096x45, and N
# is 45x45.
Ccols = []
current = I_W.copy()
r = rank3(current)
for j in range(45):
    e = np.eye(45, dtype=np.int64)[:, j:j+1]
    q = rank3(np.column_stack([current, e]))
    if q > r:
        Ccols.append(j)
        current = np.column_stack([current, e])
        r = q
        if r == 45:
            break
assert len(Ccols) == 10
C = np.eye(45, dtype=np.int64)[:, Ccols]

Dbar_coords = (O_left @ D @ C) % P if rank_D == 10 else None
Dbar_rank = rank3(Dbar_coords) if rank_D == 10 else None

NC = (N @ C) % P
NC_coords = (U_left @ NC) % P
NC_rank = rank3(NC_coords)

induced_U_to_O = None
induced_intertwiner_residuals = []
if kernel_equals_I and rank_D == 10:
    assert Dbar_rank == 10
    assert NC_rank == 10
    induced_U_to_O = (Dbar_coords @ inverse3(NC_coords)) % P
    assert rank3(induced_U_to_O) == 10
    for AU, AO in zip(A_U, A_O):
        lhs = (AO @ induced_U_to_O) % P
        rhs = (induced_U_to_O @ AU) % P
        induced_intertwiner_residuals.append(not np.array_equal(lhs, rhs))

induced_equivariant = induced_U_to_O is not None and not any(induced_intertwiner_residuals)

# ------------------------------------------------------------
# Optional O2-3D: independent 10x10 intertwiner solve if the direct induced
# map is not already equivariant. This is diagnostic only.
# ------------------------------------------------------------
solve_intertwiner = trace_match and not induced_equivariant
intertwiner_found = False
if solve_intertwiner:
    rows = []
    for AU, AO in zip(A_U, A_O):
        for r in range(10):
            for c in range(10):
                row = np.zeros(100, dtype=np.int64)
                for k in range(10):
                    row[k * 10 + c] = (row[k * 10 + c] + AO[r, k]) % P
                    row[r * 10 + k] = (row[r * 10 + k] - AU[k, c]) % P
                rows.append(row)
    Z = np.array(rows, dtype=np.int64) % P
    for v in nullspace3(Z):
        X = v.reshape((10, 10)) % P
        if rank3(X) == 10:
            intertwiner_found = True
            break

print('O2-3 / U = im(N) VS O = im(D_stack)')
print('D_stack shape =', D.shape)
print('rank(D_stack) =', rank_D)
print('dim ker(D_stack) =', ker_dim)
print('D_stack annihilates I =', kernel_contains_I)
print('ker(D_stack) = I = ker(N) =', kernel_equals_I)
print('dim U =', rank3(N))
print('dim O =', rank_D)
print()
print('TRACE PRECHECK')
print('trace(U) on 5 generators =', trace_U)
print('trace(O) on 5 generators =', trace_O)
print('character/trace precheck =', 'PASS' if trace_match else 'FAIL')
print()
print('INDUCED MAP')
print('quotient complement columns =', Ccols)
print('rank(Dbar: W/I -> O) =', Dbar_rank)
print('rank(N: quotient representative C -> U) =', NC_rank)
print('induced U -> O map rank =', None if induced_U_to_O is None else rank3(induced_U_to_O))
print('induced U -> O H-equivariant =', induced_equivariant)
print('optional independent 10x10 solve needed =', solve_intertwiner)
print('optional independent 10x10 invertible intertwiner found =', intertwiner_found)

PASS = (kernel_equals_I and rank_D == 10 and Dbar_rank == 10 and
        NC_rank == 10 and induced_equivariant)
print()
print('O2-3 RESULT =', 'PASS' if PASS else 'FAIL')
