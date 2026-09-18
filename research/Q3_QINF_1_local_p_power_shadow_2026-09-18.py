"""Q3/Qinf-1: local p-power shadow comparison.

This is deliberately smaller than a full q=infinity reconstruction.
It reuses the authoritative O2-7 coordinates/conventions and compares:
  q=3: d=[X1^[3],X2], with its nilpotent shadow N(d)
  q=infinity: d_inf=0, hence N(d_inf)=0

The experiment tests only the local p-power shadow distinction.
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
d = np.array(ns["d"], dtype=np.int64) % P
d_W = np.array(ns["d_W"], dtype=np.int64) % P
Nd = np.array((N @ d_W) % P, dtype=np.int64)

# q=infinity local p-power contribution is absent by definition of the
# comparison: d_inf = 0 in the same coordinate convention.
d_inf_W = np.zeros_like(d_W)
Nd_inf = (N @ d_inf_W) % P

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

rank_d_q3 = rank3(d_W)
rank_Nd_q3 = rank3(Nd)
rank_d_qinf = rank3(d_inf_W)
rank_Nd_qinf = rank3(Nd_inf)

q3_nonzero_shadow = rank_Nd_q3 > 0
qinf_zero_shadow = rank_Nd_qinf == 0
separates = q3_nonzero_shadow and qinf_zero_shadow

print("Q3/QINF-1 LOCAL P-POWER SHADOW COMPARISON")
print("rank(d_q3 in W coordinates) =", rank_d_q3)
print("rank(N(d_q3)) =", rank_Nd_q3)
print("rank(d_qinf in W coordinates) =", rank_d_qinf)
print("rank(N(d_qinf)) =", rank_Nd_qinf)
print("Q3_NONZERO_U_SHADOW =", q3_nonzero_shadow)
print("QINF_P_POWER_SHADOW_ZERO =", qinf_zero_shadow)
print("Q3_QINF_LOCAL_SHADOW_SEPARATES =", separates)

artifact = {
    "experiment": "Q3/QINF-1",
    "field": "F3",
    "source": "O2-7 authoritative coordinates/conventions",
    "rank_d_q3_W": rank_d_q3,
    "rank_Nd_q3": rank_Nd_q3,
    "rank_d_qinf_W": rank_d_qinf,
    "rank_Nd_qinf": rank_Nd_qinf,
    "q3_nonzero_U_shadow": q3_nonzero_shadow,
    "qinf_p_power_shadow_zero": qinf_zero_shadow,
    "local_shadow_separates": separates,
    "scope": "local p-power shadow only; not a full q=infinity reconstruction",
}
(ART / "q3_qinf_1_local_p_power_shadow.json").write_text(
    json.dumps(artifact, indent=2), encoding="utf-8"
)

assert rank_d_q3 == 1
assert q3_nonzero_shadow
assert qinf_zero_shadow
assert separates
print("Q3/QINF-1 RESULT = PASS")
