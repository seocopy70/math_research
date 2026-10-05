# Paper 5 — Step 3 Second-Order Lifting Audit
Date: 2026-10-05

## Classification

**FAIL / CLOSED as submitted proof; Step 3 equality remains OPEN / LOAD-BEARING.**

The submitted argument attempts to close kernel preservation by a second-order lifting law for the Zassenhaus filtration. The first-order inclusion
\[
r_k^{-1}\tilde g(r)\in D_{k+1}
\]
is acceptable once the matching degree-k initial form has been established. The claimed upgrade to \(D_{k+2}\), however, is not a valid general lemma in the form stated.

## Decisive defects

### 1. The BCH/exponential notation is not justified

For a general free pro-p group and its Zassenhaus filtration, writing
\[
a=\exp(X+A+\cdots),\qquad b=\exp(X+B+\cdots)
\]
with \(X\in gr_k\) and \(A,B\in gr_{k+1}\) is not an intrinsic group-theoretic representation. The graded pieces are vector-space classes, not elements of a canonical Lie algebra admitting a global logarithm/exponential parametrization of the required form. In particular, the argument cannot invoke BCH on these symbols without first supplying a valid filtered Lie/Magnus model and a compatible section.

The Zassenhaus filtration is canonically related to a restricted graded Lie algebra and to the augmentation/Magnus filtration, but this does not provide the asserted canonical BCH expansion of arbitrary pro-p group elements. Standard references instead formulate the filtration through Jennings/Lazard/Magnus machinery. See the external audit sources cited in the research discussion.

### 2. \(in_{k+1}(a)\) is undefined for \(a\in D_k\setminus D_{k+1}\)

The statement
\[
in_{k+1}(r_k)=in_{k+1}(\tilde g(r))=0
\]
is the load-bearing error. Both \(r_k\) and \(\tilde g(r)\) are asserted to lie in \(D_k\setminus D_{k+1}\). Their canonical initial form is therefore in \(D_k/D_{k+1}\), not in \(D_{k+1}/D_{k+2}\).

A class in \(gr_{k+1}\) can only be assigned after removing a degree-k component by a chosen lift/section or after passing to a specified filtered extension. No such section is defined here. Thus the alleged equality of second-order terms is not a well-typed statement.

### 3. The actual second-order datum is exactly the missing factorization problem

For \(k\ge2\),
\[
[D_k,D_k]\subseteq D_{2k}\subseteq D_{k+2},
\]
so \(D_k/D_{k+2}\) is abelian. But the short exact sequence
\[
0\to D_{k+1}/D_{k+2}\to D_k/D_{k+2}\to D_k/D_{k+1}\to0
\]
does not canonically split. Equality of the degree-k initial forms therefore does **not** by itself produce a canonical difference in \(gr_{k+1}\). One must either:
- construct a canonical second-order section/jet, or
- prove directly that the relevant two elements have the same class in \(D_k/D_{k+2}\).

The present argument does neither.

### 4. The strengthened \(L_m\) statement therefore does not follow

The claimed
\[
\tilde g(R\cap D_m)\subseteq(R\cap D_m)D_{m+2}
\]
depends on the invalid second-order comparison at the first step. Hence the subsequent induction is not established.

Once an actual element \(d_m\in D_m\) is known to satisfy \(in_m(d_m)=0\), the conclusion \(d_m\in D_{m+1}\) is tautological from the definition of \(gr_m\). The nontrivial issue is obtaining the vanishing of \(in_m(d_m)\), not invoking a second-order law after it has already been assumed.

### 5. The exceptional \(p\) and \(p^2\) layers do not repair the missing first lift

The proposed later steps at \(m=p\) and \(m=p^2\) may be useful **after** a correctly defined residual element reaches those layers. They do not justify the initial passage from \(D_k\) to \(D_{k+2}\).

Moreover, an induction through all \(m\) requires a complete description of the exceptional graded layers encountered along the induction. It is not enough to discuss only \(p\) and \(p^2\) unless the relevant window is explicitly truncated and the absence of further exceptional layers is proved.

## Correct status

- \(r_k^{-1}\tilde g(r)\in D_{k+1}\): **PASS / LOCAL**, conditional on the first-order graded invariance and a correctly chosen \(r_k\).
- Claimed BCH second-order law as written: **FAIL / CLOSED**.
- Canonical second-order lifting law for Zassenhaus filtration: **OPEN / LOAD-BEARING**.
- Strengthened \(L_m\): **OPEN / LOAD-BEARING**.
- \(\tilde g(R)\subseteq R\): **OPEN / LOAD-BEARING**.
- Step 3 equality \(\operatorname{Im}=S_{11}(p)\): **OPEN / LOAD-BEARING**.
- \(p^2(p-1)\) automorphism-order theorem: **CONDITIONAL**.

## Important positive refinement

The useful target is now sharper. Rather than trying to manufacture \(in_{m+1}(r_m)\) for an element still in \(D_m\setminus D_{m+1}\), define an intrinsic filtered relation object controlling the class of
\[
r^{-1}\tilde g(r)\in D_{m+1}
\]
in \(D_{m+1}/D_{m+2}\), and prove that the automorphism action kills this class. That is a genuine second-order relation-jet/factorization statement. It must be proved independently; it cannot be obtained merely from equality of first-order initial forms.

## Literature sanity check

The Zassenhaus filtration is characterized by the restricted commutator/power laws and by the Jennings/Magnus augmentation filtration. Standard references give recursive descriptions such as
\[
G(n)=G(\lceil n/p\rceil)^p\prod_{i+j=n}[G(i),G(j)]
\]
and Lazard's product formula. These support the filtration-degree estimates used above, but they do not supply the asserted canonical exponential/BCH splitting of \(D_k/D_{k+2}\).

## Decision

The proposed Step 3 closure is **rejected**. The previous repository status claiming Step 3 equality CLOSED/GENERAL is superseded. Step 2 may remain CLOSED/GENERAL only to the extent independently established in its own filtered-extension audit; this audit does not reopen Step 2.
