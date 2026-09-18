"""Q3/QINF-2: full canonical U-shadow generation.

Independent gate beyond Q3/QINF-1:
recompute the H-span of N(d_3) with a self-contained full-span
closure routine, then compare it with the authoritative U=im(N).

The q=infinity local p-power contribution is zero in this local model;
this experiment does not claim a full q=infinity reconstruction.
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
gens = [np.array(g, dtype=np.int64) % P for g in ns["action_matrices"]]

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

def independent_append(basis, v):
    v = np.array(v, dtype=np.int64).reshape(-1) % P
    if rank3(basis) == rank3(np.column_stack([basis, v])):
        return basis, False
    return np.column_stack([basis, v]), True

def full_h_span(v0):
    """Closure under every generator applied to every current basis vector."""
    basis = np.array(v0, dtype=np.int64).reshape(-1, 1) % P
    changed = True
    while changed:
        changed = False
        current = basis.copy()
        for j in range(current.shape[1]):
            v = current[:, j]
            for g in gens:
                basis, added = independent_append(basis, (g @ v) % P)
                changed = changed or added
    return basis

Nd = (N @ d_W) % P
U_basis = np.array(ns["U_basis"], dtype=np.int64) % P
shadow_basis = full_h_span(Nd)

shadow_rank = rank3(shadow_basis)
u_rank = rank3(U_basis)
join_rank = rank3(np.column_stack([shadow_basis, U_basis]))
equal_shadow = shadow_rank == u_rank == join_rank == 10

# q=infinity local p-power contribution in the same local model.
d_inf = np.zeros_like(d_W)
shadow_inf = full_h_span((N @ d_inf) % P)
qinf_rank = rank3(shadow_inf)

artifact = {
    "experiment": "Q3/QINF-2",
    "field": "F3",
    "source": "O2-7 authoritative coordinates/conventions",
    "closure": "independent full-span H-closure: every generator on every current basis vector",
    "rank_Nd_q3": rank3(Nd),
    "rank_H_span_Nd_q3": shadow_rank,
    "rank_U": u_rank,
    "rank_join_shadow_U": join_rank,
    "q3_shadow_equals_U": bool(equal_shadow),
    "qinf_shadow_rank": qinf_rank,
    "qinf_local_shadow_zero": bool(qinf_rank == 0),
    "scope": "canonical U-shadow generation in the local p-power comparison; not a full q=infinity reconstruction",
}
(ART / "q3_qinf_2_full_U_shadow.json").write_text(
    json.dumps(artifact, indent=2), encoding="utf-8"
)

print("Q3/QINF-2 FULL U-SHADOW GENERATION")
print("rank(N(d_q3)) =", rank3(Nd))
print("rank(<H.N(d_q3)>) =", shadow_rank)
print("rank(U=im(N)) =", u_rank)
print("rank(join(shadow,U)) =", join_rank)
print("Q3_SHADOW_EQUALS_U =", equal_shadow)
print("rank(<H.N(d_qinf)>) =", qinf_rank)
print("QINF_LOCAL_SHADOW_ZERO =", qinf_rank == 0)

assert rank3(Nd) == 1
assert shadow_rank == 10
assert u_rank == 10
assert join_rank == 10
assert equal_shadow
assert qinf_rank == 0
print("Q3/QINF-2 RESULT = PASS")
