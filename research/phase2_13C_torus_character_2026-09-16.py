"""Phase 2-13C: torus character of the unique U^+(F3)-fixed line.

Uses exact finite-field matrix inversion. No full algebraic highest-weight
identification is claimed.
"""
from pathlib import Path
import runpy
import numpy as np

P=3
ROOT=Path(__file__).resolve().parents[1]
ns=runpy.run_path(str(ROOT/'research'/'phase2_13B_positive_unipotent_2026-09-15.py'))
quotient_action_single=ns['quotient_action_single']
fixed=ns['fixed']
Pmat=ns['Pmat']; Pinv=ns['Pinv']; J=ns['J']
roots=ns['roots']

assert len(fixed)==1
v=np.array(fixed[0],dtype=np.int64)%P

def torus(a,b):
    ai=pow(int(a),-1,P); bi=pow(int(b),-1,P)
    d=np.diag([a,b,ai,bi]).astype(np.int64)%P
    return (Pmat@d@Pinv)%P

def rank3(A):
    A=np.array(A,dtype=np.int64,copy=True)%P
    m,n=A.shape; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if A[i,c]),None)
        if q is None: continue
        A[[r,q]]=A[[q,r]]
        if A[r,c]==2: A[r]=(2*A[r])%P
        for i in range(m):
            if i!=r and A[i,c]: A[i]=(A[i]-A[i,c]*A[r])%P
        r+=1
        if r==m: break
    return r

def scalar_on_line(A,v):
    Av=(A@v)%P
    if rank3(np.column_stack([v,Av]))>1:
        return None, Av
    i=int(np.flatnonzero(v)[0])
    return int(Av[i]), Av

def key(A): return tuple(np.array(A,dtype=np.int64).flatten().tolist())

# Explicit positive-unipotent subgroup.
Uplus={key(np.eye(4,dtype=np.int64)):np.eye(4,dtype=np.int64)}
frontier=list(Uplus.values())
while frontier:
    a=frontier.pop()
    for g in roots:
        b=(a@g)%P; k=key(b)
        if k not in Uplus:
            Uplus[k]=b; frontier.append(b)
assert len(Uplus)==81

# Exact inverse over F_3. Do not use floating-point np.linalg.inv here.
def inverse3(A):
    A=np.array(A,dtype=np.int64,copy=True)%P
    n=A.shape[0]
    aug=np.column_stack([A,np.eye(n,dtype=np.int64)])%P
    for c in range(n):
        q=next((i for i in range(c,n) if aug[i,c]),None)
        if q is None: raise ValueError('singular matrix over F3')
        aug[[c,q]]=aug[[q,c]]
        if aug[c,c]==2: aug[c]=(2*aug[c])%P
        for i in range(n):
            if i!=c and aug[i,c]:
                aug[i]=(aug[i]-aug[i,c]*aug[c])%P
    return aug[:,n:]%P

rows=[]
for a in [1,2]:
    for b in [1,2]:
        g=torus(a,b)
        symp=np.array_equal((g.T@J@g)%P,J)
        gi=inverse3(g)
        assert np.array_equal((g@gi)%P,np.eye(4,dtype=np.int64))
        assert np.array_equal((gi@g)%P,np.eye(4,dtype=np.int64))
        normalizes=True
        for u in Uplus.values():
            c=(g@u@gi)%P
            if key(c) not in Uplus:
                normalizes=False
                break
        A=quotient_action_single(g)
        lam,Av=scalar_on_line(A,v)
        rows.append((a,b,lam,symp,normalizes,A.shape,Av))
        print('CHECK a,b =',a,b,'symplectic =',symp,
              'normalizes U+ =',normalizes,
              'fixed-line preserved =',lam is not None,'A shape =',A.shape)
        if lam is None:
            print('  witness v =',v.tolist())
            print('  Av =',Av.tolist())

assert all(r[3] for r in rows)
assert all(r[4] for r in rows)
assert all(r[2] is not None for r in rows)

print('PHASE 2-13C / TORUS CHARACTER OF U+-FIXED LINE')
print('fixed-line dimension =',len(fixed))
print('standard C2 split torus elements = 4')
for a,b,lam,symp,norm,shape,_ in rows:
    print('a,b =',a,b,'lambda =',lam,'symplectic =',symp,'normalizes U+ =',norm,'shape =',shape)
print('TORUS_CHARACTER_TABLE =',[(a,b,lam) for a,b,lam,_,_,_,_ in rows])
print('CERTIFICATE: unique U^+(F3)-fixed line is preserved by the split torus.')
print('INTERPRETATION: finite-field torus character only; no full algebraic highest weight is claimed.')
