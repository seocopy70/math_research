"""Phase 2-14 v2: direct F9 scalar extension of certified W.

Uses the certified 45-dimensional W representation over F3, extends scalars
to F9, constructs U=im(N) correctly as a 10-column basis, complements it
to W, and computes E=W/U. Then checks U^+(F9)-fixed lines and torus
characters exactly. No L4/R4 reconstruction is used.
"""
from pathlib import Path
import runpy,itertools,numpy as np
ROOT=Path(__file__).resolve().parents[1]

def add(x,y): return ((x[0]+y[0])%3,(x[1]+y[1])%3)
def neg(x): return ((-x[0])%3,(-x[1])%3)
def sub(x,y): return add(x,neg(y))
def mul(x,y): return ((x[0]*y[0]+2*x[1]*y[1])%3,(x[0]*y[1]+x[1]*y[0])%3)
def zero(x): return x==(0,0)
def inv(x):
    if zero(x): raise ZeroDivisionError
    d=(x[0]*x[0]+x[1]*x[1])%3;di=1 if d==1 else 2
    return ((x[0]*di)%3,(-x[1]*di)%3)
def div(x,y): return mul(x,inv(y))
def pow9(x,n):
    r=(1,0)
    while n:
        if n&1:r=mul(r,x)
        x=mul(x,x);n//=2
    return r
F9=[(a,b) for a in range(3) for b in range(3)];F9star=[x for x in F9 if not zero(x)]
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
            for k in range(A.shape[1]):s=add(s,mul(A[i,k],B[k,j]))
            C[i,j]=s
    return C

def mv(A,v):
    out=[]
    for i in range(A.shape[0]):
        s=(0,0)
        for j in range(A.shape[1]):s=add(s,mul(A[i,j],v[j]))
        out.append(s)
    return np.array(out,dtype=object)

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

def inv9(A):
    A=np.array(A,dtype=object,copy=True);n=A.shape[0];aug=np.empty((n,2*n),dtype=object);aug[:,:n]=A;aug[:,n:]=I(n)
    for c in range(n):
        q=next(i for i in range(c,n) if not zero(aug[i,c]));aug[[c,q]]=aug[[q,c]];z=inv(aug[c,c]);aug[c]=[mul(z,x) for x in aug[c]]
        for i in range(n):
            if i!=c and not zero(aug[i,c]):
                z=aug[i,c];aug[i]=[sub(aug[i,j],mul(z,aug[c,j])) for j in range(2*n)]
    return aug[:,n:]

def ext(A): return np.array([[(int(x)%3,0) for x in row] for row in np.asarray(A)],dtype=object)

ns1=runpy.run_path(str(ROOT/'research/phase2_1_invariant_space_verification_2026-09-15.py'))
A3=[np.array(A,dtype=int)%3 for A in ns1['action_matrices']]
ns3=runpy.run_path(str(ROOT/'research/phase2_3_endH_optimized_2026-09-15.py'))
N=np.array(ns3['N'],dtype=int)%3
assert len(A3)==5 and all(A.shape==(45,45) for A in A3)
assert rank3(N)==10 and np.array_equal((N@N)%3,np.zeros((45,45),dtype=int))
A=[ext(g) for g in A3]

# Correctly extract a basis of im(N): independent columns of N.
Ucols=[];r=0
for j in range(45):
    cand=N[:,j]
    C=np.column_stack(Ucols+[cand]) if Ucols else cand.reshape(45,1)
    q=rank3(C)
    if q>r:Ucols.append(cand.copy());r=q
    if r==10:break
U3=np.column_stack(Ucols)
assert U3.shape==(45,10) and rank3(U3)==10

# Complement U to a full W basis.
Ccols=[];r=10
for j in range(45):
    cand=np.eye(45,dtype=int)[:,j]
    C=np.column_stack([U3]+Ccols+[cand])
    q=rank3(C)
    if q>r:Ccols.append(cand.copy());r=q
    if r==45:break
C3=np.column_stack(Ccols)
Q3=np.column_stack([U3,C3])
assert Q3.shape==(45,45) and rank3(Q3)==45
Q=ext(Q3);Qinv=inv9(Q)

def coord_action(g):return mat(Qinv,mat(g,Q))
def act_U(g):return coord_action(g)[:10,:10]
def act_E(g):return coord_action(g)[10:,10:]

P=np.eye(4,dtype=int)[:,[0,2,1,3]];Pinv=P.T
P9=ext(P);Pinv9=ext(Pinv)
def root(kind,t=(1,0)):
    R=I(4)
    if kind=='a1':R[0,1]=t;R[3,2]=neg(t)
    elif kind=='a2':R[1,3]=t
    elif kind=='a12':R[0,3]=t;R[1,2]=t
    elif kind=='a112':R[0,2]=t
    return mat(P9,mat(R,Pinv9))
roots=[root(k) for k in ['a1','a2','a12','a112']]
EU=[act_E(g) for g in roots];UU=[act_U(g) for g in roots]
fixedE=null9(np.vstack([np.array([[sub(g[i,j],I(35)[i,j]) for j in range(35)] for i in range(35)],dtype=object) for g in EU]))
fixedU=null9(np.vstack([np.array([[sub(g[i,j],I(10)[i,j]) for j in range(10)] for i in range(10)],dtype=object) for g in UU]))
assert len(fixedE)==1 and len(fixedU)==1
v=fixedE[0]

# Torus in standard C2 coordinates, then conjugate to repository coordinates.
def torus(a,b):
    D=I(4);D[0,0]=a;D[1,1]=b;D[2,2]=inv(a);D[3,3]=inv(b)
    return mat(P9,mat(D,Pinv9))
def scalar(A,v):
    Av=mv(A,v);i=next(i for i,x in enumerate(v) if not zero(x));lam=div(Av[i],v[i])
    assert all(zero(sub(Av[j],mul(lam,v[j]))) for j in range(len(v)))
    return lam
chi={(a,b):scalar(act_E(torus(a,b)),v) for a,b in itertools.product(F9star,F9star)}
for a,b,c,d in itertools.product(F9star,repeat=4):
    assert chi[(mul(a,c),mul(b,d))]==mul(chi[(a,b)],chi[(c,d)])
matches=[(e1,e2) for e1 in range(8) for e2 in range(8) if all(chi[(a,b)]==mul(pow9(a,e1),pow9(b,e2)) for a,b in itertools.product(F9star,F9star))]
assert matches==[(3,1)]

# U highest-line character sanity: expected (2,0)=2 epsilon_1, so a^2.
u=fixedU[0]
chiU={(a,b):scalar(act_U(torus(a,b)),u) for a,b in itertools.product(F9star,F9star)}
assert all(chiU[(a,b)]==pow9(a,2) for a,b in itertools.product(F9star,F9star))

print('PHASE 2-14 v2 / DIRECT F9 SCALAR EXTENSION OF W')
print('|F9*| =',len(F9star))
print('dim W = 45')
print('dim U = 10')
print('dim E = 35')
print('dim E^{U+(F9)} =',len(fixedE))
print('dim U^{U+(F9)} =',len(fixedU))
print('E character exponents mod 8 =',matches)
print('E expected a^3 b =',True)
print('U expected character a^2 =',True)
print('CERTIFICATE: exact F9 character laws verified on all 64 torus elements for E and U.')
