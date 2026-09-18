"""Q3/Q9 Gate C-1a — degree-9 Magnus arithmetic sanity.

Preflight only: this does not define Delta_9 or any downstream probe.
"""
from collections import defaultdict

P = 3
TRUNC = 9

def add(*As):
    out = defaultdict(int)
    for A in As:
        for w, c in A.items():
            out[w] = (out[w] + c) % P
    return {w:c for w,c in out.items() if c}

def neg(A):
    return {w:(-c)%P for w,c in A.items() if c%P}

def mul(A,B):
    out = defaultdict(int)
    for wa,ca in A.items():
        for wb,cb in B.items():
            w=wa+wb
            if len(w)<=TRUNC:
                out[w]=(out[w]+ca*cb)%P
    return {w:c for w,c in out.items() if c}

def power(A,k):
    if k==0: return {():1}
    if k>0:
        out={():1}
        for _ in range(k): out=mul(out,A)
        return out
    U=add(A,{():-1%P})
    out={():1}; term={():1}
    for i in range(1,TRUNC+1):
        term=mul(term,U)
        out=add(out, term if i%2==0 else neg(term))
    return out

def homogeneous(A,d):
    return {w:c for w,c in A.items() if len(w)==d and c%P}

def fmt(A):
    return ", ".join(f"{w}:{c}" for w,c in sorted(A.items())) or "0"

x1={():1,(1,):1}
x1_9=power(x1,9)

print("Q3/Q9 GATE C-1a — DEGREE-9 MAGNUS ARITHMETIC SANITY")
print("field: F_3")
print("truncation degree:",TRUNC)
print("x1^9 =",fmt(x1_9))
for d in range(1,10):
    print(f"in_{d}(x1^9) =",fmt(homogeneous(x1_9,d)))

expected={():1,(1,)*9:1}
assert x1_9==expected
inv_x1=power(x1,-1)
assert mul(x1,inv_x1)=={():1}
assert mul(inv_x1,x1)=={():1}

print("POWER_IDENTITY = PASS")
print("INVERSE_SANITY = PASS")
print("GATE C-1a RESULT = PASS")
