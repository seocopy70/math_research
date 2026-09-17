"""Q3-5 execution-grade automatic-transfer and independent q=infinity test.

Purpose
-------
Determine whether the A3-4 degree-4 filtration data are genuinely q-sensitive,
without importing q=3 A/B data into the q=infinity construction.

The script exhausts all End_H candidates over F_3 for rank-10 square-zero N,
reconstructs tau independently from the original affine condition
    A_Wd X = X A_W,   X I = K_Wd,
and then computes A=Im Delta_u and B=Im Delta_tau independently for q=infinity.
If the affine tau system has more than a small finite solution set, the script
reports that it cannot exhaust it rather than selecting an arbitrary candidate.
"""
import runpy
import numpy as np
from itertools import product

P=3; NGEN=4; DIM=45
ROOT='research/'


def r3(A):
    A=np.array(A,dtype=np.int64,copy=True)%P
    if A.ndim==1:A=A[:,None]
    m,n=A.shape;r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i,c]),None)
        if p is None: continue
        A[[r,p]]=A[[p,r]]
        if A[r,c]==2:A[r]=(2*A[r])%P
        for i in range(m):
            if i!=r and A[i,c]:A[i]=(A[i]-A[i,c]*A[r])%P
        r+=1
        if r==m:break
    return r


def null3(A):
    A=np.array(A,dtype=np.int64,copy=True)%P
    m,n=A.shape;R=A.copy();piv=[];r=0
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
    A=np.array(A,dtype=np.int64)%P;n=A.shape[0]
    R=np.column_stack([A,np.eye(n,dtype=np.int64)])
    for c in range(n):
        p=next((i for i in range(c,n) if R[i,c]),None)
        if p is None:raise ValueError('singular matrix')
        R[[c,p]]=R[[p,c]]
        if R[c,c]==2:R[c]=(2*R[c])%P
        for i in range(n):
            if i!=c and R[i,c]:R[i]=(R[i]-R[i,c]*R[c])%P
    return R[:,n:]


def solve_linear(A,b):
    A=np.array(A,dtype=np.int64)%P;b=np.array(b,dtype=np.int64).reshape(-1)%P
    R=np.column_stack([A,b]);m,n= A.shape;r=0;piv=[]
    for c in range(n):
        p=next((i for i in range(r,m) if R[i,c]),None)
        if p is None:continue
        R[[r,p]]=R[[p,r]]
        if R[r,c]==2:R[r]=(2*R[r])%P
        for i in range(m):
            if i!=r and R[i,c]:R[i]=(R[i]-R[i,c]*R[r])%P
        piv.append(c);r+=1
        if r==m:break
    if any(np.all(R[i,:n]==0) and R[i,n]!=0 for i in range(r,m)):
        return None,[],n-r
    x=np.zeros(n,dtype=np.int64)
    for rr,c in enumerate(piv):x[c]=R[rr,n]
    free=[c for c in range(n) if c not in piv]
    basis=[]
    for f in free:
        z=np.zeros(n,dtype=np.int64);z[f]=1
        for rr,c in enumerate(piv):z[c]=(-R[rr,f])%P
        basis.append(z)
    return x,basis,n-r


def hom_basis(G,H):
    n=G[0].shape[0];cols=[]
    for q in range(n*n):
        T=np.zeros((n,n),dtype=np.int64);T.flat[q]=1
        cols.append(np.concatenate([((T@a-b@T)%P).reshape(-1) for a,b in zip(G,H)]))
    return null3(np.column_stack(cols))


def independent_columns(M):
    M=np.array(M,dtype=np.int64)%P;B=np.empty((M.shape[0],0),dtype=np.int64);rr=0
    for j in range(M.shape[1]):
        C=np.column_stack([B,M[:,j]])
        q=r3(C)
        if q>rr:B=C;rr=q
        if rr==M.shape[0]:break
    return B


def vec4(a,index4):
    v=np.zeros(256,dtype=np.int64)
    for w,c in a.items():v[index4[w]]=c%P
    return v


def ambient_basis_and_coords(R4,basis):
    R4i=independent_columns(R4)
    B=np.column_stack([R4i,np.column_stack([vec4(a,INDEX4) for a in basis])])
    assert r3(B)==60
    rows=[];R=np.empty((0,60),dtype=np.int64);rr=0
    for i in range(256):
        C=np.vstack([R,B[i:i+1]])
        q=r3(C)
        if q>rr:rows.append(i);R=C;rr=q
        if rr==60:break
    Binv=inv3(B[rows,:])
    def coords(V):
        V=np.array(V,dtype=np.int64)%P
        return (Binv@(V[rows]))[15:,:]%P
    W=np.column_stack([vec4(a,INDEX4) for a in basis])%P
    return W,coords


def build_Wd(gens,apply,index4):
    d=np.zeros(256,dtype=np.int64)
    d[index4[(1,1,1,2)]]=1
    d[index4[(2,1,1,1)]]=2
    seen={tuple(d.tolist())};Q=[d]
    for a in Q:
        for g in gens:
            b=np.array(apply({w:int(c) for w,c in []},g) if False else a,dtype=np.int64)
            # Apply the linear map through the ambient matrix induced by g.
            # Reuse apply on a sparse word dictionary.
            dd={INDEX4_INV[i]:int(c) for i,c in enumerate(a) if int(c)%P}
            out=apply(dd,g);b=np.zeros(256,dtype=np.int64)
            for w,c in out.items():b[index4[w]]=c%P
            k=tuple(b.tolist())
            if k not in seen:seen.add(k);Q.append(b)
    M=np.column_stack(Q)%P
    assert len(Q)==360 and r3(M)==45
    return independent_columns(M),M


def intersection_coords(W,U):
    K=null3(np.column_stack([W,(-U)%P]))
    assert len(K)==35
    Iamb=(W@np.column_stack([x[:45] for x in K]))%P
    # W has 45 independent columns; coordinate extraction by pivot rows.
    rows=[];R=np.empty((0,45),dtype=np.int64);rr=0
    for i in range(256):
        C=np.vstack([R,W[i:i+1]])
        q=r3(C)
        if q>rr:rows.append(i);R=C;rr=q
        if rr==45:break
    L=inv3(W[rows,:])
    return (L@Iamb[rows,:])%P,Iamb


def restricted_action(A,Wsub,ambient_W):
    rows=[];R=np.empty((0,Wsub.shape[1]),dtype=np.int64);rr=0
    for i in range(Wsub.shape[0]):
        C=np.vstack([R,Wsub[i:i+1]])
        q=r3(C)
        if q>rr:rows.append(i);R=C;rr=q
        if rr==Wsub.shape[1]:break
    L=inv3(Wsub[rows,:]);out=[]
    for A0 in A:
        Y=(Wsub@A0)%P
        out.append((L@Y[rows,:])%P)
    return out


def affine_tau(A_src,A_tgt,I,K):
    n=A_src[0].shape[0];rows=[];rhs=[]
    def vi(r,c):return r*n+c
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
    sol,ker,nullity=solve_linear(np.array(rows),np.array(rhs))
    return sol,ker,nullity


def bracket_col(v,gen):
    out=np.zeros(1024,dtype=np.int64)
    for j,c in enumerate(v):
        c=int(c)%P
        if not c:continue
        w=WORDS4[j]
        out[INDEX5[w+(gen,)]]=(out[INDEX5[w+(gen,)]]+c)%P
        out[INDEX5[(gen,)+w]]=(out[INDEX5[(gen,)+w]]-c)%P
    return out


def delta_u(W,Nmat):
    cols=[]
    for j in range(45):
        z=(W@Nmat[:,j])%P
        cols.append(np.concatenate([bracket_col(z,g) for g in range(1,5)]))
    return np.column_stack(cols)%P


def delta_tau(W,Wd,tau):
    cols=[]
    for j in range(45):
        z=(Wd@tau[:,j]-W[:,j])%P
        cols.append(np.concatenate([bracket_col(z,g) for g in range(1,5)]))
    return np.column_stack(cols)%P


# Ambient free associative word indexing (used only for degree-4/5 bracket maps).
WORDS4=list(product(range(1,5),repeat=4));INDEX4={w:i for i,w in enumerate(WORDS4)};INDEX4_INV={i:w for i,w in enumerate(WORDS4)}
WORDS5=list(product(range(1,5),repeat=5));INDEX5={w:i for i,w in enumerate(WORDS5)}

# Gate-0A is independent q3/q-infinity construction. It supplies two separately
# built Q4 modules, not q3 A/B data.
gate=runpy.run_path(ROOT+'GATE0A_Q3_QINF_INDEPENDENT_W45_2026-09-17.py')
A3=[np.array(a,dtype=np.int64)%P for a in gate['q3']['actions']]
Ai=[np.array(a,dtype=np.int64)%P for a in gate['qinf']['actions']]
H=hom_basis(A3,Ai)
assert len(H)==2
Tlist=[]
for x in H:
    M=x.reshape(45,45)%P
    if r3(M)==45:Tlist.append(M)
assert Tlist
T=Tlist[0];Ti=inv3(T)

# Exhaust all 9 End_H elements, not just basis vectors.
E3=hom_basis(A3,A3);Ei=hom_basis(Ai,Ai)
assert len(E3)==2 and len(Ei)==2
all_Ei=[]
for a,b in product(range(3),repeat=2):
    all_Ei.append((a*Ei[0].reshape(45,45)+b*Ei[1].reshape(45,45))%P)
Ninf_all=[X for X in all_Ei if r3(X)==10 and np.array_equal((X@X)%P,np.zeros((45,45),dtype=np.int64))]
assert Ninf_all
N3=np.array(runpy.run_path(ROOT+'phase2_3_endH_optimized_2026-09-15.py')['N'],dtype=np.int64)%P
NT=(T@N3@Ti)%P
N_compatible=[X for X in Ninf_all if np.array_equal(X,NT) or np.array_equal(X,(-NT)%P)]
N_auto=bool(N_compatible)

# Independently construct the common Wd ambient module and its q=infinity coordinates.
gens=gate['gens'];apply=gate['apply_linear_map']
Wd, Wd_orbit=build_Wd(gens,apply,INDEX4)
W3,_=ambient_basis_and_coords(gate['q3']['R4'],gate['q3']['basis'])
Wi,_=ambient_basis_and_coords(gate['qinf']['R4'],gate['qinf']['basis'])
assert r3(W3)==r3(Wi)==45 and r3(Wd)==45

# q3 canonical tau is used only as a reference for the transport test; q=infinity
# tau is reconstructed below independently from its own W/I/K data.
ns23=runpy.run_path(ROOT+'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
tau3=np.array(ns23['X_intertwiner'],dtype=np.int64)%P
Wd3=np.array(ns23['Wd'],dtype=np.int64)%P if 'Wd' in ns23 else Wd
# Build the canonical target-coordinate change S from q3 Wd coordinates to the
# common ambient Wd basis. phase2_23 uses the same deterministic Wd basis, but S
# is computed explicitly rather than assumed to be identity.
S=np.column_stack([np.array([],dtype=np.int64)]) if False else None
# q3 Wd basis exported by phase2_18 is the same deterministic basis used here.
ns18=runpy.run_path(ROOT+'phase2_18_A3_4_5_intersection_K_and_Sym2_2026-09-16.py')
Wd3=np.array(ns18['Wd_basis'],dtype=np.int64)%P
# S satisfies Wd @ S = Wd3.
rows=[];R=np.empty((0,45),dtype=np.int64);rr=0
for i in range(256):
    C=np.vstack([R,Wd[i:i+1]])
    q=r3(C)
    if q>rr:rows.append(i);R=C;rr=q
    if rr==45:break
S=(inv3(Wd[rows,:])@Wd3[rows,:])%P
assert np.array_equal((Wd@S)%P,Wd3)
tau_transport=(S@tau3@Ti)%P

# q=infinity I and affine tau candidates for every compatible N.
Iinf,Iamb=intersection_coords(Wi,Wd)
assert Iinf.shape==(45,35) and r3(Iinf)==35
Awd_inf=restricted_action([gate['gens'][0] if False else np.eye(45,dtype=np.int64) for _ in range(5)],Wd,Wd) if False else None
# Wd action is obtained directly from ambient generator action, then restricted to Wd.
A4=[]
for g in gens:
    G=np.zeros((256,256),dtype=np.int64)
    for j,w in enumerate(WORDS4):
        out=apply({w:1},g)
        for ww,c in out.items():G[INDEX4[ww],j]=(G[INDEX4[ww],j]+c)%P
    A4.append(G)
Awd_inf=[]
for G in A4:
    Y=(G@Wd)%P
    rows=[];R=np.empty((0,45),dtype=np.int64);rr=0
    for i in range(256):
        C=np.vstack([R,Wd[i:i+1]])
        q=r3(C)
        if q>rr:rows.append(i);R=C;rr=q
        if rr==45:break
    Awd_inf.append((inv3(Wd[rows,:])@Y[rows,:])%P)

# Every compatible N candidate gives its own K and affine tau solution set.
case_records=[]
for ni,Ninf in enumerate(N_compatible):
    K=null3(Ninf);Kcoord=np.column_stack(K);assert Kcoord.shape==(45,35)
    Kamb=(Wi@Kcoord)%P
    rows=[];R=np.empty((0,45),dtype=np.int64);rr=0
    for i in range(256):
        C=np.vstack([R,Wd[i:i+1]])
        q=r3(C)
        if q>rr:rows.append(i);R=C;rr=q
        if rr==45:break
    Kwd=(inv3(Wd[rows,:])@Kamb[rows,:])%P
    sol,ker,nullity=affine_tau(Ai,Awd_inf,Iinf,Kwd)
    assert sol is not None
    tau0=sol.reshape(45,45)%P
    tau_candidates=[]
    if nullity<=8:
        for coeffs in product(range(3),repeat=nullity):
            flat=tau0.copy().reshape(-1)
            for c,z in zip(coeffs,ker):flat=(flat+c*z)%P
            tau_candidates.append(flat.reshape(45,45)%P)
    else:
        tau_candidates=[]
    case_records.append((Ninf,Kcoord,Kwd,nullity,tau_candidates))

# Compute q3 A/B and each independently reconstructed q=infinity A/B.
N3mat=N3
A3mat=delta_u(W3,N3mat)
tau3_check=tau3
B3mat=delta_tau(W3,Wd3,tau3_check)
rank_A3=r3(A3mat);rank_B3=r3(B3mat)

final_cases=[]
for ni,(Ninf,Kcoord,Kwd,nullity,tau_candidates) in enumerate(case_records):
    if nullity>8:
        final_cases.append({'n':ni,'tau_exhausted':False})
        continue
    for ti,tau in enumerate(tau_candidates):
        Ainf=delta_u(Wi,Ninf)
        Binf=delta_tau(Wi,Wd,tau)
        ra,rb=r3(Ainf),r3(Binf)
        # Inclusion A_inf <= B_inf is tested in the actual common degree-5 ambient space.
        nested=r3(np.column_stack([Binf,Ainf]))==rb
        quotient=rb-ra if nested else None
        # Exact transport checks are separate from the classification outcome.
        A_transport=np.array_equal((Ainf@np.eye(45,dtype=np.int64))%P,Ainf) if False else r3(np.column_stack([Ainf,A3mat]))==ra==rank_A3
        B_transport=r3(np.column_stack([Binf,B3mat]))==rb==rank_B3
        tau_transport_ok=np.array_equal(tau,tau_transport)
        final_cases.append({'n':ni,'tau':ti,'tau_exhausted':True,'tau_transport':tau_transport_ok,
                            'A_rank':ra,'B_rank':rb,'nested':nested,'quotient':quotient,
                            'A_same_as_q3':A_transport,'B_same_as_q3':B_transport})

print('Q3-5 EXECUTION-GRADE AUTO-TRANSFER + INDEPENDENT QINF')
print('Gate0A Hom dimension =',len(H))
print('Gate0A invertible intertwiners found =',len(Tlist))
print('End_H(q3) dimension =',len(E3))
print('End_H(qinf) dimension =',len(Ei))
print('qinf rank-10 square-zero candidates among all 9 End elements =',len(Ninf_all))
print('N_AUTO_TRANSFER =',N_auto)
print('N_COMPATIBLE_CANDIDATES =',len(N_compatible))
print('dim I_inf =',r3(Iinf))
print('q3 ranks: A3 =',rank_A3,'B3 =',rank_B3,'B3/A3 =',rank_B3-rank_A3)
for i,(Ninf,Kcoord,Kwd,nullity,tcs) in enumerate(case_records):
    print('N_CASE',i,'tau_affine_nullity =',nullity,'tau_candidates_exhausted =',len(tcs))
for rec in final_cases:print('CASE',rec)

if not N_compatible:
    RESULT='N TRANSFER NOT FORCED: no qinf rank-10 square-zero candidate matches transported N'
elif any(not c.get('tau_exhausted',False) for c in final_cases):
    RESULT='INCONCLUSIVE: tau candidate set too large to exhaust safely'
else:
    nonnested=[c for c in final_cases if not c['nested']]
    diffshape=[c for c in final_cases if c['nested'] and c['quotient']!=35]
    q36=[c for c in final_cases if c['nested'] and c['quotient']==35]
    if nonnested: RESULT='STRUCTURE EXISTS, NON-NESTED'
    elif diffshape: RESULT='STRUCTURE EXISTS, DIFFERENT SHAPE'
    elif q36: RESULT='NESTED + QUOTIENT 35: PROCEED Q3-6'
    else: RESULT='DEGREE-4 TRACK POWERLESS: all tested data forced identical'
print('RESULT =',RESULT)
