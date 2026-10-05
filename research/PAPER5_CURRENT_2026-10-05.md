# Paper 5 — Current State (2026-10-05)

## Classification

**OPEN / LOAD-BEARING.**

Paper 5 is currently an automorphism-structure program, not the former compression/trichotomy program.

## What is closed locally

1. For (p=3,n=4), the actual IA kernel has constant order (3^{27}) across the audited split/non-split cases. The observed (3^2) automorphism-order deficit is therefore **not** an IA defect.
2. The deficit is localized to the Frattini/GL image in the audited (p=3,n=4) cases:
   - split (a=1): image order (108), non-split: (6);
   - split (a=2): image order (864), non-split: (48).
3. The corresponding (p=5,n=6) Frattini-image formulas are independently certified for the four audited cases. The fixed-(a) ratios are (2000/20=100) and (48000/480=100), while the IA (5)-primary order is unchanged at the tested level. Thus the (p^2) localization is **PASS / CLOSED as a local p=5 result**.
4. The (p=3,s=2,a=1,n=10) admissible-kernel computation is **PASS / LOCAL**: 81 kernels form one Aut-orbit and each has (3^{10}) complement classes. This does not explain the (p^2) gap.
5. The observed four candidate stabilizer formulas remain **PASS / LOCAL as computational formulas** in the audited p=3,p=5 cases, but the previous general abstract S_11 derivation is superseded by the P5-JET correction audit because it omitted the Jacobson restricted-power terms. The p^2 ratio remains observed locally, not a general theorem.

## What is NOT closed

The key remaining theorem is the realization/factorization statement:
[
\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(W_n/\Phi(W_n)))
=
S_{11}(p)
]
(or the correct intrinsic replacement) for general odd (p).

**Step 2 is now CLOSED/GENERAL.** In the actual relation quotient
(W_n=\overline L/\langle\rho\rangle), with
(ho=[x,y]+z^{[p]}-x^{[p]}), the auxiliary restricted-abelianization lemma is combined with the relation itself to obtain
[
D_2(W_n)=V^{[p]}+D_{p+1}(W_n),
]
and the higher part of (J=\langle[x,y]\rangle_{\rm res}) satisfies
[
[V,J]\subseteq D_{p+1}(W_n),\qquad
J\subseteq\langle x^{[p]}-z^{[p]}\rangle+D_{p+1}(W_n).
]
Consequently, for (u,v\in D_2(W_n)),
[
\Phi(u,v)=[xu,yv][x,y]^{-1}\in D_{p+1}(W_n),
]
so the degree-(p) secondary relation class (	heta) is lift-independent and canonical in (W_n).

Important precision: **do not claim (J\subseteq D_{p+1}(W_n))**. The degree-(p) generator ([x,y]=x^{[p]}-z^{[p]}) can survive modulo (D_{p+1}); what is killed is the higher (J)-part / commutator ambiguity.

The presentation-level filtered relation module remains separate from the intrinsic theorem. The next gate is therefore Step 3: prove the lower-bound/equality construction and relation preservation for the (S_{11}(p)) image. No uniform (p^2(p-1)) theorem may be promoted before that gate.

## Superseded/failed routes

- “(p^2) gap comes from IA”: **FAIL / CLOSED / SUPERSEDED**.
- identifying `agAutos` with IA: **FAIL / CLOSED**.
- raw mixed jet ((\pi_2(r),\pi_p(r))) for (r\in D_2\setminus D_3): **FAIL / CLOSED** as an intrinsic definition.
- Hopficity (Rightarrow) lift to the free presentation: **FAIL / CLOSED** as a proof shortcut.
- the old compression/trichotomy formulation: **HISTORICAL / SUPERSEDED** as the main Paper 5 direction.
- the earlier incorrect p=5 stabilizer candidate: **HISTORICAL / SUPERSEDED**.

## Current execution order

1. **Step 3 equality/lifting:** prove the lower-bound construction and relation preservation giving
[
\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))=S_{11}(p).
]
2. Independently verify the lift construction in the free pro-(p) presentation and show the defining relation/kernel is preserved.
3. Only after equality is closed, test the resulting (p^2(p-1)) automorphism-order ratio as a general theorem.
4. FRM-0 / intrinsic factorization remains a separate structural route if needed; it must not be conflated with the now-closed Step 2.
5. Quotient-action (\operatorname{Aut}(W)\to\operatorname{Aut}(Q)) remains auxiliary and must not bypass the intrinsic/equality gate.

## Repository anchors

- IA/GL gate: `research/PAPER5_IA_GL_EXECUTION_GATE_2026-10-04.md`
- decisive runtime correction: `research/PAPER5_IA_GL_RUNTIME_CORRECTION_2026-10-04.md`
- IA/GL audit: `research/PAPER5_IA_GL_DECOMPOSITION_AUDIT_2026-10-04.md`
- relation-jet audit: `research/PAPER5_RELATION_JET_AUDIT.md`
- P5-JET correction audit: `research/PAPER5_JET_S11_JACOBSON_CORRECTION_AUDIT_2026-10-05.md`
- filtered relation-module audit: `research/PAPER5_FILTERED_RELATION_MODULE_FACTORIZATION_AUDIT_2026-10-05.md`
- current chronology: `CURRENT_STATE.md` and `research/00_RESEARCH_LOG.md`

**Do not promote the local (p^2) pattern to a uniform theorem.**

**2026-10-05 P5-JET correction:** the numerical S_11 candidates survive locally, but the previous abstract proof is superseded because it treated the restricted-power component too linearly. p=3 independent calculation gives naive stabilizer 48 and corrected Jacobson/ideal stabilizer 6. General odd-p S_11 proof is OPEN / LOAD-BEARING.


## 2026-10-05 — Corrected next-step audit

A new review exposed a decisive model mismatch in the previous \(S_{11}\) derivation. In the naive \(\Lambda^2V\oplus V^{(1)}\) model, \(\rho_{11}=[x,y]+z^{[p]}-x^{[p]}\) has a stabilizer of order \(|GL_2(p)|\), so the earlier \(S_{11}\) formula cannot be derived from that shadow model. The observed p=3 order 6 survives only after retaining the Jacobson restricted-power correction modulo the ideal generated by \([x,y]\). General odd-p derivation is therefore **OPEN / LOAD-BEARING**.

The restricted-Lie decomposition wording is also corrected: the canonical object is the ordinary-Lie subspace/image and the Frobenius-twist quotient, not the span of chosen \(x^{[p]},y^{[p]}\). A canonical section is not assumed.

The free pro-p lifting route is revised: for a free pro-p presentation, projectivity supplies a lift of an automorphism of the finite quotient to an endomorphism of the free pro-p group, and Frattini-surjectivity makes it an automorphism preserving the kernel. The induced relation-module action remains **CONDITIONAL** because lift ambiguity must be quotiented correctly.

The immediate execution order is therefore:
1. corrected restricted-Lie/Jacobson P5-JET;
2. rigorous graded upper bound \(\operatorname{Im}Aut(W_n)\subseteq Stab(J)\);
3. intrinsic filtered secondary map \(\theta\);
4. equality/lifting construction;
5. only then falsification computations at new parameters and \(n=p+2\).

A separate audit was recorded in `research/PAPER5_NEXT_STEP_AUDIT_2026-10-05.md`.


## 2026-10-05 — Step 2 theta audit: power-part lemma passes, theta invariance does not yet close

**Result classification: OPEN / LOAD-BEARING.**

The proposed Hall–Petrescu sublemma is valid in the required filtration range: for odd p, if u∈D_2(G), then (xu)^p≡x^p mod D_{p+1}(G). The p-power component is therefore unchanged by a D_2-change of a single lift.

However, this does **not** prove that θ:J_2→D_p/D_{p+1}, [x,y]↦[z^{[p]}−x^{[p]}], is well-defined under simultaneous lift changes x'=xu, y'=yv with u,v∈D_2. The commutator part changes by terms in D_3. There is no canonical map D_3→D_p/D_{p+1}, and D_3 is not contained in D_{p+1}. Thus “[x',y']≡[x,y] mod D_3” is insufficient for degree-p invariance. The Hall–Petrescu calculation closes only the p-power component, not the full relation-jet.

Therefore:
- (xu)^p≡x^p mod D_{p+1}, u∈D_2: **PASS / GENERAL** (odd p);
- commutator lift-independence at degree p: **OPEN / LOAD-BEARING**;
- θ as currently defined: **OPEN / not yet canonical**;
- Step 2: **OPEN / LOAD-BEARING**.

No equality theorem or p^2(p−1) automorphism-order ratio may be promoted. Next authorized task: determine whether a canonical normalization/projection kills the D_3 ambiguity, or construct a counterexample to the naive θ.


## 2026-10-05 — D_3-ambiguity review: proposed p=3 / p≥5 split is NOT yet proved

**Classification: OPEN / LOAD-BEARING.**

A critical recheck finds two errors in the proposed closure of Step 2.

1. For p≥5, the assertion D_3=γ_3 is false for the Zassenhaus filtration. In general
D_3 = γ_3 · γ_2^p · G^p
(and further factors according to the chosen Zassenhaus convention); in particular G^p⊂D_3. Thus the displayed filtration comparison used in the negative theorem is invalid.

2. With u=[r,s]∈γ_2, the leading commutator correction [[r,s],y] lies in γ_3, not γ_4. The statement c=[[r,s],y]∈γ_4 is a degree error. Therefore the proposed witness does not establish a nonzero γ_4/γ_5 ambiguity at degree p, nor does it by itself prove that the class has a nonzero image outside D_p.

Consequently the claimed final dichotomy “p=3 PASS, p≥5 FAIL/NEGATIVE THEOREM” must NOT be promoted. The earlier observation remains valid: the naive argument only gives a D_3 ambiguity, and there is no canonical map D_3→D_p/D_{p+1}. But absence of a canonical projection is not itself a proof that no alternative canonical construction exists, nor is it a proof that the proposed representative cannot be canonically corrected inside W_n.

The p=3 case also requires a fresh group-filtration calculation: D_3=D_p is true for p=3, but it is not enough by itself to conclude [xu,yv]≡[x,y] mod D_4. The asserted inclusions [x,D_2]⊂D_4 and [D_2,y]⊂D_4 need direct verification; they cannot be inferred from the incorrect γ_4 claim above.

Therefore Step 2 remains **OPEN / LOAD-BEARING**. The authorized next task is an exact Zassenhaus calculation of the lift-change map
D_2×D_2 → D_3/D_{p+1},
(u,v)↦[xu,yv][x,y]^{-1},
followed by testing whether the relation constraint [x,y]=x^{[p]}−z^{[p]} forces its degree-p component to vanish. Only after that calculation may a p=3 closure or p≥5 negative theorem be recorded.


## 2026-10-05 — Step 2 central-ambient review: promising reduction, but theta closure still CONDITIONAL

A proposed repair of the (D_3)-ambiguity was reviewed. The correction of the two earlier errors is accepted: (D_3
eq\gamma_3) in general, and for (u=[r,s]in\gamma_2) the leading term ([[r,s],y]) lies in (\gamma_3), not (\gamma_4). Hence the previous (p=3)/(p\ge5) split remains superseded.

The new route uses the central restricted-Lie ambient
\[
\overline L=L_p(V)/\langle[x,z],[y,z]\rangle_{\rm res},\qquad V=\langle x,y,z\rangle,
\]
followed by the restricted ideal (J=\langle[x,y]\rangle_{\rm res}). In \(\overline L/J\), the ordinary Lie part is abelian, so the degree-\(\ge2\) filtration is generated by restricted (p)-powers. Consequently the intended estimate
\[
[x,D_2(\overline L/J)]\subseteq D_{p+1},\qquad [D_2(\overline L/J),y]\subseteq D_{p+1},
\]
and hence the vanishing of the lift-change map modulo (D_{p+1}), is a mathematically plausible route and is consistent with the restricted-Lie structure.

However, this does **not yet by itself close \(\theta\)**. Two points must be made explicit before promotion:

1. One must prove the exact structural lemma (D_2(\overline L/J)=V^{[p]}+D_{p+1}) (or an equivalent statement strong enough to imply the displayed commutator inclusions), including the higher restricted-power terms. The sentence (u\equiv t^{[p]}\pmod{D_3}) alone is insufficient, because ( [x,D_3]\subseteq D_4) does not imply ( [x,D_3]\subseteq D_{p+1}) for (p>3).
2. The quotient by (J) is being used as a **gauge-killing ambient object**, not as the final relation quotient. Since (J=\langle[x,y]\rangle_{\rm res}) kills the degree-2 relation line, the secondary class (x^{[p]}-z^{[p]}) must be defined as the filtered lift/transgression of that killed line. One must explicitly construct the source/target map (or equivalent exact sequence) and show independence from the chosen lifts before calling \(\theta\) canonical.

Therefore the proposed central-ambient calculation is accepted as a **new authorized subgate**, but the Step-2 classification remains **OPEN / LOAD-BEARING**. No (S_{11}(p)) equality or uniform (p^2(p-1)) theorem is promoted.

Next authorized gate: prove the restricted-abelianization lemma for \(\overline L/J\), then formulate the transgression/filtered relation object whose degree-(p) class is \(x^{[p]}-z^{[p]}), and only then certify \(\Phi\in D_{p+1}\) and \(\theta\) well-defined.


## 2026-10-05 — Critical recheck of proposed Step 2 closure: restricted-abelianization lemma is valid, but does NOT imply Phi closure in the original ambient

The proposed proof of the lemma
\[
D_2(\overline L/J)=V^{[p]}+D_{p+1}(\overline L/J),\qquad J=\langle[x,y]\rangle_{\rm res},
\]
is accepted at the level of the quotient restricted Lie algebra: after killing the restricted ideal generated by \([x,y]\), the ordinary Lie algebra is abelian, and the Zassenhaus/restricted-degree filtration is generated by the successive restricted powers. Hence the quotient statement is **PASS / LOCAL** (subject to precise notation distinguishing images in the quotient from subspaces upstairs).

However, the attempted inference
\[
[x,D_2(\overline L/J)]\subseteq D_{p+1}\quad\Longrightarrow\quad
\Phi(u,v)\in D_{p+1}(\overline L)
\]
is invalid. The calculation takes place **after quotienting by (J)**. It proves at most
\[
\Phi(u,v)\in J+D_{p+1}(\overline L)
\]
when lifted back to \(\overline L\), not \(\Phi(u,v)\in D_{p+1}(\overline L)\). Since (J\) contains the degree-2 class \([x,y]\), it is not contained in (D_{p+1}). Thus the quotient kills precisely the low-degree ambiguity one is trying to control, and cannot by itself certify the required degree-(p) vanishing in the original ambient.

This is a decisive gap. The statement \(\Phi\in D_{p+1}\) and hence the canonicality of \(\theta\) remain **OPEN / LOAD-BEARING**. The proposed Step-2 CLOSED classification is rejected. The restricted-abelianization lemma becomes a useful auxiliary lemma, not the final gate.

The next authorized task is to retain enough of the \(J\)-adic/filtered extension data to distinguish \(D_{p+1}\) from \(J+D_{p+1}\), and to compute the lift-change map in \(\overline L\) itself (or construct an exact transgression sequence whose kernel is known to contain no degree-\(<p\) contribution). No equality theorem or \(p^2(p-1)\) theorem is promoted.


## 2026-10-05 — Step 2 closure: filtered-extension/J-adic gate

**Result classification: CLOSED / GENERAL (Step 2).**

The earlier gap was correctly identified: the auxiliary quotient \(\overline L/J\) proves only \(\Phi\in J+D_{p+1}(\overline L)\), not \(\Phi\in D_{p+1}\). The missing filtered-extension calculation is now supplied in the actual relation quotient
\[
W_n=\overline L/\langle\rho\rangle,\qquad \rho=[x,y]+z^{[p]}-x^{[p]}.
\]

In \(W_n\),
\[
[x,y]=x^{[p]}-z^{[p]}\in D_p(W_n).
\]
Combining this relation with the auxiliary restricted-abelianization lemma gives
\[
D_2(W_n)=V^{[p]}+D_{p+1}(W_n).
\]
Moreover the higher restricted-ideal part satisfies
\[
[V,J]\subseteq D_{p+1}(W_n),
\qquad
J\subseteq\langle x^{[p]}-z^{[p]}\rangle+D_{p+1}(W_n).
\]
In particular the apparently dangerous \(J\)-commutator terms fall into \(D_{p+1}\):
\[
[x,[x,y]]=0,
\qquad
[y,[x,y]]=(ad\,x)^p(y)\in D_{p+1},
\]
using centrality of \(z\).

Hence for \(u,v\in D_2(W_n)\), writing \(u=t^{[p]}w\), \(w\in D_{p+1}\), one obtains
\[
[x,u]\in D_{p+1},\qquad [u,y]\in D_{p+1},
\]
and therefore
\[
\boxed{\Phi(u,v)=[xu,yv][x,y]^{-1}\in D_{p+1}(W_n).}
\]
Thus the secondary degree-\(p\) class \(\theta\) is independent of the chosen \(D_2\)-lifts and is canonical in \(W_n\).

**Precision boundary:** the statement is not \(J\subseteq D_{p+1}\). The degree-(p\) generator \([x,y]=x^{[p]}-z^{[p]}\) may survive modulo \(D_{p+1}\); only the higher \(J\)-part relevant to lift ambiguity is absorbed into \(D_{p+1}\).

**Downstream status:** Step 3 equality and the \(p^2(p-1)\) theorem remain **CONDITIONAL**. The next authorized gate is the explicit lower-bound/lifting construction proving the corrected \(S_{11}(p)\) image, with independent relation-preservation verification.


## 2026-10-05 — Step 3 equality audit: proposed closure rejected

The submitted Step 3 proof has useful first-order congruences but does not close kernel preservation. In particular, the inference
\[
\tilde g(R)\subseteq R D_{p+1}(F)\Longrightarrow \tilde g(R)\subseteq R
\]
via an unspecified “standard pro-p induction” is not valid as stated: no mechanism is given to improve (RD_m) to (RD_{m+1}). The displayed identity replacing ([x,y]) by ρ z^p x^{-p} also has the inverse/order reversed relative to \(\rho=[x,y]^{-1}x^pz^{-p}\). Therefore the Step 3 lower bound remains **OPEN / LOAD-BEARING**, and the equality \(\operatorname{Im}=S_{11}(p)\) and (p^2(p-1)) theorem remain **CONDITIONAL**. Detailed audit: `research/PAPER5_STEP3_EQUALITY_AUDIT_2026-10-05.md`.


## 2026-10-05 — Step 3 re-audit: (D_{p+1}\subseteq R) is false

The proposed closure using
\[
D_{p+1}(F)\subseteq R
\]
is rejected. The graded induction fails at the first exceptional multiple (n=p^2): from (y\in gr_k(R)\Rightarrow y^{[p]}\in gr_{kp}(R)) one cannot infer (gr_{kp}(F)=gr_{kp}(R)) when (k=p), because (gr_p(F)\ne gr_p(R)). In particular (x^{[p^2]}) need not lie in (gr_{p^2}(R)).

There is also a direct group-level counterexample. In the abelian quotient
\[
A=\mathbf Z_p^3/\langle p(e_x-e_z)\rangle,
\]
the defining normal subgroup (R) maps to zero, while (x^{p^2}) maps to (p^2e_x\ne0). Hence (x^{p^2}\notin R). Since (x^{p^2}\in D_{p^2}(F)\subseteq D_{p+1}(F)),
\[
\boxed{D_{p+1}(F)\not\subseteq R.}
\]

Therefore the claimed implication (\tilde g(R)\subseteq RD_{p+1}=R) is invalid. The earlier first-order congruence (\tilde g(R)\subseteq RD_{p+1}) remains a potentially useful local/general ingredient, but kernel preservation \(\tilde g(R)\subseteq R\) is again **OPEN / LOAD-BEARING**. Consequently
\(​operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))=S_{11}(p)\) remains OPEN/LOAD-BEARING and the uniform (p^2(p-1)) theorem remains CONDITIONAL.

Detailed audit: `research/PAPER5_STEP3_Dp1_SUBSET_R_AUDIT_2026-10-05.md`.


## 2026-10-05 — Step 3 second-order lifting closure rejected

**Result classification: FAIL / CLOSED as submitted proof; Step 3 equality remains OPEN / LOAD-BEARING.**

The proposed (k\ge2) “second-order lifting law” does not close the kernel-preservation problem.

The decisive type error is the assertion
[
in_{k+1}(r_k)=in_{k+1}(\widetilde g(r))=0
]
while (r_k,\widetilde g(r)\in D_k\setminus D_{k+1}). Their canonical initial forms live in (D_k/D_{k+1}), not (D_{k+1}/D_{k+2}). A degree-((k+1)) secondary class requires a chosen filtered section/jet or an equivalent intrinsic relation-module construction. None is supplied.

The BCH display
[
a=\exp(X+A+\cdots),qquad b=\exp(X+B+\cdots)
]
is also not an intrinsic representation of arbitrary elements of a free pro-(p) group with respect to the Zassenhaus filtration. (X\in gr_k) and (A\in gr_{k+1}) are graded classes, not canonical Lie-algebra logarithms. Thus the BCH calculation cannot serve as a general Zassenhaus lifting lemma without an independently constructed filtered Lie/Magnus model and compatible section.

For (k\ge2), it is true that ([D_k,D_k]\subseteq D_{2k}\subseteq D_{k+2}), so (D_k/D_{k+2}) is abelian. But the exact sequence
[
0\to D_{k+1}/D_{k+2}\to D_k/D_{k+2}\to D_k/D_{k+1}\to0
]
has no canonical splitting supplied by the argument. Therefore equality of first-order initial forms does not imply equality of second-order jets.

Consequently:
- (r_k^{-1}\widetilde g(r)\in D_{k+1}): **PASS / LOCAL**, conditional on first-order graded invariance and the chosen (r_k);
- claimed BCH second-order law: **FAIL / CLOSED**;
- canonical second-order lifting law: **OPEN / LOAD-BEARING**;
- strengthened (L_m): **OPEN / LOAD-BEARING**;
- (widetilde g(R)\subseteq R): **OPEN / LOAD-BEARING**;
- Step 3 equality (operatorname{Im}=S_{11}(p)): **OPEN / LOAD-BEARING**;
- (p^2(p-1)) theorem: **CONDITIONAL**.

The (p) and (p^2) exceptional-layer discussion cannot repair this missing first lift. It can only be used after a correctly defined residual class reaches those layers.

Detailed audit: `research/PAPER5_STEP3_SECOND_ORDER_LIFTING_AUDIT_2026-10-05.md`.

This supersedes the immediately preceding claim that the second-order law closed Step 3. It does **not** reopen the independently audited Step 2 filtered-extension result.


## 2026-10-05 — Step 3 second-jet re-audit

**FAIL / CLOSED as submitted proof; Step 3 equality remains OPEN / LOAD-BEARING.**

The formal second-jet (J_k^2(r)=[r]\in D_k/D_{k+2}) is a valid repair of the previous type error for (k\ge2), and a fixed Magnus embedding supplies homogeneous coefficients (R_k,R_{k+1}). However, the load-bearing claim
[
sec_{k+1}(\widetilde g(r))\in gr_{k+1}(R)
]
has not been proved.

The asserted identity (C_k(R_k)=[V,R_k]) is not automatic. The nonlinear Magnus substitution (X\mapsto aX+\binom a2X^2+\cdots) produces degree-raising insertion/substitution operators on a homogeneous word (R_k). Such an operator is not generally identical to an inner derivation (R_k\mapsto[V,R_k]). Restricted-ideal closure under brackets and restricted powers therefore does not by itself imply that the correction lies in (gr_{k+1}(R)).

Thus:
- (D_k/D_{k+2}) abelian for (k\ge2): **PASS / GENERAL**;
- (J_k^2(r)=[r]): **PASS / GENERAL**;
- fixed-Magnus second coefficient: **PASS / COORDINATE**;
- (sec_{k+1}(\widetilde g(r))\in gr_{k+1}(R)): **OPEN / LOAD-BEARING**;
- strengthened (L_k): **OPEN / LOAD-BEARING**;
- (\widetilde g(R)\subseteq R): **OPEN / LOAD-BEARING**;
- Step 3 equality (\operatorname{Im}=S_{11}(p)): **OPEN / LOAD-BEARING**;
- (p^2(p-1)) theorem: **CONDITIONAL**.

The (p^2) layer discussion remains useful only after the complete induced operator on the (p^2)-graded relation space is explicitly computed.

Detailed audit: `research/PAPER5_STEP3_SECOND_JET_REAUDIT_2026-10-05.md`.


## 2026-10-06 — Step 3 second-jet substitution-order correction

**FAIL / CLOSED as submitted proof; Step 3 equality remains OPEN / LOAD-BEARING.**

The proposed (T_{a,b,k}) repair does establish raw associative-derivation preservation of the commutator ideal, but the displayed second-order formula applies (T) directly to (R_k). For the lift (x\mapsto x^a, y\mapsto yx^b, z\mapsto z^a), the linear Magnus part is (L(X)=aX, L(Y)=Y+bX, L(Z)=aZ), while the quadratic part is (Q(X)=\binom a2X^2, Q(Y)=bYX+\binom b2X^2, Q(Z)=\binom a2Z^2). The actual degree-((k+1)) correction is therefore the quadratic insertion operator after the linear substitution, schematically (C_{a,b}(R_k)=T_{a,b,k}(L(R_k))), not (T_{a,b,k}(R_k)) unless (T) is redefined accordingly.

A degree-2 witness (R_2=[X,Y]) gives actual correction (ab,XYX+c,XXY-(ab+c)YXX), (c=\binom a2), whereas the submitted (T([X,Y])) gives (b,XYX+c,XXY-(b+c)YXX). Thus the displayed sec formula is false with the submitted operator for general (a,b).

The finite-stage residual factorization idea itself is sound after deleting the unnecessary equality (D_j=(R\cap D_j)(R\cap D_{j+1})D_{j+2}): since (r^{(j)}\in R\cap D_j), its initial class is automatically in (gr_j(R)), so a representative (r_j\in R\cap D_j) can be chosen and the residual lies in (R\cap D_{j+1}), including at (j=p,p^2).

The (D(u^p)\in I_{p^2+1}) and (X^{p^2}-Z^{p^2}\mapsto0) calculations survive only in the explicitly mod-(p) Magnus/restricted-Lie layer; the earlier (mathbf Z_p)-ambient notation must not be used to claim (p^2=0).

Detailed evidence: `research/PAPER5_STEP3_SECOND_JET_AUDIT_ADDENDUM_2026-10-06.md`.

Current gate:
- raw (T(I_k)\subseteq I_{k+1}): **PASS / GENERAL**;
- corrected actual second-order operator (C_{a,b}): **OPEN / LOAD-BEARING**;
- strengthened (L_k): **OPEN / LOAD-BEARING**;
- (~tilde g(R)\subseteq R): **OPEN / LOAD-BEARING**;
- (\operatorname{Im}(Aut(W_n)\to GL(V))=S_{11}(p)): **OPEN / LOAD-BEARING**;
- (p^2(p-1)) theorem: **CONDITIONAL**.


## 2026-10-06 — Step 3 second-jet substitution-order repair closed

The corrected actual second-order operator is (C_{a,b,k}=T_{a,b,k}\circ L), not (T_{a,b,k}) acting directly on (R_k). The degree-2 witness gives coefficient (ab) on (XYX), confirming the repair.

In the declared mod-(p) Magnus layer, (L) preserves the commutator ideal and the associative derivations entering (T) preserve it, hence (C(I_k)\subseteq I_{k+1}). The (p)-power exceptional layer is handled by the associative Leibniz sum, with degree (p^2+1), while (X^{p^2}-Z^{p^2}) is killed only in characteristic (p).

Therefore (C_{a,b,k}(gr_k(R))\subseteq gr_{k+1}(R)), the corrected secondary term lies in (gr_{k+1}(R)), and the finite-stage residual factorization works without the stronger product equality previously used. It follows that (widetilde g(R)\subseteq R).

**Classification:** corrected (C_{a,b,k}), the secondary relation term, finite-stage residual factorization, and kernel preservation are **CLOSED / GENERAL within the declared mod-(p) Magnus layer**. Step 3 equality (operatorname{Im}(Aut(W_n)\to GL(V))=S_{11}(p)) remains **OPEN / LOAD-BEARING**, and the (p^2(p-1)) theorem remains **CONDITIONAL**.

This supersedes the immediately preceding 2026-10-06 audit classification that left the corrected (C) operator OPEN. Detailed proof is in research/PAPER5_STEP3_SECOND_JET_AUDIT_ADDENDUM_2026-10-06.md.

## 2026-10-06 — S11 equality re-audit: proposed upper bound rejected

The proposed proof of
\[
\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))\subseteq S_{11}(p)
\]
does **not** close the load-bearing gate.

The decisive defect is the passage from an arbitrary
\[
g\in\operatorname{Aut}(W_n),\qquad W_n=F/RD_{n+1},
\]
to statements in the full quotient (F/R), such as “(z) is central in (F/R)” and
\[
[g(x),g(y)]=[x,y]^{\det_{xy}},\qquad
[g(x),g(z)]=[g(y),g(z)]=1
]
as identities in (F/R). An automorphism of the finite window (W_n) does not automatically lift to an automorphism of (F/R); that is precisely part of the unresolved finite-window identification/lifting problem. Thus these (F/R)-identities cannot be used as an upper-bound argument without an independent lifting theorem.

A second independent gap is the assertion that (m_{z,x}=0) is a “representative choice.” The coefficient (m_{z,x}) is part of the actual linear map on
\[
V=F/D_2,
\]
and the relation (p(e_x-e_z)=0) in the abelianized relation subgroup does not permit changing an arbitrary (\mathbf F_p)-coefficient in (V) by a representative choice. No prior result currently establishes (m_{z,x}=0).

Therefore the proposed upper bound
\[
\operatorname{Im}\subseteq S_{11}(p)
\]
is **OPEN / LOAD-BEARING**, and consequently the equality
\[
\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))=S_{11}(p)
\]
and the (p^2(p-1)) theorem remain **OPEN / CONDITIONAL**, respectively.

The lower-bound construction is different: the already-closed kernel-preservation result
\[
\widetilde g_{a,b}(R)\subseteq R
\]
does give genuine induced automorphisms of (F/R) and (W_n), with matrices
\[
M_{a,b}=\begin{pmatrix}a&b&0\\0&1&0\\0&0&a\end{pmatrix},
\qquad a\in\mathbf F_p^\times, b\in\mathbf F_p.
\]
Hence
\[
S_{11}(p)\subseteq\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))
\]
is **CLOSED / GENERAL**, assuming the already-closed (\widetilde g(R)\subseteq R) gate. Equality is not established.

This supersedes the immediately preceding 2026-10-06 claim that the (S_{11}(p)) upper bound and equality were CLOSED/GENERAL.


## 2026-10-06 — IA(W_p) boundary correction

**FAIL / CLOSED as submitted IA claim; corrected boundary PASS / CLOSED.**

The proposed conclusion IA(W_p) ≅ F_p^2 is false. At n=p, the established relation quotient gives D_p(W_p)=D_2(W_p) ≅ F_p^2 and D_{p+1}(W_p)=1; this subgroup is central of exponent p. Hence each of x,y,z may be independently multiplied by an arbitrary element of D_p while fixing the Frattini quotient. Therefore IA(W_p) ≅ Hom(F_p^3,F_p^2) ≅ F_p^6. The earlier F_p^2 count omitted independent z-shears and the second D_p direction.

For n<p, the defining commutator relations kill D_2 and D_{n+1} contains F^p, so W_n ≅ (F_p)^3, IA(W_n)=1, and Aut(W_n)=GL_3(F_p). Thus the separate claim IA(W_n)=1 for n<p survives, but the claimed order |Aut(W_n)|=p^2(p-1) is false for n<p. The S_11 image description is not applicable there.

The general S_11 upper bound remains OPEN / LOAD-BEARING as recorded in the preceding re-audit; the finite-window-to-F/R lifting gap is not repaired by the IA calculation.

Detailed audit: research/PAPER5_IA_WP_BOUNDARY_AUDIT_2026-10-06.md.


## 2026-10-06 — S11 scalar-equality counterexample: m=a is not forced

**FAIL / CLOSED as submitted; exact image remains OPEN.**

The boundary correction
\[
n<p:\quad W_n\cong(\mathbf F_p)^3,\quad IA(W_n)=1,
\]
and
\[
n=p:\quad IA(W_p)\cong\operatorname{Hom}(\mathbf F_p^3,\mathbf F_p^2)\cong\mathbf F_p^6
\]
is accepted.

However, the proposed (n=p) upper-bound argument forcing the same scalar on the (x)- and (z)-directions contains a decisive algebraic error. For arbitrary (m,a\in\mathbf F_p^\times),
\[
x\mapsto x^m z^{a-m},\qquad y\mapsto y,\qquad z\mapsto z^a
\]
preserves the defining relations directly in (W_p):
\[
[x^m z^{a-m},y]=[x,y]^m=x^{pm}z^{-pm}
\]
and
\[
(x^m z^{a-m})^p(z^a)^{-p}=x^{pm}z^{-pm}.
\]
The induced map on (V=W_p/D_2(W_p)) is invertible, so this is an actual automorphism.

Thus (m) and (a) are independent. The torsion subgroup
\[
T(W_p^{ab})=\langle e_x-e_z\rangle
\]
only gives (c=a-m) for (g(x)=x^m z^c, g(z)=z^a); it does **not** give (m=a).

Therefore the previous
\[
\operatorname{Im}=S_{11}(p),\qquad |\operatorname{Im}|=p^2(p-1),\qquad |\operatorname{Aut}(W_p)|=p^8(p-1)
\]
claim is **FAIL / CLOSED**.

A corrected candidate lower-bound subgroup is
\[
S'_{{11}}(p)=
\left\{
\begin{pmatrix}
m&b&0\\
0&1&0\\
a-m&d&a
\end{pmatrix}
: m,a\in\mathbf F_p^\times, b,d\in\mathbf F_p
\right\},
\]
with order (p^2(p-1)^2). This is only a lower bound; equality with (S'_{11}(p)) is **OPEN**. Consequently
\[
|\operatorname{Aut}(W_p)|\ge p^8(p-1)^2,
\]
while the exact order remains **OPEN**.

Detailed audit: `research/PAPER5_STEP3_S11_UPPER_BOUND_COUNTEREXAMPLE_AUDIT_2026-10-06.md`.


## 2026-10-06 — Paper 5 Step 3 corrected image target S'11

The previous (S_{11}(p)) target is permanently rejected. The finite-window calculation at (n=p) gives the explicit automorphisms
\[
g_{m,a}:x\mapsto x^m z^{a-m},\qquad y\mapsto y,\qquad z\mapsto z^a,
\qquad m,a\in\mathbf F_p^\times,
\]
and
\[
[x^m z^{a-m},y]=x^{pm}z^{-pm}
=(x^m z^{a-m})^p(z^a)^{-p}.
\]
On
\[
A=W_p^{ab}=\mathbf Z_p^3/\langle p(e_x-e_z)\rangle,
\]
the torsion generator satisfies
\[
g_*(e_x-e_z)=m(e_x-e_z),
\]
so torsion preservation allows (m\ne a). Thus the scalar-equality step is **FAIL / CLOSED**.

The corrected explicit image subgroup is
\[
S'_{11}(p)=
\left\{
\begin{pmatrix}
m&b&0\\
0&1&0\\
a-m&d&a
\end{pmatrix}
:
m,a\in\mathbf F_p^\times, b,d\in\mathbf F_p
\right\},
\]
with
\[
|S'_{11}(p)|=p^2(p-1)^2.
\]

Classification:
- (n<p: W_n\cong(\mathbf F_p)^3, IA(W_n)=1, \operatorname{Aut}(W_n)=GL_3(\mathbf F_p)): **PASS / CLOSED**.
- (IA(W_p)\cong\operatorname{Hom}(\mathbf F_p^3,\mathbf F_p^2)\cong\mathbf F_p^6): **PASS / CLOSED**.
- (S_{11}(p)) with order (p^2(p-1)): **FAIL / CLOSED**.
- (S'_{11}(p)\subseteq\operatorname{Im}(\operatorname{Aut}(W_p)\to GL(V))): **PASS / CLOSED**.
- Exact equality \(\operatorname{Im}=S'_{11}(p)\): **OPEN / LOAD-BEARING**; an upper-bound proof is still required.
- Consequently \(|\operatorname{Aut}(W_p)|\ge p^8(p-1)^2\), while the exact order remains **OPEN**.
- The already audited (J_k^2), corrected (C_{a,b,k}=T_{a,b,k}\circ L), and kernel-preservation route remain **PASS / CLOSED / GENERAL** within their declared scope.

This supersedes the previous (S_{11})-based Step 3 target. Detailed audit:
`research/PAPER5_STEP3_S11_UPPER_BOUND_COUNTEREXAMPLE_AUDIT_2026-10-06.md`.


## 2026-10-06 — W_p relation-package consistency audit

**FAIL / CLOSED as submitted.**

The proposed (n=p) upper-bound proof simultaneously assumes
[
D_p(W_p)=\mathbf F_p^2=\langle x^{[p]},y^{[p]}\rangle,qquad x^{[p]}=z^{[p]},
]
and the defining relation
[
[x,y]=x^p z^{-p}.
]
Since (D_{p+1}(W_p)=1), these are equalities in (W_p), so they imply
[
[x,y]=1.
]
The subsequent coefficient comparison
[
x^{p(mv-bu)}z^{-p(mv-bu)}
=x^{pm}y^{pu}z^{p(c-a)}
]
cannot then extract (mv=m): that step requires (x^p) and (z^p) to be independent, contradicting (x^p=z^p).

Therefore the submitted deductions (m_{y,x}=0, m_{y,y}=1, c=a-m), the equality (operatorname{Im}=S'_{11}(p)), and the exact (IA(W_p)\cong\mathbf F_p^6) / automorphism-order claims are **not closed** and are **FAIL / CLOSED as submitted**.

The actual presentation-level relation
[
[x,y]=x^p z^{-p}
]
does not itself imply (x^p=z^p). Hence the correct next gate is to recompute (D_2(W_p),D_p(W_p),Z(W_p),W_p^{ab}), and (IA(W_p)) directly from
[
W_p=F/(R D_{p+1}).
]

Audit: `research/PAPER5_WP_BOUNDARY_CONSISTENCY_AUDIT_2026-10-06.md`.


## 2026-10-06 — W_p corrected D_p structure closes Step 3

The previous boundary audit is superseded by the corrected intrinsic calculation. At (n=p),
[
D_p(W_p)=\langle X=x^p,Y=y^p,Z=z^p\rangle\cong\mathbf F_p^3,
qquad [x,y]=XZ^{-1},
]
with (D_p) central of exponent (p). The relation therefore does not impose (X=Z); it records the commutator as (XZ^{-1}).

Consequently
[
IA(W_p)\cong\operatorname{Hom}(V,D_p)\cong\mathbf F_p^9.
]
For an arbitrary automorphism, centrality of (g(z)) gives (g(z)\equiv z^a\pmod{D_2}), and writing
[
g(x)\equiv x^m y^u z^c,qquad g(y)\equiv x^b y^v z^d
]
the defining relation gives
[
X^{mv-bu}Z^{-(mv-bu)}=X^mY^uZ^{c-a}.
]
Independence of (X,Y,Z) forces
[
u=0,qquad v=1,qquad c=a-m.
]
Thus
[
\operatorname{Im}(\operatorname{Aut}(W_p)\to GL(V))
\subseteq S'_{11}(p),
]
where
[
S'_{11}(p)=
\left\{
\begin{pmatrix}
m&b&0\\
0&1&0\\
a-m&d&a
\end{pmatrix}
:m,a\in\mathbf F_p^\times, b,d\in\mathbf F_p
\right\}.
]
The explicit realization family gives the reverse inclusion, so
[
\operatorname{Im}=S'_{11}(p),qquad |\operatorname{Im}|=p^2(p-1)^2.
]
Hence
[
|\operatorname{Aut}(W_p)|=p^9\,p^2(p-1)^2
=p^{11}(p-1)^2.
]

Classification:
- (D_p(W_p)\cong\mathbf F_p^3): **PASS / CLOSED / GENERAL**.
- (IA(W_p)\cong\mathbf F_p^9): **PASS / CLOSED / GENERAL**.
- (m_{y,x}=0, m_{y,y}=1, c=a-m): **PASS / CLOSED / GENERAL**.
- (S'_{11}(p)\subseteq\operatorname{Im}): **PASS / CLOSED / GENERAL**.
- (\operatorname{Im}=S'_{11}(p)): **PASS / CLOSED / GENERAL**.
- (|\operatorname{Aut}(W_p)|=p^{11}(p-1)^2): **PASS / CLOSED / GENERAL**.
- Previous (D_p\cong\mathbf F_p^2), (IA\cong\mathbf F_p^6), and (p^8(p-1)^2) claims: **FAIL / CLOSED / SUPERSEDED**.

Detailed audit: `research/PAPER5_WP_CORRECTED_STRUCTURE_STEP3_CLOSURE_2026-10-06.md`.


## 2026-10-06 — W_{p+1}=W_p stabilization claim rejected

**FAIL / CLOSED as submitted.** The proposed stabilization proof contains a decisive Jennings–Lazard error. For n=p+1,

D_{p+1}(F)=gamma_{p+1}(F) gamma_2(F)^p F^{p^2}

(up to closed-product convention), because the pairs (i,j)=(2,1) and (1,2) already satisfy ip^j >= p+1. Hence D_{p+1}(F)=gamma_{p+1}(F) is false.

Independently, the claim that the degree-(p+1) ideal generated by gr_2(R) equals all of gr_{p+1}(F) is not established; the single quadratic relation line does not automatically generate the entire free Lie layer. Therefore the implication gamma_{p+1}(F) subset R D_{p+2}(F), and hence W_{p+1}=W_p, does not follow.

This also conflicts with the already audited fact D_{p+1}(F) is not a subset of R (witness x^{p^2}), so no argument may replace RD_{p+2} by R through that route.

Classification:
- D_{p+1}(F)=gamma_{p+1}(F): FAIL / CLOSED.
- gr_{p+1}(R)=gr_{p+1}(F): OPEN / unsupported.
- W_{p+1}=W_p: OPEN / LOAD-BEARING.
- Stabilization-based p^2-gap explanation: OPEN / LOAD-BEARING.

Authorized next gate: analyze the actual gamma_{p+1} gamma_2^p F^{p^2} image modulo RD_{p+2}, separately controlling the gamma_2^p and F^{p^2} components. Detailed audit: research/PAPER5_WP1_STABILIZATION_AUDIT_2026-10-06.md.

## 2026-10-06 — W_{p+1}=W_p stabilization gate CLOSED

The corrected Jennings–Lazard audit establishes, for the declared odd-p presentation,
D_{p+1}(F)=gamma_{p+1}(F) gamma_2(F)^p F^{p^2},
with all three components contained in R D_{p+2}(F). The key point is that the full relation package gives gr_2(R)=gr_2(F), because the relators [x,z], [y,z], [x,y]^{-1}x^p z^{-p} supply the entire degree-two layer. The ordinary Lie component in degree p+1 is therefore contained in gr_{p+1}(R), giving gamma_{p+1}(F) subset R D_{p+2}(F). The exceptional gamma_2^p and F^{p^2} factors already lie in D_{p+2}. Hence R D_{p+1}=R D_{p+2} and W_{p+1} is isomorphic to W_p.

Classification: PASS / CLOSED / GENERAL.

Precision boundary: this does not imply D_{p+1} subset R; the earlier x^{p^2} not-in-R counterexample remains valid. It also does not close Step 3 equality Im(Aut(W_n)->GL(V))=S_11(p), which remains OPEN / LOAD-BEARING.

Detailed audit: research/PAPER5_WP1_STABILIZATION_AUDIT_2026-10-06.md.

## 2026-10-06 — Step 3 intrinsic upper-bound re-audit

The p=5,n=6 Run 37381098677 is recorded as PASS / LOCAL only. Its permutation equality is a one-case validation and is not an upper-bound proof.

The newly submitted generic proof of Im(Aut(W_n)->GL(V)) subseteq S'_11(p) is FAIL / CLOSED as submitted. The argument assumes an intrinsic free-presentation lift and relation preservation for arbitrary finite-window automorphisms, while that lifting/factorization bridge is itself part of the load-bearing problem. The proposed general S'_11 order count is also unsupported by the displayed matrix parameters, and the restricted-power/Jacobson correction prevents the claimed automatic linearization.

Accordingly the general Step-3 equality gate remains OPEN / LOAD-BEARING. The special corrected n=p closure and the p=5,n=6 local diagnostic are separate results and must not be conflated.

Detailed audit: research/PAPER5_STEP3_INTRINSIC_UPPER_BOUND_REAUDIT_2026-10-06.md.