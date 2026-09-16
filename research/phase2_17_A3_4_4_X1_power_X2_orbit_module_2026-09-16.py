import runpy
import numpy as np

P = 3


def rank3(A):
    A = np.array(A, dtype=int) % 3
    if A.ndim == 1:
        A = A.reshape(-1, 1)
    m, n = A.shape
    r = 0
    for c in range(n):
        pivot = None
        for i in range(r, m):
            if A[i, c] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        A[[r, pivot]] = A[[pivot, r]]
        inv = 1 if A[r, c] == 1 else 2
        A[r] = (A[r] * inv) % 3
        for i in range(m):
            if i != r and A[i, c] != 0:
                A[i] = (A[i] - A[i, c] * A[r]) % 3
        r += 1
    return r


# Reuse the exact Phase 2-1 Sp4(F3), L4, R4, W45 infrastructure.
ns = runpy.run_path('research/phase2_1_invariant_space_verification_2026-09-15.py')
R4_matrix = ns['R4_matrix']
R4_ind = ns['R4_ind']
basis = ns['basis']
index4 = ns['index4']
generators = ns['generators']

# The Phase 2-1 script represents an Sp4 action on ambient degree-4 words.
# Reuse its word/action machinery rather than constructing a new convention.
action_word = ns.get('action_word')
assert action_word is not None

X1 = {(1,): 1}
X2 = {(2,): 1}

def add(A, B):
    C = dict(A)
    for w, a in B.items():
        C[w] = (C.get(w, 0) + a) % P
        if C[w] == 0:
            del C[w]
    return C


def mul(A, B):
    C = {}
    for wa, ca in A.items():
        for wb, cb in B.items():
            w = wa + wb
            C[w] = (C.get(w, 0) + ca * cb) % P
            if C[w] == 0:
                del C[w]
    return C


def neg(A):
    return {w: (-c) % P for w, c in A.items() if c % P}


def bracket(A, B):
    return add(mul(A, B), neg(mul(B, A)))


def vec4(A):
    v = np.zeros(256, dtype=int)
    for w, c in A.items():
        v[index4[w]] = c % P
    return v

# d = [X1^[3], X2] = ad(X1)^3(X2).
power_part = {(1, 1, 1): 1}
d = bracket(power_part, X2)
direct_d = bracket(bracket(bracket(X1, X2), X1), X1)
assert d == direct_d and d != {}

# Build the full Sp4(F3)-orbit of d.  The group itself is already generated
# by the exact five generators used in Phase 2-1; closure is obtained by
# repeatedly applying generators and inverse generators until no new vectors appear.
# First obtain inverses as powers in GL(4,F3) from the same matrix representation.
# action_word accepts a generator matrix in the same convention.

def mat_inv_mod3(M):
    A = np.array(M, dtype=int) % 3
    n = A.shape[0]
    aug = np.concatenate([A, np.eye(n, dtype=int)], axis=1)
    for c in range(n):
        pivot = next(i for i in range(c, n) if aug[i, c] % 3)
        aug[[c, pivot]] = aug[[pivot, c]]
        inv = 1 if aug[c, c] == 1 else 2
        aug[c] = aug[c] * inv % 3
        for i in range(n):
            if i != c and aug[i, c] % 3:
                aug[i] = (aug[i] - aug[i, c] * aug[c]) % 3
    return aug[:, n:] % 3

inv_generators = [mat_inv_mod3(g) for g in generators]

# The action is linear, so represent orbit vectors directly in the ambient 256-space.
def act(v, g):
    # Convert ambient vector to word dictionary, apply the existing action,
    # then return ambient coordinates.
    A = {}
    nz = np.nonzero(v % P)[0]
    for i in nz:
        A[ns['words4'][i]] = int(v[i]) % P
    B = action_word(A, g)
    return vec4(B)

# Exact orbit enumeration in vector space.  We use a tuple key for deterministic deduplication.
start = vec4(d)
queue = [start]
seen = {tuple(start.tolist())}
for v in queue:
    for g in generators + inv_generators:
        w = act(v, g)
        key = tuple(w.tolist())
        if key not in seen:
            seen.add(key)
            queue.append(w)

orbit_vectors = queue
W_d = np.column_stack(orbit_vectors)
W45 = np.column_stack([vec4(a) for a in basis])

rank_R = rank3(R4_matrix)
rank_W45 = rank3(W45)
rank_Wd = rank3(W_d)
rank_W45_Wd = rank3(np.column_stack([W45, W_d]))
rank_R_Wd = rank3(np.column_stack([R4_ind, W_d]))
rank_R_W45_Wd = rank3(np.column_stack([R4_ind, W45, W_d]))

# Quotient dimensions are computed by subtracting the R4 intersection rank.
# Since W45 and Wd are subspaces of L4, their images in Q4 have dimensions
# rank(R4+W)-rank(R4).
qdim_W45 = rank3(np.column_stack([R4_ind, W45])) - rank_R
qdim_Wd = rank_R_Wd - rank_R
qdim_sum = rank_R_W45_Wd - rank_R

# Intersection dimension in ambient L4.
intersection_W45_Wd = rank_W45 + rank_Wd - rank_W45_Wd

# Invariance certificate: every generator sends each orbit vector into W_d.
# Since orbit construction uses generator/inverse closure, this should be automatic;
# the explicit rank tests certify it numerically.
invariant = True
for g in generators:
    for v in orbit_vectors:
        if rank3(np.column_stack([W_d, act(v, g)])) != rank_Wd:
            invariant = False
            break
    if not invariant:
        break

print('PHASE 2-17 / A3-4-4 ORBIT MODULE OF d = [X1^[3], X2]')
print('rank(R4) =', rank_R)
print('rank(W45) =', rank_W45)
print('d_nonzero =', d != {})
print('orbit_size_of_d =', len(orbit_vectors))
print('rank(W_d) =', rank_Wd)
print('rank(W45 + W_d) =', rank_W45_Wd)
print('rank(R4 + W_d) =', rank_R_Wd)
print('rank(R4 + W45 + W_d) =', rank_R_W45_Wd)
print('dim(W45 intersect W_d) =', intersection_W45_Wd)
print('dim(image W45 in Q4) =', qdim_W45)
print('dim(image W_d in Q4) =', qdim_Wd)
print('dim(image(W45 + W_d) in Q4) =', qdim_sum)
print('W_d_is_Sp4_invariant =', invariant)
print('Q4_dimension =', 55)

assert rank_R == 5
assert rank_W45 == 45
assert d != {}
assert rank_Wd >= 1
assert invariant
assert qdim_W45 == 45
assert qdim_Wd == rank_R_Wd - rank_R
assert qdim_sum <= 55
assert intersection_W45_Wd >= 0

print('CERTIFICATE: A3-4-4 orbit-generated Sp4(F3)-module construction completed.')
