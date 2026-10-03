#!/usr/bin/env python3
"""Independent base-case check for the corrected intrinsic W10 Schreier calculation.

Model: p=3, s=2, r=z^9*x^-9*[x,y]^-1.
Basis: (u,a0,a1,a2,b0,b1,b2), u=z^3.
"""

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

# RS abelianization relations: 3u - 9 a_i = 0, i=0,1,2.
A = sp.zeros(3, 7)
for i in range(3):
    A[i, 0] = 3
    A[i, i + 1] = -9

S = smith_normal_form(A, domain=ZZ)
assert [S[i, i] for i in range(3)] == [3, 9, 9]

# sigma fixes u and cycles each of a0,a1,a2 and b0,b1,b2.
P = sp.zeros(7)
P[0, 0] = 1
for base in (1, 4):
    P[base + 1, base] = 1
    P[base + 2, base + 1] = 1
    P[base, base + 2] = 1

D2 = (P - sp.eye(7)) ** 2
v = sp.Matrix([0, 1, 0, 0, 0, 0, 0])
w = D2 * v

# Mod 3: delta^2(a0) = a0+a1+a2.
assert [int(x) % 3 for x in w] == [0, 1, 1, 1, 0, 0, 0]

# Integral nonvanishing of 3*delta^2(a0): test membership in row lattice A.
target = sp.Matrix([[0, 3, 3, 3, 0, 0, 0]])
# Solve A^T c = target^T over Q and check there is no solution.
assert sp.linsolve((A.T, target.T)) == sp.EmptySet

print("SNF =", S)
print("P =")
print(P)
print("(sigma-1)^2(a0) =", list(w))
print("3*(sigma-1)^2(a0) is nonzero in the RS abelianization lattice.")
