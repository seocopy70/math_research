import runpy
import numpy as np
from itertools import product

P = 3
ROOT = 'research/'

# Use the authoritative TRUE-Q4 coordinate system directly from phase2-1.
# This avoids rebuilding a second L4 = (R)_4 + complement coordinate system,
# which was the source of the previous false rank(Q_W45) assertion.
ns1 = runpy.run_path(ROOT + 'phase2_1_invariant_space_verification_2026-09-15.py')
rank3 = ns1['rank3']
apply_linear_map = ns1['apply_linear_map']
bracket = ns1['bracket']
add = ns1['add']
neg = ns1['neg']
mul = ns1['mul']
gens = ns1['gens']
index4 = ns1['index4']
words4 = ns1['words4']
coordinates = ns1['coordinates']
W_words = ns1['basis']
A_W = [np.array(a, dtype=np.int64) % P for a in ns1['action_matrices']]


def vec4(A):
    v = np.zeros(256, dtype=np.int64)
    for w, c in A.items():
        v[index4[w]] = c % P
    return v


def basis_columns(M, target):
    B = np.empty((M.shape[0], 0), dtype=np.int64)
    r = 0
    for j in range(M.shape[1]):
        C = np.column_stack([B, M[:, j]])
        q = rank3(C)
        if q > r:
            B = C
            r = q
            if r == target:
                break
    assert r == target
    return B


def null3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    m, n = A.shape
    R = A.copy()
    piv = []
    r = 0
    for c in range(n):
        q = next((i for i in range(r, m) if R[i, c]), None)
        if q is None:
            continue
        R[[r, q]] = R[[q, r]]
        if R[r, c] == 2:
            R[r] = (2 * R[r]) % P
        for i in range(m):
            if i != r and R[i, c]:
                R[i] = (R[i] - R[i, c] * R[r]) % P
        piv.append(c)
        r += 1
        if r == m:
            break
    out = []
    free = [j for j in range(n) if j not in piv]
    for f in free:
        x = np.zeros(n, dtype=np.int64)
        x[f] = 1
        for rr, c in enumerate(piv):
            x[c] = (-R[rr, f]) % P
        out.append(x)
    return out


W = np.column_stack([vec4(a) for a in W_words]) % P
assert W.shape == (256, 45) and rank3(W) == 45

# Reconstruct Wd from d=[X1^[3],X2] and the same verified Sp4 generators.
d = bracket({(1, 1, 1): 1}, {(2,): 1})
queue = [d]
seen = {tuple(vec4(d).tolist())}
for a in queue:
    for g in gens:
        b = apply_linear_map(a, g)
        key = tuple(vec4(b).tolist())
        if key not in seen:
            seen.add(key)
            queue.append(b)

Wd_raw = np.column_stack([vec4(a) for a in queue])
Wd = basis_columns(Wd_raw, 45)
assert Wd.shape == (256, 45) and rank3(Wd) == 45

# Actual ambient intersection I = W45 intersect Wd.
S = np.column_stack([W, (-Wd) % P]) % P
ker = null3(S)
assert len(ker) == 35
KERNEL = np.column_stack(ker)
I_ambient = (W @ KERNEL[:45, :]) % P
assert rank3(I_ambient) == 35
# phase2-1 coordinates() returns all 60 coordinates in L4=(R)_4+W45;
# the final 45 entries are the TRUE-Q4 coordinates.
I_coord_full = np.column_stack([coordinates(I_ambient[:, j]) for j in range(35)]) % P
assert I_coord_full.shape == (60, 35) and rank3(I_coord_full) == 35
I_coord = I_coord_full[15:, :]
assert I_coord.shape == (45, 35) and rank3(I_coord) == 35

# The authoritative phase2-1 coordinates are coordinates in
# L4 = (R)_4 + W = L4. Hence the final 45 coordinates are Q4 coordinates.
Q_W45 = np.column_stack([coordinates(W[:, j])[15:] for j in range(45)]) % P
Q_Wd = np.column_stack([coordinates(Wd[:, j])[15:] for j in range(45)]) % P
assert rank3(Q_W45) == 45
assert rank3(Q_Wd) == 45


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


# Canonical quotient-induced tau: pi(tau(w)) = pi(w).
tau_coord = (inv3(Q_Wd) @ Q_W45) % P
action_Wd = []
T_ambient = (Wd @ tau_coord) % P
E = (T_ambient - W) % P

# Since tau is the identity on I, its displacement factors through W/I,
# so rank(tau-id) <= 10.
assert rank3(E) <= 10
assert rank3((E @ I_coord) % P) == 0

# Degree-5 ambient bracket discrepancy.
words5 = list(product((1, 2, 3, 4), repeat=5))
tuple_index = {w: i for i, w in enumerate(words5)}

def br(v, g):
    out = np.zeros(1024, dtype=np.int64)
    for j, c in enumerate(v):
        c = int(c) % P
        if c:
            w = words4[j]
            out[tuple_index[w + (g,)]] = (out[tuple_index[w + (g,)] ] + c) % P
            out[tuple_index[(g,) + w]] = (out[tuple_index[(g,) + w]] - c) % P
    return out

D = np.vstack([
    np.column_stack([br(E[:, j], g) for j in range(45)])
    for g in range(1, 5)
]) % P

# H-equivariance in the same authoritative quotient coordinates.
h_eq = all(
    np.array_equal((A @ tau_coord) % P, (tau_coord @ A) % P)
    for A in A_W
)

print('A3-4-10 / CANONICAL QUOTIENT TAU REVALIDATION')
print('dim W45 =', rank3(W))
print('dim Wd =', rank3(Wd))
print('dim I =', rank3(I_coord))
print('rank(Q_W45) =', rank3(Q_W45))
print('rank(Q_Wd) =', rank3(Q_Wd))
print('rank(tau-id) =', rank3(E))
print('nullity(tau-id) on W45 =', 45 - rank3(E))
print('rank((tau-id)|I) =', rank3(E @ I_coord))
print('tau fixes I exactly =', rank3(E @ I_coord) == 0)
print('canonical tau is H-equivariant =', h_eq)
print('canonical bracket obstruction rank =', rank3(D))
print('canonical obstruction shape =', D.shape)

assert h_eq
print('RESULT: canonical quotient-induced tau reconstructed from the authoritative TRUE-Q4 coordinates.')
print('RESULT: the previous ad hoc quotient-coordinate assertion is eliminated.')
print('ALL CANONICAL TAU REVALIDATION CHECKS PASSED')
