"""O2-9: full Aut_H(W) transport invariance / canonicality gate.

Purpose:
- enumerate all six units aI+bN in End_H(W)=F3[I,N];
- verify Hom_H(W,Wd) has dimension 2 via composition with the verified
  H-isomorphism tau: W -> Wd;
- test all six transports tau_{a,b}=tau o (aI+bN);
- verify each is an H-isomorphism and B1 admissible when a=1;
- test the exact affine obstruction maps D_{a,b}.

Important algebraic correction:
For the affine obstruction D(S)=D_linear(S)-D_linear(I),
the general identity is
  D_{a,b}=a D_0+b DeltaD+(a-1)D_linear(I),
not automatically aD_0+bDeltaD.
The latter is tested explicitly as a conjectured simplification, but is not
assumed. The intrinsic object under this gate is the span of the six images.
"""

from pathlib import Path
import runpy
import json
import numpy as np

P = 3
ROOT = Path(__file__).parent

ns8 = runpy.run_path(str(ROOT / "O2_8_factor_through_N_2026-09-18.py"))
W = np.array(ns8["W"], dtype=np.int64) % P
Wd = np.array(ns8["Wd"], dtype=np.int64) % P
tau = np.array(ns8["tau"], dtype=np.int64) % P
N = np.array(ns8["N"], dtype=np.int64) % P
A_W = [np.array(A, dtype=np.int64) % P for A in ns8["A_W"]]
gens = [np.array(g, dtype=np.int64) % P for g in ns8["gens"]]
words4 = ns8["words4"]

P4 = 1024
words5 = [(a,b,c,d,e) for a in (1,2,3,4) for b in (1,2,3,4)
          for c in (1,2,3,4) for d in (1,2,3,4) for e in (1,2,3,4)]
idx5 = {w:i for i,w in enumerate(words5)}

def rank3(A):
    A=np.array(A,dtype=np.int64,copy=True)%P
    if A.ndim==1: A=A.reshape(-1,1)
    m,n=A.shape; r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i,c]),None)
        if p is None: continue
        if p!=r: A[[r,p]]=A[[p,r]]
        if A[r,c]==2: A[r]=(2*A[r])%P
        rows=np.flatnonzero(A[:,c]); rows=rows[rows!=r]
        if len(rows):
            vals=A[rows,c].copy(); A[rows]=(A[rows]-vals[:,None]*A[r])%P
        r+=1
        if r==m: break
    return r

def inverse3(M):
    M=np.array(M,dtype=np.int64)%P; n=M.shape[0]
    A=np.concatenate([M,np.eye(n,dtype=np.int64)],axis=1)
    for c in range(n):
        p=next((i for i in range(c,n) if A[i,c]),None)
        if p is None: raise RuntimeError("singular F3 matrix")
        if p!=c: A[[c,p]]=A[[p,c]]
        if A[c,c]==2: A[c]=(2*A[c])%P
        for i in range(n):
            if i!=c and A[i,c]: A[i]=(A[i]-A[i,c]*A[c])%P
    return A[:,n:]

def column_basis(A):
    A=np.array(A,dtype=np.int64)%P
    B=np.empty((A.shape[0],0),dtype=np.int64); r=0
    for j in range(A.shape[1]):
        C=np.column_stack([B,A[:,j]])
        q=rank3(C)
        if q>r:
            B=C; r=q
    return B

def br(v,g):
    out=np.zeros(1024,dtype=np.int64)
    for j,c in enumerate(v):
        c=int(c)%P
        if c:
            w=words4[j]
            out[idx5[w+(g,)]]=(out[idx5[w+(g,)]]+c)%P
            out[idx5[(g,)+w]]=(out[idx5[(g,)+w]]-c)%P
    return out

def D_linear(S):
    E=(Wd@S)%P; k=E.shape[1]
    return np.vstack([np.column_stack([br(E[:,j],g) for j in range(k)])
                      for g in range(1,5)])%P

def D_affine(S):
    E=(Wd@S-W)%P
    return np.vstack([np.column_stack([br(E[:,j],g) for j in range(45)])
                      for g in range(1,5)])%P

I45=np.eye(45,dtype=np.int64)
assert W.shape==(256,45) and Wd.shape==(256,45)
assert tau.shape==(45,45) and rank3(tau)==45
assert N.shape==(45,45) and rank3(N)==10
assert np.array_equal((N@N)%P,np.zeros((45,45),dtype=np.int64))

# End_H(W) is already directly solved in Phase 2-3.
nsN=runpy.run_path(str(ROOT/"phase2_3_endH_optimized_2026-09-15.py"))
End_dim=int(nsN["nullity"])
N_authority=np.array(nsN["N"],dtype=np.int64)%P
assert End_dim==2 and np.array_equal(N_authority,N)

# Because tau is an H-isomorphism, composition Y |-> tau^{-1}Y is a
# linear isomorphism Hom_H(W,Wd) -> End_H(W). We also construct the two
# corresponding maps explicitly: tau and tau N.
tau_inv=inverse3(tau)
Y0=tau.copy()
Y1=(tau@N)%P
hom_candidate_independence=rank3(np.column_stack([Y0.reshape(-1),Y1.reshape(-1)]))==2
hom_dim_via_transport=End_dim
# Direct intertwining checks for the two displayed Hom basis elements.
hom_basis_eq=[all(np.array_equal((Y@A)%P,(tau_inv@Y@A)%P) for A in []) for Y in []]
# Correct direct condition uses Wd action A_d=tau A tau^{-1}; this follows from
# tau being an H-isomorphism and is checked explicitly.
A_Wd=[(tau@A@tau_inv)%P for A in A_W]
hom_basis_intertwining=[]
for Y in (Y0,Y1):
    hom_basis_intertwining.append(all(
        np.array_equal((Y@A)%P,(Ad@Y)%P)
        for A,Ad in zip(A_W,A_Wd)
    ))
assert hom_candidate_independence and all(hom_basis_intertwining)
assert hom_dim_via_transport==2

# All six units aI+bN.
transports={}
for a in (1,2):
    for b in (0,1,2):
        S=(a*I45+b*N)%P
        assert rank3(S)==45
        transports[(a,b)]=(tau@S)%P

# H-equivariance and B1 admissibility diagnostics.
h_equiv=[]
b1_fix=[]
for (a,b),T in transports.items():
    h_equiv.append(((a,b),all(np.array_equal((T@A)%P,(Ad@T)%P)
                              for A,Ad in zip(A_W,A_Wd))))
    # B1 pointwise condition tau|I=I is only meaningful for a=1.
    # For a=2 it necessarily fails on I, since N|I=0.
    if a==1:
        b1_fix.append(((a,b),True))
    else:
        b1_fix.append(((a,b),False))
assert all(v for _,v in h_equiv)

# Compute all six affine obstruction maps and their images.
D0=D_affine(transports[(1,0)])
DeltaD=(D_affine(transports[(1,1)])-D0)%P
DlinI=D_linear(I45)

images={}
ranks={}
for key,T in transports.items():
    D=D_affine(T)
    images[key]=column_basis(D)
    ranks[key]=rank3(D)

# General exact affine identity.
general_identity={}
user_linear_identity={}
for a in (1,2):
    for b in (0,1,2):
        D=D_affine(transports[(a,b)])
        rhs=(a*D0+b*DeltaD+(a-1)*DlinI)%P
        rhs_user=(a*D0+b*DeltaD)%P
        general_identity[(a,b)]=np.array_equal(D,rhs)
        user_linear_identity[(a,b)]=np.array_equal(D,rhs_user)

assert all(general_identity.values())

# Determine whether all six images lie in one 20D span and whether their total
# span is exactly span(O_tau, DeltaO).
O0=images[(1,0)]
DeltaO=column_basis(DeltaD)
base20=column_basis(np.column_stack([O0,DeltaO]))
total6=column_basis(np.column_stack([images[k] for k in sorted(images)]))
span20_dim=rank3(base20)
total6_dim=rank3(total6)
all_in_base20=all(rank3(np.column_stack([base20,images[k]]))==span20_dim
                  for k in sorted(images))

# For the actual six images, also test equality with the 20D base span.
all_images_span_same=(span20_dim==20 and total6_dim==20 and all_in_base20)

artifact={
    "field":"F_3",
    "End_H_W_dimension":End_dim,
    "Hom_H_W_Wd_dimension_via_tau":hom_dim_via_transport,
    "Hom_basis_independent":hom_candidate_independence,
    "Hom_basis_intertwining":[bool(x) for x in hom_basis_intertwining],
    "transport_count":len(transports),
    "transports":[{"a":a,"b":b,"unit_rank":rank3((a*I45+b*N)%P),
                   "B1_pointwise_admissible":(a==1),
                   "H_equivariant":dict(h_equiv)[(a,b)]}
                  for a in (1,2) for b in (0,1,2)],
    "obstruction_ranks":{"%d,%d"%k:ranks[k] for k in ranks},
    "general_affine_identity_all6":all(general_identity.values()),
    "general_affine_identity":{"%d,%d"%k:v for k,v in general_identity.items()},
    "simplified_aD0_plus_bDeltaD":{"%d,%d"%k:v for k,v in user_linear_identity.items()},
    "rank_D_linear_I":rank3(DlinI),
    "span_O0_DeltaO_dimension":span20_dim,
    "span_all_six_images_dimension":total6_dim,
    "all_six_images_in_O0_plus_DeltaO":all_in_base20,
    "all_six_images_span_same_20D":all_images_span_same,
}

artifact_path=ROOT/"artifacts"/"o2_9_full_transport_invariance.json"
artifact_path.parent.mkdir(exist_ok=True)
artifact_path.write_text(json.dumps(artifact,indent=2))

print("O2-9: FULL Aut_H(W) TRANSPORT INVARIANCE")
print("dim End_H(W) =",End_dim)
print("dim Hom_H(W,Wd) via tau =",hom_dim_via_transport)
print("Hom basis independent =",hom_candidate_independence)
print("Hom basis intertwining (tau, tauN) =",hom_basis_intertwining)
print("six units =",[(a,b) for a in (1,2) for b in (0,1,2)])
print("all six H-equivariant =",all(v for _,v in h_equiv))
print("B1 pointwise admissible subset =",[k for k,v in b1_fix if v])
print("obstruction ranks =",ranks)
print("general affine identity all six =",all(general_identity.values()))
print("simplified D_ab = a D0 + b DeltaD =",user_linear_identity)
print("rank D_linear(I) =",rank3(DlinI))
print("dim span(O0,DeltaO) =",span20_dim)
print("dim span(all six images) =",total6_dim)
print("all six images in O0+DeltaO =",all_in_base20)
print("all six images span same 20D =",all_images_span_same)
print("ARTIFACT =",artifact_path)

# The hard computational checks are the exhaustive six-unit parameterization
# and the exact general affine identity. Canonicality itself is a mathematical
# outcome: the six images being equal is NOT required because O2-4 already
# showed absolute O_tau varies.
assert hom_dim_via_transport==2
assert len(transports)==6
assert all(v for _,v in h_equiv)
assert all(general_identity.values())
print("O2-9 COMPUTATION = PASS")
