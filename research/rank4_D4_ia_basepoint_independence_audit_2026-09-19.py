#!/usr/bin/env python3
"""Rank-4 D4 IA basepoint-independence audit.
Exact F3, Magnus degree <=3. For each fixed linear action, compare the
degree-3 defect-change map from every first-layer IA basepoint with that from
the canonical base lift. Both left and right fibre parameterizations are tested.
"""
from itertools import combinations,product
import json
P,N,D=3,4,3; ONE={():1}; GEN=[{():1,(i,):1} for i in range(N)]
PAIRS=list(combinations(range(N),2)); S=[(i,j,k) for i in range(N) for j,k in PAIRS]
def add(a,b):
 c=dict(a)
 for w,v in b.items(): c[w]=(c.get(w,0)+v)%P; c.pop(w,None) if c[w]==0 else None
 return c
def sc(a,s):return {w:v*s%P for w,v in a.items() if v*s%P}
def mu(a,b):
 c={}
 for x,u in a.items():
  for y,v in b.items():
   w=x+y
   if len(w)<=D:c[w]=(c.get(w,0)+u*v)%P
 return {w:v for w,v in c.items() if v}
def inv(a):
 h=add(a,sc(ONE,-1)); z=dict(ONE); t=dict(ONE)
 for k in range(1,D+1):t=mu(t,h);z=add(z,sc(t,(-1)**k))
 return z
def comm(i,j):return[(i,1),(j,1),(i,-1),(j,-1)]
def sub(w,A):
 o=[]
 for i,s in w:
  z=A[i];o+=z if s==1 else[(j,-t)for j,t in z[::-1]]
 return o
def comp(A,B):return[sub(w,A)for w in B]
def ev(w,G):
 z=dict(ONE)
 for i,s in w:z=mu(z,G[i]if s==1 else inv(G[i]))
 return z
def vec(a,d):return[a.get(w,0)for w in product(range(N),repeat=d)]
def rank(rows):
 if not rows:return 0
 a=[r[:]for r in rows];m,n=len(a),len(a[0]);r=0
 for c in range(n):
  p=next((i for i in range(r,m)if a[i][c]%P),None)
  if p is None:continue
  a[r],a[p]=a[p],a[r];q=pow(a[r][c],-1,P);a[r]=[x*q%P for x in a[r]]
  for i in range(m):
   if i!=r and a[i][c]:
    q=a[i][c];a[i]=[(a[i][j]-q*a[r][j])%P for j in range(n)]
  r+=1
 return r
def coeff(s):
 c=[[0]*6 for _ in range(N)];i,j,k=s;c[i][PAIRS.index((j,k))]=1;return c
def ia(c):
 o=[]
 for i in range(N):
  w=[(i,1)]
  for a,(j,k) in zip(c[i],PAIRS):
   for _ in range(a%P):w+=comm(j,k)
  o.append(w)
 return o
R3=[(0,1)]*3+comm(0,1)+comm(2,3);RI=comm(0,1)+comm(2,3)
B3=ev(R3,GEN);BI=ev(RI,GEN);R2={w:v for w,v in B3.items()if len(w)==2}
X=[{(i,):1}for i in range(N)]
C3=[vec(add(mu(X[i],R2),sc(mu(R2,X[i]),-1)),3)for i in range(N)];assert rank(C3)==4
CASES={"identity":[[(0,1)],[(1,1)],[(2,1)],[(3,1)]],
"minus_I":[[(0,-1)],[(1,-1)],[(2,-1)],[(3,-1)]],
"transvection":[[(0,1),(1,1)],[(1,1)],[(2,1)],[(3,1)]]}
def lift(g,p,side):
 w=comp(p,g)if side=="left"else comp(g,p);return[ev(x,GEN)for x in w]
out={}
for name,g in CASES.items():
 out[name]={}
 base=[ev(w,GEN)for w in g]
 for side in("left","right"):
  # Reference change map at the canonical basepoint.
  ref=[]
  for a in S:
   L=lift(g,ia(coeff(a)),side);ref.append([(x-y)%P for x,y in zip(
    vec(add(ev(R3,L),sc(B3,-1)),3),vec(add(ev(R3,base),sc(B3,-1)),3))])
  raw=mod=0
  # Every one of the 24 IA basis lifts is used as a basepoint; every one of
  # the 24 directions is then applied. This is 576 actual fibre comparisons.
  for b in S:
   pb=ia(coeff(b)); LB=lift(g,pb,side)
   db3=vec(add(ev(R3,LB),sc(B3,-1)),3)
   dbi=vec(add(ev(RI,LB),sc(BI,-1)),3)
   for k,a in enumerate(S):
    pa=ia(coeff(a))
    # Apply a on the same side to the already perturbed basepoint.
    if side=="left": LBA=[ev(w,GEN)for w in comp(pa,comp(pb,g))]
    else: LBA=[ev(w,GEN)for w in comp(g,comp(pb,pa))]
    da3=vec(add(ev(R3,LBA),sc(B3,-1)),3)
    daI=vec(add(ev(RI,LBA),sc(BI,-1)),3)
    change=[(x-y)%P for x,y in zip(da3,db3)]
    changeI=[(x-y)%P for x,y in zip(daI,dbi)]
    assert change==changeI
    diff=[(x-y)%P for x,y in zip(change,ref[k])]
    if any(diff):raw+=1
    if rank(C3+[diff])>rank(C3):mod+=1
  out[name][side]={"basepoints":24,"directions":24,"comparisons":576,
   "reference_variation_rank":rank(ref),"raw_basepoint_dependence":raw,
   "basepoint_dependence_mod_C3":mod}
for z in out.values():
 for r in z.values():
  assert r["reference_variation_rank"]==20
  assert r["basepoint_dependence_mod_C3"]==0
print(json.dumps({"status":"PASS_BASEPOINT_LOCAL",
"interpretation":"For every tested first-layer IA basepoint and direction, the actual degree-3 defect change agrees with the canonical-base change modulo C3, for both q=3 and q=infinity and for both left/right fibre parameterizations. This closes the basepoint-independence question at the tested graded level.",
"scope":"identity, -I, one transvection; 24x24 fibre comparisons per side; exact F3; Magnus degree <=3","cases":out},indent=2))
