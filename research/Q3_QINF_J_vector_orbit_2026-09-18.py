"""Q3/QINF-J: exact vector-orbit cardinality probe.

Substantive test:
    J(N(d_3)) = |H_U . N(d_3)|  ?= 1.

The q=infinity side is analytically fixed at J(0)=1; its execution
is only an implementation consistency check.

This script deliberately computes orbit cardinality, not H-span dimension.
It also audits |Sp4(F3)|, the kernel of H -> GL(U), and
orbit-stabilizer independently.
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

ns_base = runpy.run_path(str(ROOT / "phase2_1_invariant_space_verification_2026-09-15.py"))
gens4 = [np.array(g, dtype=np.int64) % P for g in ns_base["gens"]]

def rank3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    if A.ndim == 1: A = A.reshape(-1, 1)
    m, n = A.shape
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i, c]), None)
        if piv is None: continue
        if piv != r: A[[r, piv]] = A[[piv, r]]
        if A[r, c] == 2: A[r] = (2 * A[r]) % P
        for i in range(m):
            if i != r and A[i, c]:
                A[i] = (A[i] - A[i, c] * A[r]) % P
        r += 1
        if r == m: break
    return r

def solve_full_column(A, b):
    A = np.array(A, dtype=np.int64) % P
    b = np.array(b, dtype=np.int64) % P
    m, n = A.shape
    aug = np.concatenate([A, b.reshape(m, 1)], axis=1)
    row = 0
    pivots = []
    for c in range(n):
        piv = next((i for i in range(row, m) if aug[i, c]), None)
        if piv is None: continue
        if piv != row: aug[[row, piv]] = aug[[piv, row]]
        if aug[row, c] == 2: aug[row] = (2 * aug[row]) % P
        for i in range(m):
            if i != row and aug[i, c]:
                aug[i] = (aug[i] - aug[i, c] * aug[row]) % P
        pivots.append(c)
        row += 1
    if np.any(np.all(aug[:, :n] == 0, axis=1) & (aug[:, n] != 0)):
        raise AssertionError("target not in column span")
    x = np.zeros(n, dtype=np.int64)
    for i, c in enumerate(pivots): x[c] = aug[i, n]
    assert np.array_equal((A @ x) % P, b)
    return x

def independent_basis(A):
    A = np.array(A, dtype=np.int64) % P
    if A.ndim == 1: A = A.reshape(-1, 1)
    B = np.zeros((A.shape[0], 0), dtype=np.int64)
    r = 0
    for j in range(A.shape[1]):
        C = np.column_stack([B, A[:, j]])
        nr = rank3(C)
        if nr > r:
            B, r = C, nr
    return B

U_basis = independent_basis(N)
assert U_basis.shape == (45, 10) and rank3(U_basis) == 10
Nd = (N @ d_W) % P
assert rank3(Nd.reshape(-1, 1)) == 1
Nd_U = solve_full_column(U_basis, Nd)

def key(v):
    return tuple(int(x) for x in (np.asarray(v, dtype=np.int64) % P).tolist())

def orbit_closure(v0):
    start = np.asarray(v0, dtype=np.int64).reshape(-1) % P
    seen, queue = {key(start)}, [start]
    head = 0
    while head < len(queue):
        v = queue[head]; head += 1
        for A in A_W:
            w = (A @ v) % P
            k = key(w)
            if k not in seen:
                seen.add(k); queue.append(w)
                if len(seen) > 3**10:
                    raise AssertionError("orbit exceeded |U| bound")
    return seen

orbit_q3 = orbit_closure(Nd)
J_q3 = len(orbit_q3)
zero = np.zeros(45, dtype=np.int64)
orbit_qinf = orbit_closure(zero)
J_qinf = len(orbit_qinf)

orbit_matrix = np.array(list(orbit_q3), dtype=np.int64).T % P
assert rank3(np.column_stack([U_basis, orbit_matrix])) == 10
assert J_qinf == 1 and orbit_qinf == {key(zero)}

# Construct H and its induced action on U simultaneously.  The pair
# (4x4 group element, 10x10 U-action) prevents accidental identification
# of distinct H elements when testing the kernel.
I4 = np.eye(4, dtype=np.int64) % P
I10 = np.eye(10, dtype=np.int64) % P
A_U = []
for A in A_W:
    M = np.column_stack([
        solve_full_column(U_basis, (A @ U_basis[:, j]) % P)
        for j in range(10)
    ]) % P
    assert np.array_equal((U_basis @ M) % P, (A @ U_basis) % P)
    A_U.append(M)

def pair_key(g, m):
    return tuple(int(x) for x in g.reshape(-1)) + tuple(int(x) for x in m.reshape(-1))

group_seen = {pair_key(I4, I10)}
group_queue = [(I4, I10)]
head = 0
while head < len(group_queue):
    g, m = group_queue[head]; head += 1
    for G, M in zip(gens4, A_U):
        ng, nm = (G @ g) % P, (M @ m) % P
        k = pair_key(ng, nm)
        if k not in group_seen:
            group_seen.add(k); group_queue.append((ng, nm))
assert len(group_seen) == 51840

kernel_size = sum(np.array_equal(m, I10) for _, m in group_queue)
H_U_order = len(group_seen) // kernel_size
stab_size = sum(np.array_equal((m @ Nd_U) % P, Nd_U) for _, m in group_queue)

# Diagnostic audit of the kernel: in particular test the central element -I4.
minus_I4 = (-I4) % P
minus_I4_matches = [
    m for g, m in group_queue if np.array_equal(g, minus_I4)
]
minus_I4_in_H = (len(minus_I4_matches) == 1)
minus_I4_U_action_is_identity = (len(minus_I4_matches) == 1 and np.array_equal(minus_I4_matches[0], I10))

print("KERNEL_DIAGNOSTICS")
print("|ker(H -> GL(U))| =", kernel_size)
print("|H_U| =", H_U_order)
print("|Stab_HU(N(d_q3))| =", stab_size)
print("-I4_IN_H =", minus_I4_in_H)
print("-I4_U_ACTION_IS_IDENTITY =", minus_I4_U_action_is_identity)
print("ORBIT_STABILIZER_LHS =", H_U_order)
print("ORBIT_STABILIZER_RHS =", J_q3 * stab_size)

print("FIRST_ISOMORPHISM_CHECK =", kernel_size * H_U_order == len(group_seen))
print("ORBIT_STABILIZER_EXACT_CHECK =", H_U_order == J_q3 * stab_size)

artifact = {
    "experiment": "Q3/QINF-J",
    "field": "F3",
    "H_U_definition": "image of H -> GL(U)",
    "dim_U": 10,
    "U_size_bound": 3**10,
    "generators": 5,
    "orbit_algorithm": "BFS under every fixed generator",
    "J_Nd_q3": J_q3,
    "J_Nd_qinf": J_qinf,
    "Sp4_order": len(group_seen),
    "kernel_H_to_GL_U": kernel_size,
    "H_U_order": H_U_order,
    "stabilizer_Nd_q3": stab_size,
    "minus_I4_in_H": minus_I4_in_H,
    "minus_I4_U_action_is_identity": minus_I4_U_action_is_identity,
    "first_isomorphism_check": kernel_size * H_U_order == len(group_seen),
    "orbit_stabilizer_check": H_U_order == J_q3 * stab_size,
    "qinf_status": "IMPLEMENTATION-LEVEL CONSISTENCY / SANITY CHECK",
    "substantive_criterion": "J(N(d3)) != 1",
    "substantive_result": bool(J_q3 != 1),
    "span_dimension_not_used_as_J": True,
}
(ART / "q3_qinf_J_orbit.json").write_text(json.dumps(artifact, indent=2), encoding="utf-8")

print("Q3/QINF-J VECTOR ORBIT CARDINALITY")
print("dim(U) =", 10)
print("|U| bound =", 3**10)
print("rank(N(d_q3)) =", rank3(Nd.reshape(-1, 1)))
print("J(N(d_q3)) =", J_q3)
print("J(N(d_qinf=0)) =", J_qinf)
print("QINF_SANITY_CHECK =", J_qinf == 1)
print("Sp4(F3) generated order =", len(group_seen))
print("|ker(H -> GL(U))| =", kernel_size)
print("|H_U| =", H_U_order)
print("|Stab_HU(N(d_q3))| =", stab_size)
print("ORBIT_STABILIZER_CHECK =", H_U_order == J_q3 * stab_size)
print("SUBSTANTIVE_CRITERION_J_Q3_NE_1 =", J_q3 != 1)

assert J_qinf == 1
assert len(group_seen) == 51840
assert kernel_size * H_U_order == len(group_seen)
assert H_U_order == J_q3 * stab_size
print("Q3/QINF-J IMPLEMENTATION SANITY = PASS")
print("Q3/QINF-J SUBSTANTIVE RESULT =", "DISTINGUISHES" if J_q3 != 1 else "DOES_NOT_DISTINGUISH")
