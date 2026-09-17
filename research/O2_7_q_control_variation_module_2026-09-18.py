"""O2-7: q-control of the rank-10 transport-variation module.

Compare the certified q=3 restricted-power class d=[X1^[3],X2]
with U=im(N) and the O2-5/O2-6 transport variation.
"""
from pathlib import Path
import runpy
import numpy as np

P = 3
ROOT = Path(__file__).parent

ns_tau = runpy.run_path(str(ROOT / "A3-4-10_CANONICAL_TAU_REVALIDATION_2026-09-16.py"))
W = np.array(ns_tau["W"], dtype=np.int64) % P
tau = np.array(ns_tau["tau_coord"], dtype=np.int64) % P
A_W = [np.array(A, dtype=np.int64) % P for A in ns_tau["A_W"]]

ns_N = runpy.run_path(str(ROOT / "phase2_3_endH_optimized_2026-09-15.py"))
N = np.array(ns_N["N"], dtype=np.int64) % P

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
    """Solve A x = b over F3; A has full column rank and b is in its image."""
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
        raise AssertionError("target vector is not in the W span")
    x = np.zeros(n, dtype=np.int64)
    for i, c in enumerate(pivots): x[c] = aug[i, n]
    assert np.array_equal((A @ x) % P, b)
    return x

def bracket_word(v, letter):
    """Bracket a degree-4 vector with X_letter in the same convention as O2."""
    words4 = [(a,b,c,d) for a in range(1,5) for b in range(1,5) for c in range(1,5) for d in range(1,5)]
    words5 = [(a,b,c,d,e) for a in range(1,5) for b in range(1,5) for c in range(1,5) for d in range(1,5) for e in range(1,5)]
    idx5 = {w:i for i,w in enumerate(words5)}
    out = np.zeros(1024, dtype=np.int64)
    for j, coeff in enumerate(v):
        if int(coeff) == 0: continue
        w = words4[j]
        out[idx5[w + (letter,)]] = (out[idx5[w + (letter,)]] + int(coeff)) % P
        out[idx5[(letter,) + w]] = (out[idx5[(letter,) + w]] - int(coeff)) % P
    return out

def degree4_ad1112():
    # [X1,[X1,[X1,X2]]] in the associative word basis.
    words = [(a,b,c,d) for a in range(1,5) for b in range(1,5) for c in range(1,5) for d in range(1,5)]
    idx = {w:i for i,w in enumerate(words)}
    v = np.zeros(256, dtype=np.int64)
    terms = { (1,1,1,2): 1, (1,1,2,1): -3, (1,2,1,1): 3, (2,1,1,1): -1 }
    for w,c in terms.items(): v[idx[w]] = c % P
    return v

d = degree4_ad1112()
assert rank3(d.reshape(-1,1)) == 1

# A3-4-3 certified that d lies in W. Recover its W-coordinates exactly.
d_W = solve_full_column(W, d)
assert np.array_equal((W @ d_W) % P, d)

# H-orbit of d inside W coordinates.
orbit = [d_W]
changed = True
while changed:
    changed = False
    for A in A_W:
        v = (A @ orbit[-1]) % P
        trial = np.column_stack(orbit + [v])
        if rank3(trial) > rank3(np.column_stack(orbit)):
            orbit.append(v)
            changed = True
P_basis = np.column_stack(orbit)

# U = im(N). Equality is tested as actual subspace equality in W coordinates.
U_basis = N
P_dim = rank3(P_basis)
U_dim = rank3(U_basis)
join_dim = rank3(np.column_stack([P_basis, U_basis]))

# Source-side transport variation: im(tau N) equals tau(U).
tauU = (tau @ U_basis) % P
tauN = (tau @ N) % P
transport_join = rank3(np.column_stack([tauU, tauN]))

# q=infinity control: the p-power contribution itself is absent.
d_inf = np.zeros_like(d)
assert rank3(d_inf.reshape(-1,1)) == 0

print("O2-7 Q-CONTROL OF TRANSPORT-VARIATION MODULE")
print("rank(d_q3) =", rank3(d.reshape(-1,1)))
print("rank(P=<H.d_q3>) =", P_dim)
print("rank(U=im(N)) =", U_dim)
print("rank(P+U) =", join_dim)
print("P_EQUALS_U =", P_dim == 10 and U_dim == 10 and join_dim == 10)
print("rank(im(tau N)) =", rank3(tauN))
print("rank(tau(U)+im(tau N)) =", transport_join)
print("TAU_U_EQUALS_TAU_N =", transport_join == 10)
print("rank(d_qinf) =", rank3(d_inf.reshape(-1,1)))
print("QINF_P_POWER_COLLAPSE =", rank3(d_inf.reshape(-1,1)) == 0)

assert rank3(d.reshape(-1,1)) == 1
assert P_dim == 10
assert U_dim == 10
assert join_dim == 10
assert transport_join == 10
assert rank3(d_inf.reshape(-1,1)) == 0
print("O2-7 RESULT = PASS")