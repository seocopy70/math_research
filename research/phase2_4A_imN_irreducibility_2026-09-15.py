"""Phase 2-4A: exhaustive irreducibility test for U=im(N) over F_3."""
from pathlib import Path
from itertools import product
import runpy
import numpy as np
P=3; d=10
ns=runpy.run_path(str(Path(__file__).with_name('phase2_3_endH_optimized_2026-09-15.py')))
A=[np.array(x,dtype=np.int64)%P for x in ns['A_list']]
N=np.array(ns['N'],dtype=np.int64)%P

def rank3(M):
 M=np.array(M,dtype=np.int64,copy=True)%P
 if M.ndim==1:M=M[:,None]
 m,n=M.shape;r=0
 for c in range(n):
  p=next((i for i in range(r,m) if M[i,c]),None)
  if p is None:continue
  if p!=r:M[[r,p]]=M[[p,r]]
  if M[r,c]==2:M[r]=(2*M[r])%P
  for i in range(m):
   if i!=r and M[i,c]:M[i]=(M[i]-M[i,c]*M[r])%P
  r+=1
  if r==m:break
 return r

def indep_cols(M):
 cols=[];B=np.empty((M.shape[0],0),dtype=np.int64);r=0
 for j in range(M.shape[1]):
  C=np.column_stack([B,M[:,j]])
  q=rank3(C)
  if q>r:cols.append(j);B=C;r=q
 return cols,B

def coords_setup(S):
 rows=[];R=np.empty((0,d),dtype=np.int64);r=0
 for i in range(S.shape[0]):
  C=np.vstack([R,S[i:i+1]]) ;q=rank3(C)
  if q>r:
   rows.append(i);R=C;r=q
   if r==d:break
 assert r==d
 aug=np.concatenate([R,np.eye(d,dtype=np.int64)],axis=1)
 for c in range(d):
  p=next(i for i in range(c,d) if aug[i,c])
  if p!=c:aug[[c,p]]=aug[[p,c]]
  if aug[c,c]==2:aug[c]=(2*aug[c])%P
  for i in range(d):
   if i!=c and aug[i,c]:aug[i]=(aug[i]-aug[i,c]*aug[c])%P
 return rows,aug[:,d:]

assert rank3(N)==10
idx,S=indep_cols(N)
rows,L=coords_setup(S)
UA=[]
for g in A:
 AS=(g@S)%P; C=(L@AS[rows])%P
 assert np.array_equal((S@C)%P,AS)
 UA.append(C)

def cyc(v):
 basis=[];q=[np.array(v,dtype=np.int64)%P];rank=0
 while q:
  x=q.pop()
  if basis:
   nr=rank3(np.column_stack(basis+[x]))
  else:nr=rank3(x[:,None])
  if nr<=rank:continue
  basis.append(x);rank=nr
  if rank==d:return d
  for g in UA:q.append((g@x)%P)
 return rank

cnt={i:0 for i in range(1,d+1)};fail=[]
for v in product(range(P),repeat=d):
 if not any(v):continue
 k=cyc(v);cnt[k]+=1
 if k<d and len(fail)<10:fail.append((v,k))
checked=P**d-1
assert sum(cnt.values())==checked
print('PHASE 2-4A: exhaustive irreducibility test for U=im(N)')
print('rank(N)=',rank3(N));print('U dimension=',d);print('basis columns=',idx)
print('coordinate rows=',rows);print('vectors checked=',checked)
print('distribution=',{k:v for k,v in cnt.items() if v})
print('min dimension=',min(k for k,v in cnt.items() if v));print('max dimension=',max(k for k,v in cnt.items() if v))
print('all nonzero vectors generate U=',cnt[d]==checked);print('failures=',fail)
assert cnt[d]==checked
print('CONCLUSION: U=im(N) is irreducible as an F_3[Sp_4(F_3)]-module.')
