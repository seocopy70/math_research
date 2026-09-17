import importlib.util
import numpy as np
P=3
p='research/A3_4_10_BRACKET_PIPELINE_SANITY_2026-09-17.py'
s=importlib.util.spec_from_file_location('a',p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
rank3=m.rank3; W,Wd,gens=m.W,m.Wd,m.gens; words4,index4=m.WORDS4,m.INDEX4; words5,index5=m.WORDS5,m.INDEX5; apply=m.apply_linear_map

def null3(A):
 A=np.array(A,dtype=np.int64,copy=True)%P;m0,n=A.shape;r=0;piv=[]
 for c in range(n):
  q=next((i for i in range(r,m0) if A[i,c]),None)
  if q is None:continue
  A[[r,q]]=A[[q,r]]
  if A[r,c]==2:A[r]=(2*A[r])%P
  for i in range(m0):
   if i!=r and A[i,c]:A[i]=(A[i]-A[i,c]*A[r])%P
  piv.append(c);r+=1
  if r==m0:break
 Z=np.zeros((n,n-len(piv)),dtype=np.int64);free=[c for c in range(n) if c not in piv]
 for j,f in enumerate(free):
  Z[f,j]=1
  for rr,c in enumerate(piv):Z[c,j]=(-A[rr,f])%P
 return Z

def coords(B,Y):
 B=np.array(B,dtype=np.int64)%P;Y=np.array(Y,dtype=np.int64)%P;out=np.zeros((B.shape[1],Y.shape[1]),dtype=np.int64)
 for j in range(Y.shape[1]):
  A=np.column_stack([B,Y[:,j]])%P;r=0;piv=[]
  for c in range(A.shape[1]-1):
   q=next((i for i in range(r,A.shape[0]) if A[i,c]),None)
   if q is None:continue
   A[[r,q]]=A[[q,r]]
   if A[r,c]==2:A[r]=(2*A[r])%P
   for i in range(A.shape[0]):
    if i!=r and A[i,c]:A[i]=(A[i]-A[i,c]*A[r])%P
   piv.append(c);r+=1
  assert len(piv)==B.shape[1]
  for rr,c in enumerate(piv):out[c,j]=A[rr,-1]
 return out

def degmat(g):
 G=np.zeros((256,256),dtype=np.int64)
 for j,w in enumerate(words4):
  for ww,c in apply({w:1},g).items():G[index4[ww],j]=(G[index4[ww],j]+int(c))%P
 return G
A4=[degmat(g) for g in gens];AW=[coords(W,(G@W)%P) for G in A4];AWd=[coords(Wd,(G@Wd)%P) for G in A4]
I45=np.eye(45,dtype=np.int64);Bgen=(AW[1]+AW[2]+AW[3]+AW[4])%P;powers=[];cur=I45.copy()
for _ in range(45):powers.append(cur.copy());cur=(cur@Bgen)%P
E=np.column_stack([np.concatenate([((Q@A-A@Q)%P).reshape(-1) for A in AW]) for Q in powers])
ends=null3(E);mats=[]
for z in ends:
 X=np.zeros((45,45),dtype=np.int64)
 for c,Q in zip(z,powers):X=(X+int(c)*Q)%P
 mats.append(X)
print('A3-4-10 N-SELECTION AUDIT')
print('dim End_H(W) =',len(mats))
for i,X in enumerate(mats):print('basis',i,'rank=',rank3(X),'square_zero=',np.array_equal((X@X)%P,np.zeros_like(X)),'is_identity=',np.array_equal(X,I45))
print('ALL NONZERO LINEAR COMBINATIONS (a,b)')
for a in range(3):
 for b in range(3):
  if a==0 and b==0:continue
  X=(a*mats[0]+b*mats[1])%P
  print((a,b),'rank=',rank3(X),'sq0=',np.array_equal((X@X)%P,np.zeros_like(X)),'identity=',np.array_equal(X,I45))
