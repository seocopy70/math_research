"""Q3-5 execution-grade automatic-transfer and independent q=infinity test.

The q=infinity objects are constructed independently. q=3 data are used only as
canonical reference data for transport comparisons. All compatible rank-10
square-zero N candidates are exhausted over F_3; tau is reconstructed from the
original affine condition A_Wd X=X A_W and X I=K_Wd for each compatible N.
"""
import runpy
import numpy as np
from itertools import product

P=3; DIM=45; ROOT='research/'
WORDS4=list(product(range(1,5),repeat=4)); INDEX4={w:i for i,w in enumerate(WORDS4)}; INDEX4_INV={i:w for i,w in enumerate(WORDS4)}
WORDS5=list(product(range(1,5),repeat=5)); INDEX5={w:i for i,w in enumerate(WORDS5)}


def r3(A):
    A=np.array(A,dtype=np.int64,copy=True)%P
    if A.ndim==1:A=A[:,None]
    m,n=A.shape;r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i,c]),None)
        if p is None:continue
        A[[r,p]]=A[[p,r]]
        if A[r,c]==2:A[r]=(2*A[r])%P
        for i in range(m):
            if i!=r and A[i,c]:A[i]=(A[i]-A[i,c]*A[r])%P
        r+=1
        if r==m:break
    return r


def null3(A):
    A=np.array(A,dtype=np.int64,copy=True)%P;m,n=A.shape;R=A.copy();piv=[];r=0
    for c in range(n):
        p=next((i for i in range(r,m) if R[i,c]),None)
        if p is None:continue
        R[[r,p]]=R[[p,r]]
        if R[r,c]==2:R[r]=(2*R[r])%P
        for i in range(m):
            if i!=r and R[i,c]:R[i]=(R[i]-R[i,c]*R[r])%P
        piv.append(c);r+=1
        if r==m:break
    out=[]
    for f in [j for j in range(n) if j not in piv]:
        x=np.zeros(n,dtype=np.int64);x[f]=1
        for rr,c in enumerate(piv):x[c]=(-R[rr,f])%P
        out.append(x)
    return out


def inv3(A):
    A=np.array(A,dtype=np.int64)%P;n=A.shape[0];R=np.column_stack([A,np.eye(n,dtype=np.int64)])
    for c in range(n):
        p=next((i for i in range(c,n) if R[i,c]),None)
        if p is None:raise ValueError('singular')
        R[[c,p]]=R[[p,c]]
        if R[c,c]==2:R[c]=(2*R[c])%P
        for i in range(n):
            if i!=c and R[i,c]:R[i]=(R[i]-R[i,c]*R[c])%P
    return R[:,n:]


def solve_affine(A,b):
    A=np.array(A,dtype=np.int64)%P;b=np.array(b,dtype=np.int64).reshape(-1)%P;m,n=A.shape;R=np.column_stack([A,b]);r=0;piv=[]
    for c in range(n):
        p=next((i for i in range(r,m) if R[i,c]),None)
        if p is None:continue
        R[[r,p]]=R[[p,r]]
        if R[r,c]==2:R[r]=(2*R[r])%P
        for i in range(m):
            if i!=r and R[i,c]:R[i]=(R[i]-R[i,c]*R[r])%P
        piv.append(c);r+=1
        if r==m:break
    if any(np.all(R[i,:n]==0) and R[i,n]!=0 for i in range(r,m)):return None,[],None
    x=np.zeros(n,dtype=np.int64)
    for rr,c in enumerate(piv):x[c]=R[rr,n]
    free=[c for c in range(n) if c not in piv];ker=[]
    for f in free:
        z=np.zeros(n,dtype=np.int64);z[f]=1
        for rr,c in enumerate(piv):z[c]=(-R[rr,f])%P
        ker.append(z)
    return x,ker,len(free)


def hom_basis(G,H):
    n=G[0].shape[0];cols=[]
    for q in range(n*n):
        X=np.zeros((n,n),dtype=np.int64);X.flat[q]=1
        cols.append(np.concatenate([((X@a-b@X)%P).reshape(-1) for a,b in zip(G,H)]))
    return null3(np.column_stack(cols))


def vec4(a):
    v=np.zeros(256,dtype=np.int64)
    for w,c in a.items():v[INDEX4[w]]=c%P
    return v


def col_basis(M,target):
    B=np.empty((M.shape[0],0),dtype=np.int64);rr=0
    for j in range(M.shape[1]):
        C=np.column_stack([B,M[:,j]])
        q=r3(C)
        if q>rr:B=C;rr=q
        if rr==target:break
    assert rr==target;return B


def coords_from(B,V):
    rows=[];R=np.empty((0,B.shape[1]),dtype=np.int64);rr=0
    for i in range(B.shape[0]):
        C=np.vstack([R,B[i:i+1]]);q=r3(C)
        if q>rr:rows.append(i);R=C;rr=q
        if rr==B.shape[1]:break
    L=inv3(B[rows,:]);return (L@np.array(V,dtype=np.int64)[rows,:])%P


def affine_tau(A_src,A_tgt,I,K):
    n=45;rows=[];rhs=[]
    vi=lambda r,c:r*n+c
    for A,B in zip(A_src,A_tgt):
        for r in range(n):
            for c in range(n):
                row=np.zeros(n*n,dtype=np.int64)
                for k in range(n):
                    row[vi(k,c)]=(row[vi(k,c)]+B[r,k])%P
                    row[vi(r,k)]=(row[vi(r,k)]-A[k,c])%P
                rows.append(row);rhs.append(0)
    for r in range(n):
        for c in range(I.shape[1]):
            row=np.zeros(n*n,dtype=np.int64)
            for k in range(n):row[vi(r,k)]=(row[vi(r,k)]+I[k,c])%P
            rows.append(row);rhs.append(int(K[r,c]))
    return solve_affine(np.array(rows),np.array(rhs))


def ambient_generator_matrices(gens,apply):
    out=[]
    for g in gens:
        G=np.zeros((256,256),dtype=np.int64)
        for j,w in enumerate(WORDS4):
            d=apply({w:1},g)
            for ww,c in d.items():G[INDEX4[ww],j]=(G[INDEX4[ww],j]+c)%P
        out.append(G)
    return out


def bracket_col(v,gen):
    out=np.zeros(1024,dtype=np.int64)
    for j,c in enumerate(v):
        c=int(c)%P
        if not c:continue
        w=WORDS4[j]
        out[INDEX5[w+(gen,)]]=(out[INDEX5[w+(gen,)]]+c)%P
        out[INDEX5[(gen,)+w]]=(out[INDEX5[(gen,)+w]]-c)%P
    return out


def delta_u(W,N):
    return np.column_stack([np.concatenate([bracket_col((W@N[:,j])%P,g) for g in range(1,5)]) for j in range(45)])%P


def delta_tau(W,Wd,tau):
    return np.column_stack([np.concatenate([bracket_col((Wd@tau[:,j]-W[:,j])%P,g) for g in range(1,5)]) for j in range(45)])%P

# Independent Gate-0A modules and genuine H-intertwiner T.
gate=runpy.run_path(ROOT+'GATE0A_Q3_QINF_INDEPENDENT_W45_2026-09-17.py')
A3=[np.array(x,dtype=np.int64)%P for x in gate['q3']['actions']];Ai=[np.array(x,dtype=np.int64)%P for x in gate['qinf']['actions']]
H=hom_basis(A3,Ai);assert len(H)==2
Tlist=[x.reshape(45,45)%P for x in H if r3(x.reshape(45,45))==45];assert Tlist
T=Tlist[0];Ti=inv3(T)

# Exhaust all End_H(q=infinity) elements over F_3.
Ei=hom_basis(Ai,Ai);E3=hom_basis(A3,A3);assert len(Ei)==len(E3)==2
all_E=[(a*Ei[0].reshape(45,45)+b*Ei[1].reshape(45,45))%P for a,b in product(range(3),repeat=2)]
Ninf_all=[X for X in all_E if r3(X)==10 and np.array_equal((X@X)%P,np.zeros((45,45),dtype=np.int64))]
assert Ninf_all

# q3 canonical N/tau are stored in the phase2_18 coordinate system. Convert them
# explicitly into the independent Gate-0A q3 coordinate system before transport.
ns18=runpy.run_path(ROOT+'phase2_18_A3_4_5_intersection_K_and_Sym2_2026-09-16.py')
W18=np.array(ns18['W'],dtype=np.int64)%P;Wd18=np.array(ns18['Wd_basis'],dtype=np.int64)%P
N18=np.array(runpy.run_path(ROOT+'phase2_3_endH_optimized_2026-09-15.py')['N'],dtype=np.int64)%P
ns23=runpy.run_path(ROOT+'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py');tau18=np.array(ns23['X_intertwiner'],dtype=np.int64)%P
W3=np.column_stack([vec4(a) for a in gate['q3']['basis']])%P
Wd=col_basis(np.column_stack([vec4(a) for a in gate['q3']['basis'][:0]]) if False else np.zeros((256,0),dtype=np.int64),0) if False else None
# The Wd orbit is common to q3/qinf because d and the H action are the same ambient data.
gens=gate['gens'];apply=gate['apply_linear_map'];A4=ambient_generator_matrices(gens,apply)
d=np.zeros(256,dtype=np.int64);d[INDEX4[(1,1,1,2)]]=1;d[INDEX4[(2,1,1,1)]]=2
Q=[d];seen={tuple(d.tolist())}
for a in Q:
    dd={INDEX4_INV[i]:int(c) for i,c in enumerate(a) if int(c)%P}
    for g in gens:
        out=apply(dd,g);b=np.zeros(256,dtype=np.int64)
        for w,c in out.items():b[INDEX4[w]]=c%P
        k=tuple(b.tolist())
        if k not in seen:seen.add(k);Q.append(b)
Wd=col_basis(np.column_stack(Q),45);assert r3(Wd)==45

# Coordinate changes from the original q3 construction to Gate-0A coordinates.
Csrc=coords_from(W3,W18)       # W18 = W3*Csrc
Ctgt=coords_from(Wd,Wd18)      # Wd18 = Wd*Ctgt
assert np.array_equal((W3@Csrc)%P,W18)
assert np.array_equal((Wd@Ctgt)%P,Wd18)
N3=(Csrc@N18@inv3(Csrc))%P
tau3_gate=(Ctgt@tau18@inv3(Csrc))%P
# Canonically transported tau target is Ctgt*tau18*Csrc^-1, then T^-1 on source.
tau_transport=(Ctgt@tau18@inv3(Csrc)@Ti)%P
NT=(T@N3@Ti)%P
N_compatible=[X for X in Ninf_all if np.array_equal(X,NT) or np.array_equal(X,(-NT)%P)]

# q=infinity Wd action and W/I intersection, built independently.
Wi=np.column_stack([vec4(a) for a in gate['qinf']['basis']])%P
Awd=[]
for G in A4:
    Y=(G@Wd)%P
    Awd.append(coords_from(Wd,Y))
Iker=null3(np.column_stack([Wi,(-Wd)%P]));assert len(Iker)==35
Iamb=(Wi@np.column_stack([z[:45] for z in Iker]))%P
Iinf=coords_from(Wi,Iamb);assert r3(Iinf)==35

# For each compatible N, reconstruct every affine tau candidate independently.
case_records=[]
for ni,Ninf in enumerate(N_compatible):
    Kcoord=np.column_stack(null3(Ninf));assert Kcoord.shape==(45,35)
    Kamb=(Wi@Kcoord)%P;Kwd=coords_from(Wd,Kamb)
    sol,ker,nullity=affine_tau(Ai,Awd,Iinf,Kwd);assert sol is not None
    candidates=[]
    if nullity<=8:
        base=sol.reshape(45,45)%P
        for coeffs in product(range(3),repeat=nullity):
            z=base.reshape(-1).copy()
            for c,v in zip(coeffs,ker):z=(z+c*v)%P
            candidates.append(z.reshape(45,45)%P)
    case_records.append((Ninf,nullity,candidates))

# q3 reference images, now all expressed in Gate-0A/common ambient coordinates.
A3mat=delta_u(W3,N3);B3mat=delta_tau(W3,Wd,tau3_gate)
rankA3=r3(A3mat);rankB3=r3(B3mat)

results=[]
for ni,(Ninf,nullity,tcs) in enumerate(case_records):
    for ti,tau in enumerate(tcs):
        Ainf=delta_u(Wi,Ninf);Binf=delta_tau(Wi,Wd,tau)
        ra,rb=r3(Ainf),r3(Binf)
        nested=(r3(np.column_stack([Binf,Ainf]))==rb)
        quotient=(rb-ra) if nested else None
        results.append({'n':ni,'tau':ti,'tau_transport':np.array_equal(tau,tau_transport),
                        'A_rank':ra,'B_rank':rb,'nested':nested,'quotient':quotient,
                        'A_same_as_q3':r3(np.column_stack([Ainf,A3mat]))==ra==rankA3,
                        'B_same_as_q3':r3(np.column_stack([Binf,B3mat]))==rb==rankB3})

print('Q3-5 EXECUTION-GRADE AUTO-TRANSFER + INDEPENDENT QINF')
print('Gate0A Hom dimension =',len(H),'invertible =',len(Tlist))
print('End_H(q3) =',len(E3),'End_H(qinf) =',len(Ei))
print('qinf rank-10 square-zero candidates among all 9 =',len(Ninf_all))
print('N_AUTO_TRANSFER =',bool(N_compatible),'compatible N candidates =',len(N_compatible))
print('dim I_inf =',r3(Iinf))
print('q3 ranks: A3 =',rankA3,'B3 =',rankB3,'B3/A3 =',rankB3-rankA3)
for i,(Ninf,nullity,tcs) in enumerate(case_records):print('N_CASE',i,'tau_affine_nullity =',nullity,'tau_candidates_exhausted =',len(tcs))
for x in results:print('CASE',x)

if not N_compatible:
    RESULT='N TRANSFER NOT FORCED: no qinf rank-10 square-zero candidate matches transported N'
elif any(nullity>8 for _,nullity,_ in case_records):
    RESULT='INCONCLUSIVE: tau affine candidate set too large to exhaust safely'
else:
    nonnested=[x for x in results if not x['nested']]
    diffshape=[x for x in results if x['nested'] and x['quotient']!=35]
    q36=[x for x in results if x['nested'] and x['quotient']==35]
    if nonnested:RESULT='STRUCTURE EXISTS, NON-NESTED'
    elif diffshape:RESULT='STRUCTURE EXISTS, DIFFERENT SHAPE'
    elif q36:RESULT='NESTED + QUOTIENT 35: PROCEED Q3-6'
    else:RESULT='DEGREE-4 TRACK POWERLESS: all tested data forced identical'
print('RESULT =',RESULT)
