"""Phase 2-10: explicit test W ~= Lambda^2(Sym^2(V)) over F3."""
from pathlib import Path
import runpy
import numpy as np
P=3
ROOT=Path(__file__).resolve().parents[1]
ns=runpy.run_path(str(ROOT/'research'/'phase2_7_M_quotient_2026-09-15.py'))
AW=[np.array(x,dtype=np.int64)%P for x in ns['AW']]
if 'gens' in ns: G=[np.array(x,dtype=np.int64)%P for x in ns['gens']]
else:
    ns1=runpy.run_path(str(ROOT/'research'/'phase2_1_invariant_space_verification_2026-09-15.py'))
    G=[np.array(x,dtype=np.int64)%P for x in ns1['gens']]
pairs=[(i,j) for i in range(4) for j in range(i,4)]; pi={p:k for k,p in enumerate(pairs)}
def sym2(g):
 S=np.zeros((10,10),dtype=np.int64)
 for c,(i,j) in enumerate(pairs):
  for a in range(4):
   for b in range(4):
    z=int(g[a,i])*int(g[b,j])
    if z:
     p=(a,b) if a<=b else (b,a); S[pi[p],c]=(S[pi[p],c]+z)%P
 return S
wp=[(i,j) for i in range(10) for j in range(i+1,10)]; wi={p:k for k,p in enumerate(wp)}
def wedge2(S):
 L=np.zeros((45,45),dtype=np.int64)
 for c,(i,j) in enumerate(wp):
  for a in range(10):
   for b in range(10):
    z=int(S[a,i])*int(S[b,j])
    if not z or a==b: continue
    p=(a,b) if a<b else (b,a); s=1 if a<b else -1
    L[wi[p],c]=(L[wi[p],c]+s*z)%P
 return L
AM=[wedge2(sym2(g)) for g in G]
def rref(A):
 A=np.array(A,dtype=np.int64,copy=True)%P; m,n=A.shape; r=0; piv=[]
 for c in range(n):
  q=next((i for i in range(r,m) if A[i,c]),None)
  if q is None: continue
  A[[r,q]]=A[[q,r]]
  if A[r,c]==2:A[r]=(2*A[r])%P
  for i in range(m):
   if i!=r and A[i,c]: A[i]=(A[i]-A[i,c]*A[r])%P
  piv.append(c); r+=1
  if r==m: break
 return r,A,piv
blocks=[]; I=np.eye(45,dtype=np.int64)
for a,b in zip(AW,AM): blocks.append((np.kron(a.T,I)-np.kron(I,b))%P)
E=np.vstack(blocks)%P; rank,R,piv=rref(E); free=[c for c in range(2025) if c not in piv]
maxrank=0
for f in free:
 x=np.zeros(2025,dtype=np.int64); x[f]=1
 for row,c in enumerate(piv): x[c]=(-R[row,f])%P
 maxrank=max(maxrank,rref(x.reshape((45,45),order='F'))[0])
print('PHASE 2-10 / W VS LAMBDA^2(SYM^2 V)')
print('W dimension =',AW[0].shape[0]); print('model dimension =',AM[0].shape[0])
print('intertwiner system shape =',E.shape); print('rank(intertwiner system) =',rank)
print('dim Hom_H =',2025-rank); print('maximum rank among basis intertwiners =',maxrank)
print('FULL_RANK_INTERTWINER_FOUND =',maxrank==45)
if maxrank==45: print('CERTIFICATE: W ~= Lambda^2(Sym^2(V))')
