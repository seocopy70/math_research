"""Phase 2-13C sanity check.

The previous torus table was mathematically impossible as a group character:
chi(1,1)=2 and multiplicativity failed. This script is intentionally a
representation-law audit before any highest-weight interpretation.

It reuses the exact construction from Phase 2-13C and adds hard assertions
for identity, torus multiplication, quotient representation law, and the
fixed-line character.
"""

from pathlib import Path
import runpy
import numpy as np

P = 3
ROOT = Path(__file__).resolve().parents[1]

# Reuse the exact Phase 2-13C construction. The audit deliberately avoids
# changing the mathematical construction before testing it.
ns = runpy.run_path(str(ROOT / "research" / "phase2_13C_torus_character_2026-09-16.py"))

# The source script is expected to expose these names. If it does not, fail
# explicitly rather than silently reconstructing a different representation.
required = ["P", "torus_element", "quotient_action_single"]
missing = [x for x in required if x not in ns]
if missing:
    raise RuntimeError(f"Missing required Phase 2-13C symbols: {missing}")

# This script is a scaffold for the exact sanity assertions. The first run
# must report whether the underlying module exposes a true quotient action.
print("PHASE 2-13C / TORUS CHARACTER SANITY CHECK")
print("source construction loaded")

# The source script currently computes the full construction on import/run.
# We intentionally do not accept its printed character table. The following
# checks are required once its internal objects are exposed consistently.

T = [(1,1), (1,2), (2,1), (2,2)]

def mm3(A, B):
    return (np.asarray(A, dtype=np.int64) @ np.asarray(B, dtype=np.int64)) % P

def eq3(A, B):
    return np.array_equal(np.asarray(A, dtype=np.int64) % P,
                          np.asarray(B, dtype=np.int64) % P)

# Exact 4x4 torus elements.
Ts = {ab: np.asarray(ns["torus_element"](*ab), dtype=np.int64) % P for ab in T}
I4 = np.eye(4, dtype=np.int64) % P
assert eq3(Ts[(1,1)], I4), "FAIL: t(1,1) is not the identity 4x4 matrix"
print("PASS: t(1,1) = I4")

# Extract quotient actions. The function must be deterministic and return
# genuine 35x35 matrices.
As = {ab: np.asarray(ns["quotient_action_single"](Ts[ab]), dtype=np.int64) % P for ab in T}
for ab, A in As.items():
    assert A.shape == (35,35), f"FAIL: quotient action shape for {ab}: {A.shape}"

I35 = np.eye(35, dtype=np.int64) % P
assert eq3(As[(1,1)], I35), "FAIL: rho(1,1) is not I35"
print("PASS: rho(1,1) = I35")

# Representation law on all 16 torus pairs.
for a in T:
    for b in T:
        ab = ((a[0]*b[0]) % P, (a[1]*b[1]) % P)
        assert eq3(mm3(As[a], As[b]), As[ab]), \
            f"FAIL: rho({a})rho({b}) != rho({ab})"
print("PASS: rho(t1*t2) = rho(t1)rho(t2) for all torus pairs")

# The unique U+ fixed line must be exposed by the source script for the
# scalar extraction. Do not infer a scalar from an arbitrary basis ratio.
if "fixed_line_basis" not in ns:
    raise RuntimeError("Missing fixed_line_basis; character extraction cannot be certified")

line = np.asarray(ns["fixed_line_basis"], dtype=np.int64) % P
if line.ndim == 2:
    assert line.shape[1] == 1, f"Expected 1D fixed line, got {line.shape}"
    v = line[:,0]
else:
    v = line
assert v.shape == (35,), f"Unexpected fixed vector shape: {v.shape}"
assert np.any(v % P), "Fixed-line vector is zero"

# Exact scalar extraction on a nonzero coordinate.
def scalar_on_line(A, v):
    Av = (A @ v) % P
    nz = np.flatnonzero(v % P)
    for i in nz:
        vi = int(v[i] % P)
        ai = int(Av[i] % P)
        inv = 1 if vi == 1 else 2
        lam = (ai * inv) % P
        if np.array_equal((Av - lam*v) % P, np.zeros_like(v)):
            return lam
        raise AssertionError("Vector is not an eigenvector of the claimed line action")
    raise AssertionError("No nonzero coordinate in fixed-line vector")

chi = {ab: scalar_on_line(As[ab], v) for ab in T}
print("CERTIFIED CANDIDATE CHARACTER TABLE:", sorted((a,b,chi[(a,b)]) for a,b in T))

assert chi[(1,1)] == 1, f"FAIL: chi(1,1) = {chi[(1,1)]}, expected 1"
assert (chi[(2,1)] * chi[(1,2)]) % P == chi[(2,2)], \
    "FAIL: torus character is not multiplicative"
print("PASS: chi(1,1) = 1")
print("PASS: chi(2,1)*chi(1,2) = chi(2,2)")
print("PHASE 2-13C SANITY CHECK PASSED")
