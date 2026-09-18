"""O2-7: explicit H-module comparison Delta O (rho_T) versus U (standard W action).

Key representation convention:
- Delta O is a subspace of the 4096-dimensional target of D_stack.
- Its natural H-action is rho_T(g) = g^{-T} tensor A_5(g), inherited from
  D_stack A_W(g) = rho_T(g) D_stack.
- U = im(N) is a subspace of W and carries the standard action A_W(g).

Therefore the precise question is:
    (Delta O, rho_T) ?cong_H (U, A_W)
not an unqualified comparison of Delta O with U, and not an assumed
contragredient/dual replacement.

This script performs:
1. authoritative reconstruction of D_0,D_1 and Delta D=D_1-D_0;
2. basis construction for Delta O=im(Delta D) and U=im(N);
3. an explicit coordinate identification phi_0: Delta O -> U by matching
   the chosen independent bases, with invertibility/well-definedness checks;
4. direct generator-level equivariance test for phi_0;
5. independent 10x10 Hom-space solve for any H-intertwiner Delta O -> U,
   so failure of phi_0 is not confused with non-isomorphism.

Mathematical negative outcomes are reported, not treated as workflow errors.
Only coordinate/algebraic inconsistencies hard-fail.
"""

from pathlib import Path
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

words5 = [
    (a, b, c, d, e)
    for a in (1, 2, 3, 4)
    for b in (1, 2, 3, 4)
    for c in (1, 2, 3, 4)
    for d in (1, 2, 3, 4)
    for e in (1, 2, 3, 4)
]
idx5 = {w: i for i, w in enumerate(words5)}


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


def column_basis(A):
    A = np.array(A, dtype=np.int64) % P
    _, pivots = rref(A)
    return A[:, pivots]


def br(v, g):
    out = np.zeros(1024, dtype=np.int64)
    for j, c in enumerate(v):
        c = int(c) % P
        if c:
            w = words4[j]
            out[idx5[w + (g,)]] = (out[idx5[w + (g,)]] + c) % P
            out[idx5[(g,) + w]] = (out[idx5[(g,) + w]] - c) % P
    return out


def obstruction_for(tau_b):
    E = (Wd @ tau_b - W) % P
    D = np.vstack([
        np.column_stack([br(E[:, j], g) for j in range(45)])
        for g in range(1, 5)
    ]) % P
    return E, D


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


def rho_T_apply(X, g):
    """Apply rho_T(g)=g^{-T} tensor A5(g) to stacked 4-block vectors."""
    A5 = degree5_action(g)
    T = inverse3(g).T % P
    X = np.array(X, dtype=np.int64) % P
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    blocks = X.reshape(4, 1024, -1)
    moved = np.zeros_like(blocks)
    for i in range(4):
        for j in range(4):
            if T[i, j]:
                moved[i] = (moved[i] + T[i, j] * (A5 @ blocks[j])) % P
    return moved.reshape(4096, -1) % P


def solve_intertwiner_space(A_src, A_tgt):
    """Return all basis vectors of Hom(A_src,A_tgt) in F3.

    We solve P A_src = A_tgt P for P in Mat_10(F3).
    """
    rows = []
    for src, tgt in zip(A_src, A_tgt):
        for r in range(10):
            for c in range(10):
                row = np.zeros(100, dtype=np.int64)
                # (P src)[r,c] = sum_k P[r,k] src[k,c]
                for k in range(10):
                    row[r * 10 + k] = (row[r * 10 + k] + src[k, c]) % P
                    # (tgt P)[r,c] = sum_k tgt[r,k] P[k,c]
                    row[k * 10 + c] = (row[k * 10 + c] - tgt[r, k]) % P
                rows.append(row)
    M = np.array(rows, dtype=np.int64) % P
    R, pivots = rref(M)
    free = [j for j in range(100) if j not in pivots]
    basis = []
    for f in free:
        z = np.zeros(100, dtype=np.int64)
        z[f] = 1
        for i, p in enumerate(pivots):
            z[p] = (-R[i, f]) % P
        basis.append(z.reshape(10, 10) % P)
    return basis


# ------------------------------------------------------------------
# Authoritative reconstruction of the O2-5 family.
# ------------------------------------------------------------------
Q_W45_inv = inverse3(Q_W45)
assert rank3(Q_W45_inv) == 45
assert rank3(N) == 10
assert np.array_equal((N @ N) % P, np.zeros((45, 45), dtype=np.int64))

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

    _, D = obstruction_for(tau_b)
    assert rank3(tau_b) == 45
    assert rank3(D) == 10
    Ds.append(D)

D0, D1 = Ds[0], Ds[1]
Delta = (D1 - D0) % P

Delta_O = column_basis(Delta)
U = column_basis(N)

dim_delta = rank3(Delta_O)
dim_u = rank3(U)
assert dim_delta == 10 and dim_u == 10
assert Delta_O.shape == (4096, 10)
assert U.shape == (45, 10)

# ------------------------------------------------------------------
# Restrict the two H-actions to 10-dimensional bases.
# Delta O: rho_T; U: standard A_W.
# ------------------------------------------------------------------
Delta_action = []
U_action = []

for g, AW in zip(gens, A_W):
    moved_delta = rho_T_apply(Delta_O, g)
    assert rank3(np.column_stack([Delta_O, moved_delta])) == 10

    # Since Delta_O has full column rank, solve Delta_O * C = moved_delta.
    # Use an invertible 10-row minor of Delta_O.
    rows = []
    R = np.empty((0, 10), dtype=np.int64)
    rr = 0
    for i in range(4096):
        C = np.vstack([R, Delta_O[i:i+1, :]])
        q = rank3(C)
        if q > rr:
            rows.append(i)
            R = C
            rr = q
            if rr == 10:
                break
    assert rr == 10
    Delta_minor_inv = inverse3(R)
    Cdelta = (Delta_minor_inv @ moved_delta[rows, :]) % P
    assert np.array_equal((Delta_O @ Cdelta) % P, moved_delta)
    Delta_action.append(Cdelta)

    # Same construction for U under the standard W action.
    moved_u = (AW @ U) % P
    rows_u = []
    Ru = np.empty((0, 10), dtype=np.int64)
    rr = 0
    for i in range(45):
        C = np.vstack([Ru, U[i:i+1, :]])
        q = rank3(C)
        if q > rr:
            rows_u.append(i)
            Ru = C
            rr = q
            if rr == 10:
                break
    assert rr == 10
    U_minor_inv = inverse3(Ru)
    Cu = (U_minor_inv @ moved_u[rows_u, :]) % P
    assert np.array_equal((U @ Cu) % P, moved_u)
    U_action.append(Cu)

# ------------------------------------------------------------------
# Explicit basis-matching map phi_0: Delta_O -> U.
# If x=Delta_O*c, phi_0(x)=U*c.
# This is well-defined exactly because Delta_O has independent columns.
# ------------------------------------------------------------------
phi0 = U % P
# As an ambient map from Delta_O to U, its coordinate matrix is I_10.
phi0_rank = rank3(np.eye(10, dtype=np.int64))
map_well_defined = (rank3(Delta_O) == 10 and rank3(U) == 10)
map_invertible = (phi0_rank == 10)

phi0_residuals = []
for Cdelta, Cu in zip(Delta_action, U_action):
    # phi_0(Cdelta c) = Cu c  <=>  Cu*Cdelta? Careful:
    # phi_0 is identity on coordinates, so equivariance requires Cdelta == Cu.
    phi0_residuals.append(np.array_equal(Cdelta % P, Cu % P))
phi0_equivariant = all(phi0_residuals)

# ------------------------------------------------------------------
# Independent isomorphism test: search the full Hom_H(Delta O,U).
# ------------------------------------------------------------------
hom_basis = solve_intertwiner_space(Delta_action, U_action)
invertible_intertwiner = None
for X in hom_basis:
    if rank3(X) == 10:
        invertible_intertwiner = X
        break

hom_dim = len(hom_basis)
module_isomorphic = invertible_intertwiner is not None

# ------------------------------------------------------------------
# Artifact: enough information to audit the representation convention.
# ------------------------------------------------------------------
artifact_dir = ROOT / "artifacts"
artifact_dir.mkdir(exist_ok=True)
artifact_path = artifact_dir / "o2_7_deltaO_vs_U.json"
artifact = {
    "field": "F_3",
    "delta_O_ambient_dimension": 4096,
    "delta_O_dimension": int(dim_delta),
    "U_ambient_dimension": 45,
    "U_dimension": int(dim_u),
    "delta_O_action": "rho_T(g) = g^{-T} tensor A5(g)",
    "U_action": "standard A_W(g) on W=45",
    "B1_defect_ranks": [int(x) for x in B1_ranks],
    "phi0_definition": "Delta_O_basis coordinates -> U_basis coordinates by identity matrix I_10",
    "MAP_WELL_DEFINED": bool(map_well_defined),
    "MAP_INVERTIBLE": bool(map_invertible),
    "PHI0_EQUIVARIANT_ALL_5": bool(phi0_equivariant),
    "PHI0_EQUIVARIANT_PER_GENERATOR": [bool(x) for x in phi0_residuals],
    "HOM_H_DIMENSION": int(hom_dim),
    "INVERTIBLE_INTERTWINER_EXISTS": bool(module_isomorphic),
    "MODULE_ISOMORPHISM_CONFIRMED": bool(module_isomorphic),
}

(artifact_dir / "o2_7_deltaO_vs_U.json").write_text(
    __import__("json").dumps(artifact, indent=2)
)

print("O2-7: DELTA O VS U — REPRESENTATION-AWARE MODULE COMPARISON")
print("DELTA_O_ACTION = rho_T(g) = g^{-T} tensor A5(g)")
print("U_ACTION = standard A_W(g) on W=45")
print("B1_DEFECT_RANKS_b0_b1_b2 =", B1_ranks)
print("dim(Delta O) =", dim_delta)
print("dim(U) =", dim_u)
print("MAP_WELL_DEFINED =", map_well_defined)
print("MAP_INVERTIBLE =", map_invertible)
print("PHI0_EQUIVARIANT_PER_GENERATOR =", phi0_residuals)
print("PHI0_EQUIVARIANT_ALL_5 =", phi0_equivariant)
print("HOM_H_DIMENSION =", hom_dim)
print("INVERTIBLE_INTERTWINER_EXISTS =", module_isomorphic)
print("MODULE_ISOMORPHISM_CONFIRMED =", module_isomorphic)
print("ARTIFACT =", artifact_path)

# Only computational consistency is hard-failed.
assert all(x == 0 for x in B1_ranks)
assert dim_delta == 10 and dim_u == 10
assert map_well_defined and map_invertible
assert all(rank3(C) == 10 for C in Delta_action)
assert all(rank3(C) == 10 for C in U_action)

# Mathematical outcomes are intentionally not asserted.
print("O2-7 COMPUTATION = PASS")
print("MATHEMATICAL OUTCOME: reported above; phi0 failure and/or no isomorphism are valid negative results.")
