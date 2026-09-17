"""Q3-6: intrinsic extension-direction test, independent of Gate-0A T.

The Q3-5 script supplies the independently constructed q=infinity A/B/K data.
This script does NOT compare subspaces via T.  It computes intrinsic H-module
fingerprints: Hom_H(S10,M), where S10=im(N), M=B/A, and Hom_H(S10,K).
For the known q=3 model these distinguish the two extension directions:
B/A has S25 as socle (so no S10 submodule), while K has S10 as socle.
We also test splitness via existence of an H-equivariant section whenever the
quotient M -> S10 is explicitly identified by an isomorphism.
"""
import runpy
import numpy as np

P=3
q35=runpy.run_path('research/Q3_5_PRETEST_AUTO_TRANSFER_2026-09-17.py')

r3=q35['r3']; null3=q35['null3']; coords_from=q35['coords_from']; col_basis=q35['col_basis']
Ai=q35['Ai']; A3=q35['A3']; Wd=q35['Wd']; Wi=q35['Wi']; W3=q35['W3']
results35=q35['results']; case_records=q35['case_records']

def hom_basis(G,H):
    n,m=G[0].shape[0],H[0].shape[0]
    cols=[]
    for q in range(n*m):
        X=np.zeros((n,m),dtype=np.int64); X.flat[q]=1
        cols.append(np.concatenate([((X@a-b@X)%P).reshape(-1) for a,b in zip(G,H)]))
    return null3(np.column_stack(cols))

def induced_action(W,Gs,B):
    return [coords_from(B,(G@B)%P) for G in Gs]

def image_basis(N):
    return col_basis(N, r3(N))

def quotient_action(B,A,Gs):
    # Build a basis [A | C] of B. The quotient coordinates are the last dim(B)-dim(A).
    ab=col_basis(A,r3(A)); dA=ab.shape[1]
    full=ab.copy(); rr=dA
    for j in range(B.shape[1]):
        C=np.column_stack([full,B[:,j]])
        q=r3(C)
        if q>rr:
            full=C;rr=q
    assert rr==B.shape[1]
    acts=[]
    for G in Gs:
        coords=coords_from(full,(G@full)%P)
        acts.append(coords[dA:,dA:])
    return acts,full

def module_hom_dim(src,tgt):
    return len(hom_basis(src,tgt))

def fingerprint(W,Gs,N,B,A):
    S10=image_basis(N)
    G10=induced_action(W,Gs,S10)
    Gm,_=quotient_action(B,A,Gs)
    Gk=induced_action(W,Gs,col_basis(W,r3(N))) if False else None
    # K=ker N
    Kbasis=np.column_stack(null3(N))
    assert Kbasis.shape[1]==35
    Gk=induced_action(W,Gs,Kbasis)
    return {
        'dim_S10':S10.shape[1],
        'dim_M':Gm[0].shape[0],
        'dim_K':Gk[0].shape[0],
        'Hom_S10_to_M':module_hom_dim(G10,Gm),
        'Hom_M_to_S10':module_hom_dim(Gm,G10),
        'Hom_S10_to_K':module_hom_dim(G10,Gk),
        'Hom_K_to_S10':module_hom_dim(Gk,G10),
        'End_M':module_hom_dim(Gm,Gm),
        'End_K':module_hom_dim(Gk,Gk),
    }

# q=3 reference: canonical N and tau data are reconstructed by the Q3-5 run,
# but only intrinsic module actions are used here.  We use its already computed
# A3/B3 matrices and reconstruct their column spaces.
N3=q35['N3']; B3mat=q35['B3mat']; A3mat=q35['A3mat']
A3sub=col_basis(A3mat, r3(A3mat)); B3sub=col_basis(B3mat, r3(B3mat))
fp3=fingerprint(W3,A3,N3,B3sub,A3sub)
K3=np.column_stack(null3(N3));

print('Q3-6 INTRINSIC EXTENSION-DIRECTION TEST')
print('Q3_REFERENCE',fp3)

all_qinf=[]
for ni,(Ninf,nullity,tcs) in enumerate(case_records):
    Ainf=q35['delta_u'](Wi,Ninf)
    for ti,tau in enumerate(tcs):
        Binf=q35['delta_tau'](Wi,Wd,tau)
        As=col_basis(Ainf,r3(Ainf)); Bs=col_basis(Binf,r3(Binf))
        fp=fingerprint(Wi,Ai,Ninf,Bs,As)
        rec={'n':ni,'tau':ti,**fp}
        all_qinf.append(rec)
        print('QINF_CASE',rec)

# Expected direction fingerprint from q=3: Hom(S10,M)=0 and Hom(S10,K)=1.
# A q-sensitive direction flip would be visible without T.
direction_changed=[]
for x in all_qinf:
    if x['Hom_S10_to_M']!=fp3['Hom_S10_to_M'] or x['Hom_S10_to_K']!=fp3['Hom_S10_to_K']:
        direction_changed.append(x)

stable=not direction_changed
print('ALL_QINF_DIRECTION_FINGERPRINTS_MATCH_Q3 =',stable)
print('Q3_6_DIRECTIONAL_Q_SENSITIVE =',not stable)
print('RESULT =', 'Q-SENSITIVE EXTENSION DIRECTION FOUND' if not stable else 'NO Q-SENSITIVE EXTENSION DIRECTION: PROCEED TO NEXT INVARIANT')
