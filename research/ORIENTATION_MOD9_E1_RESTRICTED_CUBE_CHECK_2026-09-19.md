# E1 RESTRICTED-CUBE CROSS-TERM CHECK — 2026-09-19

## Question

Does a degree-2 correction \(Q_i\in L_2\) alter the degree-3 restricted-power component \(X_i^{[3]}\)?

## Degree argument

In the associated graded restricted Lie algebra, the restricted operation has homogeneous degree multiplication by 3. For homogeneous \(X\) of degree 1 and \(Q\) of degree 2,
\[
(X+Q)^{[3]}=X^{[3]}+Q^{[3]}+\sum s_j(X,Q).
\]
Here \(Q^{[3]}\) has degree 6. Every mixed Jacobson term \(s_j(X,Q)\) contains three total homogeneous factors in the cubic operation; with at least one occurrence of \(Q\), its total degree is at least
\[
1+1+2=4.
\]
Equivalently, in the Magnus associative expansion, every mixed word containing one degree-2 correction and two degree-1 factors has total degree 4, while the pure cube has degree 3. Hence
\[
(X+Q)^{[3]}\equiv X^{[3]}\pmod{L_{\ge4}}.
\]

Thus the earlier *conclusion* that the degree-3 restricted-power term is unchanged was correct, but the proof should be stated as a filtered-degree argument for the cubic restricted operation, not as an informal statement about substituting into an arbitrary degree-3 homogeneous polynomial.

## Consequence for E1

With \(Q_i=c_iR_2\), the degree-3 power component contributes no new degree-3 term. The only degree-3 change comes from applying the generator correction to the quadratic commutator relation, which is
\[
\delta R_2=[v,R_2].
\]
A common relation-generator unit multiplies both components by \(u\). Therefore
\[
(R_2,P_3)\mapsto(uR_2,uP_3+[v,R_2])
\]
modulo degree \(\ge4\).

Since degree-one evaluation kills \([v,R_2]\),
\[
\Theta\mapsto u\Theta.
\]

## Strict status

- restricted-cube cross-term check: **PASS / CLOSED**;
- degree-(2,3) residual-gauge lemma: **PASS / CLOSED, conditional on the standard minimal one-relator presentation input**;
- full relation-module canonicity: **FAIL** (the explicit stabilizing lift still changes its generator by a unit);
- projective degree-(2,3) recovery observable naturality: **PASS / CLOSED under the stated hypotheses**;
- universal higher-degree intrinsic tower: **OPEN**.

This calculation supersedes the temporary reopening in the immediately preceding re-audit: the alleged obstruction was a degree-counting false alarm. The relevant mixed cubic terms begin in degree 4, not degree 3.
