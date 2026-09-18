"""O2-9(pre): scalar compatibility of the O2-7 and O2-8 isomorphisms.

Compute Psi = Phi_0 o F : Im(N) -> U=Im(N), where
- Phi_0: Delta O -> U is the O2-7 basis-coordinate identification;
- F: Im(N) -> Delta O is the O2-8 injective, H-equivariant map.

Since O2-7 independently computed dim Hom_H(Delta O,U)=1, both
Phi_0 and F^{-1} must be scalar multiples. Thus Psi must be c I,
c in F_3^*={1,2}. We check the full 10x10 matrix exactly, including
all off-diagonal entries.
"""

from pathlib import Path
import runpy
import json
import numpy as np

P = 3
ROOT = Path(__file__).parent

ns7 = runpy.run_path(str(ROOT / "O2_7_deltaO_vs_U_representation_2026-09-18.py"))
ns8 = runpy.run_path(str(ROOT / "O2_8_factor_through_N_2026-09-18.py"))

# O2-7: Delta_O and U=Im(N), with Phi_0 defined by identity on coordinates.
Delta_O = np.array(ns7["Delta_O"], dtype=np.int64) % P
U = np.array(ns7["U"], dtype=np.int64) % P
hom_dim = int(ns7["hom_dim"])

# O2-8: F has domain coordinates given by the chosen Im(N) basis.
F = np.array(ns8["F"], dtype=np.int64) % P
ImN = np.array(ns8["ImN"], dtype=np.int64) % P

assert Delta_O.shape == (4096, 10)
assert U.shape == (45, 10)
assert ImN.shape == (45, 10)
assert F.shape == (4096, 10)
assert hom_dim == 1

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

def restrict_coordinate_map(B, Y):
    """Solve B*C=Y exactly over F3 using an invertible row minor."""
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
    C = (inverse3(R) @ Y[rows, :]) % P
    assert np.array_equal((B @ C) % P, Y % P)
    return C, rows

# F maps ImN-coordinate vectors to DeltaO. Recover F's 10x10
# coordinate matrix C_F from F = Delta_O * C_F.
C_F, delta_rows = restrict_coordinate_map(Delta_O, F)

# Phi_0 is the identity on the chosen DeltaO/U basis coordinates.
# Therefore Psi = Phi_0 o F is represented by C_F itself.
# The previous version incorrectly formed the ambient 45x10 matrix U*C_F.
Psi = C_F % P

I10 = np.eye(10, dtype=np.int64)
scalar_checks = {}
for c in (1, 2):
    scalar_checks[str(c)] = bool(np.array_equal(Psi, (c * I10) % P))

is_scalar = scalar_checks["1"] or scalar_checks["2"]
scalar = 1 if scalar_checks["1"] else 2 if scalar_checks["2"] else None

diag = [int(Psi[i, i]) for i in range(10)]
offdiag_nonzero = [
    [i, j, int(Psi[i, j])]
    for i in range(10)
    for j in range(10)
    if i != j and int(Psi[i, j]) % P != 0
]

# Full scalar condition means exact diagonal equality AND every off-diagonal is zero.
diagonal_scalar_ok = scalar is not None and all(x == scalar for x in diag)
offdiagonal_zero = len(offdiag_nonzero) == 0
full_scalar_exact = is_scalar and diagonal_scalar_ok and offdiagonal_zero

artifact = {
    "field": "F_3",
    "dim_Hom_H_DeltaO_U": hom_dim,
    "Phi0_definition": "identity on the chosen DeltaO/U basis coordinates",
    "F_definition": "O2-8 F = D_linear o tau restricted to Im(N)",
    "Psi_definition": "Phi0 o F",
    "Psi_coordinate_space": "10x10 coordinates on the Im(N) basis",
    "Psi_matrix": Psi.tolist(),
    "diagonal": diag,
    "offdiagonal_nonzero_entries": offdiag_nonzero,
    "Psi_equals_I": scalar_checks["1"],
    "Psi_equals_2I": scalar_checks["2"],
    "full_scalar_exact": full_scalar_exact,
    "scalar_c": scalar,
    "delta_minor_rows": delta_rows,
}

artifact_dir = ROOT / "artifacts"
artifact_dir.mkdir(exist_ok=True)
artifact_path = artifact_dir / "o2_9_pre_scalar_compatibility.json"
artifact_path.write_text(json.dumps(artifact, indent=2))

print("O2-9(pre): PHI0 / F INDEPENDENT COMPATIBILITY")
print("dim Hom_H(Delta O,U) =", hom_dim)
print("Psi shape =", Psi.shape)
print("Psi =")
print(Psi)
print("Psi diagonal =", diag)
print("OFFDIAGONAL_NONZERO_COUNT =", len(offdiag_nonzero))
print("OFFDIAGONAL_NONZERO_ENTRIES =", offdiag_nonzero)
print("Psi = I exactly =", scalar_checks["1"])
print("Psi = 2I exactly =", scalar_checks["2"])
print("FULL_SCALAR_EXACT =", full_scalar_exact)
print("SCALAR c =", scalar)
print("ARTIFACT =", artifact_path)

# This is a consistency experiment: non-scalar is a research/bug signal, not a
# mathematical theorem failure. We hard-fail here because the stated O2-9(pre)
# hypothesis is the exact compatibility being tested.
assert hom_dim == 1
assert full_scalar_exact

print("O2-9(pre) = PASS")
