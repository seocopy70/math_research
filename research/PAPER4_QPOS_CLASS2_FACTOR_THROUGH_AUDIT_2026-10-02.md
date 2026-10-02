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



### 7. Targeted class-2 reduction: the surviving nonabelian datum

The stress relation
[
z^{p^s}=r_D
]
has a class-2 consequence that is invisible after passing to coinvariants but is not automatically invisible in the relative class-2 extension.

Let
[
A_n=K_n/gamma_2(K_n),qquad B_n=gamma_2(K_n)/gamma_3(K_n).
]
The quotient (C_n^{(2)}) carries the (D/D_n(D))-action on (A_n) and (B_n). For (xin D), write (T_x) for the induced action on (A_n), and let (c_x(ar z)) denote the class of the kernel commutator/defect determined by ([z,x]) at the relevant class-2 level.

The identity
[
[z^{r},x]
=
[z,x]^{,1+x+cdots+x^{r-1}}
]
becomes, after passing to the abelianized kernel layer, a norm-operator identity
[
[z^{p^s},x]
=
N_{p^s}(T_x),c_x(ar z),
qquad
N_{p^s}(T_x)=1+T_x+cdots+T_x^{p^s-1}.
]
On the other hand (z^{p^s}=r_D), so the same class-2 datum is constrained by
[
N_{p^s}(T_x)c_x(ar z)
=
[r_D,x].
]

This gives the precise boundary between the closed E2 layer and the surviving candidate.

After taking (D)-coinvariants, (T_x) becomes (1), so
[
N_{p^s}(T_x)longmapsto p^s.
]
The previously established Ext/H1 calculation then sees only
[
p^smod p^a,
]
which is zero for every (sge a). Thus the untwisted E2/H1 saturation is recovered exactly.

But (C_n^{(2)}) retains the full (D)-action, so the operator (N_{p^s}(T_x)) need not collapse to (p^s). Consequently the old H1 saturation argument does **not** prove factorization of (C_n^{(2)}) through the closed layers.

This is the first concrete nonabelian obstruction that survives the earlier closures.

### 8. Exact T1 reduction

For a fixed external threshold (m>a), take the candidate window at a depth (n=n(m)) large enough that the Zassenhaus level (p^m) is represented. The T1 problem for (C_n^{(2)}) reduces to the following finite intrinsic question:

> Does the isomorphism class of the (D/D_n(D))-module data
> [
> (A_n,B_n,eta_n,ho_n,	ext{class-2 power map})
> ]
> distinguish the norm operators (N_{p^s}(ho_n(x))) for (a<s<m) from the regime (sge m), after quotienting all admissible extension automorphisms?

Equivalently, one must determine whether the deep-tail parameter survives in the **non-coinvariant norm action** while disappearing from the coinvariant quotient.

This is a substantially narrower computation than a raw Magnus/Fox search. It has exactly the required input and gauge constraints and tests the first genuinely nonabelian layer.

### 9. Independent literature/method check

Hamza's treatment confirms that lower-central and Zassenhaus filtrations naturally carry group/module actions and that finitely presented pro-(p) groups are a natural setting for such equivariant filtered objects. It supports the legitimacy of the filtration/action framework, but does not prove the present T1 separation statement. citeturn1search0turn1search17

Relation-module literature likewise treats the conjugation action on the relation module as intrinsic structure of a pro-(p) presentation, while warning that presentation-level coefficients must not be mistaken for intrinsic invariants. This supports using the action/extension class rather than a selected scalar coefficient. citeturn3search2turn3search3

### 10. Classification after the reduction

- A1 intrinsicity: **PASS / LOCAL**;
- A2 functoriality: **PASS / LOCAL**;
- A3 gauge invariance: **PASS / LOCAL** at the quotient-object level;
- A4 q-blindness: **PASS**;
- A5 orientation-blind input: **PASS**;
- class-2 non-coinvariant norm defect: **PASS / LOCAL** as the first surviving structural datum;
- factor-through H1/E2/ordinary graded layers: **NOT ESTABLISHED; prior closure does not apply**;
- T1 threshold separation: **OPEN / LOAD-BEARING**;
- A6 strictness: **OPEN**;
- A7 non-reencoding: **OPEN**.

No positive T1 theorem is claimed yet. The candidate remains alive, but the next computation is now uniquely specified: compute the norm-action orbit on (A_n) (with the induced (B_n,eta_n), and power map only as needed) for the smallest (a<s<m) and the first (sge m), then test whether the resulting compressed objects are non-isomorphic.
