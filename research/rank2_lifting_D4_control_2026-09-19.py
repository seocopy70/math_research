#!/usr/bin/env python3
"""
Rank-2 n=4 lifting/relator-preservation control.

Frozen convention:
  p = 3
  G_q^(2) = <x1,x2 | r_q = x1^q [x1,x2]>
  D_4 is the standard p-Zassenhaus term, and for the free pro-3 group
  F the quotient F/D_4 is tested through the Magnus expansion modulo
  augmentation degree >= 4.

The weak-data control does NOT construct the abstract quotient G_q/D_4.
It tests prescribed free-group lifts of selected SL_2(F_3) linear maps.

At degree <= 3, relator preservation modulo the normal closure is checked
by:
  (i) degree-2 class must agree (the SL_2 determinant condition fixes it);
  (ii) the degree-3 difference must lie in span{[X1,R2],[X2,R2]}.
For q=3 the degree-3 p-power source X1^[3] is retained in r_3.
For q=infinity it is absent.

This script is a control experiment, not a rank-4 theorem.
"""
from itertools import product
import json

P = 3
NGEN = 2
MAX_DEG = 3

def add(a, b):
    c = dict(a)
    for k, v in b.items():
        c[k] = (c.get(k, 0) + v) % P
        if c[k] == 0:
            del c[k]
    return c

def scale(a, s):
    s %= P
    return {k: (v * s) % P for k, v in a.items() if (v * s) % P}

def mul(a, b):
    c = {}
    for wa, va in a.items():
        for wb, vb in b.items():
            w = wa + wb
            if len(w) <= MAX_DEG:
                c[w] = (c.get(w, 0) + va * vb) % P
    return {k: v for k, v in c.items() if v}

ONE = {(): 1}
X = [{(i,): 1} for i in range(NGEN)]

def inv_group_generator(i):
    x = X[i]
    # (1+X)^(-1) = 1-X+X^2-X^3 mod degree 4
    return add(add(add(ONE, scale(x, -1)), mul(x, x)),
               scale(mul(mul(x, x), x), -1))

GEN = [add(ONE, X[i]) for i in range(NGEN)]
GINV = [inv_group_generator(i) for i in range(NGEN)]

def inv_word(w):
    return [(i, -s) for i, s in reversed(w)]

def eval_word(w):
    z = ONE
    for i, s in w:
        z = mul(z, GEN[i] if s == 1 else GINV[i])
    return z

def substitute_word(word, lift):
    out = []
    for i, s in word:
        base = lift[i]
        out.extend(base if s == 1 else inv_word(base))
    return out

COMM = [(0, 1), (1, 1), (0, -1), (1, -1)]
R3 = [(0, 1)] * 3 + COMM
RINF = COMM

def relator_image(lift, q3):
    return eval_word(substitute_word(R3 if q3 else RINF, lift))

def degree_vec(poly, degree):
    words = list(product(range(NGEN), repeat=degree))
    return [poly.get(w, 0) % P for w in words]

def rank_mod3(rows):
    if not rows:
        return 0
    A = [list(map(lambda x: x % P, row)) for row in rows]
    m, n = len(A), len(A[0])
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, m) if A[i][col] % P), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        inv = pow(A[rank][col], -1, P)
        A[rank] = [(x * inv) % P for x in A[rank]]
        for i in range(m):
            if i != rank and A[i][col] % P:
                f = A[i][col]
                A[i] = [(A[i][j] - f * A[rank][j]) % P for j in range(n)]
        rank += 1
        if rank == m:
            break
    return rank

def in_span_mod3(columns, v):
    if not columns:
        return all(x % P == 0 for x in v)
    m = len(v)
    base = [[columns[j][i] for j in range(len(columns))] + [v[i]]
            for i in range(m)]
    return rank_mod3(base) == rank_mod3([row[:-1] for row in base])

# Degree-2 baseline relation and its degree-3 conjugation directions.
R2 = eval_word(RINF)
R2 = {w: c for w, c in R2.items() if len(w) == 2}

def bracket_x_R2(i):
    left = {(i,): 1}
    return add(mul(left, R2), scale(mul(R2, left), -1))

CONJ_DIRECTIONS = [
    degree_vec(bracket_x_R2(i), 3) for i in range(NGEN)
]

# Selected lifts, with column convention e_j -> sum_i g_ij e_i.
LIFTS = {
    "identity": [[(0, 1)], [(1, 1)]],                 # I
    "line_stabilizer_unipotent": [[(0, 1)], [(0, 1), (1, 1)]],  # [[1,1],[0,1]]
    "line_stabilizer_minus_identity": [[(0, -1)], [(1, -1)]],   # -I
    "line_moving_transvection": [[(0, 1), (1, 1)], [(1, 1)]],   # [[1,0],[1,1]]
}

EXPECTED = {
    "identity": {"moves_line": False, "q3_admissible": True, "qinf_admissible": True},
    "line_stabilizer_unipotent": {"moves_line": False, "q3_admissible": True, "qinf_admissible": True},
    "line_stabilizer_minus_identity": {"moves_line": False, "q3_admissible": False, "qinf_admissible": True},
    "line_moving_transvection": {"moves_line": True, "q3_admissible": False, "qinf_admissible": True},
}

def analyze(name, lift, q3):
    base = R3 if q3 else RINF
    base_img = eval_word(base)
    img = relator_image(lift, q3)

    d2 = [(a - b) % P for a, b in zip(degree_vec(img, 2), degree_vec(base_img, 2))]
    d3 = [(a - b) % P for a, b in zip(degree_vec(img, 3), degree_vec(base_img, 3))]

    # Degree-2 equality is mandatory because the relator's initial class is nonzero.
    d2_equal = all(x == 0 for x in d2)

    # Once degree 2 agrees, normal-closure conjugation changes degree 3
    # exactly by span{[X1,R2],[X2,R2]}.
    admissible = d2_equal and in_span_mod3(CONJ_DIRECTIONS, d3)
    return {
        "name": name,
        "q": 3 if q3 else "infinity",
        "degree2_equal": d2_equal,
        "degree3_difference": d3,
        "admissible": admissible,
    }

def main():
    # Sanity: R2 is nonzero and conjugation directions are independent.
    assert any(R2.values())
    assert rank_mod3(CONJ_DIRECTIONS) == 2

    results = []
    for name, lift in LIFTS.items():
        q3r = analyze(name, lift, True)
        qinfr = analyze(name, lift, False)
        results.extend([q3r, qinfr])

        exp = EXPECTED[name]
        assert q3r["admissible"] == exp["q3_admissible"], (name, q3r)
        assert qinfr["admissible"] == exp["qinf_admissible"], (name, qinfr)

    # The q=3 admissible representative set among the tested symmetries
    # is strictly smaller than the q=infinity set.
    q3_ok = [r["name"] for r in results if r["q"] == 3 and r["admissible"]]
    qinf_ok = [r["name"] for r in results if r["q"] == "infinity" and r["admissible"]]
    assert q3_ok == ["identity", "line_stabilizer_unipotent"]
    assert qinf_ok == list(LIFTS.keys())

    payload = {
        "status": "PASS",
        "filtration": "D4 standard p-Zassenhaus; Magnus modulo degree >=4",
        "field": "F3",
        "ambient_linear_group": "SL2(F3)",
        "tested_lifts": list(LIFTS.keys()),
        "conjugation_span_rank_degree3": rank_mod3(CONJ_DIRECTIONS),
        "results": results,
        "scope": [
            "rank-2 control only",
            "selected representative lifts only",
            "not evidence for a rank-4 theorem",
            "does not use the abstract finite quotient G/D4 as input",
        ],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
