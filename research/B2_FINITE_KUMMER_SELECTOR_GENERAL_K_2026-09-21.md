# B2 FINITE KUMMER SELECTOR — GENERAL k (2026-09-21)

## Scope
This document records the proof-level closure of the three mathematical gates in the finite Kummer selector branch:
1. the general lower-3-central window for crossed homomorphisms;
2. the Fox–Kummer equivalence;
3. direct uniqueness/existence in the standard odd-p Demushkin presentation.

The novelty gate is deliberately NOT closed here.

## 1-A. General finite-window factorization

Let
\[
A_k=\mathbf Z/3^k,\qquad U_j=1+3^j\mathbf Z/3^k,
\qquad S_k=A_k\rtimes U_1,
\]
with $(a,u)(b,v)=(a+ub,uv)$.

For
\[
T_j:=3^{j-1}A_k\rtimes U_j
\]
we prove by induction that
\[
P_j(S_k)=T_j.
\]

Base: $T_1=S_k$.

For $(a,u)\in T_j$ and $(b,v)\in S_k$,
\[
[(a,u),(b,v)]=((1-v)a+(u-1)b,1)\in 3^jA_k,
\]
because $a\in3^{j-1}A_k$, $1-v\in3A_k$, and $u-1\in3^jA_k$.
Also
\[
(a,u)^3=(a(1+u+u^2),u^3),
\]
and $1+u+u^2\equiv0\pmod3$, so the $A_k$-component lies in $3^jA_k$, while $u^3\in U_{j+1}$.

Conversely, choosing $v=4$ gives
\[
[(a,1),(0,v)]=((1-v)a,1),
\]
which generates $3^jA_k$, and the cube map on the odd-prime principal-unit filtration gives
\[
U_j^3=U_{j+1}.
\]
Hence $T_{j+1}$ is generated inside $P_{j+1}$, proving equality.

Therefore
\[
P_{k+1}(S_k)=1,\qquad P_k(S_k)=3^{k-1}A_k\ne1.
\]

For any crossed cocycle $z:G\to A_k(\rho)$, the pair
\[
\psi=(z,\rho):G\to S_k
\]
is a homomorphism. Functoriality of the lower 3-central series gives
\[
\psi(P_{k+1}(G))\subseteq P_{k+1}(S_k)=1.
\]
Thus $z$ and $\rho$ factor through
\[
Q_k=G/P_{k+1}(G).
\]
At cochain level this gives equality of the relevant crossed-homomorphism complexes, hence
\[
H^1(G,A_k(\rho))\cong H^1(Q_k,A_k(\bar\rho)),
\]
provided the coefficient character is the induced quotient character.

**Classification: PASS.** This closes the previous load-bearing general-k window claim.

## 2. Fox–Kummer equivalence

Let
\[
G=F/\langle\!\langle r\rangle\!\rangle
\]
be one-relator, and let $\rho(r)=1$. Write $F_i(\rho)$ for the twisted Fox row. A crossed homomorphism with generator values $a=(a_1,\ldots,a_d)$ descends exactly when
\[
\sum_iF_i(\rho)a_i=0.
\]

Let $I=(F_1(\rho),\ldots,F_d(\rho))\subset R=\mathbf Z/3^k$.
If the reduction
\[
H^1(Q_k,R(\rho))\to H^1(Q_k,\mathbf F_3)
\]
is surjective, each basis vector $e_i$ has a lift $a=e_i+3c$. Therefore
\[
F_i+3\sum_jF_jc_j=0,
\]
so $I\subseteq3I$. Since $R$ is local with maximal ideal $(3)$, Nakayama gives $I=0$.

The converse is immediate. Hence
\[
\mathsf K_k(\rho)
\Longleftrightarrow
F_i(\rho)\equiv0\pmod{3^k}\quad\forall i.
\]

**Classification: PASS.** Exhaustive k=2/k=3 computations are retained as independent checks, not as the proof.

## 3. Direct standard-presentation solution

For odd $p=3$ a Demushkin group has the standard presentation
\[
r=x_1^q[x_1,x_2]\cdots[x_{2m-1},x_{2m}],
\]
with $q\in\{0,3,3^2,\ldots\}$ (equivalently the corresponding standard Demushkin invariant).

For a character $\rho$ with values in $1+3\mathbf Z/3^k$, the Fox equations give:

\[
F_{2i}=\rho_{2i-1}^{-1}\rho_{2i}^{-1}(\rho_{2i-1}-1),
\]
hence $\rho_{2i-1}=1$.

For $i>1$,
\[
F_{2i-1}=\rho_{2i-1}^{-1}(\rho_{2i}^{-1}-1),
\]
hence $\rho_{2i}=1$.

Finally
\[
F_1=q+\rho_2^{-1}-1,
\]
so
\[
\rho_2=(1-q)^{-1}.
\]

Because $q$ is divisible by 3 when nonzero, $1-q$ is a unit modulo $3^k$; for $q=0$ this gives $\rho_2=1$.
Thus the solution is unique and equals the reduction of the canonical Demushkin orientation in the standard presentation.

Labute's classification supplies the standard presentation for odd $p$; therefore this gives a classification-dependent extension from the rank-four standard case to arbitrary odd-p Demushkin groups.

**Classification: PASS / LOCAL.**

## 4. Hensel status

The previous Hensel-based proof route is withdrawn as unnecessary for existence/uniqueness in this branch.
The Jacobian/variation calculation remains useful as an independent, representation-aware explanation, but is not a proof dependency for the direct selector theorem.

## 5. What is still open: novelty

The mathematical statement proved here is:

> For odd-p Demushkin groups, the finite quotient $Q_k=G/P_{k+1}(G)$ supports a natural finite Kummer lifting predicate, and in the standard classification this predicate has the unique solution equal to $\chi\bmod p^k$.

However, the underlying Kummerian lifting characterization of the canonical orientation is classical: the literature states surjectivity of
$H^1(G,\mathbf Z_p(\theta)/p^n)\to H^1(G,\mathbf F_p)$ for all $n$ as the Kummerian condition/canonical orientation characterization. Therefore novelty cannot be claimed merely from rewriting that condition.

The remaining novelty question is narrower and precise:

**Is the finite-window factorization/recognition theorem from the intrinsic quotient $Q_k=G/P_{k+1}(G)$, with the predicate defined without inserting $\chi$, $q$, or the dualizing action into the input, already present in the literature?**

This gate remains **OPEN** pending a targeted literature comparison.

## Final classification
- 1-A general finite-window factorization: **PASS**
- Fox–Kummer equivalence: **PASS**
- standard odd-p existence/uniqueness: **PASS / LOCAL**
- arbitrary odd-p Demushkin extension via Labute classification: **PASS / LOCAL**
- Hensel proof dependency: **WITHDRAWN**
- representation-free intrinsic uniqueness independent of classification: **OPEN**
- novelty of the finite-window formulation: **OPEN / DECISIVE**


## 6. Kθ/P_{k+1} literature correction

A later audit corrects the quotient-inheritance discussion. Existing Efrat–Quadrelli/Quadrelli–Weigel quotient results require conditions involving the already-given orientation, such as N⊆Kθ(G) or N⊆ker θ, but this does not prove that P_{k+1} fails those conditions. In particular, for the finite coefficient character θ mod 3^k one has P_{k+1}⊆ker(θ mod 3^k). Therefore the remaining novelty question is specifically whether a finite-coefficient/mod-p^n version, perhaps formulated with K_{θ mod p^n}, already gives the required quotient inheritance. No such theorem has yet been confirmed in the audited sources.

**Correction:** any earlier wording that “excludes” the quotient-inheritance route is HISTORICAL / SUPERSEDED. The mathematical B2 gates remain PASS; novelty is now **OPEN / LOW-LIKELIHOOD — LITERATURE VERIFICATION REQUIRED**.

## 7. One-relator scope stress test

A fresh exhaustive Fox enumeration was run on several non-Demushkin one-relator pro-3 relations at k=2,3. The standard nondegenerate rank-4 Demushkin relation remains uniquely selectable. Degenerate quadratic relations such as [x1,x2][x1,x3] and [x1,x2][x2,x3] have 3 and 9 Kummer candidates at k=2 and k=3, respectively; x1^3[x1,x2][x2,x3] has no candidate at either level. This is a **PASS / LOCAL** scope boundary for the finite Kummer selector. It is not yet a calculation of the intrinsic higher obstruction δ̄4∘ι1. The next authorized test is that higher obstruction on r=[x1,x2][x1,x3] across its multiple Kummer characters.

Detailed record: research/ONE_RELATOR_KUMMER_SELECTOR_STRESS_TEST_2026-09-21.md.
