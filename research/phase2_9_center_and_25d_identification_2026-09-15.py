"""Phase 2-9: center obstruction and literature-level identification of M.

Purpose:
1. Record an exact certificate that the central element -I of Sp4(F3)
   acts trivially on every homogeneous degree-4 Lie piece over F3.
2. Therefore the 25-dimensional irreducible module M from Phase 2-8B
   factors through PSp4(3)=Sp4(3)/{+-I}.
3. This rules out identifying M with a highest-weight module whose center
   acts nontrivially (in particular, the naive L(2,1) identification must
   not be asserted without checking conventions).

The literature check is recorded separately in the accompanying result file.
This script does not claim a highest-weight label for M.
"""

P = 3
DEGREE = 4
CENTER_SCALAR = -1 % P
CENTER_ON_DEGREE4 = pow(CENTER_SCALAR, DEGREE, P)

assert CENTER_SCALAR == 2
assert CENTER_ON_DEGREE4 == 1

print("PHASE 2-9 / CENTER CHECK")
print("center element = -I in Sp4(F3)")
print("scalar on generators =", CENTER_SCALAR)
print("degree =", DEGREE)
print("scalar on homogeneous degree-4 Lie monomials =", CENTER_ON_DEGREE4)
print("CENTER_ACTS_TRIVIALLY_ON_L4 =", CENTER_ON_DEGREE4 == 1)
print("CENTER_ACTS_TRIVIALLY_ON_Q4 =", CENTER_ON_DEGREE4 == 1)
print("CENTER_ACTS_TRIVIALLY_ON_W =", CENTER_ON_DEGREE4 == 1)
print("CENTER_ACTS_TRIVIALLY_ON_M =", CENTER_ON_DEGREE4 == 1)
print()
print("CONCLUSION:")
print("M factors through PSp4(3) = Sp4(3)/{+-I}.")
print("Do NOT identify M with L(2,1) merely from dimension 25.")
print("A literature-level 25-dimensional PSp4(3)-simple-module identification is the next safe label.")
