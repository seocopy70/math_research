"""Q3/QINF-J: exact vector-orbit cardinality probe.

Substantive test:
    J(N(d_3)) = |H_U . N(d_3)|  ?= 1.

The q=infinity side is analytically fixed at J(0)=1; its execution
is only an implementation consistency check.

This script deliberately computes orbit cardinality, not the dimension
of the H-span.
"""
from pathlib import Path
import runpy
import json
import numpy as np

P = 3
ROOT = Path(__file__).parent
ART = ROOT / "artifacts"
ART.mkdir(exist_ok=True)

ns = runpy.run_path(str(ROOT / "O2_7_q_control_variation_module_2026-09-18.py"))
N = np.array(ns["N"], dtype=np.int64) % P
d_W = np.array(ns["d_W"], dtype=np.int64) % P
A_W = [np.array(A, dtype=np.int64) % P for A in ns["A_W"]]
U_image = N.copy()

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

def independent_basis(A):
    A = np.array(A, dtype=np.int64) % P
    if A.ndim == 1:
        A = A.reshape(-1, 1)
    basis = np.zeros((A.shape[0], 0), dtype=np.int64)
    r = 0
    for j in range(A.shape[1]):
        cand = np.column_stack([basis, A[:, j]])
        nr = rank3(cand)
        if nr > r:
            basis = cand
            r = nr
    return basis

U_basis = independent_basis(U_image)
assert U_basis.shape == (45, 10)
assert rank3(U_basis) == 10

Nd = (N @ d_W) % P
assert rank3(Nd.reshape(-1, 1)) == 1

# Coordinate-free orbit enumeration in the authoritative W coordinates.
# This is exactly the same vector set as the H_U-orbit, because the
# generators are the fixed generators of H and act through their image on U.
def vector_key(v):
    return tuple(int(x) for x in (np.array(v, dtype=np.int64) % P).tolist())

def orbit_closure(v0):
    start = np.array(v0, dtype=np.int64).reshape(-1) % P
    seen = {vector_key(start)}
    queue = [start]
    head = 0
    while head < len(queue):
        v = queue[head]
        head += 1
        for A in A_W:
            w = (A @ v) % P
            k = vector_key(w)
            if k not in seen:
                seen.add(k)
                queue.append(w)
                if len(seen) > 3**10:
                    raise AssertionError("orbit exceeded |U|=3^10 bound")
    return seen

orbit_q3 = orbit_closure(Nd)
J_q3 = len(orbit_q3)

zero = np.zeros(45, dtype=np.int64)
orbit_qinf = orbit_closure(zero)
J_qinf = len(orbit_qinf)

# Every q=3 orbit vector must lie in U=im(N).
orbit_matrix = np.array(list(orbit_q3), dtype=np.int64).T % P
assert rank3(np.column_stack([U_basis, orbit_matrix])) == 10
assert J_qinf == 1
assert orbit_qinf == {vector_key(zero)}

artifact = {
    "experiment": "Q3/QINF-J",
    "field": "F3",
    "H_U_definition": "image of H -> GL(U)",
    "action_coordinates": "authoritative W coordinates; orbit is the same vector set as in U",
    "generators": 5,
    "orbit_algorithm": "BFS/closure under every fixed generator",
    "explicit_inverses": False,
    "inverse_justification": "generators are invertible and generate H",
    "dim_U": 10,
    "U_size_bound": 3**10,
    "rank_Nd_q3": rank3(Nd.reshape(-1, 1)),
    "J_Nd_q3": J_q3,
    "J_Nd_qinf": J_qinf,
    "qinf_status": "IMPLEMENTATION-LEVEL CONSISTENCY / SANITY CHECK",
    "substantive_criterion": "J(N(d3)) != 1",
    "substantive_result": bool(J_q3 != 1),
    "span_dimension_not_used_as_J": True,
}
(ART / "q3_qinf_J_orbit.json").write_text(
    json.dumps(artifact, indent=2), encoding="utf-8"
)

print("Q3/QINF-J VECTOR ORBIT CARDINALITY")
print("dim(U) =", 10)
print("|U| bound =", 3**10)
print("rank(N(d_q3)) =", rank3(Nd.reshape(-1, 1)))
print("J(N(d_q3)) =", J_q3)
print("J(N(d_qinf=0)) =", J_qinf)
print("QINF_SANITY_CHECK =", J_qinf == 1)
print("SUBSTANTIVE_CRITERION_J_Q3_NE_1 =", J_q3 != 1)

assert J_qinf == 1
print("Q3/QINF-J IMPLEMENTATION SANITY = PASS")
print("Q3/QINF-J SUBSTANTIVE RESULT =", "DISTINGUISHES" if J_q3 != 1 else "DOES_NOT_DISTINGUISH")
