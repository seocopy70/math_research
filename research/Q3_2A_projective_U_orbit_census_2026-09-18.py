"""Q3-2A: projective H-orbit census on U = im(N).

Structural investigation only. No q=3/q=infinity decision is made here.
The target invariant candidate is the H-orbit type of the projective line [N(d_3)] in P(U).
"""
from pathlib import Path
import runpy, json, itertools
import numpy as np

P = 3
ROOT = Path(__file__).parent
ART = ROOT / "artifacts"

ns = runpy.run_path(str(ROOT / "O2_7_q_control_variation_module_2026-09-18.py"))
N = np.array(ns["N"], dtype=np.int64) % P
A_W = [np.array(A, dtype=np.int64) % P for A in ns["A_W"]]
d_W = np.array(ns["d_W"], dtype=np.int64) % P

def rank3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    if A.ndim == 1: A = A.reshape(-1,1)
    m,n = A.shape; r=0
    for c in range(n):
        piv = next((i for i in range(r,m) if A[i,c]), None)
        if piv is None: continue
        if piv != r: A[[r,piv]] = A[[piv,r]]
        if A[r,c] == 2: A[r] = (2*A[r]) % P
        for i in range(m):
            if i != r and A[i,c]:
                A[i] = (A[i] - A[i,c]*A[r]) % P
        r += 1
        if r == m: break
    return r

def rref_basis(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    if A.ndim == 1: A=A.reshape(-1,1)
    m,n=A.shape; row=0; piv=[]
    for c in range(n):
        p=next((i for i in range(row,m) if A[i,c]),None)
        if p is None: continue
        if p!=row: A[[row,p]]=A[[p,row]]
        if A[row,c]==2: A[row]=(2*A[row])%P
        for i in range(m):
            if i!=row and A[i,c]:
                A[i]=(A[i]-A[i,c]*A[row])%P
        piv.append(c); row+=1
        if row==m: break
    return A[:row], piv

U_rref, piv = rref_basis(N)
U_basis = U_rref.T  # 45 x 10; columns span im(N)
assert rank3(U_basis) == 10

def solve_full_column(A,b):
    A=np.array(A,dtype=np.int64)%P; b=np.array(b,dtype=np.int64)%P
    m,n=A.shape
    aug=np.concatenate([A,b.reshape(m,1)],axis=1)
    row=0; ps=[]
    for c in range(n):
        p=next((i for i in range(row,m) if aug[i,c]),None)
        if p is None: continue
        if p!=row: aug[[row,p]]=aug[[p,row]]
        if aug[row,c]==2: aug[row]=(2*aug[row])%P
        for i in range(m):
            if i!=row and aug[i,c]:
                aug[i]=(aug[i]-aug[i,c]*aug[row])%P
        ps.append(c); row+=1
    if np.any(np.all(aug[:,:n]==0,axis=1)&(aug[:,n]!=0)):
        raise AssertionError("vector not in U")
    x=np.zeros(n,dtype=np.int64)
    for i,c in enumerate(ps): x[c]=aug[i,n]
    assert np.array_equal((A@x)%P,b)
    return x

# Induced H-action on U coordinates.
A_U=[]
for A in A_W:
    cols=np.column_stack([solve_full_column(U_basis,(A@U_basis[:,j])%P) for j in range(10)])
    A_U.append(cols%P)
    assert np.array_equal((U_basis@cols)%P,(A@U_basis)%P)

def line_key(v):
    v=np.array(v,dtype=np.int64)%P
    nz=np.flatnonzero(v)
    if len(nz)==0: raise ValueError("zero vector")
    k=int(nz[0]); scale=1 if v[k]==1 else 2
    return tuple(((scale*v)%P).tolist())

# Enumerate P(U) using first nonzero coordinate normalized to 1.
lines=[]
for vals in itertools.product(range(P), repeat=10):
    if all(x==0 for x in vals): continue
    if next(x for x in vals if x)!=1: continue
    lines.append(tuple(vals))
assert len(lines)==(3**10-1)//2

line_set=set(lines)
def act_line(key,A):
    v=np.array(key,dtype=np.int64)
    return line_key((A@v)%P)

# Full projective orbit census.
unseen=set(line_set)
orbits=[]
while unseen:
    seed=min(unseen)
    orb={seed}
    changed=True
    while changed:
        changed=False
        for x in list(orb):
            for A in A_U:
                y=act_line(x,A)
                if y not in orb:
                    orb.add(y); changed=True
    unseen-=orb
    orbits.append(orb)

orbits.sort(key=lambda o:(len(o),min(o)))

Nd=(N@d_W)%P
nd_coord=solve_full_column(U_basis,Nd)
nd_line=line_key(nd_coord)
target_idx=next(i for i,o in enumerate(orbits) if nd_line in o)

sizes=[len(o) for o in orbits]
artifact={
    "experiment":"Q3-2A",
    "object":"projective H-orbit census on P(U), U=im(N)",
    "field":"F3",
    "dim_U":10,
    "num_projective_lines":len(lines),
    "num_H_orbits":len(orbits),
    "orbit_sizes":sizes,
    "target_line_Nd3":list(nd_line),
    "target_orbit_index":target_idx,
    "target_orbit_size":len(orbits[target_idx]),
    "target_orbit_stabilizer_order_if_H_order_51840":51840//len(orbits[target_idx]),
    "scope":"structural census only; no q=3 vs q=infinity claim",
}
ART.mkdir(exist_ok=True)
(ART/"q3_2a_projective_U_orbit_census.json").write_text(json.dumps(artifact,indent=2),encoding="utf-8")

print("Q3-2A PROJECTIVE U ORBIT CENSUS")
print("dim(U) =",10)
print("|P(U)| =",len(lines))
print("number of H-orbits =",len(orbits))
print("orbit sizes =",sizes)
print("[N(d3)] orbit index =",target_idx)
print("[N(d3)] orbit size =",len(orbits[target_idx]))
print("stabilizer order (using |Sp4(F3)|=51840) =",51840//len(orbits[target_idx]))
print("Q3-2A RESULT = STRUCTURAL CENSUS COMPLETE")
