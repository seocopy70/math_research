import numpy as np
from itertools import product

P=3; D4=256
WORDS=list(product(range(1,5),repeat=4)); IDX={w:i for i,w in enumerate(WORDS)}

def add(A,B):
    C=dict(A)
    for w,c in B.items():
        C[w]=(C.get(w,0)+c)%P
        if C[w]==0: del C[w]
    return C

def mul(A,B):
    C={}
    for a,ca in A.items():
        for b,cb in B.items():
            w=a+b; C[w]=(C.get(w,0)+ca*cb)%P
            if C[w]==0: del C[w]
    return C

def neg(A): return {w:(-c)%P for w,c in A.items() if c%P}
def br(A,B): return add(mul(A,B),neg(mul(B,A)))

def vec(A):
    v=np.zeros(D4,dtype=np.int64)
    for w,c in A.items(): v[IDX[w]]=c%P
    return v

def rank3(A):
    A=np.array(A,dtype=np.int64,copy=True)%P
    if A.ndim==1:A=A[:,None]
    m,n=A.shape;r=0
    for c in range(n):
        q=next((i for i in range(r,m) if A[i,c]),None)
        if q is None:continue
        A[[r,q]]=A[[q,r]]
        if A[r,c]==2:A[r]=(2*A[r])%P
        for i in range(m):
            if i!=r and A[i,c]:A[i]=(A[i]-A[i,c]*A[r])%P
        r+=1
        if r==m:break
    return r

def null3(A):
    A=np.array(A,dtype=np.int64,copy=True)%P;m,n=A.shape;r=0;piv=[]
    for c in range(n):
        q=next((i for i in range(r,m) if A[i,c]),None)
        if q is None:continue
        A[[r,q]]=A[[q,r]]
        if A[r,c]==2:A[r]=(2*A[r])%P
        for i in range(m):
            if i!=r and A[i,c]:A[i]=(A[i]-A[i,c]*A[r])%P
        piv.append(c);r+=1
    free=[c for c in range(n) if c not in piv]
    Z=np.zeros((n,len(free)),dtype=np.int64)
    for j,f in enumerate(free):
        Z[f,j]=1
        for rr,c in enumerate(piv):Z[c,j]=(-A[rr,f])%P
    return Z

def amap(A,g):
    imgs=[]
    for j in range(4):
        imgs.append({(i+1,):int(g[i,j])%P for i in range(4) if int(g[i,j])%P})
    out={}
    for w,co in A.items():
        cur={():co}
        for x in w:cur=mul(cur,imgs[x-1])
        out=add(out,cur)
    return out

def trans(v):
    J=np.array([[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]],dtype=np.int64)%P
    v=np.array(v,dtype=np.int64)%P
    return (np.eye(4,dtype=np.int64)+np.outer(v,(J@v)%P))%P

def indep(M,target):
    B=np.empty((M.shape[0],0),dtype=np.int64);r=0
    for j in range(M.shape[1]):
        C=np.column_stack([B,M[:,j]]);q=rank3(C)
        if q>r:B=C;r=q
        if r==target:break
    assert r==target;return B

def orbit(seed,gens,target,mod):
    B=mod.copy();out=[];Q=[seed];seen=set()
    while Q:
        a=Q.pop(0);k=tuple(vec(a).tolist())
        if k in seen:continue
        seen.add(k);C=np.column_stack([B,vec(a)])
        if rank3(C)>rank3(B):
            B=C;out.append(a)
            if len(out)==target:break
        Q.extend(amap(a,g) for g in gens)
    assert len(out)==target;return out

X=[{(i,):1} for i in range(1,5)]
L2=[br(X[i],X[j]) for i in range(4) for j in range(i+1,4)]
R=add(L2[0],L2[5]);R3=[br(x,R) for x in X];R4=[br(x,r) for x in R3 for r in X]
R4M=np.column_stack([vec(a) for a in R4]);assert rank3(R4M)==15
G=[trans(v) for v in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(1,0,1,0)]]
T=br(br(br(X[2],X[3]),X[0]),X[0]);d=br({(1,1,1):1},{(2,):1})
W=np.column_stack([vec(a) for a in orbit(T,G,45,R4M)])
O=[d];seen={tuple(vec(d).tolist())}
for a in O:
    for g in G:
        b=amap(a,g);k=tuple(vec(b).tolist())
        if k not in seen:seen.add(k);O.append(b)
assert len(O)==360
Wd=indep(np.column_stack([vec(a) for a in O]),45)
assert rank3(W)==45 and rank3(Wd)==45

# Quotient action on W: coordinates in [R4_ind | W], then take the W block.
R4i=indep(R4M,15);QB=np.column_stack([R4i,W]);assert rank3(QB)==60
rows=[];M=np.empty((0,60),dtype=np.int64);rr=0
for i in range(256):
    C=np.vstack([M,QB[i:i+1]])
    q=rank3(C)
    if q>rr:rows.append(i);M=C;rr=q
    if rr==60:break
assert len(rows)==60

def inv3(A):
    n=A.shape[0];M=np.concatenate([A%P,np.eye(n,dtype=np.int64)],axis=1)
    for c in range(n):
        q=next(i for i in range(c,n) if M[i,c]);M[[c,q]]=M[[q,c]]
        if M[c,c]==2:M[c]=(2*M[c])%P
        for i in range(n):
            if i!=c and M[i,c]:M[i]=(M[i]-M[i,c]*M[c])%P
    return M[:,n:]
Qi=inv3(QB[rows]);qco=lambda v:(Qi@(v[rows]%P))%P
AW=[]
for g in G:
    cols=[]
    for j in range(45):
        a={w:int(c) for w,c in zip(WORDS,W[:,j]) if int(c)%P}
        cols.append(qco(vec(amap(a,g)))[15:])
    AW.append(np.column_stack(cols)%P)
AW=np.stack(AW)

# Reconstruct End_H(W) and the historical N independently.
B=(AW[1]+AW[2]+AW[3]+AW[4])%P;pows=[];cur=np.eye(45,dtype=np.int64)
for _ in range(45):pows.append(cur.copy());cur=(cur@B)%P
assert rank3(np.column_stack([p.reshape(-1) for p in pows]))==45
C=[]
for A in AW:C.append(np.column_stack([((p@A-A@p)%P).reshape(-1) for p in pows]))
Z=null3(np.vstack(C));assert Z.shape[1]==2
EB=[]
for j in range(2):
    E=np.zeros((45,45),dtype=np.int64)
    for t,p in enumerate(pows):E=(E+int(Z[t,j])*p)%P
    EB.append(E)
N=None
for a in range(3):
    for b in range(3):
        if a==0 and b==0:continue
        E=(a*EB[0]+b*EB[1])%P
        if rank3(E)==10 and np.array_equal((E@E)%P,np.zeros((45,45),dtype=np.int64)):N=E;break
    if N is not None:break
assert N is not None
KN=null3(N);assert KN.shape==(45,35) and rank3(KN)==35

# I=W intersect Wd, in W and Wd coordinates.
Zint=null3(np.column_stack([W,(-Wd)%P]));assert Zint.shape[1]==35
IW=Zint[:45]%P;IWd=Zint[45:]%P
Iamb=(W@IW)%P;assert rank3(Iamb)==35
aug=rank3(np.column_stack([KN,IW]));equal=(aug==35)

print('A3-4 N-K-I DIAGNOSTIC')
print('dim W =',rank3(W));print('dim Wd =',rank3(Wd));print('dim I =',rank3(Iamb))
print('Krylov rank =',rank3(np.column_stack([p.reshape(-1) for p in pows])))
print('dim End_H(W) =',Z.shape[1]);print('rank N =',rank3(N));print('dim ker N =',KN.shape[1]);print('N^2=0 =',True)
print('rank [K_N | I_W] =',aug);print('K_N = I =',equal)
print('DIAGNOSTIC PASS =', all([rank3(W)==45,rank3(Wd)==45,rank3(Iamb)==35,rank3(np.column_stack([p.reshape(-1) for p in pows]))==45,Z.shape[1]==2,rank3(N)==10,KN.shape[1]==35,aug==35]))
