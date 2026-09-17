"""O2-4: transport-independence test for the rank-10 obstruction.

Question:
    Does the O2-2/O2-3 obstruction image depend on the choice of
    H-equivariant transport tau, even after fixing the quotient map W/I ->
    Wd/I to be the canonical identity induced by the authoritative Q4
    coordinates?

Verified background:
    End_H(W) = F_3[I,N], N^2=0, rank(N)=10, I=ker(N).

Any H-equivariant automorphism of W which induces the identity on W/I has
form S_b = I + bN, b in F_3.  Therefore the three transports
    tau_b = tau o S_b,  b=0,1,2,
are the complete quotient-fixed transport family under the frozen
End_H(W) computation.

For each tau_b we recompute the stacked degree-5 bracket discrepancy D_b
and compare im(D_b).  Equality of all three images is the target PASS.
"""

from pathlib import Path
import runpy
import numpy as np

P = 3
ROOT = Path(__file__).parent

# Canonical authoritative tau / ambient setup.
ns_tau = runpy.run_path(str(ROOT / "A3-4-10_CANONICAL_TAU_REVALIDATION_2026-09-16.py"))
W = np.array(ns_tau["W"], dtype=np.int64) % P
Wd = np.array(ns_tau["Wd"], dtype=np.int64) % P
tau = np.array(ns_tau["tau_coord"], dtype=np.int64) % P
A_W = [np.array(A, dtype=np.int64) % P for A in ns_tau["A_W"]]
words4 = ns_tau["words4"]

# Authoritative N.
ns_N = runpy.run_path(str(ROOT / "phase2_3_endH_optimized_2026-09-15.py"))
N = np.array(ns_N["N"], dtype=np.int64) % P


def rank3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    if A.ndim == 1:
        A = A.reshape(-1, 1)
    m, n = A.shape
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i, c]), None)
        if pivot is None:
            continue
        if pivot != r:
            A[[r, pivot]] = A[[pivot, r]]
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


def inv3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    n = A.shape[0]
    E = np.column_stack([A, np.eye(n, dtype=np.int64)]) % P
    for c in range(n):
        q = next(i for i in range(c, n) if E[i, c])
        E[[c, q]] = E[[q, c]]
        if E[c, c] == 2:
            E[c] = (2 * E[c]) % P
        for i in range(n):
            if i != c and E[i, c]:
                E[i] = (E[i] - E[i, c] * E[c]) % P
    return E[:, n:]

# Degree-5 bracket on a degree-4 vector represented in the words4 basis.
words5 = [(a, b, c, d, e)
          for a in (1, 2, 3, 4)
          for b in (1, 2, 3, 4)
          for c in (1, 2, 3, 4)
          for d in (1, 2, 3, 4)
          for e in (1, 2, 3, 4)]
tuple_index = {w: i for i, w in enumerate(words5)}

def br(v, g):
    out = np.zeros(1024, dtype=np.int64)
    for j, c in enumerate(v):
        c = int(c) % P
        if c:
            w = words4[j]
            out[tuple_index[w + (g,)]] = (out[tuple_index[w + (g,)]] + c) % P
            out[tuple_index[(g,) + w]] = (out[tuple_index[(g,) + w]] - c) % P
    return out


def obstruction_for(tau_b):
    T_ambient = (Wd @ tau_b) % P
    E = (T_ambient - W) % P
    D = np.vstack([
        np.column_stack([br(E[:, j], g) for j in range(45)])
        for g in range(1, 5)
    ]) % P
    return E, D

# The quotient-fixed family S_b = I + bN.
I45 = np.eye(45, dtype=np.int64)
results = []
images = []

for b in range(3):
    S = (I45 + b * N) % P
    S_inv = (I45 - b * N) % P  # N^2=0
    assert np.array_equal((S @ S_inv) % P, I45)
    assert all(np.array_equal((S @ A) % P, (A @ S) % P) for A in A_W)
    # S induces identity on W/I because N(W) subset I.
    tau_b = (tau @ S) % P
    assert np.array_equal((tau_b @ N) % P, (tau @ N) % P)
    E, D = obstruction_for(tau_b)
    assert rank3(tau_b) == 45
    assert all(np.array_equal((Wd @ tau_b @ A) % P,
                              (Wd @ tau_b) @ A % P)
               for A in A_W)
    results.append((b, rank3(E), rank3(D)))
    images.append(D)

# Compare the three obstruction images as actual ambient subspaces.
pairwise_join_ranks = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(rank3(np.column_stack([images[i], images[j]])))
    pairwise_join_ranks.append(row)

all_equal = all(pairwise_join_ranks[i][j] == 10
                for i in range(3) for j in range(3))

print("O2-4 TRANSPORT-INDEPENDENCE / QUOTIENT-FIXED TEST")
print("End_H(W) = F3[I,N] with N^2=0, rank(N)=10")
print("candidate quotient-fixed transports: tau_b = tau o (I+bN), b=0,1,2")
for b, rank_E, rank_D in results:
    print(f"b={b}: rank(tau_b-id)={rank_E}, rank(D_b)={rank_D}")
print("pairwise join ranks of obstruction images:")
for row in pairwise_join_ranks:
    print(row)
print("all three obstruction images equal =", all_equal)

assert all_equal
assert all(rank_D == 10 for _, _, rank_D in results)
print("O2-4 RESULT = PASS")
print("The rank-10 obstruction image is unchanged across all quotient-fixed")
print("H-equivariant transports tau_b = tau o (I+bN), b in F3.")
