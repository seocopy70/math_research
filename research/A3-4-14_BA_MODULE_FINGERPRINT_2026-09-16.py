import runpy
import numpy as np
from itertools import product
P=3; ROOT='research/'
ns=runpy.run_path(ROOT+'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
rank3=ns['rank3']; W=np.array(ns['W'],dtype=np.int64)%P; I_W=np.array(ns['I_W'],dtype=np.int64)%P; K_coord=np.array(ns['K_coord'],dtype=np.int64)%P; D_tau=np.array(ns['D'],dtype=np.int64)%P; B_W=ns['B_W']
nsN=runpy.run_path(ROOT+'phase2_3_endH_optimized_2026-09-15.py'); N=np.array(nsN['N'],dtype=np.int64)%P
nsH=runpy.run_path(ROOT+'phase2_1_invariant_space_verification_2026-09-15.py'); gens=nsH['gens']; apply_linear_map=nsH['apply_linear_map']; index4=nsH['index4']; words4=list(index4.keys()); words5=list(product((1,2,3,4),repeat=5)); index5={w:i for i,w in enumerate(words5)}
assert W.shape==(256,45) and I_W.shape==(45,35) and K_coord.shape==(45,35) and D_tau.shape==(4096,45)
assert rank3(W)==45 and rank3(I_W)==35 and rank3(K_coord)==35 and rank3(D_tau)==45 and rank3(N)==10 and np.array_equal((N@N)%P,np.zeros((45,45),dtype=np.int64))

def solve(A,b):
    A=np.array(A,dtype=np.int64)%P; b=np.array(b,dtype=np.int64).reshape(-1)%P; R=np.column_stack([A,b]); m,n1=R.shape; n=n1-1; r=0; piv=[]
    for c in range(n):
        q=next((i for i in range(r,m) if R[i,c]),None)
        if q is None: continue
        R[[r,q]]=R[[q,r]]
        if R[r,c]==2:R[r]=(2*R[r])%P
        for i in range(m):
            if i!=r and R[i,c]:R[i]=(R[i]-R[i,c]*R[r])%P
        piv.append(c); r+=1
        if r==m:break
    for i in range(r,m):
        if np.all(R[i,:n]==0) and R[i,n]!=0:return None
    x=np.zeros(n,dtype=np.int64)
    for rr,c in enumerate(piv):x[c]=R[rr,n]
    return x%P

# H action on W in ambient degree-4 coordinates.  Each transformed W-basis
# vector is solved directly in the W basis; do not solve W*x=e_j for ambient
# standard basis vectors, since most e_j are outside Im(W).
A_W_coord=[]
for g in gens:
    G=np.zeros((256,256),dtype=np.int64)
    for j,w in enumerate(words4):
        out=apply_linear_map({w:1},g)
        for ww,c in out.items():G[index4[ww],j]=(G[index4[ww],j]+c)%P
    cols=[]
    for j in range(45):
        z=solve(W,(G@W[:,j])%P); assert z is not None
        cols.append(z)
    A_W_coord.append(np.array(cols,dtype=np.int64).T%P)
assert all(np.array_equal((A@np.eye(45,dtype=np.int64))%P,A) for A in A_W_coord)

# A=Im Delta_u; complete it by Delta_tau columns to C=[A|Q].
D_u=np.vstack([((np.array(B,dtype=np.int64)@N)%P) for B in B_W]); assert rank3(D_u)==10
A_basis=np.empty((4096,0),dtype=np.int64)
for j in range(D_u.shape[1]):
    c=D_u[:,j:j+1]
    if rank3(np.column_stack([A_basis,c]))>rank3(A_basis):A_basis=np.column_stack([A_basis,c])
assert A_basis.shape==(4096,10)
Q_cols=[]; cur=A_basis
for j in range(D_tau.shape[1]):
    c=D_tau[:,j:j+1]
    if rank3(np.column_stack([cur,c]))>rank3(cur):Q_cols.append(D_tau[:,j]);cur=np.column_stack([cur,c])
    if len(Q_cols)==35:break
Q_basis=np.array(Q_cols,dtype=np.int64).T%P; C=np.column_stack([A_basis,Q_basis])%P
assert C.shape==(4096,45) and rank3(C)==45

# Actual ambient Hom(V,T^5) action.
def gen_matrix(g):
    M=np.zeros((4,4),dtype=np.int64)
    for j in range(1,5):
        out=apply_linear_map({(j,):1},g)
        for ww,c in out.items():
            if len(ww)==1:M[ww[0]-1,j-1]=(M[ww[0]-1,j-1]+c)%P
    return M%P

def tensor5(M):
    T=np.zeros((1024,1024),dtype=np.int64)
    for j,w in enumerate(words5):
        partial={():1}
        for letter in w:
            nxt={}
            for pref,coef in partial.items():
                for out in range(4):
                    a=int(M[out,letter-1])%P
                    if a:nxt[pref+(out+1,)]=(nxt.get(pref+(out+1,),0)+coef*a)%P
            partial=nxt
        for ww,c in partial.items():T[index5[ww],j]=c%P
    return T%P

def hom_action(h,M,T):
    Minv=np.column_stack([solve(M,np.eye(4,dtype=np.int64)[:,j]) for j in range(4)])%P
    blocks=[h[j*1024:(j+1)*1024]%P for j in range(4)]; out=[]
    for j in range(4):
        v=np.zeros(1024,dtype=np.int64)
        for k in range(4):v=(v+int(Minv[k,j])*blocks[k])%P
        out.append((T@v)%P)
    return np.concatenate(out)%P
Mgens=[gen_matrix(g) for g in gens]; T5=[tensor5(M) for M in Mgens]
BA=[]
for M,T in zip(Mgens,T5):
    cols=[]
    for j in range(35):
        z=solve(C,hom_action(Q_basis[:,j],M,T)); assert z is not None; cols.append(z[10:])
    BA.append(np.array(cols,dtype=np.int64).T%P)
assert all(rank3(T)==35 for T in BA)

# K action in the correct 45D W-coordinate system.
K=[]
for A in A_W_coord:
    cols=[]
    for j in range(35):
        z=solve(K_coord,(A@K_coord[:,j])%P); assert z is not None; cols.append(z)
    K.append(np.array(cols,dtype=np.int64).T%P)
assert all(rank3(T)==35 for T in K)

def mat_order(T,max_order=5000):
    R=np.eye(35,dtype=np.int64)
    for k in range(1,max_order+1):
        R=(R@T)%P
        if np.array_equal(R,np.eye(35,dtype=np.int64)):return k
    return None

def minpoly_degree(T,maxdeg=80):
    pw=[np.eye(35,dtype=np.int64)]
    for d in range(1,maxdeg+1):
        pw.append((pw[-1]@T)%P)
        if rank3(np.column_stack([x.reshape(-1) for x in pw]))<len(pw):return d
    return None

def fingerprint(T):
    D=(T-np.eye(35,dtype=np.int64))%P; ranks=[]; R=D.copy()
    for _ in range(35):
        r=rank3(R); ranks.append(r)
        if r==0:break
        R=(R@D)%P
    return {'trace':int(np.trace(T)%P),'order':mat_order(T),'fixed_dim':35-rank3(D),'rank(T-I)':rank3(D),'ranks_powers':ranks,'minpoly_degree':minpoly_degree(T)}

print('A3-4-14 / BA MODULE FINGERPRINT')
print('dim(B/A) =',35); print('dim(K) =',35); print('rank Delta_tau =',rank3(D_tau)); print('rank Delta_u =',rank3(D_u)); print('number of H generators =',len(gens)); print()
all_equal=True
for i,(Tb,Tk) in enumerate(zip(BA,K),1):
    fb=fingerprint(Tb); fk=fingerprint(Tk); eq=(fb==fk); all_equal=all_equal and eq
    print('GENERATOR',i)
    print('  B/A trace =',fb['trace'],' K trace =',fk['trace'])
    print('  B/A order =',fb['order'],' K order =',fk['order'])
    print('  B/A fixed_dim =',fb['fixed_dim'],' K fixed_dim =',fk['fixed_dim'])
    print('  B/A rank(T-I) =',fb['rank(T-I)'],' K rank(T-I) =',fk['rank(T-I)'])
    print('  B/A ranks((T-I)^k) =',fb['ranks_powers'])
    print('  K   ranks((T-I)^k) =',fk['ranks_powers'])
    print('  B/A minpoly degree =',fb['minpoly_degree'],' K minpoly degree =',fk['minpoly_degree'])
    print('  fingerprint_equal =',eq)
print(); print('ALL_GENERATOR_FINGERPRINTS_EQUAL =',all_equal)
if all_equal:print('RESULT: tested generator fingerprints do not distinguish B/A from K; class-level analysis required next.')
else:print('RESULT: B/A and K differ on at least one generator-level representation fingerprint.')
print('NOTE: generator traces alone are not claimed to be the full character table.')
print('ALL A3-4-14 CHECKS COMPLETED')
