#!/usr/bin/env python3
"""Actual rank-4 D4 first-layer lift-fibre audit.
Exact F3 Magnus degree <=3. Tests L_c = phi_c o g and L_c = g o phi_c.
"""
from itertools import combinations,product
import json
P,N,D=3,4,3
ONE={():1}; GEN=[{():1,(i,):1} for i in range(N)]
PAIRS=list(combinations(range(N),2)); SPECS=[(i,j,k) for i in range(N) for j,k in PAIRS]
def add(a,b):
 c=dict(a)
 for w,v in b.items(): c[w]=(c.get(w,0)+v)%P; c.pop(w,None) if c[w]==0 else None
 return c
def sc(a,s): return {w:v*s%P for w,v in a.items() if v*s%P}
def mu(a,b):
 c={}
 for x,u in a.items():
  for y,v in b.items():
   w=x+y
   if len(w)<=D:c[w]=(c.get(w,0)+u*v)%P
 return {w:v for w,v in c.items() if v%P}
def inv(a):
 h=add(a,sc(ONE,-1)); z=dict(ONE); t=dict(ONE)
 for k in range(1,D+1): t=mu(t,h); z=add(z,sc(t,(-1)**k))
 return z
def comm(i,j): return [(i,1),(j,1),(i,-1),(j,-1)]
def sub(w,A):
 o=[]
 for i,s in w:
  z=A[i]; o += z if s==1 else [(j,-t) for j,t in z[::-1]]
 return o
def comp(A,B): return [sub(w,A) for w in B] # A o B
def ev(w,G):
 z=dict(ONE)
 for i,s in w:z=mu(z,G[i] if s==1 else inv(G[i]))
 return z
def vec(a,d): return [a.get(w,0) for w in product(range(N),repeat=d)]
def rank(rows):
 if not rows:return 0
 a=[r[:] for r in rows]; m,n=len(a),len(a[0]); r=0
 for c in range(n):
  p=next((i for i in range(r,m) if a[i][c]%P),None)
  if p is None:continue
  a[r],a[p]=a[p],a[r]; q=pow(a[r][c],-1,P); a[r]=[x*q%P for x in a[r]]
  for i in range(m):
   if i!=r and a[i][c]:
    q=a[i][c]; a[i]=[(a[i][j]-q*a[r][j])%P for j in range(n)]
  r+=1
 return r
def coeff(s):
 c=[[0]*6 for _ in range(N)]; i,j,k=s; c[i][PAIRS.index((j,k))]=1; return c
def cadd(a,b): return [[(x+y)%P for x,y in zip(u,v)] for u,v in zip(a,b)]
def ia(c):
 out=[]
 for i in range(N):
  w=[(i,1)]
  for a,(j,k) in zip(c[i],PAIRS):
   for _ in range(a%P):w+=comm(j,k)
  out.append(w)
 return out
R3=[(0,1)]*3+comm(0,1)+comm(2,3); RI=comm(0,1)+comm(2,3)
B3=ev(R3,GEN); BI=ev(RI,GEN); R2={w:v for w,v in B3.items() if len(w)==2}
X=[{(i,):1} for i in range(N)]
C3=[vec(add(mu(X[i],R2),sc(mu(R2,X[i]),-1)),3) for i in range(N)]
assert rank(C3)==4
CASES={
 "identity":[[(0,1)],[(1,1)],[(2,1)],[(3,1)]],
 "minus_I":[[(0,-1)],[(1,-1)],[(2,-1)],[(3,-1)]],
 "transvection":[[(0,1),(1,1)],[(1,1)],[(2,1)],[(3,1)]],
}
def lift(g,p,side):
 w=comp(p,g) if side=="left" else comp(g,p)
 return [ev(x,GEN) for x in w]
def defect(R,B,L):return vec(add(ev(R,L),sc(B,-1)),3)
out={}
for name,g in CASES.items():
 out[name]={}
 bg=[ev(w,GEN) for w in g]
 for side in ("left","right"):
  d0=defect(R3,B3,bg); i0=defect(RI,BI,bg); V=[]; W=[]
  for s in SPECS:
   L=lift(g,ia(coeff(s)),side)
   assert all(vec(L[i],1)==vec(bg[i],1) for i in range(N))
   V.append([(x-y)%P for x,y in zip(defect(R3,B3,L),d0)])
   W.append([(x-y)%P for x,y in zip(defect(RI,BI,L),i0)])
  assert V==W
  raw=mod=0
  for a,b in combinations(SPECS,2):
   pa,pb=ia(coeff(a)),ia(coeff(b)); ps=ia(cadd(coeff(a),coeff(b))); pc=comp(pa,pb)
   S=comp(ps,g) if side=="left" else comp(g,ps)
   C=comp(pc,g) if side=="left" else comp(g,pc)
   ds=defect(R3,B3,[ev(w,GEN) for w in S]); dc=defect(R3,B3,[ev(w,GEN) for w in C])
   diff=[(x-y)%P for x,y in zip(dc,ds)]
   raw+=bool(any(diff)); mod+=rank(C3+[diff])>rank(C3)
  q=[(x-y)%P for x,y in zip(d0,i0)]; gr=rank(C3+V)
  out[name][side]={"IA_variation_rank":rank(V),"q_variation_equal":V==W,
   "composition_pairs":276,"raw_composition_failures":raw,
   "composition_failures_mod_C3":mod,"gauge_rank":gr,
   "q_signal_nonzero":any(q),"q_signal_survives_quotient":rank(C3+V+[q])>gr}
for z in out.values():
 for r in z.values():
  assert r["IA_variation_rank"]==20 and r["q_variation_equal"]
  assert r["composition_failures_mod_C3"]==0
for n in ("minus_I","transvection"):
 for s in ("left","right"):assert out[n][s]["q_signal_survives_quotient"]
print(json.dumps({"status":"PASS_GRADED_FIBRE_LOCAL",
"interpretation":"Actual left/right first-layer IA perturbations of a fixed linear lift were tested as genuine lift fibres. Their associated-graded parameter law agrees through degree 2; degree-3 composition discrepancy is absorbed by C3. The q=3 and q=infinity defect-change maps agree, have rank 20, and the q-sensitive base defect survives the C3+IA quotient for the nontrivial tested representatives.",
"scope":"identity, -I, one transvection; first IA layer; exact F3; Magnus degree <=3","cases":out},indent=2))
