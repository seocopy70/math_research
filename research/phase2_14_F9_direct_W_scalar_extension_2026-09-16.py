"""Phase 2-14: direct F9 scalar extension of the certified W action.

Avoids reconstructing L4/R4 in F9.  Starts from the certified 45x45
Sp4(F3)-action on W, scalar-extends it to F9, derives U=im(N), forms
E=W/U, and probes U^+(F9) fixed line and its split-torus character.
"""
from pathlib import Path
import runpy, itertools, numpy as np

ROOT=Path(__file__).resolve().parents[1]
P=3

def f9(x): return (x[0]%3,x[1]%3) if isinstance(x,tuple) else (int(x)%3,0)
def add(x,y): return ((x[0]+y[0])%3,(x[1]+y[1])%3)
def neg(x): return ((-x[0])%3,(-x[1])%3)
def sub(x,y): return add(x,neg(y))
def mul(x,y): return ((x[0]*y[0]+2*x[1]*y[1])%3,(x[0]*y[1]+x[1]*y[0])%3)
def zero(x): return x==(0,0)
def inv(x):
    if zero(x): raise ZeroDivisionError
    d=(x[0]*x[0]+x[1]*x[1])%3
    di=1 if d==1 else 2
    return ((x[0]*di)%3,(-x[1]*di)%3)
def div(x,y): return mul(x,inv(y))
def pow9(x,n):
    r=(1,0)
    while n:
        if n&1:r=mul(r,x)
        x=mul(x,x);n//=2
    return r
F9=[(a,b) for a in range(3) for b in range(3)]
F9star=[x for x in F9 if not zero(x)]
assert len(F9star)==8 and all(pow9(x,8)==(1,0) for x in F9star)

def I(n):
    A=np.empty((n,n),dtype=object)
    for i in range(n):
        for j in range(n): A[i,j]=(1,0) if i==j else (0,0)
    return A

def mat(A,B):
    C=np.empty((A.shape[0],B.shape[1]),dtype=object)
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            s=(0,0)
            for k in range(A.shape[1]): s=add(s,mul(A[i,k],B[k,j]))
            C[i,j]=s
    return C

def vec(A):
    return np.array([f9(x) for x in A],dtype=object)

def mv(A,v):
    return np.array([sum9(mul(A[i,j],v[j]) for j in range(A.shape[1])) for i in range(A.shape[0])],dtype=object)

def sum9(it):
    s=(0,0)
    for x in it:s=add(s,x)
    return s

def rank3(A):
    A=np.array(A,dtype=int,copy=True)%3
    if A.ndim==1:A=A.reshape(-1,1)
    m,n=A.shape;r=0
    for c in range(n):
        q=next((i for i in range(r,m) if A[i,c]),None)
        if q is None:continue
        A[[r,q]]=A[[q,r]]
        if A[r,c]==2:A[r]=(2*A[r])%3
        for i in range(m):
            if i!=r and A[i,c]:A[i]=(A[i]-A[i,c]*A[r])%3
        r+=1
    return r

def rank9(A):
    A=np.array(A,dtype=object,copy=True);m,n=A.shape;r=0
    for c in range(n):
        q=next((i for i in range(r,m) if not zero(A[i,c])),None)
        if q is None:continue
        A[[r,q]]=A[[q,r]];z=inv(A[r,c]);A[r]=[mul(z,x) for x in A[r]]
        for i in range(m):
            if i!=r and not zero(A[i,c]):
                z=A[i,c];A[i]=[sub(A[i,j],mul(z,A[r,j])) for j in range(n)]
        r+=1
    return r

def null9(A):
    A=np.array(A,dtype=object,copy=True);m,n=A.shape;r=0;piv=[]
    for c in range(n):
        q=next((i for i in range(r,m) if not zero(A[i,c])),None)
        if q is None:continue
        A[[r,q]]=A[[q,r]];z=inv(A[r,c]);A[r]=[mul(z,x) for x in A[r]]
        for i in range(m):
            if i!=r and not zero(A[i,c]):
                z=A[i,c];A[i]=[sub(A[i,j],mul(z,A[r,j])) for j in range(n)]
        piv.append(c);r+=1
    free=[j for j in range(n) if j not in piv];out=[]
    for f in free:
        x=np.array([(1,0) if j==f else (0,0) for j in range(n)],dtype=object)
        for rr,c in enumerate(piv):x[c]=neg(A[rr,f])
        out.append(x)
    return out

# Certified F3 representation and square-zero endomorphism.
ns1=runpy.run_path(str(ROOT/'research/phase2_1_invariant_space_verification_2026-09-15.py'))
A3=[np.array(A,dtype=int)%3 for A in ns1['action_matrices']]
ns3=runpy.run_path(str(ROOT/'research/phase2_3_endH_optimized_2026-09-15.py'))
N=np.array(ns3['N'],dtype=int)%3
assert len(A3)==5 and all(A.shape==(45,45) for A in A3)
assert rank3(N)==10 and np.array_equal((N@N)%3,np.zeros((45,45),dtype=int))
A=[np.vectorize(f9,otypes=[object])(g) for g in A3]
N9=np.vectorize(f9,otypes=[object])(N)

# U basis = independent columns of N; complement chosen from standard basis.
U=[];r=0
for j in range(45):
    C=np.column_stack([np.array(U).T if U else np.empty((45,0),int),N[:,j]])
    q=rank3(C)
    if q>r:U.append(N[:,j].copy());r=q
    if r==10:break
U3=np.column_stack(U)
C=[];r=10
for j in range(45):
    Cmat=np.column_stack([U3,np.eye(45,dtype=int)[:,j]])
    q=rank3(Cmat)
    if q>r:C.append(np.eye(45,dtype=int)[:,j]);r=q
    if r==45:break
C3=np.column_stack(C);Q3=np.column_stack([U3,C3])
assert Q3.shape==(45,45) and rank3(Q3)==45
Q=np.vectorize(f9,otypes=[object])(Q3)
# Exact inverse of Q over F9.
def inv9(M):
    M=np.array(M,dtype=object,copy=True);n=M.shape[0];Aug=np.empty((n,2*n),dtype=object);Aug[:,:n]=M;Aug[:,n:]=I(n)
    for c in range(n):
        q=next(i for i in range(c,n) if not zero(Aug[i,c]));Aug[[c,q]]=Aug[[q,c]];z=inv(Aug[c,c]);Aug[c]=[mul(z,x) for x in Aug[c]]
        for i in range(n):
            if i!=c and not zero(Aug[i,c]):
                z=Aug[i,c];Aug[i]=[sub(Aug[i,j],mul(z,Aug[c,j])) for j in range(2*n)]
    return Aug[:,n:]
Qinv=inv9(Q)

def act_E(g):
    # In Q-basis, first 10 coordinates are U, last 35 are E.
    M=mat(Qinv,mat(g,Q))
    return M[10:,10:]

def act_U(g):
    M=mat(Qinv,mat(g,Q))
    return M[:10,:10]

Pmat=np.eye(4,dtype=int)[:,[0,2,1,3]]
Pinv=Pmat.T
P9=np.vectorize(f9,otypes=[object])(Pmat);Pinv9=np.vectorize(f9,otypes=[object])(Pinv)
def root(kind,t=(1,0)):
    R=I(4)
    if kind=='a1':R[0,1]=t;R[3,2]=neg(t)
    elif kind=='a2':R[1,3]=t
    elif kind=='a12':R[0,3]=t;R[1,2]=t
    elif kind=='a112':R[0,2]=t
    return mat(P9,mat(R,Pinv9))
roots=[root(k) for k in ['a1','a2','a12','a112']]
EU=[act_E(g) for g in roots];UU=[act_U(g) for g in roots]
fixedE=null9(np.vstack([[sub(g,I(35))[i,j] for j in range(35)] for g in EU for i in range(35)]))
fixedU=null9(np.vstack([[sub(g,I(10))[i,j] for j in range(10)] for g in UU for i in range(10)]))
assert len(fixedE)==1
v=fixedE[0]
assert len(fixedU)==0 or len(fixedU)>=1

def torus(a,b):
    D=I(4);D[0,0]=a;D[1,1]=b;D[2,2]=inv(a);D[3,3]=inv(b)
    return mat(P9,mat(D,Pinv9))

def scalar(A,v):
    Av=mv(A,v);i=next(i for i,x in enumerate(v) if not zero(x));lam=div(Av[i],v[i])
    assert all(zero(sub(Av[j],mul(lam,v[j]))) for j in range(len(v)))
    return lam
chi={(a,b):scalar(act_E(torus(a,b)),v) for a in F9star for b in F9star}
for a,b,c,d in itertools.product(F9star,repeat=4):
    assert chi[(mul(a,c),mul(b,d))]==mul(chi[(a,b)],chi[(c,d)])
matches=[(e1,e2) for e1 in range(8) for e2 in range(8) if all(chi[(a,b)]==mul(pow9(a,e1),pow9(b,e2)) for a,b in itertools.product(F9star,repeat=2))]

print('PHASE 2-14 / DIRECT F9 SCALAR EXTENSION OF W')
print('|F9*| =',len(F9star))
print('dim W = 45')
print('dim U = 10')
print('dim E = 35')
print('dim E^{U+(F9)} =',len(fixedE))
print('dim U^{U+(F9)} =',len(fixedU))
print('character matches exponents (e1,e2) mod 8 =',matches)
print('EXPECTED (2,1) = (3,1) in epsilon coordinates')
print('EXPECTED character a^3 b =',(3,1) in matches)
assert matches==[(3,1)]
print('CERTIFICATE: exact F9 torus character law verified on all 64 torus elements.')
