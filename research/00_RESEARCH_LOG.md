## 2026-10-02 — PAPER 4 FILTERED q-PROFILE QUOTIENT / UNIQUENESS BOUNDARY

The dangerous-model attack was completed.

The long ordinary chain
\[
r_1-r_2-a\to s
\]
confirms the lower-filtration mechanism: for the origin \(a\), \([s,a]\) first survives at degree \(q\), while \([r_1,a]\) has a degree-2 obstruction. Hence \([s+r_1,a]\notin D_q\). The q-layer projection can hide this obstruction, but the full filtered profile rejects it.

However, the same model shows that the normalized filtered-profile locus need not affinely span the ambient \(U=L_1/O_q\): ordinary non-origin directions can remain in \(U\) while carrying canonical orientation value 0. Thus the ambient statement
\[
\operatorname{Aff}(\mathcal S_q)=\omega_q^{-1}(1)
\]
is **FAIL / CLOSED as stated**.

A stronger mixed test uses the disjoint union
\[
(a\to s)\sqcup\{z\}_{\rm ordinary}.
\]
Modulo the recovered origin sector, \(s\) has the normalized q-profile, while \(z\) is blocked by a lower-degree commutator. The profile therefore sees \(s\) but imposes no value on the \(z\)-coordinate. The family
\[
\omega_c(\alpha s+\beta z)=\alpha+c\beta
\]
agrees on the normalized profile for every \(c\in\mathbf F_p\), whereas the canonical orientation has \(c=0\). Hence the filtered q-profile alone does **not** determine \(\omega_q\) on all of \(U\).

This is not a return to carrier hunting. It proves that a genuine quotient \(U/N_q\) is necessary.

A second boundary is decisive: an isolated special vertex has no q-profile witness but canonical orientation value 1. Therefore a naive \(N_q\) defined from profile-invisibility cannot satisfy \(N_q\subseteq\ker\omega_q\) on the unrestricted specially oriented class. The earlier Gate-D obstruction remains controlling there.

The surviving local lemma is structural: in a specially oriented graph, once lower-degree contamination is absent, any adjacent special vertex is a special terminus, ordinary neighbors contribute no q-defect, and non-neighbors produce lower-degree obstruction. Thus the normalized q-defect equals the visible special coefficient sum.

Current classification:
- lower-filtration + q-defect mechanism: **PASS / LOCAL**;
- ambient affine-hyperplane uniqueness: **FAIL / CLOSED**;
- unrestricted quotient uniqueness: **FAIL / CLOSED**;
- restricted quotient theorem on a class with no isolated special vertices: **OPEN / LOAD-BEARING**;
- Paper 4: **OPEN**.

The next authorized task is singular: define \(N_q\) non-tautologically from the *relations among lower-filtration obstructions* and test it on the long chain, mixed ordinary/special component, separated two-sink, and chordal-tree controls. It is explicitly forbidden to define \(N_q\) as the span of all q-invisible directions, because the separated two-sink vector \(s+t\) is q-invisible under full flatness but has \(\omega_q(s+t)=2\ne0\).

Detailed audit: research/PAPER4_FILTERED_PROFILE_QUOTIENT_UNIQUENESS_AUDIT_2026-10-02.md.

## 2026-10-02 — PAPER 4 CRITICAL CORRECTION + NONABELIAN FILTERED PROFILE GATE

The previous whole-package kernel-shear no-go overclaimed: P_E is a genuine restricted-power map and cannot be treated as pointwise fixed under an arbitrary shear. The whole-linear-package closure is therefore HISTORICAL/SUPERSEDED.

What remains closed:
- omega_q does not descend through ker Phi in the chordal-tree model;
- ker Phi alone is not an orientation carrier.

A convention correction is also recorded: absence of an edge in an oriented pro-p RAAG does not mean commutation. Ordinary edges give commutation; special edges give wuw^{-1}=u^{1+q}. Thus the separated-model accidental-direction explanation must use lower-filtration contamination, not “t commutes with a”.

The authorized next object is the full filtered commutator profile:
[u,x] in D_q, followed by [u,x] = c_x(u)P_E(x) mod D_{q+1}.
For specially oriented RAAGs, lower-degree vanishing forces support visibility from x, and the normalized q-defect measures the visible special coefficient sum.

Classification:
- kernel-only: FAIL / CLOSED;
- previous whole-linear-package shear closure: HISTORICAL / SUPERSEDED;
- lower-filtration + q-defect profile: OPEN / LOAD-BEARING;
- Paper 4: OPEN.

Detailed audit: research/PAPER4_NONABELIAN_FILTERED_PROFILE_GATE_2026-10-02.md.

## 2026-10-02 — PAPER 4 PAIRING/KERNEL SHEAR NO-GO: LINEAR PACKAGE CLOSED

The \\(\\ker\\Phi) analysis strengthens to a no-go for the entire linear package \\(\\mathcal D=(U,O,A,P_E,\\Phi)\\).

In the chordal-tree model,
\\[
\\Phi(s)=P_a,\\quad \\Phi(t)=P_b,\\quad \\Phi(u)=P_a+P_b,
\\]
so
\\[
k=u-s-t\\in\\ker\\Phi,\\qquad \\omega_q(k)=-1\\ne0.
\\]

Define the invisible shear
\\[
g_c(s)=s,\\quad g_c(t)=t,\\quad g_c(u)=u+c,k.
\\]
For \\(c=1)\\), this is an automorphism of \\(U)\\), and since \\(\\Phi(k)=0)\\),
\\[
\\Phi\\circ g_c=\\Phi.
\\]
It acts trivially on the origin sector and on the intrinsic q-power target \\(P_E)\\). Hence the whole package \\(\\mathcal D)\\) is fixed, while
\\[
\\omega_q(g_1(u))=0\\ne1=\\omega_q(u).
\\]

Therefore no natural/intrinsic construction from \\(U,O,A,P_E,\\Phi)\\) alone can equal \\(\\omega_q)\\). The kernel is precisely an invisible shear direction carrying nonzero orientation mass.

Classification:
- linear pairing/kernel package as an orientation carrier: **FAIL / CLOSED**;
- \\(\\ker\\Phi)\\) as diagnostic/no-go data: **PASS / LOCAL**;
- full finite-window orientation problem: **OPEN**.

Detailed audit: research/PAPER4_PAIRING_KERNEL_SHEAR_NO_GO_AUDIT_2026-10-02.md.

Next boundary: only a genuinely non-linear/nonabelian extension datum can break this shear symmetry. No new linear functional on the same package is authorized.

## 2026-10-02 — PAPER 4 \\(\\ker\\Phi) ORIENTATION TEST: KERNEL-RESCUE BRANCH CLOSED

The proposed \\(\\ker\\Phi) rescue was tested on the smallest models.

In the already audited chordal tree with ordinary a,b and special s,t,u,
\\[
\\Phi(s)=P_a,\\quad \\Phi(t)=P_b,\\quad \\Phi(u)=P_a+P_b,
\\]
so
\\[
\\ker\\Phi=\\mathbf F_p(u-s-t).
\\]
But
\\[
\\omega_q(u-s-t)=1-1-1=-1\\ne0
\\]
for odd p. Hence \\(\\omega_q) does not descend to \\(U/\\ker\\Phi) and is not in \\(\\operatorname{im}\\Phi^*=\\ker(\\Phi)^\\perp).

The complementary separated two-sink model
\\[
G=\\langle a,b,s,t\\mid sas^{-1}=a^{1+q},\\ tbt^{-1}=b^{1+q}\\rangle
\\]
has
\\[
\\Phi(s)=P_a,\\quad \\Phi(t)=P_b,
\\]
so \\(\\ker\\Phi=0) while \\(\\omega_q(\\alpha s+\\beta t)=\\alpha+\\beta) remains nontrivial. This model also satisfies the natural Gate-D repair candidate “every special vertex is the terminus of a special edge.”

Therefore the kernel is not an orientation carrier: it records incidence dependencies, not a canonical orientation normalization. The stronger factorization route through \\(U/\\ker\\Phi)\\) or \\(\\operatorname{im}\\Phi^*)\\) is structurally closed.

Classification:
- \\(\\ker\\Phi) intrinsic diagnostic: **PASS / LOCAL**;
- nonzero \\(\\omega_q) on kernel in the tree model: **PASS / LOCAL**;
- orientation recovery from \\(\\ker\\Phi) alone: **FAIL / CLOSED**;
- orientation descent through \\(U/\\ker\\Phi): **FAIL / CLOSED**;
- Paper 4 overall: **OPEN**.

Detailed audit: research/PAPER4_KER_PHI_ORIENTATION_AUDIT_2026-10-02.md.

Immediate next boundary: do not search for another functional on the same kernel. Any continuation must introduce a materially richer intrinsic datum and rerun the full pre-check.

## 2026-10-02 — PAPER 4 CREATIVE RE-EXAMINATION: GLOBAL PAIRING / TRACE / AFFINE-HULL CLOSURES

The global pairing proposal was tested as a structural alternative after Gate D.

Retain Φ(u)=B_q(u,-) as diagnostic data. However:
- rank-one atoms: FAIL/CLOSED as a universal orientation-normalization mechanism;
- trace/total-mass functional on Im Φ: FAIL/CLOSED;
- naive affine-hull normalization: FAIL/CLOSED;
- three-window: OPEN/LOCAL only;
- projective-only orientation target: FAIL/CLOSED for exact χ mod p^k.

Decisive chordal tree: ordinary a,b; special s,t,u; special edges a→s, b→t, a→u, b→u. At first q-defect:
Φ(s)=P_a, Φ(t)=P_b, Φ(u)=P_a+P_b.
Thus τ(Φ(s))=τ(Φ(t))=τ(Φ(u))=1 would imply 1=2, impossible for odd p.

For x=αs+βt+γu, simultaneous normalized equations are α+γ=1 and β+γ=1, giving an affine line in F_p^3, codimension 2. Thus the natural affine-hull claim is false for this signature.

This is independent of the isolated-special Gate D obstruction. Gate D remains FAIL/CLOSED for the unrestricted class; this new result is a second structural boundary for restricted-class continuation.

Detailed audit: research/PAPER4_CREATIVE_REVIEW_PHI_TRACE_THREEWINDOW_PROJECTIVE_2026-10-02.md.

## 2026-10-02 — PAPER 4 GATE D DECISIVE NO-GO

Gate D was tested exactly as required: before any new observable, search for two admissible oriented objects with the same un-oriented finite window but different orientation targets.

A decisive counterexample exists inside the current specially oriented pro-p RAAG class.

Choose a nontrivial specially oriented graph Γ0 with a visible special-edge q-layer and an isolated vertex z. Define ΓA=Γ0⊔{z}_ordinary and ΓB=Γ0⊔{z}_special. The literature permits isolated special vertices and explicitly distinguishes the ordinary/special designation even when the geometric graph is identical. Both graphs are specially oriented. Since z is isolated, its status contributes no relation, so GΓA,λ=GΓB,λ as un-oriented pro-p groups. Hence all Zassenhaus quotients, and in particular the entire adjacent pair W_q←W_{q+1}, are identical.

The canonical orientation differs: θA(z)=1 and θB(z)=λ(1)=1+q. For q=p^{k-1}, 1+q is not congruent to 1 modulo p^k. Therefore the same finite window supports two different orientation targets.

This closes Gate D at the current admissible class. It also proves a stronger statement than failure of any particular carrier: orientation is not a function of the un-oriented filtered group itself on this class, so no finite-window-only carrier can repair the problem.

Literature control: Blumer–Quadrelli–Weigel, definition of oriented pro-ℓ RAAGs, Remark 2.4 (isolated vertex may be declared ordinary or special), Definition 2.5 (special graph condition), and canonical orientation definition. Independent web verification was performed on 2026-10-02.

The recent T1 affine-hull failure remains valid but is now secondary. The current program must stop carrier search on this class.

Boundary:
- current specially oriented RAAG class: FAIL / CLOSED for Gate D;
- class excluding isolated special vertices: OPEN;
- enriching the finite input by an explicit orientation marking: OPEN;
- positive finite-window theorem on a restricted orientation-rigid class: OPEN.

Detailed audit: research/PAPER4_GATE_D_SAME_WINDOW_DIFFERENT_ORIENTATION_AUDIT_2026-10-02.md.

Next authorized action: do not design another carrier. First define the restricted admissible class/input for any attempted positive continuation, then run the full pre-check from Object through Stop.

## 2026-10-02 — PAPER 4 T1 AFFINE-HULL GATE REFUTED / T1 CURRENT REALIZATION CLOSED

The proposed final gate Aff(S_E)=omega_q^{-1}(1) fails for the current existential local-uniform signature.

Separated two-sink graph: G=<a,b,s,t | sas^{-1}=a^(1+q), tbt^{-1}=b^(1+q)>. Modulo the origin sector O=span(a,b), U=span(s,t). Although omega_q(s)=omega_q(t)=1, u=s+t is accepted by the current signature because t commutes with a, so (st)a(st)^(-1)=a^(1+q) and B_q(u,a)=P_E(a). Hence u is in S_E but omega_q(u)=2 != 1 for odd p. Since s,t are also in S_E, Aff(S_E)=U and has codimension 0.

This is stronger than the overlapping example, where (s+t)/2 happened to remain on omega_q=1. The separated model is a structural counterexample: local 2-generator recognition cannot constrain sink components invisible to the chosen origin.

Classification: affine containment S_E subseteq omega_q^{-1}(1) = FAIL / CLOSED; codimension-one affine hull = FAIL / CLOSED; current T1 local-uniform realization = FAIL / CLOSED; intrinsic q-power target = PASS / LOCAL; Paper 4 overall = OPEN.

No larger scan is authorized for this T1 branch. Any revival requires a materially different observable and a fresh pre-check.

Detailed audit: research/PAPER4_T1_AFFINE_HULL_GATE_AUDIT_2026-10-02.md

## 2026-10-02 — PAPER 4 T1 OVERLAPPING MULTI-SINK RESULT / TARGET REFINEMENT

The smallest overlapping multi-sink model was tested:
\[
G=\langle a,s,t\mid sas^{-1}=a^{1+q},\;tat^{-1}=a^{1+q}\rangle.
\]
For \(u=\alpha\bar s+\beta\bar t\),
\[
B_q(u,\bar a)=(\alpha+\beta)\overline{a^q}.
\]
For odd \(p\), choosing \(m\in\mathbf F_p^\times\) with \(2m=1\) gives
\[
z=(st)^m,\qquad \bar z=m(\bar s+\bar t),
\]
with
\[
zaz^{-1}\equiv a^{1+q}\pmod{D_{q+1}},
\]
hence
\[
B_q(\bar z,\bar a)=P_E(\bar a).
\]
Thus a non-vertex direction can satisfy the full normalized rank-one special-edge signature.

This closes only the literal vertex-set formulation:
\[
S_q=\{\bar w:\ w\text{ is a special/sink vertex}\}
\]
is **FAIL / CLOSED**.

A critical correction is recorded: an accidental normalized direction is not automatically a counterexample to T1, because T1 seeks the linear functional \(\omega_q\), not the literal set of graph vertices. In the overlapping model the accidental direction lies on the same normalized affine hyperplane
\[
\alpha+\beta=1=\omega_q(\alpha\bar s+\beta\bar t).
\]
Therefore the correct target is the affine hull of all intrinsically normalized signature directions:
\[
\operatorname{Aff}(\mathcal S_E)\stackrel{?}{=}\omega_q^{-1}(1).
\]
This remains OPEN / LOAD-BEARING and is now the precise next theorem.

The top-down reset remains active: no new carrier search. The problem has narrowed from “find the right sink vectors” to “prove the normalized signature locus is an intrinsic affine hyperplane whose level-one functional is \(\omega_q\)”.
## 2026-10-02 — PAPER 4 T1: INTRINSIC q-POWER TARGET CLOSED LOCALLY

The recommended attack “define the intrinsic q-power target from the adjacent finite window” was executed.

For an adjacent finite extension
\[
1\to A\to Y\xrightarrow{\pi}X\to1
\]
at the target window \(X=W_q,\;Y=W_{q+1}\), define
\[
e(X)=\exp(X),\qquad L(X)=X/\Phi(X),\qquad A=\ker\pi,
\]
and
\[
P_E(\bar x)=\tilde x^{\,e(X)}.
\]
At the specially oriented RAAG jump, \(e(W_q)=q\). The kernel \(A=D_q/D_{q+1}\) is central and elementary abelian, so the value is independent of the lift in \(Y\). Independence of the degree-one representative is exactly the iterated Zassenhaus restricted \(p\)-operation \(D_1/D_2\to D_q/D_{q+1}\), hence \(P_E\) is intrinsic to the adjacent window. No basis, generator, presentation, orientation, or displayed \(q\) is used.

Independent literature verification: the Zassenhaus graded quotients \(D_n/D_{n+1}\) carry the restricted Lie structure and \(p\)-operation induced by group powers. This is stated in standard treatments of Jennings–Lazard theory and in the cited sources. citeturn6search12turn6search14

Local consistency:
- 2-generator special edge: \(P_E(\bar v)=\overline{v^q}=B_q(\bar w,\bar v)\);
- common-sink: \(P_E(\bar v_i)=\overline{v_i^q}=B_q(\bar w,\bar v_i)\).

Therefore the scale condition is now intrinsic:
\[
B_q(\lambda\bar w,\bar v)=P_E(\bar v)\ne0\Rightarrow\lambda=1.
\]

Classification:
- intrinsic q-power target: **PASS / LOCAL**;
- q-blind adjacent-window definition: **PASS / LOCAL**;
- scale fixing relative to target: **PASS / LOCAL**;
- T1: **OPEN / LOAD-BEARING**.

Important limitation: \(P_E\) is not asserted to be linear on arbitrary \(L_1\); it is the iterated restricted-power map. The remaining decisive problem is no longer target construction. It is recognition of the normalized sink set \(S_q\), beginning with the smallest overlapping multi-sink configuration, plus filtered-isomorphism naturality.

Consequence for methodology: this confirms the top-down reset. No new carrier search is authorized.

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

The latest complete-3-vertex counterexample closes the current arbitrary-linear-direction purity formulation for \(J_q(u)\): a non-origin linear direction can be q-active. This is not evidence that Paper 4 has returned to an unconstrained carrier search; it is evidence that the present bottom-up incidence target is too strong.

The earlier top-down transition remains controlling. T−1 (intrinsic canonical orientation target) and T0 (finite-window identifiability at the standard Demuškin scope) remain closed. Paper 4 must therefore return to target-first design: first specify the exact orientation-relevant information that a finite window must determine, then derive the weakest non-tautological intrinsic observable capable of carrying that information. Full directed-incidence reconstruction is not a prerequisite unless the target-first analysis proves it necessary.

Accordingly, the recent sequence \(J_q\) → joint \((P_q,B_q)\) → restricted origin extension is classified as local carrier exploration, not as a new mandate to continue generating carriers indefinitely. The restricted origin extension remains OPEN/LOAD-BEARING only as a possible realization after the target-first pre-check; it is not authorized to expand into another open-ended carrier hunt.

Immediate methodological decision:
1. freeze the failed \(J_q\) purity theorem;
2. do not pursue arbitrary-incidence reconstruction as the default target;
3. reconstruct the top-down target decomposition: orientation target → necessary finite observable → non-reencoding/coarseness requirement → candidate realization;
4. only then test whether the existing RP-3 origin carrier plus a relative extension datum is actually required.

Classification: **TOP-DOWN RESET = ACTIVE; bottom-up carrier search = NOT AUTHORIZED until target-first necessity is established.**

## 2026-10-02 — PAPER 4 ARBITRARY-LINEAR-DIRECTION J_q PURITY REFUTED

The exact-depth centralizer jump survives ordinary-edge removal but fails as a pure one-direction incidence detector for arbitrary linear directions.

In the complete three-vertex specially oriented graph
\[
G=\langle s,a,b\mid[a,b]=1,\;sas^{-1}=a^{1+q},\;sbs^{-1}=b^{1+q}\rangle,
\]
the degree-q defect is
\[
B_q(\bar a,\bar s)=\overline{a^q},\quad
B_q(\bar b,\bar s)=\overline{b^q},\quad
B_q(\bar a,\bar b)=0.
\]
For
\(u=\alpha\bar a+\beta\bar b+\gamma\bar s\),
\[
B_q(u,x)
=(\alpha\gamma'-\gamma\alpha')\overline{a^q}
 +(\beta\gamma'-\gamma\beta')\overline{b^q}.
\]
The form has zero radical. Since every degree-one commutator in the complete graph already lies in \(D_q\), \(C_q(u)=L_1\) and \(C_{q+1}(u)=\ker B_q(u,-)\). Hence \(J_q(u)\neq0\) for every nonzero \(u\in L_1\).

In particular \(u=\bar s+\bar a\notin O=\operatorname{span}(\bar a,\bar b)\) but \(B_q(u,\bar a)=\pm\overline{a^q}\neq0\), so \(J_q(u)\neq0\) although \(u\) is not an origin direction. Even \(\bar s\) is q-active.

Therefore the load-bearing purity claim \(J_q(u)\neq0\iff u\) is a genuine origin direction is **FAIL / CLOSED**. This is structural, not an accidental cancellation.

The exact-depth mechanism remains valid for ordinary-edge removal and the previously established RP-5 pairwise separation. The next object must retain target-labelled/pairwise information and an independent anchor such as the restricted-power map \(P_q\), rather than the scalar predicate \(J_q(u)\neq0\).

Detailed audit: research/PAPER4_ARBITRARY_LINEAR_DIRECTION_JQ_AUDIT_2026-10-02.md.

Next authorized action: audit a combined intrinsic carrier such as \((P_q,B_q)\), with fresh Object/Input/Functoriality/Gauge/Orientation-bridge/q-blindness/Separation/Novelty/Stop checks. Do not reopen the false one-direction purity theorem.

## 2026-10-02 — RP-3 Q-BLIND CARRIER REFINEMENT: ADJACENT EXPONENT JUMP

A uniform q-blind carrier was constructed from an adjacent finite Zassenhaus window. For (X=W_n) and (Y=W_{n+1}), let (e(Z)=log_pexp(Z^{ab})), and define the lift subspace by
[
mathcal L(X,Y)=
operatorname{im}igl(operatorname{Hom}(Y,mathbf Z/p^{e(Y)})	ooperatorname{Hom}(Y,mathbf F_p)igr)
]
when (e(Y)>e(X)), and (0) otherwise.

At (n=q=p^f) for a specially oriented RAAG,
[
W_q^{ab}cong(mathbf Z/q)^V,qquad
W_{q+1}^{ab}cong(mathbf Z/pq)^{Vsetminus S}oplus(mathbf Z/q)^S.
]
Reduction from (mathbf Z/pq) therefore produces exactly the degree-one characters vanishing on the sinkhole torsion sector. If there is no free/non-sinkhole sector, the exponent does not jump and the carrier is zero, again matching (kereta_f).

Hence
[
mathcal L(W_q,W_{q+1})=kereta_f,
qquad
mathcal L(W_q,W_{q+1})^perp
=(kereta_f)^perp
=operatorname{span}{ar s:sin S}subset L_1.
]

This resolves the earlier q-blindness gap at PASS/LOCAL level and makes Massey interference non-load-bearing for the stated kernel-recognition target. Full (H^2)-class reconstruction is still not claimed.

Detailed audit: research/RP3_FINITE_WINDOW_BOCKSTEIN_AUDIT_2026-10-02.md

Classification:
- q-blind adjacent-window carrier: PASS / LOCAL;
- RP-3 target: PASS / LOCAL;
- non-reencoding/minimality: OPEN;
- non-special graph extension: OPEN.

Next authorized action: independent model verification and then the admissible-category/non-reencoding audit.

## 2026-10-02 — RP-3 BOCKSTEIN AUDIT: LOCAL KERNEL RESULT, FINITE-WINDOW FACTORIZATION STILL OPEN

The submitted RP-3 development was critically reviewed against the authoritative state and the higher-Bockstein literature.

The following survives: for a specially oriented pro-p RAAG with sinkhole set S and q=p^f, the minimal presentation gives
[
G^{ab}cong mathbf Z_p^{Vsetminus S}oplus(mathbf Z/p^f)^S.
]
The higher Bockstein (eta_f) detects the obstruction to lifting a mod-p character to (mathbf Z/p^{f+1}). Hence
[
kereta_f
=
{chi:chi	ext{ lifts to }mathbf Z/p^{f+1}},
]
and this kernel is the annihilator of the sinkhole torsion sector. This is a valid local result.

A typing error in the submitted (C_f) formula was corrected: since (H^1=L_1^*), its annihilator lies in (L_1), so
[
(kereta_f)^perp=operatorname{span}{ar s:sin S}subseteq L_1.
]
Writing (ar s^*) there is not intrinsic.

The decisive correction concerns Step 5. The finite pair ((W_q,W_{q+1})) does not automatically determine the global class (eta_f(chi)in H^2(G,mathbf F_p)). The legitimate finite-window statement is only the liftability predicate: every homomorphism (G	omathbf Z/p^{f+1}) kills (D_{q+1}) in the cyclic target and therefore factors through (W_{q+1}). Thus the kernel can potentially be recognized from the adjacent window, but the required construction is not yet q-blind because the coefficient target (mathbf Z/p^{f+1}) explicitly uses f.

Massey products are not currently a blocker for the kernel-recognition problem; they matter only if the actual (H^2)-class or richer higher structure is to be reconstructed.

Classification:
- local Bockstein kernel/liftability: PASS / LOCAL;
- finite-window full-(eta_f) factorization: OPEN / NOT PROVED;
- q-blind uniform carrier: OPEN / LOAD-BEARING;
- RP-3 overall: OPEN / LOAD-BEARING.

Detailed audit: research/RP3_FINITE_WINDOW_BOCKSTEIN_AUDIT_2026-10-02.md
Next authorized action: define a uniform q-blind adjacent-window liftability object for arbitrary n and test its specialization at n=p^f. No Massey computation is authorized before this structural gate is resolved.

## 2026-10-02 — CRITICAL AUDIT OF RESTRICTED-POWER REFINEMENT: LOCAL LEMMA VALID, GENERAL CARRIER NOT YET LEGITIMATE

Critical review identifies a genuine strengthening and several load-bearing gaps.

1. The complete 3-vertex counterexample correctly closes the first-survival Grassmannian carrier, after correcting (U_1\cap U_2=0) to (U_1\cap U_2=\mathbf F_p(\bar s+\bar a)). The full intersection is still zero using (U_3=\operatorname{span}(\bar s,\bar b)).

2. The local claim
[
P_q^{-1}(\operatorname{im}B_q)=\mathbf F_p\bar s
]
is mathematically plausible and consistent with the complete-graph restricted structure, but the previous record overstated its proof status. Independence of (\bar s^{[q]},\bar a^{[q]},\bar b^{[q]}) must be established from the associated restricted Lie algebra/group model, not asserted.

3. More importantly, (P_q) is not generally a linear map on a nonabelian degree-one restricted Lie algebra. In the complete graph (L_1) is abelian, so the local preimage is well behaved; this does not transfer automatically to non-complete graphs.

4. The finite-window input must also be stated precisely. (P_q:L_1\to L_q=D_q/D_{q+1}) and the defect image in (L_q) require the window through (D_{q+1}), not merely (W_q=G/D_q). Thus any q-blind carrier must discover the first level q and then use the next quotient, or be defined as a family over all finite levels. The earlier wording "finite-window" was too loose.

5. The orientation bridge is still absent. Recovering a distinguished line (\mathbf F_p\bar s) in one model does not yet produce source/sink incidence, nor a natural coefficient functional (\chi\).

Classification:
- Grassmannian carrier: FAIL / CLOSED.
- Accidental-plane exclusion: FAIL / CLOSED.
- Complete 3-vertex restricted-power preimage: PASS / LOCAL (subject to an explicit independence lemma).
- General (P_q^{-1}(\operatorname{im}\delta_q)) carrier: OPEN.
- Intrinsic/functorial restricted-power construction: OPEN / LOAD-BEARING.
- Orientation reconstruction: OPEN.
- Categorical no-go: OPEN / NOT ESTABLISHED.

Authorized next action: first prove the complete-graph restricted-power independence lemma and define the exact finite-window input; only then test the candidate on the 2-generator and 3-vertex common-sink models. Do not claim a general carrier or orientation recovery before these gates pass.

## 2026-10-02 — SPECIAL-PLANE COUNTEREXAMPLE CORRECTED; RESTRICTED-POWER REFINEMENT REOPENS A LOCAL CARRIER GATE

The complete specially oriented 3-vertex graph refutes the first-survival Grassmannian carrier. The earlier audit contained a concrete linear-algebra error: for
[
U_1=\operatorname{span}(\bar s,\bar a),qquad
U_2=\operatorname{span}(\bar s+\bar a,\bar b),
]
one has (U_1\cap U_2=\mathbf F_p(\bar s+\bar a)), not zero. The full intersection is nevertheless zero after adding (U_3=\operatorname{span}(\bar s,\bar b)).

A finer local invariant survives. The degree-(q) extension defect has image
[
\operatorname{im}B_q=\mathbf F_p\overline{s^q},
]
and the restricted q-power operation satisfies
[
P_q^{-1}(\operatorname{im}B_q)=\mathbf F_p\bar s
]
in this complete 3-vertex model.

Classification:
- special-plane Grassmannian: **FAIL / CLOSED**;
- accidental-plane exclusion: **FAIL / CLOSED**;
- corrected full-intersection computation: **PASS / LOCAL**;
- restricted-power refinement: **PASS / LOCAL**;
- general intrinsic restricted-power carrier: **OPEN / LOAD-BEARING**;
- categorical no-go for all intrinsic finite-window carriers: **OPEN / NOT ESTABLISHED**.

Next authorized action: test (P_q^{-1}(\operatorname{im}\kappa_q)) on the already audited 2-generator and 3-vertex common-sink models, then audit intrinsicity, q-blindness, gauge invariance, and separation. No categorical no-go is authorized yet.


## 2026-10-02 — 2-GENERATOR SPECIAL-EDGE RAAG AUDIT: TYPE MISMATCH + GAUGE BOUNDARY

A critical audit of the 2-generator special-edge model G=<v,w | wvw^{-1}=v^{1+q}, q=p^f found a genuine first-survival boundary but rejected the stronger intrinsic role-recognition proof as written.

Robust:
- [w,v]=v^q lies in D_q, so the q-dependent deformation is invisible for n<=q;
- v^q first survives in G/D_{q+1}, giving PASS/LOCAL first-survival evidence and preserving the candidate threshold q+1.

Decisive correction: with L_i=D_i/D_{i+1}, the restricted-Lie bracket has target L_{i+j}. Thus [vbar,wbar] is in L_2, not L_q. For q>2 the relation makes the degree-2 bracket class zero, while the same element has a later class in L_q. Hence the proposed canonical map Lambda^2 L_1 -> L_q and the identity P_q^{-1}(Delta_q)=F_p vbar are not established. The missing object is a filtered relation-module/extension-class defect.

Independent gauge stress test: phi_{a,c}(v)=v^a, phi_{a,c}(w)=v^c w preserves the defining relation and the characteristic Zassenhaus filtration, while changing the displayed character by (theta phi)(v)=(1+q)^a and (theta phi)(w)=(1+q)^c. This is a serious bare-window orientation obstruction. Before promoting it to a theorem-level no-go, the exact scope of the literature's orientation-uniqueness statement must be reconciled with this automorphism family.

Classification:
- deg_Z(v^q)=q: PASS/CLOSED.
- q-dependent defect invisible for n<=q: PASS/LOCAL.
- first survival at n=q+1: PASS/LOCAL.
- Lambda^2 L_1 -> L_q as ordinary graded map: FAIL/CLOSED — TYPE MISMATCH.
- intrinsic sinkhole-line recognition at q+1: OPEN/LOAD-BEARING; previous PASS/LOCAL claim superseded.
- gauge automorphism family: PASS/LOCAL.
- exact bare-window orientation recovery: STRONG NO-GO CANDIDATE; literature-scope check required.

Detailed audit: research/PAPER3_RAAG_2GEN_SPECIAL_EDGE_AUDIT_2026-10-02.md

Immediate next action: construct the intrinsic filtered relation-module/extension-class defect at degree q and resolve its automorphism/gauge behavior; simultaneously settle the precise scope of the RAAG orientation-uniqueness theorem. No larger RAAG computation is authorized before this gate is resolved.

## 2026-10-02 — ADJACENT CLASS SELECTED: SPECIAL ORIENTED PRO-p RAAG

A literature-first adjacent-class search was completed. Free pro-p fails orientation rigidity at the object level, while locally-uniform/θ-abelian groups have canonical orientations but remain too close to a one-parameter p-power/q model. The stronger candidate is the class of **special oriented right-angled Artin pro-p groups**.

Literature establishes that for a special digraph Γ and p-power q, the oriented pro-p RAAG has a canonical orientation
\\[
\\theta_\\Gamma(v)=1+q\\text{ on sinkholes},\\qquad 1\\text{ otherwise},
\\]
and that this is the unique orientation satisfying the Kummerian lifting property. Special/elementary-type digraphs are also characterized through 1-cyclotomicity and related Galois-theoretic properties. citeturn3search0turn5search0

This class is materially richer than the Demuškin q-family because the finite defining digraph contributes independent combinatorial data. The finite-window problem naturally splits into:
1. degree-two graph recovery;
2. degree-q deformation recovery for special directed edges;
3. canonical orientation reconstruction from the sinkhole support and q.

For a relation \\([w,u]=u^q\\), the commutator term has Zassenhaus degree 2 while the q-power term has degree q. Thus the same candidate threshold \\(N_k=p^{k-1}+1\\) is structurally plausible: if q=p^s<p^k then q<N_k, while q>=p^k gives trivial orientation mod p^k. But this is only a mechanism, not yet a theorem.

Critical load-bearing gate:
**intrinsic directed/sinkhole separation from the abstract finite window.**
The proof must not choose the original digraph or relator basis. If the argument requires such a choice, classify FAIL/CLOSED — presentation-level re-encoding. If it descends to an intrinsic relation-module/extension-class object, the branch remains OPEN toward a genuine finite-window orientation theorem.

Classification:
- special oriented pro-p RAAG orientation rigidity: PASS/LOCAL;
- non-q structural richness: PASS/LOCAL;
- candidate threshold N_k: CONDITIONAL;
- full finite-window orientation identifiability: OPEN;
- intrinsic directed/sinkhole separation: OPEN / LOAD-BEARING.

Detailed gate: research/PAPER3_ORIENTATION_RIGID_ADJACENT_RAAG_GATE_2026-10-02.md.

## 2026-10-02 — ADMISSIBLE CATEGORY / ADJACENT-CLASS AUDIT

The proposed A–D admissible-category plan was critically checked. It is not yet a category-level minimality theorem: a functor \\(F:\\mathrm{Dem}\\to\\mathrm{Fin}\\) can still encode target data, condition C is only a family-level nonconstancy condition, and quotient closure does not by itself produce a coarsest object. The correct abstraction is an explicitly specified factorization preorder on non-reencoding admissible realizations. Classical minimal sufficiency supports this factorization viewpoint only by analogy; it depends on a statistical model and is not directly transferable. citeturn2search0turn2search8

Two technical corrections were recorded. First, \\(\\bigoplus_{n\\le N_k}\\mathrm{gr}_n(G)\\) is the associated graded Zassenhaus object, not an abelianization; degree labels and any retained restricted-Lie operations must be part of the carrier if they are used to detect the defect degree. Second, the earlier vector-space cardinality statement \\(p^{\\dim V}\\ge k\\) is not valid for a bare vector space considered up to isomorphism; the invariant lower bound is \\(|\\mathrm{Iso}(C_k)|\\ge k\\). A dimension bound requires marked/distinguished data or an underlying-state observation convention.

The proposed cohomological carrier using a “\\chi-twisted part” is target-circular and therefore fails the target-blind/q-blind carrier test.

An adjacent-class stress test was then completed. Published literature states that every orientation on a free pro-p group yields a 1-cyclotomic oriented pro-p group, while an infinite Demuškin group has a unique 1-cyclotomic orientation. citeturn1search0turn1search8 Hence, after enlarging the underlying class to free pro-p groups while retaining the un-oriented finite window as input, orientation is not a single-valued invariant of the underlying object. This gives an object-level no-go, stronger than a finite-window counterexample.

Classification:
- A–D complete admissible category: FAIL/CLOSED.
- minimal-sufficiency transfer: PASS/LOCAL as factorization analogy only.
- X_ab as terminology: FAIL/CLOSED.
- X_ab as genuinely new same-family carrier: FAIL/CLOSED — q re-encoding.
- chi-twisted cohomological carrier: FAIL/CLOSED — circular.
- free-pro-p un-oriented orientation identifiability: FAIL/CLOSED.
- orientation-rigidity prerequisite: PASS/LOCAL.

Detailed audit: research/PAPER3_ADMISSIBLE_CATEGORY_AND_ADJACENT_CLASS_AUDIT_2026-10-02.md

Next authorized action: identify an adjacent class with canonical/unique orientation but without Demuškin q-classification, then test finite-window identifiability. No large computation is authorized before the structural gates pass.

## 2026-10-02 — FULL-ORIENTATION COARSE REALIZATION AUDIT

After T−1/T0 closure, the target was strengthened from recognition to the full finite-level canonical orientation [χ_G mod p^k]. The target values in the standard odd-p fixed-rank Demuškin family are exactly 1, (1-p)^(-1), …, (1-p^(k-1))^(-1) mod p^k, with the stable value 1 covering q=0 and q≥p^k. Distinctness follows because equality of two inverse values implies equality of the corresponding p-powers modulo p^k. Therefore the target has exactly k values.

This gives a carrier-independent lower bound: any full-orientation carrier determined by W_k must have at least k isomorphism classes; an F_p-linear carrier has dimension at least ceil(log_p k). Consequently the previously frozen 1D cup-line selector is not a full orientation carrier for k≥p+1 (in particular k≥4 for p=3); its theorem remains a recognition/selection result.

The audited q-reconstruction suggests an exact k-class intrinsic defect-index carrier: the first q-dependent Zassenhaus relation defect degree p^s for s<k, with one stable class for q=0 or q≥p^k. It reaches the information bound and recovers χ_k by the canonical formula. But it is a re-encoding of the already-classified invariant q, not a new carrier theorem at the present scope.

Classification:
- target cardinality: PASS/CLOSED;
- carrier lower bound: PASS/CLOSED;
- exact defect-index realization: PASS/LOCAL;
- full-orientation factorization: PASS/LOCAL;
- novelty of same-family coarsest carrier: FAIL/CLOSED — classification re-encoding.

Detailed audit: research/PAPER3_TOP_DOWN_FULL_ORIENTATION_COARSE_REALIZATION_AUDIT_2026-10-02.md.

Next authorized action: move to an adjacent admissible class or a genuinely different global target. Same-family q-compressions are no longer authorized unless they yield a structural consequence beyond classification.
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

## 2026-10-01 — POST-PAPER-3 CARRIER NON-REDUNDANCY AUDIT

## 2026-10-01 — MIXED (3,I)-ADIC FINITE BRIDGE ATTACK

The mixed candidate survived the standard-family finite-level attack. Using the projective Fox row for r_q=x_1^q[x_1,x_2][x_3,x_4], the mixed maximal-ideal truncation at m^{k+1}, m=(3,A-1,B-1,C-1,D-1), retains exactly the finite precision needed for chi mod 3^k on the standard family. The equations force A=C=D=1 and the remaining equation gives B=(1-q)^(-1) to the required precision. This is a direct Fox-equation bridge, not the forbidden q-classification-repackaging route.

Status: completed projective intrinsicity PASS/LOCAL; finite mixed carrier PASS/LOCAL on the standard Demushkin family; direct orientation bridge PASS/LOCAL on that family; non-redundancy against the closed C_k selector PASS/LOCAL. The global finite-pair descent theorem remains OPEN/LOAD-BEARING. The next decisive dichotomy is: prove that the finite mixed scheme modulo m^{k+1} is a functor of the project's abstract finite-pair input, or construct two admissible same-pair inputs with different mixed finite schemes and close the branch.

Detailed audit: research/PAPER3_MIXED_3I_ADIC_FINITE_BRIDGE_AUDIT_2026-10-01.md.

## 2026-10-01 — GENUINELY NEW CARRIER BRANCH / MIXED (3,I)-ADIC GATE

The O_k universal-property branch is closed and will not be revisited. The remaining branch is a genuinely new finite filtered carrier satisfying finite filtered input → intrinsic carrier → chi.

The mixed (3,I)-adic Fox candidate is the first authorized target. Its completed/projective construction survives the definition-level attacks: relator conjugation acts by a unit, relation-generator gauge acts projectively, Nielsen changes act by invertible Fox Jacobian plus coordinate substitution, and the maximal ideal m=(3,U_1,...,U_d) is preserved. Therefore completed/projective intrinsicity is **PASS / LOCAL**.

However, this is not yet a finite-pair theorem. The natural mixed finite object A_F/m^n is characteristic-zero filtered data, whereas the project finite pair W_k is built from the mod-3 Zassenhaus filtration. Standard literature identifies Zassenhaus with powers of the augmentation ideal in F_3[[G]], not with the mixed (3,I)-adic filtration over Z_3[[G]]. Thus factorization W_k → mixed finite carrier is a separate, load-bearing theorem and remains **OPEN**.

Orientation bridge to chi mod 3^k is also **OPEN / LOAD-BEARING**. It must be direct and natural, not merely mixed carrier → q-class → known Demushkin orientation formula. Non-redundancy against the closed one-dimensional C_k selector is **OPEN**.

Decision: mixed candidate remains **OPEN**, but no numerical scan is authorized. The next and only authorized attack is finite-pair factorization: prove W_k determines the relevant mixed finite carrier, or construct an admissible same-W_k/different-mixed-data counterexample and close the branch.

Hard stop: if intrinsicity of a genuinely new finite carrier cannot be established within two weeks of this branch opening, close the branch. For the mixed candidate, completed/projective intrinsicity has passed locally; the two-week boundary concerns finite-level intrinsicity/factorization rather than further refinement of the exact Fox scheme.

Detailed audit: research/PAPER3_MIXED_3I_ADIC_CARRIER_GATE_AUDIT_2026-10-01.md.

## 2026-10-01 — O_k FINITE-PAIR UNIVERSAL OBSTRUCTION PROPERTY AUDIT

The proposed load-bearing attack on the finite transgression carrier is now resolved at the categorical level.

For the fixed pair E_k→Q_k, with O_k=H^2(Q_k,F_p)/im(tra_k), a linear obstruction carrier defined by a natural map from H^2(Q_k,F_p) that annihilates the transgression sector automatically receives a unique map from O_k. This is exactly the cokernel universal property, so it is PASS / CLOSED but TAUTOLOGICAL / NOT LOAD-BEARING.

The opposite proposed direction, in which every independent admissible separating carrier C canonically factors C→O_k, is not implied by D2 or by finite-pair functoriality. Moreover, if uniqueness is included, the claim is decisively false: the admissible direct-sum carrier C=O_k⊕O_k with diagonal obstruction map has at least two natural projections C→O_k.

Therefore:
- O_k as finite intrinsic obstruction carrier: PASS / CLOSED.
- O_k→C universality among quotient-type obstruction carriers: PASS / CLOSED, TAUTOLOGICAL.
- Universal C→O_k existence for a genuinely broader carrier category: OPEN / NOT PROVED.
- Universal C→O_k uniqueness: FAIL / CLOSED.
- Absolute O_k minimality: FAIL / CLOSED as ill-posed.

The existing one-dimensional cup-line C_k remains the already-established sufficient recognition carrier; it is not promoted as a new result by this audit. The O_k universal-property branch is therefore exhausted. The next authorized branch must be a genuinely independent finite-pair carrier, subject first to object/intrinsicity/functoriality/gauge/orientation-bridge/q-blindness/non-redundancy checks. No large computation is authorized before those checks.

Detailed audit: research/PAPER3_OK_FINITE_PAIR_UNIVERSAL_OBSTRUCTION_AUDIT_2026-10-01.md.

The first post-Paper-3 carrier battleground was pushed to a structural stopping boundary.

The full delta-family survives intrinsicity, but its zero predicate is exactly the already completed Kummer selector. The finite cup-line is a genuine intrinsic compression at the audited scope, but it has the same recognition predicate and is therefore redundant as a new theorem. The single-vector t_2 remains closed by the explicit presentation-gauge witness.

The transgression quotient O_k remains useful as a finite proof carrier because it removes the finite transgression ambiguity; it is not itself the orientation invariant. Its universal/minimal finite-pair property is still open.

Classification:
- Paper 3 본체: **FROZEN / COMPLETE**.
- Paper 2 selector: **FROZEN / COMPLETE; no reproof**.
- t_2: **FAIL / CLOSED**.
- full delta-family as new recognition: **FAIL / CLOSED — REDUNDANT**.
- cup-line as new recognition: **FAIL / CLOSED — REDUNDANT**; mathematically **PASS / LOCAL** as compression.
- O_k: **PASS / LOCAL** as proof carrier; universal/minimal carrier **OPEN**.
- genuinely new non-redundant carrier: **OPEN**.

No deeper computation is authorized merely to re-establish the frozen selector. Detailed record: research/POST_PAPER3_CARRIER_NONREDUNDANCY_AUDIT_2026-10-01.md.

## 2026-10-01 — TRACK CORRECTION: PAPER 3 본체 고정 / 후속 일반화 연구 분리

현재 작업을 “Paper 3 핵심 주장의 재검증”이라고 부르는 것은 부정확하다.

정확한 구분:
1. **Paper 3 본체 = 완성·고정.**
2. **현재 연구 = Paper 3에서 제시한 후속 일반화/연구 프로그램을 별도 branch로 공격.**
3. (t_2), full (delta)-family, intrinsic carrier, Gate D는 Paper 3 본체의 필수 증명 단계가 아니다.
4. 이 후속 branch가 FAIL/CLOSED가 되어도 Paper 3 본체의 정리·증명·완성본은 영향을 받지 않는다.
5. Paper 2 selector는 완료된 선행 결과이며 재증명하지 않는다.

현재 연구의 정확한 질문은
[
	ext{finite-window}	o	ext{intrinsic carrier}	o	ext{global orientation}
]
이라는 **Paper 3 이후 일반화 프로그램이 실제로 살아남는가**이다.

앞으로는 “Paper 3를 다시 증명한다” 또는 “Paper 3의 핵심 주장을 다시 검증한다”는 표현을 사용하지 않는다. 정확한 표현은 “Paper 3 이후 후속 일반화 연구에서 carrier의 생존 여부를 검증한다”이다.

현재 후속 연구의 첫 실제 승부처는 carrier intrinsicity/functoriality/gauge independence이고, 다음이 orientation bridge의 비중복성이다. 구조적 실패 시 해당 branch만 닫는다.


## 2026-10-01 — F2 STANDARD ELEMENTARY-TYPE SAME-W3 CONTROL SEARCH CLOSED

The authorized construction-level search is complete. Within the standard elementary-type cyclotomic class generated by free pro-p groups, Demushkin groups, free products, and cyclotomic semidirect products, no rank-4 two-relator control has the F2 repeated-root Pfaffian type.

At rank 4 with two quadratic relators, the relevant construction shapes reduce to either disjoint rank-2 one-relator factors (Pfaffian ~ab) or a semidirect-action pair sharing a direction (Pfaffian identically 0). F2 has Pfaffian ~a^2. Therefore no W3 isomorphism is possible in this class.

Classification:
- standard elementary-type F2 same-W3 control: **FAIL / CLOSED**;
- arbitrary cyclotomic pro-p control: **OPEN / CONDITIONAL**;
- finite W4 computation: **NOT AUTHORIZED**;
- broad F2 finite-window recognition: **OPEN / CONDITIONAL**.

This is a genuine structural boundary: the F2 repeated-root W3 type is not supplied by the standard elementary-type cyclotomic construction mechanisms. No claim is made that every conceivable cyclotomic pro-p group is excluded.

## 2026-10-01 — F2 SAME-W3 CYCLOTOMIC CONTROL PRE-CHECK / LITERATURE AUDIT

The required pre-check was completed before any new computation. The search was restricted to genuinely cyclotomic constructions capable in principle of producing a rank-4, two-dimensional quadratic relation space of the F2 repeated-root Pfaffian type.

Primary literature checked:
- Quadrelli–Weigel, *Profinite Groups with a Cyclotomic p-Orientation* (arXiv:1811.02250 / Doc. Math. 25 (2020)): cyclotomicity is preserved under free products and specified fibre/semidirect constructions; the elementary-type framework is generated from free pro-p groups and Demushkin groups by free products and cyclotomic semidirect/fibre-product operations.
- Mináč–Pasini–Quadrelli–Tân, *Koszul algebras and quadratic duals in Galois cohomology* (arXiv:1808.01695 / Adv. Math. 380 (2021)): cyclotomic semidirect products are part of the elementary-type construction, and the quadratic dual is tied to the p-Zassenhaus relation data.
- Blumer–Quadrelli, arXiv:2603.15464v2: the F2 family has the two-dimensional quadratic relation space used in this gate and is globally non-1-cyclotomic.

Pre-check conclusion:
1. A meaningful cyclotomic control class definitely exists; the search target is mathematically legitimate.
2. No explicit rank-4 cyclotomic example with W3 quadratic relation pencil GL4-equivalent to the F2 repeated-root type was found in the targeted literature search.
3. The standard elementary-type free-product control remains FAIL/CLOSED by the Pfaffian test.
4. Cyclotomic semidirect/fibre-product operations are genuine candidates, but the standard constructions inspected do not immediately furnish a rank-4, two-relation F2-type quadratic shadow. This is a warning, not a no-go theorem.
5. No large computation is authorized. The next legitimate step is a construction-level symbolic search among the smallest cyclotomic fibre/semidirect constructions and rank-preserving combinations, testing the W3 relation pencil before any finite-group enumeration.

Classification:
- meaningful cyclotomic control class: **PASS / CLOSED**;
- actual F2-matching W3 control: **OPEN / DECISIVE**;
- free-product control: **FAIL / CLOSED**;
- broad F2 finite-window recognition: **OPEN / CONDITIONAL**.

Important boundary: this negative literature pre-check is not a proof that no cyclotomic control exists.

## 2026-10-01 — F1 CYCLOTOMIC FINITE-WINDOW GENERALIZATION OPENED

The next research branch deliberately leaves the torsion-free Demushkin category. Rather than treating F1 Massey sharpness as the endpoint, F1 is adopted as an adversarial near-Demushkin test-bed for the finite-window recognition program.

Primary target:
\[
T_{\mathrm{cyc}}(G)=1 \iff G\text{ admits a 1-cyclotomic/Kummerian orientation}.
\]

The first category is the paired Demushkin/F1 family at fixed odd p, even rank d, and finite admissible q. The finite input is the intrinsic Zassenhaus window W_n(G); q, presentation data, and a preselected orientation are excluded from the target definition.

The decisive question is whether a finite window can distinguish the 1-cyclotomic Demushkin member from the non-1-cyclotomic F1 variation, and if so whether the first separating datum has an intrinsic Kummerian obstruction interpretation.

Pre-check status:
- Object: PASS.
- Input: PASS.
- Functoriality: PASS.
- Gauge: OPEN / must be proved for the eventual obstruction carrier.
- Orientation bridge: OPEN / LOAD-BEARING.
- q-blindness: PASS at definition level.
- Separation: OPEN / DECISIVE.
- Novelty: targeted 2026 audit found no exact finite-Zassenhaus 1-cyclotomic recognition theorem for this D/F1 pair.
- Stop: no large computation authorized yet.

Targeted literature update:
- Blumer–Quadrelli establish F1 as non-1-cyclotomic and give the parameter-dependent sufficient strong-Massey bound n<=q.
- Palaisti (arXiv:2609.00253, 2026-08-31) concerns F2, not F1, and does not resolve F1 sharpness.
- A fresh web audit found no exact F1 converse/sharpness or finite-window 1-cyclotomic recognition result. This is PASS / LOCAL, not an absolute priority claim.

Smallest authorized stress test:
(p,d,q)=(3,2,3), Demushkin versus F1. First determine the relation depth/window at which they can differ and whether the difference yields an intrinsic finite Kummerian obstruction.

Detailed stage document:
research/PAPER3_F1_CYCLOTOMIC_FINITE_WINDOW_GATE_2026-10-01.md

Classification:
F1 finite-window 1-cyclotomic recognition: OPEN / DECISIVE.


## 2026-09-28 — THREE-PAPER EXACT ARTIFACT + LITERATURE GATE CLOSED

The three-paper revision checklist was completed through independent source→CI→PDF verification.

Paper 1:
- A source-binding defect was discovered during audit: the generic paper-build workflow on the Paper 1 branch compiled paper/main.tex, which is the Paper 2 manuscript, while the Paper 1 source is paper/successor_main.tex.
- The resulting successful run was therefore explicitly rejected as Paper 1 evidence.
- A dedicated source-correct workflow, .github/workflows/paper1-build.yml, was added on paper1-fixes-2026-09-28.
- Authoritative source blob: 1855e9a992a98caf0a0f6deae484f13e049d0a20.
- Source-correct CI: run 36401507321, all steps PASS.
- Full artifact: 10960891547; 8 pages.
- PDF SHA-256: 4efec62888f3803935717658f9f638902ff2ef2bd8845c83a32dc6770542e5ef.
- Independent PDF text audit confirmed the sharp affine theorem, all-f/d lower-bound witness, category-relative minimality, factorization-vs-recognition boundary, and the newly added Mináč–Tân–Trà literature boundary.
- Visual inspection of representative pages passed.
- Classification: PASS / CLOSED.

Paper 2:
- The first clean validation branch contained a non-mathematical validation-marker edit to paper/main.tex, so its artifact was not accepted as exact-source evidence.
- The authoritative source from paper2-fixes-clean-2026-09-28 was restored byte-for-byte on paper2-ci-clean-2026-09-28.
- Exact-source CI run 36401141711: all steps PASS.
- Authoritative source blob: 7411d241505b8a0a496f46cee05bbecc8d40eb47.
- Full artifact: 10959918919; 13 pages.
- PDF SHA-256: 1381f75048bf0f83d9174c6a2b8bb85b31e62010f945697413182c9f5be94c64.
- Independent audit confirmed U4 labeling, U5c finite-coefficient PD² duality, the 1412.7685 literature identification, and the final theorem text. U5c was checked internally: finite-coefficient duality identifies the dual of the socle inclusion with A_{k-1} -> F_3, a surjection, so the H² map is injective.
- Visual inspection of representative pages passed.
- Classification: PASS / CLOSED.

Paper 3:
- Revision branch paper3-fixes-2026-09-28 compiled successfully under the existing build and citation-hygiene workflows.
- Authoritative source blob: aa351f77c07a748588208d0d383f0c4dbd6dfca7.
- CI run 36395985678: Build paper PDF and citation hygiene PASS.
- Full artifact: 10957609279; 17 pages.
- PDF SHA-256: 2be2e84e06eb77eb9e6e4c9bbfb522bb037db5675bb04c7a9a0c6bac34a9787e.
- Independent audit confirmed §8 typed cup-line chain, D4 exact selector depth, literature-audit scope, and explicit non-claims. Visual inspection of representative pages passed.
- Classification: PASS / CLOSED.

Literature verification:
- arXiv:1412.7685 verified as Claudio Quadrelli, Cohomology of absolute Galois groups; its scope includes cyclotomic orientations and Zassenhaus/restricted-Lie/cohomological material.
- arXiv:2510.20133 verified as J. Mináč, N. D. Tân, N. T. Trà, Zassenhaus filtrations as intersections. Its stated scope is a representation-theoretic description of Zassenhaus terms as intersections of kernels; Paper 1 now cites it only as surrounding methodology, not as prior identity with the exact affine sharpness theorem.
- Labute Theorem 4 and Proposition 6 orientation attribution were cross-checked against later literature reproducing those exact references; the q≠2 normal form and canonical orientation criterion are consistent with the manuscript.
- NSW Theorem 3.9.15 / Chapter III PD²-Demuškin relationship was cross-checked through secondary sources. MathSciNet/zbMATH Open were not searched and are not claimed as searched.

Final three-paper publication-artifact classification:
- Paper 1: PASS / CLOSED
- Paper 2: PASS / CLOSED
- Paper 3: PASS / CLOSED
- Publication novelty: OPEN / CONDITIONAL
- No absolute priority claim.

## 2026-09-28 — THREE-PAPER AUTHORITATIVE REVISION CHECKLIST EXECUTION

The supplied revision checklist was treated as the authoritative edit list for Paper 1/2/3. No direct edits were made to the previously frozen main-branch artifacts.

Paper 1:
- Revision branch: `paper1-fixes-2026-09-28`.
- The all-(f) lower-bound witness was consolidated into one proposition, and the category-relative minimality/free-product statements were repaired.
- Literature-boundary wording was kept conditional; Mináč–Tân–Trà arXiv:2510.20133 was added as surrounding Zassenhaus literature.
- CI compile: PASS (PDF produced, 8 pages).
- Repository verify step: FAIL only because the workflow's warning-grep rejects unresolved citation warnings in the LaTeX log; no LaTeX compilation error occurred. Therefore Paper 1 artifact gate is OPEN/PENDING citation-hygiene cleanup and re-verification.

Paper 2:
- Revision branch: `paper2-fixes-clean-2026-09-28`.
- U4 was explicitly labeled as the base-level identification proposition.
- U5c was rewritten with the finite-coefficient (PD^2) duality direction and the dual reduction map (A_{k-1}	woheadrightarrowmathbf F_3).
- arXiv:1412.7685 was identified explicitly in the literature boundary/bibliography.
- Clean CI validation branch: `paper2-ci-clean-2026-09-28`, run **36398580257**: PASS.
- No PDF/artifact closure is claimed yet beyond successful clean compilation; exact-source/PDF/hash gate remains pending.

Paper 3:
- Revision branch: `paper3-fixes-2026-09-28`.
- U5c and literature-audit wording were updated within the supplied checklist scope.
- CI runs on the revision branch completed successfully; exact final artifact closure still requires the independent PDF/content/hash gate.

Important process note:
- Several early Paper 2 patch attempts were deliberately discarded after CI exposed malformed section boundaries. The clean Paper 2 branch was rebuilt from the authoritative base commit rather than repairing a corrupted intermediate.
- No failed intermediate branch is authoritative.
- Current classification: Paper 1 OPEN/PENDING citation-hygiene verification; Paper 2 PASS/LOCAL (clean compilation, artifact gate pending); Paper 3 PASS/LOCAL (CI compile/build success, exact artifact gate pending).
- Publication novelty remains OPEN/CONDITIONAL.

## 2026-09-28 — PAPER 3 REFEREE DETAIL REPAIR / ARTIFACT GATE REOPENED

A new adversarial manuscript review raised M1–M10. The source was checked against the authoritative research state and primary literature before editing.

Result:
- M1 D3 relation-module image chain: PASS/CLOSED after explicit R_k -> P_2/P_3 chain.
- M2 D4 shallow range: PASS/CLOSED; existing valuation chain is correct.
- M3 D4 middle range: PASS/CLOSED after explicit x_2^N in G^N subseteq P_N subseteq P_m chain.
- M4 D2 transgression: PASS/CLOSED after explicit P_{N_k+1} subseteq P_2=Phi(G), hence K_k subseteq Phi(E_k).
- M5 C_k typing: PASS/CLOSED; finite cup image and coefficient-extension target are explicitly separated.
- M6 Labute Theorem 4: PASS/CLOSED; primary-source check confirms the existence/uniqueness plus Proposition-6 crossed-homomorphism criterion attribution.
- M7 alleged U3 d inconsistency: FAIL/CLOSED as an objection; r in Phi(F) implies H/Phi(H) ~= F/Phi(F), so rank(F)=dim H^1(H,F_3)=d.
- M8 Fox coefficients: PASS/CLOSED after adding a cochain-level derivation appendix.
- M9 G^{3^e}: PASS/CLOSED after defining the power subgroup and stating G^{3^e} subseteq P_{3^e}.
- M10 Appendix A formatting: PASS/CLOSED.

Source repair commit: f686fef1bfbab0b566d2cd424aa097955a2c61ec.
Detailed audit: research/PAPER3_REFEREE_DETAIL_REPAIR_2026-09-28.md.

Artifact gate is explicitly reopened because the source changed. The next authorized sequence is exact-source CI -> independent PDF/content audit -> checksum/package verification -> final manifest update. No prior PDF is authoritative after this source change.

## 2026-09-28 — MANUSCRIPT SOURCE CLEANUP CORRECTION

The first cleanup commit accidentally introduced repeated-character typos while replacing the reviewer-noted “ogether” typo. This was caught immediately by source inspection and corrected.

- Corrected manuscript commit: `dc73b0365be4020545e73ec768dbea5fed889b0e`.
- `ttogether` / `Ttogether` contamination: **REMOVED**.
- Recognition theorem label, D2 \(\mathcal O_k\) section, U2/U3 repairs, D3 Proposition 7.1 citation, and D4 corrections remain present.
- CI/PDF verification remains **PENDING** for the corrected source.

No mathematical status changes.

## 2026-09-28 — PAPER 3 REFEREE GAP CLOSURE / MANUSCRIPT RESYNCHRONIZATION

The adversarial manuscript review exposed real source-level gaps despite the prior publication artifact closure. The mathematical research frontier was already closed at the relevant scopes, but the manuscript had not faithfully synchronized several load-bearing proof details. This is classified as a **MANUSCRIPT SYNCHRONIZATION DEFECT**, not a reopening of the mathematics.

Corrected in `paper/main.tex`:
- U2 now explicitly states the coefficient-triviality/inflation chain: \(\rho\equiv1\pmod3\), \(P_{3^{k-1}+1}\subseteq P_2=\Phi\), and the kernel acts trivially on \(A_k(\rho)\).
- U3 now states the minimal one-relator hypothesis explicitly, including the free rank \(d=\dim H^1(H,\mathbf F_3)\) and \(r\in\Phi(F)\).
- The finite transgression quotient \(\mathcal O_k=H^2(Q_k,\mathbf F_3)/\operatorname{im}(\operatorname{tra}_k)\) is now included as the D2 proof carrier, while explicitly not claiming it is the final minimal carrier.
- The finite cup-line proof now cites Mináč–Pasini–Quadrelli–Tân, Proposition 7.1 at the actual relation-module/cup pairing step and explains why the added \(P_n(F)\subseteq P_3(F)\) relators contribute no quadratic initial form.
- The selector lower bound for \(m\le3^{k-2}\) now gives the direct valuation calculation showing \(\chi_G\) does not factor through \(W_m\).
- The LTE argument now correctly records \(v_3(u-1)=1\) and derives \(v_3(S_N(u))=k-1\).
- The recognition theorem is given an explicit LaTeX label for cross-reference, and manuscript typos were cleaned.
- The literature boundary now includes \(\mathcal O_k\) as a proof carrier while retaining the conditional novelty wording.

Independent source check:
- Mináč–Pasini–Quadrelli–Tân, Proposition 7.1 was verified directly from the published article: it gives the commutative pairing diagram relating the relation initial-form map to cup-product evaluation. This supports the manuscript's rank-one finite cup-line argument under the stated minimal-presentation hypotheses.
- Labute Theorem 4 was independently checked for existence/uniqueness of the canonical orientation and the value \(\chi(x_2)=(1-q)^{-1}\) in the odd-\(p\) normal form.

Classification:
- mathematical D2/D3/D4 status: **UNCHANGED / PASS-CLOSED at declared scopes**;
- manuscript synchronization: **REPAIR COMMITTED**;
- prior “final artifact” state: **SUPERSEDED by this source revision**;
- CI/PDF verification of commit `7adb6fe8ab43dd924daf282730c0c316757a892a`: **PENDING**;
- publication novelty: **OPEN / CONDITIONAL**.

Next authorized action: independent CI compilation, PDF text/content audit, artifact hash capture, then update the manuscript manifest and final state only after those gates pass.

## 2026-09-28 — FINAL PAPER 3 ARTIFACT / MANUSCRIPT SYNCHRONIZATION CLOSED

The manuscript synchronization gate required after the stale-PDF incident is now fully closed.

Authoritative final source: \`paper/main.tex\`.

Completed checks:
- source line-by-line audit and structural reordering;
- compile-failure diagnosis: unmatched closing math delimiter in U5a;
- repair and successful clean LaTeX compilation;
- Build Paper PDF CI run **36363508628**: PASS/CLOSED;
- workflow shell audit run **36363508467**: PASS/CLOSED;
- citation hygiene run **36363508580**: PASS/CLOSED;
- independent extraction/content audit of the CI PDF: PASS/CLOSED;
- exact artifact checksum capture.

Final artifact:
- PDF artifact ID: **10946925073**
- full submission artifact ID: **10945849160**
- PDF SHA-256: \`813fda4840783c3b37002828ccfbe092ccffed6ad189f46430222e5e930a56b0\`
- source package SHA-256: \`759476d1003fe2d106cfeae5d82f12f8d866afabfddbdd4a3d063cc0d90e7af0\`
- PDF size/pages: **405,622 bytes / 14 pages**
- CI validation commit: \`3acf4d551f66b21df7ed0528164ef76c690cbc13\`
- main-branch manuscript blob: \`c82e6c5277dd7aa21d3bc4ab9d5490d25cf6c694\`

A separate CI audit also found citation-artifact Unicode/tokens in three Paper 3 research notes; these were cleaned, and citation hygiene subsequently passed. This is a repository hygiene correction, not a mathematical change.

The final manuscript now explicitly reflects the closed research frontier: finite-window recognition, U5 uniqueness, intrinsic 1D cup-line carrier, and fixed rank-4 \(q=3\) selector minimality. The stronger finite-pair functional reconstruction remains OPEN/NOT LOAD-BEARING. Publication novelty remains OPEN/CONDITIONAL.

The temporary validation PR #5 was closed without merge after successful validation.

Classification:
- manuscript synchronization: **PASS / CLOSED**
- final PDF artifact: **PASS / CLOSED**
- publication novelty: **OPEN / CONDITIONAL**


## 2026-09-27 — M2 POST-BLUMER–QUADRELLI F1 SHARPNESS AUDIT CLOSED

A targeted post-publication literature audit was completed before computation. Marina Palaisti, arXiv:2609.00253 (submitted 2026-08-31), is explicitly an F2 two-relator paper: it studies the added commuting relator, develops support-block reductions, and proves a five-fold vanishing theorem for the full-interior-support case while reducing remaining support types. It does not treat the F1 one-relator family or prove sharpness/failure for F1 at n>q. Targeted searches for F1 + n>q + Massey/Demuškin likewise found no exact converse or obstruction.

The F2 result is therefore a methodological comparison, not prior art resolving F1. Its one-relator reduction relies on the extra commuting relator/second central defect; no transfer to F1 is assumed.

Classification:
- M2 post-Blumer–Quadrelli prior-art audit: **PASS / CLOSED** (audited negative; not an absolute claim about unindexed/unpublished work).
- F1 proof-mechanism breakpoint at n=q+1: **PASS / CLOSED** from independent hand calculation.
- Actual F1 sharpness/failure at n=q+1: **OPEN / LOAD-BEARING**.
- M3 finite-window recognition: **NOT YET AUTHORIZED**.

Next authorized action: smallest M1 computation (p,q,d,n)=(3,3,2,4), U_5(F_3), with exact admissibility/cup-vanishing/Dwyer-lift conditions and independent verification.

Detailed audit: research/M2_POST_BQ_F1_SHARPNESS_LITERATURE_AUDIT_2026-09-27.md

## 2026-09-27 — PAPER 3 M-GATE: BLUMER–QUADRELLI F1 MASSEY SHARPNESS

The uploaded arXiv-2603.15464v2 source was independently unpacked and checked against the current Paper 3 target discussion.

Verified from the actual source:
- Proposition (2.a): for G in F1 and n <= q, G satisfies a strong variant of n-fold Massey vanishing.
- Example 2(a): ordinary Demuškin groups satisfy strong n-fold Massey vanishing for every n >= 3, with Blumer–Quadrelli citing Pál–Szabó, Theorem 3.5 (arXiv:1811.06192). The earlier Mináč–Tân attribution is corrected.
- For G in F1, the associated graded restricted Lie algebra is explicitly presented by <X1,Y1,...,Xd,Yd | [X2,Y2]+...+[Xd,Yd]=0>, so the F1 branch is structurally compatible with the existing Zassenhaus/initial-form/Magnus-Fox toolkit.

## 2026-10-01 — THREE-PAPER PUBLICATION-STYLE FINALIZATION

A style-only publication pass was completed after the existing mathematical and artifact gates had closed. The pass removed companion-paper/placeholder boilerplate, reduced repetitive defensive novelty language, standardized finite coefficient notation, made p=q=3,f=1 explicit in Paper 2, replaced informal "kills" terminology, and tightened the motivation/abstract language. No mathematical theorem, proof, hypothesis, scope, or novelty conclusion was intentionally changed.

Final style artifacts:
- Paper 1: branch paper1-style-final-2026-10-01; 8 pages; SHA-256 b4806dc7ed111ffeb3b93d5ef9066d958252fff132506a5d95f25dad76afe960.
- Paper 2: branch paper2-style-final-2026-10-01; 13 pages; SHA-256 97504d2bc5db7f668f2287d62bca902cde0b285b1a4b7ef11ffe58c0c8928e32.
- Paper 3: branch paper3-style-final-2026-10-01; 17 pages; SHA-256 3518e5f966401d48eae9c8b76b80fe7a9ba4e53f76bc4255edb66862082bf7ff.

CI/PDF verification and visual first-page inspection: PASS/CLOSED. Publication novelty remains OPEN/CONDITIONAL. Detailed record: research/THREE_PAPER_PUBLICATION_STYLE_FINAL_2026-10-01.md.


## 2026-10-01 — THREE-PAPER EDITORIAL FINAL PDF PASS

A final editorial pass was applied to the three publication-candidate manuscripts to remove visible AI/session scaffolding and amateur-style presentation without changing the mathematical claims or reopening closed proof branches.

- Paper 1 branch: `paper1-editorial-final-2026-10-01`; source `paper/successor_main.tex`; final CI run **36797031449**: PASS; PDF 8 pages; final PDF SHA-256 `ec25a3bb55ae19e48629895bca722981ad5e33827cc5be2ce1228326c64271b0`.
- Paper 2 branch: `paper2-editorial-final-2026-10-01`; source `paper/main.tex`; final CI run **36796701931**: PASS; PDF 12 pages; final PDF SHA-256 `aabe2f0056b0ce250e06fa7cba1840f93a58754d02c8fb0bfacc46d00bdbdcb7`.
- Paper 3 branch: `paper3-editorial-final-2026-10-01`; source `paper/main.tex`; final CI run **36797451738**: PASS; PDF 14 pages; final PDF SHA-256 `15eef73b46fa70db087f434108a187e4f79fcbc01a88326507127d7d0f34a95a`.

Editorial changes include: removal of placeholder companion-paper/arXiv language; removal of repeated defensive novelty boilerplate; replacement of informal “kills” in the Paper 1 definition by the standard “factors through” formulation; clearer separation of factorization, recognition, and scope; explicit (q=p=3) identification in the fixed rank-four papers; consistent Demuškin typography; and clearer standalone titles. No mathematical theorem, hypothesis, boundary, or novelty classification was changed.

Two review comments were deliberately not adopted because they are not errors in the authoritative source: (1+3A_k) is a multiplicative principal-unit subgroup (so the notation is legitimate), and extracted strings such as “3j” are PDF text-extraction artifacts rather than source-level (3^j) failures. The research frontier remains unchanged: Paper 1/2/3 mathematical status PASS/CLOSED at their declared scopes; publication novelty remains OPEN/CONDITIONAL.


## 2026-10-01 — F1 GENERALIZATION ROADMAP FROZEN BEFORE NEXT RESEARCH WINDOW

The current research decision is to postpone new mathematics until a fresh chat/window and preserve the forward roadmap in the authoritative stage record. The F1 branch is an ambitious but legitimate generalization test, not a claim that the field is awaiting this exact theorem. Its value rises sharply only for an intrinsic structural result: finite separation, sharp recognition threshold, no-go theorem, or reusable carrier. Reproving that F1 is not 1-cyclotomic is not new by itself; the new target is finite-window visibility/intrinsicization of the known obstruction.

Forward sequence: A) smallest D/F1 pair at (3,2,3); B) uniform F1 parameter theorem if supported; C) genuinely different category enlargement (F2 deferred); D) enlargement from T_cyc to a family of global properties; E) general finite-window recognition theory r_T(C;D_bullet). Promotion requires theorem-level finite separation, sharp threshold, no-go, or reusable carrier. Do not run large computation before the mandatory pre-checks. Do not re-open the closed F1 Massey route without new evidence. Do not claim priority or that the field is waiting for this result.

Classification: F1 finite-window recognition OPEN / DECISIVE; roadmap CONDITIONAL; Paper 1–3 publication novelty OPEN / CONDITIONAL.


## 2026-10-01 — PAPER 3 PHASE A: D vs F1 FINITE-WINDOW RECOGNITION

Phase A was executed after the mandatory repository restoration and pre-checks.

For the fixed two-family category C_{p,d,q}={ordinary Demushkin D_{d,q}, Blumer–Quadrelli F1_{d,q}} and target T_cyc = 1-cyclotomicity:
- W_2 is identical for the two families: both have the same 2d-dimensional abelianization window.
- At W_3, the intrinsic commutator/cup pairing has rank 2d for D and 2d-2 for F1.
- The reason is the degree-2 initial form: D has sum_{i=1}^d [X_i,Y_i], whereas F1 has sum_{i=2}^d [X_i,Y_i], because [x_1^q,y_1] starts in Zassenhaus degree q+1 >= 3.
- Therefore W_3 separates D from F1 without inserting q or using a presentation-dependent lift.
- At (p,d,q)=(3,2,3), the ranks are 4 and 2; an independent exact matrix calculation confirms this.
- Since W_2 does not separate and W_3 does, the declared two-object recognition threshold is exactly r_{T_cyc}(C_{3,2,3};D)=3. The same argument gives the uniform pairwise result r=3 for odd p, d>=2, q=p^f.

Literature boundary: the underlying D/F1 degree-2 structures and the global 1-cyclotomic/non-1-cyclotomic facts are already explicit in Blumer–Quadrelli and the Demushkin literature. Thus the r=3 statement is a finite-window reformulation/derivation, not a priority claim.

Classification:
- Phase A fixed pair: **PASS / CLOSED**.
- Uniform D-vs-F1 pairwise theorem: **PASS / CLOSED**.
- Novelty from Phase A alone: **OPEN / CONDITIONAL; currently weak**.
- F1 broader finite-window recognition program: **OPEN / DECISIVE**.

Detailed record: research/PAPER3_PHASE_A_D_VS_F1_FINITE_RECOGNITION_2026-10-01.md

Next authorized direction: seek a broader category in which the same intrinsic W_3 carrier recognizes 1-cyclotomicity without hard-coding family membership or q; do not treat the D/F1 pair alone as sufficient for a new-paper claim.


## 2026-10-01 — PAPER 3 PHASE B: D/F1/F2 RECOGNITION

Phase B extends the finite-window test category from D vs F1 to the three-family category {D,F1,F2}.

For odd p, d>=2, q=p^f:
- W_2 is identical across the three families.
- D has one quadratic relation line with nondegenerate alternating rank 2d.
- F1 has one quadratic relation line with rank 2d-2.
- F2 has a two-dimensional quadratic relation space (the Demushkin quadratic relation plus the independent unpaired commutator).
Thus W_3 separates all three family types intrinsically, and the exact recognition threshold for T_cyc on the declared three-family category is r=3.

Classification:
- D/F1/F2 recognition: **PASS / CLOSED**.
- Uniform parameter statement: **PASS / CLOSED**.
- Reusable W_3 carrier: **PASS / LOCAL**.
- Novelty from this family-by-family extension: **OPEN / CONDITIONAL; weak**.

The important negative boundary is now explicit: continuing to add families whose non-cyclotomicity is already encoded in the quadratic relation does not deepen the program. The next decisive test is a cyclotomic/non-cyclotomic pair with the same W_3 quadratic/cup data. If such a pair exists, W_3 recognition is false on the enlarged category and a higher finite carrier is required; if no such pair exists in a meaningful category, a structural theorem must explain why.
Detailed record: research/PAPER3_PHASE_B_D_F1_F2_FINITE_RECOGNITION_2026-10-01.md


## 2026-10-01 — SAME-W3 OBSTRUCTION FOUND: F1 vs CYCLOTOMIC CONTROL

The decisive obstruction test produced a genuine same-window/different-target pair at (p,d,q)=(3,2,3).

Take
\[
G_{F1}=\langle x_1,y_1,x_2,y_2\mid [x_1^3,y_1][x_2,y_2]=1\rangle
\]
and the cyclotomic control
\[
G_{cyc}=D_{1,3}*F_2
=\langle x_1,y_1,x_2,y_2\mid x_2^3[x_2,y_2]=1\rangle.
\]

Blumer–Quadrelli gives T_cyc(G_F1)=false; the Demushkin factor is 1-cyclotomic and free pro-p products of cyclotomic pairs remain cyclotomic, so T_cyc(G_cyc)=true.

Modulo D_3, both defining relators reduce to the same quadratic relation [x_2,y_2]=1:
- in F1, [x_1^3,y_1] has Zassenhaus degree 4;
- in the cyclotomic control, x_2^3 has degree 3 and is discarded by G/D_3.
Thus W_3(G_F1) ~= W_3(G_cyc), while the global target differs.

Conclusion:
\[
\boxed{r_{T_cyc}\ge4}
\]
for every admissible category containing this pair.

This closes the proposed general W_3 recognition route:
- general W_3 recognition: **FAIL / CLOSED**;
- same-W_3 separation pair: **PASS / CLOSED**;
- lower bound r>=4: **PASS / CLOSED**;
- exact threshold: **OPEN / LOAD-BEARING**.

This is the first result in the F1 branch that directly realizes the intended Paper 3 obstruction pattern rather than merely rephrasing known family differences.

Next authorized gate: determine intrinsically whether W_4 separates the pair. Do not use a presentation-local p-power coordinate without proving its naturality.
Detailed record: research/PAPER3_SAME_W3_OBSTRUCTION_F1_VS_CYC_CONTROL_2026-10-01.md


## 2026-10-01 — SAME-W3 OBSTRUCTION FOUND: F1 vs CYCLOTOMIC CONTROL

The decisive obstruction test produced a genuine same-window/different-target pair at (p,d,q)=(3,2,3).

Take G_F1=<x_1,y_1,x_2,y_2 | [x_1^3,y_1][x_2,y_2]=1> and the cyclotomic control G_cyc=D_{1,3}*F_2=<x_1,y_1,x_2,y_2 | x_2^3[x_2,y_2]=1>.

Blumer–Quadrelli gives T_cyc(G_F1)=false; the Demushkin factor is 1-cyclotomic and free pro-p products of cyclotomic pairs remain cyclotomic, so T_cyc(G_cyc)=true.

Modulo D_3, both defining relators reduce to the same quadratic relation [x_2,y_2]=1: in F1, [x_1^3,y_1] has Zassenhaus degree 4; in the cyclotomic control, x_2^3 has degree 3 and is discarded by G/D_3. Thus W_3(G_F1) ~= W_3(G_cyc), while the global target differs.

Conclusion: r_{T_cyc}>=4 for every admissible category containing this pair.

Classification:
- same-W_3 separation pair: PASS / CLOSED;
- lower bound r>=4: PASS / CLOSED;
- general W_3 recognition: FAIL / CLOSED;
- exact threshold: OPEN / LOAD-BEARING.

Next authorized gate: determine intrinsically whether W_4 separates the pair. Do not use a presentation-local p-power coordinate without proving its naturality.

Detailed record: research/PAPER3_SAME_W3_OBSTRUCTION_F1_VS_CYC_CONTROL_2026-10-01.md

## 2026-10-01 — W_4 CLOSES THE CONCRETE F1 RECOGNITION PAIR

The same-W_3 obstruction pair was pushed one level further at (p,d,q)=(3,2,3).

For F1, modulo D_4 the relation gives [x_2,y_2]=1 because [x_1^3,y_1] lies in D_4.

For the cyclotomic control D_{1,3}*F_2, the relation gives [x_2,y_2]=x_2^{-3}; the class x_2^3 is nonzero in D_3/D_4 because the associated restricted Lie algebra has only the quadratic relation [X_2,Y_2] and no degree-3 relation killing X_2^[3].

Thus W_4 separates the pair. Combined with W_3 equality:
r_{T_cyc}({G_F1,G_cyc};D)=4.

Classification:
- W_3 equality: PASS / CLOSED;
- W_4 separation: PASS / CLOSED for the concrete pair;
- exact concrete threshold 4: PASS / CLOSED;
- uniform q=p^f threshold q+1: OPEN / LOAD-BEARING.

Detailed record: research/PAPER3_SAME_W3_OBSTRUCTION_F1_VS_CYC_CONTROL_2026-10-01.md


## 2026-10-01 — W4 INTRINSICITY AUDIT / CONCRETE THRESHOLD 4 CLOSED

The prior critical review identified a load-bearing gap in the W4 argument: the statement that x2^[3] survives in D3/D4 was correct in substance but the earlier record did not make the invariant presentation-independent. This has now been repaired.

For the concrete pair
G_F1=<x1,y1,x2,y2 | [x1^3,y1][x2,y2]=1> and
G_cyc=D_{1,3}*F(x1,y1), with D_{1,3}=<x2,y2 | x2^3[x2,y2]=1>,
the uploaded Blumer–Quadrelli source explicitly identifies the F1 associated graded restricted Lie algebra as a free product of a free rank-2 restricted Lie algebra and a rank-2 Demushkin restricted Lie algebra. In the latter, the only defining quadratic relation is [X2,Y2], so X2^[3] is nonzero in degree 3.

The intrinsic comparison is made at the truncated restricted relation module over the common W3 quadratic shadow:
- F1 has zero degree-3 defining relation component.
- The cyclotomic control has a nonzero degree-3 p-power component X2^[3].
The p-power image is functorial under restricted-Lie isomorphisms, so the distinction is not tied to the chosen generator x2.

Therefore W4 separates the pair intrinsically. Combined with W3 equality:
r_Tcyc({G_F1,G_cyc};D_bullet)=4.

Classification:
- intrinsic W4 separation: PASS / CLOSED;
- exact threshold 4 for the declared two-object category: PASS / CLOSED;
- uniform q=p^f analogue: OPEN / LOAD-BEARING;
- broad recognition theorem: OPEN / CONDITIONAL;
- novelty/priority: OPEN / CONDITIONAL.

Literature source: Blumer–Quadrelli, arXiv:2603.15464v2; it proves the global F1 non-1-cyclotomicity and gives the relevant associated graded restricted Lie algebra structure. The finite-window W4 deduction is the present research step.

Authoritative detail: research/PAPER3_W4_INTRINSIC_SEPARATION_AUDIT_2026-10-01.md


## 2026-10-01 — F1 UNIFORM FINITE-q THRESHOLD CLOSED

The concrete W4 result generalizes cleanly to every finite q=p^f (odd p, d>=2) without relying on a presentation-local carrier.

Define
G_F1(q)=<x1,y1,...,xd,yd | [x1^q,y1] [x2,y2]... [xd,yd]=1>
and the cyclotomic control
G_cyc(q)=D_{1,q}*F_{2d-2}, with D_{1,q}=<x2,y2 | x2^q[x2,y2]=1>.

W_q equality: x1^q contributes only in D_{q+1} after commutation in F1, while x2^q in the control lies in D_q; modulo D_q both relators have the same quadratic word. Thus W_q isomorphic.

W_{q+1} separation: in the control, x2^q=[x2,y2]^{-1}, so x2^q is trivial in the abelianization of W_{q+1}. In F1, Blumer–Quadrelli's explicit associated restricted Lie algebra description implies X2^[q] is nonzero, so x2^q survives in D_q/D_{q+1} and remains nontrivial in the abelianization of W_{q+1}. Hence the two W_{q+1} windows are non-isomorphic.

Therefore, for every finite q=p^f with p odd and d>=2:
r_Tcyc({G_F1(q),G_cyc(q)};D_bullet)=q+1.

This is stronger than the earlier analogy-based q+1 candidate: it is a proved local pairwise threshold theorem. It does NOT establish a broad category recognition theorem or a q-independent carrier.

Classification:
- uniform finite-q pairwise threshold: PASS / CLOSED;
- broad category recognition: OPEN / CONDITIONAL;
- novelty/priority: OPEN / CONDITIONAL.

Literature input: Blumer–Quadrelli arXiv:2603.15464v2 proves the F1 non-1-cyclotomicity and the explicit associated restricted Lie algebra structure; the finite-window threshold deduction is the present work.

Record: research/PAPER3_W4_INTRINSIC_SEPARATION_AUDIT_2026-10-01.md


## 2026-10-01 — F2 GATE PRE-CHECK: OBVIOUS CYCLOTOMIC FREE-PRODUCT CONTROL RULED OUT AT W3

The next enlargement is the Blumer–Quadrelli F2 family. Before computation, the required pre-check was completed.

For the smallest rank-4 F2 quadratic relation space
R_F2=<[X1,Y1]+[X2,Y2],[X1,X2]>,
the Pfaffian of the relation pencil is proportional to a^2. For the natural cyclotomic control D_{1,q}*D_{1,q}, the relation space is <[X1,Y1],[X2,Y2]> and its Pfaffian is proportional to ab. These pencil types are not GL4-equivalent (repeated root versus two distinct roots), so W3 cannot match.

Thus the immediate free-product cyclotomic control is FAIL / CLOSED as a same-W3 candidate. This does not rule out all cyclotomic controls.

Next authorized search: cyclotomic groups outside this free-product control class, especially elementary-type cyclotomic semidirect products, for a W3 quadratic relation space of F2 type. No large computation until such a control is identified.

Record: research/PAPER3_F2_SAME_W3_CONTROL_GATE_2026-10-01.md

## 2026-10-01 — F1 UNIFORM THRESHOLD CRITICAL RECHECK CLOSED

A critical review challenged the parameter-uniform F1/cyclotomic-control theorem on two points: whether (W_q) equality had been shown for the full filtered quotient, and whether (X_2^{[p^f]}
eq0) had been established uniformly.

Independent recheck closes both.

- **Full (W_q) equality:** in the common free pro-(p) group (F), both defining relators reduce modulo (D_q(F)) to the same word (s=[x_2,y_2]cdots[x_d,y_d]). Using (D_q(F/R)=D_q(F)R/R), both windows are exactly (F/(D_q(F),s)). This is stronger than equality of initial forms.
- **Restricted-power nonvanishing:** the Blumer–Quadrelli F1 associated restricted Lie algebra admits a restricted map (X_2mapsto t), all other generators to (0), into a free rank-one abelian restricted Lie algebra. Hence (X_2^{[p^f]}
eq0) for every finite (q=p^f).
- **Independent group-level verification:** the (W_{q+1}) abelianizations are
  [
  (mathbb Z/p^{f+1})^{2d}
  quad	ext{and}quad
  (mathbb Z/p^{f+1})^{2d-1}oplusmathbb Z/p^f,
  ]
  so their orders differ by (p). This independently forces (W_{q+1}) non-isomorphism.

Classification:
- uniform pairwise threshold (r=q+1): **PASS / CLOSED**;
- broad category-level recognition: **OPEN / CONDITIONAL**;
- novelty/priority: **OPEN / CONDITIONAL**.

The result remains a pairwise local theorem and does not establish a q-independent recognition carrier.


## 2026-10-01 — F2 SAME-W3 CYCLOTOMIC CONTROL GATE CLOSED

The F2 same-W3 control search was completed at the authorized structural level. For the smallest rank-4 F2 relation space
\[
R_{F2}=\langle \omega_1+\omega_2,\eta\rangle,
\qquad \operatorname{Pf}(a(\omega_1+\omega_2)+b\eta)\sim a^2,
\]
the repeated-root Pfaffian type is incompatible with the split-root type of the standard elementary-type cyclotomic constructions examined at rank 4 with two defining relations. The latter yield only Pfaffian type \(ab\) or the degenerate case \(0\), not \(a^2\).

Classification:
- F2 × standard elementary-type cyclotomic control: **FAIL / CLOSED**.
- F2 × arbitrary cyclotomic pro-p group: **OPEN / CONDITIONAL**; no universal no-go theorem is claimed.
- F2 \(W_4\) computation: **NOT AUTHORIZED** because no legitimate W3-matching control was found.
- F2 broader finite-window recognition: **OPEN / CONDITIONAL**.

This is a structural boundary, not a failed search report: the standard elementary-type cyclotomic construction mechanism cannot realize the repeated-root F2 \(W_3\) quadratic type in the audited rank-4/two-relator setting. F1 is not reopened. The next research direction must therefore be a genuinely broader finite-window recognition question, subject to a fresh pre-check and literature/non-redundancy audit.

Authoritative detail: research/PAPER3_F2_SAME_W3_CONTROL_GATE_2026-10-01.md


## 2026-10-01 — F2 SAME-W3 CYCLOTOMIC CONTROL GATE CLOSED

The F2 same-W3 control search was completed at the authorized structural level. For the smallest rank-4 F2 relation space
\[
R_{F2}=\langle \omega_1+\omega_2,\eta\rangle,
\qquad \operatorname{Pf}(a(\omega_1+\omega_2)+b\eta)\sim a^2,
\]
the repeated-root Pfaffian type is incompatible with the split-root type of the standard elementary-type cyclotomic constructions examined at rank 4 with two defining relations. The latter yield only Pfaffian type \(ab\) or the degenerate case \(0\), not \(a^2\).

Classification:
- F2 × standard elementary-type cyclotomic control: **FAIL / CLOSED**.
- F2 × arbitrary cyclotomic pro-p group: **OPEN / CONDITIONAL**; no universal no-go theorem is claimed.
- F2 \(W_4\) computation: **NOT AUTHORIZED** because no legitimate W3-matching control was found.
- F2 broader finite-window recognition: **OPEN / CONDITIONAL**.

This is a structural boundary, not a failed search report: the standard elementary-type cyclotomic construction mechanism cannot realize the repeated-root F2 \(W_3\) quadratic type in the audited rank-4/two-relator setting. F1 is not reopened. The next research direction must therefore be a genuinely broader finite-window recognition question, subject to a fresh pre-check and literature/non-redundancy audit.

Authoritative detail: research/PAPER3_F2_SAME_W3_CONTROL_GATE_2026-10-01.md


## 2026-10-01 — F2 CONTROL AUDIT CORRECTION: PFAFFIAN VERIFIED; CANDIDATE COMPLETENESS REMAINS OPEN

A one-time independent verification was performed on the F2 same-\(W_3\) control gate, without reopening the F2 research branch.

For the rank-4 F2 relation plane
\[
R_{F2}=\langle X_1\wedge Y_1+X_2\wedge Y_2,\;X_1\wedge X_2\rangle,
\]
the ordered-basis skew matrix of \(a(\omega_1+\omega_2)+b\eta\) has direct Pfaffian
\[
\operatorname{Pf}=a^2.
\]
For the two construction shapes actually preserved in the earlier elementary-type audit:
1. split/free-product of two rank-2 one-relator factors: \(R=\langle\omega_1,\omega_2\rangle\), giving \(\operatorname{Pf}=ab\);
2. shared-direction semidirect shape followed by a free rank-1 factor: the two quadratic forms share a degree-one direction, giving \(\operatorname{Pf}=0\).

Thus the direct calculation independently confirms the candidate-level obstruction \(a^2\not\sim ab,0\) under \(GL_4\).

However, the repository does **not** contain an independent proof that these two shapes exhaust the full standard elementary-type rank-4/two-relator construction class. The earlier wording “structural no-go for the audited standard construction mechanism” / “construction mechanism itself” therefore overstated the evidence.

Corrected classifications:
- recovered examined elementary-type candidates: **FAIL / CLOSED**;
- completeness of the recovered candidate list: **OPEN**;
- arbitrary cyclotomic pro-\(p\) control: **OPEN / CONDITIONAL**;
- operational F2 branch: **CLOSED** unless new evidence supplies a new construction or proves completeness;
- no \(W_4\) computation authorized.

This entry supersedes only the strength of the prior no-go wording. It does not reopen F1 or the already rejected candidates.

Record: `research/PAPER3_F2_SAME_W3_CONTROL_GATE_2026-10-01.md`

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

## 2026-10-01 — NEXT RESEARCH SCOPE FROZEN: FINITE-PAIR UNIVERSALITY/MINIMALITY OR GENUINELY NEW CARRIER

The post-Paper-3 research scope has been explicitly narrowed.

Paper 3 is **FROZEN / COMPLETE**. The next branch is not a re-proof or further audit of Paper 3. The only authorized mathematical targets are:

- the existing carrier's **finite-pair universal property / minimality**, with the admissible carrier category stated explicitly; or
- a **genuinely new carrier**, meaning a finite-input, q-blind, functorial, gauge-independent object not equivalent to the frozen selector and yielding a new separation/threshold/factorization consequence.

Consequences:
- the completed Kummer selector, full delta-family, intrinsic cup-line, and prior Gate D machinery are fixed inputs/boundaries;
- no W_11/W_12, Fox, or large-dimensional computation is authorized merely to repackage the completed selector;
- broader F1/F2 recognition examples are not active targets unless they directly produce a new carrier or settle the finite-pair universal/minimality question;
- any “minimality” claim without a declared admissible category is not authorized.

Decision gate: **finite-pair universal property/minimality → PASS/LOCAL, FAIL/CLOSED, or OPEN; otherwise pursue a genuinely new carrier.**

This entry controls the next research window and supersedes broader historical roadmap wording where it conflicts with this narrower scope.


## 2026-10-01 — O_k FINITE-PAIR MINIMALITY ATTACK: IMMEDIATE REDUNDANCY BOUNDARY

The proposed five-step plan was critically reordered before execution. The exact transgression quotient is already defined and its intrinsic finite-pair legitimacy is already CLOSED at the declared scope:
\[
Q_k=G/D_{p^{k-1}+1},\quad E_k=G/D_{p^{k-1}+2},\quad
\mathcal O_k=H^2(Q_k,\mathbf F_p)/\operatorname{im}(\operatorname{tra}_k).
\]
The central extension and five-term transgression make this construction presentation-independent and functorial under morphisms of filtered finite extensions (contravariantly on cohomology); orientation and q are not part of its definition.

The decisive minimality issue is already bounded by the frozen finite cup-line result. The intrinsic line
\[
C_k(Q_k)=\operatorname{im}(H^1(Q_k,\mathbf F_p)^{\otimes2}\xrightarrow{\cup}H^2(Q_k,\mathbf F_p))
\]
has \(\dim C_k=1\) by the audited relation-module/cup-duality argument, embeds into \(\mathcal O_k\), and the finite selector's false-branch obstruction outputs lie in \(C_k\). Thus \(C_k\) is already a one-dimensional finite-input, q-blind, intrinsic selector carrier, while \(\mathcal O_k\) is only a proof carrier.

This creates a hard boundary: \(\mathcal O_k\) cannot be the minimal recognition carrier in any admissible category that contains both the transgression carrier and this intrinsic cup-line carrier. Reopening the cup-line proof is not authorized; it is a frozen input. The remaining genuinely mathematical question is narrower: whether \(\mathcal O_k\) nevertheless has a finite-pair UNIVERSAL property as a proof/obstruction carrier, i.e. whether every admissible functorial linear obstruction carrier for the transient-stable separation problem factors canonically through \(\mathcal O_k\). The existence of the smaller selector carrier prevents conflating this with recognition minimality.

The previously suggested two-week elapsed-time stop rule is rejected as a mathematical criterion. The correct stop is structural: if \(C_k\) already supplies the required recognition property, the \(\mathcal O_k\)-minimality branch is CLOSED as REDUNDANT; only the distinct universal-obstruction property may remain OPEN. If a genuinely new carrier is proposed, it must be finite-input, q-blind, functorial, gauge-independent, non-equivalent to the frozen selector, and yield a new separation/threshold/factorization consequence.

Classification:
- exact definition of \(\mathcal O_k\): PASS / CLOSED;
- presentation/orientation independence: PASS / CLOSED at the declared finite-pair scope;
- functoriality: PASS / CLOSED for filtered-pair morphisms/isomorphisms, with cohomological variance stated explicitly;
- recognition minimality of \(\mathcal O_k\): FAIL / CLOSED by existing intrinsic one-dimensional \(C_k\) carrier;
- finite-pair universal obstruction property of \(\mathcal O_k\): OPEN / LOAD-BEARING;
- Paper 2 selector redundancy: CLOSED as a recognition theorem; \(\mathcal O_k\) adds only the proof-carrier quotient unless a universal-obstruction theorem is proved;
- new carrier: NOT OPENED yet.

Next authorized attack: formalize the finite-pair category and test the universal factorization property of \(\mathcal O_k\). No new W-depth, Fox, 45-dimensional, or Paper 2 reproof computation is authorized.

## 2026-10-01 — MIXED FOX CRITICAL FACTORIZATION REVIEW

Independent review corrected the interpretation of the standard-family mixed Fox calculation. The equations for r_q correctly give A=C=D=1 and B=(1-q)^(-1) mod 3^k, and completed/projective covariance remains PASS / LOCAL. However, q-level congruence/factorization within the standard family is not the required abstract finite-pair theorem W_k(G)≅W_k(H) ⇒ M_k(G)≅M_k(H). Therefore global finite-pair descent remains OPEN / LOAD-BEARING. The earlier non-redundancy statement was also narrowed: higher 3-adic information relative to the bare F_3 vector-space object is a local information distinction, not yet a category-level non-redundancy theorem. No larger computation is authorized. Detailed correction: research/PAPER3_MIXED_FACTORISATION_CRITICAL_REVIEW_2026-10-01.md.


## 2026-10-01 — MIXED FOX WEIGHTED MAGNUS DESCENT RESULT

A literature-backed weighted Magnus argument materially narrows the finite-pair descent problem. For N_k=3^{k-1}+1, Efrat's p-adic Magnus coefficient bound for D_{N_k} gives v_3(epsilon_w)>=ceil(log_3(N_k/|w|)); hence |w|+v_3(epsilon_w)>=k+1 for all relevant word lengths. Therefore D_{N_k} is invisible to the mixed (3,I)-adic coefficient jet below precision k, while the boundary contribution is carried by D_{N_k}/D_{N_k+1}. Classification: weighted coefficient descent PASS/CLOSED; boundary role PASS/LOCAL. The exact projective Fox relation-module descent W_k -> M_k remains OPEN/LOAD-BEARING because a categorical identification of the projective relation jet with the weighted Magnus datum is still required. A naive deep-relator counterexample is ruled out by the same valuation bound. Detailed record: research/PAPER3_MIXED_3I_ADIC_WEIGHTED_MAGNUS_DESCENT_2026-10-01.md.



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

## 2026-10-01 — MIXED FOX EXTENSION-WINDOW CATEGORICAL AUDIT

The categorical descent issue was sharpened after the weighted Magnus step.

For
\[
N_k=3^{k-1}+1,\quad Q_k=G/D_{N_k},\quad E_k=G/D_{N_k+1},\quad A_k=D_{N_k}/D_{N_k+1},
\]
the natural finite input for the projective mixed Fox relation jet is the central extension
\[
1\to A_k\to E_k\to Q_k\to1.
\]

This resolves the type defect in treating \((Q_k,A_k)\) as though \(A_k\) were a subgroup of \(Q_k\). But it also exposes a stronger logical boundary: the extension window is an enriched input. The forgetful map
\[
U:\mathbf{ExtWin}_k\to\mathbf{Pair}_k,qquad
(A_k\hookrightarrow E_k\twoheadrightarrow Q_k)\mapsto(Q_k,A_k)
\]
forgets the extension class.

Therefore the original finite-pair theorem requires the mixed Fox construction \(F_k\) on extension windows to factor through \(U\):
\[
F_k=\overline F_k\circ U,
\]
equivalently, to be constant up to canonical projective equivalence on every admissible fiber of \(U\).

No extension reconstruction or fiber-invariance theorem is currently proved. Thus adding \(E_k\) is not yet justified as a canonical enrichment of the original finite pair; it must be treated as additional input.

Positive result: because \(E_k\) is finite, the mixed Fox relation jet can be formulated from the finite group algebra \(\mathbf Z_3[E_k]\), its mixed maximal ideal, and the stable/projective relation-module construction. The weighted Magnus result then supplies compatibility with the precision-k jet of the original group. This makes the extension-window branch legitimate, but it does not yet make it a finite-pair carrier.

Literature control: Mel'nikov's pro-p relation-module exact sequence supplies the Fox/Lyndon structural mechanism; Efrat supplies natural finite Zassenhaus/Magnus constructions. Neither source supplies the present project-specific finite-pair factorization. citeturn0search24turn0search4turn0academia23

Classification:
- extension-window object: **PASS / CLOSED**;
- extension-window → projective mixed Fox construction: **PASS / LOCAL**;
- extension-window as canonical enrichment of \((Q_k,A_k)\): **OPEN**;
- original finite-pair → mixed Fox descent: **OPEN / LOAD-BEARING**;
- novelty: **OPEN**.

Next authorized action: test fiber invariance / canonical reconstruction. No larger Fox computation is authorized. Detailed audit: `research/PAPER3_MIXED_EXTENSION_WINDOW_CATEGORICAL_AUDIT_2026-10-01.md`.


## 2026-10-01 — MIXED FOX EXTENSION-WINDOW FIBER ATTACK / BROAD-CATEGORY NO-GO

The first direct fiber-invariance attack exposed a prerequisite that had not been formalized: the phrase “admissible extension window” must specify the category before a same-pair fiber test can be interpreted as the project's theorem.

For the broad category of finite central 3-extensions with fixed trivial pair Q=C3×C3, A=C3, there are distinct extension classes in H^2(Q,A). Concrete examples with the same forgotten pair are the power-type extension C9×C3 and the exponent-3 Heisenberg extension with center C3. Their extension classes have different power/Bockstein versus commutator components, and the relation-module/Fox boundary data distinguishes those components. Projectivization removes unit/gauge rescaling but does not identify the two extension classes.

Therefore:
- arbitrary-extension pair descent: FAIL / CLOSED;
- extension-window mixed Fox construction: PASS / LOCAL;
- Demuškin-restricted pair descent: OPEN / LOAD-BEARING;
- admissible Demuškin extension-window category: OPEN / PREREQUISITE.

This is a structural counterexample, not a large numerical computation. It does not prove failure on the specific Demuškin family because that family may impose a unique/constrained extension class over each pair.

The correct next order is now: define the admissible Demuškin ExtWin category → analyze fibers of U → test invariance/reconstruction. No W_11/W_12, large Fox scan, or unrelated branch is authorized. Paper 3 remains frozen and unaffected.

Detailed audit: research/PAPER3_MIXED_EXTENSION_WINDOW_FIBER_NO_GO_AUDIT_2026-10-01.md.

## 2026-10-01 — DEMUŠKIN ADMISSIBILITY / EXTENSION-FIBER RECONSTRUCTION

The previously undefined “admissible Demuškin extension-window category” was made explicit for the active mixed-Fox branch: canonical Zassenhaus windows of infinite odd-prime finite-rank Demuškin groups of fixed rank, with q a p-power or 0.

Using the standard Demuškin classification and the Zassenhaus grading, the forgetful map from the extension window to the bare pair has a singleton fiber up to extension-window isomorphism at the declared scope:
- q<N_k is detected by Q_k through the first q-dependent graded relation;
- q=N_k is detected by dim(A_k);
- q>N_k gives the same E_k through precision N_k+1.

Hence the earlier broad-category H^2 obstruction does not propagate automatically to the Demuškin family.

Classification:
- broad arbitrary-extension pair descent: FAIL/CLOSED;
- Demuškin admissibility definition: PASS/CLOSED at declared scope;
- Demuškin pair→extension reconstruction: PASS/LOCAL;
- extension-window→Mixed Fox: PASS/LOCAL;
- original pair→Mixed Fox: OPEN/LOAD-BEARING.

Primary literature control: Labute/Demuškin classification and Mináč–Rogelstad–Tân Zassenhaus-dimension results were checked. Detailed audit: research/PAPER3_MIXED_DEMUSHKIN_ADMISSIBILITY_RECONSTRUCTION_AUDIT_2026-10-01.md.

Next authorized action: formalize the reconstruction lemma and independently verify naturality/projective covariance of the extension-window→Mixed Fox map. No large Fox computation is authorized.



## 2026-10-02 — MIXED FOX DEMUŠKIN PAIR DESCENT / NATURALITY BOUNDARY

The admissibility/fiber prerequisite was advanced to a precise logical boundary.

For N_k=3^{k-1}+1 and the standard odd-p fixed-rank Demuškin family, the canonical extension window
1 -> A_k=D_{N_k}/D_{N_k+1} -> E_k=G/D_{N_k+1} -> Q_k=G/D_{N_k} -> 1
is determined up to extension-window isomorphism by the bare pair (Q_k,A_k):

- q<N_k is recovered from the first q-dependent intrinsic Zassenhaus graded defect below N_k;
- q=N_k is distinguished from q>N_k by the boundary-layer dimension of A_k;
- q>N_k (including q=0) yields the same truncated extension window.

This is a Demuškin-restricted reconstruction statement and does not contradict the already CLOSED broad arbitrary-central-extension no-go.

Critical logical correction: singleton fibers establish descent of an isomorphism-invariant object assignment, but do not automatically produce a functorial section on arbitrary pair morphisms. The mixed Fox construction on extension windows is therefore classified as PASS/LOCAL for covariance/projective gauge, while the full natural-transformation factorization through a formally specified Pair_k morphism category remains OPEN.

Classification:
- Demuškin pair -> extension-window reconstruction: PASS/CLOSED at isomorphism-class scope;
- extension-window -> projective mixed Fox jet: PASS/LOCAL;
- bare pair -> mixed Fox jet as an isomorphism-invariant assignment: PASS/LOCAL;
- full categorical naturality/functorial factorization: OPEN;
- arbitrary-extension pair descent: FAIL/CLOSED;
- Paper 3: FROZEN/COMPLETE.

Independent literature control used Labute/Demuškin classification and Mináč–Rogelstad–Tân Zassenhaus-dimension results; Fox/Lyndon relation-module covariance remains the standard structural mechanism, while the project-specific finite-pair factorization is not claimed as prior literature.

Detailed audit:
research/PAPER3_MIXED_DEMUSHKIN_PAIR_DESCENT_NATURALITY_AUDIT_2026-10-02.md

Next authorized action: formalize and independently verify the projective mixed-Fox covariance under extension-window isomorphism, Nielsen/generator change, relation-generator gauge, relator conjugation, and mixed maximal-ideal truncation. No W_11/W_12, large Fox, 45-dimensional, or Paper 2 reproof computation.


## 2026-10-02 — MIXED FOX NATURALITY / REDUNDANCY FINAL DECISION

The remaining Mixed Fox naturality attack was completed at the intrinsic scope.

Critical correction: the earlier q=N_k case was vacuous. In the standard odd-p Demuškin family q=p^s or 0, whereas N_k=p^{k-1}+1 is not a p-power. The genuine cases are q<p^k, where q is detected below N_k, and q>=p^k (or q=0), where the q-term is invisible through the window and the truncated window collapses.

For filtered finite-pair isomorphisms, Demuškin reconstruction plus classification gives extension-window isomorphism, and the projective mixed Fox construction is invariant under induced group-algebra transport, Fox/Lyndon relation-module equivalence, Nielsen Jacobians, relation-generator gauge, relator conjugation, and mixed truncation.

Status:
- pair -> extension-window reconstruction: PASS/CLOSED;
- pair-isomorphism covariance: PASS/CLOSED;
- finite-pair -> projective Mixed Fox object: PASS/LOCAL;
- arbitrary non-invertible Pair_k functoriality: OPEN, not load-bearing for intrinsic isomorphism-class well-definedness;
- Mixed Fox as genuinely new recognition carrier: FAIL/CLOSED — REDUNDANT;
- genuinely new carrier: OPEN.

The non-redundancy closure is category-relative: at fixed rank in the standard Demuškin family, the finite window carries the same q-regime information already used by the frozen orientation/Kummer selector. Recovering chi mod p^k through q/classification is not a new bridge. This closes only the Mixed Fox new-recognition branch, not the validity of the finite projective Fox object itself.

Important: do not reopen q=N_k, W_11/W_12, large Fox scans, or Paper 2. Next authorized action is a genuinely different finite-input carrier search, beginning with Object/Input/Functoriality/Gauge/Orientation bridge/q-blindness/Separation/Novelty/Stop.


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

## 2026-10-02 — CRITICAL REVIEW OF EXTERNAL LEDGER INTERPRETATION

The external critique was independently checked against the latest Mixed Fox and discovery-ladder records. It contains useful methodological discipline but also several stale or overstrong next-step suggestions.

Accepted: the O_k quotient diagnosis; the need to distinguish quotient-initiality from any terminal/minimality claim; explicit evidence requirements; and the need to formalize any proposed carrier category before making categorical universal claims.

Rejected/corrected: (i) direct Fox-jet -> chi is not the next Mixed Fox task because that bridge was already established locally; the branch closed later on category-relative redundancy; (ii) q-blindness should not be defined by replacing q with 0, since q=0 is itself an admissible Demushkin regime and substitution changes the object; (iii) p=2/non-standard Demushkin reopening is not currently authorized; (iv) status labels must remain, but may never substitute for equations, counterexamples, literature theorems, or reproducible computations.

Classification:
- ledger methodological review: PASS / LOCAL;
- admissible-carrier category proposal: OPEN / NOT LOAD-BEARING;
- direct Fox -> chi as next Mixed Fox task: HISTORICAL / SUPERSEDED;
- q->0 definition of q-blindness: FAIL / CLOSED;
- p=2/non-standard extension now: CONDITIONAL / NOT AUTHORIZED;
- evidence-type rule: PASS / LOCAL;
- genuinely new finite-input carrier: OPEN / LOAD-BEARING.

Detailed audit: research/PAPER3_POST_EXPLORATION_CRITICAL_REVIEW_2026-10-02.md


## 2026-10-02 — TOP-DOWN ORIENTATION IDENTIFIABILITY REFRAME

The post-Paper-3 search is deliberately reversed at framework level. Instead of inventing a finite carrier and testing whether it recovers orientation, first fix the target chi_k=chi mod p^k and ask whether it is identifiable from the declared finite input W_k at all.

Define W_k-equivalence by finite-input isomorphism. The decisive gate is whether W_k(G)≅W_k(H) can occur with chi_G mod p^k != chi_H mod p^k. A positive counterexample is a carrier-independent no-go theorem: no carrier constructed solely from W_k can recover chi_k. If identifiability holds, define the target-induced observable partition as a benchmark and then search for an intrinsic realization that does not use chi in its definition.

This is not a new O_k universal-property claim. It is a target-first inverse/observability formulation. The existing extension-fiber analysis becomes evidence for or against identifiability, while Mixed Fox becomes only one historical realization attempt.

Classification:
- top-down identifiability framework: PASS / LOCAL;
- finite-window orientation identifiability: OPEN / LOAD-BEARING;
- target-defined coarsest quotient: CONDITIONAL / specification;
- observability depth: OPEN;
- new carrier construction before identifiability: NOT AUTHORIZED.

Detailed audit: research/PAPER3_POST_EXPLORATION_TOP_DOWN_ORIENTATION_IDENTIFIABILITY_2026-10-02.md


## 2026-10-02 — TOP-DOWN T0 CRITICAL CORRECTION / TARGET IDENTIFICATION GATE

The external review found a substantive error in the first top-down T0 attempt. The carrier-independent no-go lemma and the \(I_k(w)\) identifiability criterion are correct, but the attempted Demuškin T0 closure was invalid.

The invalid step was the implicit identification
\[
\theta(x_2)=(1-q)^{-1}
\quad\Longrightarrow\quad
\chi_G\bmod p^k=(1-q)^{-1}
\]
where \(\theta\) is a Labute crossed-derivation/coefficient twist attached to the chosen presentation, while \(\chi_G\) is intended as an intrinsic Demuškin/cyclotomic orientation target. No explicit theorem connecting these objects under the declared target convention had been supplied.

Consequences:
- previous Demuškin T0 PASS/CLOSED: **HISTORICAL / SUPERSEDED — invalid inference**;
- target identification T-1: **OPEN / LOAD-BEARING**;
- Demuškin finite-window T0: **OPEN / LOAD-BEARING**;
- broad orientation identifiability: **OPEN / NOT PROVED**;
- broad extension reconstruction: **FAIL / CLOSED** remains valid;
- observability-depth monotonicity: **OPEN**;
- automatic monotonicity from filtration functoriality: **FAIL / CLOSED**.

The algebraic q-regime facts survive:
\(q=p^s,\ s\ge k\Rightarrow q>N_k=p^{k-1}+1\), and \((1-q)^{-1}\equiv1\pmod{p^k}\). But this scalar congruence is not itself a statement about the intrinsic orientation character.

The repository literature gate already records:
- Labute: full-group crossed-derivation/Kummerian orientation criterion;
- Efrat–Quadrelli: unique Kummerian orientation for torsion-free Demuškin groups;
- Quadrelli–Weigel: cyclotomic/dualizing orientation results;
- none of the audited results, by themselves, supplies the project's finite-window factorization \(\chi_k=\Phi_k\circ W_k\).

A new correction audit was added:
research/PAPER3_TOP_DOWN_T0_CORRECTION_2026-10-02.md

Decision: do not construct a new carrier before T-1 and T0 are closed. The next mathematical task is to fix the target object basis-free/intrinsically and establish the exact relation, if any, among Demuškin orientation, cyclotomic orientation, and the Labute coefficient twist.


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


## 2026-10-02 — 2-GENERATOR FILTERED EXTENSION DEFECT: CARRIER FOUND

The proposed relation-module route was critically corrected. The q-correction \(v^q\) should not be identified with a class of \(\operatorname{gr}_q(R)\): the relator \(r=[w,v]v^{-q}\) has initial Zassenhaus degree 2, while \([w,v]\notin R\), so subtracting the degree-2 term does not produce an element of the relation subgroup.

The correct intrinsic carrier is the central extension
\[
1\to A_n=D_n/D_{n+1}\to W_{n+1}\to W_n\to1
\]
and its commutator defect \(\kappa_n\) when \(W_n\) is abelian. For
\[
G=\langle v,w\mid wvw^{-1}=v^{1+q}\rangle,
\]
one has \(G'=\overline{\langle v^q\rangle}\subseteq D_q\). Hence \(W_n\) is abelian for \(n\le q\), \(\operatorname{im}\kappa_n=0\) for \(n<q\), and
\[
\operatorname{im}\kappa_q
=G'D_{q+1}/D_{q+1}
=\mathbf F_p\overline{v^q}.
\]
Thus q is intrinsically the first nonzero extension-commutator degree.

The restricted q-power operation then isolates the origin line:
\[
\{x\in L_1:P_q(x)\in\operatorname{im}\kappa_q\}
=\mathbf F_p\bar v
\]
in the rank-2 model. The sinkhole is therefore canonically determined only as the quotient direction \(L_1/\mathbf F_p\bar v\); a canonical complementary line has not been established.

The former gauge obstruction remains rejected. Under the standard convention the sinkhole is \(w\), \(\theta(v)=1\), \(\theta(w)=1+q\), and \(v\mapsto v^a,\ w\mapsto v^cw\) preserves \(\theta\).

Classification:
- intrinsic extension-commutator carrier: **PASS / LOCAL**;
- q first-defect detection: **PASS / LOCAL**;
- origin-line recognition: **PASS / LOCAL**;
- canonical sinkhole line: **CONDITIONAL**;
- naive \(\operatorname{gr}(R)\) q-correction: **FAIL / CLOSED — WRONG OBJECT**;
- gauge orientation obstruction: **FAIL / CLOSED**;
- standard 2-generator orientation bridge: **PASS / LOCAL**;
- general multi-special-edge separation: **OPEN / LOAD-BEARING**.

Detailed audit: research/PAPER3_RAAG_2GEN_FILTERED_EXTENSION_DEFECT_AUDIT_2026-10-02.md.

Next authorized action: smallest genuinely multi-special-edge configuration, with no large computation until object/functoriality/gauge/orientation-bridge/q-blindness/separation/novelty/stop are rechecked.

## 2026-10-02 — 3-VERTEX COMMON-SINK MULTI-EDGE TEST

The smallest multi-special-edge commuting-origin model
\[
\langle v_1,v_2,w\mid[v_1,v_2]=1,;wv_iw^{-1}=v_i^{1+q}\rangle
\]
was checked directly. Its degree-q extension commutator defect has image
\(\operatorname{span}\{v_1^q,v_2^q\}\), and the restricted q-power operation recovers the ordinary/origin plane. Since the ambient degree-one space has dimension three, the quotient is the one-dimensional sinkhole direction. Hence the filtered extension mechanism survives the first genuine multi-edge test.

The critical failure boundary is now explicit: if ordinary origins have nontrivial degree-2 commutators, then \(W_q\) is not abelian and the simple extension commutator pairing on \(W_q\) cannot be used directly. The general problem is therefore a **degree-2 ordinary sector separation → degree-q extension defect** construction.

Classification:
- 3-vertex common-sink mechanism: PASS / LOCAL;
- general RAAG directed/sinkhole separation: OPEN / LOAD-BEARING.

Detailed audit: research/PAPER3_RAAG_3VERTEX_COMMON_SINK_AUDIT_2026-10-02.md.

## 2026-10-02 — NON-ABELIAN (W_q) WALL REFINED / SPECIAL-PLANE INCIDENCE CARRIER

The previous critical boundary was refined. It is correct that a non-abelian (W_q) prevents defining a global bilinear commutator pairing
[
kappa_q:W_q	imes W_q	o D_q/D_{q+1},
]
but it is too strong to conclude that the intrinsic extension-defect method is unavailable.

For commuting pairs in (W_n), the commutator lift is canonically defined modulo (D_{n+1}), because changing a lift by (D_n) changes the commutator by ([D_n,D_1]subseteq D_{n+1}). To remove contamination from pairs with the same degree-one direction and deep corrections, the defect is organized by (2)-planes (Ule L_1) and their first nonzero commutator-survival degree
[
ho(U).
]

The smallest non-abelian-origin special model
[
G=langle x,y,zmid xyx^{-1}=y^{1+q}, xzx^{-1}=z^{1+q}angle
]
was analyzed. The origin subgroup (langle y,zangle) is free pro-(p), so (2)-planes contained in its degree-one span have ordinary degree-2 commutator survival. By contrast, planes (operatorname{span}(ar x,u)) with (0
e uinoperatorname{span}(ar y,ar z)) have first survival degree (q). If (operatorname{span}(ar x+v,u)) has independent (v,u) in the origin plane, its degree-2 commutator is nonzero, so it is not a (q)-special plane.

Hence the local (q)-special Grassmannian is precisely the incidence family of the sinkhole line with its origin plane. If the origin plane has dimension at least two, its intersection is the sinkhole line.

This is a genuine advance over the commuting-origin test because it survives the first model in which the degree-2 ordinary commutator sector is nontrivial.

Classification:
- global bilinear (kappa_q) on non-abelian (W_q): FAIL / CLOSED — wrong domain;
- lift-independent commuting-pair defect: PASS / LOCAL;
- (2)-plane first-survival carrier: PASS / LOCAL;
- noncommuting-origin special-line test: PASS / LOCAL;
- sinkhole incidence recovery for common sink with at least two independent origins: PASS / LOCAL;
- general special-graph incidence theorem: OPEN / LOAD-BEARING;
- accidental (q)-special plane exclusion: OPEN / LOAD-BEARING.

Detailed audit: research/PAPER3_RAAG_SPECIAL_PLANE_INCIDENCE_AUDIT_2026-10-02.md.

Next authorized action: prove/refute the accidental-plane exclusion theorem for arbitrary specially oriented graphs. If it passes, reconstruct sinkhole/source incidence from the special-plane family; if it fails, retain the explicit counterexample as the new obstruction. No large computation or reopening of frozen branches.

## 2026-10-02 — ACCIDENTAL-PLANE EXCLUSION REFUTED / SPECIAL-PLANE CARRIER CLOSED

The active Gate D was pursued to completion. The theorem excluding accidental q-special 2-planes is false on the full specially oriented RAAG class.

Counterexample:
[
G=langle s,a,bmid asa^{-1}=s^{1+q},;bsb^{-1}=s^{1+q},;[a,b]=1angle,
]
with (s) the unique special/sinkhole vertex and (a,b) ordinary. This is a complete specially oriented graph, a class explicitly allowed in the literature. citeturn0search0

Since the underlying graph is complete, all degree-2 commutators vanish. Therefore the extension defect at degree (q) is represented intrinsically by an alternating form (B_q) on (L_1), with
[
B_q(a,s)=s^q,quad B_q(b,s)=s^q,quad B_q(a,b)=0.
]
Its radical is (mathbf F_p(a-b)). The q-special 2-planes are exactly those not containing this radical. In particular
[
U_1=langle s,aangle,qquad U_2=langle s+a,bangle
]
are both q-special while (U_1cap U_2=0). Hence the intersection of all q-special planes is zero, not the sinkhole line.

This directly refutes the proposed accidental-plane exclusion and the claimed general sinkhole recovery from (mathscr S_q).

The failure mechanism is structural: when the ordinary-neighbor sector is abelian, degree-2 separation disappears and the q-defect becomes an alternating form whose Grassmannian support detects its radical rather than the sinkhole.

Classification:
- accidental q-special-plane exclusion: **FAIL / CLOSED**;
- special-plane first-survival carrier: **FAIL / CLOSED**;
- sinkhole recovery by (mathscr S_q): **FAIL / CLOSED**;
- noncommuting-origin local mechanism: **PASS / LOCAL** only under its explicit hypothesis;
- general directed/sinkhole separation by this carrier: **FAIL / CLOSED**;
- alternative intrinsic carrier: **OPEN**.

Detailed audit: research/PAPER3_RAAG_SPECIAL_PLANE_INCIDENCE_AUDIT_2026-10-02.md.

The carrier branch is frozen. No additional (mathscr S_q) computation is authorized.

## 2026-10-02 — RP-3 NON-REENCODING AUDIT COMPLETED

The q-blind adjacent-window carrier was subjected to the required non-reencoding audit.

Definition:
\[
e(Z)=\log_p\exp(Z^{ab}),\qquad
\mathcal L(X,Y)=
\begin{cases}
\operatorname{im}(\operatorname{Hom}(Y,\mathbf Z/p^{e(Y)})\to\operatorname{Hom}(Y,\mathbf F_p)),&e(Y)>e(X),\\
0,&e(Y)=e(X).
\end{cases}
\]

For the specially oriented RAAG jump at \(q=p^f\),
\[
W_q^{ab}\cong(\mathbf Z/q)^V,qquad
W_{q+1}^{ab}\cong(\mathbf Z/pq)^{V\setminus S}\oplus(\mathbf Z/q)^S,
\]
so
\[
\mathcal L(W_q,W_{q+1})=\ker\beta_f,
\qquad
\mathcal L(W_q,W_{q+1})^\perp=\operatorname{span}\{\bar s:s\in S\}.
\]

The decisive non-reencoding test is that, for fixed p, rank |V|, and sinkhole count |S|, the abstract carrier has dimension |V|-|S| independent of f. Hence it cannot encode q or the full coefficient \((1-q)^{-1}\bmod p^k\). Distinct q-regimes therefore yield isomorphic carrier types. This is a genuine recognition carrier, not a q-labelled encoding.

However, it is target-relative: on the declared family it is exactly the Bockstein-kernel predicate. It should not be advertised as a new independent invariant or a full-orientation carrier.

Independent verification:
1. Smallest non-complete model \(G=\langle a,s,b\mid sas^{-1}=a^{1+q}\rangle\):
\[
G^{ab}\cong\mathbf Z_p\langle s\rangle\oplus\mathbf Z_p\langle b\rangle\oplus(\mathbf Z/q)\langle a\rangle,
\]
hence \(\mathcal L=\operatorname{span}\{\bar s^*,\bar b^*\}\) and \(\mathcal L^\perp=\mathbf F_p\bar a\). PASS/LOCAL.
2. Multiple sinks: \(\mathcal L\) is the free/non-sinkhole character subspace and its annihilator is the full sinkhole span. PASS/LOCAL.
3. All-sinkhole case: no exponent jump, so \(\mathcal L=0=\ker\beta_f\). PASS/LOCAL.
4. Full orientation from \(\mathcal L\) alone fails because the carrier type is q-independent. FAIL/CLOSED.
5. Full arbitrary pair-morphism functoriality is not claimed; isomorphism covariance is sufficient for the present intrinsicity statement. OPEN/NOT LOAD-BEARING.
6. Absolute minimality/coarseness is not established.

Literature control: Blumer–Quadrelli–Weigel define oriented pro-\ell RAAGs from oriented graphs and give the canonical orientation as 1 on ordinary vertices and \(\lambda(1)\) on special vertices; this supports the declared special/sinkhole convention but does not state the project-specific finite-window carrier theorem. citeturn1view0

Classification:
- q-blind kernel/annihilator carrier: PASS / LOCAL;
- q-non-reencoding: PASS / LOCAL;
- smallest non-complete and multiple-sink checks: PASS / LOCAL;
- full orientation from carrier alone: FAIL / CLOSED;
- full \(\beta_f\) reconstruction: OPEN / NOT LOAD-BEARING;
- arbitrary morphism-level functoriality: OPEN / NOT LOAD-BEARING;
- absolute minimality: OPEN / NOT AUTHORIZED;
- graph-directed incidence refinement: OPEN.

Detailed audit: research/RP3_NONREENCODING_AUDIT_2026-10-02.md


## 2026-10-02 — RP-4 CRITICAL RE-AUDIT: EXTENSION DEFECT NOT ABELIANIZATION-FACTOR

The proposed RP-4 closure was critically rechecked against the authoritative filtered-extension results. Two claims in the draft are false.

First, the working definition
\\[
\\mathcal C\\text{ graph-sensitive}\\iff \\mathcal C\\text{ does not factor through abelianization}
\\]
is too strong. Same-abelianization separation is the actual criterion B. Abelianization factorization implies failure of B, but non-factorization does not imply B.

Second, the claim that the Zassenhaus extension commutator defect \\(\\kappa_n\\) is an abelianization factor is false. In the rank-2 special-edge model
\\[
G=\\langle v,w\\mid wvw^{-1}=v^{1+q}\\rangle,
\\]
\\(G'\\subseteq D_q\\), hence \\(\\operatorname{im}\\kappa_n=0\\) for \\(n<q\\) and
\\[
\\operatorname{im}\\kappa_q=\\mathbf F_p\\overline{v^q}\\ne0.
\\]
The draft's claimed nonzero class in \\(D_2/D_3\\) is wrong for odd \\(p\\), because \\(v^q\\in D_q\\subseteq D_3\\) for \\(q\\ge3\\). The extension class/commutator defect depends on the multiplication of \\(W_{n+1}\\), not only on \\(G^{ab}\\).

Therefore the previously written RP-4 FAIL/CLOSED conclusion is HISTORICAL / SUPERSEDED. The correct boundary is:
- raw central extension/commutator defect: PASS / LOCAL in the audited models;
- Grassmannian special-plane extraction: FAIL / CLOSED;
- claim that \\(\\kappa_n\\) is abelianization-only: FAIL / CLOSED — FALSE CLAIM;
- full extension-class carrier: OPEN / LOAD-BEARING;
- general graph-incidence separation: OPEN / LOAD-BEARING.

A corrected audit was recorded as research/RP4_EXTENSION_DEFECT_REAUDIT_2026-10-02.md. RP-5 is therefore a legitimate next branch, but only after an explicit pre-check of the actual finite central extension \\(E_n=W_{n+1}\\to W_n\\), its extension class in \\(H^2(W_n,A_n)\\), q-blind first-defect detection, and same-abelianization separation. No large computation is authorized before that pre-check.


## 2026-10-02 — RP-5 LOCAL SEPARATION RESULT

RP-5 produced a four-vertex same-abelianization separation pair. Graph A has special edges (a,s),(b,s); Graph B has (a,s),(b,t); no ordinary edges. Both have abelianization (Z/q)^2 + Z_p^2. At the first q-defect layer, the intrinsic origin plane is recovered by the q-power preimage of the defect image. In this control family the complementary special plane is recovered from the degree-2 centralizer. The cross q-extension defect has rank 1 for A and rank 2 for B. Therefore criterion B is PASS / LOCAL: filtered extension data are genuinely graph-sensitive. Full directed-incidence recovery remains OPEN / LOAD-BEARING.

Important convention correction: in the audited literature, a special edge (v,w) has ordinary origin v, special terminus w, and relation w v w^{-1}=v^(1+q). Thus v is q-torsion in abelianization and w is free. Earlier RP-3 text identifying the torsion/annihilator sector with the special/sinkhole vertices is reversed under this convention and requires a separate correction audit.

Detailed audit: research/RP5_NONABELIAN_EXTENSION_CLASS_AUDIT_2026-10-02.md


## 2026-10-02 — CONVENTION CORRECTION AUDIT COMPLETED

Independent literature verification confirms that for a special edge (v,w), v is the ordinary origin, w is the special terminus, and wvw^{-1}=v^{1+q}. Hence v^q=1 in abelianization. The earlier RP-3 use of the special/sinkhole set as the torsion/annihilator sector was reversed.

Correction consequence:
- O = ordinary origins of special edges = q-torsion directions;
- S = special termini/sinkholes = non-torsion directions from the special-edge relation;
- G^ab = (Z/q)^O ⊕ Z_p^(V\O);
- at the first adjacent jump, the exponent-jump annihilator recovers span(O), not span(S).

The RP-3 q-blind carrier architecture survives locally, but any bridge from the recovered origin sector to the special/sinkhole sector is a separate theorem and is not assumed. RP-5 is unaffected because its current notation already uses O for origins and S for special termini.

Classification: CONDITIONAL CORRECTION / SUPERSEDES EARLIER LABELS.
Detailed audit: research/CONVENTION_CORRECTION_AUDIT_2026-10-02.md.


## 2026-10-02 — PAPER 4 EXACT-DEPTH CENTRALIZER-JUMP CARRIER

The ordinary-contamination gate was sharpened. A global quotient of the degree-2 sector is rejected as the primary abstraction. For u in L_1=D_1/D_2 define intrinsic filtration centralizers C_m(u)={x:[u~,x~] in D_m} and the exact-depth jump J_m(u)=C_m(u)/C_{m+1}(u). An ordinary edge has infinite commutator depth, a nonedge has degree 2, and a special edge has exact depth q; hence ordinary edges disappear from the q-jump without a presentation-dependent quotient.

Explicit checks: mixed ordinary/special model gives J_q(a)=F_p s and J_q(b)=0; RP-5 A gives J_q(a)=J_q(b)=F_p s; RP-5 B gives J_q(a)=F_p s and J_q(b)=F_p t; the complete one-sink model gives J_q(a)=J_q(b)=F_p s. Thus RP-5 separation survives in a stronger exact-depth form.

The remaining load-bearing issue is linear-combination cancellation. Quadrelli's 2024 analysis gives essential q-fold Massey obstructions for linear combinations such as u*+v*, so higher-q behaviour of non-basis directions is a genuine issue, not a technicality. citeturn14view0turn13view0

Classification: global W_2 ordinary quotient = **FAIL / CLOSED as primary abstraction**; exact-depth J_m = **PASS / LOCAL**; ordinary/special separation = **PASS / LOCAL**; RP-5 strengthened separation = **PASS / LOCAL**; q-blind local definition = **PASS / LOCAL**; linear-combination purity = **OPEN / LOAD-BEARING**; arbitrary incidence reconstruction = **OPEN**.

Detailed record: research/PAPER4_EXACT_DEPTH_CENTRALIZER_JUMP_AUDIT_2026-10-02.md.


## 2026-10-02 — PAPER 4 ORIGIN-CONDITIONED DEFECT CANDIDATE AUDIT

Candidate 1, the raw origin-restricted pairing \(B_q|_{O\times L_1}\), fails the intrinsicity pre-check in the general nonabelian case. A lift change by \(D_2\) produces a commutator correction in \([D_2,D_1]\subseteq D_3\), so there is no general lift-independent value in \(D_q/D_{q+1}\). This is a genuine definition-level obstruction, not an ordinary-edge issue.

A corrected object survives: for each adjacent window \(E_n:1\to A_n\to W_{n+1}\to W_n\to1\), use the q-blind RP-3 origin sector \(O_n\subset L_1\), form its canonical preimage \(H_n(O)\le W_n\), and restrict the finite extension to \(H_n(O)\). The resulting extension class is intrinsic and gauge-independent. Its actual centralizer commutator defect is likewise well-defined because the kernel \(A_n\) is central in \(W_{n+1}\).

RP-5 retains the rank-1/rank-2 separating signal, and the mixed ordinary/special model retains zero ordinary-edge defect versus nonzero special-edge defect. These remain local checks, not a general incidence theorem.

Classification: raw pairing **FAIL / CLOSED**; restricted origin extension **PASS / LOCAL**; canonical degree-one extraction **OPEN / LOAD-BEARING**; arbitrary directed incidence **OPEN / LOAD-BEARING**.

Detailed audit: research/PAPER4_ORIGIN_CONDITIONED_DEFECT_AUDIT_2026-10-02.md.


## 2026-10-02 — PAPER 4 T1 LOCAL-UNIFORM NORMALIZATION CANDIDATE

The T1 target has now produced a concrete target-first construction rather than another carrier search.

Literature control: Blumer–Quadrelli–Weigel show that for a special edge (v,w), the 2-generator subgroup is locally uniform and its canonical orientation is determined by the locally uniform group structure; Proposition 4.11 extends this structural orientation determination to clique subgroups. Theorem 4.9 identifies the canonical orientation as the unique torsion-free Kummerian orientation for specially oriented graphs. citeturn5search0turn0search0

Project transfer: define, from the adjacent finite window and the already established origin sector O_q, a q-blind set P_q in U_q=L_1/O_q consisting of classes admitting a finite special-edge local signature at the first nonzero extension-defect depth. The signature is intended to be intrinsic: rank-one first defect, special-edge semidirect type, and normalization against the restricted q-power class. The desired conclusion is P_q={special-vertex directions} and hence a unique functional omega_q with omega_q(P_q)=1.

This is materially different from the failed J_q(u) != 0 criterion: arbitrary q-active linear directions are not automatically admitted; the test requires a compatible 2-generator special-edge signature. In the 2-generator, complete one-sink, and common-sink controls, the local mechanism yields the correct normalized quotient direction. These are PASS / LOCAL only.

New audit: research/PAPER4_T1_LOCAL_UNIFORM_DIRECTION_AUDIT_2026-10-02.md.

Classification:
- literature method transfer: PASS / LOCAL;
- T1 local-uniform finite signature: OPEN / LOAD-BEARING;
- 2-generator normalization: PASS / LOCAL;
- complete one-sink and common-sink normalization: PASS / LOCAL;
- accidental-direction exclusion: OPEN / LOAD-BEARING;
- finite-window naturality: OPEN / LOAD-BEARING;
- T1: OPEN / LOAD-BEARING.

The active question is now theorem-level and sharply bounded: does the finite window intrinsically recognize the normalized special-direction set without reconstructing the full directed graph? No new carrier family is authorized before this gate is resolved.


## 2026-10-02 — PAPER 4 T1 SCALE-FIXING / MULTI-SINK AUDIT

Critical correction accepted: 2-generator coefficient observability does not by itself prove canonical normalization. The common-sink calculation sharpens the issue. In the model with origins v_i and one sink w, B_q(w,v_i)=overline{v_i^q}; replacing w by lambda w multiplies every target by lambda. Therefore, once the restricted-power target is intrinsically identified, lambda=1 is forced. This proves local scale fixing relative to an intrinsic q-power target, but not recovery of that target in an arbitrary abstract window.

Separated multi-sink control: for u=sum alpha_j w_j, pairing against an origin attached only to sink j detects alpha_j. If at least two independent sink sectors occur, a generic sum has rank >=2 and is excluded from the rank-one special-edge signature. Sink permutation symmetry preserves the desired all-ones functional, while a shear w_1 -> w_1+c w_2 is detected by the origin-specific defect in the separated model.

The T1 target is therefore reformulated as an intrinsic affine set S_q of normalized sink vectors, selected by rank-one special-edge defects whose targets are restricted-power classes of O_q. Then omega_q is defined by omega_q(s)=1 on S_q. No arbitrary projective/basis normalization is permitted.

New bottlenecks:
1. recover the intrinsic q-power target q-blindly from the adjacent window;
2. exclude accidental rank-one directions in overlapping multi-sink configurations;
3. prove filtered-isomorphism invariance of S_q.

Detailed audit: research/PAPER4_T1_MULTI_SINK_SCALE_AUDIT_2026-10-02.md.

Classification:
- coefficient observability: PASS / LOCAL;
- local scale fixing relative to intrinsic q-power target: PASS / LOCAL;
- separated multi-sink rank test: PASS / LOCAL;
- intrinsic q-power target: OPEN / LOAD-BEARING;
- accidental-direction exclusion: OPEN / LOAD-BEARING;
- T1: OPEN / LOAD-BEARING.

Next authorized attack: smallest overlapping multi-sink model. No new carrier hunt.


## 2026-10-02 — PAPER 4 GATE D1 FORMALIZATION: GLOBAL LOWER-FILTRATION SIGNATURE

The current D1 target was formalized without returning to carrier hunting.

For an adjacent finite window E: 1→A=D_n/D_{n+1}→Y=W_{n+1}→X=W_n→1, with L_1=X/Φ(X), define the full attainable commutator-depth relation over all lifts. Equivalently, for u∈L_1, define the global signature L_E(u)=(R_m(u))_m, where R_m(u) is the set of all x∈L_1 admitting lifts whose commutator lies in D_m(Y).

This is explicitly a global signature across all degree-one directions and all filtration depths, not a selected pairwise q-defect and not a bilinear map into D_q/D_{q+1}. Complete lift-fiber quantification gives presentation/lift/gauge independence; filtered isomorphisms transport it; no displayed q, basis, section, presentation, or orientation enters the definition. Hence D1 passes the definition-level Object/Input/Functoriality/Gauge/q-blindness/non-tautology checks.

Independent controls confirm the intended boundary: the rank-two special edge has first special depth q; the long ordinary-chain profile distinguishes special from lower-degree-contaminated directions; the separated two-sink model shows that D1 can detect local q-defects without identifying literal sink directions; the isolated-special same-window obstruction remains a separate unrestricted Gate-D no-go.

Classification: global lower-filtration signature = PASS / LOCAL; intrinsicity/gauge independence = PASS / LOCAL; filtered-isomorphism covariance = PASS / LOCAL; q-blindness = PASS / LOCAL; non-tautological definition = PASS / LOCAL; linearity/subspace structure = OPEN / LOAD-BEARING; canonical quotient N_q = OPEN / LOAD-BEARING; orientation bridge = OPEN / LOAD-BEARING; unrestricted Gate D = FAIL / CLOSED.

Detailed audit: research/PAPER4_D1_GLOBAL_LOWER_FILTRATION_SIGNATURE_AUDIT_2026-10-02.md.

Next authorized action: D2 only, extracting a quotient from relations among the full signatures. Do not define N_q as the span of q-invisible directions and do not reopen the closed affine/profile carriers.
\n\n## 2026-10-02 — PAPER 4 D2 SIGNATURE-RELATION QUOTIENT NO-GO

The authorized D2 attack was completed.

D1 defines the global lower-filtration depth signature
\[
S_E(u)=\mathcal L_E(u)=(\mathscr R_m(u))_m,
\]
which records attainable commutator depths but not the nonzero leading coefficient.

The decisive rank-two special-edge model
\[
G=\langle v,w\mid wvw^{-1}=v^{1+q}\rangle
\]
shows that for every \(\lambda\in\mathbf F_p^\times\),
\[
S_E(\lambda\bar w)=S_E(\bar w),
\]
while
\[
\omega_q(\lambda\bar w)=\lambda\ne1=\omega_q(\bar w)
\]
for \(\lambda\ne1\). Hence the canonical orientation cannot factor through the D1 signature, nor through any quotient/relation object whose information is exhausted by those signature values.

This is a stronger obstruction than the earlier chordal-tree kernel result: D1 already loses scalar normalization before any quotient is formed.

Independent controls:
- separated two-sink: nonzero scalar multiples of each sink direction have identical depth signatures, while their orientation values scale;
- chordal tree: the coefficient-valued incidence relation \(u-s-t\) lies in the q-defect kernel but has \(\omega_q(u-s-t)=-1\ne0\), so simply restoring coefficients via the incidence package does not produce an orientation quotient.

Therefore:
- D1 depth signature: **PASS / LOCAL**;
- D2 quotient from relations among D1 signatures: **FAIL / CLOSED**;
- D2 orientation factorization through D1: **FAIL / CLOSED**;
- coefficient-valued incidence quotient as orientation carrier: **FAIL / CLOSED**;
- restricted-origin coefficient-valued extension datum: **OPEN / LOAD-BEARING**;
- unrestricted Gate D: **FAIL / CLOSED**.

The next authorized step is singular: define the smallest coefficient-valued intrinsic extension object that augments D1 enough to restore scalar normalization, then run a fresh full pre-check before computation. This is not authorization for a new unconstrained carrier hunt.

Detailed audit: research/PAPER4_D2_SIGNATURE_RELATION_QUOTIENT_NO_GO_AUDIT_2026-10-02.md.

