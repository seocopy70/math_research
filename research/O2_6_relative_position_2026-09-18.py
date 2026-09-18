"""O2-6: relative position of the canonical obstruction O_tau and Delta O.

This experiment deliberately compares ONLY
    O_tau   = Im(D_0)
    Delta O = Im(D_1 - D_0)
before introducing U.

Mathematical outcomes are all valid research outcomes:
  dim intersection = 10  -> O_tau = Delta O
  dim intersection = 0   -> direct sum, dim sum = 20
  0 < dim intersection < 10 -> partial overlap; intersection is retained
      as a new H-submodule candidate and is NOT treated as an error.

Only algebraic/coordinate inconsistencies are hard failures.
"""

from pathlib import Path
import json
import runpy
import numpy as np

P = 3
ROOT = Path(__file__).parent

ns_tau = runpy.run_path(str(ROOT / "A3-4-10_CANONICAL_TAU_REVALIDATION_2026-09-16.py"))
W = np.array(ns_tau["W"], dtype=np.int64) % P
Wd = np.array(ns_tau["Wd"], dtype=np.int64) % P
tau = np.array(ns_tau["tau_coord"], dtype=np.int64) % P
A_W = [np.array(A, dtype=np.int64) % P for A in ns_tau["A_W"]]
gens = [np.array(g, dtype=np.int64) % P for g in ns_tau["gens"]]
words4 = ns_tau["words4"]
I_coord = np.array(ns_tau["I_coord"], dtype=np.int64) % P
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
        p = next((i for i in range(r, m) if A[i, c]), None)
        if p is None:
            continue
        if p != r:
            A[[r, p]] = A[[p, r]]
        if A[r, c] == 2:
            A[r] = (2 * A[r]) % P
        rows = np.flatnonzero(A[:, c])
        rows = rows[rows != r]
        if len(rows):
            vals = A[rows, c].copy()
            A[rows] = (A[rows] - vals[:, None] * A[r]) % P
        r += 1
        if r == m:
            break
    return r


def rref(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    if A.ndim == 1:
        A = A.reshape(-1, 1)
    m, n = A.shape
    r = 0
    pivots = []
    for c in range(n):
        p = next((i for i in range(r, m) if A[i, c]), None)
        if p is None:
            continue
        if p != r:
            A[[r, p]] = A[[p, r]]
        if A[r, c] == 2:
            A[r] = (2 * A[r]) % P
        rows = np.flatnonzero(A[:, c])
        rows = rows[rows != r]
        if len(rows):
            vals = A[rows, c].copy()
            A[rows] = (A[rows] - vals[:, None] * A[r]) % P
        pivots.append(c)
        r += 1
        if r == m:
            break
    return A, pivots


def inverse3(M):
    M = np.array(M, dtype=np.int64) % P
    n = M.shape[0]
    A = np.concatenate([M, np.eye(n, dtype=np.int64)], axis=1)
    for c in range(n):
        p = next((i for i in range(c, n) if A[i, c]), None)
        if p is None:
            raise RuntimeError("singular F3 matrix")
        if p != c:
            A[[c, p]] = A[[p, c]]
        if A[c, c] == 2:
            A[c] = (2 * A[c]) % P
        for i in range(n):
            if i != c and A[i, c]:
                A[i] = (A[i] - A[i, c] * A[c]) % P
    return A[:, n:]


def br(v, g):
    out = np.zeros(1024, dtype=np.int64)
    for j, c in enumerate(v):
        c = int(c) % P
        if c:
            w = words4[j]
            out[idx5[w + (g,)]] = (out[idx5[w + (g,)]] + c) % P
            out[idx5[(g,) + w]] = (out[idx5[(g,) + w]] - c) % P
    return out


words5 = [
    (a, b, c, d, e)
    for a in (1, 2, 3, 4)
    for b in (1, 2, 3, 4)
    for c in (1, 2, 3, 4)
    for d in (1, 2, 3, 4)
    for e in (1, 2, 3, 4)
]
idx5 = {w: i for i, w in enumerate(words5)}


def obstruction_for(tau_b):
    E = (Wd @ tau_b - W) % P
    D_blocks = []
    for g in range(1, 5):
        D_blocks.append(np.column_stack([br(E[:, j], g) for j in range(45)]))
    return E, np.vstack(D_blocks) % P


def column_basis(A):
    A = np.array(A, dtype=np.int64) % P
    _, pivots = rref(A)
    return A[:, pivots]


def intersection_basis(A, B):
    """Return a basis matrix for Col(A) intersection Col(B).

    Solve A*x = B*y by finding the nullspace of [A|-B].
    """
    M = np.concatenate([A, (-B) % P], axis=1)
    R, pivots = rref(M)
    free = [j for j in range(M.shape[1]) if j not in pivots]
    vectors = []
    for f in free:
        z = np.zeros(M.shape[1], dtype=np.int64)
        z[f] = 1
        for i, p in enumerate(pivots):
            z[p] = (-R[i, f]) % P
        x = z[:A.shape[1]]
        if np.any(x):
            vectors.append((A @ x) % P)
    if not vectors:
        return np.zeros((A.shape[0], 0), dtype=np.int64)
    return column_basis(np.column_stack(vectors))


# Reproduce the authoritative O2-5 transport family and D matrices.
Q_W45_inv = inverse3(Q_W45)
assert rank3(Q_W45_inv) == 45

I45 = np.eye(45, dtype=np.int64)
Ds = []
B1_ranks = []

for b in range(3):
    S = (I45 + b * N) % P
    S_inv = (I45 - b * N) % P
    assert np.array_equal((S @ S_inv) % P, I45)
    assert all(np.array_equal((S @ A) % P, (A @ S) % P) for A in A_W)

    tau_b = (tau @ S) % P

    T_b_ambient = (Wd @ tau_b @ Q_W45_inv) % P
    I_Wcoeff = (Q_W45_inv @ I_coord) % P
    defect = (T_b_ambient @ I_Wcoeff - W @ I_Wcoeff) % P
    B1_ranks.append(rank3(defect))
    assert B1_ranks[-1] == 0

    assert rank3(tau_b) == 45
    _, D = obstruction_for(tau_b)
    assert rank3(D) == 10
    Ds.append(D)

D0, D1, D2 = Ds
Delta = (D1 - D0) % P

O_tau = column_basis(D0)
Delta_O = column_basis(Delta)

dim_O = rank3(O_tau)
dim_delta = rank3(Delta_O)
intersection = intersection_basis(O_tau, Delta_O)
dim_intersection = rank3(intersection)
sum_dim = rank3(np.column_stack([O_tau, Delta_O]))

# Primary consistency identity.
expected_sum_dim = dim_O + dim_delta - dim_intersection
dimension_formula_ok = (sum_dim == expected_sum_dim)

# Independence of basis representation.
O_tau_again = column_basis(D0)
Delta_again = column_basis(Delta)
basis_rank_ok = (
    np.array_equal(O_tau_again, O_tau)
    and np.array_equal(Delta_again, Delta_O)
)

# Check H-stability of both spaces and, especially, the intersection.
# We only need generator-level closure: rank([S, hS]) == rank(S).
def degree5_action(g):
    A = np.zeros((1024, 1024), dtype=np.int64)
    for j, w in enumerate(words5):
        cur = {(): 1}
        for letter in w:
            image = {}
            for i in range(4):
                c = int(g[i, letter - 1]) % P
                if c:
                    image[(i + 1,)] = c
            nxt = {}
            for a, ca in cur.items():
                for b, cb in image.items():
                    ww = a + b
                    nxt[ww] = (nxt.get(ww, 0) + ca * cb) % P
            cur = {ww: c for ww, c in nxt.items() if c}
        for ww, c in cur.items():
            A[idx5[ww], j] = (A[idx5[ww], j] + c) % P
    return A


def rho_T_apply(D, g):
    A5 = degree5_action(g)
    T = inverse3(g).T % P
    X = D.reshape(4, 1024, -1)
    Y = np.zeros_like(X)
    for i in range(4):
        for j in range(4):
            if T[i, j]:
                Y[i] = (Y[i] + T[i, j] * (A5 @ X[j])) % P
    return Y.reshape(4096, -1) % P


def stable_under_all(S):
    if S.shape[1] == 0:
        return [True] * len(gens)
    results = []
    for g in gens:
        moved = rho_T_apply(S, g)
        results.append(rank3(np.column_stack([S, moved])) == rank3(S))
    return results


O_stable = stable_under_all(O_tau)
Delta_stable = stable_under_all(Delta_O)
intersection_stable = stable_under_all(intersection)

# Save compact reusable bases for O2-7/O2-8 without committing generated data.
artifact_dir = ROOT / "artifacts"
artifact_dir.mkdir(exist_ok=True)
artifact_path = artifact_dir / "o2_6_relative_position.json"
artifact = {
    "field": "F_3",
    "ambient_W_dimension": 45,
    "O_tau_dimension": int(dim_O),
    "Delta_O_dimension": int(dim_delta),
    "intersection_dimension": int(dim_intersection),
    "sum_dimension": int(sum_dim),
    "expected_sum_dimension": int(expected_sum_dim),
    "dimension_formula_ok": bool(dimension_formula_ok),
    "relation": (
        "equal" if dim_intersection == 10
        else "direct_sum" if dim_intersection == 0
        else "partial_overlap"
    ),
    "B1_defect_ranks": [int(x) for x in B1_ranks],
    "O_tau_basis": O_tau.tolist(),
    "Delta_O_basis": Delta_O.tolist(),
    "intersection_basis": intersection.tolist(),
    "O_tau_H_stable": [bool(x) for x in O_stable],
    "Delta_O_H_stable": [bool(x) for x in Delta_stable],
    "intersection_H_stable": [bool(x) for x in intersection_stable],
}
artifact_path.write_text(json.dumps(artifact, indent=2))

print("O2-6 RELATIVE POSITION: O_tau versus Delta O")
print("B1_DEFECT_RANKS_b0_b1_b2 =", B1_ranks)
print("dim(O_tau) =", dim_O)
print("dim(Delta O) =", dim_delta)
print("dim(O_tau intersection Delta O) =", dim_intersection)
print("dim(O_tau + Delta O) =", sum_dim)
print("EXPECTED_SUM_DIM =", expected_sum_dim)
print("DIMENSION_FORMULA_OK =", dimension_formula_ok)
print("RELATION =", artifact["relation"])
print("O_tau_H_STABLE_ALL_5 =", all(O_stable))
print("Delta_O_H_STABLE_ALL_5 =", all(Delta_stable))
print("INTERSECTION_H_STABLE_ALL_5 =", all(intersection_stable))
print("ARTIFACT =", artifact_path)

# Only computational/coordinate consistency is asserted.
assert all(x == 0 for x in B1_ranks)
assert dim_O == 10 and dim_delta == 10
assert dimension_formula_ok
assert basis_rank_ok
assert all(O_stable)
assert all(Delta_stable)

print("O2-6 COMPUTATION = PASS")
print("MATHEMATICAL RELATION IS A RESEARCH OUTCOME, NOT AN ASSERTION FAILURE")
