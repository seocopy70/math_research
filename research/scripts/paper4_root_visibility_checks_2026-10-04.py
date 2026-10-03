"""Independent checks for Paper 4 root-visibility/non-rigidity audit (2026-10-04)."""
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def snf_invariants(p,s,a,d):
    A=sp.zeros(d+2,d+1)
    for i in range(d+1):
        A[i,i]=p**(s+1)
    A[d+1,0]=p**s
    A[d+1,1]=-p**a
    S=smith_normal_form(A, domain=ZZ)
    return [abs(S[i,i]) for i in range(min(S.shape)) if S[i,i] != 0]

cases=[(3,2,1,2),(3,3,2,2),(5,2,1,4),(3,5,2,2),(3,2,2,2)]
for p,s,a,d in cases:
    got=snf_invariants(p,s,a,d)
    expected=[p**a]+[p**(s+1)]*d
    assert got==expected, (p,s,a,d,got,expected)
    print((p,s,a,d), "PASS", got)

for p,s in [(3,1),(3,2),(5,2),(3,3)]:
    assert p**s >= 3
print("delayed-window filtration check: PASS")
