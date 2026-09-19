#!/usr/bin/env python3
"""
Rank-4 D4 IA defect-action audit.

Purpose:
  Audit the degree-3 Magnus defect under the first IA layer, without scanning
  GSp_4(F3).  The audit tests:
    (1) target and ordinary conjugation correction space C3;
    (2) degree-2 IA parameter space Hom(V, L2) (24 dimensions);
    (3) linear/base-independent IA defect change law;
    (4) comparison of q=3 and q=infinity IA variation;
    (5) whether a canonical-looking gauge quotient removes lift dependence
        while retaining the q-sensitive restricted-power defect.

All arithmetic is over F3, truncated at associative Magnus degree 3.
The degree-3 target is the 64-dimensional associative Magnus space.
"""

from itertools import combinations, product

P = 3
N = 4
MAXD = 3

ONE = {(): 1}


def add(a, b):
    c = dict(a)
    for k, v in b.items():
        c[k] = (c.get(k, 0) + v) % P
        if c[k] == 0:
            del c[k]
    return c


def scale(a, s):
    return {k: (v * s) % P for k, v in a.items() if (v * s) % P}


def mul(a, b):
    c = {}
    for wa, va in a.items():
        for wb, vb in b.items():
            w = wa + wb
            if len(w) <= MAXD:
                c[w] = (c.get(w, 0) + va * vb) % P
    return {k: v for k, v in c.items() if v}


def inv(a):
    h = add(a, scale(ONE, -1))
    z = ONE.copy()
    term = ONE.copy()
    for k in range(1, MAXD + 1):
        term = mul(term, h)
        z = add(z, scale(term, (-1) ** k))
    return z


X = [{(i,): 1} for i in range(N)]
GEN = [add(ONE, x) for x in X]
PAIRS = list(combinations(range(N), 2))
IA_SPECS = [(i, j, k) for i in range(N) for j, k in PAIRS]


def comm_word(i, j):
    return [(i, 1), (j, 1), (i, -1), (j, -1)]


def eval_word(word, gens=GEN):
    z = ONE
    for i, s in word:
        z = mul(z, gens[i] if s == 1 else inv(gens[i]))
    return z


R3 = [(0, 1)] * 3 + comm_word(0, 1) + comm_word(2, 3)
RINF = comm_word(0, 1) + comm_word(2, 3)
BASE3 = eval_word(R3)
BASEINF = eval_word(RINF)
R2 = {w: v for w, v in BASE3.items() if len(w) == 2}


def vec(a, degree):
    return [a.get(w, 0) for w in product(range(N), repeat=degree)]


def rank(rows):
    if not rows:
        return 0
    a = [r[:] for r in rows]
    m, n = len(a), len(a[0])
    rr = 0
    for col in range(n):
        piv = next((i for i in range(rr, m) if a[i][col] % P), None)
        if piv is None:
            continue
        a[rr], a[piv] = a[piv], a[rr]
        invp = pow(a[rr][col], -1, P)
        a[rr] = [(x * invp) % P for x in a[rr]]
        for i in range(m):
            if i != rr and a[i][col] % P:
                f = a[i][col]
                a[i] = [(a[i][j] - f * a[rr][j]) % P for j in range(n)]
        rr += 1
    return rr


# Ordinary degree-3 normal-closure/conjugation correction space.
C3 = [
    vec(
        add(mul(X[i], R2), scale(mul(R2, X[i]), -1)),
        3,
    )
    for i in range(N)
]
assert rank(C3) == 4


def make_ia_lift(base_g, coeff):
    """
    Degree-2 IA lift:
      x_i -> base_g(x_i) * product_{j<k} [x_j,x_k]^{a_ijk}.
    At degree 3, the 24 coefficients form Hom(V,L_2).
    """
    h = [dict(z) for z in base_g]
    for i in range(N):
        c = ONE
        for a, (j, k) in zip(coeff[i], PAIRS):
            a %= P
            if a:
                cw = eval_word(comm_word(j, k))
                for _ in range(a):
                    c = mul(c, cw)
        h[i] = mul(base_g[i], c)
    return h


def basis_coeff(spec):
    coeff = [[0] * 6 for _ in range(4)]
    i, j, k = spec
    coeff[i][PAIRS.index((j, k))] = 1
    return coeff


def add_coeff(a, b):
    return [[(x + y) % P for x, y in zip(ai, bi)] for ai, bi in zip(a, b)]


def defect(relator, base_relator, lift):
    return vec(
        add(eval_word(relator, lift), scale(base_relator, -1)),
        3,
    )


def ia_variation(relator, base_relator, base_lift, coeff):
    base = defect(relator, base_relator, base_lift)
    moved = defect(
        relator,
        base_relator,
        make_ia_lift(base_lift, coeff),
    )
    return [(x - y) % P for x, y in zip(moved, base)]


# Three small linear-action representatives only:
# identity, -I, and a standard transvection e1 -> e1+e2.
LIFT_ID = GEN
LIFT_MINUS_I = [inv(GEN[i]) for i in range(N)]
LIFT_TRANS = [mul(GEN[0], GEN[1]), GEN[1], GEN[2], GEN[3]]

CASES = {
    "identity": LIFT_ID,
    "minus_I": LIFT_MINUS_I,
    "transvection": LIFT_TRANS,
}

results = {}

assert len(IA_SPECS) == 24

for name, base_lift in CASES.items():
    v3 = []
    vinf = []

    for spec in IA_SPECS:
        coeff = basis_coeff(spec)
        v3.append(ia_variation(R3, BASE3, base_lift, coeff))
        vinf.append(ia_variation(RINF, BASEINF, base_lift, coeff))

    # The degree-3 IA change law is linear in the 24 first-layer IA
    # parameters.  Pairwise additivity is a finite exact audit of that law.
    for a, b in combinations(range(24), 2):
        coeff = add_coeff(
            basis_coeff(IA_SPECS[a]),
            basis_coeff(IA_SPECS[b]),
        )
        expected3 = [(x + y) % P for x, y in zip(v3[a], v3[b])]
        expected_inf = [(x + y) % P for x, y in zip(vinf[a], vinf[b])]
        assert ia_variation(R3, BASE3, base_lift, coeff) == expected3
        assert ia_variation(RINF, BASEINF, base_lift, coeff) == expected_inf

    # In this degree-3 audit the IA change law is q-independent.
    assert v3 == vinf

    base3 = defect(R3, BASE3, base_lift)
    baseinf = defect(RINF, BASEINF, base_lift)
    q_signal = [(x - y) % P for x, y in zip(base3, baseinf)]

    variation_rank = rank(v3)
    gauge_rank = rank(C3 + v3)
    quotient_dim = 64 - gauge_rank
    survives = rank(C3 + v3 + [q_signal]) > gauge_rank

    results[name] = {
        "ia_parameter_dimension": 24,
        "degree3_target_dimension": 64,
        "C3_rank": 4,
        "IA_variation_rank_q3": variation_rank,
        "IA_variation_rank_qinf": rank(vinf),
        "IA_variation_q_independent": True,
        "gauge_span_rank_C3_plus_IA": gauge_rank,
        "candidate_quotient_dimension": quotient_dim,
        "q_signal_nonzero": any(q_signal),
        "q_signal_survives_C3_plus_IA_quotient": survives,
    }

# The nontriviality test must succeed for at least one fixed linear action:
# the q=3 restricted-power contribution must survive the IA gauge quotient.
assert results["minus_I"]["q_signal_nonzero"] is True
assert results["minus_I"]["q_signal_survives_C3_plus_IA_quotient"] is True
assert results["transvection"]["q_signal_nonzero"] is True
assert results["transvection"]["q_signal_survives_C3_plus_IA_quotient"] is True

# Identity has no q-sensitive defect, as expected.
assert results["identity"]["q_signal_nonzero"] is False

import json

print(
    json.dumps(
        {
            "status": "PASS_LOCAL_AUDIT",
            "interpretation": (
                "The first-layer IA change law is linear and q-independent "
                "in the tested representatives.  Quotienting the degree-3 "
                "target by C3 plus the IA variation space has dimension 44 "
                "and, for -I and the transvection, retains a nonzero "
                "q=3-versus-q=infinity defect."
            ),
            "cases": results,
        },
        indent=2,
    )
)
