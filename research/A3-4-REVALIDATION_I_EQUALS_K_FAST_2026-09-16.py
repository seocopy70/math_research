import runpy
import numpy as np
P=3

def rank3(A):
    A=np.array(A,dtype=np.int64,copy=True)%P
    if A.ndim==1:A=A[:,None]
    m,n=A.shape;r=0
    for c in range(n):
        q=next((i for i in range(r,m) if A[i,c]),None)
        if q is None: continue
        A[[r,q]]=A[[q,r]]
        if A[r,c]==2:A[r]=(2*A[r])%P
        for i in range(m):
            if i!=r and A[i,c]:A[i]=(A[i]-A[i,c]*A[r])%P
        r+=1
        if r==m:break
    return r

def null3(A):
    A=np.array(A,dtype=np.int64,copy=True)%P
    m,n=A.shape;R=A.copy();p=[];r=0
    for c in range(n):
        q=next((i for i in range(r,m) if R[i,c]),None)
        if q is None:continue
        R[[r,q]]=R[[q,r]]
        if R[r,c]==2:R[r]=(2*R[r])%P
        for i in range(m):
            if i!=r and R[i,c]:R[i]=(R[i]-R[i,c]*R[r])%P
        p.append(c);r+=1
        if r==m:break
    out=[]
    for f in [j for j in range(n) if j not in p]:
        x=np.zeros(n,dtype=np.int64);x[f]=1
        for rr,c in enumerate(p):x[c]=(-R[rr,f])%P
        out.append(x)
    return out

def basis_columns(M,target):
    B=np.empty((M.shape[0],0),dtype=np.int64);r=0
    for j in range(M.shape[1]):
        C=np.column_stack([B,M[:,j]]);q=rank3(C)
        if q>r:
            B=C;r=q
            if r==target:break
    assert r==target;return B

ns=runpy.run_path('research/phase2_1_invariant_space_verification_2026-09-15.py')
ns3=runpy.run_path('research/phase2_3_endH_optimized_2026-09-15.py')
idx=ns['index4'];basis=ns['basis'];gens=ns['gens'];act=ns['apply_linear_map'];N=np.array(ns3['N'],dtype=np.int64)%P

def vec(A):
    v=np.zeros(256,dtype=np.int64)
    for w,c in A.items():v[idx[w]]=c%P
    return v
W=np.column_stack([vec(a) for a in basis]);assert rank3(W)==45

def add(A,B):
    C=dict(A)
    for w,c in B.items():
        C[w]=(C.get(w,0)+c)%P
        if C[w]==0:del C[w]
    return C

def mul(A,B):
    C={}
    for wa,ca in A.items():
        for wb,cb in B.items():
            w=wa+wb;C[w]=(C.get(w,0)+ca*cb)%P
            if C[w]==0:del C[w]
    return C

def neg(A):return {w:(-c)%P for w,c in A.items() if c%P}
def br(A,B):return add(mul(A,B),neg(mul(B,A)))
d=br({(1,1,1):1},{(2,):1})
q=[d];seen={tuple(vec(d).tolist())}
for a in q:
    for g in gens:
        b=act(a,g);k=tuple(vec(b).tolist())
        if k not in seen:seen.add(k);q.append(b)
Wd=basis_columns(np.column_stack([vec(a) for a in q]),45);assert rank3(Wd)==45
S=np.column_stack([W,(-Wd)%P])%P
ker=null3(S);assert len(ker)==35
I=(W@np.column_stack(ker)[:45,:])%P;assert rank3(I)==35
Kcoord=np.column_stack(null3(N));assert Kcoord.shape==(45,35) and rank3(Kcoord)==35
K=(W@Kcoord)%P;assert rank3(K)==35
combined=rank3(np.column_stack([I,K]));actual_equal=(combined==35)
print('A3-4 FAST I/K REVALIDATION')
print('orbit size =',len(q))
print('dim W45 =',rank3(W))
print('dim Wd =',rank3(Wd))
print('rank([W45|Wd]) =',rank3(np.column_stack([W,Wd])))
print('dim I =',rank3(I))
print('dim K =',rank3(K))
print('rank([I|K]) =',combined)
print('I_EQUALS_K =',actual_equal)
assert actual_equal
print('RESULT: I = K as actual ambient degree-4 subspaces.')
print('Since the equality is literal, I is automatically isomorphic to K as an Sp4(F3)-module.')
print('ALL FAST I/K REVALIDATION CHECKS PASSED')
