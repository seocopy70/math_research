"""Phase 2-4B: analyze the 25-dimensional middle quotient K/U.

K = ker(N), U = im(N), M = K/U for the Phase 2-3 representation.
All computations are exact over F_3 and reuse the authoritative Phase 2-3
construction without changing conventions.

Goals:
1. Construct K and U exactly and verify dim K=35, dim U=10, U subset K.
2. Build a canonical 25-dimensional quotient coordinate system M=K/U.
3. Induce the five Sp_4(F_3) generator matrices on M.
4. Compute dim End_H(M) using a cyclic centralizer reduction when available;
   otherwise fall back to the full 625-variable commutant system.
5. Probe cyclic submodules deterministically using all nonzero vectors only
   when feasible; for M (3^25-1 vectors) exhaustive enumeration is deliberately
   NOT attempted.
6. Report exact data without claiming irreducibility from finite probes alone.

This script is exploratory for Phase 2-4B. A later script may perform a
stronger invariant-subspace/composition-factor analysis based on these results.
"""
from pathlib import Path
import runpy
import numpy as np
from itertools import product

P = 3
nW = 45

ns = runpy.run_path(str(Path(__file__).with_name("phase2_3_endH_optimized_2026-09-15.py")))
A = [np.array(x, dtype=np.int64) % P for x in ns["A_list"]]
N = np.array(ns["N"], dtype=np.int64) % P


def r3(M):
    M = np.array(M, dtype=np.int64, copy=True) % P
    if M.ndim == 1:
        M = M[:, None]
    m, n = M.shape
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if M[i, c]), None)
        if p is None:
            continue
        if p != r:
            M[[r, p]] = M[[p, r]]
        if M[r, c] == 2:
            M[r] = (2 * M[r]) % P
        rows = np.flatnonzero(M[:, c])
        rows = rows[rows != r]
        if len(rows):
            vals = M[rows, c].copy()
            M[rows] = (M[rows] - vals[:, None] * M[r]) % P
        r += 1
        if r == m:
            break
    return r


def ns3(M):
    M = np.array(M, dtype=np.int64, copy=True) % P
    m, n = M.shape
    R = M.copy()
    piv = []
    rr = 0
    for c in range(n):
        p = next((i for i in range(rr, m) if R[i, c]), None)
        if p is None:
            continue
        if p != rr:
            R[[rr, p]] = R[[p, rr]]
        if R[rr, c] == 2:
            R[rr] = (2 * R[rr]) % P
        rows = np.flatnonzero(R[:, c])
        rows = rows[rows != rr]
        if len(rows):
            vals = R[rows, c].copy()
            R[rows] = (R[rows] - vals[:, None] * R[rr]) % P
        piv.append(c)
        rr += 1
        if rr == m:
            break
    free = [c for c in range(n) if c not in piv]
    out = []
    for f in free:
        x = np.zeros(n, dtype=np.int64)
        x[f] = 1
        for i, c in enumerate(piv):
            x[c] = (-R[i, f]) % P
        out.append(x)
    return out


def independent_columns(M, target=None):
    cols = []
    B = np.empty((M.shape[0], 0), dtype=np.int64)
    rank = 0
    for j in range(M.shape[1]):
        C = np.column_stack([B, M[:, j]])
        q = r3(C)
        if q > rank:
            cols.append(j)
            B = C
            rank = q
            if target is not None and rank == target:
                break
    return cols, B


def quotient_setup(K_basis, U_basis):
    """Return a 45x25 complement Q to U inside K and a 35-column K basis.

    K_basis and U_basis are matrices whose columns span K and U.
    We choose Q columns greedily from K_basis so [U Q] is a basis of K.
    """
    ucols = [U_basis[:, j] for j in range(U_basis.shape[1])]
    B = np.column_stack(ucols) if ucols else np.empty((nW, 0), dtype=np.int64)
    rank = r3(B)
    Q = []
    for j in range(K_basis.shape[1]):
        c = K_basis[:, j]
        C = np.column_stack([B, c])
        q = r3(C)
        if q > rank:
            Q.append(c)
            B = C
            rank = q
            if rank == 35:
                break
    assert len(Q) == 25
    Q = np.column_stack(Q)
    return Q

# ---- Exact subspaces U=im N and K=ker N ----
rankN = r3(N)
assert rankN == 10
U_basis, _ = independent_columns(N, target=10)
U = N[:, U_basis] if False else None
# The image is spanned by the independent columns selected from N.
Umat = N[:, U_basis]
Knull = ns3(N)
Kmat = np.column_stack(Knull)
assert Kmat.shape == (45, 35)
assert r3(Kmat) == 35
assert r3(np.column_stack([Kmat, Umat])) == 35

Qmat = quotient_setup(Kmat, Umat)
assert r3(np.column_stack([Umat, Qmat])) == 35

# ---- Quotient coordinates ----
# S=[U Q] is a 45x35 basis of K. For each generator and Q-column,
# gQ remains in K. Express it in S, and retain the last 25 coordinates.
S = np.column_stack([Umat, Qmat])
assert r3(S) == 35

# Build a left inverse on a selected independent set of rows of S.
def left_inverse_rows(S):
    rows = []
    R = np.empty((0, S.shape[1]), dtype=np.int64)
    rank = 0
    for i in range(S.shape[0]):
        C = np.vstack([R, S[i:i+1]])
        q = r3(C)
        if q > rank:
            rows.append(i)
            R = C
            rank = q
            if rank == S.shape[1]:
                break
    assert rank == S.shape[1]
    aug = np.concatenate([R, np.eye(S.shape[1], dtype=np.int64)], axis=1)
    m = S.shape[1]
    for c in range(m):
        p = next(i for i in range(c, m) if aug[i, c])
        if p != c:
            aug[[c, p]] = aug[[p, c]]
        if aug[c, c] == 2:
            aug[c] = (2 * aug[c]) % P
        for i in range(m):
            if i != c and aug[i, c]:
                aug[i] = (aug[i] - aug[i, c] * aug[c]) % P
    return rows, aug[:, m:]

rowsS, Linv = left_inverse_rows(S)

M_actions = []
for g in A:
    gQ = (g @ Qmat) % P
    # Coordinates in K from the selected rows.
    C = (Linv @ gQ[rowsS]) % P
    assert np.array_equal((S @ C) % P, gQ)
    # The U-block can be discarded on K/U.
    M_actions.append(C[10:, :])

assert all(X.shape == (25, 25) for X in M_actions)

# Verify induced matrices satisfy the group action relation on quotient.
# In particular, they must be invertible.
assert all(r3(X) == 25 for X in M_actions)

# ---- Endomorphism algebra of M ----
# First try a cyclic linear combination B. If its Krylov powers span the full
# matrix centralizer dimension 25, reduce End_H(M) to 25 unknowns.
I = np.eye(25, dtype=np.int64)
B = sum(M_actions[1:], np.zeros((25, 25), dtype=np.int64)) % P
powers = []
cur = I.copy()
for _ in range(25):
    powers.append(cur.copy())
    cur = (cur @ B) % P
Krylov = np.column_stack([X.reshape(-1) for X in powers])
krylov_rank = r3(Krylov)

if krylov_rank == 25:
    eq_cols = []
    for X in powers:
        pieces = [((X @ g - g @ X) % P).reshape(-1) for g in M_actions]
        eq_cols.append(np.concatenate(pieces))
    E = np.column_stack(eq_cols)
    rankE = r3(E)
    end_basis = ns3(E)
    end_dim = len(end_basis)
    end_method = "cyclic centralizer reduction"
else:
    # Full commutant: 625 unknowns, 4*625 scalar equations.
    eq_cols = []
    basis_mats = []
    for a in range(25):
        for b in range(25):
            X = np.zeros((25, 25), dtype=np.int64)
            X[a, b] = 1
            basis_mats.append(X)
            pieces = [((X @ g - g @ X) % P).reshape(-1) for g in M_actions]
            eq_cols.append(np.concatenate(pieces))
    E = np.column_stack(eq_cols)
    rankE = r3(E)
    end_basis = ns3(E)
    end_dim = len(end_basis)
    end_method = "full 625-variable commutant"

# ---- Deterministic cyclic-submodule probes ----
# Full enumeration of 3^25-1 is infeasible. Probe standard basis and selected
# low-Hamming-weight vectors. This is evidence only, not an irreducibility proof.
def cyclic_dim(v):
    basis = []
    queue = [np.array(v, dtype=np.int64) % P]
    rank = 0
    while queue:
        x = queue.pop()
        nr = r3(np.column_stack(basis + [x])) if basis else r3(x[:, None])
        if nr <= rank:
            continue
        basis.append(x)
        rank = nr
        if rank == 25:
            return 25
        for g in M_actions:
            queue.append((g @ x) % P)
    return rank

probe_vectors = []
for i in range(25):
    e = np.zeros(25, dtype=np.int64); e[i] = 1
    probe_vectors.append(e)
for i in range(25):
    e = np.zeros(25, dtype=np.int64); e[i] = 1; e[(i+1) % 25] = 1
    probe_vectors.append(e)
for i in range(24):
    e = np.zeros(25, dtype=np.int64); e[i] = 1; e[i+1] = 2
    probe_vectors.append(e)

probe_dims = [cyclic_dim(v) for v in probe_vectors]

print("PHASE 2-4B: middle quotient M=ker(N)/im(N)")
print("W dimension =", nW)
print("rank(N) =", rankN)
print("dim U=im(N) =", Umat.shape[1])
print("dim K=ker(N) =", Kmat.shape[1])
print("dim M=K/U =", 25)
print("quotient generator matrices =", len(M_actions))
print("quotient action matrix shape =", M_actions[0].shape)
print("quotient action ranks =", [r3(g) for g in M_actions])
print("Krylov rank for B=A2+A3+A4+A5 on M =", krylov_rank)
print("End_H(M) method =", end_method)
print("End_H(M) rank =", rankE)
print("dim End_H(M) =", end_dim)
print("probe count =", len(probe_vectors))
print("probe dimension distribution =", {d: probe_dims.count(d) for d in sorted(set(probe_dims))})
print("probe minimum dimension =", min(probe_dims))
print("probe maximum dimension =", max(probe_dims))
print("NOTE: finite probes do NOT establish irreducibility.")
