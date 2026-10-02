# PAPER 4 — Relative Class-2 Factor-Through Audit
## 2026-10-02

### Purpose

Test whether the first strict-compression candidate
\[
C_n^{(2)}(E_n):
1\to K_n/\gamma_3(K_n)\to W_n/\gamma_3(K_n)\to D/D_n(D)\to1
\]
is already determined by the previously closed abelian/H1-extension/ordinary-graded layers.

This is a factor-through pretest only. It does not yet claim T1 separation.

### 1. Intrinsic decomposition

Put
\[
A_n=K_n/\gamma_2(K_n),\qquad
B_n=\gamma_2(K_n)/\gamma_3(K_n).
\]
Then the class-2 kernel is determined by the central extension
\[
1\to B_n\to K_n/\gamma_3(K_n)\to A_n\to1
\]
together with the commutator pairing
\[
\beta_n:A_n\wedge A_n\to B_n,
\qquad
\beta_n(\bar u,\bar v)=[u,v]\bmod\gamma_3(K_n),
\]
and the induced action of \(D/D_n(D)\).

The key point is that the previously closed H1-extension layer retains only the abelian kernel module/coinvariant extension data. It has no slot in which the alternating commutator pairing \(\beta_n\) can be reconstructed in general.

### 2. Structural non-factorization test

A universal factorization
\[
C_n^{(2)}=F(A_n,(A_n)_D,H_1\text{-extension},\operatorname{gr}_{Zass})
\]
would force \(\beta_n\) to be a functorial invariant of those closed layers.

That implication is false at the level of the ambient class-2 extension category: class-2 central extensions with the same abelianization/module data can have different commutator pairings. Thus the class-2 quotient contains a genuinely new type of information, namely an integral commutator-extension datum, which is not formally a function of the abelian/E2 package.

This is only a **structural PASS / LOCAL**. The admissible Paper-4 stress family is narrower, so an explicit pair inside the q>0 stress family is still required before declaring a stress-family non-factorization theorem.

### 3. Ordinary associated-graded comparison

The mod-p Zassenhaus associated graded is already closed as an s-detector in the q>0 stress model. Its degree-2 bracket records only the initial Demushkin commutator form.

The class-2 quotient is not identical to this graded object: it retains integral lower-central information and the p-power/central-extension structure before reduction to the associated graded.

Therefore the previous graded blindness does **not** imply
\[
C_n^{(2)}\text{ factors through }\operatorname{gr}_{Zass}.
\]
No closure is justified from the graded result alone.

### 4. What remains unresolved

The load-bearing question is now sharply reduced to the stress family
\[
G_{s,a}=\langle z,x_1,\ldots,x_d\mid z^{p^s}=r_D\rangle,
\qquad q_D=p^a>0,
\qquad s>a.
\]

For fixed external threshold \(m>a\), the required T1 test is whether a single depth \(n=n(m)\), independent of s, makes
\[
C_n^{(2)}(G_{s,a})\not\cong C_n^{(2)}(G_{t,a})
\]
whenever
\[
s<m\le t.
\]

The first quantity to compute is not a raw Magnus coefficient. It is the intrinsic central extension invariant:
- the D-module \(A_n\);
- the central commutator target \(B_n\);
- the pairing \(\beta_n\);
- and, crucially, the induced p-power map on the class-2 kernel modulo \(\gamma_3\).

A successful T1 proof must show that the threshold information survives all quotient/kernel automorphisms and does not reduce to the already closed abelian/E2/graded data.

### 5. Current classification

- structural distinction of class-2 data from abelian/H1 layers: **PASS / LOCAL**;
- factorization through ordinary mod-p associated graded: **OPEN**, not implied by prior graded blindness;
- stress-family factor-through test: **OPEN / LOAD-BEARING**;
- T1 separation for \(C_n^{(2)}\): **OPEN / LOAD-BEARING**;
- strictness A6: **OPEN**;
- non-reencoding A7: **OPEN**.

### 6. Stop/next action

No broad carrier search.

The next authorized computation is a targeted class-2 stress calculation for \(G_{s,a}\), at the candidate threshold scale, extracting only \((A_n,B_n,\beta_n,\text{power map},D\text{-action})\).

If these data are constant for s>a up to the threshold, classify \(C_n^{(2)}\) **FAIL / CLOSED** for T1. If they separate s<m from s\ge m, independently verify gauge invariance and strictness before any promotion.

