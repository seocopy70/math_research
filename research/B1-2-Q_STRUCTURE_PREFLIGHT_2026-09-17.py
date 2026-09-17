import runpy
import subprocess
import tempfile
import os
import numpy as np

P = 3
ROOT = 'research/'
ns = runpy.run_path(ROOT + 'phase2_1_invariant_space_verification_2026-09-15.py')
ns3 = runpy.run_path(ROOT + 'phase2_3_endH_optimized_2026-09-15.py')
A = [np.array(x, dtype=np.int64) % P for x in ns['action_matrices']]
N = np.array(ns3['N'], dtype=np.int64) % P
rank3 = ns['rank3']
B = np.array(ns['B'], dtype=np.int64) % P
basisW = [dict(x) for x in ns['basis']]
vec4 = ns['vec4']
gens = ns['gens']
apply_linear_map = ns['apply_linear_map']
bracket = ns['bracket']

assert len(A) == 5 and all(g.shape == (45,45) for g in A)
assert rank3(N) == 10
assert np.array_equal((N @ N) % P, np.zeros_like(N))
assert all(np.array_equal((N @ g) % P, (g @ N) % P) for g in A)

# W_d and W in the authoritative L4 coordinates.
d = bracket({(1,1,1): 1}, {(2,): 1})
wd = np.empty((256,0), dtype=np.int64)
queue = [d]; seen = set()
while queue:
    a = queue.pop(0)
    key = tuple(sorted(a.items()))
    if key in seen: continue
    seen.add(key)
    v = vec4(a)
    if rank3(np.column_stack([wd,v])) > rank3(wd):
        wd = np.column_stack([wd,v])
    for g in gens: queue.append(apply_linear_map(a,g))
assert rank3(wd) == 45
W = np.column_stack([vec4(a) for a in basisW])
assert rank3(W) == 45

# F3 nullspace of N; K is ker(N) inside W.
def nullspace3(M):
    M=np.array(M,dtype=np.int64)%P
    m,n=M.shape; R=M.copy(); piv=[]; r=0
    for c in range(n):
        p=next((i for i in range(r,m) if R[i,c]),None)
        if p is None: continue
        R[[r,p]]=R[[p,r]]
        if R[r,c]==2: R[r]=(2*R[r])%P
        for i in range(m):
            if i!=r and R[i,c]: R[i]=(R[i]-R[i,c]*R[r])%P
        piv.append(c); r+=1
        if r==m: break
    free=[c for c in range(n) if c not in piv]
    out=[]
    for f in free:
        x=np.zeros(n,dtype=np.int64); x[f]=1
        for i,c in enumerate(piv): x[c]=(-R[i,f])%P
        out.append(x)
    return np.column_stack(out)

K=(W @ nullspace3(N))%P
assert rank3(K)==35
assert rank3(np.column_stack([W,wd]))==55
assert rank3(np.column_stack([K,wd]))==45

# Extend K to a 60D basis and obtain the quotient L4/K action.
def inverse3(M):
    M=np.array(M,dtype=np.int64)%P; n=M.shape[0]
    aug=np.concatenate([M,np.eye(n,dtype=np.int64)],axis=1)
    for c in range(n):
        p=next((i for i in range(c,n) if aug[i,c]),None)
        if p is None: raise ValueError('singular F3 matrix')
        aug[[c,p]]=aug[[p,c]]
        if aug[c,c]==2: aug[c]=(2*aug[c])%P
        for i in range(n):
            if i!=c and aug[i,c]: aug[i]=(aug[i]-aug[i,c]*aug[c])%P
    return aug[:,n:]

C=K.copy(); rc=rank3(C)
for j in range(B.shape[1]):
    T=np.column_stack([C,B[:,j]]); nr=rank3(T)
    if nr>rc: C=T; rc=nr
    if rc==60: break
assert rc==60
rows=[]; Rsel=np.empty((0,60),dtype=np.int64); rr=0
for i in range(256):
    T=np.vstack([Rsel,C[i:i+1,:]]); nr=rank3(T)
    if nr>rr: rows.append(i); Rsel=T; rr=nr
    if rr==60: break
assert rr==60
Bsel=B[rows,:]
C_in_B=(inverse3(Bsel) @ C[rows,:])%P
Ci=inverse3(C_in_B)
Qgens=[]
for ga in A:
    Ab=np.zeros((60,60),dtype=np.int64); Ab[:15,:15]=np.eye(15,dtype=np.int64); Ab[15:,15:]=ga
    Ca=(Ci @ Ab @ C_in_B)%P
    assert np.all(Ca[35:,:35]==0)
    Qgens.append(Ca[35:,35:])
assert all(q.shape == (25,25) and rank3(q) <= 25 for q in Qgens)

# GAP row/right action: transpose authoritative column-action matrices.
def gap_rows(M):
    return '['+','.join('['+','.join(str(int(x)%P) for x in row)+']' for row in M.tolist())+']'
def gap_list(mats): return '['+','.join(gap_rows(M.T) for M in mats)+']'
raw=gap_list(Qgens)
code=r'''F := GF(3);;
Raw := %s;;
Gens := List(Raw,m->ImmutableMatrix(F,List(m,r->List(r,x->One(F)*x))));;
M := GModuleByMats(Gens,F);;
Print("B1-2 Q STRUCTURE PREFLIGHT\n");
Qdim := Length(Gens[1]);;
if not ForAll(Gens,g->Length(g)=Qdim) then Error("inconsistent Q generator dimensions"); fi;
Print("Q_DIM = ",Qdim,"\n");
Print("Q_INDECOMPOSABLE = ",MTX.IsIndecomposable(M),"\n");
Print("Q_SIMPLE = ",MTX.IsIrreducible(M),"\n");
mins := MTX.BasesMinimalSubmodules(M);;
Print("MINIMAL_COUNT = ",Length(mins),"\n");
Print("MINIMAL_DIMS = ",List(mins,Length),"\n");
QUIT;
''' % raw
with tempfile.NamedTemporaryFile('w',suffix='.g',delete=False,encoding='utf-8') as f:
    f.write(code); path=f.name
try:
    p=subprocess.run(['gap','-q',path],text=True,capture_output=True)
finally:
    os.unlink(path)
print(p.stdout,end='')
if p.stderr: print('--- GAP STDERR ---\n'+p.stderr,end='')
if p.returncode!=0 or 'Error,' in p.stdout or 'Error,' in p.stderr:
    raise SystemExit('B1-2 Q structure preflight failed')
print('B1_2_Q_STRUCTURE_PREFLIGHT_PASS = true')
