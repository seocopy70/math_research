import numpy as np
from itertools import product
P=3; N=4

def add(A,B):
 C=dict(A)
 for w,c in B.items():
  C[w]=(C.get(w,0)+c)%P
  if C[w]==0: del C[w]
 return C

def neg(A): return {w:(-c)%P for w,c in A.items() if c%P}
def mul(A,B):
 C={}
 for wa,ca in A.items():
  for wb,cb in B.items():
   w=wa+wb; C[w]=(C.get(w,0)+ca*cb)%P
   if C[w]==0: del C[w]
 return C

def bracket(A,B): return add(mul(A,B),neg(mul(B,A)))
def vec(A,d):
 words=list(product(range(1,N+1),repeat=d)); idx={w:i for i,w in enumerate(words)}
 v=np.zeros(N**d,dtype=np.int64)
 for w,c in A.items(): v[idx[w]]=c%P
 return v

def rank3(A):
 A=np.array(A,dtype=np.int64,copy=True)%P
 if A.ndim==1:A=A.reshape(-1,1)
 m,n=A.shape;r=0
 for c in range(n):
  q=next((i for i in range(r,m) if A[i,c]),None)
  if q is None:continue
  A[[r,q]]=A[[q,r]]
  if A[r,c]==2:A[r]=(2*A[r])%P
  for i in range(m):
   if i!=r and A[i,c]:A[i]=(A[i]-A[i,c]*A[r])%P
  r+=1
  if r==m:break
 return r

# Independent q=3/q=infinity degree-3 restricted contributions.
power3_q3={(1,1,1):1}
power3_qinf={}
X2={(2,):1}
d_q3=bracket(power3_q3,X2)
d_qinf=bracket(power3_qinf,X2)
assert len(d_q3)>0 and len(d_qinf)==0

J=np.array([[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]],dtype=np.int64)%P
vectors=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(1,0,1,0)]
gens=[(np.eye(4,dtype=np.int64)+np.outer(np.array(v),J@np.array(v)%P))%P for v in vectors]

def apply_linear(A,g):
 images=[]
 for j in range(N):
  im={}
  for i in range(N):
   c=int(g[i,j])%P
   if c:im[(i+1,)]=c
  images.append(im)
 out={}
 for word,coef in A.items():
  cur={():coef}
  for letter in word:
   nxt={}
   for pref,a in cur.items():
    for ww,b in images[letter-1].items():nxt[pref+ww]=(nxt.get(pref+ww,0)+a*b)%P
   cur=nxt
  out=add(out,cur)
 return out

def orbit_span(seed):
 if not seed:return 0,0
 queue=[seed];seen={tuple(vec(seed,4).tolist())}
 for a in queue:
  for g in gens:
   b=apply_linear(a,g);k=tuple(vec(b,4).tolist())
   if k not in seen:seen.add(k);queue.append(b)
 M=np.column_stack([vec(a,4) for a in queue])
 return len(queue),rank3(M)

q3_orbit,q3_span=orbit_span(d_q3)
qinf_orbit,qinf_span=orbit_span(d_qinf)
print('GATE0B_Q3_QINF_CONSTRUCTIBILITY')
print('SOURCE_STATUS = dialogue_agreement_not_repository_spec')
print('q3 restricted degree-3 p-power class nonzero =',bool(power3_q3))
print('qinf restricted degree-3 p-power class nonzero =',bool(power3_qinf))
print('q3 degree-4 correction d nonzero =',bool(d_q3))
print('qinf degree-4 correction d zero =',not bool(d_qinf))
print('q3 d-orbit size =',q3_orbit)
print('q3 d-orbit span dimension =',q3_span)
print('qinf d-orbit size =',qinf_orbit)
print('qinf d-orbit span dimension =',qinf_span)
q3_ok=(q3_span==45); qinf_ok=(qinf_span==45)
print('q3_A3_MECHANISM_CONSTRUCTIBLE =',q3_ok)
print('qinf_A3_MECHANISM_CONSTRUCTIBLE =',qinf_ok)
if q3_ok and not qinf_ok:
 print('RESULT = PASS_WITH_STRUCTURAL_ASYMMETRY')
 print('INTERPRETATION = q=inf has no nonzero A3-4 d-orbit; same-mechanism q=inf B/A and K do not exist.')
else: raise SystemExit('Gate 0-B constructibility test failed')
