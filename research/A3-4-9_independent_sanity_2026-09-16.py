"""
Independent sanity check for A3-4-9.

The primary certificate proves rank([W45|S])=60 in the 256-dimensional
associative word coordinates.  Here we add two explicit checks:
1. reduce the 16 generators of S to an independent 15-column basis, select
   60 independent ambient coordinate rows, form the resulting 60x60 maximal
   minor of M=[W45|S_basis], and compute its determinant directly over F_3;
2. solve that minor for a nontrivial L4 Lie element and reconstruct the full
   256-coordinate vector exactly from its W45 and S_basis components.

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


def independent_column_indices(A, target):
    """Select target independent columns of A over F_3."""
    basis = {}
    selected = []
    rank = 0
    for idx in range(A.shape[1]):
        col = {i: int(v) % MOD for i, v in enumerate(A[:, idx]) if int(v) % MOD}
        while col:
            p = min(col)
            if p not in basis:
                coeff = col[p]
                if coeff == 2:
                    col = {j: (v * 2) % MOD for j, v in col.items()}
                basis[p] = col
                rank += 1
                selected.append(idx)
                break
            factor = col[p]
            pivot = basis[p]
            for j, v in pivot.items():
                nv = (col.get(j, 0) - factor * v) % MOD
                if nv:
                    col[j] = nv
                else:
                    col.pop(j, None)
        if rank == target:
            return selected
    raise AssertionError(f"could not select {target} independent columns")


def independent_row_indices(A, target):
    """Select target independent rows of A over F_3."""
    selected = []
    basis = {}
    rank = 0
    for idx, raw in enumerate(A):
        row = {i: int(v) % MOD for i, v in enumerate(raw) if int(v) % MOD}
        while row:
            p = min(row)
            if p not in basis:
                coeff = row[p]
                if coeff == 2:
                    row = {j: (v * 2) % MOD for j, v in row.items()}
                basis[p] = row
                rank += 1
                selected.append(idx)
                break
            factor = row[p]
            pivot = basis[p]
            for j, v in pivot.items():
                nv = (row.get(j, 0) - factor * v) % MOD
                if nv:
                    row[j] = nv
                else:
                    row.pop(j, None)
        if rank == target:
            return selected
    raise AssertionError(f"could not select {target} independent rows")


def det_mod3(A):
    """Direct determinant via pivot elimination, separate from rank routine."""
    A = np.asarray(A, dtype=np.int64) % MOD
    assert A.shape == (60, 60), f"expected 60x60 minor, got {A.shape}"
    A = A.copy()
    det = 1
    for c in range(60):
        piv = next((i for i in range(c, 60) if A[i, c] % MOD), None)
        if piv is None:
            return 0
        if piv != c:
            A[[c, piv]] = A[[piv, c]]
            det = (-det) % MOD
        pivot = int(A[c, c]) % MOD
        det = (det * pivot) % MOD
        inv = 1 if pivot == 1 else 2
        A[c, c:] = (A[c, c:] * inv) % MOD
        for i in range(c + 1, 60):
            factor = int(A[i, c]) % MOD
            if factor:
                A[i, c:] = (A[i, c:] - factor * A[c, c:]) % MOD
    return int(det % MOD)


def solve_mod3(A, b):
    """Gauss-Jordan solve over F_3 for an invertible 60x60 matrix."""
    A = np.asarray(A, dtype=np.int64) % MOD
    b = np.asarray(b, dtype=np.int64) % MOD
    assert A.shape == (60, 60)
    aug = np.concatenate([A, b.reshape(60, 1)], axis=1)
    for c in range(60):
        piv = next(i for i in range(c, 60) if aug[i, c] % MOD)
        if piv != c:
            aug[[c, piv]] = aug[[piv, c]]
        inv = 1 if aug[c, c] == 1 else 2
        aug[c, :] = (aug[c, :] * inv) % MOD
        for i in range(60):
            if i != c and aug[i, c] % MOD:
                factor = aug[i, c]
                aug[i, :] = (aug[i, :] - factor * aug[c, :]) % MOD
    return aug[:, -1] % MOD


# W is already a 45-column basis. S has 16 natural generators but rank 15,
# so explicitly extract a 15-column basis before constructing M.
s_basis_indices = independent_column_indices(Sm, 15)
S_basis = Sm[:, np.asarray(s_basis_indices, dtype=np.int64)]
assert S_basis.shape == (256, 15)
assert row_rank_mod3(S_basis.T) == 15

M = np.concatenate([W, S_basis], axis=1) % MOD

rank_W = row_rank_mod3(W.T)
rank_S = row_rank_mod3(Sm.T)
rank_old = row_rank_mod3(oldm.T)
rank_M = row_rank_mod3(M.T)
rank_S_old = row_rank_mod3(np.concatenate([Sm, oldm], axis=1).T)

intersection = rank_W + rank_S - rank_M
inclusion = rank_S_old == rank_S

# M has 256 ambient rows, so the literal 60x60 object is a maximal minor.
row_indices = np.asarray(independent_row_indices(M, 60), dtype=np.int64)
assert len(row_indices) == 60
minor = M[row_indices, :]
assert minor.shape == (60, 60), f"minor shape = {minor.shape}"
det_minor = det_mod3(minor)

# Nontrivial Lie element in L4: [[X1,X2],[X3,X4]].
v = vec4(bracket(bracket(X[0], X[1]), bracket(X[2], X[3]))) % MOD
coeff = solve_mod3(minor, v[row_indices])
w_coeff = coeff[:45]
s_coeff = coeff[45:]
w = (W @ w_coeff) % MOD
s = (S_basis @ s_coeff) % MOD
reconstructed = (w + s) % MOD
residual = (reconstructed - v) % MOD
reconstruction_ok = np.array_equal(reconstructed, v)

print("A3-4-9 INDEPENDENT DETERMINANT + RECONSTRUCTION CHECK")
print("=======================================================")
print(f"independent rank(W45) = {rank_W}")
print(f"independent rank(S) = {rank_S}")
print(f"selected S basis columns = {s_basis_indices}")
print(f"independent rank([W45 | S_basis]) = {rank_M}")
print(f"independent dim(W45 intersection S) = {intersection}")
print(f"independent rank([S | [L2,R]]) = {rank_S_old}")
print(f"independent [L2,R] subset S = {inclusion}")
print(f"selected independent ambient rows = {len(row_indices)}")
print(f"det(60x60 maximal minor of [W45 | S_basis]) mod 3 = {det_minor}")
print("test vector = [[X1,X2],[X3,X4]]")
print(f"reconstruction exact over F_3 = {reconstruction_ok}")
print(f"reconstruction residual nonzero entries = {int(np.count_nonzero(residual))}")

assert rank_W == 45
assert rank_S == 15
assert rank_old == 5
assert rank_M == 60
assert intersection == 0
assert rank_S_old == 15
assert inclusion
assert det_minor != 0
assert reconstruction_ok
assert np.count_nonzero(residual) == 0

print("INDEPENDENT DETERMINANT + RECONSTRUCTION CHECK PASSED")
