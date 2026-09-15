"""Phase 2-13C sanity check.

The previous torus table was mathematically impossible as a group character:
chi(1,1)=2 and multiplicativity failed. This audit checks the representation
law first, then extracts the 1-dimensional character, and finally verifies
that the character is one of the four and only four characters of
T(F_3) ~= (F_3^*)^2 ~= (Z/2)^2.

Audit record: strengthened exhaustive character classification retained in
PHASE2_13C_CURRENT_STATUS_2026-09-16.md.
"""

from pathlib import Path
import runpy
import numpy as np

P = 3
ROOT = Path(__file__).resolve().parents[1]

# Reuse the exact Phase 2-13C construction. Do not silently reconstruct a
# different representation in the audit.
ns = runpy.run_path(str(ROOT / "research" / "phase2_13C_torus_character_2026-09-16.py"))
required = ["P", "torus", "quotient_action_single", "fixed"]
missing = [x for x in required if x not in ns]
if missing:
    raise RuntimeError(f"Missing required Phase 2-13C symbols: {missing}")

P = int(ns["P"])
assert P == 3
T = [(1,1), (1,2), (2,1), (2,2)]

def mm3(A, B):
    return (np.asarray(A, dtype=np.int64) @ np.asarray(B, dtype=np.int64)) % P

def eq3(A, B):
    return np.array_equal(np.asarray(A, dtype=np.int64) % P,
                          np.asarray(B, dtype=np.int64) % P)

print("PHASE 2-13C / TORUS CHARACTER SANITY CHECK")

Ts = {ab: np.asarray(ns["torus"](*ab), dtype=np.int64) % P for ab in T}
I4 = np.eye(4, dtype=np.int64) % P
assert eq3(Ts[(1,1)], I4), "FAIL: t(1,1) is not I4"
print("PASS: t(1,1) = I4")

for a in T:
    for b in T:
        ab = ((a[0] * b[0]) % P, (a[1] * b[1]) % P)
        assert eq3(mm3(Ts[a], Ts[b]), Ts[ab]), \
            f"FAIL: torus multiplication for {a},{b}"
print("PASS: torus multiplication law on all 16 pairs")

As = {ab: np.asarray(ns["quotient_action_single"](Ts[ab]), dtype=np.int64) % P
      for ab in T}
for ab, A in As.items():
    assert A.shape == (35,35), f"FAIL: quotient action shape for {ab}: {A.shape}"

I35 = np.eye(35, dtype=np.int64) % P
assert eq3(As[(1,1)], I35), "FAIL: rho(1,1) is not I35"
print("PASS: rho(1,1) = I35")

for a in T:
    for b in T:
        ab = ((a[0] * b[0]) % P, (a[1] * b[1]) % P)
        assert eq3(mm3(As[a], As[b]), As[ab]), \
            f"FAIL: rho({a})rho({b}) != rho({ab})"
print("PASS: rho(t1*t2) = rho(t1)rho(t2) for all torus pairs")

fixed = ns["fixed"]
assert len(fixed) == 1, f"FAIL: expected one fixed-line basis vector, got {len(fixed)}"
v = np.asarray(fixed[0], dtype=np.int64) % P
assert v.shape == (35,), f"FAIL: unexpected fixed vector shape {v.shape}"
assert np.any(v), "FAIL: fixed-line vector is zero"

def rank3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
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

def scalar_on_line(A, v):
    Av = (A @ v) % P
    if rank3(np.column_stack([v, Av])) > 1:
        raise AssertionError("FAIL: torus action does not preserve the claimed fixed line")
    i = int(np.flatnonzero(v)[0])
    vi = int(v[i] % P)
    inv = 1 if vi == 1 else 2
    lam = (int(Av[i]) * inv) % P
    assert np.array_equal((Av - lam * v) % P, np.zeros_like(v)), \
        "FAIL: scalar extraction did not reproduce the full vector"
    return lam

chi = {ab: scalar_on_line(As[ab], v) for ab in T}
print("CHARACTER_TABLE =", [(a, b, chi[(a,b)]) for a,b in T])

assert chi[(1,1)] == 1, f"FAIL: chi(1,1) = {chi[(1,1)]}, expected 1"
for a in T:
    for b in T:
        ab = ((a[0] * b[0]) % P, (a[1] * b[1]) % P)
        assert (chi[a] * chi[b]) % P == chi[ab], \
            f"FAIL: character multiplicativity for {a},{b}"
print("PASS: chi(1,1) = 1")
print("PASS: chi is multiplicative on all 16 torus pairs")

expected_patterns = {
    "trivial": (1,1,1,1),
    "first_coordinate": (1,1,2,2),
    "second_coordinate": (1,2,1,2),
    "product": (1,2,2,1),
}
observed = tuple(chi[ab] for ab in T)
matches = [name for name, pattern in expected_patterns.items() if observed == pattern]
assert len(matches) == 1, \
    f"FAIL: extracted character {observed} is not exactly one of the four characters; matches={matches}"
print("PASS: character matches exactly one of the four Hom(T(F3), F3^*) patterns")
print("MATCHED_CHARACTER =", matches[0])
print("PHASE 2-13C SANITY CHECK PASSED")
