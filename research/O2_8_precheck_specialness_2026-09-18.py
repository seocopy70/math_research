"""O2-8 PRECHECK: audit complete H-orbit closure for the q=3 shadow.

This is deliberately a control experiment, not a quotient interpretation.
We compare the q=3 class d with deterministic generic/control vectors in W
and with deterministic vectors directly sampled in U=im(N).
"""
from pathlib import Path
import runpy
import numpy as np

P = 3
ROOT = Path(__file__).parent

ns_tau = runpy.run_path(str(ROOT / "A3-4-10_CANONICAL_TAU_REVALIDATION_2026-09-16.py"))
A_W = [np.array(A, dtype=np.int64) % P for A in ns_tau["A_W"]]
coordinates = ns_tau["coordinates"]
Q_W45 = np.array(ns_tau["Q_W45"], dtype=np.int64) % P

ns_N = runpy.run_path(str(ROOT / "phase2_3_endH_optimized_2026-09-15.py"))
N = np.array(ns_N["N"], dtype=np.int64) % P

def rank3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    if A.ndim == 1:
        A = A.reshape(-1, 1)
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

def solve_full_column(A, b):
    A = np.array(A, dtype=np.int64) % P
    b = np.array(b, dtype=np.int64) % P
    m, n = A.shape
    aug = np.concatenate([A, b.reshape(m, 1)], axis=1)
    row = 0
    pivots = []
    for c in range(n):
        piv = next((i for i in range(row, m) if aug[i, c]), None)
        if piv is None:
            continue
        if piv != row:
            aug[[row, piv]] = aug[[piv, row]]
        if aug[row, c] == 2:
            aug[row] = (2 * aug[row]) % P
        for i in range(m):
            if i != row and aug[i, c]:
                aug[i] = (aug[i] - aug[i, c] * aug[row]) % P
        pivots.append(c)
        row += 1
    if np.any(np.all(aug[:, :n] == 0, axis=1) & (aug[:, n] != 0)):
        raise AssertionError("target vector is not in W")
    x = np.zeros(n, dtype=np.int64)
    for i, c in enumerate(pivots):
        x[c] = aug[i, n]
    assert np.array_equal((A @ x) % P, b)
    return x

def h_span_dim(v):
    v = np.array(v, dtype=np.int64) % P
    basis = [v]
    while True:
        old = rank3(np.column_stack(basis))
        added = False
        for A in A_W:
            for b in list(basis):
                w = (A @ b) % P
                trial = np.column_stack(basis + [w])
                if rank3(trial) > old:
                    basis.append(w)
                    old += 1
                    added = True
        if not added:
            return old

def ad3_vector(i, j):
    # In characteristic 3, ad(X_i)^3(X_j)=X_i^3 X_j-X_j X_i^3.
    words = [(a,b,c,d) for a in range(1,5) for b in range(1,5)
             for c in range(1,5) for d in range(1,5)]
    idx = {w:k for k,w in enumerate(words)}
    v = np.zeros(256, dtype=np.int64)
    v[idx[(i,i,i,j)]] = 1
    v[idx[(j,i,i,i)]] = (-1) % P
    return v

# Reconstruct the certified q=3 vector d in W coordinates.
d = ad3_vector(1, 2)
d_Q = np.array(coordinates(d)[15:], dtype=np.int64) % P
d_W = solve_full_column(Q_W45, d_Q)
Nd = (N @ d_W) % P
d_shadow_dim = h_span_dim(Nd)

# Deterministic generic/control vectors in W.
rng = np.random.default_rng(20260918)
random_W = []
for k in range(12):
    v = rng.integers(0, P, size=45, dtype=np.int64)
    if rank3(v.reshape(-1,1)) == 0:
        v[0] = 1
    random_W.append(v)

random_shadow_dims = [h_span_dim((N @ v) % P) for v in random_W]

# Direct controls in U: random linear combinations of the image basis.
# This removes any possibility that the effect comes from how v was chosen in W.
U_basis = N
random_U = []
while len(random_U) < 12:
    c = rng.integers(0, P, size=45, dtype=np.int64)
    u = (U_basis @ c) % P
    if rank3(u.reshape(-1,1)):
        random_U.append(u)

random_U_dims = [h_span_dim(u) for u in random_U]

# Exhaustive control over the nonzero columns of N.
column_dims = []
for j in range(N.shape[1]):
    u = N[:, j]
    if rank3(u.reshape(-1,1)):
        column_dims.append((j, h_span_dim(u)))

# q=3 natural restricted-power family ad(X_i)^3(X_j), i != j.
q3_dims = []
q3_embedded = 0
for i in range(1,5):
    for j in range(1,5):
        if i == j:
            continue
        v = ad3_vector(i, j)
        try:
            vQ = np.array(coordinates(v)[15:], dtype=np.int64) % P
            vW = solve_full_column(Q_W45, vQ)
        except AssertionError:
            q3_dims.append((i,j,"NOT_IN_W"))
            continue
        q3_embedded += 1
        q3_dims.append((i,j,h_span_dim((N @ vW) % P)))

print("O2-8 PRECHECK: COMPLETE H-ORBIT CLOSURE AUDIT")
print("d_shadow_dim =", d_shadow_dim)
print("random_W_shadow_dims =", random_shadow_dims)
print("random_U_orbit_dims =", random_U_dims)
print("N_column_orbit_dims =", column_dims)
print("q3_restricted_power_shadow_dims =", q3_dims)
print("q3_restricted_power_vectors_in_W =", q3_embedded)

assert d_shadow_dim == 10
assert len(random_W_shadow_dims) == 12
assert len(random_U_dims) == 12
assert len(column_dims) > 0
assert all(x in (9,10) for x in random_W_shadow_dims)
assert all(x in (9,10) for x in random_U_dims)
print("O2-8 PRECHECK RESULT = PASS")
