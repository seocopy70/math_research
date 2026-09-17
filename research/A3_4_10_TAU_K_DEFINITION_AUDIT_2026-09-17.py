import importlib.util
import numpy as np
P=3
p='research/A3_4_10_BRACKET_PIPELINE_SANITY_2026-09-17.py'
s=importlib.util.spec_from_file_location('a',p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
rank3=m.rank3; W,Wd,gens=m.W,m.Wd,m.gens; words4,index4=m.WORDS4,m.INDEX4; words5,index5=m.WORDS5,m.INDEX5; apply=m.apply_linear_map

def coords(B,Y):
 B=np.array(B,dtype=np.int64)%P; Y=np.array(Y,dtype=np.int64)%P; out=np.zeros((B.shape[1],Y.shape[1]),dtype=np.int64)
 for j in range(Y.shape[1]):
  A=np.column_stack([B,Y[:,j]])%P; r=0;piv=[]
  for c in range(A.shape[1]-1):
   q=next((i for i in range(r,A.shape[0]) if A[i,c]),None)
   if q is None: continue
   A[[r,q]]=A[[q,r]]
   if A[r,c]==2:A[r]=(2*A[r])%P
   for i in range(A.shape[0]):
    if i!=r and A[i,c]:A[i]=(A[i]-A[i,c]*A[r])%P
   piv.append(c);r+=1
  assert len(piv)==B.shape[1]
  for rr,c in enumerate(piv):out[c,j]=A[rr,-1]
 return out

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

def degmat(g):
 G=np.zeros((256,256),dtype=np.int64)
 for j,w in enumerate(words4):
  for ww,c in apply({w:1},g).items():G[index4[ww],j]=(G[index4[ww],j]+int(c))%P
 return G
A4=[degmat(g) for g in gens]; AW=[coords(W,(G@W)%P) for G in A4]; AWd=[coords(Wd,(G@Wd)%P) for G in A4]
# Reproduce canonical N from phase2-3 without importing that phase.
I45=np.eye(45,dtype=np.int64); Bgen=(AW[1]+AW[2]+AW[3]+AW[4])%P;powers=[];cur=I45.copy()
for _ in range(45):powers.append(cur.copy());cur=(cur@Bgen)%P
Ecols=[]
for Q in powers:Ecols.append(np.concatenate([((Q@A-A@Q)%P).reshape(-1) for A in AW]))
ends=null3(np.column_stack(Ecols)); mats=[]
for z in ends:
 X=np.zeros((45,45),dtype=np.int64)
 for c,Q in zip(z,powers):X=(X+int(c)*Q)%P
 mats.append(X)
N=next(X for X in mats if not np.array_equal(X,I45));assert rank3(N)==10 and np.array_equal((N@N)%P,np.zeros_like(N))
Kc=null3(N);assert Kc.shape==(45,35)
# I=W intersect Wd
Z=null3(np.column_stack([W,(-Wd)%P]));assert Z.shape[1]==35
Iw=Z[:45,:]; Iwd=Z[45:,:]; Iamb=(W@Iw)%P
Kamb=(W@Kc)%P
# Exact containment/equality diagnostics.
stack=np.column_stack([Iamb,Kamb])
print('A3-4-10 K DEFINITION AUDIT')
print('dim W45 =',rank3(W),'dim Wd =',rank3(Wd))
print('dim I =',rank3(Iamb),'dim ker(N) =',rank3(Kc))
print('rank([I | K]) =',rank3(stack))
print('K subset I =',rank3(stack)==35)
print('K equals I =',np.array_equal(Iamb,Kamb))
# If K is actually inside Wd, recover its Wd coordinates; otherwise stop cleanly.
if rank3(np.column_stack([Wd,Kamb]))!=45:
 print('K_IN_Wd = False; cannot reproduce old K-target tau equation.')
 print('RESULT = AUDIT_REQUIRES_REVIEW')
else:
 Kw=coords(Wd,Kamb);print('K_IN_Wd = True')
 n=45;rows=[];rhs=[];idx=lambda r,c:r*n+c
 for A,Ad in zip(AW,AWd):
  for r in range(n):
   for c in range(n):
    row=np.zeros(n*n,dtype=np.int64)
    for k in range(n):row[idx(k,c)]=(row[idx(k,c)]+Ad[r,k])%P;row[idx(r,k)]=(row[idx(r,k)]-A[k,c])%P
    rows.append(row);rhs.append(0)
 for r in range(n):
  for c in range(35):
   row=np.zeros(n*n,dtype=np.int64)
   for k in range(n):row[idx(r,k)]=(row[idx(r,k)]+Iw[k,c])%P
   rows.append(row);rhs.append(int(Kw[r,c]))
 R=np.column_stack([np.array(rows,dtype=np.int64)%P,np.array(rhs,dtype=np.int64)[:,None]%P]);r=0;piv=[]
 for c in range(n*n):
  q=next((i for i in range(r,R.shape[0]) if R[i,c]),None)
  if q is None:continue
  R[[r,q]]=R[[q,r]]
  if R[r,c]==2:R[r]=(2*R[r])%P
  for i in range(R.shape[0]):
   if i!=r and R[i,c]:R[i]=(R[i]-R[i,c]*R[r])%P
  piv.append(c);r+=1
  if r==R.shape[0]:break
 assert not any(np.all(R[i,:-1]==0) and R[i,-1] for i in range(r,R.shape[0]))
 tau=np.zeros(n*n,dtype=np.int64)
 for rr,c in enumerate(piv):tau[c]=R[rr,-1]
 tau=tau.reshape((45,45))%P
 print('tau system rank =',len(piv),'nullity =',n*n-len(piv),'tau rank =',rank3(tau))
 print('TAU_INTERTWINER =',all(np.array_equal((Ad@tau)%P,(tau@A)%P) for A,Ad in zip(AW,AWd)))
 print('TAU_MAPS_I_TO_K =',np.array_equal((tau@Iw)%P,Kw))
 def bm(M,h):
  B=np.zeros((1024,45),dtype=np.int64)
  for j in range(45):
   for k,c0 in enumerate(M[:,j]):
    c=int(c0)%P
    if c:
     w=words4[k];B[index5[w+(h,)],j]=(B[index5[w+(h,)],j]+c)%P;B[index5[(h,)+w],j]=(B[index5[(h,)+w],j]-c)%P
  return B
 obs=[]
 for h in range(4):obs.append((bm(Wd,h)@tau-bm(W,h))%P)
 print('TAU_BRACKET_OBSTRUCTION_RANK =',rank3(np.vstack(obs)))
 print('RESULT = AUDIT_COMPLETE')
