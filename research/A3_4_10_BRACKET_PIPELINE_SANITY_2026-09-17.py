import runpy
import numpy as np
from itertools import product

P = 3
ROOT = 'research/'
ns = runpy.run_path(ROOT + 'phase2_18_A3_4_5_intersection_K_and_Sym2_2026-09-16.py')
rank3 = ns['rank3']
W = np.array(ns['W'], dtype=np.int64) % P
Wd = np.array(ns['Wd_basis'], dtype=np.int64) % P
ns1 = runpy.run_path(ROOT + 'phase2_1_invariant_space_verification_2026-09-15.py')
gens = ns1['gens']
apply_linear_map = ns1['apply_linear_map']
words4 = list(ns1['index4'].keys())
index4 = ns1['index4']
words5 = list(product((1,2,3,4), repeat=5))
index5 = {w:i for i,w in enumerate(words5)}
assert W.shape == (256,45) and Wd.shape == (256,45)

def mul(A,B):
    out={}
    for wa,ca in A.items():
        for wb,cb in B.items():
            w=wa+wb; out[w]=(out.get(w,0)+ca*cb)%P
    return {w:c for w,c in out.items() if c%P}

def add(A,B):
    out=dict(A)
    for w,c in B.items():
        out[w]=(out.get(w,0)+c)%P
        if out[w]==0: del out[w]
    return out

def bracket(A,B):
    return add(mul(A,B), {w:(-c)%P for w,c in mul(B,A).items()})

def degree4_action(g):
    G=np.zeros((256,256),dtype=np.int64)
    for j,w in enumerate(words4):
        for ww,c in apply_linear_map({w:1},g).items():
            G[index4[ww],j]=(G[index4[ww],j]+int(c))%P
    return G

def vec_dict(v):
    return {words4[k]:int(v[k])%P for k in range(256) if int(v[k])%P}

def vec5(a):
    v=np.zeros(1024,dtype=np.int64)
    for w,c in a.items(): v[index5[w]]=int(c)%P
    return v

print('A3-4-10 BRACKET PIPELINE SANITY CHECK')
print('dim W45 =',rank3(W),'dim Wd =',rank3(Wd))
# Strong empirical check: for every generator, every W/Wd basis vector,
# and every degree-1 generator X_h, verify
# D5(g)[v,X_h] = [D4(g)v, D1(g)X_h].
for gi,g in enumerate(gens):
    D4=degree4_action(g)
    for label,M in [('W45',W),('Wd',Wd)]:
        for j in range(M.shape[1]):
            vdict=vec_dict(M[:,j])
            for h in range(1,5):
                bh=bracket(vdict,{(h,):1})
                lhs=vec5({ww:cc for w,c in bh.items() for ww,cc in apply_linear_map({w:int(c)},g).items()})
                gv=(D4@M[:,j])%P
                gh=apply_linear_map({(h,):1},g)
                rhs=vec5(bracket(vec_dict(gv),gh))
                assert np.array_equal(lhs,rhs),(gi,label,j,h)
    print('GEN',gi,'BRACKET_EQUIVARIANCE_W_AND_Wd = True')
print('RESULT = PASS')
print('This validates the ambient bracket/action pipeline, including the X_h side, independently of the A3-4-10 tau compatibility conclusion.')
