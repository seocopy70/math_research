import runpy
import numpy as np
from itertools import product

P = 3
ROOT = 'research/'

# Reuse the already-verified TRUE-Wd revalidation construction.  In particular,
# reuse its quotient coordinates instead of rebuilding a second copy of the
# L4 = R4 + complement coordinate system here.
ns = runpy.run_path(ROOT + 'A3-4-REVALIDATION_I_AND_K_TRUE_Wd_2026-09-16.py')
rank3 = ns['rank3']
W = np.array(ns['W45'], dtype=np.int64) % P
Wd = np.array(ns['Wd'], dtype=np.int64) % P
I = np.array(ns['I_coord'], dtype=np.int64) % P
Q_W45 = np.array(ns['Q_W45'], dtype=np.int64) % P
Q_Wd = np.array(ns['Q_Wd'], dtype=np.int64) % P
A_W = [np.array(a, dtype=np.int64) % P for a in ns['A_W']]
words4 = list(ns['index4'].keys())

assert W.shape == (256, 45) and rank3(W) == 45
assert Wd.shape == (256, 45) and rank3(Wd) == 45
assert rank3(I) == 35
assert Q_W45.shape == (45, 45) and rank3(Q_W45) == 45
assert Q_Wd.shape == (45, 45) and rank3(Q_Wd) == 45


def inv3(A):
    A = np.array(A, dtype=np.int64) % P
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


def br(v, g):
    out = np.zeros(1024, dtype=np.int64)
    for j, c in enumerate(v):
        c = int(c) % P
        if c:
            w = words4[j]
            out[tuple_index[w + (g,)]] = (out[tuple_index[w + (g,)]] + c) % P
            out[tuple_index[(g,) + w]] = (out[tuple_index[(g,) + w]] - c) % P
    return out

# Canonical quotient-induced map tau: W45 -> Wd is defined by equality of
# quotient classes pi(tau(w)) = pi(w).  Since Q_W45 and Q_Wd are the
# verified 45x45 quotient-coordinate isomorphisms, this is exact.
tau_coord = (inv3(Q_Wd) @ Q_W45) % P
T_ambient = (Wd @ tau_coord) % P
E = (T_ambient - W) % P

# The displacement fixes the 35-dimensional actual intersection and therefore
# has rank at most 45-35 = 10.
assert rank3(E) <= 10
assert rank3((E @ I) % P) == 0

# Degree-5 ambient bracket discrepancy.
words5 = list(product((1, 2, 3, 4), repeat=5))
tuple_index = {w: i for i, w in enumerate(words5)}
D = np.vstack([
    np.column_stack([br(E[:, j], g) for j in range(45)])
    for g in range(1, 5)
]) % P

# H-equivariance is checked in the same verified quotient coordinates.
h_eq = all(
    np.array_equal((A @ tau_coord) % P, (tau_coord @ A) % P)
    for A in A_W
)

print('A3-4-10 / CANONICAL QUOTIENT TAU REVALIDATION')
print('dim W45 =', rank3(W))
print('dim Wd =', rank3(Wd))
print('dim I =', rank3(I))
print('rank(Q_W45) =', rank3(Q_W45))
print('rank(Q_Wd) =', rank3(Q_Wd))
print('rank(tau-id) =', rank3(E))
print('nullity(tau-id) on W45 =', 45 - rank3(E))
print('rank((tau-id)|I) =', rank3(E @ I))
print('tau fixes I exactly =', rank3(E @ I) == 0)
print('canonical tau is H-equivariant =', h_eq)
print('canonical bracket obstruction rank =', rank3(D))
print('canonical obstruction shape =', D.shape)

assert h_eq
print('RESULT: canonical quotient-induced tau reconstructed from the already-verified TRUE quotient coordinates.')
print('ALL CANONICAL TAU REVALIDATION CHECKS PASSED')
