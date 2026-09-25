# FRESH END-TO-END PROOF AUDIT — 2026-09-25

## Verdict

THEOREM ASSEMBLY: PASS / PROVISIONAL.

A fresh line-by-line attack on the latest paper/main.tex found no fatal logical contradiction and no circularity in the U1 -> U2 -> U3 -> U4 -> U5 -> theorem chain.

## U1 — Zassenhaus

The current Jennings-Lazard formula, the commutator series, the power series, the inequality controlling all i>=2 terms, and the boundary P_{3^(k-1)} nontrivial / P_{3^(k-1)+1}=1 are consistent. Edge cases n=1,2,3,3^(k-1),3^(k-1)+1 were checked.

Status: PASS / CLOSED.

Publication hardening: the sentence that the binomial formula gives S_k^(3^j)=3^j A_k semidirect U_{j+1} is too compressed. Write both inclusions explicitly, using (a,u)^(3^j) and the 3-adic valuation of (u^(3^j)-1)/(u-1).

## U2 — arbitrary candidates

The crossed cocycle plus character is a homomorphism into S_k. Zassenhaus functoriality therefore kills P_{3^(k-1)+1}(G). The twisted H1 isomorphism is correct. The previously hidden target issue is also closed because P_{3^(k-1)+1}(G) is contained in P2(G)=Phi(G), so H1(Q_k,F3) -> H1(G,F3) is an isomorphism; coefficient reduction makes the square commute.

Status: PASS / CLOSED.

## U3 — Fox criterion

The minimal one-relator hypothesis is explicit. The valuation induction is valid: basis-vector lifting gives F_i in 3A_k; if all F_j are in 3^m A_k, the relation equation gives F_i in 3^(m+1) A_k. Iteration gives F_i=0. The converse is immediate.

Status: PASS / CLOSED.

## U4 — k=2 anchor

The four displayed twisted Fox coefficients were independently re-derived from the stated crossed-cocycle convention. They force the unique candidate (1,4,1,1) mod 9. No use of the desired theorem conclusion occurs in this calculation.

Status: PASS / CLOSED.

## U5a/U5b

Reduction is immediate. The coefficient-extension variation calculation is correct at cochain level; the missing rho_k(g) factor disappears modulo 3^k because rho_k(g) is 1 modulo 3. The resulting difference of connecting maps is the socle inclusion applied to nu cup minus.

Status: PASS / CLOSED.

## U5c — PD2

The canonical branch is the only place where the independently known canonical orientation is used. For M=A_{k-1}(chi), the twisted dual tensor the dualizing module becomes the trivial A_{k-1} module. Under natural PD2 duality, the dual of the socle inclusion 1 -> 3^(k-2) is reduction A_{k-1} -> F3. Hence the H2 socle map is injective.

Status: PASS / CLOSED.

Publication hardening: state or cite the exact PD2 duality theorem and explicitly fix the dualizing-module convention. This is not a discovered failure, but it should not remain implicit in a submission manuscript.

## Theorem assembly

Quantifier order is sound: arbitrary rho on Q_k -> transfer to G -> reduce to level 2 -> U4 fixes the base -> U5 fixes every higher digit. Existence comes independently from the classical Kummerian canonical orientation and is transferred back by U2. No desired-theorem conclusion is used to prove U5c.

Status: PASS / PROVISIONAL.

## Remaining gates

1. Harden U1 power valuation proof.
2. Harden/cite U5c PD2 duality.
3. Fresh clean build of exact latest commit 233e92371b7061dc7f3cc6b91e3911a23497d719. Earlier records report successful builds of earlier corrected states; that is not a fresh build of this exact commit.
4. Minimality of P_{3^(k-1)+1}: OPEN.
5. Exact publication novelty: OPEN / CONDITIONAL.

## Final classification

PROOF ARCHITECTURE: PASS.
MANUSCRIPT: NOT YET SUBMISSION-CLOSED.

The remaining work is proof hardening and exact-build verification, not a new mathematical branch.
