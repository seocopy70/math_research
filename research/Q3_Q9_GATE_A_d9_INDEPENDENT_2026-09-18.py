"""Q3/Q9 Gate A — independent exact truncated-Magnus derivation of d9.

This verifier is intentionally self-contained. It does not import any q=3
research script or downstream N/J code.

Conventions:
- F_3 arithmetic.
- Magnus substitution x_i = 1 + X_i.
- truncation by total degree <= 3.
- group commutator [a,b] = a b a^{-1} b^{-1}.
- q=9 control is x1^9.
- baseline q=infinity omits x1^q.

The Gate-A target is derived, not selected:
  in_3(s9), in_3(sinf), Delta_3(9), d9.
"""

from pathlib import Path
import json

P = 3
TRUNC = 3


def add(*As):
    out = {}
    for A in As:
        for w, c in A.items():
            c = (out.get(w, 0) + c) % P
            if c:
                out[w] = c
            elif w in out:
                del out[w]
    return out


def neg(A):
    return {w: (-c) % P for w, c in A.items() if c % P}


def mul(A, B):
    out = {}
    for wa, ca in A.items():
        for wb, cb in B.items():
            w = wa + wb
            if len(w) > TRUNC:
                continue
            c = (out.get(w, 0) + ca * cb) % P
            if c:
                out[w] = c
            elif w in out:
                del out[w]
    return out


def power(A, k):
    if k == 0:
        return {(): 1}
    if k > 0:
        out = {(): 1}
        for _ in range(k):
            out = mul(out, A)
        return out

    # A = 1 + U, so A^{-1} = 1-U+U^2-U^3 modulo degree 3.
    U = add(A, {(): -1 % P})
    out = {(): 1}
    term = {(): 1}
    for i in range(1, TRUNC + 1):
        term = mul(term, U)
        sign = -1 if i % 2 else 1
        out = add(out, {w: sign * c for w, c in term.items()})
    return out


def homogeneous(A, degree):
    return {w: c for w, c in A.items() if len(w) == degree and c % P}


def fmt(A):
    return ", ".join(f"{w}:{c}" for w, c in sorted(A.items())) or "0"


def degree3(A):
    return homogeneous(A, 3)


def bracket(A, B):
    return add(mul(A, B), neg(mul(B, A)))


# Independent Magnus generators.
x = [None] + [{(): 1, (i,): 1} for i in range(1, 5)]
x1, x2, x3, x4 = x[1], x[2], x[3], x[4]

# Fixed relation commutator factor [x3,x4].
comm34 = mul(
    mul(x3, x4),
    mul(power(x3, -1), power(x4, -1)),
)


def C_finite(q):
    # The relation-derived finite-q control expression fixed by the protocol.
    return mul(
        mul(mul(x1, x2), comm34),
        mul(power(x1, q), power(x2, -1)),
    )


def C_infinity():
    # Fixed q=infinity baseline: omit the finite-q power factor.
    return mul(mul(x1, x2), mul(comm34, power(x2, -1)))


def strip_common_factors(C):
    # Remove the common x1 and [x3,x4] factors exactly as in the
    # baseline-relative definition of s_q.
    return mul(mul(C, power(x1, -1)), power(comm34, -1))


# ---- Gate-A derivation ----
C9 = C_finite(9)
Cinf = C_infinity()
s9 = strip_common_factors(C9)
sinf = strip_common_factors(Cinf)

in3_s9 = degree3(s9)
in3_sinf = degree3(sinf)
delta9 = degree3(add(s9, neg(sinf)))
d9 = bracket(delta9, {(2,): 1})

# Independent algebraic cross-check for the p-power term.
x19 = power(x1, 9)
x19_degree3 = degree3(x19)

print("Q3/Q9 GATE A — INDEPENDENT TRUNCATED-MAGNUS DERIVATION")
print("presentation: G9 = <x1,x2,x3,x4 | x1^9[x1,x2][x3,x4] = 1>")
print("field: F_3")
print("truncation degree:", TRUNC)
print("in_3(x1^9) =", fmt(x19_degree3))
print("in_3(s9)    =", fmt(in3_s9))
print("in_3(sinf)  =", fmt(in3_sinf))
print("Delta_3(9)  =", fmt(delta9))
print("d9=[Delta_3(9),X2] =", fmt(d9))

# The protocol forbids a preselected downstream result. These assertions
# therefore verify the independently derived algebra, not an input target.
assert x19_degree3 == {}, "x1^9 unexpectedly contributes at degree 3"
assert delta9 == {}, "q=9 degree-3 baseline difference is nonzero"
assert d9 == {}, "d9 must follow as the bracket of the derived zero source"

# Explicitly record the exact degree-3 equality.
assert in3_s9 == in3_sinf

artifact = {
    "experiment": "Q3/Q9 Gate A",
    "status": "PASS",
    "independence": "self-contained truncated-Magnus implementation; no q=3 research import",
    "presentation": "G9=<x1,x2,x3,x4 | x1^9[x1,x2][x3,x4]=1>",
    "field": "F_3",
    "truncation_degree": 3,
    "commutator_convention": "[a,b]=a b a^{-1} b^{-1}",
    "baseline": "q=infinity pure-commutator presentation",
    "in3_x1_power_9": sorted([[list(w), c] for w, c in x19_degree3.items()]),
    "in3_s9": sorted([[list(w), c] for w, c in in3_s9.items()]),
    "in3_sinf": sorted([[list(w), c] for w, c in in3_sinf.items()]),
    "Delta3_9": sorted([[list(w), c] for w, c in delta9.items()]),
    "d9": sorted([[list(w), c] for w, c in d9.items()]),
    "gate_A_criterion": "d9 is derived from the q=9 presentation/control independently before any N/J computation",
    "gate_A_result": "PASS",
    "gate_B_status": "BLOCKED until this Gate-A artifact is accepted",
}

art_dir = Path(__file__).parent / "artifacts"
art_dir.mkdir(exist_ok=True)
out = art_dir / "q3_q9_gate_a_d9_independent.json"
out.write_text(json.dumps(artifact, indent=2), encoding="utf-8")

print("Q3/Q9 GATE A RESULT = PASS")
print("artifact =", out)
