"""
Independent sanity check for A3-4-9.

Two checks are deliberately separated from the primary rank certificate:
1. A direct determinant computation of the 60x60 matrix M=[W45|S] over F_3.
2. An explicit reconstruction of a nontrivial L4 Lie element from the
   W45-part and S-part using M^{-1}.

A separate sparse row-rank computation is retained as an additional check.
"""

import runpy
import numpy as np

MOD = 3
BASE = runpy.run_path(
    "research/phase2_22_A3_4_9_W45_true_relation_intersection_2026-09-16.py"
)

W = BASE["W"] % MOD
Sm = BASE["Sm"] % MOD
oldm = BASE["oldm"] % MOD
X = BASE["X"]
bracket = BASE["bracket"]
vec4 = BASE["vec4"]


def row_rank_mod3(A):
    """Independent sparse row-oriented rank over F_3."""
    rows = []
    for raw in A:
        row = {i: int(v) % MOD for i, v in enumerate(raw) if int(v) % MOD}
        rows.append(row)
    pivots = {}
    rank = 0
    for row in rows:
        while row:
            p = min(row)
            coeff = row[p] % MOD
            if p not in pivots:
                if coeff == 2:
                    row = {j: (v * 2) % MOD for j, v in row.items()}
                pivots[p] = row
                rank += 1
                break
            pivot = pivots[p]
            factor = coeff
            for j, v in pivot.items():
                nv = (row.get(j, 0) - factor * v) % MOD
                if nv:
                    row[j] = nv
                else:
                    row.pop(j, None)
    return rank


def det_mod3(A):
    """Direct determinant via pivot elimination, independent of row_rank_mod3."""
    A = np.array(A, dtype=np.int64) % MOD
    n, m = A.shape
    assert n == m
    A = A.copy()
    det = 1
    for c in range(n):
        piv = next((i for i in range(c, n) if A[i, c] % MOD), None)
        if piv is None:
            return 0
        if piv != c:
            A[[c, piv]] = A[[piv, c]]
            det = (-det) % MOD
        pivot = int(A[c, c]) % MOD
        det = (det * pivot) % MOD
        inv = 1 if pivot == 1 else 2
        A[c, c:] = (A[c, c:] * inv) % MOD
        for i in range(c + 1, n):
            factor = int(A[i, c]) % MOD
            if factor:
                A[i, c:] = (A[i, c:] - factor * A[c, c:]) % MOD
    return int(det % MOD)


def solve_mod3(A, b):
    """Gauss-Jordan solve over F_3 for an invertible square matrix."""
    A = np.array(A, dtype=np.int64) % MOD
    b = np.array(b, dtype=np.int64) % MOD
    n = A.shape[0]
    aug = np.concatenate([A, b.reshape(n, 1)], axis=1)
    for c in range(n):
        piv = next(i for i in range(c, n) if aug[i, c] % MOD)
        if piv != c:
            aug[[c, piv]] = aug[[piv, c]]
        inv = 1 if aug[c, c] == 1 else 2
        aug[c, :] = (aug[c, :] * inv) % MOD
        for i in range(n):
            if i != c and aug[i, c] % MOD:
                factor = aug[i, c]
                aug[i, :] = (aug[i, :] - factor * aug[c, :]) % MOD
    return aug[:, -1] % MOD


M = np.concatenate([W, Sm], axis=1) % MOD

# Retain the independent rank check as a separate diagnostic.
rank_W = row_rank_mod3(W.T)
rank_S = row_rank_mod3(Sm.T)
rank_old = row_rank_mod3(oldm.T)
rank_M = row_rank_mod3(M.T)
rank_S_old = row_rank_mod3(np.concatenate([Sm, oldm], axis=1).T)

intersection = rank_W + rank_S - rank_M
inclusion = rank_S_old == rank_S

det_M = det_mod3(M)

# Nontrivial Lie element in L4: [[X1,X2],[X3,X4]].
# This is constructed independently from the columns of M.
v = vec4(bracket(bracket(X[0], X[1]), bracket(X[2], X[3]))) % MOD
coeff = solve_mod3(M, v)
w_coeff = coeff[:45]
s_coeff = coeff[45:]
w = (W @ w_coeff) % MOD
s = (Sm @ s_coeff) % MOD
reconstructed = (w + s) % MOD
reconstruction_ok = np.array_equal(reconstructed, v)

print("A3-4-9 INDEPENDENT DETERMINANT + RECONSTRUCTION CHECK")
print("=======================================================")
print(f"independent rank(W45) = {rank_W}")
print(f"independent rank(S) = {rank_S}")
print(f"independent rank([W45 | S]) = {rank_M}")
print(f"independent dim(W45 intersection S) = {intersection}")
print(f"independent rank([S | [L2,R]]) = {rank_S_old}")
print(f"independent [L2,R] subset S = {inclusion}")
print(f"det([W45 | S]) mod 3 = {det_M}")
print("test vector = [[X1,X2],[X3,X4]]")
print(f"reconstruction exact over F_3 = {reconstruction_ok}")
print(f"reconstruction residual nonzero entries = {int(np.count_nonzero((reconstructed - v) % MOD))}")

assert rank_W == 45
assert rank_S == 15
assert rank_old == 5
assert rank_M == 60
assert intersection == 0
assert rank_S_old == 15
assert inclusion
assert det_M != 0
assert reconstruction_ok
assert np.array_equal(reconstructed, v)

print("INDEPENDENT DETERMINANT + RECONSTRUCTION CHECK PASSED")
