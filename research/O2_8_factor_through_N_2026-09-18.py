"""O2-8: factor the transport variation through Im(N).

Question:
    Delta D = D_1 - D_0 = D(tau N)

with N: W -> W.  The map tau N therefore has type W -> W in the
authoritative 45-dimensional coordinates, and the induced linear
obstruction map is

    F = D_linear o tau : Im(N) -> target,

where D_linear(S) is the bracket obstruction obtained from Wd S
(without the affine -W term).  This script explicitly checks the
type/coordinate identity before studying F.

It verifies:
1. rank(N)=10 and N^2=0;
2. exact factorization Delta D = D_linear(tau N);
3. F is computed on an explicit basis of Im(N);
4. Im(F)=Delta O;
5. ker(F), without inferring injectivity from equal dimensions.

Only coordinate/algebraic inconsistencies hard-fail.  Kernel/image
results are mathematical outcomes.
"""

from pathlib import Path
import runpy
import json
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
Q_W45 = np.array(ns_tau["Q_W45"], dtype=np.int64) % P
I_coord = np.array(ns_tau["I_coord"], dtype=np.int64) % P

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


def nullspace3(A):
    R, pivots = rref(A)
    n = R.shape[1]
    free = [j for j in range(n) if j not in pivots]
    basis = []
    for f in free:
        z = np.zeros(n, dtype=np.int64)
        z[f] = 1
        for i, p in enumerate(pivots):
            z[p] = (-R[i, f]) % P
        basis.append(z)
    return np.column_stack(basis) if basis else np.zeros((n, 0), dtype=np.int64)


def br(v, g):
    out = np.zeros(1024, dtype=np.int64)
    for j, c in enumerate(v):
        c = int(c) % P
        if c:
            w = words4[j]
            out[idx5[w + (g,)]] = (out[idx5[w + (g,)]] + c) % P
            out[idx5[(g,) + w]] = (out[idx5[(g,) + w]] - c) % P
    return out


def D_linear(S):
    """Linear part S -> bracket(Wd*S), target dimension 4096 x 45."""
    E = (Wd @ S) % P
    k = E.shape[1]
    return np.vstack([
        np.column_stack([br(E[:, j], g) for j in range(k)])
        for g in range(1, 5)
    ]) % P


def D_affine(S):
    """Original affine obstruction D(S), so D_affine(S)=D_linear(S)-D_linear(I)."""
    E = (Wd @ S - W) % P
    return np.vstack([
        np.column_stack([br(E[:, j], g) for j in range(45)])
        for g in range(1, 5)
    ]) % P


# ------------------------------------------------------------------
# Authoritative O2-5 family and exact factorization.
# ------------------------------------------------------------------
Q_W45_inv = inverse3(Q_W45)
assert rank3(Q_W45_inv) == 45

rank_N = rank3(N)
N2_zero = np.array_equal((N @ N) % P, np.zeros((45, 45), dtype=np.int64))
assert rank_N == 10
assert N2_zero

I45 = np.eye(45, dtype=np.int64)
tau0 = tau % P
tau1 = (tau @ ((I45 + N) % P)) % P

D0 = D_affine(tau0)
D1 = D_affine(tau1)
DeltaD = (D1 - D0) % P

# Type audit: all are endomorphisms of the authoritative 45-dimensional W coordinates.
type_audit = {
    "N_shape": list(N.shape),
    "tau_shape": list(tau.shape),
    "tauN_shape": list((tau @ N).shape),
    "N_is_W_to_W": N.shape == (45, 45),
    "tau_is_W_to_W_coordinate_representative": tau.shape == (45, 45),
    "tauN_is_W_to_W": (tau @ N).shape == (45, 45),
}
assert all(type_audit[k] for k in ["N_is_W_to_W", "tau_is_W_to_W_coordinate_representative", "tauN_is_W_to_W"])

# The affine -W cancels in D1-D0, so the correct factorization is linear.
tauN = (tau @ N) % P
D_tauN = D_linear(tauN)
factorization_exact = np.array_equal(DeltaD, D_tauN)
assert factorization_exact

# ------------------------------------------------------------------
# F = D_linear o tau restricted to Im(N).
# ------------------------------------------------------------------
ImN = column_basis(N)
assert ImN.shape == (45, 10)
assert rank3(ImN) == 10

F = D_linear((tau @ ImN) % P)
Delta_O = column_basis(DeltaD)

dim_ImN = rank3(ImN)
rank_F = rank3(F)
dim_DeltaO = rank3(Delta_O)

# Explicitly compare the images, not merely their dimensions.
images_equal = (
    rank3(np.column_stack([F, Delta_O])) == dim_DeltaO
    and rank_F == dim_DeltaO
)

# Kernel of F as a map from the 10-dimensional coordinate space of Im(N).
ker_F = nullspace3(F)
ker_F_dim = ker_F.shape[1]

# Strong consistency: F's nullity must agree with rank-nullity.
rank_nullity_ok = (rank_F + ker_F_dim == 10)

# If F is injective, it gives an explicit isomorphism Im(N) -> Delta O.
injective = (ker_F_dim == 0)
if injective:
    assert rank_F == 10
    assert images_equal

# ------------------------------------------------------------------
# Optional H-equivariance check for F on Im(N).
# N commutes with H, so Im(N) is H-stable.  The target action is rho_T.
# We verify F(hx)=rho_T(h)F(x) generator by generator.
# ------------------------------------------------------------------
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


# Restrict rho_T to DeltaO and A_W to ImN with exact basis coordinates.
def restrict_action(B, moved):
    rows = []
    R = np.empty((0, B.shape[1]), dtype=np.int64)
    rr = 0
    for i in range(B.shape[0]):
        C = np.vstack([R, B[i:i+1, :]])
        q = rank3(C)
        if q > rr:
            rows.append(i)
            R = C
            rr = q
            if rr == B.shape[1]:
                break
    assert rr == B.shape[1]
    Cinv = inverse3(R)
    coeff = (Cinv @ moved[rows, :]) % P
    assert np.array_equal((B @ coeff) % P, moved)
    return coeff


F_H_equivariant = []
for g, AW in zip(gens, A_W):
    moved_imn = (AW @ ImN) % P
    moved_F = rho_T_apply(F, g)
    src_action = restrict_action(ImN, moved_imn)
    lhs = (F @ src_action) % P
    rhs = moved_F % P
    F_H_equivariant.append(np.array_equal(lhs, rhs))

# ------------------------------------------------------------------
# Artifact.
# ------------------------------------------------------------------
artifact = {
    "field": "F_3",
    "W_dimension": 45,
    "N_shape": list(N.shape),
    "tau_shape": list(tau.shape),
    "tauN_shape": list(tauN.shape),
    "TYPE_AUDIT": type_audit,
    "rank_N": int(rank_N),
    "N_squared_zero": bool(N2_zero),
    "dim_ImN": int(dim_ImN),
    "DeltaD_shape": list(DeltaD.shape),
    "DeltaO_dimension": int(dim_DeltaO),
    "factorization_DeltaD_equals_D_tauN": bool(factorization_exact),
    "F_domain": "Im(N) with explicit 10-column basis",
    "F_definition": "D_linear o tau restricted to Im(N)",
    "F_rank": int(rank_F),
    "ker_F_dimension": int(ker_F_dim),
    "rank_nullity_ok": bool(rank_nullity_ok),
    "F_injective": bool(injective),
    "ImF_equals_DeltaO": bool(images_equal),
    "F_H_equivariant_per_generator": [bool(x) for x in F_H_equivariant],
    "F_H_equivariant_all_5": bool(all(F_H_equivariant)),
}

artifact_dir = ROOT / "artifacts"
artifact_dir.mkdir(exist_ok=True)
artifact_path = artifact_dir / "o2_8_factor_through_N.json"
artifact_path.write_text(json.dumps(artifact, indent=2))

print("O2-8: FACTORIZATION THROUGH Im(N)")
print("TYPE_AUDIT =", type_audit)
print("rank(N) =", rank_N)
print("N^2 = 0 =", N2_zero)
print("dim Im(N) =", dim_ImN)
print("DeltaD shape =", DeltaD.shape)
print("Delta O dimension =", dim_DeltaO)
print("DeltaD = D_linear(tau N) EXACT =", factorization_exact)
print("F = D_linear o tau | Im(N)")
print("rank(F) =", rank_F)
print("dim ker(F) =", ker_F_dim)
print("rank-nullity check =", rank_nullity_ok)
print("F injective =", injective)
print("Im(F) = Delta O =", images_equal)
print("F H-equivariant per generator =", F_H_equivariant)
print("F H-equivariant all 5 =", all(F_H_equivariant))
print("ARTIFACT =", artifact_path)
print("O2-8 COMPUTATION = PASS")
print("MATHEMATICAL OUTCOME: reported above; injectivity/image results are not hard-fail conditions.")

# Only computational consistency is hard-failed.
assert rank_nullity_ok
assert factorization_exact
assert rank_F == dim_DeltaO if images_equal else True
