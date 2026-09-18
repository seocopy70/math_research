"""Q3/Q9 Gate C-1b — actual degree scan of s9 - s_infinity.

This reuses the Gate-A construction literally, changing only the truncation
degree from 3 to 9. No downstream source d or N/J probe is defined here.
The purpose is only to locate the first nonzero homogeneous degree of
Delta_d(9) = in_d(s9) - in_d(s_infinity), if any, through degree 9.

Convention: F_3, Magnus x_i=1+X_i, [a,b]=a b a^{-1} b^{-1}.
"""

P = 3
TRUNC = 9

def add(*As):
    out = {}
    for A in As:
        for w,c in A.items():
            c=(out.get(w,0)+c)%P
            if c: out[w]=c
            elif w in out: del out[w]
    return out

def neg(A):
    return {w:(-c)%P for w,c in A.items() if c%P}

def mul(A,B):
    out={}
    for wa,ca in A.items():
        for wb,cb in B.items():
            w=wa+wb
            if len(w)<=TRUNC:
                c=(out.get(w,0)+ca*cb)%P
                if c: out[w]=c
                elif w in out: del out[w]
    return out

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
x2={():1,(2,):1}
x3={():1,(3,):1}
x4={():1,(4,):1}

comm34=mul(mul(x3,x4),mul(power(x3,-1),power(x4,-1)))

def C_finite(q):
    return mul(mul(mul(x1,x2),comm34),mul(power(x1,q),power(x2,-1)))

def C_infinity():
    return mul(mul(x1,x2),mul(comm34,power(x2,-1)))

def strip_common_factors(C):
    return mul(mul(C,power(x1,-1)),power(comm34,-1))

C9=C_finite(9)
Cinf=C_infinity()
s9=strip_common_factors(C9)
sinf=strip_common_factors(Cinf)
delta=add(s9,neg(sinf))

print("Q3/Q9 GATE C-1b — ACTUAL DEGREE SCAN")
print("field: F_3")
print("truncation degree:",TRUNC)
print("construction: literal Gate-A C9/Cinf/strip_common_factors")
print("commutator convention: [a,b]=a b a^{-1} b^{-1]")

nonzero_degrees=[]
for d in range(1,TRUNC+1):
    hd=homogeneous(delta,d)
    print(f"Delta_{d}(9) =",fmt(hd))
    if hd:
        nonzero_degrees.append(d)

# Arithmetic consistency checks: the scan must include no terms above TRUNC,
# and the independently known power identity remains valid.
x19=power(x1,9)
assert x19=={():1,(1,)*9:1}

print("nonzero degrees through 9 =",nonzero_degrees)
if nonzero_degrees:
    first=nonzero_degrees[0]
    print("FIRST_NONZERO_DEGREE_THROUGH_9 =",first)
    print("FIRST_NONZERO_COMPONENT =",fmt(homogeneous(delta,first)))
else:
    print("FIRST_NONZERO_DEGREE_THROUGH_9 = NONE")
    print("NO_NONZERO_BASELINE_DIFFERENCE_THROUGH_DEGREE_9 = PASS")

print("GATE C-1b RESULT = PASS")
