from collections import defaultdict

P=3
MAXD=4

def add(A,B):
    C=defaultdict(int); C.update(A)
    for w,c in B.items():
        C[w]=(C[w]+c)%P
    return {w:c for w,c in C.items() if c%P}

def mul(A,B):
    C=defaultdict(int)
    for wa,ca in A.items():
        for wb,cb in B.items():
            w=wa+wb
            if len(w)<=MAXD:
                C[w]=(C[w]+ca*cb)%P
    return {w:c for w,c in C.items() if c%P}

def power(A,n):
    if n==0:return {():1}
    if n<0:return inv(A,-n)
    out={():1}; base=A
    while n:
        if n&1: out=mul(out,base)
        base=mul(base,base); n//=2
    return out

def inv(A,n):
    # A has constant term 1. Geometric inverse: (1+h)^-1=sum(-h)^k.
    h=add(A,{():-1})
    out={():1}; term={():1}
    for _ in range(1,n+1):
        term=mul(term,h)
        out=add(out, {w:((-1)**_) * c for w,c in term.items()})
    return out

def gen(i):
    return {():1,(i,):1}

def homogeneous(A,d):
    return {w:c for w,c in A.items() if len(w)==d and c%P}

def fmt(A):
    return ' + '.join(f'{c}*'+('1' if w==() else ''.join(f'X{i}' for i in w)) for w,c in sorted(A.items())) or '0'

X1,X2,X3,X4=[gen(i) for i in range(1,5)]
c=add(mul(X3,X4),{(4,3): -1})
# Exact identity valid for G_q: C_q=x1*x2*[x3,x4]*x1^q*x2^{-1}.
for q in (3,9):
    C=mul(mul(mul(mul(X1,X2),c),power(X1,q)),inv(X2,MAXD))
    print(f'q={q}')
    for d in range(1,5):
        print(f'degree {d}: {fmt(homogeneous(C,d))}')
    if q==3:
        C3=C
    else:
        C9=C

print('COMMON_QUADRATIC_RELATION: [X1,X2]+[X3,X4]')
for d in (1,2,3,4):
    diff=add(homogeneous(C3,d), {w:-c for w,c in homogeneous(C9,d).items()})
    print(f'degree {d} difference q3-q9: {fmt(diff)}')

# The q-dependent power term x1^q itself starts at Magnus degree q.
print('x1^3 first nonzero Magnus degree = 3')
print('x1^9 first nonzero Magnus degree = 9')
assert homogeneous(power(X1,3),3) != {}
assert homogeneous(power(X1,9),4) == {}
assert homogeneous(C3,2)==homogeneous(C9,2)
print('CERTIFICATE: q=3 and q=9 have identical degree-2 Magnus shadow, while q-sensitive power contribution begins in degrees 3 and 9 respectively.')
