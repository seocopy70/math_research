## 2026-10-02 — PAPER 4 TOP-DOWN TARGET SHARPENED: NORMALIZATION FUNCTIONAL GATE

The top-down reset has now been carried through to a sharper mathematical target. For a specially oriented RAAG with (q=p^f), the first nontrivial orientation layer is a linear functional
[
omega_q:L_1	omathbf F_p
]
with kernel containing the intrinsic origin/torsion sector (O_q), and normalized by (omega_q(ar w)=1) on sinkhole generators. Thus the remaining finite-window problem is not full directed-incidence reconstruction but construction (or impossibility) of this normalized functional from (W_q\leftarrow W_{q+1}).

The information decomposition is:
[
W_{q+1}Longrightarrow(q,O_q,omega_q)Longrightarrowchimod p^k.
]
Here q is locally visible as the first nonzero extension-defect degree; (O_q) is recovered locally by RP-3; and abelianization alone cannot normalize (omega_q). The nonabelian finite extension contains additional normalization data, as verified in the 2-generator semidirect model.

A new local observation was verified in the complete 3-vertex one-sink model: the rank of (B_q(u,-)) is 1 on nonzero origin directions and 2 when the sink component of (u) is nonzero. This shows the failed (J_q(u)\neq0) predicate was too coarse, but rank-stratification is not universal: in the 2-generator model every nonzero direction has rank 1. Therefore no rank-only carrier is promoted.

New load-bearing gate:
[
oxed{T1:quad W_q\leftarrow W_{q+1}\Longrightarrowomega_q ?}
]
Required: intrinsicity, lift/gauge independence, q-blindness, non-tautological definition, direct orientation bridge, and independent verification on the audited local models. If two admissible specially oriented RAAGs have isomorphic adjacent windows but different normalized (omega_q), T1 is FAIL/CLOSED at this window.

Classification:
- top-down reset: **PASS / ACTIVE**;
- q recovery: **PASS / LOCAL**;
- origin sector: **PASS / LOCAL**;
- abelianization-only normalization: **FAIL / CLOSED**;
- normalized finite-window orientation functional (omega_q): **OPEN / LOAD-BEARING**;
- full incidence reconstruction as prerequisite: **NOT ESTABLISHED / NOT AUTHORIZED**.

Detailed audit: research/PAPER4_TOP_DOWN_ORIENTATION_TARGET_AUDIT_2026-10-02.md.
## 2026-10-02 — PAPER 4 TOP-DOWN RESET / CARRIER-HUNTING BOUNDARY

The latest complete-3-vertex counterexample closes the current arbitrary-linear-direction purity formulation for (J_q(u)): a non-origin linear direction can be q-active. This is not evidence that Paper 4 has returned to an unconstrained carrier search; it is evidence that the present bottom-up incidence target is too strong.

The earlier top-down transition remains controlling. T−1 (intrinsic canonical orientation target) and T0 (finite-window identifiability at the standard Demuškin scope) remain closed. Paper 4 must therefore return to target-first design: first specify the exact orientation-relevant information that a finite window must determine, then derive the weakest non-tautological intrinsic observable capable of carrying that information. Full directed-incidence reconstruction is not a prerequisite unless the target-first analysis proves it necessary.

Accordingly, the recent sequence (J_q) → joint ((P_q,B_q)) → restricted origin extension is classified as local carrier exploration, not as a new mandate to continue generating carriers indefinitely. The restricted origin extension remains OPEN/LOAD-BEARING only as a possible realization after the target-first pre-check; it is not authorized to expand into another open-ended carrier hunt.

Immediate methodological decision:
1. freeze the failed (J_q) purity theorem;
2. do not pursue arbitrary-incidence reconstruction as the default target;
3. reconstruct the top-down target decomposition: orientation target → necessary finite observable → non-reencoding/coarseness requirement → candidate realization;
4. only then test whether the existing RP-3 origin carrier plus a relative extension datum is actually required.

Classification: **TOP-DOWN RESET = ACTIVE; bottom-up carrier search = NOT AUTHORIZED until target-first necessity is established.**

## 2026-10-02 — PAPER 4 J_q ARBITRARY-LINEAR-DIRECTION PURITY FAILS

The exact-depth centralizer jump
\[
J_q(u)=C_q(u)/C_{q+1}(u)
\]
does remove ordinary-edge contamination, but it is **not** a pure one-direction incidence detector for arbitrary linear \(u\).

In the complete three-vertex model
\[
G=\langle s,a,b\mid[a,b]=1,\;sas^{-1}=a^{1+q},\;sbs^{-1}=b^{1+q}\rangle,
\]
the q-layer defect is
\[
B_q(u,x)
=(\alpha\gamma'-\gamma\alpha')\overline{a^q}
 +(\beta\gamma'-\gamma\beta')\overline{b^q}
\]
for \(u=\alpha\bar a+\beta\bar b+\gamma\bar s\). The form has zero radical. Since all degree-one commutators lie in \(D_q\) in this complete graph, \(C_q(u)=L_1\) and \(C_{q+1}(u)=\ker B_q(u,-)\). Therefore
\[
J_q(u)\neq0
\]
for every nonzero projective direction \([u]\in\mathbf P(L_1)\).

Explicitly,
\[
u=\bar s+\bar a\notin O=\operatorname{span}(\bar a,\bar b),
\qquad
B_q(u,\bar a)=\pm\overline{a^q}\neq0.
\]
Thus a non-origin linear direction is q-active. The sinkhole direction \(\bar s\) is q-active as well.

Current classification:
- exact-depth \(J_m\): **PASS / LOCAL**;
- ordinary/special depth separation: **PASS / LOCAL**;
- RP-5 pairwise separation: **PASS / LOCAL**;
- arbitrary-linear-direction purity \(J_q(u)\neq0\iff u\) is a genuine origin direction: **FAIL / CLOSED**;
- the prior “linear-combination purity” formulation: **FAIL / CLOSED — false as stated**;
- combined target-labelled/restricted-power carrier: **OPEN / LOAD-BEARING**;
- full directed-incidence reconstruction: **OPEN**;
- full orientation reconstruction: **OPEN**.

This closes the current purity formulation, not the Paper-4 program. The next authorized branch is a fresh intrinsicity audit of a joint carrier such as \((P_q,B_q)\), or an equivalent extension-class object, with no large scan before Object/Input/Functoriality/Gauge/Orientation-bridge/q-blindness/Separation/Novelty/Stop are checked.

Detailed audit: research/PAPER4_ARBITRARY_LINEAR_DIRECTION_JQ_AUDIT_2026-10-02.md.

## 2026-10-02 — CONVENTION CORRECTION AUDIT COMPLETED

Independent source verification confirms the controlling convention: special edge (v,w) has ordinary origin v, special terminus w, and wvw^{-1}=v^{1+q}. Thus the q-torsion direction is v, the origin, not the special/sinkhole terminus. citeturn1search0turn1search1

Corrected RP-3 state:
[
G^{ab}cong(mathbf Z/q)^Ooplusmathbf Z_p^{Vsetminus O},
qquad
mathcal L(W_q,W_{q+1})^perp=operatorname{span}(O).
]
The prior span(S) statement is superseded. The carrier remains q-blind/intrinsic locally, but it recovers the origin/torsion sector; a separate origin-to-sinkhole bridge is required for any sinkhole/orientation conclusion.

RP-5 remains PASS / LOCAL for same-abelianization separation, with its existing O/S notation already convention-correct. Grassmannian extraction remains FAIL / CLOSED.

## 2026-10-02 — RP-5 GRAPH-SENSITIVE SEPARATION

RP-5 now has a decisive local separation result. Two four-vertex specially oriented graphs with no ordinary edges, A=(a,s),(b,s) and B=(a,s),(b,t), have isomorphic abelianizations but different first-q filtered extension defects. The q-power preimage of the defect image recovers the origin plane; in this control family the degree-2 centralizer recovers the special plane; the cross q-defect has rank 1 versus rank 2. Thus criterion B is PASS / LOCAL. Full incidence reconstruction remains OPEN / LOAD-BEARING.

Critical convention correction: the literature defines special edge (v,w) with ordinary origin v and special terminus w, relation w v w^{-1}=v^(1+q). Hence v, not w, is q-torsion in abelianization. Earlier RP-3 identification of the torsion/annihilator sector with special/sinkhole vertices is therefore reversed under the literature convention and requires a correction audit before reuse.

Detailed audit: research/RP5_NONABELIAN_EXTENSION_CLASS_AUDIT_2026-10-02.md

## 2026-10-02 — RP-4 CRITICAL RE-AUDIT: EXTENSION DEFECT BRANCH REOPENED/CORRECTED

The proposed RP-4 closure based on “\\(\\kappa_n\\) is an abelianization factor” is rejected. Two corrections are controlling.

1. The Part-I equivalence “graph-sensitive iff not factoring through abelianization” is logically too strong. Criterion B (existence of two equal-abelianization graphs separated by the carrier) is the actual separation test; non-factorization is necessary but not sufficient.

2. The extension commutator defect is genuine filtered extension data. In the rank-2 special-edge model, \\(G'\\subseteq D_q\\), so \\(\\operatorname{im}\\kappa_n=0\\) for \\(n<q\\) and \\(\\operatorname{im}\\kappa_q=\\mathbf F_p\\overline{v^q}\\). The draft's claimed nonzero element of \\(D_2/D_3\\) is false for odd \\(p\\): \\(v^q\\in D_q\\subseteq D_3\\).

Therefore the prior RP-4 FAIL/CLOSED label is HISTORICAL/SUPERSEDED. The Grassmannian special-plane carrier remains FAIL/CLOSED, but the raw extension-defect object remains locally valid and is not abelianization-only.

Current classification:
- central extension / commutator defect: PASS / LOCAL;
- rank-2 first defect at q: PASS / LOCAL;
- common-sink local extension defect: PASS / LOCAL;
- Grassmannian special-plane extraction: FAIL / CLOSED;
- “\\(\\kappa_n\\) factors through abelianization”: FAIL / CLOSED — FALSE CLAIM;
- full extension-class carrier: OPEN / LOAD-BEARING;
- general graph-incidence separation: OPEN / LOAD-BEARING.

Next authorized gate: RP-5 full extension class \\([E_n]\\in H^2(W_n,A_n)\\), but only after pre-checking the actual extension object \\(E_n=W_{n+1}\\to W_n\\), functoriality/gauge, q-blind first-defect detection, and same-abelianization separation. Do not begin with a bare \\(H^2(W_1,A_1)\\) computation as though it already captured the q-layer.

Detailed correction: research/RP4_EXTENSION_DEFECT_REAUDIT_2026-10-02.md

## 2026-10-02 — RP-3 Q-BLIND ADJACENT-WINDOW CARRIER FOUND

The RP-3 Bockstein branch has advanced beyond the previous OPEN q-blindness gap.

For an adjacent finite pair (X=W_nleftarrow Y=W_{n+1}), define intrinsically
[
e(Z)=log_pexp(Z^{ab})
]
and
[
mathcal L(X,Y)=
egin{cases}
operatorname{im}igl(operatorname{Hom}(Y,mathbf Z/p^{e(Y)})	ooperatorname{Hom}(Y,mathbf F_p)igr),&e(Y)>e(X),\
0,&e(Y)=e(X).
end{cases}
]
This definition is q-blind: it uses only the adjacent finite groups, their abelianizations, exponent, Hom, reduction mod p, and the annihilator pairing.

At the specially oriented RAAG jump (n=q=p^f),
[
W_q^{ab}cong(mathbf Z/q)^V,qquad
W_{q+1}^{ab}cong(mathbf Z/pq)^{Vsetminus S}oplus(mathbf Z/q)^S.
]
Thus, if (Vsetminus S
eqarnothing), (mathcal L(W_q,W_{q+1})) is exactly the free/non-sinkhole character subspace, hence (kereta_f). If (Vsetminus S=arnothing), the exponent does not jump and the definition gives (mathcal L=0=kereta_f).

Therefore the intrinsic carrier
[
F(W_q,W_{q+1})=mathcal L(W_q,W_{q+1})^perpsubseteq L_1
]
recovers exactly the sinkhole sector:
[
F(W_q,W_{q+1})=(kereta_f)^perp=operatorname{span}{ar s:sin S}.
]

This also fixes the previous dual-space type error: the annihilator is a subspace of (L_1), not (L_1^*).

Classification:
- q-blind adjacent-window carrier: **PASS / LOCAL**;
- intrinsic/functorial construction: **PASS / LOCAL**;
- kernel identification: **PASS / LOCAL** under the specially oriented RAAG abelianization structure;
- full (eta_f) class reconstruction: **OPEN / NOT LOAD-BEARING**;
- RP-3 overall: **PASS / LOCAL** for the declared target (F(W_{m finite})=(kereta_f)^perp);
- non-special oriented graphs: separate OPEN branch;
- non-reencoding/minimality: OPEN and not yet claimed.

Detailed audit: research/RP3_FINITE_WINDOW_BOCKSTEIN_AUDIT_2026-10-02.md

Next authorized attack: independently verify the carrier in the smallest non-complete graph, multiple-sink graph, and the degenerate all-sinkhole case; then perform the admissible-category/non-reencoding audit. Do not switch to Massey calculations unless a verification failure makes them load-bearing.

## 2026-10-02 — RP-3 BOCKSTEIN FINITE-WINDOW CLAIM CORRECTED: LIFTABILITY SURVIVES, FULL β-RECONSTRUCTION OPEN

The proposed RP-3 finite-window Bockstein argument has been critically audited. The local algebraic conclusion is sound, but the draft overclaimed the finite-window factorization.

For a specially oriented pro-p RAAG with sinkhole set S and q=p^f,
[
G^{ab}cong mathbf Z_p^{Vsetminus S}oplus(mathbf Z/p^f)^S,
]
and the higher Bockstein satisfies the liftability criterion
[
chiinkereta_f
iff
chi:H^1(G,mathbf F_p)	omathbf F_p
	ext{ lifts to }mathbf Z/p^{f+1}.
]
Thus the kernel is exactly the annihilator of the sinkhole torsion sector. This is PASS/LOCAL.

A type correction is mandatory:
[
H^1=L_1^*,quad(kereta_f)^perpsubseteq L_1,
]
so the sinkhole carrier is (operatorname{span}{ar s:sin S}), not a span of dual basis vectors unless an auxiliary identification (L_1cong L_1^*) is chosen.

The key finite-window statement must be weakened. (W_{q+1}) does not automatically determine the full cohomology class (eta_f(chi)in H^2(G,mathbf F_p)), because no identification of global (H^2(G)) with (H^2(W_{q+1})) has been proved. What is locally established is that every lift to (mathbf Z/p^{f+1}) factors through (W_{q+1}), yielding a finite-window liftability predicate.

The remaining load-bearing issue is **q-blind uniformization**: the liftability test currently names the coefficient group (mathbf Z/p^{f+1}), hence q indirectly. A valid RP-3 carrier must be defined uniformly from an arbitrary adjacent pair ((W_n,W_{n+1})), without inserting q, and then shown to specialize at (n=p^f) to ((kereta_f)^perp).

Classification:
- abelianization/free-vs-sinkhole decomposition: **PASS / LOCAL**;
- higher-Bockstein kernel via liftability: **PASS / LOCAL**;
- three local graph models: **PASS / LOCAL**;
- dual-space typing of (C_f): **FAIL / CLOSED — TYPE ERROR**;
- full (eta_f) reconstruction from ((W_q,W_{q+1})): **OPEN / NOT PROVED**;
- finite-window liftability predicate: **PASS / LOCAL**;
- q-blind uniform carrier: **OPEN / LOAD-BEARING**;
- RP-3 overall: **OPEN / LOAD-BEARING**.

Detailed audit: research/RP3_FINITE_WINDOW_BOCKSTEIN_AUDIT_2026-10-02.md

Immediate next authorized attack: construct and test the uniform adjacent-window liftability object before any Massey-interference or non-special-graph expansion. If the uniform construction fails, seek a same-window counterexample and close RP-3. Do not reopen the closed Grassmannian carrier branch.

## 2026-10-02 — SPECIAL-PLANE FAILURE, BUT RESTRICTED-POWER REFINEMENT SURVIVES LOCALLY

The complete 3-vertex special graph is a decisive counterexample to the **Grassmannian first-survival carrier**, not to all intrinsic finite-window carriers. The intermediate claim (U_1\cap U_2=0) was corrected to (U_1\cap U_2=\mathbf F_p(\bar s+\bar a)); the full intersection over all q-special planes is still zero after including (U_3=\operatorname{span}(\bar s,\bar b)).

More importantly,
[
\operatorname{im}B_q=\mathbf F_p\overline{s^q},
qquad
P_q^{-1}(\operatorname{im}B_q)=\mathbf F_p\bar s.
]
So the Grassmannian loses the sinkhole line, while the extension-defect image together with restricted q-power structure recovers it in this model.

Classification:
- first-survival Grassmannian carrier: **FAIL / CLOSED**;
- accidental-plane exclusion: **FAIL / CLOSED**;
- corrected full-intersection computation: **PASS / LOCAL**;
- restricted-power refinement in complete 3-vertex model: **PASS / LOCAL**;
- general restricted-power/extension-defect carrier: **OPEN / LOAD-BEARING**;
- categorical no-go for all intrinsic finite-window carriers: **OPEN / NOT ESTABLISHED**.

Next gate: test (P_q^{-1}(\operatorname{im}\kappa_q)) across the previously audited 2-generator special-edge and 3-vertex common-sink models, then audit its intrinsic domain, q-blindness, gauge invariance, and separation on the smallest non-complete specially oriented graph.


## 2026-10-02 — 3-VERTEX COMMON-SINK TEST: ORIGIN PLANE RECOVERED

The first multi-special-edge stress test was completed at the smallest commuting-origin model
\[
G=\langle v_1,v_2,w\mid[v_1,v_2]=1,;wv_iw^{-1}=v_i^{1+q}\rangle.
\]
Here the intrinsic extension commutator defect at degree q has image
\[
\operatorname{im}\kappa_q
=\operatorname{span}\{\overline{v_1^q},\overline{v_2^q}\}.
\]
The restricted q-power operation therefore recovers the entire ordinary/origin plane:
\[
P_q^{-1}(\operatorname{im}\kappa_q)
=\operatorname{span}\{\bar v_1,\bar v_2\}.
\]
Since \(L_1\) has dimension three, the quotient by this plane is the one-dimensional sinkhole direction \(\bar w\). Thus the rank-2 quotient-line ambiguity disappears in this smallest common-sink multi-edge model.

Classification:
- common-sink extension defect: **PASS / LOCAL**;
- origin-plane recognition: **PASS / LOCAL**;
- sinkhole quotient direction: **PASS / LOCAL**;
- standard-family orientation bridge: **PASS / LOCAL**;
- general RAAG separation: **OPEN / LOAD-BEARING**.

Critical boundary: if ordinary origin vertices do not commute, degree-2 ordinary commutators survive below q, so \(W_q\) is not abelian and the simple \(\kappa_q\) pairing on \(W_q\) is unavailable. The next real problem is therefore to quotient/separate the degree-2 ordinary relation sector and retain the degree-q extension defect. This is the first genuinely general carrier question.

Detailed audit: research/PAPER3_RAAG_3VERTEX_COMMON_SINK_AUDIT_2026-10-02.md.
## 2026-10-02 — 2-GENERATOR FILTERED EXTENSION DEFECT: INTRINSIC CARRIER FOUND / GENERALIZATION OPEN

The gauge correction is now incorporated, and the next filtered-carrier attack has produced a genuine local result.

For
\[
G=\langle v,w\mid wvw^{-1}=v^{1+q}\rangle,
\]
the naive \(\operatorname{gr}(R)\) claim that the higher term \(v^q\) itself defines a degree-q relation-module class is rejected: the relator has initial degree 2, and \([w,v]\notin R\), so the subtraction argument is not an element of the relation subgroup.

The correct intrinsic object is the finite central extension
\[
1\to A_n=D_n/D_{n+1}\to W_{n+1}\to W_n\to1
\]
together with its commutator defect \(\kappa_n\) whenever \(W_n\) is abelian. In the 2-generator special-edge model:
\[
\operatorname{im}\kappa_n=0\ (n<q),\qquad
\operatorname{im}\kappa_q=\mathbf F_p\overline{v^q}\neq0.
\]
Thus q is recovered intrinsically as the first nonzero extension-commutator degree.

Combining this defect line with the restricted q-power operation gives, in the rank-2 model,
\[
\{x\in L_1:P_q(x)\in\operatorname{im}\kappa_q\}
=\mathbf F_p\bar v,
\]
so the ordinary/origin line is intrinsically recognized. The sinkhole direction is canonically the quotient
\[
L_1/\mathbf F_p\bar v,
\]
but a canonical complementary line in \(L_1\) has not been proved.

The former gauge obstruction is fully CLOSED: with the standard convention the sinkhole is w and
\[
\theta(v)=1,\quad\theta(w)=1+q,
\]
and \(v\mapsto v^a,\ w\mapsto v^cw\) preserves this canonical orientation.

Classification:
- central extension commutator carrier \(\kappa_q\): **PASS / LOCAL**;
- q as first nonzero defect degree: **PASS / LOCAL**;
- intrinsic origin-line recognition: **PASS / LOCAL**;
- literal canonical sinkhole line: **CONDITIONAL**;
- naive \(\operatorname{gr}(R)\) q-correction: **FAIL / CLOSED — WRONG OBJECT**;
- gauge orientation obstruction: **FAIL / CLOSED**;
- standard 2-generator orientation bridge: **PASS / LOCAL**, but not a new theorem because it still uses the known canonical special-edge formula;
- general RAAG directed/sinkhole separation: **OPEN / LOAD-BEARING**.

Detailed audit: research/PAPER3_RAAG_2GEN_FILTERED_EXTENSION_DEFECT_AUDIT_2026-10-02.md.

Immediate next gate: smallest genuinely multi-special-edge configuration; test whether the intrinsic extension-commutator defect separates multiple special sinks without presentation labels. No large computation, Paper 2, Mixed Fox, O_k, q=N_k, or W_11/W_12 reopening.
## 2026-10-02 — 2-GENERATOR RAAG GATE CORRECTED: FIRST SURVIVAL YES, INTRINSIC ROLE RECOGNITION OPEN

The first 2-generator special-edge stress test has been critically audited. The candidate threshold mechanism survives only at the Zassenhaus first-survival level: for [w,v]=v^q, the q-dependent term is invisible through W_q and first survives in W_{q+1}.

The stronger intrinsic role-recognition proof is not closed. The displayed Delta_q=im(Lambda^2 L_1 -> L_q) is ill-typed: the ordinary graded bracket L_1 wedge L_1 -> L_2, while the q-power term survives in L_q. A genuine proof therefore requires an intrinsic filtered relation-module/extension-class defect connecting the degree-2 relation to its degree-q correction.

An independent gauge family v -> v^a, w -> v^c w preserves the 2-generator group and its characteristic filtration while changing the displayed orientation character. This is a serious obstruction to recovering a generator-normalized theta from bare abstract-window data. Before calling this a theorem-level no-go, the exact scope of the literature's orientation-uniqueness statement must be reconciled with the automorphism family.

Classification:
- first q-defect survival at q+1: PASS/LOCAL;
- intrinsic sinkhole-line recognition at q+1: OPEN/LOAD-BEARING;
- ordinary graded Lambda^2 L_1 -> L_q construction: FAIL/CLOSED — TYPE MISMATCH;
- bare-window exact orientation recovery: STRONG NO-GO CANDIDATE / OPEN pending literature-scope reconciliation.

Detailed audit: research/PAPER3_RAAG_2GEN_SPECIAL_EDGE_AUDIT_2026-10-02.md.

Next authorized action: resolve the 2-generator filtered extension-class defect and the orientation-uniqueness/gauge compatibility before any larger RAAG computation.

## 2026-10-02 — SPECIAL ORIENTED PRO-p RAAG SELECTED AS ADJACENT OPEN GATE

Literature-first search identifies special oriented right-angled Artin pro-p groups as the strongest current adjacent-class candidate. For special digraphs, the canonical orientation is uniquely characterized by the Kummerian lifting property and is given by 1+q on sinkholes and 1 elsewhere. The class contains independent finite graph structure in addition to the p-power q parameter. citeturn3search0turn5search0

The candidate finite-window mechanism is:
degree-2 relation structure -> underlying graph;
degree-q correction in [w,u]=u^q -> special directed/sinkhole data and q;
canonical orientation -> [theta mod p^k].
The same N_k=p^{k-1}+1 threshold is plausible but remains CONDITIONAL.

New load-bearing gate:
**intrinsic directed/sinkhole separation from the abstract finite window**.
Presentation-dependent relator reading is not admissible. An intrinsic relation-module/extension-class descent is required.

Classification:
- special oriented pro-p RAAG orientation rigidity: PASS/LOCAL;
- non-q structural richness: PASS/LOCAL;
- candidate threshold: CONDITIONAL;
- full finite-window orientation identifiability: OPEN;
- intrinsic directed/sinkhole separation: OPEN/LOAD-BEARING.

Detailed gate: research/PAPER3_ORIENTATION_RIGID_ADJACENT_RAAG_GATE_2026-10-02.md.

## 2026-10-02 — ADMISSIBLE CATEGORY CRITIQUE / ADJACENT-CLASS ORIENTATION-RIGIDITY BOUNDARY

The proposed A–D admissible-category sketch was audited. It is useful as a design checklist but is not yet a valid minimality category: functoriality + finiteness + intrinsicity do not prevent target re-encoding, and quotient closure alone does not define a coarsest realization. A factorization preorder on explicitly non-reencoding realizations is required.

A critical correction was also recorded: \\(\bigoplus_{n\le N_k}\operatorname{gr}_n(G)\\) is the associated graded Zassenhaus object, not an abelianization. If used as a carrier, degree labels/operations must be retained. Likewise, the earlier vector-space bound \\(p^{\dim V}\ge k\\) requires the carrier observation to retain distinguishable elements/marked data; for bare vector spaces up to isomorphism it is false. The invariant lower bound \\(|\\operatorname{Iso}(C_k)|\\ge k\\) remains valid.

The first adjacent-class test was then completed using the free pro-p class. Literature states that for a free pro-p group, every orientation \\(\\theta:F\\to1+p\\mathbb Z_p\\) is 1-cyclotomic, whereas an infinite Demuškin group has a unique 1-cyclotomic orientation. Therefore, if the input remains the underlying un-oriented finite window \\(W_k(G)\\), orientation is not even a single-valued invariant on the free-pro-p class. No carrier constructed solely from that input can recover an arbitrary orientation.

Classification:
- A–D as complete admissible-category definition: FAIL/CLOSED — insufficient to exclude re-encoding.
- minimal-sufficiency analogy: PASS/LOCAL — factorization preorder only.
- proposed X_ab terminology: FAIL/CLOSED — associated graded, not abelianization.
- same-family graded-piece carrier as new theorem: FAIL/CLOSED — q-classification re-encoding.
- chi-twisted cohomological carrier: FAIL/CLOSED — target-circular.
- free-pro-p un-oriented orientation identifiability: FAIL/CLOSED — object-level non-identifiability.
- orientation-rigidity prerequisite: PASS/LOCAL.

Detailed audit: research/PAPER3_ADMISSIBLE_CATEGORY_AND_ADJACENT_CLASS_AUDIT_2026-10-02.md

Immediate next gate: find an adjacent class with a unique/canonical orientation but without Demuškin q-classification, then test finite-window identifiability. No new same-family compression, Mixed Fox, O_k, q=N_k, W_11/W_12, Paper 2, or large computation is authorized.

## 2026-10-02 — FULL-ORIENTATION COARSE REALIZATION BOUNDARY

T−1/T0 are closed at the declared standard odd-p fixed-rank Demuškin scope. The next attack asked for the coarsest intrinsic realization of the full target [χ_G mod p^k], rather than the weaker selector/recognition predicate.

A target-cardinality calculation gives a sharp information bound. For q=0 or q=p^s with s≥k, χ_k=1. For 1≤s<k, the target values are (1-p^s)^(-1) mod p^k, and these are pairwise distinct. Hence the full target has exactly k values. Any full-orientation carrier determined by W_k must therefore have at least k isomorphism classes; an F_p-vector-space carrier must have dimension at least ceil(log_p k). In the active p=3 case, the frozen 1D cup-line cannot encode the full orientation for k≥4. It remains a valid recognition/selector carrier, not a full orientation carrier.

The audited Demuškin window reconstruction yields an exact k-class defect-index carrier: read the first q-dependent Zassenhaus relation defect degree p^s for s<k, and use one stable symbol for q=0 or q≥p^k. This carrier reaches the information lower bound and factors to χ_k by the canonical formula. However, at the present standard-family scope it is classification-equivalent to q and therefore does not constitute a genuinely new theorem.

Classification:
- target cardinality |Ω_k|=k: PASS/CLOSED;
- universal carrier lower bound: PASS/CLOSED;
- vector-space dimension lower bound: PASS/CLOSED;
- exact defect-index realization: PASS/LOCAL;
- full-orientation factorization through defect index: PASS/LOCAL;
- genuinely new coarsest carrier theorem: FAIL/CLOSED — classification re-encoding.

Detailed audit: research/PAPER3_TOP_DOWN_FULL_ORIENTATION_COARSE_REALIZATION_AUDIT_2026-10-02.md

Immediate next gate: adjacent-class/general-target test. Do not reopen Mixed Fox, O_k, q=N_k, W_11/W_12, Paper 2, or the frozen cup-line proof. A new branch must first pass Object/Input/Functoriality/Gauge/Orientation bridge/q-blindness/Separation/Novelty/Stop.
## 2026-10-02 — TOP-DOWN T−1/T0 CLOSURE: INTRINSIC DEMUŠKIN ORIENTATION IS NOW IDENTIFIED

The target-identification defect found in the first top-down T0 attempt is repaired by an explicit literature theorem.

For the declared standard odd-p fixed-rank Demuškin family, Labute's Theorem 4 gives a unique continuous character
\[
\chi_G:G\to U_p
\]
with the crossed-derivation/Kummerian property. In the standard odd-p normal form
\[
G=\langle x_1,\ldots,x_d\mid x_1^q[x_1,x_2][x_3,x_4]\cdots=1\rangle,
\]
the same theorem gives
\[
\chi_G(x_2)=(1-q)^{-1},\qquad \chi_G(x_i)=1\ (i\ne2).
\]
Modern literature identifies this character as the canonical Demuškin orientation and as the unique 1-cyclotomic/Kummerian orientation. Hence the previous objection that the \((1-q)^{-1}\) formula was merely a presentation-level coefficient twist is no longer valid at this scope.

The target is defined basis-free as the isomorphism class of the canonical orientation \([\chi_G\bmod p^k]\). If \varphi:G\cong H\), then \chi_H\circ\varphi is a Kummerian orientation on G; uniqueness forces \chi_H\circ\varphi=\chi_G. Thus the target is functorial under abstract group isomorphism.

Combining this with the independently audited Demuškin finite-window reconstruction gives the corrected T0 result. Let \(N_k=p^{k-1}+1\).

- If \(q=p^s<p^k\), then \(s<k\) and \(q<N_k\); the intrinsic Zassenhaus graded defect below \(N_k\) recovers q.
- If \(q\ge p^k\) or \(q=0\), then the q-term is beyond the finite window and \(q\equiv0\pmod{p^k}\); therefore \((1-q)^{-1}\equiv1\pmod{p^k}\), and q=0 gives exactly 1.
- The previously used q=N_k case is impossible because standard odd-p Demuškin q is a p-power or 0, while \(p^{k-1}+1\) is not a p-power.

Therefore
\[
W_k(G)\cong W_k(H)\Longrightarrow[\chi_G\bmod p^k]=[\chi_H\bmod p^k]
\]
for the standard odd-p fixed-rank Demuškin family.

Classification:
- T−1 target identification: **PASS/CLOSED** at declared standard scope.
- Demuškin finite-window T0 orientation identifiability: **PASS/CLOSED** at declared standard scope.
- Previous T0 PASS: **HISTORICAL/SUPERSEDED** (invalid inference repaired by theorem-level target identification).
- Broad orientation non-identifiability: **OPEN/NOT PROVED**.
- Observability-depth monotonicity: **OPEN**.
- New carrier construction is no longer blocked by T0, but any candidate must still pass Object/Input/Functoriality/Gauge/Orientation bridge/q-blindness/Separation/Novelty/Stop.
- Mixed Fox remains **FAIL/CLOSED — REDUNDANT** as a new recognition carrier; its finite projective object remains PASS/LOCAL.

Detailed audit:
research/PAPER3_TOP_DOWN_T1_T0_CLOSURE_2026-10-02.md

Immediate next gate:
**coarsest/non-tautological intrinsic realization of the already-forced finite-window map \(W_k\mapsto[\chi_k]\)**. No reopening of Mixed Fox, q=N_k, W_11/W_12, or Paper 2.



## 2026-10-02 — TOP-DOWN T0 CORRECTION: TARGET IDENTIFICATION IS LOAD-BEARING

The external critical review found a substantive error in the first T0 audit draft. The carrier-independent top-down method is valid, but the attempted closure of T0 for the standard Demuškin family was invalid because it identified Labute's presentation-level crossed-derivation/coefficient value
\[
\theta(x_2)=(1-q)^{-1}
\]
with the intrinsic Demuškin orientation/cyclotomic character without an explicit theorem establishing that identification.

Therefore:
- previous T0 PASS/CLOSED: **HISTORICAL / SUPERSEDED — invalid inference**;
- target identification (T-1): **OPEN / LOAD-BEARING**;
- finite-window orientation identifiability T0: **OPEN / LOAD-BEARING**;
- broad orientation no-go: **OPEN / NOT PROVED**;
- broad extension reconstruction no-go: **FAIL / CLOSED** remains valid;
- automatic observability-depth monotonicity: **FAIL / CLOSED**; monotonicity itself remains OPEN.

The corrected audit is:
research/PAPER3_TOP_DOWN_T0_CORRECTION_2026-10-02.md

The literature gate already establishes that canonical Demuškin/Kummerian/cyclotomic orientation theory is known, while the project's finite-window factorization problem is distinct. The immediate task is therefore not to rediscover orientation existence, but to fix the exact target object and prove/cite the relation among Demuškin orientation, cyclotomic orientation, and the Labute coefficient twist under the declared hypotheses.

No new carrier construction is authorized before T-1 and T0.


## 2026-10-02 — TOP-DOWN REFRAME: ORIENTATION IDENTIFIABILITY BEFORE CARRIER SEARCH

A genuinely different research direction is authorized at framework level: reverse the usual bottom-up search finite-window -> carrier -> chi into target-first orientation -> finite observability -> coarsest sufficient information -> intrinsic realization.

The decisive first question is whether chi_k(G)=chi_G mod p^k is constant on every finite-input equivalence class W_k(G)≅W_k(H). If a same-W_k/different-chi pair exists, then no carrier functorially constructed solely from W_k can recover chi_k; this is a carrier-independent no-go theorem. If identifiability is proved, only then should an intrinsic carrier be sought as a realization of the target-defined observable quotient.

This reframing does not reopen O_k minimality, Mixed Fox, q=N_k, W_11/W_12, Paper 2, or p=2. It creates a new load-bearing gate: T0 finite-window orientation identifiability. The earlier discovery-ladder idea of extension-fiber rigidity is retained as one possible mechanism for proving or refuting T0, not as the carrier itself.

Classification:
- top-down identifiability framework: PASS / LOCAL;
- T0 finite-window orientation identifiability: OPEN / LOAD-BEARING;
- carrier construction before T0: NOT AUTHORIZED;
- target-defined coarsest quotient: CONDITIONAL / specification only;
- observability-depth invariant: OPEN.

Detailed audit: research/PAPER3_POST_EXPLORATION_TOP_DOWN_ORIENTATION_IDENTIFIABILITY_2026-10-02.md


## 2026-10-02 — CRITICAL REVIEW OF EXTERNAL LEDGER INTERPRETATION

The external critique was audited against the authoritative state. It is accepted only in part.

- O_k diagnosis is correct: O_k -> C is the quotient universal property, while terminal-style unique C -> O_k fails by the direct-sum counterexample. However, an admissible carrier category is not yet a mathematical category until objects, morphisms, and closure are specified; this is not the immediate load-bearing target.
- The proposed next step direct Fox jet -> chi is stale. That bridge was already established at PASS/LOCAL scope for the standard family. The Mixed Fox branch was later closed as a new-recognition carrier because its finite-pair information is redundant at the declared scope, not because the direct Fox bridge failed.
- The proposed q-blindness definition by replacing q with 0 is rejected as a general definition. q=0 is a genuine Demushkin regime, and substitution can change the group/class. q-blindness should constrain the definition/input, while separation and output sensitivity are tested separately.
- Reopening p=2/non-standard Demushkin cases is not authorized now; q=0 is already included in the odd-p standard family. Such cases may be future stress tests only after a genuinely new carrier survives the structural gates.
- Evidence-type enforcement is accepted, but status labels remain mandatory protocol summaries. Correct rule: labels never substitute for explicit evidence and scope.

Detailed audit: research/PAPER3_POST_EXPLORATION_CRITICAL_REVIEW_2026-10-02.md

Current active gate remains: genuinely new finite-input carrier search, after Object/Input/Functoriality/Gauge/Orientation bridge/q-blindness/Separation/Novelty/Stop checks.


## 2026-10-02 — CRITICAL REVIEW OF POST-PAPER-3 EXTERNAL LEDGER INTERPRETATION

The proposed external review was audited against the authoritative state. It is accepted only in part.

- O_k diagnosis is correct: O_k -> C is the quotient universal property, while terminal-style unique C -> O_k fails by the direct-sum counterexample. However, an "admissible carrier category" is not yet a mathematical category until objects, morphisms, and closure are specified; this is not the immediate load-bearing target.
- The proposed next step "direct Fox jet -> chi" is stale. That bridge was already established at PASS/LOCAL scope for the standard family. The Mixed Fox branch was later closed as a new-recognition carrier because its finite-pair information is redundant at the declared scope, not because the direct Fox bridge failed.
- The proposed q-blindness definition by replacing q with 0 is rejected as a general definition. q=0 is a genuine Demushkin regime, and substitution can change the group/class. q-blindness should constrain the definition/input, while separation and output sensitivity are tested separately.
- Reopening p=2/non-standard Demushkin cases is not authorized now; q=0 is already included in the odd-p standard family. Such cases may be future stress tests only after a genuinely new carrier survives the structural gates.
- Evidence-type enforcement is accepted, but status labels remain mandatory protocol summaries. Correct rule: labels never substitute for explicit evidence and scope.

Detailed audit: research/PAPER3_POST_EXPLORATION_CRITICAL_REVIEW_2026-10-02.md

Current active gate remains: genuinely new finite-input carrier search, after Object/Input/Functoriality/Gauge/Orientation bridge/q-blindness/Separation/Novelty/Stop checks.
## 2026-10-02 — POST-PAPER-3 DISCOVERY LADDER REVIEW

The proposed “failure → boundary → axiom → adjacent class” strategy is accepted as a useful correction to the post-Paper-3 exploration program, but three repairs are required before authorization.

First, the arbitrary-extension counterexample is a boundary marker: positive descent requires rigidity of the admissible extension-class fiber over the finite window. This is a better abstraction than the presentation-dependent phrase “relator coupling.”

Second, rank variation is not a substantive first theorem: Demuškin rank is already visible through H^1 of the finite quotient, and the standard odd-p classification has rank constraints. The proposed T1 is therefore reformulated as a control/sanity check, not the main discovery target.

Third, the proposed relator axiom (R) is not intrinsic as written, and T2 does not follow from it. The condition must first be expressed on an invariant relation-module/extension-class object. Likewise the proposed T3 for all mild pro-p groups is too strong: mildness controls initial forms/graded structure but does not by itself imply finite-window determination of the next extension layer. Literature confirms strong graded consequences of mildness, but not the proposed shallow-window rigidity theorem. citeturn0search3turn0search8

Revised active gate:
\[
\mathfrak F(W)=\{[E]:E\text{ admissible and projects to }W\},\qquad |\mathfrak F(W)|=1?
\]
The next authorized attack is to identify the smallest higher-order deformation invisible to W_k, test whether it changes the extension class E_k, and then formulate the weakest intrinsic condition that removes that deformation. Only after such a rigidity class survives should a genuinely new q-free orientation carrier be defined.

Classification:
- failure-to-boundary reinterpretation: PASS / LOCAL;
- original S1/T1: CONDITIONAL / REFORMULATE;
- original R/T2: OPEN / NOT YET INTRINSIC;
- T3 for all mild pro-p: FAIL / CLOSED as overstrong target;
- nearest-class rigidity search: OPEN / LOAD-BEARING;
- genuinely new q-free carrier: OPEN.

Detailed audit: research/PAPER3_POST_EXPLORATION_DISCOVERY_LADDER_REVIEW_2026-10-02.md

## 2026-10-02 — MIXED FOX NATURALITY CLOSED AT INTRINSIC SCOPE / NEW-CARRIER BRANCH CLOSED

The final naturality attack produced two corrections and one closure.

First, the earlier q=N_k boundary case was mathematically vacuous: in the standard odd-p Demuškin family q=p^s or 0, while N_k=p^{k-1}+1 is not a p-power. The correct reconstruction has only two genuine regimes:
- q<p^k: q is detected intrinsically below N_k;
- q>=p^k (or q=0): the q-term is invisible through the window and all such cases give the same truncated extension window.

Second, for intrinsicity the needed morphisms are filtered finite-pair **isomorphisms**. If W_k(G)≅W_k(H), the reconstructed Demuškin windows are isomorphic up to the same q-regime, and the finite projective Mixed Fox construction is invariant under the induced group-algebra/Fox-Lyndon transport, Nielsen Jacobians, relation-generator gauge, relator conjugation, and mixed truncation. Therefore:
- pair-isomorphism covariance: **PASS / CLOSED**;
- pair -> extension-window reconstruction: **PASS / CLOSED** at declared standard scope;
- finite-pair -> projective Mixed Fox object: **PASS / LOCAL**.

Arbitrary non-invertible morphism functoriality remains OPEN, but it is not load-bearing for intrinsic isomorphism-class well-definedness.

Third, the non-redundancy gate closes the Mixed Fox branch as a new recognition theorem. At fixed rank in the standard Demuškin family, the finite extension window carries only the q-regime visible at the stated precision; extracting chi mod p^k from it via q/classification is classification repackaging, explicitly not a new orientation bridge. Thus:
- Mixed Fox as a genuinely new recognition carrier: **FAIL / CLOSED — REDUNDANT**.
- genuinely new carrier search: **OPEN**.

Detailed audit:
research/PAPER3_MIXED_FOX_NATURALITY_NONREDUNDANCY_DECISION_2026-10-02.md

No W_11/W_12, large Fox scan, q=N_k reopening, or Paper 2 reproof is authorized. Next branch must be genuinely different finite-input carrier and pass Object/Input/Functoriality/Gauge/Orientation bridge/q-blindness/Separation/Novelty/Stop.

## 2026-10-02 — DEMUŠKIN PAIR DESCENT / NATURALITY BOUNDARY

The admissibility/fiber prerequisite has been pushed one step further and its logical scope is now fixed.

For
\[
N_k=3^{k-1}+1,\quad
Q_k=G/D_{N_k},\quad
E_k=G/D_{N_k+1},\quad
A_k=D_{N_k}/D_{N_k+1},
\]
inside the declared standard odd-p fixed-rank Demuškin family:

- q<N_k is intrinsically recovered from the first q-dependent Zassenhaus graded defect below N_k;
- q=N_k is separated from q>N_k by the boundary-layer dimension of A_k;
- q>N_k (including q=0) gives the same truncated extension window.

Hence the forgetful fiber is a singleton **up to extension-window isomorphism**.

The crucial correction is that this proves object/isomorphism-class reconstruction, not automatically a functorial section on arbitrary pair morphisms. Therefore:

- Demuškin pair -> extension-window reconstruction: **PASS / CLOSED at isomorphism-class scope**;
- extension-window -> projective Mixed Fox jet: **PASS / LOCAL**;
- bare finite-pair -> Mixed Fox jet as an isomorphism-invariant assignment: **PASS / LOCAL**;
- full categorical natural transformation through a specified Pair_k morphism category: **OPEN**.

The broad arbitrary-central-extension no-go remains **FAIL / CLOSED** and is not contradicted.

Primary literature control: Labute/Demuškin classification and Mináč–Rogelstad–Tân Zassenhaus-dimension results; Fox/Lyndon relation-module mechanism is standard. The project-specific categorical factorization remains our own load-bearing step.

Detailed audit:
research/PAPER3_MIXED_DEMUSHKIN_PAIR_DESCENT_NATURALITY_AUDIT_2026-10-02.md

Next authorized action: formal covariance/naturality of the projective Mixed Fox construction under extension-window isomorphisms, Nielsen/generator change, relation-generator gauge, relator conjugation, and mixed truncation. No W_11/W_12, large Fox, 45-dimensional, or Paper 2 reproof computation.

## 2026-10-01 — DEMUŠKIN ADMISSIBILITY / EXTENSION-FIBER RECONSTRUCTION GATE

The admissibility prerequisite for the Mixed Fox branch has now been made explicit at the declared standard scope.

Define the active category ExtWin^Dem_{k,d} by canonical Zassenhaus windows
1 -> A_k=D_{N_k}/D_{N_k+1} -> E_k=G/D_{N_k+1} -> Q_k=G/D_{N_k} -> 1,
N_k=3^{k-1}+1,
arising from infinite odd-prime finite-rank Demuškin groups of fixed rank d, with q(G) a p-power or 0. Morphisms are whole-extension isomorphisms.

A fiber analysis gives three cases:
- q<N_k: Q_k sees the first q-dependent Zassenhaus graded relation;
- q=N_k: Q_k does not see the q-term, but dim A_k distinguishes the degree-N_k relation;
- q>N_k (including q=0): the q-term is invisible through E_k, so the extension window itself is independent of q.

Thus, within the standard odd-p fixed-rank Demuškin family,
(Q_k,A_k) => [E_k -> Q_k]
up to extension-window isomorphism.

Classification:
- admissible Demuškin category definition: PASS / CLOSED at declared scope;
- Demuškin fiber reconstruction: PASS / LOCAL;
- extension-window -> mixed Fox: PASS / LOCAL;
- original bare-pair -> mixed Fox: OPEN / LOAD-BEARING;
- arbitrary-extension pair descent: FAIL / CLOSED only for the broad category;
- Paper 3: FROZEN / COMPLETE.

This materially narrows the previous OPEN gate. The next authorized action is formal lemma packaging plus independent naturality/projective-covariance verification. No large Fox computation is authorized.

Detailed audit: research/PAPER3_MIXED_DEMUSHKIN_ADMISSIBILITY_RECONSTRUCTION_AUDIT_2026-10-01.md.

## 2026-10-01 — POST-PAPER-3 RESEARCH SCOPE FROZEN: CARRIER UNIVERSALITY / MINIMALITY ONLY

The next research branch is now deliberately narrowed to exactly two possible outcomes:

1. attack the **finite-pair universal property / minimality** of the existing carrier; or
2. construct a **genuinely new carrier** that is not merely a reformulation/compression of the frozen Paper 3 selector.

Nothing else is authorized as a primary research target.

In particular:
- Paper 3 itself remains **FROZEN / COMPLETE** and is not to be re-proved.
- The completed Kummer selector, full delta-family, intrinsic cup-line, and prior Gate D proof machinery are fixed inputs/boundaries, not targets for reproof.
- No larger-window calculation (including W_11/W_12), Fox computation, or high-dimensional carrier computation is authorized unless it is forced by the finite-pair universal/minimality question or by a genuinely new carrier construction.
- A carrier counts as genuinely new only if it is finite-input, q-blind, functorial, gauge-independent, and non-equivalent to the frozen selector, with a new separation/threshold/factorization consequence.
- Any minimality statement must name its admissible carrier category; “absolute minimality” without a category is not an authorized claim.

Immediate decision gate:
**finite-pair universal property/minimality → PASS/LOCAL, FAIL/CLOSED, or OPEN; otherwise new-carrier construction.**

This scope supersedes broader historical roadmap language that would reopen F1/F2 recognition branches merely for additional family examples. Those branches remain historical/conditional unless they directly supply a new carrier or resolve the finite-pair universal/minimality problem.


## 2026-10-01 — POST-PAPER-3 CARRIER NON-REDUNDANCY AUDIT

The first post-Paper-3 carrier battleground has been taken to its current structural boundary.

- Paper 3 본체: **FROZEN / COMPLETE**.
- Paper 2 selector: **FROZEN / COMPLETE; no reproof authorized**.
- single-vector t_2: **FAIL / CLOSED** as an intrinsic carrier.
- full delta-family: intrinsic as a proof/input family, but **FAIL / CLOSED — REDUNDANT** as a new post-Paper-3 recognition theorem because its zero predicate is exactly the completed Kummer selector.
- finite one-dimensional cup-line: **PASS / LOCAL** as an intrinsic compression at the audited scope, but **FAIL / CLOSED — REDUNDANT** as a new recognition theorem for the same reason.
- transgression quotient O_k: **PASS / LOCAL** as the finite proof carrier; universal/minimal finite-pair status remains **OPEN**.
- genuinely new non-redundant finite-pair carrier: **OPEN**, but only if it is finite-input, q-blind, functorial, gauge-independent, non-equivalent to the frozen selector, and yields a new category-relative separation/threshold statement.

This is a post-Paper-3 research boundary, not a reopening of Paper 3. No W_11/W_12, Fox, or 45-dimensional computation is authorized merely to repackage the completed selector.

Detailed audit: research/POST_PAPER3_CARRIER_NONREDUNDANCY_AUDIT_2026-10-01.md.

## 2026-10-01 — PAPER 3 본체 고정 / 후속 일반화 연구 트랙 분리

중요한 연구-정체성 정정이다.

- **Paper 3 본체:** 이미 완성된 논문으로 간주하고 고정한다. 현재 후속 연구에서 Paper 3의 정리·증명·완성도를 다시 검증하는 것으로 해석하지 않는다.
- **현재 작업:** Paper 3에서 제시한 **후속 연구 프로그램**, 즉 finite-window → intrinsic carrier → global orientation으로의 일반화 가능성을 별도 연구 가지로 공격한다.
- (t_2), full (delta)-family, intrinsic carrier, Gate D는 Paper 3 본체의 필수 증명 단계가 아니다.
- 후속 연구가 실패하거나 닫혀도 Paper 3 본체의 기존 정리와 완성본은 영향을 받지 않는다.
- Paper 2 selector를 다시 증명하지 않는다. 완료된 선행 결과는 후속 연구의 고정 입력/경계로만 사용한다.

정확한 트랙:
[
oxed{	ext{Paper 3 본체}=	ext{완성·고정}}
qquad
oxed{	ext{현재 작업}=	ext{Paper 3 이후의 후속 일반화 연구}}
]

앞으로 “Paper 3의 핵심 주장을 다시 검증한다”는 표현은 사용하지 않는다. 정확한 표현은 **“Paper 3 이후 후속 일반화 연구에서 carrier의 생존 여부를 검증한다”**이다.

현재 후속 연구의 첫 실제 승부처는 carrier intrinsicity / functoriality / gauge independence이며, 다음 승부처는 orientation bridge의 비중복성이다. 구조적 실패 시 해당 후속 carrier branch만 닫고 Paper 3 본체나 Paper 2 selector를 재개방하지 않는다.

## 2026-10-01 — F2 ONE-TIME INDEPENDENT CONTROL AUDIT / COMPLETENESS LIMIT

The F2 branch was independently checked once, without reopening the search. The F2 rank-4 quadratic relation pencil has direct Pfaffian \(a^2\). The recovered elementary-type candidate list contains exactly two construction shapes in the surviving audit trail: (i) split/free-product rank-2 one-relator factors, with Pfaffian \(ab\); and (ii) a shared-direction cyclotomic semidirect shape with a free rank-1 factor, with Pfaffian \(0\).

The direct Pfaffian calculation is **PASS / CLOSED** for these examined candidates. But the repository does not independently prove that the recovered two-shape list is exhaustive for the entire standard elementary-type rank-4/two-relator class.

Therefore the correct status is:
- F2 × recovered examined candidates: **FAIL / CLOSED**.
- completeness of examined candidate list: **OPEN**.
- F2 × arbitrary cyclotomic pro-p group: **OPEN / CONDITIONAL**.
- F2 W4 computation: **NOT AUTHORIZED**.
- operational F2 branch: **CLOSED** unless new evidence supplies a new construction or proves completeness.
- broad F2 finite-window recognition: **OPEN / CONDITIONAL**.

This supersedes the stronger wording that the standard elementary-type construction mechanism itself had been ruled out. The correct statement is candidate-level, not universal.

Detailed audit: research/PAPER3_F2_SAME_W3_CONTROL_GATE_2026-10-01.md

## 2026-10-01 — F2 STANDARD ELEMENTARY-TYPE CONTROL ROUTE CLOSED

The F2 same-W3 search was carried through the authorized construction-level pre-check. Literature confirms cyclotomic free products and fibre/semidirect constructions as legitimate control mechanisms, but the standard elementary-type class cannot supply a rank-4 two-relator quadratic relation plane of F2 repeated-root Pfaffian type. Symbolic rank/relation bookkeeping reduces the relevant rank-4/two-relator shapes to Pfaffian ~ab or Pfaffian 0, whereas F2 has Pfaffian ~a^2.

Status:
- F1 uniformity: not reopened; remains PASS/CLOSED at declared pairwise scope.
- F2 same-W3 control in standard elementary-type class: **FAIL / CLOSED**.
- F2 same-W3 control among arbitrary cyclotomic pro-p groups: **OPEN / CONDITIONAL**.
- finite W4 computation: **NOT AUTHORIZED** because no genuine W3-matching control was found.
- broad F2 finite-window recognition: **OPEN / CONDITIONAL**.

This is a structural boundary, not an absolute no-go theorem for every cyclotomic pro-p group. The next escalation, if pursued, must be a genuinely non-elementary cyclotomic construction with explicit W3 matching; otherwise the F2 branch should be closed as a control-search dead end.

Detailed record: research/PAPER3_F2_SAME_W3_CONTROL_GATE_2026-10-01.md.

## 2026-10-01 — F2 SAME-W3 CYCLOTOMIC CONTROL GATE CLOSED

The F2 same-W3 control search is now closed at the authorized structural level. For the smallest rank-4 F2 relation space, the Pfaffian pencil has repeated-root type \(a^2\). The audited standard elementary-type cyclotomic constructions with rank 4 and two defining relations have only Pfaffian type \(ab\) or \(0\); these are not GL4-equivalent to \(a^2\).

Status:
- F2 × standard elementary-type cyclotomic control: **FAIL / CLOSED**.
- F2 × arbitrary cyclotomic pro-p group: **OPEN / CONDITIONAL**; no universal no-go theorem is claimed.
- F2 \(W_4\) computation: **NOT AUTHORIZED**.
- F2 broader finite-window recognition: **OPEN / CONDITIONAL**.

This closes the standard construction mechanism rather than all possible cyclotomic pro-p groups. F1 is not reopened. No large computation is authorized merely to force a nonstandard control.

Detailed record: research/PAPER3_F2_SAME_W3_CONTROL_GATE_2026-10-01.md
## 2026-10-01 — F1 SAME-W3 OBSTRUCTION / W4 INTRINSIC SEPARATION AUDIT

The concrete (p,d,q)=(3,2,3) pair has now passed an independent W4 intrinsicity audit. The earlier presentation-local equation is not used as the invariant. Instead, the truncated restricted relation module has a canonical degree-3 p-power component: it is zero for F1 and nonzero for the cyclotomic free-product control. This is preserved by restricted-Lie isomorphisms.

Status:
- W3 equality: **PASS / CLOSED**.
- W4 intrinsic separation: **PASS / CLOSED** for the declared pair.
- Exact two-object threshold r=4: **PASS / CLOSED**.
- Uniform q=p^f extension: **OPEN / LOAD-BEARING**.
- Broad category-level recognition theorem: **OPEN / CONDITIONAL**.
- Novelty/priority: **OPEN / CONDITIONAL**; no priority claim.

Authoritative audit: research/PAPER3_W4_INTRINSIC_SEPARATION_AUDIT_2026-10-01.md

Parameter-uniform finite-q threshold is now **PASS / CLOSED** for the declared F1/cyclotomic-control pair: r=q+1 for every finite q=p^f, p odd, d>=2. Next authorized gate: seek a genuinely broader category or a same-window obstruction beyond this pair; do not infer a broad recognition theorem from the pairwise result.


## 2026-10-01 — THREE-PAPER PUBLICATION-STYLE FINALIZATION

A style-only publication pass was completed on the three already-audited manuscript sources. The mathematical content and research classifications are unchanged.

- Paper 1 style-final branch: paper1-style-final-2026-10-01; 8-page PDF; SHA-256 b4806dc7ed111ffeb3b93d5ef9066d958252fff132506a5d95f25dad76afe960; PASS/CLOSED.
- Paper 2 style-final branch: paper2-style-final-2026-10-01; 13-page PDF; SHA-256 97504d2bc5db7f668f2287d62bca902cde0b285b1a4b7ef11ffe58c0c8928e32; PASS/CLOSED.
- Paper 3 style-final branch: paper3-style-final-2026-10-01; 17-page PDF; SHA-256 3518e5f966401d48eae9c8b76b80fe7a9ba4e53f76bc4255edb66862082bf7ff; PASS/CLOSED.
- Removed companion/placeholder boilerplate, reduced repetitive defensive novelty language, standardized finite coefficient notation, improved introductions, and replaced informal "kills" terminology.
- Paper 3 uses the source-correct dedicated style-final workflow because the legacy paper3-build workflow targets the older paper3/main.tex application manuscript.
- PDF text extraction and first-page visual checks passed.
- Publication novelty remains OPEN / CONDITIONAL; mathematical frontier unchanged.
- Detailed record: research/THREE_PAPER_PUBLICATION_STYLE_FINAL_2026-10-01.md.

## 2026-09-28 — THREE-PAPER ARTIFACT GATE FINALIZATION

The authoritative three-paper revision checklist has now been followed through the source→CI→PDF→independent audit chain.

- Paper 1: branch paper1-fixes-2026-09-28, authoritative paper/successor_main.tex blob 1855e9a992a98caf0a0f6deae484f13e049d0a20; source-correct CI run 36401507321; PDF artifact 10960891547; 8 pages; PDF SHA-256 4efec62888f3803935717658f9f638902ff2ef2bd8845c83a32dc6770542e5ef. Source identity, PDF text, visual pages, and checksum passed. PASS / CLOSED.
- Paper 2: authoritative manuscript source blob 7411d241505b8a0a496f46cee05bbecc8d40eb47 was restored exactly on CI branch paper2-ci-clean-2026-09-28; final exact-source CI run 36401141711; full artifact 10959918919; 13 pages; PDF SHA-256 1381f75048bf0f83d9174c6a2b8bb85b31e62010f945697413182c9f5be94c64. Source identity, U4/U5c text, PDF visual audit, and checksum passed. PASS / CLOSED.
- Paper 3: authoritative paper/main.tex blob aa351f77c07a748588208d0d383f0c4dbd6dfca7; CI run 36395985678; full artifact 10957609279; 17 pages; PDF SHA-256 2be2e84e06eb77eb9e6e4c9bbfb522bb037db5675bb04c7a9a0c6bac34a9787e. Source identity, §8 cup-line chain, D4 threshold, literature audit, PDF visual audit, and checksum passed. PASS / CLOSED.
- Publication novelty remains OPEN / CONDITIONAL; no priority claim.

Important synchronization correction:
- The generic paper-build.yml on the Paper 1 branch builds paper/main.tex, not paper/successor_main.tex. Its successful run therefore produced a Paper 2 PDF and was not accepted as Paper 1 evidence.
- A dedicated source-correct .github/workflows/paper1-build.yml was added on the Paper 1 branch; the resulting run is the authoritative Paper 1 CI artifact.
- This was caught by the required independent source↔artifact identity check; no wrong artifact was promoted.

Literature verification completed:
- Claudio Quadrelli, Cohomology of absolute Galois groups, arXiv:1412.7685: author/title/source identity verified.
- J. Mináč, N. D. Tân, N. T. Trà, Zassenhaus filtrations as intersections, arXiv:2510.20133: author/title and its broader representation-theoretic Zassenhaus scope verified; Paper 1 now records it as surrounding literature, without claiming identity with the exact affine theorem.
- Labute Theorem 4 / Proposition 6 orientation attribution and the standard Demuškin classification boundary were independently cross-checked against later literature reproducing those exact references.
- NSW Chapter III / Theorem 3.9.15 and the PD²/Demuškin relationship were cross-checked through secondary sources; no MathSciNet/zbMATH Open search is claimed.

Mathematical U5c check:
- Paper 2 U5c's finite-coefficient PD² duality argument is internally type-correct: the dual of the socle inclusion is the reduction map A_{k-1} -> F_3, hence surjective and therefore the original H^2 map is injective.

## 2026-09-28 — THREE-PAPER REVISION CHECKLIST GATE

The supplied revision checklist is now the controlling edit list for the three manuscripts.

- Paper 1: source revision branch `paper1-fixes-2026-09-28`; LaTeX compilation PASS, workflow verification blocked only by citation-warning hygiene. Artifact gate OPEN/PENDING.
- Paper 2: clean source revision branch `paper2-fixes-clean-2026-09-28`; clean CI compilation PASS (run 36398580257). Artifact gate OPEN/PENDING exact PDF/content/hash verification.
- Paper 3: source revision branch `paper3-fixes-2026-09-28`; CI compilation/build PASS. Artifact gate OPEN/PENDING exact PDF/content/hash verification.
- No intermediate failed Paper 2 patch branch is authoritative.
- Publication novelty remains OPEN/CONDITIONAL.


## 2026-09-28 — PAPER 3 ARTIFACT GATE CLOSED

The repaired source commit `dd3d2e69c4e320129a3d0025c853747dabe744e4` successfully completed the `Build paper PDF` workflow (run `36393007041`). The CI-built submission bundle was independently unpacked and checked.

The packaged `main.tex` has Git blob SHA `0a71fab5f2227b7f4659d5f10fca3e555c7add8b`, matching the authoritative current `paper/main.tex`. The CI PDF is 17 pages. The repaired §8 typed cohomology chain and the subsequent Lemma 5.2 comparison were verified in the extracted PDF text, and pages 9–10 were visually inspected.

CI submission PDF checksum: `2ab01035bb42a16b36b2f1efafa66cafda9c73b041c5a3c5c5aa2c9ca5a8e697`.

Classification:
- artifact gate: **PASS / CLOSED**
- overall Paper 3: **INTERNAL REVIEW PASSED**
- publication novelty: **OPEN / CONDITIONAL**

## 2026-09-28 — PAPER 3 §8 CUP-LINE TYPE REPAIR

The authoritative `paper/main.tex` was repaired at commit `dd3d2e69c4e320129a3d0025c853747dabe744e4`.

The previous §8 sentence incorrectly described the image of \\(\iota_*\\) as still lying in \\(H^2(G,\\mathbb F_3)\\). It is now written with the explicit typed chain
\\[
C_k\xrightarrow{\operatorname{infl}}H^2(G,\mathbb F_3)
\xrightarrow{\iota_*}H^2(G,A_{k-1}(\chi_{k-1})),
\\]
followed by Lemma U5b's identification with the connecting-map variation.

Primary-source verification against Mináč–Pasini–Quadrelli–Tân (Adv. Math. 380 (2021), §7):
- Proposition 7.1: relation initial forms and cup-product evaluation form a commutative pairing diagram.
- Proposition 7.2: for odd p, the relevant degree-two pairing is perfect on the alternating part \\(\Lambda^2(V)\\).
- The present p=3 rank-four relation has one-dimensional degree-two initial-form span, so the §8 finite cup carrier has rank one.

Classification:
- §8 type repair: **PASS / CLOSED**.
- §8 rank-one primary-source compatibility: **PASS / LOCAL**.
- Publication artifact gate: **OPEN / PENDING exact-source CI + PDF/content audit + checksum**.
- Publication novelty: **OPEN / CONDITIONAL**.

The mathematical frontier is unchanged; this is a source-detail repair and independent literature verification.

## 2026-09-28 — PAPER 3 DETAIL REPAIR / LITERATURE AUDIT CURRENT STATE

The authoritative Paper 3 source changed at commit `470d06e34088db2b101acac7ad3bf4b0eaa1bb02`.

Applied:
- §9 lower-bound wording corrected to distinguish (m\le3^{k-2}) (outside (mathcal D_{k,m})) from (3^{k-2}<m\le3^{k-1}) (inside domain, selector fails).
- U5c final sentence now explicitly derives injectivity of (iota_*) from surjectivity of its dual.
- Literature audit wording records only searches actually performed: arXiv and general web searches on 2026-09-28; MathSciNet/zbMATH Open are not claimed.

Targeted literature result:
- Efrat–Quadrelli 2019 confirms prior art for Kummerianity/cohomological and 1-cocycle lifting.
- Mináč–Pasini–Quadrelli–Tân 2021 confirms the minimal-presentation relation/cup-product pairing used here.
- No exact theorem combining the present bare-(Q_k), arbitrary-candidate, finite Kummer recognition, and fixed-scope sharp selector-depth package was identified in the targeted search.

Classification:
- mathematical frontier: unchanged, PASS / CLOSED at declared scope;
- literature audit: PASS / LOCAL;
- publication artifact gate: OPEN / PENDING exact-source CI + PDF/content audit + checksum.

## 2026-09-28 — THREE-PAPER MATHEMATICAL CONTRIBUTION ASSESSMENT RECORDED

For future research continuity, the researcher-facing synthesis is frozen in:
`research/THREE_PAPER_MATHEMATICAL_CONTRIBUTION_ASSESSMENT_2026-09-28.md`.

The three-paper arc is recorded as:
**Paper 1 = finite recognition/factorization → Paper 2 = sharp affine threshold (p^{k-1}+1) → Paper 3 = recognition at the sharp scale, with fixed rank-4 (p=3) selector threshold (3^{k-1}+1) and 1D linear selector-carrier minimality.**

Overall mathematical assessment: **research-level coherent finite-recognition program at the declared scopes**.
Publication novelty: **OPEN / CONDITIONAL**; no priority claim.

This is an explanatory synthesis only; authoritative mathematical classifications remain in the individual Gate/audit records.



## 2026-09-28 — PAPER 3 EXACT-SOURCE ARTIFACT GATE CLOSED

The repaired `paper/main.tex` has now passed the exact-source CI/PDF gate and independent artifact audit.

Authoritative source: `ac53cc2e753fc7b8fb0eb4b78a0085ccfdbc5a89`; blob `3f0bc48ac532d0ed72bcfe876a8283bed178dfbc`; source SHA-256 `bc951dce61717ed184e8763118a3ffef310615b09b95b8fd6ae7ca0a83e42a49`.
CI run **36374270475** and PDF verification: **PASS / CLOSED**. PDF artifact **10950077812**, SHA-256 `d38c63bd1b453482217c7876d818ff7b50e48cbde7f219552953d8a5e36d56c0`, 17 pages. Independent PDF/content audit: **PASS / CLOSED**.

The publication artifact gate is therefore **PASS / CLOSED**. No earlier PDF remains authoritative.
## 2026-09-28 — PAPER 3 REFEREE DETAIL REPAIR 2 / ARTIFACT GATE

The authoritative manuscript source was repaired in commit `2ab97e7d11f5238f6586aa435c9da36d62781d91`. The source-level repair is complete and rechecked. The exact commit triggered Build paper PDF run `36373920812`, currently **IN PROGRESS**.

The publication artifact remains **OPEN / PENDING** until CI compilation, PDF verification, and independent artifact/content audit complete. No prior PDF is authoritative for this source revision.

The mathematical classifications remain unchanged: finite-window recognition PASS/CLOSED; fixed-scope selector threshold PASS/CLOSED; 1D cup-line carrier/minimality PASS/CLOSED in the declared linear selector-carrier category; stronger finite-pair functional OPEN/NOT LOAD-BEARING; novelty OPEN/CONDITIONAL.

## 2026-09-28 — THREE-PAPER PDF REVIEW AUDIT / VERSION-MAPPING CORRECTION

The externally supplied three-paper review was checked against the exact artifacts previously delivered in this session.

- Paper 1 artifact: affine factorization paper, run 36212215849, commit 73001ba0611e4f4aa7db8c733ee01d67542e16eb, 8 pages, SHA-256 09d67cbb88c647e4b7bb92bb91b2d46fe6b9b2c4b32959b7cebd7e468a554eda.
- Paper 2 artifact: finite-window Kummer recognition paper, run 36216012111, commit 0194e01176ae1c21fc70858be3797eeb1a3e7c18, 13 pages, SHA-256 af14b4b7ab971d8ed2d8cac84daae3ff6422ed389cec92b690cc3e184dde1aee.
- Paper 3 artifact: selector-minimality paper, run 36368630643, commit 2b4ccb849e93af840ca216b06c06c72a36c84dd8, 17 pages, SHA-256 00a4ee8deba65eb7c08a9b703d3c19b50801ffdde2c13cab0155186c247bb4e3.

Critical correction:
- The alleged Paper 2 page-3 grid of repeated 1 glyphs is NOT present in the exact delivered Paper 2 artifact. Independent text extraction and visual rendering of page 3 show a normal proof page. No rebuild is authorized from that objection alone.
- The supplied Paper 1 objections correspond to a different/older manuscript mapping; the delivered Paper 1 already uses p,f,k rather than an undefined q and contains the relation with the preceding recognition paper.
- The alleged Paper 3 x3 typo is absent: current source uses x_2^{3^e}.

## 2026-10-01 — EDITORIAL PDF ARTIFACT STATUS

The three-paper editorial final pass is complete on isolated final branches. The resulting CI-built PDFs are verified and ready as publication-candidate artifacts; mathematical status is unchanged. The branches are intentionally kept separate from the frozen main manuscript until the artifact set is promoted.

- Paper 1: `paper1-editorial-final-2026-10-01`, CI 36797031449, 8 pages.
- Paper 2: `paper2-editorial-final-2026-10-01`, CI 36796701931, 12 pages.
- Paper 3: `paper3-editorial-final-2026-10-01`, CI 36797451738, 14 pages.
- Editorial artifact status: **PASS / CLOSED**.
- Mathematical research status: **UNCHANGED**.
- Publication novelty: **OPEN / CONDITIONAL**.


## 2026-10-01 — ACTIVE NEXT-GENERALIZATION ROADMAP

The next research window starts from research/PAPER3_F1_CYCLOTOMIC_FINITE_WINDOW_GATE_2026-10-01.md after mandatory continuity restoration. The fixed conditional sequence is: (1) D versus F1 at (3,2,3); (2) F1 parameter-uniform extension if supported; (3) a genuinely different category such as deferred F2; (4) enlargement from T_cyc to a family of global properties; (5) category-relative finite-window recognition theory r_T(C;D_bullet). A failed intrinsic-carrier or separation attempt may terminate the branch or produce a no-go theorem and does not authorize escalation. Current F1 finite-window recognition is now **PASS / LOCAL** at the concrete pair, with exact two-object threshold **PASS / CLOSED**. The parameter-uniform extension remains **OPEN / LOAD-BEARING**; the general recognition theory is **OPEN / CONDITIONAL**.


## 2026-10-01 — F1 UNIFORM FINITE-q THRESHOLD

The pairwise obstruction theorem is now uniform in finite q=p^f:
\[
r_{T_{cyc}}(\{G_{F1}(q),G_{cyc}(q)\};D_\bullet)=q+1
\]
for odd p and d>=2. W_q isomorphism follows directly from Zassenhaus degree bookkeeping; W_{q+1} non-isomorphism follows from the intrinsic abelianization difference, using the nonzero restricted p^f-power class in the F1 associated graded Lie algebra.

Classification: **PASS / CLOSED** at the declared two-object category. Broad category-level recognition remains **OPEN / CONDITIONAL**.

Authoritative detail: research/PAPER3_W4_INTRINSIC_SEPARATION_AUDIT_2026-10-01.md


## 2026-10-01 — F2 SAME-W3 CYCLOTOMIC CONTROL GATE CLOSED

The F2 same-W3 control search is now closed at the authorized structural level. The audited rank-4/two-relator standard elementary-type cyclotomic constructions have Pfaffian type \(ab\) or \(0\), whereas the F2 quadratic relation pencil has repeated-root type \(a^2\). These types are not GL4-equivalent.

Status:
- F2 × standard elementary-type cyclotomic control: **FAIL / CLOSED**.
- F2 × arbitrary cyclotomic pro-p group: **OPEN / CONDITIONAL**; no universal no-go theorem is claimed.
- F2 \(W_4\) computation: **NOT AUTHORIZED**.
- F2 broader finite-window recognition: **OPEN / CONDITIONAL**.

This closes the standard construction mechanism rather than claiming that all cyclotomic groups are impossible controls. F1 is not reopened. Detailed record: research/PAPER3_F2_SAME_W3_CONTROL_GATE_2026-10-01.md

## 2026-10-01 — AUTHORITATIVE CORRECTION: F1 UNIFORM q=p^f THRESHOLD RECHECK

A post-closure critical review requested an explicit theorem-level audit of the two load-bearing steps in the uniform F1/cyclotomic-control result.

Both steps are now closed:

- Full W_q equality: both relators have the same image modulo D_q(F), and quotient functoriality gives D_q(F/R)=D_q(F)R/R. Hence the two W_q quotients are literally the same quotient F/(D_q(F),s), not merely associated-graded-equivalent.
- Uniform X_2^[p^f] nonvanishing: the Blumer–Quadrelli F1 restricted-Lie presentation admits a map X_2 to a free rank-one abelian restricted Lie algebra, proving X_2^[p^f] != 0 for every finite q=p^f.
- Independent group-level separation: the abelianizations of W_{q+1} are (Z/p^{f+1})^{2d} and (Z/p^{f+1})^{2d-1} direct-sum Z/p^f, so they have different orders.

Authoritative status after the recheck:
- W_q full equality: PASS / CLOSED.
- W_{q+1} intrinsic separation: PASS / CLOSED.
- Uniform pairwise threshold r=q+1: PASS / CLOSED for every odd p, finite q=p^f, d>=2, at the declared two-object category.
- Broad category-level recognition: OPEN / CONDITIONAL.
- Novelty/priority: OPEN / CONDITIONAL.

This correction supersedes any earlier entry in CURRENT_STATE that still labels the uniform extension OPEN/LOAD-BEARING. Detailed audit: research/PAPER3_W4_INTRINSIC_SEPARATION_AUDIT_2026-10-01.md.

## 2026-10-01 — GATE D FINITE-WINDOW RECOGNITION PRE-CHECK

The F2 branch remains operationally sealed. A mandatory Gate-D pre-check was completed before any new computation.

For the proposed fixed-scope chain
\\[
W_{10}\\to L(\\rho_2)\\to\\{\\delta_{3,\\rho_3}\\}\\to\\chi\\bmod27,
\\]
Object/Input/Functoriality/Gauge/Orientation-bridge/q-blindness pass at the audited p=3,k=3 scope. However, the same bare finite quotient + arbitrary-candidate Kummer selector mechanism is already assembled in the completed Paper 2 theorem for
\\(Q_k=G/P_{3^{k-1}+1}\\). Therefore merely repackaging W_10 as a carrier to chi mod 27 is not a new Paper 3 theorem.

The load-bearing Paper 3 question is the recognition layer: the carrier must yield a category-relative statement about
\\(r_T(\\mathcal C;D_\\bullet)\\), including a genuine same-window/different-target separation for lower bounds or a uniform same-window recognition theorem for upper bounds. The already proved F1/cyclotomic pairwise threshold q+1 is retained as a benchmark, not conflated with the Paper 2 selector theorem.

Classification:
- fixed W_10 selector chain: PASS / CLOSED (existing Gates A-C);
- literal delta-family \\cap Q_4^*: FAIL / CLOSED (type mismatch, superseded);
- W_10\\tochi mod27 as a new standalone Paper 3 theorem: FAIL / CLOSED on redundancy grounds;
- Gate D broader finite-window recognition: OPEN / LOAD-BEARING.

No W_11/W_12 or new Fox computation is authorized merely to extend the selector chain. Detailed pre-check: research/PAPER3_GATE_D_FINITE_WINDOW_RECOGNITION_PRECHECK_2026-10-01.md.

## 2026-10-01 — CRITICAL REVIEW OF GATE D STATUS

The prior Gate-D framing was refined after critical review. F2 remains PASS / CLOSED operationally, with candidate-completeness OPEN and no universal no-go claim.

Paper 3's immediate target is kept specific: finite-window recognition of the declared global target (canonical cyclotomic orientation / chi mod 3^k), not a general theory for arbitrary T. A broader category-level recognition theory is a later research program, not silently promoted into Paper 3.

Gate D status is now stratified rather than a bare OPEN label:
- Chain existence / finite calculation: PARTIALLY VERIFIED at the fixed audited scope.
- Intrinsic carrier: OPEN.
- Orientation bridge carrier -> chi mod 27: OPEN.
- Gauge/presentation independence: OPEN as a dedicated proof obligation.
- Functoriality: OPEN as a dedicated carrier-level obligation.
- Paper 2 redundancy boundary: CLOSED — merely restating W_10 -> chi mod 27 is not a new Paper 3 result.

The next action is a focused three-item pre-check/attack: (1) Object definition, (2) carrier-level functoriality/intrinsicity, (3) orientation bridge. The full nine-item checklist remains a guardrail, not a prerequisite bureaucracy. No large computation is authorized before these three pass or produce a decisive obstruction.

Stop rule: if the carrier is shown to depend essentially on presentation/orientation choices, close that carrier branch as FAIL / CLOSED rather than generalizing around the artifact. If the carrier survives but the bridge remains unresolved, classify OPEN. If a natural bridge is proved, classify PASS / LOCAL or PASS / CLOSED according to scope. A time-based two-week deadline is not adopted as a mathematical stop criterion; the branch stops on structural evidence, not elapsed time.


## 2026-10-01 — GATE D THREE-ATTACK INTRINSIC-CARRIER TRIAGE

After mandatory continuity restoration, the immediate Gate-D work was narrowed to three structural attacks before any new computation:
1. exact object legitimacy;
2. carrier intrinsicity/functoriality/gauge independence — designated as the first decisive battleground;
3. orientation bridge without inserting the known orientation.

The object attack passes for the audited W_10 -> L(rho_2) -> {delta_{3,rho_3}} chain. The full delta family is a genuine cohomological object, and Gate B's finite quotient construction is already PASS/CLOSED at the audited fixed scope.

The intrinsicity attack gives a split result. The proposed single-vector t_2 compression is decisively FAIL/CLOSED by the existing relator-conjugation witness t_2 -> t_2+p while the abstract group and full connecting family remain unchanged. The quotient/diagonal repairs are also closed. In contrast, the full connecting family rho_3 -> delta_{3,rho_3} survives as a natural cohomological family once rho_2 is fixed, and Gate B already reconstructs it from W_10 at the declared scope.

Thus the presentation/orientation-dependence attack does NOT kill the full delta family, but it does kill the tempting coordinate-level carrier. A genuinely new coarser carrier remains OPEN/LOAD-BEARING.

The orientation bridge exists at the audited fixed Demushkin scope via the zero-connecting-map selector, but that mechanism is already part of the completed Paper 2 theorem. Therefore using W_10 -> delta -> chi mod 27 alone is FAIL/CLOSED as a new Paper 3 theorem on redundancy grounds.

Decision: no W_11/W_12 or Fox computation is authorized. The next admissible research target is a genuinely non-redundant carrier extracted from the surviving family, subject again to the intrinsicity/gauge test. Paper 2 selector reproof is explicitly not authorized.

Detailed record: research/PAPER3_GATE_D_THREE_ATTACK_INTRINSIC_CARRIER_2026-10-01.md

## 2026-10-01 — O_k MINIMALITY BOUNDARY CLOSED; UNIVERSALITY IS THE ONLY LIVE O_k QUESTION

The post-Paper-3 attack has now been sharpened using the frozen carrier-compression result.

- Exact definition of \(\mathcal O_k\): **PASS / CLOSED**.
- Presentation/orientation independence: **PASS / CLOSED** at the finite-pair level; \(\mathcal O_k\) is constructed from the intrinsic central extension \(E_k\to Q_k\), cohomology, and transgression, with no presentation coordinate or orientation inserted.
- Functoriality: **PASS / CLOSED** for filtered finite-pair morphisms/isomorphisms, with the expected contravariant cohomological variance.
- Recognition minimality of \(\mathcal O_k\): **FAIL / CLOSED — REDUNDANT**. The frozen intrinsic cup-line \(C_k\subset H^2(Q_k,\mathbf F_p)\) is one-dimensional, finite-input, q-blind, intrinsic, and already carries all false-branch selector outputs. Hence \(\mathcal O_k\) is not the minimal recognition carrier in any category containing \(C_k\).
- Paper 2 selector redundancy: **CLOSED** as a recognition issue; no reproof is authorized.
- Finite-pair universal obstruction property of \(\mathcal O_k\): **OPEN / LOAD-BEARING**. This is a different claim from recognition minimality: the live question is whether every admissible functorial linear obstruction carrier for the transient/stable separation problem factors canonically through \(\mathcal O_k\).- Genuinely new carrier: **NOT OPENED**; only to be pursued if the universal-property attack fails or is shown irrelevant.

The proposed elapsed-time “2 weeks” stop rule is not adopted. Structural evidence controls closure. The branch closes immediately on the recognition-minimality question because a smaller frozen carrier already exists; only the distinct universal-obstruction question remains.

Next authorized action: explicitly define the finite-pair category and morphisms, define “separating obstruction carrier” and the factorization/universal property, then attempt the universal theorem or construct a counterexample. No W_11/W_12, Fox, 45-dimensional computation, or Paper 2 reproof is authorized.


## 2026-10-01 — MIXED FOX FACTORIZATION INTERPRETATION CORRECTED

The standard-family mixed Fox calculation remains valid but is explicitly classified only as **PASS / LOCAL** evidence. Parameter congruence q≡q' (mod 3^k) within the standard family is not the same statement as descent from the abstract finite pair W_k. The required global implication W_k(G)≅W_k(H) ⇒ M_k(G)≅M_k(H) remains **OPEN / LOAD-BEARING**. Likewise, “higher 3-adic information” is not by itself a category-level non-redundancy theorem; category-relative non-redundancy remains OPEN. No larger computation is authorized before the A/B descent-versus-counterexample gate is resolved. See research/PAPER3_MIXED_FACTORISATION_CRITICAL_REVIEW_2026-10-01.md.


## 2026-10-01 — MIXED FOX WEIGHTED MAGNUS GATE NARROWED

The apparent characteristic-zero/mod-3 incompatibility is no longer the main obstruction. Efrat's p-adic Magnus coefficient estimate implies that for N_k=3^{k-1}+1, D_{N_k} is invisible to the mixed (3,I)-adic coefficient jet through precision k, while the boundary term is represented by D_{N_k}/D_{N_k+1}. Thus the weighted coefficient descent is **PASS / CLOSED**, and naive deep-relator counterexamples are **FAIL / CLOSED**. The remaining load-bearing issue is specifically categorical projective relation-module descent W_k -> M_k. Even if that succeeds, a separate non-redundancy gate remains because the frozen selector already recognizes chi mod 3^k at the same window. No large computation is authorized. See research/PAPER3_MIXED_3I_ADIC_WEIGHTED_MAGNUS_DESCENT_2026-10-01.md.



## 2026-10-01 — MIXED FOX CATEGORICAL RELATION-MODULE DESCENT AUDIT

The weighted Magnus descent is confirmed as **PASS / CLOSED**: at N_k=3^{k-1}+1, the mixed (3,I)-adic coefficient jet through precision k is insensitive to D_{N_k}, and the first possible relation contribution is exactly the boundary layer D_{N_k}/D_{N_k+1}.

The remaining categorical issue was isolated more sharply. The natural finite input for the projective Fox relation-jet descent is the finite **extension window**
1 -> A_k -> E_k -> Q_k -> 1,
with E_k=G/D_{N_k+1}, Q_k=G/D_{N_k}, A_k=D_{N_k}/D_{N_k+1}, not merely the two abstract objects Q_k and A_k separately. The latter notation is under-specified because A_k is not a subgroup of Q_k and does not by itself encode the extension class.

Using the pro-3 Fox/Lyndon relation-module exact sequence together with the weighted boundary estimate gives the proof architecture: the finite quotient determines the lower mixed jet; the extension determines the finite relation-module class; the boundary layer supplies the weighted-order-k relation contribution; stable presentation changes disappear after projectivization. This is **PASS / LOCAL** as a proof architecture, not yet a formally written natural-transformation theorem.

Classification:
- weighted coefficient descent: **PASS / CLOSED**;
- stable/projective Fox mechanism: **PASS / LOCAL**;
- descent from the finite extension window to the projective mixed Fox jet: **PASS / LOCAL — formal naturality statement remains to be written and independently checked**;
- descent from the bare (Q_k,A_k) notation: **OPEN / NOT WELL-TYPED until the input category is explicitly defined**;
- whole Mixed Fox branch: **OPEN / LOAD-BEARING**.

Detailed audit: research/PAPER3_MIXED_RELATION_MODULE_DESCENT_AUDIT_2026-10-01.md.

Next authorized action: formalize the extension-window category and the natural transformation W_k -> M_k, then perform an independent covariance/naturality check. No larger Fox computation is authorized.

## 2026-10-01 — MIXED FOX EXTENSION-WINDOW CATEGORICAL AUDIT / INPUT-STRENGTHENING BOUNDARY

The categorical packaging was pushed one step further. The correct finite input for the projective mixed Fox construction is the central extension window
\[
1\to A_k\to E_k\to Q_k\to1,
\quad
E_k=G/D_{N_k+1},\quad
Q_k=G/D_{N_k},\quad
A_k=D_{N_k}/D_{N_k+1}.
\]

This fixes the previous type defect: \(A_k\) is not a subgroup of \(Q_k\), so the bare notation \((Q_k,A_k)\) does not encode the extension class.

However, a critical new boundary is now explicit. Passing from the original pair
\[
W_k=(Q_k,A_k)
\]
to the extension window
\[
\mathsf W_k^{ext}=(A_k\hookrightarrow E_k\twoheadrightarrow Q_k)
\]
adds genuine input unless a reconstruction/fiber-invariance theorem is proved. The forgetful map
\[
U:\mathbf{ExtWin}_k\to\mathbf{Pair}_k
\]
must therefore be treated as load-bearing.

The original finite-pair descent is equivalent to the factorization condition
\[
F_k=\overline F_k\circ U,
\]
where \(F_k\) is the extension-window mixed Fox construction. Equivalently, the mixed Fox jet must be constant, up to canonical projective equivalence, on every admissible fiber of \(U\).

Current classification:
- extension-window object: **PASS / CLOSED**;
- type correctness: **PASS / CLOSED**;
- extension-window → projective mixed Fox construction: **PASS / LOCAL** as the correct finite-input proof target; formal naturality still requires independent verification;
- extension-window as canonical enrichment of the original pair: **OPEN**;
- original pair → mixed Fox descent: **OPEN / LOAD-BEARING**;
- genuine finite-pair carrier: **OPEN**;
- novelty: **OPEN**.

No larger Fox computation is authorized. The next decisive attack is fiber invariance / extension reconstruction. If an admissible same-pair/different-extension pair yields different projective mixed Fox jets, the original finite-pair branch is **FAIL / CLOSED**. If fiber invariance or canonical reconstruction is proved, the extension-window theorem can descend to the original pair.

Detailed audit: `research/PAPER3_MIXED_EXTENSION_WINDOW_CATEGORICAL_AUDIT_2026-10-01.md`.


## 2026-10-01 — MIXED FOX FIBER-INVARIANCE ATTACK / CATEGORY BOUNDARY

The direct fiber attack has produced a structural boundary. The proposed descent F_k=\bar F_k∘U cannot hold on the broad category of arbitrary finite central extension windows: the same pair (Q,A) can support distinct extension classes, and the projective Fox relation data retains the power/commutator distinction. A concrete same-pair example is Q=C3×C3, A=C3, with C9×C3 versus the exponent-3 Heisenberg extension.

This closes only the **broad arbitrary-extension descent**:
- arbitrary extension-window → bare pair: **FAIL / CLOSED**;
- mixed Fox extension-window construction: **PASS / LOCAL**.

It does **not** yet close the intended Demuškin-restricted theorem. The missing prerequisite is an explicit admissible category of extension windows arising from the project's filtered Demuškin objects. The active gate is therefore:

**define admissible Demuškin ExtWin category → analyze fibers of U → determine whether extension class is reconstructible from (Q_k,A_k) or whether a same-pair Demuškin counterexample exists.**

Until that category is defined, “fiber invariance” is not a well-typed universal claim. No large Fox/W_11/W_12 computation is authorized. Paper 3 remains FROZEN / COMPLETE and is unaffected.

Detailed audit: research/PAPER3_MIXED_EXTENSION_WINDOW_FIBER_NO_GO_AUDIT_2026-10-01.md.


## 2026-10-02 — POST-PAPER-3 EXPLORATION EXTERNAL-VERIFICATION LEDGER

A referee-style verification ledger was added as:
`research/PAPER3_POST_EXPLORATION_EXTERNAL_VERIFICATION_LEDGER_2026-10-02.md`.

Purpose: replace status-only closure language with an externally checkable evidence chain. The ledger explicitly records the equations/counterexamples/literature controls behind the post-Paper-3 carrier exploration.

Key corrections and boundaries:
- O_k: the factorization O_k -> C is exactly the quotient/cokernel universal property and is therefore tautological as a new theorem; the proposed universal C -> O_k with uniqueness is explicitly false via C=O_k⊕O_k and the two projections. General existence C -> O_k remains unproved and is not claimed.
- Mixed Fox: explicit local identities are recorded, including D(grg^{-1})=chi(g)D(r), Fox/Lyndon relation-module differential, Nielsen/Jacobian covariance, relation-generator gauge, and preservation of m=(3,I). These establish the standard structural mechanism but not a project-specific finite-pair theorem by themselves.
- Broad extension descent: explicit same-(Q,A) examples C9×C3 and the exponent-3 Heisenberg extension show that arbitrary (Q,A) does not determine E.
- Demuškin restriction: the reconstruction is only within the standard odd-p fixed-rank family. The earlier q=N_k case is explicitly removed as impossible because q is p^s or 0 whereas N_k=p^{k-1}+1 is not a p-power. The genuine ranges are q<N_k and q>N_k (including q=0).
- Novelty boundary: Mixed Fox is closed only as a genuinely new recognition carrier under the project's non-redundancy criterion. It is not claimed to be mathematically false. A direct Fox-to-chi theorem beyond q-classification would be a separate result and was not established.

Publication discipline is also recorded: the open post-Paper-3 generalization search is independent of the frozen publication candidates and should not delay their submission.

Detailed ledger: `research/PAPER3_POST_EXPLORATION_EXTERNAL_VERIFICATION_LEDGER_2026-10-02.md`.

### 2026-10-02 correction: gauge obstruction withdrawn

A direct check against Blumer–Quadrelli–Weigel, Example 4.3 and Theorem 4.9 shows that in the standard convention for a special edge (v,w), the relation is w v w^{-1}=v^{1+q}, but the special/sinkhole vertex is w and the canonical orientation is theta(v)=1, theta(w)=1+q. The earlier audit had reversed these labels.

Therefore the automorphisms v->v^a, w->v^c w preserve the canonical orientation:
(theta o phi)(v)=1 and (theta o phi)(w)=1+q.
The previously claimed gauge/shear orientation no-go is superseded and is now FAIL/CLOSED as an argument.

This also removes the apparent conflict with the literature's uniqueness theorem: for specially oriented graphs the canonical orientation is the unique torsion-free orientation yielding the Kummerian property. The full-group gauge family is compatible because it fixes that orientation.

The remaining genuine issue is the filtered carrier: the q-dependent relator r=[w,v]v^{-q} has initial Zassenhaus degree 2, so H^2 / the ordinary degree-2 relation class does not directly encode the higher q-correction. The ordinary map Lambda^2 L_1 -> L_q remains type-invalid. The needed object is an intrinsic filtered relation-module/extension defect.

Current classification:
- q-defect first survival q+1: PASS/LOCAL;
- ordinary Lambda^2 L_1 -> L_q: FAIL/CLOSED — TYPE MISMATCH;
- P_q: PASS/CLOSED as a restricted-power map;
- H^2 as direct q-defect carrier: FAIL/CLOSED;
- filtered relation/extension defect: OPEN/LOAD-BEARING;
- intrinsic sinkhole recognition: OPEN/LOAD-BEARING;
- exact orientation recovery from bare W_n: OPEN;
- orientation no-go from phi_{a,c}: FAIL/CLOSED.

## 2026-10-02 — NON-ABELIAN (W_q): BILINEAR WALL REPLACED BY SPECIAL-PLANE INCIDENCE GATE

The previous statement that non-abelian (W_q) blocks the intrinsic extension approach is too strong. It blocks the global bilinear pairing (kappa_q:W_q	imes W_q	o A_q), but a finite-window 2-plane first-survival invariant remains available.

For each (2)-plane (Ule L_1=D_1/D_2), define (ho(U)) as the first Zassenhaus degree at which an independent pair spanning (U) has a nonzero commutator defect. Equivalently, define the intrinsic incidence family
[
mathscr S_n(G)={Uinoperatorname{Gr}(2,L_1):ho(U)=n}.
]
The construction is presentation/lift independent and (q)-blind.

The smallest genuinely non-abelian-origin special model
[
G=langle x,y,zmid xyx^{-1}=y^{1+q}, xzx^{-1}=z^{1+q}angle
]
is (Vtimeslangle xangle) with (V=langle y,zangle) free pro-(p). In this model:
- (2)-planes contained in (operatorname{span}{ar y,ar z}) have degree-2 commutator survival;
- (2)-planes (operatorname{span}{ar x,u}), (0
e uinoperatorname{span}{ar y,ar z}), have first survival degree (q);
- planes (operatorname{span}{ar x+v,u}) with (v,u) independent in the free-origin plane already have degree-2 survival.

Thus the (q)-special planes form the incidence family of the sinkhole line with its origin plane, and when the origin plane has dimension at least two their intersection recovers the sinkhole line intrinsically.

This is the first local mechanism that survives the non-abelian-origin test.

Classification:
- commuting-pair defect on (W_q): PASS / LOCAL as a partial domain, not a global bilinear pairing;
- special-plane first-survival invariant: PASS / LOCAL;
- noncommuting-origin special-line model: PASS / LOCAL;
- sinkhole recovery by incidence intersection when at least two independent special neighbors exist: PASS / LOCAL;
- general special-graph incidence formula: OPEN / LOAD-BEARING;
- exclusion of accidental (q)-special (2)-planes: OPEN / LOAD-BEARING;
- general directed/sinkhole separation: OPEN / LOAD-BEARING.

Detailed audit: research/PAPER3_RAAG_SPECIAL_PLANE_INCIDENCE_AUDIT_2026-10-02.md.

Immediate next gate:
**prove or refute the accidental-plane exclusion theorem**: every independent (2)-plane with first commutator survival at (q>2) must arise from a sinkhole direction together with its special-neighbor span. No large computation is authorized until this gate is resolved.

## 2026-10-02 — GATE D RESOLVED NEGATIVELY: SPECIAL-PLANE CARRIER REFUTED

The proposed accidental-plane exclusion theorem has been refuted by the smallest complete specially oriented graph with one sinkhole (s) and two ordinary vertices (a,b):
[
G=langle s,a,bmid asa^{-1}=s^{1+q},;bsb^{-1}=s^{1+q},;[a,b]=1angle.
]
This graph is within the standard specially oriented class; the literature explicitly allows a complete special graph with one special vertex joined by special edges to all other vertices. citeturn0search0

Because the underlying graph is complete, the degree-2 commutator sector vanishes. Thus (W_q) is abelian and the intrinsic extension commutator pairing is available. Its first degree-(q) defect on (L_1) is the alternating form
[
B_q(ar a,ar s)=ar s^q,quad B_q(ar b,ar s)=ar s^q,quad B_q(ar a,ar b)=0
]
(up to global sign), with radical (mathbf F_p(ar a-ar b)).

Hence the proposed special-plane family is
[
mathscr S_q={Uinoperatorname{Gr}(2,L_1):operatorname{rad}(B_q)
otsubset U}.
]
It does not recover the sinkhole. For instance
[
U_1=langlear s,ar aangle,qquad
U_2=langlear s+ar a,ar bangle
]
are both q-special but (U_1cap U_2=0). Therefore
[
igcap_{Uinmathscr S_q}U=0.
]

This is an intrinsic finite-window counterexample, not a presentation artifact.

Classification:
- special-plane first-survival carrier: **FAIL / CLOSED**;
- accidental q-special-plane exclusion: **FAIL / CLOSED**;
- sinkhole recovery by Grassmannian intersection: **FAIL / CLOSED**;
- conditional special-plane mechanism when origin sector has degree-2 noncommutativity: **PASS / LOCAL**;
- general directed/sinkhole separation via this carrier: **FAIL / CLOSED**;
- some other intrinsic finite-window carrier: **OPEN**.

This closes the current carrier branch. Do not continue computing (mathscr S_q); the next research question must be a genuinely different carrier or a broader no-go theorem.

## 2026-10-02 — RP-3 NON-REENCODING AUDIT / SMALLEST NON-COMPLETE + MULTIPLE-SINK CHECK

The q-blind adjacent-window carrier
\[
\mathcal L(X,Y)=
\begin{cases}
\operatorname{im}\bigl(\operatorname{Hom}(Y,\mathbf Z/p^{e(Y)})\to\operatorname{Hom}(Y,\mathbf F_p)\bigr),&e(Y)>e(X),\\
0,&e(Y)=e(X)
\end{cases}
\]
has now passed the admissible non-reencoding audit at the declared recognition scope.

The strong test is negative for q-reencoding: for fixed p, rank |V|, and sinkhole count |S|, the abstract carrier has dimension |V|-|S| (and annihilator dimension |S|), independent of q=p^f. Thus the carrier does not encode the q-value or the full orientation coefficient. Distinct q-regimes can have isomorphic carriers. The result should therefore be described as a kernel/annihilator recognition carrier, not as a full orientation carrier.

Independent model checks:
- smallest non-complete model \(\langle a,s,b\mid sas^{-1}=a^{1+q}\rangle\): PASS / LOCAL;
- multiple-sink sinkhole-sector recovery: PASS / LOCAL;
- all-sinkhole case: PASS / LOCAL;
- full categorical functoriality for arbitrary non-isomorphic pair morphisms: OPEN / NOT LOAD-BEARING;
- full \(\beta_f\) reconstruction: OPEN / NOT LOAD-BEARING;
- full orientation reconstruction from \(\mathcal L\) alone: FAIL / CLOSED;
- absolute minimality/coarseness: OPEN / NOT AUTHORIZED;
- directed incidence recovery: OPEN.

Important qualification: the carrier is exactly \(\ker\beta_f\) on the declared specially oriented RAAG family, so it is target-relative as a recognition device. The justified novelty claim is only that this target predicate has a q-blind intrinsic finite-window realization; no independent global invariant or absolute minimality claim is made.

Detailed audit: research/RP3_NONREENCODING_AUDIT_2026-10-02.md

Next authorized branch: if continuing RP-3, seek a genuinely graph-sensitive refinement of the abelianization carrier, starting again with Object/Input/Functoriality/Gauge/Orientation bridge/q-blindness/Separation/Novelty/Stop. No Massey calculation is load-bearing.


## 2026-10-02 — PAPER 4 EXACT-DEPTH CENTRALIZER-JUMP CARRIER

The ordinary-contamination gate was sharpened. A global quotient of the degree-2 sector is rejected as the primary abstraction. For u in L_1=D_1/D_2 define intrinsic filtration centralizers C_m(u)={x:[u~,x~] in D_m} and the exact-depth jump J_m(u)=C_m(u)/C_{m+1}(u). An ordinary edge has infinite commutator depth, a nonedge has degree 2, and a special edge has exact depth q; hence ordinary edges disappear from the q-jump without a presentation-dependent quotient.

Explicit checks: mixed ordinary/special model gives J_q(a)=F_p s and J_q(b)=0; RP-5 A gives J_q(a)=J_q(b)=F_p s; RP-5 B gives J_q(a)=F_p s and J_q(b)=F_p t; the complete one-sink model gives J_q(a)=J_q(b)=F_p s. Thus RP-5 separation survives in a stronger exact-depth form.

The remaining load-bearing issue is linear-combination cancellation. Quadrelli's 2024 analysis gives essential q-fold Massey obstructions for linear combinations such as u*+v*, so higher-q behaviour of non-basis directions is a genuine issue, not a technicality. citeturn14view0turn13view0

Classification: global W_2 ordinary quotient = **FAIL / CLOSED as primary abstraction**; exact-depth J_m = **PASS / LOCAL**; ordinary/special separation = **PASS / LOCAL**; RP-5 strengthened separation = **PASS / LOCAL**; q-blind local definition = **PASS / LOCAL**; linear-combination purity = **OPEN / LOAD-BEARING**; arbitrary incidence reconstruction = **OPEN**.

Detailed record: research/PAPER4_EXACT_DEPTH_CENTRALIZER_JUMP_AUDIT_2026-10-02.md.


## 2026-10-02 — PAPER 4 JOINT (P_q,B_q) GATE CLOSED AS A NOVEL ORIGIN CARRIER

The proposed joint restricted-power/extension-defect carrier was pursued through the complete 3-vertex, 2-generator, and non-abelian common-sink controls, followed by a structural reduction.

Define, with the span correction required by nonlinearity,
\[
C_q=\operatorname{Span}_{\mathbf F_p}\{u\in L_1:P_q(u)\in\Delta_q\},
\]
where \(\Delta_q\) is the intrinsic degree-q extension-defect image.

The local tests survive:
- complete one-sink model: \(C_q=\mathbf F_p\bar s\);
- 2-generator special-edge model: \(C_q=\mathbf F_p\bar v\);
- common-sink non-abelian-origin model: \(C_q=\operatorname{span}\{\bar y,\bar z\}\).

However, the structural role of \(P_q\) is now clear. Under the corrected literature convention, special edge \((v,w)\) has ordinary origin \(v\), special terminus \(w\), and \(wvw^{-1}=v^{1+q}\). Hence the origin sector is exactly the q-torsion sector in the abelianization. Since the degree-q extension defect lies in the commutator filtration, its image is invisible in abelianization; the condition \(P_q(u)\in\Delta_q\) therefore forces the q-th power of the abelianized \(u\) to vanish, hence \(u\) lies in the origin/torsion sector. Conversely every special-edge origin contributes its q-power to the degree-q defect. Thus the span-preimage is the same origin-sector recognition already supplied by the q-blind adjacent-window/Bockstein carrier, on the declared specially oriented RAAG class.

Therefore:
\[
\boxed{P_q\text{-part = redundant recognition/cross-check, not a new carrier.}}
\]

The extension-defect component remains genuinely graph-sensitive: RP-5 separates two same-abelianization four-vertex graphs by rank 1 versus rank 2 of the cross q-defect. Hence the only potentially new mathematical content is an **origin-conditioned filtered defect**: first recognize the origin sector by the existing intrinsic carrier, then extract the degree-q extension defect relative to that sector without assuming \(W_q\) is abelian and without using the failed Grassmannian support/intersection construction.

Classification:
- \((P_q,B_q)\) local origin recognition: PASS / LOCAL;
- \((P_q,B_q)\) as a novel independent origin carrier: **FAIL / CLOSED — REDUNDANT WITH RP-3**;
- RP-5 same-abelianization separation: PASS / LOCAL;
- origin-conditioned degree-q defect for arbitrary graphs: **OPEN / LOAD-BEARING**;
- arbitrary directed-incidence reconstruction: OPEN / LOAD-BEARING;
- full orientation reconstruction: OPEN.

Detailed audit: research/PAPER4_JOINT_POWER_EXTENSION_CARRIER_GATE_2026-10-02.md.

Decision: do not continue treating \((P_q,B_q)\) as one new invariant. The active Paper-4 problem is now sharply reduced to a canonical origin-conditioned filtered defect. If that object cannot be defined without a splitting/presentation choice, this branch should be closed as a carrier failure.


## 2026-10-02 — PAPER 4 ORIGIN-CONDITIONED DEFECT CANDIDATE: RAW PAIRING CLOSED, RESTRICTED EXTENSION OPEN

The proposed raw pairing
\[
B_q|_{O\times L_1}:O\times L_1\to A_q
\]
is not intrinsically defined on the general nonabelian class: changing a degree-one lift by \(D_2\) changes the commutator by a term in \([D_2,D_1]\subseteq D_3\), which is not generally contained in \(D_{q+1}\). Thus the pairing cannot be promoted from the commuting/abelian control models to a general theorem without extra structure.

The correct surviving object is the origin-conditioned restricted finite extension. For every adjacent window
\[
1\to A_n=D_n/D_{n+1}\to W_{n+1}\to W_n\to1,
\]
let \(O_n\subseteq L_1\) be the q-blind RP-3 origin carrier and \(H_n(O)=\pi^{-1}(O_n)\le W_n\). The canonical candidate is
\[
\mathfrak D_n(O):=[E_n|_{H_n(O)}],
\]
with its intrinsic extension-level commutator on the actual centralizer when defined. This removes the section/lift ambiguity at the level of the primary object.

Control results: RP-5 separation remains rank 1 versus rank 2; mixed ordinary/special control shows ordinary-edge defect is zero while the special-edge defect survives. These are PASS / LOCAL only.

Classification:
- raw \(B_q|_{O\times L_1}\): **FAIL / CLOSED — not intrinsically defined as written**;
- restricted origin extension \(E_n|_{H_n(O)}\): **PASS / LOCAL**;
- extension-level centralizer defect: **PASS / LOCAL**;
- canonical degree-one cross-defect extraction: **OPEN / LOAD-BEARING**;
- arbitrary directed-incidence reconstruction: **OPEN / LOAD-BEARING**;
- full orientation reconstruction: **OPEN**.

Next authorized attack: construct a canonical relative extension-class quotient using \(O_n\) and intrinsic degree-2 bracket data, then test it first on the mixed ordinary/special model and RP-5. If a section/basis/presentation is unavoidable, close this carrier branch. Detailed audit: research/PAPER4_ORIGIN_CONDITIONED_DEFECT_AUDIT_2026-10-02.md.
