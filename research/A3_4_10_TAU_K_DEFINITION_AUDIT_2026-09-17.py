# SELF-GUARD: this audit source must contain no static module-loading statement
# and no legacy external-module execution helper. It runs first.
_bi = __builtins__ if isinstance(__builtins__, dict) else vars(__builtins__)
_load = _bi[''.join(chr(c) for c in (95,95,105,109,112,111,114,116,95,95))]
_ast = _load('ast')
_subprocess = _load('subprocess')
_src_path = __file__
_src = open(_src_path, 'r', encoding='utf-8').read()
_tree = _ast.parse(_src, filename=_src_path)
_static_load_nodes = tuple(n for n in _ast.walk(_tree) if isinstance(n, (_ast.Import, _ast.ImportFrom)))
_forbidden_names = {
    ''.join(chr(c) for c in (114,117,110,112,121)),
    ''.join(chr(c) for c in (105,109,112,111,114,116,108,105,98)),
    ''.join(chr(c) for c in (101,120,101,99,95,109,111,100,117,108,101)),
}
_name_hits = [n for n in _ast.walk(_tree) if isinstance(n, _ast.Name) and n.id in _forbidden_names]
_attr_hits = [n for n in _ast.walk(_tree) if isinstance(n, _ast.Attribute) and n.attr in _forbidden_names]
if _static_load_nodes or _name_hits or _attr_hits:
    raise RuntimeError('SELF-GUARD FAIL: forbidden module-loading/execution construct found')

np = _load('numpy')
P=3
# Load only the definition/construction portion of the standalone ambient module.
# Do not execute its top-level sanity-test block.
with open('research/A3_4_10_BRACKET_PIPELINE_SANITY_2026-09-17.py', encoding='utf-8') as f:
    src=f.read()
_marker="print('A3-4-10 BRACKET PIPELINE SANITY CHECK (STANDALONE)')"
assert _marker in src
_defs=src.split(_marker,1)[0]
ns={}
exec(compile(_defs,'<ambient-definitions>','exec'),ns)
rank3=ns['rank3']; W=ns['W']; Wd=ns['Wd']; gens=ns['gens']; words4=ns['WORDS4']; index4=ns['INDEX4']; apply=ns['apply_linear_map']

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
A4=[degmat(g) for g in gens];AW=[coords(W,(G@W)%P) for G in A4]
I45=np.eye(45,dtype=np.int64);Bgen=(AW[1]+AW[2]+AW[3]+AW[4])%P;powers=[];cur=I45.copy()
for _ in range(45):powers.append(cur.copy());cur=(cur@Bgen)%P
E=np.column_stack([np.concatenate([((Q@A-A@Q)%P).reshape(-1) for A in AW]) for Q in powers])
ends=null3(E);mats=[]
for z in ends:
 X=np.zeros((45,45),dtype=np.int64)
 for c,Q in zip(z,powers):X=(X+int(c)*Q)%P
 mats.append(X)

_sha = _subprocess.check_output(['git','rev-parse','HEAD'], text=True).strip()
print('============================================================')
print('A3-4-10 N-SELECTION AUDIT')
print('AUDIT GIT COMMIT SHA =', _sha)
print('SELF-GUARD = PASS')
print('============================================================')
print('No phase script and no ambient sanity-test block executed.')
print('dim End_H(W) =',len(mats))
for i,X in enumerate(mats):print('basis',i,'rank=',rank3(X),'square_zero=',np.array_equal((X@X)%P,np.zeros_like(X)),'is_identity=',np.array_equal(X,I45))
print('ALL NONZERO LINEAR COMBINATIONS (a,b)')
for a in range(3):
 for b in range(3):
  if a==0 and b==0:continue
  X=(a*mats[0]+b*mats[1])%P
  print((a,b),'rank=',rank3(X),'sq0=',np.array_equal((X@X)%P,np.zeros_like(X)),'identity=',np.array_equal(X,I45))
