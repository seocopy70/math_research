

## 2026-10-03 — T1-C END-OF-BRANCH AUDIT

T1-C is now at its present logical boundary. Relative Fox divisibility is established on the declared rank-two stress family; the existing finite-kernel survival witness is valid when r=floor(s/a)<s, hence in particular a>=2. Therefore the exact relative threshold p^s+1 is certified for a>=2, s>a. The a=1 boundary remains OPEN because r=s and the witness becomes p^s z=0.

The intrinsic unmarked problem remains OPEN/LOAD-BEARING. The obstruction is defined on the marked extension 1->K_n->W_n->D/D_n(D)->1; canonical reconstruction from abstract W_n has not been proved, and no admissible same-window separation pair has been found. Thus neither intrinsic factorization nor no-go is established.

Closed routes are not to be reopened: degree-5 residual modulo ad_x2, scalar/coinvariant/norm collapse, blind carrier construction, and transfer of the RAAG orientation counterexample.

Next authorized gates: (A) an independent actual finite-kernel witness for a=1, or (B) an unmarked reconstruction/separation theorem. No repeat of closed Fox calculations.

Classification: relative threshold PASS/CLOSED for a>=2,s>a; a=1 OPEN; intrinsic reconstruction OPEN/LOAD-BEARING; same-window separation OPEN; coarsest intrinsic compression OPEN; universal theorem OPEN; blind carrier search STOP.
## 2026-10-03 — T1-C SCOPE CORRECTION: a=1 SURVIVAL GAP / NONBOUNDARY TEST

Critical re-audit found a genuine load-bearing error in the current T1-C generalization. The integral Fox divisibility calculation itself permits all s>a>=1, but the stated metabelian survival witness uses r=floor(s/a) and (y-1)^r z=p^r z !=0 in C_{p^s}, which requires r<s. This fails when a=1: then r=s and p^r z=p^s z=0. Therefore the metabelian quotient does NOT certify actual finite-kernel survival for the entire previously declared range a>=1.

The relative threshold theorem is consequently retained only for the nonboundary subfamily for which the existing survival argument actually works, in particular a>=2 (with s>a), pending an independent witness for a=1. The previously stated all-a>=1 PASS/CLOSED claim is superseded and must not be used.

Authorized representative nonboundary test: (p,s,a)=(3,5,2), so q=9, r=2<s=5, and n=p^s+1=244. This is deliberately chosen to avoid the a=1 boundary. The earlier (3,2,1), n=10 calculation remains valid for the degree-5 mod-p gauge test, but it is NOT a valid generic witness for the integral finite-kernel survival theorem.

Status after correction:
- integral Fox divisibility on the stress presentation: PASS / LOCAL for s>a>=1;
- actual finite-kernel survival via the stated metabelian witness: PASS / CLOSED for a>=2, OPEN for a=1;
- exact relative threshold p^s+1: PASS / CLOSED for the currently certified nonboundary subfamily a>=2; OPEN for a=1;
- unmarked intrinsic factorization: OPEN / LOAD-BEARING;
- blind carrier search: STOP / NOT AUTHORIZED.

This correction takes precedence over any older “all a>=1” threshold label.

## 2026-10-03 — T1-C UNMARKED SAME-WINDOW FINAL BOUNDARY

After the relative threshold was frozen, the required unmarked same-window separation test was taken as far as the current data permit.

No valid pair of admissible marked extension diagrams with isomorphic underlying finite windows but different relative split/non-split data has been established. The earlier RAAG same-underlying-group/different-orientation obstruction is not transferable: it changes orientation data, not the splitting class of a quotient extension. Postcomposition of the quotient map by a quotient automorphism also cannot separate split from non-split.

The stress-family pair (G_{s,a},G_{t,a}) is not a same-window counterexample at (n=p^s+1): the relative theorem detects a genuine finite-layer difference there. For (nle p^s) the windows agree and the relative extensions are both split.

Thus the correct conclusion is not a no-go and not an intrinsicity theorem. The remaining theorem is exactly the reconstruction/separation dichotomy:
[
W_{p^s+1}(G_{s,a})
stackrel{?}{longrightarrow}
left(W_{p^s+1}(G_{s,a})	o D/D_{p^s+1}(D)ight)
stackrel{?}{longrightarrow}
[	ext{extension class}].
]

Classification:
- relative threshold (n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1): **PASS / CLOSED** for the declared stress family;
- unmarked same-window no-go: **OPEN**;
- canonical reconstruction of the marked quotient: **OPEN / LOAD-BEARING**;
- intrinsic factorization/coarsest realization: **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

No threshold recomputation, degree-5 reopening, scalar/norm shortcut, or blind carrier search is authorized.

Detailed audit: research/PAPER4_T1C_UNMARKED_SAME_WINDOW_FINAL_BOUNDARY_AUDIT_2026-10-03.md.

## 2026-10-03 — T1-C INTRINSIC FACTORIZATION PRE-CHECK / UNMARKED INPUT GATE

After freezing the relative threshold theorem, a fresh target-first pre-check was run before any new carrier construction.

The target
\[
\mathsf T(W_n\to D/D_n(D))
\]
is a property of the marked extension diagram, not automatically a function of the abstract finite group \(W_n\). Forgetting the quotient map \(\pi\) removes the distinguished quotient/kernel data unless that map is canonically reconstructible from the finite window.

Consequently the unmarked Object/Input/Functoriality gates are not yet passed. This is not a no-go theorem: the proper next test is whether two admissible marked extension diagrams with different relative threshold data can have isomorphic unmarked finite windows at the same depth.

Classification:
- marked relative threshold: **PASS / CLOSED**;
- unmarked factorization: **OPEN / LOAD-BEARING**;
- unmarked same-window no-go: **OPEN**;
- coarsest intrinsic realization: **OPEN**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

Next authorized action: same-window separation at the unmarked level, not another Fox/norm/degree-5 calculation.

Detailed audit: research/PAPER4_T1C_INTRINSIC_FACTORIZATION_PRECHECK_2026-10-03.md.

## 2026-10-03 — T1-C POST-THRESHOLD CRITICAL RE-AUDIT

The general integral Fox calculation is confirmed as a genuine relative threshold theorem for the declared stress family, with one proof-packaging refinement.

For \(q=p^a\), \(s>a\), the pure-Y Fox row is \(q-Y\), so cancelling the scalar defect \(p^s\bar z\) requires \((q-Y)A(Y)=p^s\). The first nonintegral coefficient occurs at \(r=\lfloor s/a\rfloor\), giving the integral divisibility residual in the \(Y^r\bar z\) direction. The metabelian quotient \(C_{p^s}\rtimes C_{p^s}\) independently shows the corresponding finite-kernel residual is nonzero, while \(D_{p^s+1}\) is trivial there. The lower bound is closed because generator lifts give a section for every \(n\le p^s\).

A critical audit isolates the only remaining formalization point: state the pushout/naturality lemma explicitly. Section-defect cocycles and their coboundaries map functorially under equivariant kernel quotients, so nonzero survival in the metabelian pushout implies nonzero class in the original abelianized-kernel pushout. The same quotient/naturality argument must be used for the higher-rank reduction.

Classification:
- integral Fox-divisibility obstruction, declared stress family: **PASS / CLOSED**;
- finite-kernel survival: **PASS / CLOSED**;
- splitting for all \(n\le p^s\): **PASS / CLOSED**;
- exact \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\): **PASS / CLOSED**;
- universal free-by-Demushkin theorem: **OPEN**;
- intrinsic/unmarked finite-window realization: **OPEN**;
- coarsest/strict compression: **OPEN**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

Next authorized action: target-first pre-check for factorization of the relative threshold obstruction through an intrinsic finite-window object, not another threshold or Fox computation.

Detailed audit: research/PAPER4_T1C_POST_THRESHOLD_CRITICAL_REAUDIT_2026-10-03.md.

## 2026-10-02 — T1 CORRECTION COMPLETED / LOCAL PASS BUT GLOBAL AFFINE FAILURE RESTORED

The corrected full-filtered normalized locus was tested to completion on the authorized controls.

Chordal tree:
[
a	o s, b	o t, a	o u, b	o u
]
gives normalized directions (s,u,t) and hence affine hull
[
alpha+eta+gamma=1=omega_q^{-1}(1).
]
So the corrected lower-filtration + q-defect mechanism is **PASS / LOCAL** and the chordal-tree control no longer supplies a no-go.

However, the mixed ordinary control supplies a genuine global obstruction. An ordinary non-origin direction (z) with no special incidence to the origin sector has no normalized q-flat witness: nonincident pairs have lower-degree commutator, while ordinary commuting pairs have zero q-defect. Thus the corrected normalized locus does not span arbitrary (z)-directions, whereas the full canonical hyperplane (omega_q^{-1}(1)) does.

Therefore:
- old separated (s+t) counterexample: **HISTORICAL / SUPERSEDED**;
- corrected full-filtered local mechanism: **PASS / LOCAL**;
- corrected chordal-tree affine reconstruction: **PASS / LOCAL**;
- full affine-hull theorem on the orientation-rigid class OR: **FAIL / CLOSED**;
- special-incidence-sector reconstruction: **OPEN / LOAD-BEARING**;
- full orientation recovery: **OPEN**, requiring a richer nonlinear extension datum.

This is a cleaner failure than the old one. The corrected local mechanism recovers the normalization on the special-incidence sector, but it does not encode the zero extension to ordinary directions or distinguish mixed directions carrying special mass from ordinary directions.

The normal-closure conjugation action remains the authorized next structural object; the branch is not closed globally.

Detailed audit: research/PAPER4_T1_CONVENTION_CORRECTION_REOPEN_AUDIT_2026-10-02.md.

## 2026-10-02 — T1 CONVENTION CORRECTION / AFFINE-HULL REOPENED

A referee-level recheck found that the earlier separated two-sink counterexample to the T1 affine-hull theorem was invalid. The error was the assertion that the absent edge between (t) and (a) implied ([t,a]=1). In an oriented pro-(p) RAAG, absent edges impose no relation; only ordinary edges commute, while special edges impose (wuw^{-1}=u^{1+q}). The literature confirms this convention. citeturn15search0turn4search0

Therefore the old calculation
[
(st)a(st)^{-1}=sas^{-1}
]
is false. The mixed element (s+t) has lower-filtration contamination from (t) against (a), so it is not a valid normalized witness for the full filtered signature.

Consequently:
- old T1 separated (s+t) affine-hull no-go: **HISTORICAL / SUPERSEDED**;
- full-filtered normalized local locus (mathcal S_E^{flat}): **OPEN / LOAD-BEARING**;
- rank-two special-edge control: **PASS / LOCAL**;
- overlapping common-sink control: **PASS / LOCAL**;
- chordal-tree control: **OPEN / LOAD-BEARING**;
- unrestricted finite-window recovery: **FAIL / CLOSED** remains unchanged by the isolated-special same-window obstruction.

The corrected T1 target is
[
mathcal S_E^{flat}
={ar u:exists,ar xin O, [u,x]in D_q, [u,x]equiv P_E(x)pmod{D_{q+1}}},
]
with lower-filtration flatness imposed before the q-layer projection. The candidate affine theorem
[
operatorname{Aff}(mathcal S_E^{flat})stackrel{?}{=}omega_q^{-1}(1)
]
is reopened only on an orientation-rigid restricted class.

This correction also weakens the previous claim that the repaired normal-closure nonlinear action is the unique next route. The authorized order is now: chordal-tree test of (mathcal S_E^{flat}) first; only if it fails, derive the exact surviving kernel and then return to the normal-closure action.

Detailed audit: research/PAPER4_T1_CONVENTION_CORRECTION_REOPEN_AUDIT_2026-10-02.md.

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
G=langle x,y,zmid xyx^{-1}=y^{1+q}, xzx^{-1}=z^{1+q}
angle
]
was analyzed. The origin subgroup (langle y,z
angle) is free pro-(p), so (2)-planes contained in its degree-one span have ordinary degree-2 commutator survival. By contrast, planes (operatorname{span}(ar x,u)) with (0
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
G=langle s,a,bmid asa^{-1}=s^{1+q},;bsb^{-1}=s^{1+q},;[a,b]=1
angle,
]
with (s) the unique special/sinkhole vertex and (a,b) ordinary. This is a complete specially oriented graph, a class explicitly allowed in the literature. citeturn0search0

Since the underlying graph is complete, all degree-2 commutators vanish. Therefore the extension defect at degree (q) is represented intrinsically by an alternating form (B_q) on (L_1), with
[
B_q(a,s)=s^q,quad B_q(b,s)=s^q,quad B_q(a,b)=0.
]
Its radical is (mathbf F_p(a-b)). The q-special 2-planes are exactly those not containing this radical. In particular
[
U_1=langle s,a
angle,qquad U_2=langle s+a,b
angle
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



## 2026-10-02 — D2 CONVENTION CORRECTION

The separated two-sink discussion in the new D2/extension audits has been corrected: absence of an edge does not imply commutation in the oriented pro-p RAAG convention. Mixed vectors can therefore carry lower-filtration contamination. This does not change D2: the rank-two special-edge model alone proves that the D1 depth signature is scalar-blind while the canonical orientation is not. The coefficient-valued extension carrier remains closed by the chordal-tree kernel obstruction.


## 2026-10-02 — D2 CRITICAL RE-AUDIT: SCOPE NARROWED; FULL EXTENSION REMAINS OPEN

A critical re-audit of the D2 conclusion identified two overclaims that must not control subsequent research.

1. **Coefficient-valued extension scope.** The chordal-tree relation \(u-s-t\in\ker\Phi\) with \(\omega_q(u-s-t)=-1\neq0\) closes the specific first-coefficient / incidence quotient used in the audit. It does **not** prove failure of the full restricted finite extension \(E|_{H(O_q)}\), because the first coefficient map is itself a projection that discards higher extension information. Therefore “coefficient-valued extension fails” is superseded by the narrower statement “the first coefficient-valued incidence quotient fails.”

2. **Isolated ordinary-direction functional argument.** The family \(\omega_c(\alpha s+\beta z)=\alpha+c\beta\) shows that the filtered q-profile does not constrain an arbitrary linear extension on the \(z\)-coordinate. It does **not**, by itself, prove non-uniqueness of the canonical orientation \(\omega_q\), because the constructed \(\omega_c\) is not shown to satisfy the defining canonical orientation conditions (e.g. torsion-free/Kummerian conditions). Thus the previous unrestricted “filtered q-profile cannot determine canonical orientation” conclusion is overbroad at that point.

The surviving structural conclusions are:
- D1 global depth signature is PASS / LOCAL;
- D1 depth signature is scalar-blind in the rank-two special-edge model, so orientation factorization through D1 and quotients exhausted by D1 signatures is FAIL / CLOSED;
- the first coefficient-valued incidence quotient is FAIL / CLOSED by the chordal-tree kernel obstruction;
- the full restricted/nonlinear finite-extension datum is **OPEN / LOAD-BEARING**;
- the separate same-window un-oriented finite-window no-go for the unrestricted specially oriented class remains controlling at the class level, unless the admissible class is explicitly restricted or orientation marking is enriched.

Methodological correction: D3 must not become a new carrier hunt. The next object must be a **smallest intrinsically defined nonlinear/extension invariant** that genuinely retains information discarded by D1 and by the first coefficient quotient, with a fresh Object/Input/Functoriality/Gauge/Orientation-bridge/q-blindness/Separation/Novelty/Stop pre-check.

The two overclaims are classified **HISTORICAL / SUPERSEDED**; the narrower D2 no-go remains **FAIL / CLOSED**. Detailed correction recorded in research/PAPER4_D2_CRITICAL_REAUDIT_2026-10-02.md.


## 2026-10-02 — PAPER 4 D3 MINIMAL NONLINEAR EXTENSION-ACTION AUDIT

The authorized D3 continuation was completed at the definition/pre-check level. The first surviving genuinely nonlinear candidate is the full finite conjugation-action extension attached to the intrinsic origin sector, not another linear coefficient quotient.

For the adjacent extension E_n: 1→A_n→Y=W_{n+1}→X=W_n→1, with intrinsic origin sector O_n⊂L_1, define the q-blind object by the filtered extension together with the subgroup generated by the complete lift-fibres of O_n and the conjugation action of Y on that subgroup. No presentation, basis, section, displayed q, or orientation is inserted.

Pre-check:
- Object: PASS / LOCAL;
- Input: PASS / LOCAL;
- Functoriality: PASS / LOCAL;
- Gauge/lift independence: PASS / LOCAL;
- q-blindness: PASS / LOCAL;
- Separation: PASS / LOCAL;
- Orientation bridge: OPEN / LOAD-BEARING;
- Novelty: CONDITIONAL;
- Stop: PASS for the four-control audit.

Structural reason for survival: the special relation is multiplicative conjugation wvw^{-1}=v^{1+q}; D1 and the first coefficient quotient discard part of this group-valued action. The full action therefore retains information genuinely absent from the closed linear packages.

Controls:
1. rank-two special edge: PASS / LOCAL — the q-correction survives in the full extension although D1 is scalar-blind;
2. separated two-sink: PASS / LOCAL — origin-specific action survives and the corrected noncommutation convention is respected;
3. long ordinary-chain: PASS / LOCAL — lower-filtration contamination remains distinguishable from the q-layer action;
4. chordal tree: OPEN / LOAD-BEARING — the first-coefficient kernel relation does not prove a full-extension kernel because the coefficient map is only a projection.

Literature control: Blumer–Quadrelli–Weigel characterize the canonical orientation on specially oriented pro-p RAAGs via the Kummerian condition and give local two-generator structural uniqueness. Thus the nonlinear action is the correct mechanism to compare against the known orientation theorem, but no finite-window factorization theorem is claimed yet.

Current theorem-level frontier:
C_q(O_q) ?→ omega_q mod p^k.

This must be proved on an explicitly orientation-rigid restricted class; the unrestricted class is already FAIL / CLOSED because isolated special vertices give identical un-oriented finite windows with different canonical orientations.

A natural candidate restriction is that every special vertex is the terminus of at least one special edge. This is only a candidate boundary, not yet a sufficiency theorem.

Classification:
- nonlinear extension-action object: PASS / LOCAL;
- finite orientation factorization: OPEN / LOAD-BEARING;
- unrestricted bare-window recovery: FAIL / CLOSED;
- absolute minimality: OPEN / NOT AUTHORIZED.

Detailed audit: research/PAPER4_D3_MINIMAL_NONLINEAR_EXTENSION_AUDIT_2026-10-02.md.

Next authorized action: prove the orientation bridge for the full conjugation action, including mixed degree-one elements, overlapping/separated sinks, lower-filtration contamination, chordal-tree control, and the orientation-rigid restriction. If a full-action kernel carries nonzero orientation mass, classify FAIL / CLOSED and stop the branch.


## 2026-10-02 — D3 DEFINITIONAL CORRECTION: RAW ORIGIN-LIFT SUBGROUP IS NOT NORMAL

A definition-level audit of the proposed D3 object found a genuine flaw that must control the branch before any orientation-bridge computation.

The previous object used the subgroup generated by the complete lift-fibres of the intrinsic origin sector and then asserted a conjugation action of the whole extension group (Y) on that subgroup. In general that subgroup is **not normal in (Y)**, so a global conjugation action (Y\curvearrowright\widehat O) is not defined.

Decisive control: the chordal-tree model with ordinary origins (a,b) and special vertices (s,t,u), with special edges (a\to s, b\to t, a\to u, b\to u). Let (H=\langle a,b\rangle\le Y). There is no defining relation between (t) and (a). Quotienting by the normal closure of (b,s,u) gives the free pro-(p) group on (a,t). Hence (tat^{-1}\notin\langle a\rangle), and therefore (tat^{-1}\notin H). Thus (H) is not normal in (Y).

Consequently the statement “the full conjugation action of (Y) on the origin-lift subgroup” is **not a valid object as written**. The prior D3 object-level PASS is superseded.

The minimal canonical repair is to replace the raw origin-lift subgroup by its **normal closure** in (Y), or equivalently to formulate the datum as the conjugation action on the normal closure of the origin sector. This repaired object is materially richer and may risk re-encoding more of the finite window; it therefore requires a fresh full pre-check before any computation.

Classification:
- raw origin-lift subgroup with (Y)-conjugation action: **FAIL / CLOSED**;
- previous D3 object-level PASS: **HISTORICAL / SUPERSEDED**;
- normal-closure conjugation object: **OPEN / LOAD-BEARING**;
- orientation bridge: **NOT YET AUTHORIZED** until the repaired object passes Object/Input/Functoriality/Gauge/Orientation-bridge/q-blindness/Separation/Novelty/Stop.

This is a definition correction, not a carrier hunt. The next authorized step is the fresh pre-check of the normal-closure repair, followed only if it passes by the mixed/chordal orientation-bridge test.


## 2026-10-02 — D3 REPAIRED-OBJECT PRE-CHECK: NORMAL CLOSURE PASSES OBJECT-LEVEL TEST, BUT ORIENTATION BRIDGE IS NOT FINITE/INTRINSICALLY SPECIFIED

The canonical repair was audited before any new computation.

Define (N_O) as the normal closure in (Y) of the preimage of the intrinsic origin sector (O_q). Then (N_O\triangleleft Y), so the conjugation action (Y\to\operatorname{Aut}(N_O)) is well-defined. The repaired package
[
\mathcal C_q^{\mathrm{nc}}=(Y,X,A_q,O_q,N_O,\operatorname{conj}_Y|_{N_O})
]
is intrinsic, functorial, lift/section-independent, and q-blind at the definition level.

However, the required orientation bridge still fails the mandatory pre-check in its present form: no canonical finite quotient of the action (Y\to\operatorname{Aut}(N_O)) has been exhibited whose scalar character is (omega_q\bmod p^k). Taking the action on (N_O) itself is not a bridge; it merely retains a large nonabelian object. Taking its obvious q-layer linearization collapses back to the already closed coefficient/incidence package. Using the literature's Kummerian criterion would be circular/re-encoding for the present finite-window program, because the criterion quantifies over all (n\ge1) and supplies the orientation as part of the oriented pair rather than extracting it from one finite window.

Independent literature control: Blumer–Quadrelli–Weigel prove that for an oriented pro-(p) RAAG there is a torsion-free Kummerian orientation exactly in the specially oriented case, and that this orientation is unique; their local locally-uniform argument likewise determines the canonical orientation from the full 2-generator group structure. This validates the *global mechanism* but does not furnish the required finite-window factorization. citeturn7search1turn4search0

Therefore no orientation-bridge computation is logically authorized from the repaired object yet. A further computation would be another carrier hunt unless a specific finite scalar quotient/action character is first derived non-tautologically from the repaired package.

Classification:
- raw origin-lift conjugation object: **FAIL / CLOSED**;
- normal-closure conjugation package: **PASS / LOCAL** at Object/Input/Functoriality/Gauge/q-blindness;
- finite orientation bridge from the repaired package: **OPEN / LOAD-BEARING**;
- finite-window factorization theorem: **OPEN**;
- absolute minimality: **OPEN / NOT AUTHORIZED**;
- unrestricted class: **FAIL / CLOSED** by the isolated-special same-window obstruction.

**Stop condition reached:** do not perform another blind computation. The next legitimate move is target-first derivation of a *specific finite scalar character* of the normal-closure action, with a full pre-check. If no such character can be defined without reintroducing the orientation or q, D3 closes as a finite-carrier realization failure while the negative Gate-D theorem remains a principal result.


## 2026-10-02 — FREE-BY-DEMUSHKIN / PD3 LITERATURE GATE

A primary-source audit of M. Palaisti, *Detecting Cohomological Dimension Three in Free-by-Demuškin Pro-p Groups*, arXiv:2610.00021v1, was completed.

The paper proves, for 1→N→G→D→1 with N nontrivial free pro-p and D Demuškin, that H^3(G,F_p)^∨ ≅ (N/Φ(N))^D and cd_p G=3 iff (N/Φ(N))^D≠0. It also identifies the lower-dimensional branch through H^1(D,W^∨) and a relation-defect class δ_G∈W_D, with δ_G represented by a lift of the defining Demuškin relator in the coinvariants. The paper further proves the top-degree fixed-Frattini mechanism for arbitrary pro-p PD^n quotients.

Critical scope correction: if G itself is pro-p PD^3, N is forced to be Z_p. Therefore the successor target is NOT “general PD3 free-by-Demuškin with arbitrary finite-rank free kernel.” The viable target is either (a) free-by-Demuškin extensions with cd_p G=3, or (b) the rank-one PD3 subfamily.

Comparison with Paper 1–3: the paper confirms a genuine PD-duality extension mechanism, and Lemma 7.2 gives a strong relation-module/Fox/transgression contact. But it does not prove any finite-window factorization of W^D, W_D, δ_G, or the Demuškin orientation. Thus U1–U5 do not automatically extend. The unresolved bridge is precisely full extension → finite filtered window.

Classification:
- literature mechanism: PASS / CLOSED;
- relation-module/Fox contact: PASS / LOCAL;
- automatic U1–U5 extension: FAIL / CLOSED;
- finite-window reconstruction of extension/orientation data: OPEN / LOAD-BEARING;
- PD3 middle-group branch with arbitrary free rank: CLOSED by rank-one restriction;
- free-by-Demuškin finite-window successor: OPEN / CONDITIONAL.

RAAG carrier search is HOLD/SUPPRESSED while this literature-first branch is tested. Detailed audit: research/PAPER4_FREE_BY_DEMUSHKIN_PD3_LITERATURE_AUDIT_2026-10-02.md.

## 2026-10-02 — K–Z ORIGINAL CONSTRUCTION AUDIT / FINITE-WINDOW OBSTRUCTION TEST

Kochloukova–Zalesskii, *Free-by-Demushkin pro-p groups*, Math. Z. 249 (2005), 731–739, was independently verified from a full-text mirror/search extract. Their Theorem 2 gives, for
\[
G_s=\langle x,y,z\mid z^{p^s}=[x,y]\rangle,
\qquad N_s=\overline{\langle z\rangle}^{\,G_s},
\qquad D=G_s/N_s\simeq\mathbf Z_p^2,
\]
that cd_p(G_s)=2, G_s is finitely generated, N_s is free pro-p of infinite rank, and the inflation maps \(H^2(S/N_s,\mathbf Z/p^n)\to H^2(S,\mathbf Z/p^n)\) are isomorphisms for all closed \(S\supseteq N_s\) and all n. citeturn0search25turn0search0

The decisive finite-window observation is filtration-theoretic: the defining relator has initial Zassenhaus degree 2, namely \([x,y]\), while the correction \(z^{p^s}\) occurs at degree \(p^s\). Hence for every fixed window depth \(n\le p^s\), the relation is indistinguishable from \([x,y]=1\) in \(G_s/D_n(G_s)\). Thus the family \(G_s\) supplies finitely generated cd=2 free-by-Demushkin examples with an arbitrarily long low-degree finite-window regime in which the genuinely extension-specific correction is invisible.

This does **not** yet prove a finite-window no-go for cd=3: we still need a cd=3 free-by-Demushkin family whose first n Zassenhaus windows agree with the same low-window model. Therefore the correct classification is not FAIL/CLOSED but a sharper boundary:
- K–Z deep-tail invisibility phenomenon: **PASS / LOCAL**;
- “K–Z alone proves finite-window cd detection impossible”: **FAIL / CLOSED as an inference**;
- finite-window detection of \(W^D\neq0\): **OPEN / LOAD-BEARING**;
- direct use of \(H^3(G)\) as a quotient cohomology of \(G/D_n\): **NOT JUSTIFIED**;
- relation-defect/Frattini data as finite-window target: **OPEN**.

Methodological consequence: do not compute a carrier yet. The next authorized test is sharper: construct or rule out a **matched cd=3 control** with the same finite initial Zassenhaus data as the K–Z cd=2 model. If such a matched pair exists at arbitrary depth, finite-window detection closes negatively. If no such pair can be produced, the finite-window factorization question remains open and the K–Z example should be retained as the principal deep-tail stress test.

Literature source: Kochloukova–Zalesskii, DOI 10.1007/s00209-004-0720-6; the accessible full-text extract explicitly states Theorem 2 and the presentation above. citeturn0search25turn0search1

## 2026-10-02 — DECISIVE MATCHED-WINDOW NO-GO: K–Z cd=2 VS ABELIAN cd=3

A matched cd=3 control has been found, so the previous “OPEN/LOAD-BEARING” boundary sharpens substantially.

Fix an odd prime p and let
\[
G_s=\langle x,y,z\mid z^{p^s}=[x,y]\rangle
\]
be the Kochloukova–Zalesskii example. Their theorem gives cd_p(G_s)=2, G_s finitely generated, and a free pro-p kernel N_s of infinite rank over the quotient D\simeq Z_p^2. citeturn0search36

Let
\[
G_+=Z_p^3=\langle x,y,z\mid [x,y]=[x,z]=[y,z]=1\rangle,
\]
viewed as the split extension 1→N_+→G_+→D→1 with N_+=Z_p and D=Z_p^2. The quotient D=Z_p^2 is a Demushkin group (odd-p classification with d=2 and q=0, relation [x,y]); hence Palaisti applies and cd_p(G_+)=3, equivalently (N_+/Phi(N_+))^D≠0. citeturn1search17turn1search20

For every n with n≤p^s,
\[
G_s/D_n(G_s)\cong G_+/D_n(G_+).
\]
Reason: in the quotient modulo D_n, the element z^{p^s} is trivial because D_{p^s}⊆D_n. The K–Z relation therefore forces [x,y]=1; the resulting quotient is exactly the Zassenhaus quotient of the abelian rank-3 pro-p group. This uses the standard Zassenhaus definition \(D_n=\prod_{ip^j\ge n}\gamma_i^{p^j}\) and functoriality under quotients. citeturn2search0turn4search5

Thus for every prescribed finite depth n there are two finitely generated free-by-Demushkin pro-p groups with the same n-th Zassenhaus window but different values of
\[
\kappa=\dim H^3(G,F_p)=\dim (N/\Phi(N))^D:
\quad \kappa(G_s)=0,\quad \kappa(G_+)=1.
\]

This is the decisive negative result for any **uniform finite-depth detector** on the full finitely generated free-by-Demushkin class: no bound n=n(p,d) depending only on p and the generator rank d can determine cd_p G or κ from G/D_n, since both examples have d=3 and s can be chosen with p^s≥n.

Crucial logical boundary: this does NOT prove that every individual G has no finite detecting depth, nor that an adaptive threshold depending on the hidden relation/extension data cannot exist. Indeed the K–Z family itself has a finite parameter s, and deeper windows may reveal it. Therefore the correct classification is:
- matched cd=2/cd=3 arbitrary-depth windows: **PASS / LOCAL**;
- uniform finite-depth cd/κ detector on the full class: **FAIL / CLOSED**;
- detector with group-dependent threshold: **OPEN / LOAD-BEARING**;
- finite-window recovery of δ_G or W^D at a threshold controlled by extension defect depth: **OPEN**;
- carrier search before resolving threshold dependence: **STOP / NOT AUTHORIZED**.

This is the first genuinely load-bearing Paper-4 negative theorem candidate and supersedes the weaker “K–Z alone is insufficient” boundary.


## 2026-10-02 — EXACT FIRST SEPARATION: THE K–Z PAIR SPLITS AT p^s+1

The previously open threshold question for the matched pair can now be closed.

For odd p, let
\\[
G_s=\\langle x,y,z\\mid z^{p^s}=[x,y]\\rangle,
\\qquad G_+=\\mathbf Z_p^3.
\\]
For every n\\le p^s, the earlier quotient-presentation argument gives
\\[
G_s/D_n(G_s)\\cong G_+/D_n(G_+).
\\]

To prove that the first separation occurs immediately after that range, construct the finite class-2 p-group
\\[
H_s=\\langle x,y,z\\mid z^{p^{s+1}}=x^{p^{s+1}}=y^{p^{s+1}}=1,\\ z\\text{ central},\\ [x,y]=z^{p^s}\\rangle.
\\]
This is a quotient of G_s. Its lower central series has \\gamma_2(H_s)=\\langle z^{p^s}\\rangle and \\gamma_3(H_s)=1. By the Lazard/Jennings description
\\[
D_n(H)=\\prod_{ip^j\\ge n}\\gamma_i(H)^{p^j},
\\]
for n=p^s+1 the i=1 contribution is H_s^{p^{s+1}}=1, while the i=2 contribution is \\gamma_2(H_s)^{p^s}=1; hence
\\[
D_{p^s+1}(H_s)=1.
\\]
Therefore z^{p^s} is nontrivial in H_s/D_{p^s+1}(H_s), so z^{p^s}\\notin D_{p^s+1}(G_s). Consequently
\\[
[x,y]=z^{p^s}\\notin D_{p^s+1}(G_s),
\\]
so G_s/D_{p^s+1}(G_s) is nonabelian. In contrast G_+=\\mathbf Z_p^3 is abelian, hence every quotient G_+/D_n(G_+) is abelian. Thus
\\[
G_s/D_{p^s+1}(G_s)\\not\\cong G_+/D_{p^s+1}(G_+).
\\]

Hence the matched pair has exact first separation depth
\\[
\\boxed{n_{\\rm sep}(G_s,G_+)=p^s+1}.
\\]
This is stronger than the previous lower-bound statement and does not require a mildness theorem or an associated-graded nonvanishing argument; the finite quotient H_s directly witnesses survival of the commutator at the critical depth.

Combined with cd_p(G_s)=2 and cd_p(G_+)=3, this yields an explicit arbitrarily delayed separation family. For fixed odd p and d=3, any universal detector must accommodate thresholds at least p^s+1 on this family. Therefore no finite bound depending only on p and d exists, while the K–Z family provides a concrete relation-depth parameter producing exact pairwise separation thresholds.

Classification:
- exact pairwise first-separation depth p^s+1: **PASS / CLOSED**;
- uniform finite-depth detector on the full finitely generated free-by-Demushkin class: **FAIL / CLOSED**;
- individual/group-dependent detection threshold: **OPEN / LOAD-BEARING**;
- identification of a canonical intrinsic threshold parameter from extension data: **OPEN**.

Independent verification used the standard Zassenhaus/Lazard product formula and an explicit finite quotient, avoiding any appeal to unverified initial-form survival.


## 2026-10-02 — CRITICAL CORRECTION: K–Z MATCHED-WINDOW / p^s+1 CLAIM SUPERSEDED

A referee-level recheck found a fatal error in the preceding “matched cd=2/cd=3 window” argument.

The invalid step was the assertion \(G_s/D_n(G_s)\cong G_+/D_n(G_+)\) for \(n\le p^s\), with \(G_+=\mathbf Z_p^3\). After \(z^{p^s}\) disappears, the K–Z relation gives only \([x,y]=1\); it does not impose \([x,z]=[y,z]=1\). Thus the quotient is not the abelian rank-3 quotient of \(G_+\).

For odd p the error is already visible at depth 3: \([x,z]\) survives in \(G_s/D_3(G_s)\), whereas every quotient of \(G_+\) is abelian. An explicit exponent-p Heisenberg quotient on \(x,z\), with \(y\) central, satisfies the K–Z relation and has \([x,z]\ne1\) and \(D_3=1\).

Therefore the “arbitrarily delayed matched separation” and the claimed pairwise threshold \(p^s+1\) are **HISTORICAL / SUPERSEDED**. The auxiliary \(H_s\) construction still correctly witnesses \(z^{p^s}\notin D_{p^s+1}(G_s)\), but it does not prove separation from \(\mathbf Z_p^3\), since that pair already separates through \([x,z]\).

Current classification:
- K–Z deep-tail invisibility of \(z^{p^s}\): **PASS / LOCAL**;
- explicit survival witness at depth \(p^s+1\): **PASS / LOCAL**;
- arbitrary-depth cd=2/cd=3 matched-window theorem: **FAIL / CLOSED — withdrawn**;
- uniform finite-depth detector no-go based on that pair: **FAIL / CLOSED as unsupported**;
- individual/group-dependent threshold: **OPEN**;
- genuine matched cd=3 control: **OPEN / next authorized test**.


## 2026-10-02 — E2/F1 K–Z SAME-WINDOW p-ADIC FACTORIZATION NO-GO

A new exact same-window lemma closes the uniform finite-depth factorization route for the E2 p-adic extension class without using the withdrawn \(\mathbf Z_p^3\) comparison.

For
\[
G_s=F(x,y,z)/\overline{\langle\!\langle z^{p^s}[x,y]^{-1}\rangle\!\rangle},
\]
if \(p^s\ge n\), then \(z^{p^s}\in D_{p^s}(F)\subseteq D_n(F)\). Hence
\[
G_s/D_n(G_s)\cong F/(D_n(F),[x,y]),
\]
so for any \(s,t\) with \(p^s,p^t\ge n\),
\[
G_s/D_n(G_s)\cong G_t/D_n(G_t).
\]
This is the correct same-window statement; it does not claim an abelian quotient, and therefore avoids the previously withdrawn \(\mathbf Z_p^3\) error.

E2 independently gives \(v_p(\epsilon_s)=s\), up to the unit ambiguity in the choice of the generator of \(H_2(D,\mathbf Z_p)\). Thus distinct sufficiently large \(s,t\) have identical depth-\(n\) windows but distinct p-adic extension-depth data. For \(s<t<m\) the truncations \(\epsilon_s\bmod p^m\) and \(\epsilon_t\bmod p^m\) are already different (the latter is zero, the former nonzero).

Therefore:
- K–Z same-window lemma: **PASS / CLOSED**;
- uniform fixed-depth recovery of the E2 p-adic class across the whole K–Z family: **FAIL / CLOSED**;
- uniform bound \(n=n(p,d,m)\) independent of hidden extension depth: **FAIL / CLOSED**;
- group-dependent/adaptive threshold \(n=n(G,m)\): **OPEN / LOAD-BEARING**;
- possibility that \(n=p^m\) or another relation-depth bound suffices for this family: **OPEN**;
- orientation recovery from E2: **OPEN**.

This is a genuine finite-window negative boundary, but it is not a cd=3 no-go and does not prove that any individual \(G_s\) lacks a finite detecting window.

Detailed audit: research/PAPER4_F1_KZ_SAME_WINDOW_P_ADIC_NO_GO_AUDIT_2026-10-02.md.


## 2026-10-02 — F1 K–Z ADAPTIVE THRESHOLD: POSITIVE LOCAL RESULT

The K–Z family admits an explicit intrinsic adaptive finite-window recovery of the E2 valuation truncation.

Since
\[
G_s^{ab}\simeq\mathbf Z_p^2\oplus\mathbf Z/p^s,
\]
and the Zassenhaus filtration is functorial under abelianization, for \(e=\lceil\log_p n\rceil\),
\[
(G_s/D_n(G_s))^{ab}
\simeq
(\mathbf Z/p^e)^2\oplus\mathbf Z/p^{\min(s,e)}.
\]
Taking \(n=p^m\) gives \(e=m\), so the torsion exponent intrinsically recovers \(\min(s,m)\). Since E2 gives \(v_p(\epsilon_s)=s\), the finite window recovers \(\min(v_p(\epsilon_s),m)\), including the vanishing/nonvanishing of \(\epsilon_s\bmod p^m\).

The same-window lemma gives a matching lower-bound scale: if \(s<t<m\) and \(p^s\ge n\), then the depth-\(n\) windows agree while the \(m\)-truncations differ. Hence a uniform K–Z-family threshold for \(m\)-digit valuation information must exceed \(p^{m-1}\) up to the integer boundary. The construction \(n=p^m\) gives the correct exponential scale, but exact minimality is not proved.

Classification:
- adaptive K–Z valuation recovery: **PASS / LOCAL**;
- intrinsic realization via finite-window abelianization: **PASS / LOCAL**;
- lower-bound scale \(n>p^{m-1}\): **PASS / LOCAL**;
- exact minimal threshold: **OPEN**;
- general free-by-Demushkin finite-window factorization: **OPEN / LOAD-BEARING**;
- orientation recovery from E2: **OPEN**.

Detailed audit: research/PAPER4_F1_KZ_ADAPTIVE_THRESHOLD_AUDIT_2026-10-02.md.


## 2026-10-02 — F1 EXACT MINIMAL THRESHOLD + HIGHER-RANK DEMUSHKIN STRESS TEST

The K–Z threshold is now exact. Writing \(e(n)=\lceil\log_p n\rceil\),
\[
(G_s/D_n(G_s))^{ab}\simeq
(\mathbf Z/p^{e(n)})^2\oplus\mathbf Z/p^{\min(s,e(n))}.
\]
For \(m\ge2\), uniform recovery of \(\min(s,m)\) requires and is achieved by \(e(n)\ge m\), hence the exact smallest integer depth is
\[
\boxed{n_m^{\mathrm{KZ}}=p^{m-1}+1}.
\]
The lower bound is reinforced by the same-window lemma: at any \(n\le p^{m-1}\), suitable \(s<t<m\) give identical full windows but different \(m\)-truncated valuations.

A higher-rank q=0 Demushkin stress model was then tested:
\[
\widetilde G_{s,d}=\langle z,x_1,\dots,x_d\mid
z^{p^s}=[x_1,x_2][x_3,x_4]\cdots[x_{d-1},x_d]\rangle,
\quad d\ge4\text{ even}.
\]
At the homological/abelianized level,
\[
\widetilde G_{s,d}^{ab}\simeq\mathbf Z_p^d\oplus\mathbf Z/p^s,
\]
so the same adaptive finite-window formula survives:
\[
(\widetilde G_{s,d}/D_{p^m})^{ab}
\simeq(\mathbf Z/p^m)^d\oplus\mathbf Z/p^{\min(s,m)}.
\]
This shows the K–Z mechanism is not rank-2-specific. However, the normal closure of \(z\) has not yet been independently certified free pro-p in this higher-rank model, so it is a stress model, not a new theorem-level free-by-Demushkin example.

For a standard Demushkin quotient with finite torsion invariant \(q=p^a\), the same construction has abelianized relation \(p^s z=p^a x_1\), whose Smith normal form yields torsion order \(p^{\min(a,s)}\). Thus abelianization saturates at the quotient's intrinsic q-depth and cannot see arbitrary extension depth once \(s>a\).

Classification:
- exact K–Z threshold \(p^{m-1}+1\): **PASS / CLOSED**;
- q=0 higher-rank stress mechanism: **PASS / LOCAL**;
- higher-rank kernel freeness: **OPEN**;
- q>0 abelianization saturation: **PASS / LOCAL**;
- general free-by-Demushkin finite-window extension-depth theorem: **OPEN / LOAD-BEARING**;
- higher nonabelian finite scalar character: **OPEN**;
- E2 → orientation: **OPEN**.

Detailed audit: research/PAPER4_F1_MINIMAL_THRESHOLD_AND_DEMUSHKIN_STRESS_AUDIT_2026-10-02.md.


## 2026-10-02 — Q>0 HIGHER-FILTERED LAYER / GAUGE AUDIT

The next authorized q>0 gate was audited before any carrier computation. For a standard odd-p Demushkin quotient with q_D=p^a and candidate extension relation z^{p^s}=r_D, abelianization gives torsion p^{min(a,s)}. Therefore pure abelianization cannot recover s once s>a: **FAIL / CLOSED for the pure abelian detector**.

A literature search did not locate a theorem-level q_D>0 variable-depth free-by-Demushkin family certifying the proposed model for arbitrary s>a. Kochloukova–Zalesskii explicitly certify the variable-depth family z^{p^s}=[x,y] only with quotient D=Z_p^2 of q_D=0. General one-relator/free-by-Demushkin results in Quadrelli require additional hypotheses and do not certify the proposed q_D>0 family.

Independent gauge control: Ben-Bassat–Gropper (2026), Proposition 4.7, exhibits a related PD^2-pair automorphism phenomenon for s_0=s_1 x^{p^r}[x,y]: for alpha congruent to 1 mod p^r, an automorphism fixes the s_1 boundary up to conjugacy and sends s_0 to a conjugate of s_0^alpha. This is not the present family, but it proves that raw p-adic relator/boundary coefficients are not automatically intrinsic. Any higher-layer scalar must therefore pass an explicit gauge-invariance test.

Classification:
- q>0 abelianization saturation: **PASS / LOCAL**;
- pure abelianization recovery for s>a: **FAIL / CLOSED**;
- q>0 higher filtered recovery of s: **OPEN / LOAD-BEARING**;
- finite-window factorization of a gauge-invariant truncation: **OPEN**;
- orientation bridge: **OPEN**;
- new carrier hunt: **STOP / NOT AUTHORIZED**.

Next authorized action: define the smallest gauge-invariant truncation of the full transgression/relation object and test finite-window factorization. If no scalar survives the gauge quotient without reintroducing q or the orientation, close this q>0 realization route.

Detailed audit: research/PAPER4_QPOS_HIGHER_LAYER_AUDIT_2026-10-02.md.


## 2026-10-02 — CRITICAL E2 q>0 HOMOLOGY CORRECTION

A decisive correction was made to the q>0 gate. The untwisted q=0 E2 transgression source H_2(D,Z_p) does not persist for a standard Demushkin quotient with q_D=p^a>0. Using the one-relator Fox/cellular boundary, the exponent-sum vector is (p^a,0,...,0), so multiplication by p^a on Z_p is injective and H_2(D,Z_p)=0. For q=0 the exponent-sum vector is zero and H_2(D,Z_p)=Z_p.

Therefore the previously proposed untwisted E2 transgression class cannot be continued to q>0: its source is zero. For the stress presentation z^{p^s}=r_D, the untwisted five-term sequence identifies (N^{ab})_D with ker(H_1(G)->H_1(D)); the associated rank-one abelian extension is classified on the quotient torsion summand by Ext^1_{Z_p}(Z/p^a,Z_p)=Z/p^a, and the relation gives class p^s mod p^a (up to sign/unit convention). Hence for s>=a the entire untwisted H_1/coinvariant extension layer is already saturated and cannot distinguish s>a.

Reclassification:
- untwisted E2 homological/transgression layer for q>0, s>a: **FAIL / CLOSED**;
- pure abelianization detector: **FAIL / CLOSED**;
- abelian H_1-extension class: **FAIL / CLOSED for s>a**;
- BBG gauge warning: **PASS / LOCAL** only;
- genuinely nonabelian higher relation data: **OPEN / LOAD-BEARING**;
- twisted/dualizing-coefficient replacement: **OPEN / NOT YET DEFINED**;
- finite-window factorization of a new nonabelian object: **OPEN**.

This replaces the previous wording that 'q>0 higher filtered E2' remained open: the untwisted E2 route is now structurally exhausted. Any continuation must be a genuinely new nonabelian relation object, or a separately justified twisted-coefficient construction that passes a fresh pre-check.

Detailed audit: research/PAPER4_E2_QPOS_HOMOLOGY_CORRECTION_2026-10-02.md.


## 2026-10-02 — Q>0 ORDINARY ZASSENHAUS GRADED STRESS

For the stress presentation G_{s,a}=<z,x_1,...,x_d | z^{p^s}=x_1^{p^a}[x_1,x_2]...[x_{d-1},x_d]> with odd p and a,s>=1, the p-Zassenhaus initial form of the defining relation is the degree-2 Demushkin commutator form rho=[X_1,X_2]+...+[X_{d-1},X_d]. The terms z^{p^s} and x_1^{p^a} occur only in degrees p^s and p^a, respectively, so the initial form is independent of s.

Using the Schmidt mildness criterion in Gärtner's formulation, with U=span{x_i} and V=span{z}, the cup product U x U surjects onto H^2 while V x V=0; hence the candidate is mild (odd-p setting). For mild groups, the associated graded completed group algebra is generated by the initial relation form. Therefore the ordinary mod-p Zassenhaus associated graded is the same for all s at this candidate level.

Classification:
- initial-form blindness to s: **PASS / CLOSED**;
- ordinary mod-p Zassenhaus associated-graded detector: **FAIL / CLOSED**;
- full finite Zassenhaus window: **OPEN**;
- intrinsic integral p-adic Magnus/relation-module truncation: **OPEN / LOAD-BEARING**.

Boundary: this does not prove finite windows cannot recover s; it proves only that recovery cannot factor solely through the ordinary associated graded mod-p object. Detailed audit: research/PAPER4_QPOS_ZASSENHAUS_GRADED_STRESS_AUDIT_2026-10-02.md.


## 2026-10-02 — CRITICAL REVIEW / q>0 BOUNDARY AND NEXT-GATE DISCIPLINE

The submitted critical review was accepted with one scope correction. The q>0 untwisted E2 closure is structurally correct: for standard odd-p Demushkin q=p^a>0, H_2(D,Z_p)=0, so the q=0 transgression source does not continue. The untwisted H_1/coinvariant extension saturates at p^a in the stated stress presentation, and the ordinary mod-p Zassenhaus associated graded is blind to s at the candidate stress-model level.

The phrase “only remaining candidate” is narrowed: intrinsic integral, gauge-invariant, nonabelian relation data is the **only remaining primary route currently authorized**, not an exhaustive list of all conceivable mathematics. Twisted/dualizing coefficients or other nonlinear cohomological objects remain logically possible but require a fresh independent pre-check and are not E2 continuations.

New active gate:
**P4-Q+ / INTEGRAL-NONABELIAN-DEFINITION = OPEN / LOAD-BEARING.**

Before any computation, the exact object must be fixed and pass Object/Input/Functoriality/Gauge/Orientation-bridge/q-blindness/Separation/Novelty/Stop. In particular, presentation coefficients, relator choices, lifts, sections, conjugacy, Nielsen changes, unit scaling, and quotient/kernel automorphisms must be explicitly quotiented or shown irrelevant. The object must not insert q or orientation and must not merely re-encode a chosen presentation coefficient.

Scope corrections:
- q>0 untwisted H_1-extension saturation is **LOCAL to the stress presentation**, not a theorem for all free-by-Demushkin extensions;
- ordinary mod-p associated-graded blindness is **LOCAL to the stress candidate** and does not imply full finite-window blindness;
- universal impossibility for q>0 deep tails remains **OPEN**.

Detailed audit: research/PAPER4_QPOS_CRITICAL_REVIEW_NEXT_GATE_2026-10-02.md.


## 2026-10-02 — FINITE-COEFFICIENT E2 TOR CHECK / DEEP-TAIL CLOSURE

A correction and subsequent explicit check were completed. The earlier statement that q>0 has no E2 continuation is literally true for Z_p coefficients, but finite coefficients A_m=Z/p^m produce a Tor source:
H_2(D,A_m) ≅ Tor(Z/p^a,Z/p^m) ≅ Z/p^{min(a,m)}.

For the stress presentation G_{s,a}=<z,x_i | z^{p^s}=r_D>, when m>a a generator is represented by p^{m-a} times the Demushkin relation cell. The lifted defect is z^{p^s}, so the transgression image is p^{m-a+s}z mod p^m. Therefore it vanishes whenever s>=a. Thus the finite-coefficient E2/Tor route does not recover the deep regime s>a.

Classification:
- finite-coefficient H2 Tor source: PASS / LOCAL;
- finite-coefficient E2 transgression for s>a: FAIL / CLOSED in the stress model;
- coefficient change as a rescue of E2: FAIL / CLOSED;
- genuinely nonabelian relation/extension object: OPEN / LOAD-BEARING;
- finite-window factorization of such an object: OPEN.

Detailed audit: research/PAPER4_QPOS_FINITE_COEFFICIENT_E2_TOR_AUDIT_2026-10-02.md.


## 2026-10-02 — MINIMAL NONABELIAN FINITE-EXTENSION PRE-CHECK

The most direct intrinsic nonlinear object induced by a window is the relative finite extension
1 -> N/(N∩D_n(G)) -> G/D_n(G) -> D/D_n(D) -> 1.
It is functorial and gauge-free once G→D is structured input, but it is not a genuine carrier: it essentially repackages the finite window together with its quotient map. Thus it fails the novelty/compression requirement as a standalone candidate.

The active problem is now sharply narrowed to a **strict intrinsic compression** of this finite relative extension: a scalar or smaller module quotient that survives all gauges, does not insert q/orientation, and factors through the finite window without simply re-encoding it.

Classification:
- finite relative extension: PASS / LOCAL as an intrinsic object;
- same object as novel compression carrier: FAIL / CLOSED;
- strict nonlinear compression: OPEN / LOAD-BEARING;
- universal no-compression theorem: OPEN;
- blind carrier hunt: STOP.

Detailed audit: research/PAPER4_QPOS_MINIMAL_NONABELIAN_FINITE_EXTENSION_PRECHECK_2026-10-02.md.


## 2026-10-02 — P4-Q+ ADMISSIBLE COMPRESSION CATEGORY PRE-CHECK

The previous frontier statement “strict intrinsic nonabelian compression” was made executable by fixing an admissible category before any further computation.

Defined audit:
\`research/PAPER4_QPOS_ADMISSIBLE_COMPRESSION_CATEGORY_PRECHECK_2026-10-02.md\`.

The admissible compression is a functorial quotient of the finite relative Zassenhaus extension
\[
1\to N/(N\cap D_n(G))\to G/D_n(G)\to D/D_n(D)\to1
\]
subject to eight requirements: A1 intrinsicity; A2 functoriality; A3 gauge invariance; A4 q-blindness; A5 orientation-blind input; A6 strict information loss; A7 non-reencoding; A8 filtration compatibility.

Two target levels were separated:
- T1 weak target = distinguish deep-tail parameters \(s\ne t\) in the q>0 stress family with \(s,t>a\);
- T2 strong target = recover \(T_m=\min(s,m)\), for fixed \(m>a\).

T1 is the default next target; T2 is secondary.

The re-encoding test is explicit: a candidate must have a certified pair of non-isomorphic admissible finite relative extensions with isomorphic compressed objects. A proper quotient that remains reconstructible is not counted as compression.

Pre-check classification:
- admissible compression category: **PASS / LOCAL**;
- T1: **DEFINED**;
- T2: **DEFINED / SECONDARY**;
- existence of a strict intrinsic compression: **OPEN / LOAD-BEARING**;
- universal no-compression theorem: **OPEN**;
- carrier computation before A1–A8: **STOP / CLOSED**.

No raw Fox/Magnus scalar computation is authorized until a specific quotient candidate and its gauge orbit are fixed.


## 2026-10-02 — T1 TARGET STRENGTHENED AFTER CRITICAL REVIEW

The first definition of T1 allowed pair-dependent depths \(n(s,t)\), which was too weak: it could collapse back toward the tautological fact that an inverse system may eventually separate individual examples.

T1 is therefore corrected to a **uniform finite-depth separation target on a declared finite stress range**. For fixed \(m>a\), a single depth \(n=n(m)\), chosen independently of the hidden tail parameter \(s\), must separate all distinct deep-tail values \(a<s,t\le m\) after compression.

Thus the next test is genuinely a finite-window factorization/compression test, not pairwise eventual separation.

Audit updated:
\`research/PAPER4_QPOS_ADMISSIBLE_COMPRESSION_CATEGORY_PRECHECK_2026-10-02.md\`.

Classification remains:
- admissible compression category: **PASS / LOCAL**;
- T1: **DEFINED / CORRECTED**;
- T2: **DEFINED / SECONDARY**;
- strict intrinsic compression existence: **OPEN / LOAD-BEARING**.


## 2026-10-02 — FIRST CONCRETE STRICT-COMPRESSION CANDIDATE: RELATIVE CLASS-2 KERNEL QUOTIENT

After correcting T1 and strictness, the first authorized candidate was fixed:
\[
C_n^{(2)}(E_n):
1\to K_n/\gamma_3(K_n)\to W_n/\gamma_3(K_n)\to D/D_n(D)\to1.
\]
This is the finite relative extension with the kernel replaced by its class-2 nilpotent quotient.

Pre-check:
- A1 intrinsicity: **PASS / LOCAL**;
- A2 functoriality: **PASS / LOCAL**;
- A3 gauge invariance: **PASS / LOCAL**;
- A4 q-blindness: **PASS**;
- A5 orientation-blind input: **PASS**;
- A6 strictness: **OPEN**;
- A7 non-reencoding: **OPEN**;
- A8 filtration compatibility: **PASS / LOCAL**.

The candidate is structurally beyond the closed H1/E2 layer because it retains the kernel commutator pairing and D-action, rather than only the abelianized extension/coinvariant information. This is not yet a separation theorem.

T1 threshold detection remains **OPEN** for this candidate. Ordinary mod-p associated-graded blindness does not by itself close the integral class-2 quotient, because the quotient retains integral extension information discarded by the mod-p graded object.

No raw Magnus/Fox expansion was performed. Next authorized test: determine whether the class-2 quotient contains a gauge-invariant datum not factoring through the already closed abelian/E2/graded layers, then test the binary threshold \(s\ge m\). If it factors through the closed layers, classify FAIL/CLOSED; if a genuinely new integral commutator datum survives, continue to T1.

Literature method check: Hamza 2023 treats lower-central/Zassenhaus filtrations and their module actions for finitely generated pro-p groups, supporting the naturality of this filtration-based construction; it does not prove the present compression theorem.


## 2026-10-02 — P4-Q+ CLASS-2 FACTOR-THROUGH PRETEST

The first authorized factor-through test for the relative class-2 kernel quotient was completed at the structural level.

For \(A_n=K_n/\gamma_2(K_n)\) and \(B_n=\gamma_2(K_n)/\gamma_3(K_n)\), the candidate retains the intrinsic commutator pairing \(\beta_n:A_n\wedge A_n\to B_n\) and the induced \(D/D_n(D)\)-action. This is a genuinely different type of datum from the closed abelian/H1-extension package; that package has no formal reconstruction of an arbitrary class-2 commutator pairing. Likewise, ordinary mod-p Zassenhaus graded blindness does not imply factorization of the integral class-2 quotient through the graded object.

This yields only **PASS / LOCAL** for structural non-factorization in the ambient class-2 extension category. It is not yet a theorem on the q>0 stress family \(G_{s,a}\): an explicit stress-family separation pair is still required.

Therefore the candidate remains:
- structural distinction from abelian/H1 layers: **PASS / LOCAL**;
- factor-through stress test: **OPEN / LOAD-BEARING**;
- T1 threshold separation: **OPEN / LOAD-BEARING**;
- A6 strictness: **OPEN**;
- A7 non-reencoding: **OPEN**.

The next authorized computation is singular and targeted: compute only \((A_n,B_n,\beta_n,\text{class-2 power map},D\text{-action})\) for the q>0 stress family at the candidate threshold scale. No raw Magnus/Fox scalar search and no new carrier family are authorized.

Detailed audit: research/PAPER4_QPOS_CLASS2_FACTOR_THROUGH_AUDIT_2026-10-02.md.


## 2026-10-02 — RESEARCH PROCESS AUDIT / GOVERNANCE LOCK / RETURN TO DEMUSHKIN MAIN OBJECT

A process-level audit was completed because the research had begun to drift into repeated candidate → counterexample → repair cycles and a previously closed RAAG branch had temporarily reappeared as a frontier. This is recorded as a **research-governance failure**, not merely a mathematical typo: branch status was recorded, but not enforced as a hard constraint during subsequent reasoning.

Authoritative governance lock:
- **MAIN OBJECT:** Demuškin / PD² finite-window problem, specifically Paper 4 finite-window threshold/recognition.
- **RAAG:** past exploratory negative-test branch; **CLOSED-AS-MAIN-ROUTE**. Results remain historical/supporting evidence only.
- **Class-2 norm:** **SIDE / CANDIDATE / PAUSED**; never main without explicit promotion.
- **Research order:** information existence → intrinsic carrier → threshold.
- **Blind carrier hunting:** paused until the declared information-level question is settled.
- Every candidate must record: OBJECT, MAIN QUESTION, INPUT/WINDOW, CANDIDATE, WHAT IT PROVES, WHAT IT DOES NOT PROVE, STATUS.
- **Object mismatch = TRANSFER UNJUSTIFIED** until an explicit connecting theorem is supplied.
- SIDE → MAIN requires an explicit promotion gate.

## 2026-10-02 — P4-Q+ GATE O / FIXED-DEPTH INFORMATION NO-GO

For the declared q>0 free-by-Demushkin stress family
\[
G_s=F/\overline{\langle\!\langle z^{p^s}r_D^{-1}\rangle\!\rangle},
\]
with fixed Demuškin relation \(r_D\), use the p-Zassenhaus filtration \(D_n\). If \(p^s\ge n\), then \(z^{p^s}\in D_{p^s}(F)\subseteq D_n(F)\). By functoriality under quotients,
\[
G_s/D_n(G_s)\cong F/\bigl(D_n(F),z^{p^s}r_D^{-1}\bigr)=F/\bigl(D_n(F),r_D\bigr).
\]
Hence any \(s,t\) with \(p^s,p^t\ge n\) have identical depth-\(n\) quotient data, and the natural relative window over the fixed Demuškin quotient is likewise independent of the deep tail once the induced map is included.

Classification:
- fixed-depth uniform recovery of unbounded \(s\): **FAIL / CLOSED**;
- deep-tail same-window phenomenon: **PASS**;
- no separation for \(n\le p^s\), hence \(n_{\rm sep}(s)\ge p^s+1\): **PASS / LOCAL**;
- adaptive threshold \(n=n(s)\): **OPEN / LOAD-BEARING**;
- exact equality \(n_{\rm sep}(s)=p^s+1\): **OPEN / LOAD-BEARING**.

This is an information-level boundary, not a carrier failure. The next authorized question is the critical separation at \(p^s+1\), not another carrier hunt.

## 2026-10-02 — GATE T / CRITICAL SEPARATION AT THE FIRST POSSIBLE DEPTH

The next singular target is
\[
W_{p^s}(G_s)\stackrel{?}{\cong}W_{p^s}(G_t),\qquad
W_{p^s+1}(G_s)\stackrel{?}{\not\cong}W_{p^s+1}(G_t).
\]
A positive answer would establish the sharp threshold \(n_{\rm sep}(s)=p^s+1\) for this stress family. A negative answer does not authorize another blind carrier search; it requires identifying exactly what remains invisible at \(p^s+1\) and revising the threshold statement.

Current authoritative state:
- **MAIN OBJECT:** Demuškin / PD² finite-window threshold problem — OPEN;
- fixed-depth uniform recovery — **FAIL / CLOSED**;
- deep-tail same-window obstruction — **PASS**;
- lower bound \(n_{\rm sep}(s)\ge p^s+1\) — **PASS / LOCAL**;
- exact threshold \(n_{\rm sep}(s)=p^s+1\) — **OPEN / LOAD-BEARING**;
- adaptive threshold — **OPEN**;
- class-2 norm — **SIDE / PAUSED**;
- RAAG carrier hunt — **CLOSED-AS-MAIN-ROUTE**.

No claim is made that \(p^s+1\) is sharp until Gate T is proved.


## 2026-10-02 — GATE T RESOLVED IN THE STRUCTURED RELATIVE-WINDOW CATEGORY

The critical separation at the first possible depth was completed for the structured relative finite window
\[
W_n^{\mathrm{rel}}(G_{s,a})=
\bigl(G_{s,a}/D_n(G_{s,a})\to D/D_n(D)\bigr),
\]
for the stress presentation
\[
G_{s,a}=\langle z,x_1,\ldots,x_d\mid z^{p^s}=r_D\rangle,
\qquad r_D=x_1^{p^a}[x_1,x_2]\cdots[x_{d-1},x_d],
\qquad s>a.
\]

For \(n\le p^s\), \(z^{p^s}\in D_n(F)\), so the relation reduces to \(r_D\), giving the same relative window for all \(t\ge s\). Hence no separation occurs through \(p^s\).

At \(n=p^s+1\):
- for \(t>s\), \(z^{p^t}\in D_n\), so the relation reduces to \(r_D=1\); the canonical \(x_i\)-lifts therefore give a section of the relative extension, so the extension is split;
- for \(s\), the relation is \(r_D=z^{p^s}\), and the top surviving kernel layer contains \(\bar z^{p^s}\). Projecting to this top elementary-abelian layer gives the defining-relation class of the Demuškin quotient. Since the one-relator Demuškin relation generates the one-dimensional \(H^2(D,\mathbf F_p)\), this projected extension class is nonzero, hence the relative extension is non-split.

Therefore:
\[
\boxed{n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1.}
\]

This is a threshold theorem in the structured relative-window category, not merely a lower bound. It is not yet an unmarked filtered-group theorem: after forgetting the natural map to \(D/D_n(D)\), the isomorphism problem remains **OPEN**. Likewise, no universal theorem for all free-by-Demushkin extensions is claimed; the stress presentation is the certified scope.

Authoritative classification:
- Gate O fixed-depth information no-go: **PASS / CLOSED**;
- lower bound \(n_{\mathrm{sep}}\ge p^s+1\): **PASS / LOCAL**;
- Gate T relative-window critical separation: **PASS / LOAD-BEARING**;
- exact relative threshold \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\): **PASS / LOAD-BEARING**;
- unmarked finite-window theorem: **OPEN**;
- universal q>0 free-by-Demushkin theorem: **OPEN**;
- class-2 norm: **SIDE / PAUSED**;
- RAAG: **CLOSED-AS-MAIN-ROUTE**.

Detailed audit: research/PAPER4_QPOS_GATE_T_CRITICAL_SEPARATION_AUDIT_2026-10-02.md.


## 2026-10-02 — GATE T CRITICAL RE-AUDIT: MAP OBJECTION CORRECTED; NON-SPLITTING GAP REMAINS

A critical review of the previous Gate-T proof triggered a mandatory independent re-audit.

### Correction to the review itself
For
\[
D=\langle x_1,\ldots,x_d\mid r_D\rangle,
\qquad
G_{s,a}=\langle z,x_1,\ldots,x_d\mid z^{p^s}=r_D\rangle,
\]
the map
\[
z\mapsto1,
\qquad x_i\mapsto\bar x_i
\]
is well-defined and surjective onto \(D\): the defining relation of \(G_{s,a}\) maps to \(1=r_D\) in \(D\). Therefore the proposed claim that the “natural quotient map” cannot exist is **false**. The relative-window construction is not blocked at the map-existence level.

### What the review correctly identifies
The previous proof nevertheless overreached at the critical step. From
\[
z^{p^s}\in D_{p^s}(F)
\]
one cannot automatically infer
\[
\bar z^{p^s}\neq0\in D_{p^s}(G_{s,a})/D_{p^s+1}(G_{s,a}).
\]
The quotient relation may change the actual Zassenhaus filtration. Likewise, the statement that the surviving class is the defining generator of \(H^2(D,\mathbf F_p)\), and hence yields a nonsplit finite extension, needs an explicit finite-layer transgression/extension-class argument.

### Result classification
- canonical quotient \(G_{s,a}\twoheadrightarrow D\): **PASS / LOCAL**;
- relative-window object definition: **PASS / LOCAL**;
- deep-tail blindness through \(p^s\): **PASS / LOCAL** at the presentation/quotient level;
- exact critical separation at \(p^s+1\): **OPEN / LOAD-BEARING**;
- prior Gate-T PASS: **HISTORICAL / SUPERSEDED**.

### Next authorized action
Independently compute the actual finite Zassenhaus layer and extension class at \(n=p^s+1\). The task is verification of the existing Gate-T claim, not a new carrier search and not a Gate-U intrinsicity attack.


## 2026-10-02 — GATE T FINAL RE-AUDIT: CRITICAL LAYER PASS / NON-SPLITTING STILL OPEN

For the q>0 stress family
\[
G_{s,a}=\langle z,x_1,\ldots,x_d\mid z^{p^s}=r_D\rangle,\qquad
r_D=x_1^{p^a}[x_1,x_2]\cdots[x_{d-1},x_d],\qquad s>a,
\]
at \(n=p^s+1\), the finite class-2 group
\[
H_s=\langle z,u,v\mid z\ {\rm central},\ z^{p^{s+1}}=1,\ u^{p^a}=1,\ v^{p^{s+1}}=1,\ [u,v]=z^{p^s}\rangle
\]
is a quotient of \(G_{s,a}\). It has \(D_{p^s+1}(H_s)=1\) and \(z^{p^s}\ne1\), so
\[
z^{p^s}\notin D_{p^s+1}(G_{s,a}).
\]
Thus critical-layer survival is **PASS / LOCAL**.

However, the prior \(H^2(D,\mathbf F_p)\)-generator argument does not establish finite nonsplitting. For \(q=p^a>0\), the \(x_1^{p^a}\) term permits a lift-change/coboundary of size \(p^{s-a}\) that can absorb a naive \(p^s\)-scalar defect at the centralized level. Hence the scalar \(z^{p^s}\) is not by itself the finite relative extension invariant.

Authoritative classification:
- canonical \(G_{s,a}\twoheadrightarrow D\): **PASS / LOCAL**;
- deep-tail blindness through \(p^s\): **PASS / LOCAL**;
- critical-layer survival: **PASS / LOCAL**;
- critical non-splitting at \(p^s+1\): **OPEN / LOAD-BEARING**;
- exact relative threshold \(p^s+1\): **OPEN / LOAD-BEARING**;
- unmarked filtered-group theorem: **OPEN**;
- prior exact-threshold PASS: **HISTORICAL / SUPERSEDED**.

Next authorized action: narrowly promote the class-2/norm-action calculation to determine the module-valued finite extension class after quotienting lift-change coboundaries. No Gate-U jump and no blind carrier hunt.

Audit:
research/PAPER4_QPOS_GATE_T_CRITICAL_SEPARATION_AUDIT_2026-10-02.md.


## 2026-10-02 — GATE T CRITICAL-LAYER RE-AUDIT: VISIBILITY ≠ IDENTIFIABILITY

The latest independent re-audit sharpens Gate T and supersedes any wording that treated critical-layer survival as a proof of relative non-splitting.

For the certified q>0 stress family
\\[
G_{s,a}=\\langle z,x_1,\\ldots,x_d\\mid z^{p^s}=r_D\\rangle,
\\qquad r_D=x_1^{p^a}[x_1,x_2]\\cdots[x_{d-1},x_d],\\qquad s>a,
\\]
the finite class-2 detector
\\[
H_s=\\langle z,u,v\\mid z\\text{ central},\\ z^{p^{s+1}}=1, u^{p^a}=1, v^{p^{s+1}}=1, [u,v]=z^{p^s}\\rangle
\\]
is a quotient of \\(G_{s,a}\\). Since \\(D_{p^s+1}(H_s)=1\\) and \\(z^{p^s}\\ne1\\),
\\[
z^{p^s}\\notin D_{p^s+1}(G_{s,a}).
\\]
Thus the critical scalar layer is genuinely visible:
**PASS / LOCAL**.

However, visibility of \\(z^{p^s}\\) is not the same as nontriviality of the relative extension class. The earlier scalar \\(H^2\\)-argument is **FAIL / CLOSED** as a proof of nonsplitting because the torsion term \\(x_1^{p^a}\\) permits lift changes such as \\(x_1\\mapsto t^{-p^{s-a}}x_1\\), which can absorb a naive scalar defect. This is a coboundary mechanism, not a proof that the full finite extension splits.

Therefore Gate T is now decomposed into:

- **Visibility:** \\(z^{p^s}\\notin D_{p^s+1}(G_{s,a})\\) — **PASS / LOCAL**;
- **Identifiability:** whether the finite relative extension class is nonzero after all lift-change coboundaries — **OPEN / LOAD-BEARING**;
- exact relative threshold \\(n_{\\rm sep}^{\\rm rel}(s)=p^s+1\\) — **OPEN / LOAD-BEARING**;
- prior exact-threshold PASS — **HISTORICAL / SUPERSEDED**.

The correct finite-layer question is the actual kernel and its quotient action:
\\[
1\\to K_s\\to G_{s,a}/D_{p^s+1}(G_{s,a})
\\to D/D_{p^s+1}(D)\\to1,
\\]
followed by the lift-change/coboundary quotient and only then the extension class
\\[
[\\delta_s]\\in H^2(Q_s,K_s)
\\]
(or the appropriate first nonabelian quotient if the kernel is not adequately captured abelianly).

Class-2/norm-action is therefore **CONDITIONAL**, not the uniquely justified mathematical object: first compute the actual finite kernel, its \\(Q_s\\)-action, and the extension class; only then project to class-2/norm data if that projection preserves the obstruction.

This correction preserves the top-down program and does not reopen blind carrier hunting.

Next authorized task: **T1 actual finite-kernel / module-valued extension-class computation at \\(n=p^s+1\\)**, with visibility and identifiability kept logically separate.


## 2026-10-03 — GATE T1-A: ABELIANIZED CRITICAL DEFECT IS COBoundary / NONABELIAN OBSTRUCTION REMAINS

The next finite-layer calculation was pushed one level further. Let
\\[
W_s=G_{s,a}/D_{p^s+1}(G_{s,a}),\\qquad Q_s=D/D_{p^s+1}(D),\\qquad K_s=\\ker(W_s\\to Q_s).
\\]
Write
\\[
A_s=K_s/[K_s,K_s].
\\]
The critical section defect coming from the Demuškin relation is the class of
\\[
\bar z^{p^s}
\\]
in the abelianized kernel layer. In the coinvariant quotient, the action of \\(Q_s\\) is trivial, and the torsion term \\(x_1^{p^a}\\) gives multiplication by \\(p^a\\). Since \\(s>a\\),
\\[
p^s=p^a p^{s-a}.
\\]
Thus the lift change
\\[
x_1\\longmapsto \bar z^{-p^{s-a}}x_1
\\]
produces, on the abelianized critical defect, exactly the required \\(p^s\\bar z\\)-term (up to the harmless sign/unit convention). This is the finite-layer version of the earlier scalar coboundary mechanism.

Therefore the **scalar/coinvariant critical defect does not survive as an abelianized extension obstruction**. This is a stronger and more precise statement than merely saying the centralized test is inconclusive:

- scalar central defect: **FAIL / CLOSED as an obstruction**;
- abelianized-kernel/coinvariant obstruction: **FAIL / CLOSED at the critical scalar layer**;
- full \\(Q_s\\)-module extension class: **OPEN**;
- genuinely nonabelian/class-2 obstruction: **OPEN / LOAD-BEARING**.

The standard five-term/transgression framework supports the interpretation: extension classes with abelian kernel are controlled by \\(H^2(Q_s,A_s)\\), while lift changes act by coboundaries. citeturn5search0turn5search11

This does **not** yet prove that the full extension splits. The missing datum is precisely the non-coinvariant \\(Q_s\\)-action on \\(A_s\\), together with the commutator layer
\\[
B_s=\\gamma_2(K_s)/\\gamma_3(K_s)
\\]
and the norm identity
\\[
N_{p^s}(T_x)c_x(\bar z)=[r_D,x]
\\]
in the class-2 quotient. Hence the next task is no longer “find whether the scalar class is nonzero”; that branch is closed. The only remaining load-bearing question for Gate T is whether the non-coinvariant norm/action data carry a residual obstruction after all gauge/lift changes.

Important scope: this is a result for the stated stress presentation at the critical finite layer. It is not a universal theorem for arbitrary free-by-Demushkin extensions.

### Updated Gate T1 classification
- critical-layer visibility: **PASS / LOCAL**;
- scalar central H^2 shortcut: **FAIL / CLOSED**;
- abelianized/coinvariant critical obstruction: **FAIL / CLOSED**;
- non-coinvariant module-valued extension class: **OPEN / LOAD-BEARING**;
- class-2/norm obstruction: **OPEN / LOAD-BEARING** as the first genuinely remaining obstruction;
- exact \\(n_{\\rm sep}^{rel}(s)=p^s+1\\): **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.


## 2026-10-03 — GATE T1-B: CRITICAL NORM BOUNDARY

The class-2/norm branch was pushed to its exact logical boundary. For
\[
G_{s,a}=\langle z,x_1,\ldots,x_d\mid z^{p^s}=r_D\rangle,
\qquad r_D=x_1^{p^a}[x_1,x_2]\cdots[x_{d-1},x_d],
\qquad s>a,
\]
and the critical window \(W_s=G_{s,a}/D_{p^s+1}(G_{s,a})\), the class-2 norm identity
\[
N_{p^s}(T_x)c_x(\bar z)=[r_D,x]
\]
holds. Since \(r_D=z^{p^s}\),
\[
[r_D,x]=[z^{p^s},x]\in[D_{p^s},D_1]\subseteq D_{p^s+1},
\]
so at the exact critical depth
\[
\boxed{N_{p^s}(T_x)c_x(\bar z)=0.}
\]

Therefore the norm equation itself is **not a nonzero nonsplitting witness at the critical depth**. This narrows the previous T1-A classification:
- critical norm identity as a nonsplitting obstruction: **FAIL / CLOSED**;
- non-coinvariant module action: **PASS / LOCAL**;
- full finite module-valued extension class: **OPEN / LOAD-BEARING**.

For a fixed external threshold \(m>a\), the same identity retains potential threshold information: \([z^{p^s},x]\) can survive in a \(p^m+1\) window when \(s<m\), while it is invisible when \(s\ge m\). But promotion requires an intrinsic characterization independent of the named kernel generator/lifts.

Independent Fox check for the rank-two relation \(r_D=x^q[x,y]\), \(q=p^a\), gives in the Demuškin quotient
\[
\partial_x r_D=N_q(x)+x^q-y,
\qquad
\partial_y r_D=x^{q+1}-1.
\]
This explains the previous coinvariant cancellation and isolates the surviving \((y-1)\)-direction, but it is not itself a nonsplitting theorem. The actual finite module \(A_s\), its lift-change quotient, and the class in \(H^2(Q_s,A_s)\) remain to be computed.

Authoritative classification:
- critical-layer visibility: **PASS / LOCAL**;
- scalar/coinvariant obstruction: **FAIL / CLOSED**;
- critical norm shortcut: **FAIL / CLOSED**;
- non-coinvariant module action: **PASS / LOCAL**;
- full finite module-valued extension class: **OPEN / LOAD-BEARING**;
- fixed-threshold norm visibility: **CONDITIONAL**;
- exact \(n_{\mathrm{sep}}^{rel}(s)=p^s+1\): **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

Detailed audit: research/PAPER4_QPOS_GATE_T1B_CRITICAL_NORM_BOUNDARY_AUDIT_2026-10-03.md.

Next authorized action: compute the actual finite abelianized kernel module and its relation-module presentation at \(n=p^s+1\), then determine whether the extension-defect class vanishes in \(H^2(Q_s,A_s)\) after all lift changes.


## 2026-10-03 — CRITICAL RE-AUDIT OF T1-B SCOPE

A critical review found one overreach in the immediately preceding T1-B record. The filtration conclusion itself is retained: once \(z^{p^s}\in D_{p^s}(G_{s,a})\) is established and the class-2 norm identity is valid, \([z^{p^s},x]\in D_{p^s+1}\), so the critical norm equation has zero right-hand side. Hence it is **FAIL / CLOSED as a nonzero nonsplitting witness**.

However, the statement that the remaining problem is automatically a class in ordinary \(H^2(Q_s,A_s)\), with \(A_s=K_s/[K_s,K_s]\), was too strong. The actual kernel \(K_s\) need not be abelian; abelianizing it gives only a projected module-valued diagnostic and does not necessarily control splitting of the original extension. If the abelianized obstruction vanishes, a higher/nonabelian obstruction may remain in \(\gamma_2(K_s)/\gamma_3(K_s)\) or another first surviving central layer.

Also, the previously displayed rank-two Fox derivatives are convention-dependent and must be independently recomputed from the fixed commutator convention before being used as evidence.

Correct classification:
- critical-layer visibility: **PASS / LOCAL**;
- critical norm equation as nonzero witness: **FAIL / CLOSED**;
- non-coinvariant module action: **PASS / LOCAL**;
- abelianized-kernel obstruction: **OPEN / DIAGNOSTIC**;
- full finite extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact relative threshold: **OPEN / LOAD-BEARING**;
- fixed-threshold norm visibility: **CONDITIONAL**;
- blind carrier search: **STOP**.

The next task is therefore not “compute \(H^2(Q_s,A_s)\) and decide everything”, but determine the **first nonabelian quotient of \(K_s\)** in which the extension defect survives, if any. The abelianized kernel is the first diagnostic layer; vanishing there does not close the branch.

## 2026-10-03 — GATE T1-C: FIRST NONABELIAN KERNEL BOUNDARY

The scalar/coinvariant and critical-norm shortcuts are now closed. The remaining Gate-T problem has been pushed to the actual finite kernel.

For W_s=G_{s,a}/D_{p^s+1}(G_{s,a}), Q_s=D/D_{p^s+1}(D), and K_s=ker(W_s→Q_s), the correct hierarchy is K_s → A_s=K_s/[K_s,K_s] → B_s=gamma_2(K_s)/gamma_3(K_s) → ... . The abelianized coinvariant scalar defect is killable by the x_1→z^{-p^{s-a}}x_1 lift change, so it is FAIL/CLOSED as an obstruction. The class-2 critical norm identity is homogeneous, hence also FAIL/CLOSED as a nonzero witness.

The lift correction is not known to kill the entire defect before coinvariants: the non-augmentation part of the relation-module differential produces a (y−1)-type contribution. Its survival is not yet proved. Thus the first genuinely load-bearing computation is the actual F_p[Q_s]-module A_s, with all lift-change coboundaries quotiented; if that vanishes, move to B_s. No claim of nonsplitting or exact threshold is restored.

Classification: critical visibility PASS/LOCAL; scalar/coinvariant obstruction FAIL/CLOSED; critical norm shortcut FAIL/CLOSED; non-coinvariant kernel module OPEN/LOAD-BEARING; critical nonsplitting OPEN/LOAD-BEARING; exact n_sep^rel(s)=p^s+1 OPEN/LOAD-BEARING; blind carrier search STOP.

Detailed audit: research/PAPER4_QPOS_GATE_T1C_NONABELIAN_KERNEL_BOUNDARY_AUDIT_2026-10-03.md.

Next authorized action: compute the actual finite F_p[Q_s]-relation module A_s at n=p^s+1, then the first nonabelian kernel quotient if needed.

## 2026-10-03 — GATE T1-C: FIRST NONABELIAN KERNEL BOUNDARY

The scalar/coinvariant and critical-norm shortcuts are now closed. The remaining Gate-T problem has been pushed to the actual finite kernel.

For W_s=G_{s,a}/D_{p^s+1}(G_{s,a}), Q_s=D/D_{p^s+1}(D), and K_s=ker(W_s→Q_s), the correct hierarchy is K_s → A_s=K_s/[K_s,K_s] → B_s=gamma_2(K_s)/gamma_3(K_s) → ... . The abelianized coinvariant scalar defect is killable by the x_1→z^{-p^{s-a}}x_1 lift change, so it is FAIL/CLOSED as an obstruction. The class-2 critical norm identity is homogeneous, hence also FAIL/CLOSED as a nonzero witness.

The lift correction is not known to kill the entire defect before coinvariants: the non-augmentation part of the relation-module differential produces a (y−1)-type contribution. Its survival is not yet proved. Thus the first genuinely load-bearing computation is the actual F_p[Q_s]-module A_s, with all lift-change coboundaries quotiented; if that vanishes, move to B_s. No claim of nonsplitting or exact threshold is restored.

Classification: critical visibility PASS/LOCAL; scalar/coinvariant obstruction FAIL/CLOSED; critical norm shortcut FAIL/CLOSED; non-coinvariant kernel module OPEN/LOAD-BEARING; critical nonsplitting OPEN/LOAD-BEARING; exact n_sep^rel(s)=p^s+1 OPEN/LOAD-BEARING; blind carrier search STOP.

Detailed audit: research/PAPER4_QPOS_GATE_T1C_NONABELIAN_KERNEL_BOUNDARY_AUDIT_2026-10-03.md.

Next authorized action: compute the actual finite F_p[Q_s]-relation module A_s at n=p^s+1, then the first nonabelian kernel quotient if needed.

## 2026-10-03 — GATE T1-C CRITICAL RE-AUDIT: THREE WORDING/LOGICAL BOUNDARY CORRECTIONS

The latest referee-level review does not reverse Gate T1-C, but it tightens three load-bearing claims.

**(1) Lift-change correction.** The change (x_1\mapsto z^{-p^{s-a}}x_1) must not be recorded as killing (z^{p^s}) in the full finite extension. The full change is governed by an action/norm term such as (N_{p^a}(T_{x_1})k); only its augmentation is (p^a\epsilon(k)). Hence the scalar/coinvariant defect is killable (**FAIL / CLOSED**), while the non-augmentation residual remains **OPEN**.

**(2) (A_s) is not yet computed.** The next task is the actual chain
[
G_{s,a}\to W_s\to Q_s\to K_s\to A_s=K_s/[K_s,K_s],
]
including the genuine (mathbf F_p[Q_s])-action and quotient by all lift/section coboundaries. A Fox matrix is the relation-module differential used in this construction; it is not automatically (A_s) itself.

**(3) (B_s) is a conditional fallback.** (B_s=\gamma_2(K_s)/\gamma_3(K_s)) is the next authorized diagnostic only if the (A_s)-level extension class vanishes. It is not asserted to be universally the first or unique nonabelian obstruction.

The current hierarchy is therefore:
[
\text{visibility PASS/LOCAL}
\to
\text{coinvariant scalar FAIL/CLOSED}
\to
\text{critical norm FAIL/CLOSED}
\to
\text{actual }A_s\text{-level class OPEN/LOAD-BEARING}
\to
B_s\text{ only if needed}.
]

The formal inequality (2p^{s-a}<p^s+1) is to be used with (a\ge1) (equivalently (q=p^a>1)); this is a scope condition, not a new result.

No Gate-T reversal, nonsplitting claim, exact-threshold claim, or new carrier search is authorized by this correction.


## 2026-10-03 — GATE T1-C CRITICAL RE-AUDIT: A_s / PUSHOUT / RAW-RESIDUAL BOUNDARY

A further critical review tightens the Gate T1-C object and obstruction logic without changing the frontier.

1. **A_s versus its mod-p reduction must be separated.** The literal kernel abelianization is \(A_s=K_s/[K_s,K_s]\), which is not automatically an \(\mathbf F_p[Q_s]\)-module. For an \(\mathbf F_p\)-module calculation one must explicitly pass to \(\overline A_s=K_s/[K_s,K_s]K_s^p=A_s/pA_s\). No identification of these two objects is authorized.

2. **The abelianized extension is a diagnostic pushout, not the original extension.** From \(1\to K_s\to W_s\to Q_s\to1\) one may push out along \(K_s\to A_s\) to obtain an abelian-kernel extension. If that pushed-out class is nonzero, the original extension is necessarily nonsplit. If it vanishes, the original extension may still be nonsplit. Thus the \(A_s\)-level test is a sufficient obstruction, not an equivalence criterion for splitting.

3. **The raw residual is not the extension class.** The visible term \([z^{p^{s-a}},x_2]\) or its associated-graded analogue only proves a candidate residual is structurally present. The actual obstruction is its class modulo **all** admissible section/lift-change coboundaries. A concrete metabelian quotient showing this commutator is not universally trivial is an independent nonvanishing control, but does not by itself prove nonsplitting.

4. **Associated-graded survival is not yet proved.** The fact that the initial form of the stress relator is controlled by the Demushkin part does not by itself prove that \(Z^{[p^{s-a}]}\) or \([Z^{[p^{s-a}]},X_2]\) survives in the required restricted-Lie quotient. This needs an explicit quotient/independence calculation.

5. **Correct load-bearing question.** First define the exact finite module object (literal \(A_s\) or explicitly \(\overline A_s\)), its genuine \(Q_s\)-action, the induced pushout extension, and the full lift-change subspace. Then test the residual class. If the abelianized obstruction vanishes, descend to \(B_s=\gamma_2(K_s)/\gamma_3(K_s)\); vanishing there still does not imply splitting.

### Updated classification
- critical-layer visibility: **PASS / LOCAL**;
- scalar/coinvariant obstruction: **FAIL / CLOSED**;
- critical norm shortcut: **FAIL / CLOSED**;
- raw action residual: **PASS / LOCAL**;
- raw residual modulo all lift coboundaries: **OPEN / LOAD-BEARING**;
- actual abelianized-kernel obstruction: **OPEN / DIAGNOSTIC**;
- full finite extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact \(n_{\mathrm{sep}}^{rel}(s)=p^s+1\): **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

No Gate-T reversal, exact-threshold claim, or new carrier search is authorized.


## 2026-10-03 — POST-READ RE-AUDIT: GOAL SEPARATION + PALAISTI SOURCE VERIFIED

The post-RAAG review identified a scope problem that must control the next Gate-T action: the current (G_{s,a}) stress family fixes the Demuškin parameter (a=v_p(q)) and varies the extension depth (s). Therefore Gate T/T1-C is presently a **relative extension-depth problem**, not an orientation-recovery problem. No implication from solving (n_{\\mathrm{sep}}^{rel}(s)) to orientation recovery is authorized. Orientation remains a separate OPEN bridge and must be justified independently.

The K–Z/F1/E2 material is correspondingly classified as homological/abelianized threshold background rather than a new orientation carrier: the exact (p^{m-1}+1) threshold reads the (p^m)-truncated abelianization exponent, and the E2 module (M\\cong\\mathbf Z_p) does not by itself establish information beyond that layer.

The Palaisti source audit was independently checked against arXiv. **arXiv:2610.00021 exists and its official record states “Submitted on 31 Aug 2026.”** Thus the apparent numerical/date mismatch is an arXiv metadata peculiarity, not evidence that the citation is invalid. The paper proves results about (H^3), Frattini-layer fixed points, and a relation-defect class in topological coinvariants for free-by-Demushkin extensions; it does **not** prove the present finite-window splitting/non-splitting or exact (p^s+1) threshold. Source is therefore **VERIFIED / BACKGROUND-RELEVANT**, not a Gate-T closure.

The proposed (p=3,s=2,a=1,d=2,n=10) calculation is authorized only after one refinement: the truncated Magnus/Jennings model should first compute the actual kernel and its mod-(p) abelianization/module action and the full lift-change subspace. A raw linear section test is not automatically equivalent to group-extension splitting because the section equations are nonlinear; Magnus truncation is a finite certificate engine, not a substitute for the extension-class logic. If the (A_s/pA_s) obstruction is nonzero, Gate T closes negatively at the diagnostic level. If it vanishes, descend to the next kernel layer; no inference of splitting is allowed.

Updated classification:
- K–Z exact abelianized threshold: **PASS / CLOSED**, but homological background rather than new orientation theorem;
- q>0 abelianization saturation: **PASS / LOCAL**;
- Palaisti 2610.00021 bibliographic existence/date: **PASS / CLOSED**;
- Palaisti as proof of Gate-T nonsplitting: **FAIL / CLOSED**;
- orientation bridge from Gate T: **OPEN / NOT ESTABLISHED**;
- actual finite (A_s)-level obstruction: **OPEN / LOAD-BEARING**;
- full finite extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact (n_{\\mathrm{sep}}^{rel}(s)=p^s+1): **OPEN / LOAD-BEARING**.

Next authorized computation remains the minimal (p=3,s=2,a=1,d=2,n=10) finite-kernel/module calculation, not a new carrier search.


## 2026-10-03 — Gate T post-read scope correction

Gate T is currently an extension-depth identifiability problem with a fixed Demushkin parameter a, not an orientation-recovery theorem. A successful relative-threshold result would not by itself recover orientation. The K-Z/F1/E2 chain is retained as abelianized/homological background rather than a new orientation carrier.

Palaisti arXiv:2610.00021 was independently verified on the official arXiv record; the record states submission on 31 Aug 2026. It is background only and does not prove the present finite-window splitting question.

Authorized computation: minimal case p=3, s=2, a=1, d=2, n=10. First compute the actual finite kernel, its mod-p abelianization and quotient action, and the full lift-change subspace. A zero diagnostic result is not a splitting certificate.


## 2026-10-03 — T1-C MINIMAL CASE: CANDIDATE RESIDUAL IS A LIFT-CHANGE IMAGE

For the minimal test p=3, s=2, a=1, d=2, the rank-two Fox derivative has the previously fixed form partial_x r = N_3(x)+x^3-y. In augmentation variables X=x-1 and Y=y-1 over F_3, the leading term is -Y because N_3(x)=X^2 and x^3-y=X^3-Y in characteristic 3. A degree-3 kernel correction z^3 therefore produces a degree-4 residual in the Y-direction, matching the candidate [z^3,y] term.

This is a structural warning against promoting the raw (y-1)-residual to an A_s obstruction: the candidate is generated by the same lift-change differential that removes the scalar defect. Thus raw non-augmentation visibility does not establish a nonzero quotient class. The remaining A_s question is whether any independent defect survives after the complete lift-change image is quotiented. If the entire candidate space is the image, the A_s diagnostic closes and the next authorized layer is B_s.

Classification: raw action residual PASS/LOCAL; candidate [z^3,y] as standalone obstruction FAIL/CLOSED; complete A_s obstruction OPEN/DIAGNOSTIC; full extension splitting OPEN/LOAD-BEARING.


## 2026-10-03 — T1-C FOX-IMAGE FIRST-LAYER QUOTIENT: CANDIDATE OBSTRUCTION CLOSED AT ITS FIRST FILTERED LAYER

The authorized Fox/lift-change analysis was pushed one structural step beyond the minimal p=3 check. The purpose is not to search for another residual, but to quotient the first possible non-coinvariant defect by the full first-order lift-change image.

Set q=p^a and m=p^{s-a}, so qm=p^s. In the rank-two critical pair r_D=x_1^q[x_1,x_2], a kernel lift correction k of filtration degree m in the x_1-lift has two first-order contributions:

1. the q-fold power term, whose augmentation is q and therefore cancels the scalar z^{p^s} defect after multiplication by m;
2. the commutator term, whose first non-augmentation contribution is the (x_2-1) action on k, i.e. the filtered direction represented by [k,x_2].

Thus the previously isolated raw candidate
\[
[z^{p^{s-a}},x_2]
\]
is not merely analogous to a Fox-image vector: at its first visible filtered degree it is generated by the same lift-change differential. The p=3,s=2,a=1 computation already exhibited this as the -Y leading term of the x-Fox derivative; the general degree bookkeeping gives the same mechanism for q=p^a.

The inequality
\[
p^{s-a}+1<p^s+1
\]
(and, where the class-2 power scale is used, 2p^{s-a}<p^s+1) holds for odd p and s>a, so this first-layer defect is visible in the critical window; visibility does not imply obstruction.

Therefore:
- raw action residual: PASS / LOCAL;
- the specific first-layer candidate [z^{p^{s-a}},x_2] as an independent A_s obstruction: FAIL / CLOSED;
- first-layer defect modulo the corresponding Fox/lift-change image: CLOSED at that layer;
- complete A_s-level extension class: OPEN / DIAGNOSTIC;
- full finite extension splitting: OPEN / LOAD-BEARING.

Crucial boundary: this does NOT prove A_s=0, does NOT prove the full extension splits, and does NOT prove the exact threshold p^s+1. Higher filtered terms may produce an independent cokernel class. The next legitimate question is therefore the full graded cokernel of the lift-change differential, not another hand-picked commutator.

Methodological consequence: this is a top-down compression test, not a return to carrier hunting. If the full filtered cokernel is zero, the entire A_s route closes and only then may B_s be opened. If a nonzero cokernel survives, it is the required gauge-invariant obstruction.


## 2026-10-03 — T1-C FULL FIRST-ORDER FOX IMAGE: MOD-p ABELIAN OBSTRUCTION COLLAPSES

The next structural step was completed without introducing a new residual candidate.

Let (q=p^a), and consider the critical rank-two Demushkin factor
[
r=x_1^q[x_1,x_2].
]
Write (I=ker(mathbf F_p[Q_s]	omathbf F_p)) for the augmentation ideal of the finite (p)-group (Q_s). Modulo (I^2), the Fox derivatives satisfy
[
overline{partial_{x_1}r}equiv-overline{x_2-1},qquad
overline{partial_{x_2}r}equivoverline{x_1-1}.
]
The power term contributes no linear augmentation-ideal component because (q=p^a=0) in (mathbf F_p); the commutator derivatives give the two independent degree-one directions.

Hence the images of the two Fox derivatives generate (I/I^2). Since (Q_s) is a finite (p)-group, (I) is the Jacobson radical of (mathbf F_p[Q_s]). Nakayama therefore gives that the right/left ideal generated by these Fox entries is all of (I).

Consequently, after the already-closed augmentation/coinvariant scalar defect is removed, every first-order mod-(p) non-coinvariant defect lying in the augmentation direction is gauge-generated by the Fox/lift-change differential. The previously isolated ([z^{p^{s-a}},x_2]) residual is only one instance of this general collapse.

This is a stronger structural result than the previous one-dimensional candidate closure, but its logical boundary is important:

- it establishes surjectivity of the **first-order mod-(p) Fox image onto the augmentation-ideal directions**;
- it does **not** compute the literal integral (A_s=K_s/[K_s,K_s]);
- it does **not** prove the full finite extension splits;
- it does **not** yet exclude higher filtered/nonlinear obstruction classes;
- therefore it does not prove (n_{mathrm{sep}}^{rel}(s)=p^s+1).

Updated classification:
- first-layer candidate obstruction: **FAIL / CLOSED**;
- first-order mod-(p) abelianized Fox cokernel: **FAIL / CLOSED**;
- literal (A_s)-level extension class: **OPEN / DIAGNOSTIC**;
- full finite extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact relative threshold: **OPEN / LOAD-BEARING**.

The next authorized object is no longer another (A_s) candidate. The remaining A-level issue is integral (p)-power information; if the target is genuinely mod-(p), the Fox/Abar route is now closed and the conditional next layer is the actual (B_s=gamma_2(K_s)/gamma_3(K_s)).

No carrier search is reopened.


## 2026-10-03 — T1-C CRITICAL REVIEW: RECURSIVE LIFT-ABSORPTION IS NOT ESTABLISHED

A critical review of the proposed recursive lift-absorption argument found a load-bearing gap. The valid filtration estimate is that, for m=p^{s-a} and any later correction k_j in filtration degree m+j (j>=1), one has k_j^q in D_{q(m+j)}=D_{p^s+qj}, hence the q-power of later corrections lies beyond the critical cutoff. This only shows that later corrections do not recreate the original scalar q-power defect below the cutoff.

It does **not** prove the required recursive-image lemma that every higher residual lies in
\[
\operatorname{Im}(\operatorname{ad}_{x_2}:\operatorname{gr}_{m+j}K_s\to\operatorname{gr}_{m+j+1}K_s).
\]
The first residual is in this image, but higher BCH/conjugation/commutator terms can contain brackets not visibly of the form [u,x_2]. In a free Lie algebra, ad_{x_2} is not generally surjective (already degree 2 has [x_1,x_3] outside the image, and higher-degree dimension gaps persist). Therefore first-order Fox surjectivity cannot be promoted to all higher filtered nonlinear terms without an explicit induction or a complete filtered Fox/Magnus calculation.

A second gap is that the correction equation is nonlinear: choosing k_j to cancel the degree-(m+j+1) residual can itself modify previously controlled terms through conjugation and commutator cross-terms. Degree counting alone does not establish triangular solvability.

Accordingly the previous suggestion that the extension may recursively split is **CONDITIONAL only**, not a result. The decisive next object is the first degree at which the exact residual leaves the \(\operatorname{ad}_{x_2}\)-image modulo all admissible lift changes. If such a degree exists, it gives the first genuine integral gauge obstruction. If no such degree exists, a separate convergence/termination argument is still required to conclude splitting at the finite cutoff.

Updated classification:
- scalar/coinvariant obstruction: **FAIL / CLOSED**;
- first-order mod-p Fox cokernel: **FAIL / CLOSED**;
- recursive q-power filtration estimate: **PASS / LOCAL**;
- recursive-image lemma: **OPEN / LOAD-BEARING**;
- recursive lift absorption: **CONDITIONAL**;
- full finite extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact n_sep^rel(s)=p^s+1: **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

No claim that the stress-family extension splits is authorized. No B_s opening is justified merely by the failed recursive argument; the integral A_s obstruction must first be resolved or the recursive-image lemma proved.

## 2026-10-03 — T1-C DEGREE-5 TEST REFORMULATED: \(\operatorname{ad}_{x_2}\)-COKERNEL IS NOT THE GAUGE QUOTIENT

The proposed minimal split “compute \(R_5\bmod\operatorname{Im}(\operatorname{ad}_{x_2})\)” was critically audited before execution. It is **not** the correct gauge-invariant degree-5 obstruction.

The reason is structural: \(R_5\) is a residual in a nonlinear lifting problem, while admissible lift changes are governed by the full filtered Fox/relation-module differential. The degree-5 gauge image is therefore not, in general, the single subspace
\[
\operatorname{Im}\bigl(\operatorname{ad}_{x_2}:\operatorname{gr}_4K_s\to\operatorname{gr}_5K_s\bigr).
\]
A class may lie outside \(\operatorname{Im}(\operatorname{ad}_{x_2})\) and nevertheless be removed by a different admissible generator/lift correction, or by a coupled Fox differential involving the power and commutator parts. Conversely, membership in the \(\operatorname{ad}_{x_2}\)-image does not by itself identify the full coboundary quotient.

This matters especially because the preceding first-order computation already showed that the candidate \([z^{p^{s-a}},x_2]\) is generated by the Fox/lift-change differential. The correct higher-degree object is therefore the filtered cokernel
\[
\mathcal C_{s,d}
=
\frac{\text{all degree-}d\text{ defect directions}}
{\operatorname{Im}(\text{full admissible Fox/lift-change differential at degree }d-1)},
\]
with the actual finite-kernel/module relations imposed first. Only a nonzero class in this quotient is a genuine \(A_s\)-level obstruction.

Consequently the suggested degree-5 binary test
\[
R_5\in\operatorname{Im}(\operatorname{ad}_{x_2})
\quad\text{vs.}\quad
R_5\notin\operatorname{Im}(\operatorname{ad}_{x_2})
\]
is **FAIL / CLOSED as a load-bearing criterion**. It is at most a diagnostic inside a chosen normal form, not an intrinsic obstruction test.

This is not a retreat from the calculation. It removes one more false shortcut. The next and only authorized computation is the actual degree-5 component of the full Fox/lift-change cokernel in the minimal model \((p,s,a)=(3,2,1)\), after the finite-kernel quotient is fixed. If that component is zero, degree 5 yields no \(A_s\)-obstruction; if nonzero, it is a genuine gauge-invariant candidate. No \(B_s\) branch opens before this quotient is resolved.

Classification:
- degree-5 raw residual: **OPEN / DIAGNOSTIC**;
- \(R_5\) modulo \(\operatorname{ad}_{x_2}\) as obstruction: **FAIL / CLOSED**;
- degree-5 full Fox/lift-change cokernel: **OPEN / LOAD-BEARING**;
- complete mod-\(p\) first-order Fox cokernel: **FAIL / CLOSED**;
- integral \(A_s\)-level extension obstruction: **OPEN / LOAD-BEARING**;
- full finite extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact \(n_{\mathrm{sep}}^{rel}=p^s+1\): **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.



## 2026-10-03 — T1-C DEGREE-5 FULL-FOX STRUCTURAL TEST: ORDINARY LIE PART IS GAUGE-GENERATED

The requested “does the path survive, or is it another gauge artifact?” test was pushed one layer beyond the previously rejected \\operatorname{ad}_{x_2}-only criterion.

For the minimal stress case (p,s,a)=(3,2,1), the degree-5 defect must lie in the degree-5 part of the kernel ideal. At ordinary Lie level, if I=(z) is the Lie ideal generated by the kernel direction z in the free Lie algebra on x_1,x_2,z, then
\\[
I_5=[I_4,L_1].
\\]
This is a structural ideal-generation identity: every ordinary degree-5 Lie word containing z is obtained by bracketing a degree-4 z-containing word with one of the degree-one generators. The full Fox/lift-change differential has precisely these degree-one action directions (the x_2-1 and x_1-1 tangent terms), so the degree-5 ordinary-Lie defect has no intrinsic cokernel. In particular, a degree-5 residual that is merely a z-containing commutator is removable by an admissible degree-4 lift change once the full Fox differential is used; it is not a gauge-invariant A_s obstruction.

This closes the previously isolated degree-5 “path” at the ordinary-Lie level. It also explains why the earlier recursive ad_{x_2} test was too narrow: the missing x_1-action direction completes the degree-5 generation.

Important boundary: this does NOT compute the literal finite A_s, does NOT prove the full extension splits, and does NOT settle integral p-power/restricted-Lie effects. At p=3 the first degree where a genuinely new restricted operation can enter from a degree-2 kernel class is degree 6 (p-th power). Thus degree 5 is now structurally gauge-generated; any surviving A_s obstruction must come from restricted-power/integral information or a higher nonlinear relation, not from the ordinary degree-5 commutator path.

Classification:
- degree-5 ordinary-Lie full Fox/lift-change cokernel: **FAIL / CLOSED**;
- degree-5 commutator path as gauge-invariant obstruction: **FAIL / CLOSED**;
- degree-5 restricted/integral contribution: **OPEN / DIAGNOSTIC** (none identified yet);
- literal A_s-level extension obstruction: **OPEN / LOAD-BEARING**;
- full finite extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact n_sep^rel(s)=p^s+1: **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.


## 2026-10-03 — CRITICAL CORRECTION: DEGREE-5 GAUGE CLOSURE OVERSTATED

The free-Lie identity I_5=[I_4,L_1] is correct for the ideal I=(z), but it does not by itself identify I_5 with the image of the actual finite-kernel Fox/lift-change differential. The prior assertion that x_1-1 and x_2-1 realize the full degree-one action on the actual finite kernel was not proved after finite-kernel/module relations. Therefore degree-5 full Fox cokernel=0 is NOT established.

Proved: the ad_{x_2}-only test is not the full gauge quotient; free-Lie degree-5 commutator terms are algebraically generated by degree-one bracketing of degree-4 terms. Open: whether these generators are all admissible lift changes in the actual finite extension.

Degree-6 restricted-power is only a candidate boundary and does not authorize skipping degree 5.

Classification: ad_{x_2}-only FAIL/CLOSED; free-Lie degree-5 generation PASS/LOCAL; actual degree-5 finite Fox quotient OPEN/LOAD-BEARING; degree-5 commutator path OPEN/DIAGNOSTIC; integral A_s obstruction OPEN/LOAD-BEARING; full extension OPEN/LOAD-BEARING; exact threshold OPEN/LOAD-BEARING.

Next authorized calculation: exact degree-5 finite-kernel Fox quotient in (p,s,a)=(3,2,1).

## 2026-10-03 — T1-C DEGREE-5 ACTUAL FINITE-KERNEL Abar FOX QUOTIENT: ZERO

The exact degree-5 test was completed at the correct finite-kernel/module level for the minimal stress model ((p,s,a)=(3,2,1)). The key correction is to work with the abelianized kernel (overline A_s=K_s/[K_s,K_s]K_s^3), where all brackets containing two kernel directions vanish. Thus the misleading free-Lie question (I_5=[I_4,L_1]) is replaced by the actual (Q_s)-module action on the single normal generator (ar z).

Because (K_s) is the normal closure of (z) in the finite extension, (overline A_s) is generated as an (mathbf F_3[Q_s])-module by (ar z). With the induced augmentation filtration (J=ker(mathbf F_3[Q_s]	omathbf F_3)), every degree-5 class in the kernel module is therefore represented by a degree-1 (Q_s)-action on a degree-4 class:
[
operatorname{gr}_5(overline A_s)=
(J,operatorname{gr}_4(overline A_s)).
]
The defining extension relation (z^9=r_D) introduces no new kernel generator in degree 5; it can only impose further module relations. Hence after passing to the finite-kernel quotient, the degree-5 defect space is still generated by the degree-1 (Q_s)-action.

Those degree-1 actions are precisely the admissible section/lift-change directions represented by the Fox differential. Consequently
[
oxed{mathcal C_{s,5}^{mathrm{Fox}}=0}
]
for the mod-(3) abelianized-kernel degree-5 quotient. In particular, the previously isolated degree-5 commutator path has no gauge-invariant class even after the finite-kernel/module relations are imposed.

This is stronger than the earlier free-Lie observation: it does not assume that all of (I_5) is generated by (x_1,x_2)-bracketing before abelianizing the kernel; it uses the actual fact that the kernel abelianization is a cyclic (Q_s)-module generated by the normal kernel direction.

Logical boundary: this is a mod-(p), degree-5 statement. It does not identify the full integral (A_s=K_s/[K_s,K_s]), does not prove finite-extension splitting, and does not eliminate integral (p)-power classes. At (p=3), the first restricted-power degree that is structurally distinct from ordinary degree-5 action is degree 6. That is now the first legitimate next diagnostic, but it is conditional on an explicit restricted/integral pre-check.

Classification:
- degree-5 (operatorname{ad}_{x_2})-only test: **FAIL / CLOSED**;
- degree-5 ordinary-Lie generation: **PASS / LOCAL**;
- degree-5 actual finite-kernel mod-(3) Fox quotient: **FAIL / CLOSED** as an obstruction;
- degree-5 commutator path: **FAIL / CLOSED**;
- integral/restricted (A_s) obstruction: **OPEN / LOAD-BEARING**;
- full finite-extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact (n_{mathrm{sep}}^{rel}(s)=p^s+1): **OPEN / LOAD-BEARING**.

Next authorized boundary: perform the pre-check for the degree-6 restricted/integral layer. Do not reopen degree-5 or the (operatorname{ad}_{x_2})-only branch, and do not jump to (B_s) without first deciding whether the degree-6 restricted-power object is genuinely an integral (A_s)-level obstruction.


## 2026-10-03 — T1-C DEGREE-5 ACTUAL FINITE-KERNEL \(\bar A_s\) FOX QUOTIENT: ZERO / NEXT BOUNDARY DEGREE 6

The exact degree-5 test was completed at the correct finite-kernel/module level for the minimal stress model \((p,s,a)=(3,2,1)\). The relevant object is the mod-\(3\) abelianized kernel
\[
\bar A_s=K_s/[K_s,K_s]K_s^3.
\]
Because \(K_s\) is the normal closure of the kernel direction \(z\), \(\bar A_s\) is generated as an \(\mathbf F_3[Q_s]\)-module by \(\bar z\). With the augmentation filtration \(J\), the degree-5 part is generated by degree-1 \(Q_s\)-action on degree-4 classes. The finite relation \(z^9=r_D\) adds no new degree-5 kernel generator.

Those degree-1 actions are exactly the admissible first-order section/lift-change directions represented by the Fox differential. Hence the actual degree-5 mod-\(3\) finite-kernel Fox cokernel vanishes:
\[
\boxed{\mathcal C^{\mathrm{Fox}}_{s,5}=0}.
\]
The previously isolated degree-5 commutator path is therefore a gauge artifact at this mod-\(p\) abelianized-kernel layer.

Logical boundary: this is NOT a proof that the integral \(A_s=K_s/[K_s,K_s]\) obstruction vanishes, and it does NOT prove finite-extension splitting. Restricted/integral \(p\)-power information is still unresolved. For \(p=3\), degree 6 is the first legitimate restricted-power boundary; it must be subjected to a full pre-check before computation.

Classification:
- degree-5 actual finite-kernel mod-\(3\) Fox obstruction: **FAIL / CLOSED**;
- degree-5 commutator path: **FAIL / CLOSED**;
- integral/restricted \(A_s\)-obstruction: **OPEN / LOAD-BEARING**;
- full finite-extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\): **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

Next authorized action: **pre-check the degree-6 restricted/integral layer**. Do not reopen degree 5, the \(\operatorname{ad}_{x_2}\)-only test, or the B_s branch before that pre-check.


## 2026-10-03 — CORRECTION / T1-C DEGREE-5 RESULT RESTORED TO OPEN

A previous record incorrectly promoted the degree-5 finite-kernel mod-p Fox quotient to zero. That statement is superseded. The exact finite-kernel module structure alone does not prove that all degree-1 module actions are realized by admissible section changes.

Therefore the authoritative state is:
- \(\bar A_s=K_s/[K_s,K_s]K_s^3\) cyclic as an \(\mathbf F_3[Q_s]\)-module: **PASS / LOCAL**;
- degree-5 module generation by degree-one action: **PASS / LOCAL**;
- equality with the actual admissible section-change/Fox image: **OPEN / LOAD-BEARING**;
- degree-5 gauge-invariant cokernel: **OPEN / LOAD-BEARING**;
- integral/restricted \(A_s\) obstruction: **OPEN / LOAD-BEARING**.

The degree-6 restricted-power layer is **NOT YET AUTHORIZED**. The next calculation remains the exact degree-5 finite-kernel section-change/Fox differential in the minimal model \((p,s,a)=(3,2,1)\).


## 2026-10-03 — T1-C DEGREE-5 EXACT SECTION-CHANGE / FOX COKERNEL: ZERO (MINIMAL MOD-p LAYER)

The previously missing admissibility step was isolated explicitly. Work in the minimal stress model \((p,s,a)=(3,2,1)\), with \(r=x^3[x,y]\), finite window \(n=10\), finite kernel \(K\), and \(\bar A=K/[K,K]K^3\). Let \(J\subset\mathbf F_3[Q]\) be the augmentation ideal.

A section change replaces the lifted generators by \(x_i\mapsto k_i x_i\), with arbitrary admissible \(k_i\in K\). After abelianizing the kernel, the change in the relator defect is the Fox section-change map
\[
\delta(k_x,k_y)=\overline{\partial_x r}\,k_x+\overline{\partial_y r}\,k_y.
\]
For the fixed commutator convention,
\[
\partial_x r=N_3(x)+x^3-y,\qquad \partial_y r=x^4-1.
\]
Modulo \(J^2\), in augmentation variables \(X=x-1,Y=y-1\),
\[
\partial_x r\equiv -Y,\qquad \partial_y r\equiv X.
\]
Thus the degree-1 Fox symbols span \(J/J^2\).

The kernel abelianization is cyclic over \(\mathbf F_3[Q]\), generated by \(\bar z\). With its induced augmentation filtration, \(\operatorname{gr}_{d+1}\bar A=J\operatorname{gr}_d\bar A\). Therefore the degree-5 target is exactly generated by the degree-1 \(J/J^2\) action on degree-4 classes. Since \(\delta\) has both independent degree-1 Fox directions \(-Y\) and \(X\), every degree-5 class is an actual section-change image.

Hence the exact minimal finite-kernel mod-3 quotient is
\[
\boxed{\mathcal C^{\mathrm{Fox}}_{s,5}=0}.
\]
This closes the degree-5 commutator path as a genuine gauge-invariant obstruction at the mod-p abelianized-kernel layer. The result is stronger than the earlier free-Lie argument because the admissible section-change map is now explicitly identified.

Logical boundary: this still does not compute the integral \(A_s=K/[K,K]\), does not prove the full nonabelian finite extension splits, and does not settle \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\). Degree 6 is now the first structurally distinct restricted-power diagnostic, but only after an explicit pre-check of whether it can survive in the integral \(A_s\)-level quotient.

Classification:
- degree-5 actual finite-kernel mod-3 Fox cokernel: **FAIL / CLOSED**;
- degree-5 commutator path: **FAIL / CLOSED**;
- integral/restricted \(A_s\)-obstruction: **OPEN / LOAD-BEARING**;
- full finite-extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\): **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

Next authorized action: perform the degree-6 restricted/integral pre-check; do not reopen degree 5.


## 2026-10-03 — T1-C DEGREE-6 PRE-CHECK: RESTRICTED SYMBOL IS NOT YET AN INTEGRAL OBSTRUCTION

The degree-6 pre-check shows an object mismatch. The restricted Lie p-operation is naturally mod-p graded, while the unresolved load-bearing object is the integral kernel abelianization A_s and its actual section-change quotient. For p=3, an integral element u has third power equal to 3u in the abelian group A_s. Thus a nonzero degree-6 restricted symbol modulo 3 is not, by itself, a new integral extension obstruction. It becomes relevant only if an integral lift survives the actual section-change image and exhibits a genuine 3-divisibility or torsion defect.

Classification: degree-6 restricted symbol alone = FAIL/CLOSED as a standalone obstruction; degree-6 as a shadow of an integral divisibility defect = CONDITIONAL; integral section-change quotient of A_s = OPEN/LOAD-BEARING. No isolated degree-6 brute-force calculation is authorized yet.

Next authorized action: construct the integral section-change map on the first potentially 3-divisible degree-2 kernel class and compute its integral cokernel/torsion before using any degree-6 restricted shadow.

## 2026-10-03 — T1-C INTEGRAL FOX LINEARIZATION: FIRST 3-DIVISIBILITY OBSTRUCTION AT I^3

The authorized integral section-change calculation was pushed one filtered order beyond the degree-6 pre-check in the minimal model \((p,s,a)=(3,2,1)\), with \(r=x^3[x,y]\) and \(R=\mathbf Z[Q]\). Put \(I=\ker(R\to\mathbf Z)\), \(X=x-1\), \(Y=y-1\). The exact Fox derivatives are
\[
f_x=N_3(x)+x^3-y=3+6X+4X^2+X^3-Y,
\qquad
f_y=x^4-1=4X+6X^2+4X^3+X^4.
\]
Modulo \(I^3\), the section-change image is generated by these two series acting on the kernel generator.

The scalar defect is \(9\bar z\). Its augmentation forces any coefficient \(a\) of \(f_x\) in a putative cancellation \(9\in(f_x,f_y)\bmod I^3\) to have constant term \(3\). The degree-one \(Y\)-coefficient then forces the \(Y\)-coefficient of \(a\) to be exactly \(1\), because \(f_y\) has no pure \(Y\)-term. At degree two, the pure \(Y^2\)-coefficient becomes
\[
-1+3c_{Y^2},
\]
where \(c_{Y^2}\in\mathbf Z\) is the quadratic coefficient of \(a\). This cannot vanish integrally. The \(f_y\)-term cannot alter the pure \(Y^2\)-coefficient because its leading term is divisible by \(X\). In degree two the relation \([X,Y]\) is already zero in the Demuškin associated graded, so no \(XY-YX\) correction changes this pure \(Y^2\) obstruction.

Equivalently, after the scalar cancellation and the degree-two linear correction, a residual proportional to \(Y^2\bar z\) remains which would require division by \(3\) to remove. This is qualitatively different from the mod-3 degree-5 commutator path: it is an **integral divisibility obstruction**, not a new ordinary-Lie commutator direction.

Logical boundary: this establishes a nonzero class in the \(I^2/I^3\) associated-graded section-change quotient **provided the corresponding \(Y^2\bar z\) class survives the finite-kernel module relation**. The remaining finite-kernel survival check is therefore now the single load-bearing verification. If it survives, the pushed-out abelian-kernel extension is nonsplit, hence the original finite extension is nonsplit. If it is killed by an additional finite-kernel relation, the obstruction closes and the integral quotient must be continued.

Classification:
- degree-6 restricted symbol alone: **FAIL / CLOSED**;
- integral Fox divisibility calculation through \(I^3\): **PASS / LOCAL**;
- pure \(Y^2\) residual before finite-kernel survival check: **PASS / LOCAL**;
- actual abelianized-kernel obstruction: **OPEN / LOAD-BEARING**;
- full finite-extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\): **OPEN / LOAD-BEARING**.

Next authorized action: verify that \(Y^2\bar z\neq0\) in the actual finite-kernel associated graded at this degree. Do not reopen degree 5, do not invoke a standalone degree-6 restricted-power obstruction, and do not open \(B_s\) yet.


## 2026-10-03 — T1-C FINITE-KERNEL SURVIVAL CHECK: INTEGRAL Abar OBSTRUCTION CONFIRMED (MINIMAL MODEL)

The remaining survival check was completed in the minimal model \((p,s,a)=(3,2,1)\), \(n=10\). The degree-2 relation of the Demuškin quotient is the initial commutator \([X,Y]\); in the finite extension the defining relation \(z^9=x^3[x,y]\) pushes this relation to the critical filtration (the \(z^9\) term lies in degree 9), but it introduces no kernel relation in degree 3 that can annihilate \(Y^2\bar z\). After abelianizing the kernel, the degree-3 kernel module is generated by the degree-2 augmentation actions on the degree-1 normal kernel class \(\bar z\). The only degree-3 relations inherited from the quotient identify the ordinary \(XY/YX\) ordering; they do not kill the pure \(Y^2\bar z\) class.

Hence the pure \(Y^2\bar z\) residual found in the integral Fox calculation survives the actual finite-kernel associated graded. Therefore the pushed-out abelian-kernel extension has a nonzero section-change class already in this low integral filtration layer. Since a split original extension would push out to a split abelian-kernel extension, the original finite extension is **nonsplit in the minimal stress model at \(n=10\)**.

This is the first genuine load-bearing obstruction obtained after all earlier scalar, mod-\(p\), and degree-5 commutator candidates were removed. It is not a degree-6 restricted-Lie artifact: it is an integral divisibility obstruction visible in the Fox section-change quotient.

Logical boundary: this proves nonsplitting for the audited minimal stress model. It does **not** yet prove the general statement for every \((p,s,a,d)\), and it does not by itself establish the exact threshold \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\). The next generalization must prove that the same integral \(Y^2\)-type obstruction persists for the full odd-prime family, or identify the precise exceptional parameters.

Classification:
- minimal-model integral \(\bar A\)-pushout obstruction: **PASS / LOCAL**;
- minimal-model finite-extension nonsplitting at \(n=10\): **PASS / LOCAL**;
- general \((p,s,a,d)\) integral obstruction: **OPEN / LOAD-BEARING**;
- exact \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\): **OPEN / LOAD-BEARING**;
- full finite-extension threshold theorem: **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

Next authorized action: transport the integral Fox divisibility obstruction from \((3,2,1,2)\) to general odd \(p\), \(s>a\), beginning with the rank-two factor. No degree-5 reopening, no standalone degree-6 branch, and no \(B_s\) promotion.


## 2026-10-03 — GATE T1-C GENERAL INTEGRAL FOX OBSTRUCTION / EXACT STRESS-FAMILY THRESHOLD

The minimal integral divisibility obstruction generalizes cleanly to every odd prime \(p\), every \(s>a\ge1\), and the rank-two stress factor \(r=x_1^{q}[x_1,x_2]\) with \(q=p^a\). Write \(I\) for the augmentation ideal of \(\mathbf Z[Q_s]\), \(X=x_1-1\), \(Y=x_2-1\). The Fox derivatives are
\[
f_1=N_q(x_1)+x_1^q-x_2,
\qquad
f_2=x_1^{q+1}-1.
\]
After projecting to the pure \(Y\)-associated-graded direction (set \(X=0\) and discard mixed terms), one has exactly
\[
f_1\mapsto q-Y,
\qquad
f_2\mapsto0.
\]
Thus any integral section-change cancellation of the scalar defect \(p^s\bar z\) would require, to successive \(Y\)-orders,
\[
(q-Y)A(Y)=p^s.
\]
Formally
\[
\frac{p^s}{q-Y}
=p^{s-a}\sum_{j\ge0}p^{-aj}Y^j.
\]
Let \(r=\lfloor s/a\rfloor\). Then the coefficients for \(j<r\) are integral, but the coefficient at \(j=r\) is
\[
p^{s-a(r+1)},
\]
which is not an integer because \(s-a(r+1)<0\). Equivalently, after all lower-order integral lift corrections are made, the first unavoidable pure-\(Y\) residual is a nonzero multiple of \(Y^r\bar z\) modulo \(q\). This is an integral divisibility obstruction, not a mod-\(p\) restricted-power artifact.

The survival of this class in the actual finite kernel is independently witnessed by the metabelian quotient
\[
H=C_{p^s}\rtimes C_{p^s},
\qquad yzy^{-1}=z^{1+p},
\]
obtained from \(G_{s,a}\) by setting \(x_1=1\) and all other \(x_i=1\). Here \(z^{p^s}=1\), \((y-1)^r z=p^r z\ne0\) because \(r<s\), and \(D_{p^s+1}(H)=1\) for odd \(p\): for \(\gamma_i(H)=\langle z^{p^{i-1}}\rangle\) one has \(i p^j\ge p^s+1\Rightarrow i-1+j\ge s\), so every Zassenhaus factor is trivial at that depth. Hence the pure-\(Y\) obstruction survives the actual finite-window kernel.

This yields a genuine nonzero class in the abelianized-kernel pushout, so the finite extension is nonsplit at \(n=p^s+1\). Conversely, for every \(n\le p^s\), the map \(D/D_n(D)\to G_{s,a}/D_n(G_{s,a})\) induced by the generator lifts is a section: the defining relation satisfies \(z^{p^s}\in D_{p^s}(G_{s,a})\subseteq D_n(G_{s,a})\), and the remaining \(D_n(D)\) relations map into \(D_n(G_{s,a})\). Therefore the relative extension splits for all \(n\le p^s\).

Consequently, for the declared rank-two stress family (and hence as a stress quotient for the higher-rank family), the exact relative separation threshold is now established:
\[
\boxed{n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1.}
\]
The higher-rank case inherits nonsplitting from the rank-two quotient by setting the extra Demuškin generators to \(1\), while the lower-bound splitting argument is unchanged.

Classification:
- general odd-\(p\) integral Fox divisibility obstruction: **PASS / LOCAL**;
- survival in the actual finite kernel: **PASS / LOCAL**;
- critical nonsplitting at \(p^s+1\): **PASS / CLOSED** for the declared stress family;
- splitting for every \(n\le p^s\): **PASS / CLOSED** for the declared stress family;
- exact \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\): **PASS / CLOSED** for the declared stress family;
- universal free-by-Demuškin theorem beyond this stress family: **OPEN**;
- blind carrier search: **STOP / NOT AUTHORIZED**.


## 2026-10-03 — CRITICAL RE-AUDIT OF POST-THRESHOLD CRITIQUE / FINITE-KERNEL SURVIVAL STATUS

A referee-style critique proposed downgrading the T1-C finite-kernel survival step to “PARTIAL (metabelian only)” and reopening an actual-class-2-kernel Gate 0. The authoritative post-threshold audit was rechecked. That downgrade is NOT current.

The load-bearing statement is not that the metabelian quotient itself is the class-2 kernel. The point is functoriality of the section-defect/pushout class: the metabelian model is a Q-equivariant quotient of the relevant kernel/module, and section-change coboundaries map to section-change coboundaries. Therefore a nonzero pushed-out obstruction in the metabelian quotient implies the original abelianized-kernel pushout class is nonzero. This is the standard pushout/naturality bridge and is explicitly recorded in the post-threshold critical re-audit.

Accordingly:
- stress-family relative threshold n_sep^rel(s)=p^s+1: PASS / CLOSED;
- integral Fox obstruction in the declared stress family: PASS / CLOSED as a theorem ingredient;
- finite-kernel survival via the explicit equivariant pushout/naturality argument: PASS / CLOSED;
- unmarked same-window no-go: OPEN;
- canonical reconstruction of the marked quotient: OPEN / LOAD-BEARING;
- intrinsic factorization/coarsest realization: OPEN / LOAD-BEARING;
- universal free-by-Demushkin theorem: OPEN.

The critique's broader methodological warning remains correct in a narrower sense: “metabelian survival” must never be phrased as though the metabelian quotient were literally the actual class-2 kernel, and the naturality lemma must be stated explicitly. But that is a proof-packaging requirement, not a remaining Gate-0 mathematical OPEN.

The correct next gate is therefore the unmarked intrinsic-factorization problem, not another finite-kernel survival calculation. No recomputation of p^s+1, degree-5 reopening, scalar/norm shortcut, or blind carrier search is authorized.


## 2026-10-03 — CRITICAL REVIEW RECONCILIATION / PUSHOUT TARGET + INTRINSIC SUB-GATES

The referee-style critique was rechecked against the authoritative T1-C audit.

1. The metabelian survival witness is an actual Q-equivariant quotient/pushout target of the kernel/module, not an unrelated witness. For the rank-two stress group,
\[
G=\langle z,x,y\mid z^{p^s}=x^q[x,y]\rangle,
\]
the assignment \(x\mapsto1,\ z\mapsto z,\ y\mapsto y\) gives
\[
G\twoheadrightarrow H=C_{p^s}\rtimes C_{p^s},
\qquad yzy^{-1}=z^{1+p},
\]
and induces a Q-equivariant kernel map to the cyclic kernel of H. Hence the nonzero-after-pushout implies nonzero-before-pushout direction is the required one. The remaining improvement is documentation: display the quotient diagram explicitly when citing the lemma.

2. Therefore the actual finite-kernel survival classification remains PASS / CLOSED for the declared nonboundary subfamily \(a\ge2\). The \(a=1\) boundary remains OPEN. The critique's downgrade to “metabelian only” would apply only if the equivariant pushout bridge were absent.

3. Intrinsic factorization is refined into three proof obligations:
   (i) canonical reconstruction of the quotient/sufficient extension datum;
   (ii) canonical and functorial definition of the extension class;
   (iii) identification of the reconstructed class with the original relative obstruction.
These are not necessarily three independent mathematical gates: a reconstruction theorem stated as an isomorphism of marked extension diagrams can make (ii) and (iii) formal consequences of functoriality.

4. The carrier STOP remains correct, but its immediate reason is the Object/Input/Functoriality mismatch. A7/non-reencoding is not automatically violated merely by attempting a carrier construction; A7 becomes a candidate-level test once an intrinsic carrier is actually defined. A carrier that simply stores the forgotten marked map would fail that test, but no such carrier is authorized.

5. Gate A (\(a=1\)) and Gate B (intrinsic reconstruction/separation) are independent. Gate B is the main line because it is the structural Paper 4 target, not because T1-C is merely “sufficiently closed”.

Current exact status:
- relative threshold \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\), declared nonboundary stress family \(a\ge2\): PASS / CLOSED;
- finite-kernel survival bridge for \(a\ge2\): PASS / CLOSED;
- \(a=1\) survival and exact threshold: OPEN;
- unmarked reconstruction: OPEN / LOAD-BEARING;
- same-window separation: OPEN;
- intrinsic factorization: OPEN / LOAD-BEARING, with the three proof obligations above;
- coarsest intrinsic compression: OPEN;
- universal free-by-Demushkin theorem: OPEN;
- blind carrier search: STOP / NOT AUTHORIZED.

No reopening of degree 5, scalar/norm, or the frozen relative threshold is authorized.


## 2026-10-03 — GATE T1-C A=1 INDEPENDENT CLOSURE

The previously unresolved a=1 boundary is now closed for the declared marked/relative stress family. An independent finite metabelian pushout was constructed: an abelian kernel A with z^(p^(s+1))=1 and p x=p^s z, and y-action z -> z^(1-p), x -> x. Then x^p[x,y]=z^(p^s), giving a quotient of G_{s,1}. At n=p^s+1, the Jennings-Zassenhaus product formula gives D_n(H_s)=1, while (y-1)^s z=(-p)^s z !=0. This supplies the missing a=1 survival witness without the invalid cyclic-quotient argument.

The integral Fox section-change equation is (p-Y)A(Y)=p^s, whose formal solution has nonintegral Y^s-coefficient p^(-1). Hence the critical defect cannot be killed by integral lift changes; the witness detects the residual. By pushout/naturality the relative extension is nonsplit at p^s+1. Together with the lower-bound splitting for n<=p^s, the exact relative threshold is n_sep^rel(s)=p^s+1 for the declared stress family.

Classification: a=1 critical survival PASS/CLOSED; a=1 integral Fox obstruction PASS/CLOSED; a=1 critical nonsplitting PASS/CLOSED in the marked/relative stress family; exact relative threshold for all declared a>=1 PASS/CLOSED; unmarked filtered-group reconstruction OPEN/LOAD-BEARING; universal free-by-Demushkin theorem OPEN; blind carrier search STOP/NOT AUTHORIZED.

Detailed audit: research/PAPER4_T1C_A1_INDEPENDENT_CLOSURE_AUDIT_2026-10-03.md. The older a=1 OPEN record is superseded, not deleted.


## 2026-10-03 — T1-C RECONCILIATION: A=1 REMAINS OPEN; MARKED THRESHOLD CLOSED ONLY ON CERTIFIED NONBOUNDARY SUBFAMILY

The latest referee-style critique was reconciled against the authoritative T1-C audit. The governing scope-corrected status is: the metabelian finite-kernel survival witness requires r=floor(s/a)<s, so it certifies the exact relative threshold only for the declared nonboundary subfamily a>=2, s>a. For a=1, the same witness collapses because (y-1)^s z=p^s z=0; therefore a=1 survival and the exact threshold remain OPEN. Older all-a>=1 CLOSED wording is superseded.

The pushout/naturality bridge is accepted as the formal packaging lemma for the certified a>=2 case: the metabelian quotient is a Q-equivariant quotient/pushout of the kernel, and section-change coboundaries map to section-change coboundaries. Thus a nonzero pushed-out obstruction implies nonzero before pushout. This closes the proof-packaging gap but does not enlarge theorem scope.

Current authoritative classification:
- integral Fox divisibility: PASS / LOCAL for s>a>=1;
- actual finite-kernel survival and exact relative threshold p^s+1: PASS / CLOSED for a>=2, s>a;
- a=1 finite-kernel survival / exact threshold: OPEN;
- unmarked reconstruction of the marked quotient/extension datum: OPEN / LOAD-BEARING;
- same-window separation: OPEN;
- intrinsic/coarsest realization: OPEN;
- blind carrier search: STOP / NOT AUTHORIZED.

Decision for continuation: do not reopen the frozen threshold, degree-5 residual, scalar/norm shortcut, or RAAG orientation counterexample. The main Paper 4 line is Gate B: either prove canonical reconstruction of sufficient marked extension data from the unmarked finite window, or produce an admissible same-window separation pair. Gate A (a=1 witness) remains an independent side branch.
