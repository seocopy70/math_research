import runpy, numpy as np
P=3; R='research/'
def rank3(A):
 A=np.array(A,dtype=np.int64,copy=True)%P; m,n=A.shape if A.ndim==2 else (len(A),1); A=A if A.ndim==2 else A[:,None]; r=0
 for c in range(n):
  q=next((i for i in range(r,m) if A[i,c]),None)
  if q is None: continue
  A[[r,q]]=A[[q,r]]
  if A[r,c]==2:A[r]=(2*A[r])%P
  for i in range(m):
   if i!=r and A[i,c]:A[i]=(A[i]-A[i,c]*A[r])%P
  r+=1
  if r==m:break
 return r
def null3(A):
 A=np.array(A,dtype=np.int64,copy=True)%P;m,n=A.shape;Rr=A.copy();p=[];r=0
 for c in range(n):
  q=next((i for i in range(r,m) if Rr[i,c]),None)
  if q is None:continue
  Rr[[r,q]]=Rr[[q,r]]
  if Rr[r,c]==2:Rr[r]=(2*Rr[r])%P
  for i in range(m):
   if i!=r and Rr[i,c]:Rr[i]=(Rr[i]-Rr[i,c]*Rr[r])%P
  p.append(c);r+=1
  if r==m:break
 return [np.array([1 if j==f else ((-Rr[rr,f])%P if j==c else 0) for j,c in enumerate(range(n))],dtype=np.int64) for f in []]
# fresh nullspace, compact
def nsnull(A):
 A=np.array(A,dtype=np.int64)%P;m,n=A.shape;Rr=A.copy();p=[];r=0
 for c in range(n):
  q=next((i for i in range(r,m) if Rr[i,c]),None)
  if q is None:continue
  Rr[[r,q]]=Rr[[q,r]]
  if Rr[r,c]==2:Rr[r]=(2*Rr[r])%P
  for i in range(m):
   if i!=r and Rr[i,c]:Rr[i]=(Rr[i]-Rr[i,c]*Rr[r])%P
  p.append(c);r+=1
  if r==m:break
 out=[]
 for f in [j for j in range(n) if j not in p]:
  x=np.zeros(n,dtype=np.int64);x[f]=1
  for rr,c in enumerate(p):x[c]=(-Rr[rr,f])%P
  out.append(x)
 return out
ns=runpy.run_path(R+'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
W=np.array(ns['W'],dtype=np.int64)%P; I=np.array(ns['I_W'],dtype=np.int64)%P; K=np.array(ns['K_coord'],dtype=np.int64)%P; AW=[np.array(a,dtype=np.int64)%P for a in ns['A_W']]; Dt=np.vstack([np.array(d,dtype=np.int64)%P for d in ns['diffs']])
ns12=runpy.run_path(R+'A3-4-12_IMAGE_INTERSECTION_DELTA_U_DELTA_TAU_2026-09-16.py'); Du=np.array(ns12['D_u'],dtype=np.int64)%P
assert rank3(Dt)==45 and rank3(Du)==10 and rank3(np.column_stack([Dt,Du]))==45
# Choose A + 35 tau columns afresh.
def addcols(M,target):
 B=np.empty((M.shape[0],0),dtype=np.int64);idx=[];r=0
 for j in range(M.shape[1]):
  T=np.column_stack([B,M[:,j]]);rr=rank3(T)
  if rr>r:B=T;idx.append(j);r=rr
  if r==target:break
 return idx,B
ia,A=addcols(Du,10);C=A.copy();qi=[];r=10
for j in range(45):
 T=np.column_stack([C,Dt[:,j]]);rr=rank3(T)
 if rr>r:C=T;qi.append(j);r=rr
 if r==45:break
assert len(qi)==35
# Independent coordinate solver using augmented elimination.
def solve(C,y):
 M=np.column_stack([C,np.array(y,dtype=np.int64)%P]);r=0;p=[]
 for c in range(45):
  q=next(i for i in range(r,M.shape[0]) if M[i,c]);M[[r,q]]=M[[q,r]]
  if M[r,c]==2:M[r]=(2*M[r])%P
  for i in range(M.shape[0]):
   if i!=r and M[i,c]:M[i]=(M[i]-M[i,c]*M[r])%P
  p.append(c);r+=1
 z=np.zeros(45,dtype=np.int64)
 for rr,c in enumerate(p):z[c]=M[rr,-1]
 assert np.array_equal((C@z)%P,y%P);return z
# Import only the already independently verified ambient action.
ns6=runpy.run_path(R+'A3-4-13_6_TRUE_AMBIENT_EQUIVARIANCE_2026-09-16.py'); tr=ns6['transform_hom_column']
S=[]
for gi in range(5):
 M=np.zeros((35,35),dtype=np.int64)
 for j in range(35):M[:,j]=solve(C,tr(Dt,gi,qi[j]))[10:]
 S.append(M%P)
T=[]
for g in AW:
 M=np.zeros((35,35),dtype=np.int64)
 for j in range(35):M[:,j]=solve(K,(g@K[:,j])%P)
 T.append(M%P)
# Fresh intertwiner system, column-major.
blocks=[]
for s,t in zip(S,T):
 Z=np.zeros((1225,1225),dtype=np.int64)
 for a in range(35):
  for b in range(35):
   E=np.zeros((35,35),dtype=np.int64);E[a,b]=1;Z[:,a+35*b]=((E@s-t@E)%P).reshape(-1,order='F')
 blocks.append(Z)
V=nsnull(np.vstack(blocks)%P);mr=max(rank3(v.reshape(35,35,order='F')) for v in V)
print('A3-4-13.7 / INDEPENDENT B/A VS K CHECK')
print('dim B =',rank3(Dt));print('dim A =',rank3(Du));print('dim(B/A) =',len(qi));print('dim K =',rank3(K));print('I = K ambient =',rank3(np.column_stack([I,K]))==35);print('independent Hom_H nullity =',len(V));print('maximum intertwiner rank =',mr);print('FULL_RANK_INTERTWINER_FOUND =',mr==35);print('RESULT:', 'B/A is H-isomorphic to K=I.' if mr==35 else 'B/A is NOT H-isomorphic to K by the independent intertwiner test.');assert len(V)==1 and mr==10;print('INDEPENDENT CHECK CONFIRMS THE 10/35 INTERTWINER-RANK RESULT');print('ALL A3-4-13.7 CHECKS COMPLETED')
