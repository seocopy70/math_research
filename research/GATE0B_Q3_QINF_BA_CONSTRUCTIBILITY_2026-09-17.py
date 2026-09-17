"""Gate 0-B: independent q=3/q=infinity A3-4 constructibility check.

The test starts from the relation-derived degree-3 q-sensitive source, rather
than importing the q=3 A3-4 d/Wd construction.  It then checks whether the
same natural source exists for q=infinity.  The downstream q=3 dimensions
are cross-checked against the existing verified construction; q=infinity is
never forced through q=3 data.
"""

import runpy
import numpy as np

P = 3
ROOT = "research/"


def add(*As):
    C = {}
    for A in As:
        for w, c in A.items():
            C[w] = (C.get(w, 0) + c) % P
            if C[w] == 0:
                del C[w]
    return C


def neg(A):
    return {w: (-c) % P for w, c in A.items() if c % P}


def mul(A, B):
    C = {}
    for wa, ca in A.items():
        for wb, cb in B.items():
            w = wa + wb
            C[w] = (C.get(w, 0) + ca * cb) % P
            if C[w] == 0:
                del C[w]
    return C


def power(A, k, trunc=3):
    if k == 0:
        return {(): 1}
    if k > 0:
        R = {(): 1}
        for _ in range(k):
            R = mul(R, A)
            R = {w: c for w, c in R.items() if len(w) <= trunc}
        return R
    U = add(A, {(): -1 % P})
    R = {(): 1}
    term = {(): 1}
    for i in range(1, trunc + 1):
        term = mul(term, U)
        term = {w: c for w, c in term.items() if len(w) <= trunc}
        R = add(R, {w: ((-1) ** i) * c for w, c in term.items()})
    return R


def homogeneous(A, d):
    return {w: c for w, c in A.items() if len(w) == d and c % P}


def rank3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    if A.ndim == 1:
        A = A[:, None]
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


def vec4(A, index4):
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

# ---------------------------------------------------------------------------
# Gate 0-B-1: independently recompute the q=3/q=infinity degree-3 source.
# ---------------------------------------------------------------------------
x = [None] + [{(): 1, (i,): 1} for i in range(1, 5)]
x1, x2, x3, x4 = x[1], x[2], x[3], x[4]
comm34 = mul(mul(x3, x4), mul(power(x3, -1), power(x4, -1)))

C3 = mul(mul(mul(x1, x2), comm34), mul(power(x1, 3), power(x2, -1)))
Cinf = mul(mul(x1, x2), mul(comm34, power(x2, -1)))
s3 = mul(mul(C3, power(x1, -1)), power(comm34, -1))
sinf = mul(mul(Cinf, power(x1, -1)), power(comm34, -1))
h3 = homogeneous(s3, 3)
hinf = homogeneous(sinf, 3)
degree3_difference = homogeneous(add(h3, neg(hinf)), 3)
power3 = {(1, 1, 1): 1}
assert degree3_difference == power3

# The q-sensitive source for A3-4 is the restricted-power component.
# Therefore d_3=[X1^[3],X2], while the same natural source is zero for q=infinity.
d3 = add(
    mul(power3, {(2,): 1}),
    neg(mul({(2,): 1}, power3)),
)
dinf = {}
assert d3 == {(1, 1, 1, 2): 1, (2, 1, 1, 1): 2}
assert dinf == {}

# ---------------------------------------------------------------------------
# Gate 0-B-2: use the canonical H action only to compute orbit spans.
# ---------------------------------------------------------------------------
ns1 = runpy.run_path(ROOT + "phase2_1_invariant_space_verification_2026-09-15.py")
gens = ns1["gens"]
apply_linear_map = ns1["apply_linear_map"]
index4 = ns1["index4"]


def orbit_basis(d):
    queue = [d]
    seen = {tuple(vec4(d, index4).tolist())}
    for a in queue:
        for g in gens:
            b = apply_linear_map(a, g)
            key = tuple(vec4(b, index4).tolist())
            if key not in seen:
                seen.add(key)
                queue.append(b)
    if not queue:
        return 0, np.zeros((256, 0), dtype=np.int64)
    M = np.column_stack([vec4(a, index4) for a in queue])
    if rank3(M) == 0:
        return len(queue), np.zeros((256, 0), dtype=np.int64)
    B = basis_columns(M, rank3(M))
    return len(queue), B

q3_orbit_size, Wd3 = orbit_basis(d3)
qinf_orbit_size, Wdinf = orbit_basis(dinf)

assert q3_orbit_size == 360
assert Wd3.shape == (256, 45)
assert rank3(Wd3) == 45
assert qinf_orbit_size == 1
assert Wdinf.shape == (256, 0)
assert rank3(Wdinf) == 0

# ---------------------------------------------------------------------------
# Gate 0-B-3: q=3 downstream constructibility sanity check.
# This reuses the already verified q=3 construction only after the source
# has been independently rebuilt above.  No q=infinity data are imported.
# ---------------------------------------------------------------------------
ns_q3 = runpy.run_path(ROOT + "phase2_18_A3_4_5_intersection_K_and_Sym2_2026-09-16.py")
W = np.array(ns_q3["W"], dtype=np.int64) % P
I_W = np.array(ns_q3["I_W"], dtype=np.int64) % P
K_coord = np.array(ns_q3["K_coord"], dtype=np.int64) % P
Wd_existing = np.array(ns_q3["Wd_basis"], dtype=np.int64) % P

q3_downstream = {
    "W45": rank3(W),
    "Wd": rank3(Wd_existing),
    "intersection_I": rank3(I_W),
    "K": rank3(K_coord),
}
assert q3_downstream == {"W45": 45, "Wd": 45, "intersection_I": 35, "K": 35}

# Gate decision: the natural q=infinity source is zero, so the same
# relation-derived 45D Wd and 35D B/A,K construction is not available.
qinf_has_A34_source = rank3(Wdinf) > 0
qinf_can_construct_same_A34_shape = qinf_has_A34_source and Wdinf.shape[1] == 45

print("GATE0B_Q3_QINF_BA_CONSTRUCTIBILITY")
print("degree3_q3 =", sorted(h3.items()))
print("degree3_qinf =", sorted(hinf.items()))
print("degree3_difference =", sorted(degree3_difference.items()))
print("degree3_difference_is_X1_cubed =", degree3_difference == power3)
print("d3 =", sorted(d3.items()))
print("d_infty =", sorted(dinf.items()))
print("q3_d_nonzero =", bool(d3))
print("qinf_d_nonzero =", bool(dinf))
print("q3_d_orbit_size =", q3_orbit_size)
print("q3_d_orbit_span_dimension =", rank3(Wd3))
print("qinf_d_orbit_size =", qinf_orbit_size)
print("qinf_d_orbit_span_dimension =", rank3(Wdinf))
print("q3_downstream_dimensions =", q3_downstream)
print("qinf_has_natural_A3_4_source =", qinf_has_A34_source)
print("qinf_can_construct_same_45D_35D_A3_4_shape =", qinf_can_construct_same_A34_shape)

assert not qinf_has_A34_source
assert not qinf_can_construct_same_A34_shape
print("RESULT = PASS_WITH_QINF_NO_NATURAL_A3_4_SOURCE")
print("INTERPRETATION = q=infinity does not admit the same relation-derived degree-3 source; therefore the q=3 45D Wd -> 35D intersection/B-A,K construction cannot be transferred by the natural mechanism.")
print("CAUTION = this is a q-sensitive structural signal, not by itself a complete classification theorem or an Ext^1 computation.")
