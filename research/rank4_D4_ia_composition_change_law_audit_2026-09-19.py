#!/usr/bin/env python3
"""Rank-4 D4 IA lift-fibre composition/change-law audit.

This is the next authorized sub-gate after the local equivariance PASS.
It audits the first graded IA fibre itself, not GSp_4 representatives.
All arithmetic is exact over F3 and truncated in associative Magnus degree <=3.
"""
from itertools import combinations, product
import json

P,N,MAXD=3,4,3
ONE={():1}
X=[{(i,):1} for i in range(N)]
GEN=[{():1,(i,):1} for i in range(N)]
PAIRS=list(combinations(range(N),2))
IA_SPECS=[(i,j,k) for i in range(N) for j,k in PAIRS]

def add(a,b):
    c=dict(a)
    for w,v in b.items():
        c[w]=(c.get(w,0)+v)%P
        if c[w]==0: del c[w]
    return c
def scale(a,s): return {w:(v*s)%P for w,v in a.items() if (v*s)%P}
def mul(a,b):
    c={}
    for wa,va in a.items():
        for wb,vb in b.items():
            w=wa+wb
            if len(w)<=MAXD: c[w]=(c.get(w,0)+va*vb)%P
    return {w:v for w,v in c.items() if v}
def inv(a):
    h=add(a,scale(ONE,-1)); z=dict(ONE); t=dict(ONE)
    for k in range(1,MAXD+1):
        t=mul(t,h); z=add(z,scale(t,(-1)**k))
    return z
def comm_word(i,j): return [(i,1),(j,1),(i,-1),(j,-1)]
def eval_word(word,gens):
    z=dict(ONE)
    for i,s in word: z=mul(z,gens[i] if s==1 else inv(gens[i]))
    return z
def ia_word_map(coeff):
    out=[]
    for i in range(N):
        w=[(i,1)]
        for a,(j,k) in zip(coeff[i],PAIRS):
            for _ in range(a%P): w += comm_word(j,k)
        out.append(w)
    return out

def substitute_word(word,images):
    out=[]
    for i,s in word:
        img=images[i]
        if s==1: out += img
        else:
            invimg=[]
            for j,t in reversed(img):
                invimg.append((j,-t))
            out += invimg
    return out

def compose_words(A,B):
    # A o B, as exact free-group words.
    return [substitute_word(Bi,A) for Bi in B]

# Frozen relators.
R3=[(0,1)]*3+comm_word(0,1)+comm_word(2,3)
RINF=comm_word(0,1)+comm_word(2,3)
BASE3=eval_word(R3,GEN)
BASEINF=eval_word(RINF,GEN)
R2={w:v for w,v in BASE3.items() if len(w)==2}
C3=[vec(add(mul(X[i],R2),scale(mul(R2,X[i]),-1)),3) for i in range(N)]
assert rank(C3)==4

# Three small fixed linear actions used in the already-authorized local audit.
CASES={
 "identity":GEN,
 "minus_I":[inv(g) for g in GEN],
 "transvection":[mul(GEN[0],GEN[1]),GEN[1],GEN[2],GEN[3]],
}

def defect(relator,base_relator,lift):
    return vec(add(eval_word(relator,lift),scale(base_relator,-1)),3)
def compose_case_with_ia(base,coeff):
    # IA acts on the target after the fixed base lift.
    return [eval_word(w,base) for w in ia_word_map(coeff)]

results={}
for name,base in CASES.items():
    zero=[[0]*6 for _ in range(N)]
    # Associated-graded torsor test: every first-layer coordinate has a unique
    # degree-2 image, and composition adds those coordinates.
    for a,b in combinations(IA_SPECS,2):
        pa,pb=ia_word_map(basis_coeff(a)),ia_word_map(basis_coeff(b))
        pc=compose_words(pa,pb)
        pab=ia_word_map(add_coeff(basis_coeff(a),basis_coeff(b)))
        pc_eval=[eval_word(w,GEN) for w in pc]
        pab_eval=[eval_word(w,GEN) for w in pab]
        for i in range(N):
            assert vec(pc_eval[i],1)==vec(pab_eval[i],1)
            assert vec(pc_eval[i],2)==vec(pab_eval[i],2)

    d0_3=defect(R3,BASE3,base); d0_i=defect(RINF,BASEINF,base)
    variations3={}; variationsI={}
    for s in IA_SPECS:
        c=basis_coeff(s)
        variations3[s]=[(x-y)%P for x,y in zip(defect(R3,BASE3,compose_case_with_ia(base,c)),d0_3)]
        variationsI[s]=[(x-y)%P for x,y in zip(defect(RINF,BASEINF,compose_case_with_ia(base,c)),d0_i)]

    # Basepoint-independent first-layer linearity, now tested through actual
    # composition rather than coefficient addition alone.
    composition_fail_raw=composition_fail_mod_C3=0
    for a,b in combinations(IA_SPECS,2):
        ca,cb=basis_coeff(a),basis_coeff(b)
        cab=add_coeff(ca,cb)
        hab=compose_case_with_ia(base,cab)
        # compose the actual IA-target actions, not the coordinate sum.
        hab_comp_words=compose_words(ia_word_map(ca),ia_word_map(cb))
        hab_comp=[eval_word(w,base) for w in hab_comp_words]
        lhs3=defect(R3,BASE3,hab_comp)
        rhs3=defect(R3,BASE3,hab)
        diff=[(x-y)%P for x,y in zip(lhs3,rhs3)]
        if any(diff): composition_fail_raw+=1
        if rank(C3+[diff])>rank(C3): composition_fail_mod_C3+=1

        lhsi=defect(RINF,BASEINF,hab_comp)
        rhsi=defect(RINF,BASEINF,hab)
        diffi=[(x-y)%P for x,y in zip(lhsi,rhsi)]
        assert diffi==diff

    # Full span of the first-layer variations and q-signal survival.
    V3=[variations3[s] for s in IA_SPECS]
    VI=[variationsI[s] for s in IA_SPECS]
    assert V3==VI
    gauge_rank=rank(C3+V3)
    qsig=[(x-y)%P for x,y in zip(d0_3,d0_i)]
    survives=rank(C3+V3+[qsig])>gauge_rank

    results[name]={
      "IA_first_layer_dim":24,
      "target_dim":64,
      "C3_rank":rank(C3),
      "IA_variation_rank":rank(V3),
      "gauge_rank":gauge_rank,
      "quotient_dim":64-gauge_rank,
      "composition_pairs":276,
      "raw_composition_failures":composition_fail_raw,
      "composition_failures_mod_C3":composition_fail_mod_C3,
      "q_variation_equal":V3==VI,
      "q_signal_nonzero":any(qsig),
      "q_signal_survives_quotient":survives,
    }

# The main mathematical checkpoint is the associated-graded law:
# composition must agree with coordinate addition modulo the ordinary
# conjugation correction, while the q-signal survives the gauge quotient.
assert all(r["composition_failures_mod_C3"]==0 for r in results.values())
assert all(r["IA_variation_rank"]==20 for r in results.values())
assert results["minus_I"]["q_signal_survives_quotient"]
assert results["transvection"]["q_signal_survives_quotient"]

print(json.dumps({
 "status":"PASS_CHANGE_LAW_LOCAL" if all(r["composition_failures_mod_C3"]==0 for r in results.values()) else "FAIL",
 "interpretation":"The first-layer IA fibre is an associated-graded torsor: actual IA composition agrees with addition of Hom(V,L2) parameters through degree 2, and its degree-3 discrepancy is absorbed by the ordinary C3 correction. The induced defect-change law is q-independent in the tested representatives, while the q=3 restricted-power signal survives the candidate quotient.",
 "cases":results
},indent=2))

# trigger audit after workflow registration
