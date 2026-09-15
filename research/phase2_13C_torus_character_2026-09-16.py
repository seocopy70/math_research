"""Phase 2-13C: torus character of the unique U^+(F3)-fixed line."""
from pathlib import Path
import runpy
import numpy as np

P=3
ROOT=Path(__file__).resolve().parents[1]

# Reuse the authoritative corrected quotient construction from Phase 2-13B.
ns=runpy.run_path(str(ROOT/'research'/'phase2_13B_positive_unipotent_2026-09-15.py'))
quotient_action_single=ns['quotient_action_single']
fixed=ns['fixed']
Pmat=ns['Pmat']; Pinv=ns['Pinv']; J=ns['J']

assert len(fixed)==1
v=np.array(fixed[0],dtype=np.int64)%P

# Standard C2 split torus: diag(a,b,a^{-1},b^{-1}).
# Over F3, a,b are 1 or 2=-1, so there are four elements.
def torus(a,b):
    ai=pow(int(a),-1,P); bi=pow(int(b),-1,P)
    d=np.diag([a,b,ai,bi]).astype(np.int64)%P
    return (Pmat@d@Pinv)%P

def scalar_on_line(A,v):
    Av=(A@v)%P
    nz=np.flatnonzero(v)
    assert len(nz)>0
    i=int(nz[0])
    lam=int(Av[i])
    assert np.all((Av-lam*v)%P==0)
    return lam

rows=[]
for a in [1,2]:
    for b in [1,2]:
        g=torus(a,b)
        symp=np.array_equal((g.T@J@g)%P,J)
        A=quotient_action_single(g)
        lam=scalar_on_line(A,v)
        rows.append((a,b,lam,symp,A.shape))

print('PHASE 2-13C / TORUS CHARACTER OF U+-FIXED LINE')
print('fixed-line dimension =',len(fixed))
print('standard C2 split torus elements = 4')
for r in rows:
    print('a,b =',r[0],r[1],'lambda =',r[2],'symplectic =',r[3],'shape =',r[4])
assert all(r[3] for r in rows)
print('TORUS_CHARACTER_TABLE =',[(a,b,lam) for a,b,lam,_,_ in rows])
print('CERTIFICATE: unique U^+(F3)-fixed line is preserved by the split torus.')
print('INTERPRETATION: this is a finite-field torus character only; no full algebraic highest weight is claimed.')
