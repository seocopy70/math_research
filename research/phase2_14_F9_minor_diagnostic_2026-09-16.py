"""Phase 2-14 F9 diagnostic: isolate scalar-extension failure before algebraic action.

Checks F9 axioms, F3 inclusion compatibility, and the certified 50x50 minor
before any F9 group action is attempted. No representation-theoretic
conclusion is drawn here.
"""
from pathlib import Path
import runpy, itertools, numpy as np
ROOT=Path(__file__).resolve().parents[1]

def add(x,y): return ((x[0]+y[0])%3,(x[1]+y[1])%3)
def neg(x): return ((-x[0])%3,(-x[1])%3)
def sub(x,y): return add(x,neg(y))
def mul(x,y): return ((x[0]*y[0]+2*x[1]*y[1])%3,(x[0]*y[1]+x[1]*y[0])%3)
def zero(x): return x==(0,0)
def inv(x):
    if zero(x): raise ZeroDivisionError
    d=(x[0]*x[0]+x[1]*x[1])%3; di=1 if d==1 else 2
    return ((x[0]*di)%3,(-x[1]*di)%3)
def pow9(x,n):
    r=(1,0)
    while n:
        if n&1:r=mul(r,x)
        x=mul(x,x); n//=2
    return r
F9=[(a,b) for a in range(3) for b in range(3)]
F9star=[x for x in F9 if not zero(x)]
def embed3(a): return (int(a)%3,0)

print('DIAGNOSTIC 1 / F9 FIELD AXIOMS')
assert len(F9)==9 and len(F9star)==8
assert all(pow9(x,8)==(1,0) for x in F9star)
assert all(not zero(inv(x)) for x in F9star)
assert all(mul(embed3(a),embed3(b))==embed3((a*b)%3) for a,b in itertools.product(range(3),repeat=2))
assert all(add(embed3(a),embed3(b))==embed3((a+b)%3) for a,b in itertools.product(range(3),repeat=2))
assert add(add(embed3(1),embed3(1)),embed3(1))==(0,0)
print('F9 axioms = PASSED')
print('F9* order =',len(F9star))
print('F3 inclusion compatibility = PASSED')
print('characteristic 3 = PASSED')

print('\nDIAGNOSTIC 2 / CERTIFIED 50x50 MINOR')
ns=runpy.run_path(str(ROOT/'research'/'phase2_1_invariant_space_verification_2026-09-15.py'))
R4_ind=np.asarray(ns['R4_ind'],dtype=int)%3
basis=ns['basis']; selected_rows=list(ns['selected_rows'])
assert R4_ind.shape==(256,5) and len(basis)==45 and len(selected_rows)==50
words4=list(itertools.product(range(1,5),repeat=4)); index4={w:i for i,w in enumerate(words4)}

def vec9(A):
    v=[(0,0) for _ in range(256)]
    for w,c in A.items(): v[index4[w]]=embed3(c)
    return v
Rcols=[[embed3(int(x)) for x in col] for col in R4_ind.T]
Wcols=[vec9(a) for a in basis]
B9=np.empty((256,50),dtype=object)
for j,col in enumerate(Rcols+Wcols):
    for i,x in enumerate(col): B9[i,j]=x
W3=np.zeros((256,45),dtype=int)
for j,col in enumerate(basis):
    for w,c in col.items(): W3[index4[w],j]=int(c)%3
B3=np.column_stack([R4_ind,W3])%3
minor3=B3[selected_rows,:]; minor9=B9[selected_rows,:]
assert minor3.shape==(50,50) and minor9.shape==(50,50)

def det3(A):
    A=np.array(A,dtype=int,copy=True)%3; n=A.shape[0]; d=1
    for c in range(n):
        q=next((i for i in range(c,n) if A[i,c]),None)
        if q is None:return 0
        if q!=c:A[[c,q]]=A[[q,c]]; d=(-d)%3
        p=int(A[c,c])%3; d=(d*p)%3; ip=1 if p==1 else 2
        for i in range(c+1,n):
            if A[i,c]:
                z=(int(A[i,c])*ip)%3; A[i,c:]=(A[i,c:]-z*A[c,c:])%3
    return d%3

def det9(A):
    A=np.array(A,dtype=object,copy=True); n=A.shape[0]; d=(1,0)
    for c in range(n):
        q=next((i for i in range(c,n) if not zero(A[i,c])),None)
        if q is None:return (0,0)
        if q!=c:A[[c,q]]=A[[q,c]]; d=neg(d)
        p=A[c,c]; d=mul(d,p); ip=inv(p)
        for i in range(c+1,n):
            if not zero(A[i,c]):
                z=mul(A[i,c],ip)
                for j in range(c,n): A[i,j]=sub(A[i,j],mul(z,A[c,j]))
    return d

d3=det3(minor3); d9=det9(minor9)
print('det_F3(minor) =',d3)
print('embed(det_F3) =',embed3(d3))
print('det_F9(extended minor) =',d9)
print('determinant agreement =',d9==embed3(d3))
assert d3!=0 and d9==embed3(d3)

mismatch=[]
for i in range(50):
    for j in range(50):
        if minor9[i,j]!=embed3(int(minor3[i,j])): mismatch.append((i,j,minor3[i,j],minor9[i,j]))
print('elementwise mismatches =',len(mismatch))
assert not mismatch
print('rank certificate = 50 over F3 and therefore over F9')
print('CERTIFICATE: scalar-extension minor is elementwise identical and determinant agrees.')
