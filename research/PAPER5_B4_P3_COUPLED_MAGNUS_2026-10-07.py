#!/usr/bin/env python3
"""Paper5 B4 p=3: coupled Magnus lift through degree 6 (a=1).
LOCAL diagnostic only.  Exact associative algebra over F3."""
from itertools import product
from math import comb
P=3; N=6; L=("X","Y","Z")
def add(a,b):
 c=dict(a)
 for w,v in b.items():
  c[w]=(c.get(w,0)+v)%P
  if not c[w]: del c[w]
 return c
def sc(a,s): return {w:(v*s)%P for w,v in a.items() if (v*s)%P}
def mul(a,b):
 c={}
 for u,cu in a.items():
  for v,cv in b.items():
   if len(u)+len(v)<=N:c[u+v]=(c.get(u+v,0)+cu*cv)%P
 return {w:v for w,v in c.items() if v}
def pw(a,n):
 if n<0: raise ValueError("negative power only via binomial")
 o={():1}; q=a
 while n:
  if n&1:o=mul(o,q)
  n//=2
  if n:q=mul(q,q)
 return o
def onepow(ch,n):
 out={}
 for k in range(N+1):
  if n>=0 and k>n: continue
  coef=comb(n,k) if n>=0 else ((-1)**k)*comb(-n+k-1,k)
  if coef%P:out[(ch,)*k]=coef%P
 return out
def inv(a):
 # a=1+h; geometric inverse
 h=add(a,{():-1}); out={():1}; q={():1}
 for _ in range(N):
  q=mul(q,sc(h,-1)); out=add(out,q)
 return out
def hom(a,d):return {w:c for w,c in a.items() if len(w)==d}
def W(d):return list(product(L,repeat=d))
def vec(a,ws):return [a.get(w,0)%P for w in ws]
def rank(A):
 if not A:return 0
 A=[r[:] for r in A]; m=len(A); n=len(A[0]); rr=0
 for j in range(n):
  q=next((i for i in range(rr,m) if A[i][j]),None)
  if q is None:continue
  A[rr],A[q]=A[q],A[rr]; iv=1 if A[rr][j]==1 else 2
  A[rr]=[(x*iv)%P for x in A[rr]]
  for i in range(m):
   if i!=rr and A[i][j]:
    t=A[i][j]; A[i]=[(A[i][k]-t*A[rr][k])%P for k in range(n)]
  rr+=1
  if rr==m:break
 return rr
def span(rhs,basis,ws):
 B=[vec(q,ws) for q in basis]; b=vec(rhs,ws)
 return rank(B)==rank(B+[b])
def ideal(RH,d):
 out=[]
 for h in range(1,d+1):
  if not RH[h]:continue
  rem=d-h
  for i in range(rem+1):
   for u in product(L,repeat=i):
    for v in product(L,repeat=rem-i):
     out.append({u+w+v:c for w,c in RH[h].items()})
 return out
def lin_solve(cols,rhs,basis,ws):
 # Find c with rhs + sum c_j cols_j in span(basis).
 allc=basis+cols; M=[vec(q,ws) for q in allc]; b=vec(sc(rhs,-1),ws)
 A=[[M[j][i] for j in range(len(M))]+[b[i]] for i in range(len(ws))]
 r=0;piv=[]
 for j in range(len(M)):
  q=next((i for i in range(r,len(A)) if A[i][j]),None)
  if q is None:continue
  A[r],A[q]=A[q],A[r];iv=1 if A[r][j]==1 else 2
  A[r]=[(x*iv)%P for x in A[r]]
  for i in range(len(A)):
   if i!=r and A[i][j]:
    t=A[i][j];A[i]=[(A[i][k]-t*A[r][k])%P for k in range(len(A[i]))]
  piv.append(j);r+=1
 for i in range(r,len(A)):
  if A[i][-1] and not any(A[i][j] for j in range(len(M))):return None
 sol=[0]*len(M)
 for i,j in enumerate(piv):
  sol[j]=A[i][-1]
 return sol[len(basis):]

ONE={():1};X={("X",):1};Y={("Y",):1};Z={("Z",):1}
x=add(ONE,X);y=add(ONE,Y);z=add(ONE,Z)
xi=onepow("X",-1); yi=onepow("Y",-1)
comm=mul(mul(mul(xi,yi),x),y)
comminv=inv(comm)
r=add(mul(mul(onepow("Z",3),onepow("X",-3)),comminv),sc(ONE,-1))
target=add(mul(pw(x,3),comm),sc(ONE,-1))
RH={d:hom(r,d) for d in range(1,N+1)}
R={d:hom(target,d) for d in range(1,N+1)}
print("B4 p=3 a=1")
print("RH supports:",{d:len(RH[d]) for d in range(1,N+1)})
print("R supports:",{d:len(R[d]) for d in range(1,N+1)})
I={d:ideal(RH,d) for d in range(1,N+1)}
U2=[{w:1} for w in product(L,repeat=2)]
U3=[{w:1} for w in product(L,repeat=3)]
U4=[{w:1} for w in product(L,repeat=4)]
# Degree 4 coupled equation: enumerate U2, no premature U=XX.
S4=[]
for cs in product(range(3),repeat=9):
 u={}
 for c,b in zip(cs,U2):
  if c:u=add(u,sc(b,c))
 q=add(hom(pw(add(Z,u),3),4),sc(R[4],-1))
 if span(q,I[4],W(4)):S4.append(u)
print("D4-compatible U2:",len(S4))
S5=[]
for u2 in S4:
 base=add(Z,u2); q=add(hom(pw(base,3),5),sc(R[5],-1))
 cols=[]
 for b in U3:
  cols.append(add(hom(pw(add(base,b),5),5),sc(hom(pw(base,3),5),-1)))
 sol=lin_solve(cols,q,I[5],W(5))
 if sol is not None:
  u3={}
  for c,b in zip(sol,U3):
   if c:u3=add(u3,sc(b,c))
  S5.append((u2,u3))
print("D5-compatible (U2,U3) pairs with one solution each:",len(S5))
S6=[]
for u2,u3 in S5:
 base=add(add(Z,u2),u3); q=add(hom(pw(base,3),6),sc(R[6],-1))
 cols=[]
 for b in U4:
  cols.append(add(hom(pw(add(base,b),6),6),sc(hom(pw(base,3),6),-1)))
 sol=lin_solve(cols,q,I[6],W(6))
 if sol is not None:S6.append((u2,u3,sol))
print("D6-compatible coupled lifts:",len(S6))
def fmt(u):
 return "+".join(("".join(w) if c==1 else str(c)+"*"+"".join(w)) for w,c in u.items()) or "0"
if S6:
 print("FIRST U2 =",fmt(S6[0][0]));print("FIRST U3 =",fmt(S6[0][1]))
 print("STATUS=PASS_LOCAL_THROUGH_D6")
else: print("STATUS=FAIL_CLOSED_AT_D6")
