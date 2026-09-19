#!/usr/bin/env python3
"""A-1 control audit for the structured Delta_q coboundary claim.

Frozen object:
  Delta_q(g) = [F_g(X1^3) - X1^3]_deg3

Pre-registered tests:
  T1: direct equality Delta_q(g) = g·X1^3 - X1^3.
  T2: q-blind control words/tensor obey the same degree-3 identity.
  T3: for every ordered representative pair, compare the composed
      Delta_q(gh) vector directly with (gh)·X1^3 - X1^3.

This is a control experiment, not a broader rank-4 scan.
Setup assertions are allowed; mathematical test outcomes are reported,
not asserted, so a non-coboundary result cannot disappear via an exception.
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

# Algebraic sanity check: the degree-3 q-defect is the coboundary of x=X1^3.
# Since F_g(X1)=g.X1 + terms of degree >=2, only (g.X1)^3 contributes
# to degree 3, so Delta_q(g)=g.x-x. This is checked independently here.
x = [1 if w == (0,0,0) else 0 for w in WORDS3]
T1_FAILURES = {}
for name, (g, m) in CASES.items():
    M = linear_matrix(g)
    expected = [(a - b) % P for a, b in zip(tensor_action(x, M), x)]
    actual = delta_q(g)
    if actual != expected:
        T1_FAILURES[name] = {
            "max_coordinate_difference": max((a - b) % P for a, b in zip(actual, expected)),
            "actual_nonzero": sum(a % P != 0 for a in actual),
            "expected_nonzero": sum(a % P != 0 for a in expected),
        }
T1_pass = not T1_FAILURES

# T2 controls: for any fixed homogeneous degree-3 associative word w,
# Delta_w(g)=[F_g(w)-w]_3 must equal g.w-w. These controls are q-blind.
def word_vec(w):
    return [1 if u == tuple(w) else 0 for u in WORDS3]

def word_image(w, L):
    # F_g acts on each generator x_i by the algebra element L[i].
    # A tuple such as (0,1,0) denotes the associative word X1 X2 X1.
    return ev([(i, 1) for i in w], L)

def delta_word(w, g):
    L = [ev(v, GEN) for v in g]
    fg = vec(word_image(w, L), 3)
    return [(a - b) % P for a, b in zip(fg, word_vec(w))]

CONTROL_WORDS = {
    "X1^3": (0, 0, 0),
    "X2^3": (1, 1, 1),
    "X1X2X1": (0, 1, 0),
}
CONTROL_T2_FAILURES = {}
CONTROL_T2_DIAGNOSTICS = {}
for label, w in CONTROL_WORDS.items():
    failures = 0
    first_failure = None
    for name, (g, _) in CASES.items():
        M = linear_matrix(g)
        expected = [(a - b) % P for a, b in zip(
            tensor_action(word_vec(w), M), word_vec(w)
        )]
        actual = delta_word(w, g)
        if actual != expected:
            failures += 1
            if first_failure is None:
                first_failure = {
                    "case": name,
                    "actual": actual,
                    "expected": expected,
                }
    CONTROL_T2_FAILURES[label] = failures
    CONTROL_T2_DIAGNOSTICS[label] = first_failure

ARBITRARY_TENSOR = [0] * 64
for w, c in [((0,0,0), 1), ((1,1,1), 2), ((0,1,0), 1)]:
    ARBITRARY_TENSOR[WORDS3.index(w)] = c

def delta_tensor(v, g):
    L = [ev(w, GEN) for w in g]
    out = [0] * 64
    for w, c in zip(WORDS3, v):
        if c:
            ew = vec(word_image(w, L), 3)
            for i, a in enumerate(ew):
                out[i] = (out[i] + c * a) % P
    return [(a - b) % P for a, b in zip(out, v)]

CONTROL_T2_FAILURES["arbitrary_tensor"] = 0
CONTROL_T2_DIAGNOSTICS["arbitrary_tensor"] = None
for name, (g, _) in CASES.items():
    M = linear_matrix(g)
    expected = [(a - b) % P for a, b in zip(
        tensor_action(ARBITRARY_TENSOR, M), ARBITRARY_TENSOR
    )]
    actual = delta_tensor(ARBITRARY_TENSOR, g)
    if actual != expected:
        CONTROL_T2_FAILURES["arbitrary_tensor"] += 1
        if CONTROL_T2_DIAGNOSTICS["arbitrary_tensor"] is None:
            CONTROL_T2_DIAGNOSTICS["arbitrary_tensor"] = {
                "case": name,
                "actual": actual,
                "expected": expected,
            }

T2_pass = not any(CONTROL_T2_FAILURES.values())


names = list(CASES)
law_fail = law_raw_fail = reversed_fail = reversed_raw_fail = 0
nonzero = 0
expected_nonzero = 0
t3_direct_failures = 0
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
        x_image = tensor_action(x, linear_matrix(gab))
        expected_class = [(u - v) % P for u, v in zip(x_image, x)]
        expected_nonzero += survives(expected_class)
        direct_t3_fail = lhs != expected_class
        if direct_t3_fail:
            t3_direct_failures += 1
        results.append((a, b, raw, qbad, rawr, qbadr, direct_t3_fail))

T3_pass = (t3_direct_failures == 0 and nonzero == expected_nonzero)
if not T1_pass:
    status = "PASS-NONTRIVIAL"
elif not T2_pass:
    status = "IMPLEMENTATION-FAILURE"
elif not T3_pass:
    status = "T3-FAIL"
else:
    status = "PASS-TRIVIAL"

print({
    "status": status,
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
    "T1_coboundary_failures": T1_FAILURES,
    "T1_pass": T1_pass,
    "T2_control_failures": CONTROL_T2_FAILURES,
    "T2_diagnostics_first_failure": CONTROL_T2_DIAGNOSTICS,
    "T2_pass": T2_pass,
    "T3_expected_nonzero_composed_classes": expected_nonzero,
    "T3_nonzero_count_matches": nonzero == expected_nonzero,
    "T3_direct_vector_failures": t3_direct_failures,
    "T3_pass": T3_pass,
    "cases": names,
    "multipliers": {k: v[1] for k, v in CASES.items()},
    "interpretation": (
        "A-1 control only. PASS-TRIVIAL closes this Delta_q track as a coboundary; "
        "PASS-NONTRIVIAL requires isolating the non-coboundary component; "
        "IMPLEMENTATION-FAILURE means the q-blind controls failed. "
        "This does not establish full GSp4 covariance or canonicality."
    ),
})
