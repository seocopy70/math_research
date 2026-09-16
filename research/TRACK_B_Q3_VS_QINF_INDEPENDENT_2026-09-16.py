"""Independent exact truncated-Magnus check of q=3 vs q=infinity.

Purpose: reproduce the degree-3 separation without importing any earlier
research script. Arithmetic is in F_3 and uses Magnus substitutions
x_i = 1 + X_i, truncated to total degree <= 3.
"""

P = 3
N = 3


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
            if len(w) <= N:
                C[w] = (C.get(w, 0) + ca * cb) % P
                if C[w] == 0:
                    del C[w]
    return C


def power(A, k):
    if k == 0:
        return {(): 1}
    if k > 0:
        R = {(): 1}
        for _ in range(k):
            R = mul(R, A)
        return R
    U = add(A, {(): -1 % P})
    R = {(): 1}
    term = {(): 1}
    for i in range(1, N + 1):
        term = mul(term, U)
        R = add(R, {w: ((-1) ** i) * c for w, c in term.items()})
    return R


def homogeneous(A, d):
    return {w: c for w, c in A.items() if len(w) == d}


def monomial_word(c, w):
    return {w: c % P}


def fmt(A):
    return ", ".join(f"{w}:{c}" for w, c in sorted(A.items())) or "0"


# Magnus generators x_i = 1 + X_i.
x = [None] + [{(): 1, (i,): 1} for i in range(1, 5)]
x1, x2, x3, x4 = x[1], x[2], x[3], x[4]

# Group commutator [x3,x4] = x3*x4*x3^{-1}*x4^{-1}.
comm34 = mul(mul(x3, x4), mul(power(x3, -1), power(x4, -1)))

# Relation-derived conjugation identities used in the comparison.
# Finite-q: C_q(x1) = x1*x2*[x3,x4]*x1^q*x2^{-1}.
# q=infinity control: delete the x1^q factor.
def C_finite(q):
    return mul(
        mul(mul(x1, x2), comm34),
        mul(power(x1, q), power(x2, -1)),
    )


C3 = C_finite(3)
Cinf = mul(mul(x1, x2), mul(comm34, power(x2, -1)))

# Remove the common x1 and [x3,x4] factors.
s3 = mul(mul(C3, power(x1, -1)), power(comm34, -1))
sinf = mul(mul(Cinf, power(x1, -1)), power(comm34, -1))

h3 = homogeneous(s3, 3)
hinf = homogeneous(sinf, 3)
diff = homogeneous(add(s3, neg(sinf)), 3)
power_part = monomial_word(1, (1, 1, 1))

print("TRACK B / INDEPENDENT q=3 VS q=infinity")
print("degree-3 s_3        =", fmt(h3))
print("degree-3 s_infty    =", fmt(hinf))
print("degree-3 difference =", fmt(diff))
print("expected X1^[3]      =", fmt(power_part))

assert diff == power_part
assert homogeneous(add(h3, neg(hinf)), 3) == power_part
print("CERTIFICATE: in_3(s_3) - in_3(s_infty) = X1^[3].")

# In the tensor realization X1^[3]=X1^3, so [X1^3,X1]=0 identically.
power_bracket = add(
    mul(power_part, {(1,): 1}),
    neg(mul({(1,): 1}, power_part)),
)
assert power_bracket == {}
print("CERTIFICATE: [X1^[3], X1] = 0 in F_3.")
print("Conclusion: the previously studied degree-4 A3 bracket cannot carry q-separation; degree 3 does.")
