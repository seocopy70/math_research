"""Q3/Q9 Gate C-2a — restricted-power identification preflight.

Purpose:
  Verify, in the one-generator associative/Magnus model over F_3, that
      X_1^[3] = X_1^3
  and
      (X_1^[3])^[3] = X_1^9
  under the standard restricted-power realization inside the universal
  enveloping algebra.

This is ONLY an identification preflight. It does not define d_9^(9),
does not test H-equivariance, and does not run N/J.
"""

P = 3
TRUNC = 9

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

def mul(A, B):
    out = {}
    for wa, ca in A.items():
        for wb, cb in B.items():
            w = wa + wb
            if len(w) <= TRUNC:
                c = (out.get(w, 0) + ca * cb) % P
                if c:
                    out[w] = c
                elif w in out:
                    del out[w]
    return out

def power(A, k):
    out = {(): 1}
    for _ in range(k):
        out = mul(out, A)
    return out

def fmt(A):
    return ", ".join(f"{w}:{c}" for w, c in sorted(A.items())) or "0"

X1 = {(1,): 1}

# In the enveloping-algebra realization of the restricted structure,
# the p-map on a primitive element is represented by associative p-th power.
X1_p = power(X1, 3)
X1_p2 = power(X1_p, 3)
X1_9 = power(X1, 9)

print("Q3/Q9 GATE C-2a — RESTRICTED-POWER IDENTIFICATION")
print("field: F_3")
print("truncation degree:", TRUNC)
print("X1^[3] =", fmt(X1_p))
print("(X1^[3])^[3] =", fmt(X1_p2))
print("X1^9 =", fmt(X1_9))

assert X1_p == {(1,1,1): 1}
assert X1_p2 == {(1,1,1,1,1,1,1,1,1): 1}
assert X1_p2 == X1_9

print("FIRST_P_POWER = PASS")
print("ITERATED_P_POWER = PASS")
print("C-2a RESULT = PASS")
print("SCOPE = restricted-power identification only; no source d and no N/J")
