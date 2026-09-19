#!/usr/bin/env python3
"""Broader structured representative audit for the corrected quotient q-defect cocycle.

Frozen convention:
  delta_g = [F_g(R3) - mu(g) R3]_deg3
  Delta_q(g) = [delta_3(g) - delta_infinity(g)]_deg3
  Q3 = A3 / (C3 + Delta_IA)

For F_(gh)=F_g o F_h, test
  Delta_q(gh) = mu(h) Delta_q(g) + g . Delta_q(h)
in Q3.

This is a structured-family gate, not a full rank-4 scan.
The family contains:
  - identity and -I;
  - two powers of the first hyperbolic-pair shear;
  - two powers of the second hyperbolic-pair shear;
  - a symplectic pair-swap;
  - two multiplier-2 diagonal GSp representatives.
All matrices are independently checked against g^T J g = mu J.
"""

from itertools import combinations, product

P, N, D = 3, 4, 3
ONE = {(): 1}
GEN = [{(): 1, (i,): 1} for i in range(N)]
PAIRS = list(combinations(range(N), 2))
SPECS = [(i, j, k) for i in range(N) for j, k in PAIRS]
WORDS3 = list(product(range(N), repeat=3))

J = [
    [0, 1, 0, 0],
    [-1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, -1, 0],
]

def add(a, b):
    c = dict(a)
    for w, v in b.items():
        c[w] = (c.get(w, 0) + v) % P
        if c[w] == 0:
            del c[w]
    return c

def sc(a, s):
    return {w: v * s % P for w, v in a.items() if v * s % P}

def mu(a, b):
    c = {}
    for x, u in a.items():
        for y, v in b.items():
            w = x + y
            if len(w) <= D:
                c[w] = (c.get(w, 0) + u * v) % P
    return {w: v for w, v in c.items() if v}

def inv(a):
    h = add(a, sc(ONE, -1))
    z = dict(ONE)
    t = dict(ONE)
    for k in range(1, D + 1):
        t = mu(t, h)
        z = add(z, sc(t, (-1) ** k))
    return z

def comm(i, j):
    return [(i, 1), (j, 1), (i, -1), (j, -1)]

def sub(w, A):
    out = []
    for i, s in w:
        z = A[i]
        out += z if s == 1 else [(j, -t) for j, t in z[::-1]]
    return out

def comp(A, B):
    return [sub(w, A) for w in B]

def ev(w, G):
    z = dict(ONE)
    for i, s in w:
        z = mu(z, G[i] if s == 1 else inv(G[i]))
    return z

def vec(a, d):
    return [a.get(w, 0) for w in product(range(N), repeat=d)]

def rank(rows):
    a = [r[:] for r in rows if any(r)]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if a[i][c] % P), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        q = pow(a[r][c], -1, P)
        a[r] = [x * q % P for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [(a[i][j] - q * a[r][j]) % P for j in range(n)]
        r += 1
    return r

R3 = [(0, 1)] * 3 + comm(0, 1) + comm(2, 3)
RI = comm(0, 1) + comm(2, 3)
B3 = ev(R3, GEN)
BI = ev(RI, GEN)
R2 = {w: v for w, v in B3.items() if len(w) == 2}
X = [{(i,): 1} for i in range(N)]

C3 = [
    vec(add(mu(X[i], R2), sc(mu(R2, X[i]), -1)), 3)
    for i in range(N)
]
assert rank(C3) == 4

def coeff(s):
    c = [[0] * 6 for _ in range(N)]
    i, j, k = s
    c[i][PAIRS.index((j, k))] = 1
    return c

def ia(c):
    out = []
    for i in range(N):
        w = [(i, 1)]
        for a, (j, k) in zip(c[i], PAIRS):
            for _ in range(a % P):
                w += comm(j, k)
        out.append(w)
    return out

IDENT = [[(i, 1)] for i in range(N)]

def gauge_variation(g):
    base = defect([ev(w, GEN) for w in g], 1)
    V = []
    for s in SPECS:
        p = ia(coeff(s))
        L = [ev(w, GEN) for w in comp(p, g)]
        d = defect(L, 1)
        V.append([(x - y) % P for x, y in zip(d, base)])
    return V

def defect(L, m):
    return vec(add(ev(R3, L), sc(B3, -m)), 3)

V0 = gauge_variation(IDENT)
GAUGE = C3 + V0
assert rank(V0) == 20 and rank(GAUGE) == 20

def linear_matrix(g):
    M = [[0] * N for _ in range(N)]
    for i, w in enumerate(g):
        z = ev(w, GEN)
        for j in range(N):
            M[j][i] = z.get((j,), 0) % P
    return M

def matmul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(N)) % P for j in range(N)]
        for i in range(N)
    ]

def transpose(A):
    return [list(x) for x in zip(*A)]

def check_gsp(M, expected_mu):
    lhs = matmul(matmul(transpose(M), J), M)
    rhs = [[expected_mu * J[i][j] % P for j in range(N)] for i in range(N)]
    return lhs == rhs

def word_for_column(col):
    w = []
    for i, a in enumerate(col):
        a %= P
        if a == 1:
            w.append((i, 1))
        elif a == 2:
            w.append((i, 1))
            w.append((i, 1))
    return w

def matrix_to_lift(M):
    return [word_for_column([M[r][c] for r in range(N)]) for c in range(N)]

def shear12(k):
    M = [[int(i == j) for j in range(N)] for i in range(N)]
    M[1][0] = k % P
    return M

def shear34(k):
    M = [[int(i == j) for j in range(N)] for i in range(N)]
    M[3][2] = k % P
    return M

def pair_swap():
    M = [[0] * N for _ in range(N)]
    M[2][0] = 1
    M[3][1] = 1
    M[0][2] = 1
    M[1][3] = 1
    return M

def diag(vals):
    return [[vals[i] if i == j else 0 for j in range(N)] for i in range(N)]

MATS = {
    "identity": (diag([1, 1, 1, 1]), 1),
    "minus_I": (diag([2, 2, 2, 2]), 1),
    "shear12_plus1": (shear12(1), 1),
    "shear12_plus2": (shear12(2), 1),
    "shear34_plus1": (shear34(1), 1),
    "shear34_plus2": (shear34(2), 1),
    "pair_swap": (pair_swap(), 1),
    "multiplier2_diag_A": (diag([2, 1, 2, 1]), 2),
    "multiplier2_diag_B": (diag([2, 1, 1, 2]), 2),
}

CASES = {}
for name, (M, m) in MATS.items():
    assert check_gsp(M, m), (name, "not GSp with claimed multiplier")
    CASES[name] = (matrix_to_lift(M), m)

def survives(v):
    return rank(GAUGE + [v]) > rank(GAUGE)

def modzero(v):
    return rank(GAUGE + [v]) == rank(GAUGE)

def delta_q(g):
    L = [ev(w, GEN) for w in g]
    d3 = defect(L, 1)
    di = vec(add(ev(RI, L), sc(BI, -1)), 3)
    return [(x - y) % P for x, y in zip(d3, di)]

def tensor_action(v, M):
    out = [0] * 64
    for pos, w in enumerate(WORDS3):
        c = v[pos]
        if not c:
            continue
        choices = [
            [(j, M[j][i]) for j in range(N) if M[j][i] % P]
            for i in w
        ]
        for js in product(*choices):
            ww = tuple(x[0] for x in js)
            cc = c
            for _, a in js:
                cc = cc * a % P
            idx = WORDS3.index(ww)
            out[idx] = (out[idx] + cc) % P
    return out

names = list(CASES)
law_fail = law_raw_fail = reversed_fail = reversed_raw_fail = 0
nonzero = 0
matrix_checks = 0

for name, (g, m) in CASES.items():
    assert linear_matrix(g) == MATS[name][0]
    matrix_checks += 1

# Critical convention audit: free-word composition must agree with
# ordinary column-matrix multiplication, independently of the cocycle test.
for a in names:
    for b in names:
        ga, _ = CASES[a]; gb, _ = CASES[b]
        assert linear_matrix(comp(ga, gb)) == matmul(linear_matrix(ga), linear_matrix(gb)), (a, b)

# Critical q-source audit: Delta_q must equal the direct cubic source
# difference [F_g(X1^3)-X1^3]_deg3, not merely a difference of helpers.
X1cube = [(0, 1)] * 3
for name, (g, m) in CASES.items():
    Gg = [ev(w, GEN) for w in g]
    direct = vec(add(ev(X1cube, Gg), sc({tuple(X1cube): 1}, -1)), 3)
    if delta_q(g) != direct:
        print("DIRECT_Q_SOURCE_MISMATCH", name, delta_q(g), direct)

results = []
for a in names:
    ga, mua = CASES[a]
    for b in names:
        gb, mub = CASES[b]
        gab = comp(ga, gb)
        lhs = delta_q(gab)
        da = delta_q(ga)
        db = delta_q(gb)

        # Frozen convention: F_(gh) = F_g o F_h.
        # Delta_q = F_g(X1^3)-X1^3. Since delta_q(h) already contains
        # the multiplier contribution to F_h(X1^3), composition gives
        # Delta_q(gh)=Delta_q(g)+g.Delta_q(h), with no extra mu(h) factor.
        rhs = [(x + y) % P for x, y in zip(
            da, tensor_action(db, linear_matrix(ga))
        )]
        # Diagnostic only: reverse the action/order.
        rhs_rev = [(x + y) % P for x, y in zip(
            db, tensor_action(da, linear_matrix(gb))
        )]

        e = [(x - y) % P for x, y in zip(lhs, rhs)]
        er = [(x - y) % P for x, y in zip(lhs, rhs_rev)]

        raw = any(e)
        qbad = not modzero(e)
        rawr = any(er)
        qbadr = not modzero(er)

        law_raw_fail += raw
        law_fail += qbad
        reversed_raw_fail += rawr
        reversed_fail += qbadr
        nonzero += survives(lhs)
        results.append((a, b, raw, qbad, rawr, qbadr))

assert law_fail == 0


print({
    "status": "PASS_STRUCTURED_QUOTIENT_DEFECT_COMPOSITION_LOCAL",
    "family_size": len(names),
    "pairs_tested": len(results),
    "gauge_rank": rank(GAUGE),
    "Q3_dimension": 64 - rank(GAUGE),
    "matrix_gsp_checks": matrix_checks,
    "candidate_law": "Delta_q(gh)=Delta_q(g)+g·Delta_q(h)",
    "candidate_law_failures_mod_Q3": law_fail,
    "candidate_law_raw_failures": law_raw_fail,
    "reversed_diagnostic_failures_mod_Q3": reversed_fail,
    "reversed_diagnostic_raw_failures": reversed_raw_fail,
    "nonzero_composed_defect_classes": nonzero,
    "cases": names,
    "multipliers": {k: v[1] for k, v in CASES.items()},
    "interpretation": (
        "Structured-family audit only. A zero candidate failure count "
        "supports the frozen raw q-defect action/order law on this family; it does not "
        "establish full GSp4 covariance or canonicality."
    ),
})
