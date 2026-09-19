# CURRENT STATE — 2026-09-19

## Authoritative current question
Can the canonical orientation character chi:G -> Z_3^times be recovered intrinsically from filtered/graded data?

## Authoritative branch
**Rank-4 D4 IA / filtered extension datum.**

## Latest mathematical conclusion — 2026-09-19

The quotient-valued object
Delta_q(g) = [F_g(X_1^3)-X_1^3]_3
is **not a new q-sensitive invariant**.

Indeed, with the frozen convention F_(gh)=F_g o F_h and
F_g(X_1)=g.X_1 + terms of degree >=2,
the degree-3 part satisfies
Delta_q(g) = g.(X_1^3) - X_1^3.

This was independently verified in the structured CI on all 9 representatives after adding the explicit coboundary check:
CI run 35420266538, head bd53311cf45dfc930599c3c24b60df8572c155cc, job 105836490226 — SUCCESS.

Therefore
Delta_q(gh)=Delta_q(g)+g.Delta_q(h)
is the ordinary coboundary identity. Modulo Q3 it represents the zero H^1 class whenever [X_1^3] is viewed as a fixed Q3 vector:
Delta_q(g)=g.[X_1^3]-[X_1^3].

### Consequence

The earlier structured cocycle passes remain valid as **implementation/convention checks only**. They do not constitute evidence for a new q-observable, canonical cocycle, or nontrivial H^1 class.

The broader rank-4 scan proposed after the structured audit is **CANCELLED**. No scan whose only purpose is to re-test this cocycle law is authorized.

## Frozen negative / closed routes

- Original linear-only rank-4 D4 lifting observable: FAIL/CLOSED due to lift-independence failure.
- Preferred Nielsen lifts: permanently prohibited as repair.
- Naive q=9 degree-9 relation space: not H-stable.
- Artificial H-closure of the q=9 relation space: invalid as a presentation relation object.
- Q3/Q9 S9 orbit route: CLOSED at definition level.
- D9-OBS natural p-layer candidate: FAIL/CLOSED as a universal p-layer shadow.
- Quotient-valued Delta_q cocycle: CLOSED as **coboundary / no new information**.

## What remains genuinely open

### Gate A — non-coboundary q-sensitive datum definition

A new candidate must satisfy all of the following before computation:

1. **Definition boundary:** its input may not already contain q=3 versus q=infinity as an explicit label or subtraction.
2. **Non-coboundary test:** it must not reduce to g.v-v for a fixed v in a pre-existing representation.
3. **Intrinsicity:** it must survive allowed IA/lift changes without choosing a preferred lift.
4. **Presentation/coordinate legitimacy:** its definition must be independent of arbitrary free-group coordinates, or the precise quotient/torsor mechanism must be proved.
5. **Nontriviality:** there must be a concrete witness showing the datum is not identically zero or a universal p-layer shadow.
6. **q-separation:** only after the datum is defined from admissible weak data may q=3 and q=infinity be compared.

A candidate failing (1) or (2) is closed immediately; no broad scan is warranted.

### Gate B — relation to the orientation character

The rank-4 D4 condition
g e_1 = mu(g)e_1
was previously used as a candidate admissibility condition, but its connection to the target orientation character chi has not been independently established.

This must be tested as a separate mathematical statement. In particular, do not assume that the line/eigenvector condition recovers chi merely because mu is visible in the ambient GSp action.

## Current authorized work

1. Audit/define a genuinely non-coboundary datum, preferably using the retained filtered/extension structure rather than Delta_q.
2. Independently analyze the exact relation between g e1 = mu(g)e1 and chi.
3. Only after a definition gate passes may a new small CI control be designed.

No unrestricted rank-4 scan is currently authorized.

## Latest implementation result

Structured cocycle audit with explicit coboundary check:
- run: 35420266538
- commit: bd53311cf45dfc930599c3c24b60df8572c155cc
- job: 105836490226
- conclusion: SUCCESS

This verifies the hand derivation against the script; it does not create a new invariant.


## A-1 coboundary control — REGISTERED / EXECUTION PENDING

The pre-registered A-1 control has been added before any broader scan.

Plan: plans/RANK4_D4_DELTA_Q_COBOUNDARY_CONTROL_2026-09-19.md
Script: research/rank4_D4_delta_q_coboundary_control_2026-09-19.py
Workflow: .github/workflows/rank4-d4-delta-q-coboundary-control.yml

T1 directly checks Delta_q(g)=g.[X1^3]-[X1^3] for all 9 structured representatives. T2 uses q-blind controls X2^3, X1X2X1, and a fixed non-monomial degree-3 tensor. T3 compares the 81-pair nonzero quotient-class count with the direct coboundary prediction.

The historical H_adm=1296 enumeration is not reconstructed in this gate because no separately reusable authoritative implementation was found in the frozen structured script; no new enumeration is invented.

No mathematical PASS/FAIL is recorded until CI execution is independently checked.


## A-1 execution result — T1 PASS / T2 CONTROL INVALID / T3 PASS

CI run 35420831517, diagnostic commit c1ac93d673af3aefb9d1c4e3df139e31f6ab56ec, job 105838085431: workflow SUCCESS.

T1: zero failures on all 9 representatives for Delta_q(g)=g.[X1^3]-[X1^3].
T3: zero direct vector failures on all 81 ordered pairs; observed and predicted nonzero class count both 60.

T2 produced 0 failures for X1^3 and X2^3 but 5 failures for X1X2X1 and 5 for the arbitrary tensor. This is classified as a control-model/implementation failure, not a non-coboundary result: the frozen evaluator is a truncated free-group/group-algebra evaluator, not a direct homogeneous Magnus/Lie substitution evaluator. X1^3 is exceptional in characteristic 3 because (1+X1)^3=1+X1^3.

Therefore A-1 is NOT yet closed as a three-test experiment. No broader scan is authorized. Next step is either a legitimate pure Magnus/Lie control definition or closure by the algebraic proof plus T1/T3, with the invalid T2 explicitly removed.


## New gate — Rank-2 relator-unit digit (definition only)

A new definition gate has been opened after the Delta_q coboundary closure:
`plans/RANK2_UNIT_DIGIT_DEFINITION_GATE_2026-09-19.md`.

Target: determine whether the first mod-9 digit of the relator unit u(phi) for actual automorphisms of the rank-2 Demushkin model can carry lift-dependent information invisible in the induced g in GL_2(F_3). The candidate is required to be q-blind at definition time and must not use a preferred lift.

The gate is **OPEN / DEFINITION ONLY**. No computation is authorized yet. The next step is a hand derivation of the exact relator-unit normalization and composition law, followed by q=infinity and q=3 mod-9 constraints. The identification of this unit with the canonical orientation is explicitly not assumed; it is EXTERNAL / TO VERIFY.


## Rank-2 unit-digit hand derivation checkpoint — 2026-09-19

A critical review of the earlier hand derivation found that lift-independence of the relator scalar was asserted too strongly. The prior statement is withdrawn.

Corrected status:
- (R/[R,F]) and the scalar action for a **chosen stabilizing free lift** remain the object under study, subject to the relation-module normalization.
- Multiplicativity is valid at the lift level, but does not yet descend to \\(\\operatorname{Aut}(G_q)\\) until lift-independence is proved.
- q=infinity: the determinant calculation remains a control derivation, not a closure of D1.
- q=3: the orientation/abelianization constraint remains auxiliary support only; it does not determine (u\\bmod9).
- The previously suggested formal IA substitution (x_1\\mapsto x_1[x_1,x_2]) is **not** admissible as a free lift witness until its status as a free-group automorphism is proved.

The key missing lemma is now explicit: determine the action on (R/[R,F]) of
\\[
\\ker(\\operatorname{Stab}(R)\\to\\operatorname{Aut}(G_q)).
\\]
If this kernel acts trivially, D1 can be closed; if not, the lift-independent (u(\\phi)) definition fails and the gate must be redesigned.

Therefore the Rank-2 unit-digit gate remains **OPEN / INCONCLUSIVE / HAND-DERIVATION CONTINUING**. No finite scan is authorized.

Next exact task: analyze the stabilizer-to-(\\operatorname{Aut}(G_q)) kernel before any (K_3) scan or mod-9 computation.



## 2026-09-19 — Rank-2 unit-digit structural correction

A further hand audit found a more fundamental problem with the proposed relator-unit definition. The earlier assumption (R/[R,F]\cong\mathbf Z_3) for q=3 is not established and conflicts with the standard five-term/Hopf exact sequence
\[
H_2(G,\mathbf Z_3)\to R/[R,F]\to F_{ab}\to G_{ab}\to0.
\]
For (G_3^{(2)}), (F_{ab}\cong\mathbf Z_3^2) and (G_{ab}\cong\mathbf Z_3\oplus\mathbf Z/3), so (R/[R,F]) has the rank-one abelianized-relation contribution; together with (H_2(G,\mathbf Z_3)\cong\mathbf Z_3) for the infinite Demushkin group, the module is not justified as a single relator line. Thus the scalar equation (	ilde\phi([r_3])=u[r_3]) is not intrinsically defined without an additional quotient/projection.

The Rank-2 relator-unit gate is therefore **OPEN / INCONCLUSIVE at a deeper definition failure**, not merely awaiting lift-kernel analysis. No mod-9 or IA scan is authorized. Next task: determine whether a canonical quotient of (R/[R,F]) exists whose automorphism action supplies the intended scalar; otherwise close/redesign this route.


## 2026-09-19 — Rank-2 relator-unit route CLOSED by explicit lift-kernel witness

The definition-level analysis is now complete enough to close this route; no finite computation is warranted.

For q=3, the five-term/Hopf sequence gives 0 -> H2(G3,Z3) -> M:=R/[R,F] -> F_ab -> G3_ab -> 0. Since F_ab is Z3^2 and G3_ab is Z3 ⊕ Z/3, the natural rank-one quotient is Q:=M/H2(G3,Z3) ≅ ker(F_ab -> G3_ab)=3 Z3 e1.

This quotient nevertheless fails lift-independence. For any r in R, alpha_r(x1)=x1 r, alpha_r(x2)=x2 induces the identity on F/Phi(F), hence is an automorphism of the free pro-3 group; since r=1 in G3 it induces id_G3 and lies in the stabilizer-to-Aut(G3) kernel. Taking r=r3 gives [r3]_F_ab=3e1, so alpha_r3 sends e1 to 4e1 and 3e1 to 4(3e1). Thus the same group automorphism id_G3 has two stabilizing free lifts whose actions on Q differ by the unit 4, already nontrivially modulo 9.

Decision: Rank-2 relator-unit digit route = FAIL / CLOSED. This is a definition-level lift-independence failure, not a computational failure. The full R/[R,F] also contains the H2 component, so there is no canonical single relator line to rescue the scalar construction. No mod-9, K3, IA, or q-comparison scan is authorized for this route.

The next authorized task returns to the independent bridge between g e1=mu(g)e1 and the canonical orientation chi; no implication is assumed.


## 2026-09-19 — Rank-2 route scope correction after critical review

The prior wording “Rank-2 relator-unit digit route = FAIL / CLOSED” was too broad. The explicit witness proves a narrower statement:

- **FAIL:** the proposed relator-unit scalar construction on the natural canonical abelianized rank-one quotient
  \(Q=M/H_2(G_3,\mathbf Z_3)\cong3\mathbf Z_3e_1\) is not lift-independent.
- **FAIL:** therefore that specific scalar cannot descend to \(\operatorname{Aut}(G_3)\), even modulo 9.
- **NOT PROVED:** every possible construction using the full relation module \(R/[R,F]\), or every possible filtered relation-module quotient, is impossible.

Accordingly, the broader “entire relator-module strategy is closed” claim is withdrawn. Any genuinely different intrinsic construction would require its own definition gate and independent proof of lift-independence/naturality.

The next authorized branch remains the independent bridge audit:
\[
ge_1=\mu(g)e_1\quad\text{versus}\quad\chi.
\]
No implication between \(\mu\) and \(\chi\) is assumed.


## 2026-09-19 — Critical correction: relation-module rank-one objection withdrawn

A further literature/structural audit found that the preceding “R/[R,F] is not rank-one because H_2(G,Z_3) contributes an extra component” argument was incorrect for this one-relator pro-p presentation. Standard Demushkin deformation literature explicitly uses that when the relation subgroup is normally generated by one relator, the relation module R/[R,F] is Z_p, and in the q != 0 case it maps into F^ab with index q. Thus for r_3=x_1^3[x_1,x_2], the map R/[R,F] -> F_ab sends a chosen generator to 3e_1 and is injective.

Accordingly:
- the earlier claim that the q=3 relation module itself has an unavoidable extra H_2 component is **WITHDRAWN**;
- the natural quotient Q=M/H_2(G_3,Z_3) is not needed for the argument and should not be treated as the canonical object;
- the explicit lift-kernel witness is stronger in the corrected setting: because M is already rank one and its image is 3e_1, the stabilizing lift alpha_{r_3} acts by 4 on M itself (mod 9), not merely on an auxiliary quotient.

The lift-independence FAIL therefore remains, and indeed becomes cleaner: the proposed scalar attached to a chosen stabilizing free lift does not descend to Aut(G_3). No mod-9/IA scan is authorized for this construction.

This correction supersedes the immediately preceding “non-rank-one relation module” discussion, but does not reopen the failed lift-independent scalar route.


## 2026-09-19 — Orientation bridge hand audit: mu versus chi

A new hand-derivation checkpoint was completed in \`research/ORIENTATION_MU_BRIDGE_HAND_AUDIT_2026-09-19.md\`.

Established:
- \(\chi:G\to\mathbf Z_3^\times\) and \(\mu\) on the degree-one automorphism side have different domains and coefficient groups.
- For q=3, \(G^{ab}\cong\mathbf Z_3^3\oplus\mathbf Z/3\), and the torsion subgroup gives a canonical one-dimensional line whose Frattini image is the project’s \(e_1\)-line under the frozen identification.
- Canonical orientation is automorphism-invariant: \(\chi\circ\phi=\chi\). In the standard presentation this forces the x2 coefficient of \(\phi(x_2)\) to be 1 mod 3.
- Therefore, for an actual automorphism whose degree-one matrix satisfies \(ge_1=a e_1\) and \(g^T Jg=\nu(g)J\), the frozen generator-side convention gives \(\nu(g)=a\) mod 3.

Not established:
- \(\mu=\chi\) or any direct recovery of \(\chi\) from \(\mu\).
- \(\mu\) is not the mod-3 reduction of \(\chi\): for q=3, \(\chi(G)\subset1+3\mathbf Z_3\), while \(\mu\) may be nontrivial in \(\mathbf F_3^\times\).

Gate consequence: **PASS for type/domain separation and the conditional intrinsic interpretation of \(\mu\); OPEN for any actual recovery bridge to \(\chi\).** No finite scan yet.


## 2026-09-19 — MU-CHI bridge definition gate: manual proof

The manual proof is now recorded in \`plans/MU_CHI_BRIDGE_DEFINITION_GATE_2026-09-19.md\`.

Results:
- **PASS:** the frozen \(e_1\)-line is intrinsic: it is the Frattini image of \(\operatorname{Tor}(G^{ab})\cong\mathbf Z/3\).
- **PASS:** actual automorphisms preserve this line, giving a genuine character \(\mu_{\mathrm{int}}:\operatorname{Aut}(G)\to\mathbf F_3^\times\).
- **PASS:** under the frozen matrix/pairing convention, \(\mu_{\mathrm{int}}\) equals the degree-one GSp multiplier on the actual automorphism image.
- **FAIL:** \(\mu\) is not \(\chi\), and is not \(\chi\bmod3\); for \(q=3\), \(\chi(G)\subset1+3\mathbf Z_3\), so its mod-3 reduction is trivial.
- **OPEN:** a deeper dualizing-module construction might relate \(\chi\) plus additional canonical structure to \(\mu_{\mathrm{int}}\). No such construction is currently established.

No finite scan is authorized or needed.


## 2026-09-19 — Dualizing top-line convention audit

Frozen (g) is on the generator/(H_1) side. Hence the induced (H^1) action is (g^{-T}), and the induced (H^2) scalar is (
u(g)^{-1}). For (p=3), (mathbf F_3^	imes={pm1}), so inversion is identical: (mu_{H^2}=mu_{m int}) as (mathbf F_3^	imes)-valued characters, although conceptually the cohomological action is inverse. This does **not** identify (mu) with the full orientation (chi:G	omathbf Z_3^	imes); (chimod3) is trivial. The MU-CHI bridge is therefore conceptually resolved: (mu) is a canonical automorphism-of-duality-line shadow, not the orientation character. No finite scan is authorized. Next work should target filtered/graded data retaining the (1+3mathbf Z_3) orientation layer.

## 2026-09-19 — Orientation mod-9 recovery gate OPEN

The MU-CHI branch is now conceptually closed: mu is the canonical F3^times character on the torsion/top-duality line, while chi is the Z3^times-valued group orientation. They are not the same object and mu carries no higher 3-adic information.

Next target is the first nontrivial orientation layer chi mod 9. A new gate requires a canonical mod-9 cohomological/Bockstein/first-lift construction and explicitly forbids reuse of the failed lift-dependent relator-unit scalar. No finite scan is authorized until the mod-9 object is hand-defined and its ambiguity is proved harmless.

## 2026-09-19 — Critical correction to mod-9 orientation gate

The first formulation overstated what mod-9 cup data could prove. The corrected status is:

- **Established:** finite-coefficient cup-product data sees the \(q=3\) power contribution; for the frozen relation its mod-9 matrix is, up to convention, \(\begin{pmatrix}6&1\\-1&0\end{pmatrix}\oplus\begin{pmatrix}0&1\\-1&0\end{pmatrix}\).
- **Not established:** this matrix recovers \(\chi(x_2)\equiv4\pmod9\).
- **Critical ambiguity:** \(H^2\)-valued pairing needs a generator/trivialization before a scalar can be extracted; basis/presentation invariance must also be proved.
- **Gate remains OPEN:** test an explicit Bockstein/finite-coefficient invariant. If it retains only q=3 and loses the value 4, close the route.

No finite scan.


## 2026-09-19 — Explicit Bockstein audit: candidate FAIL / CLOSED

The authorized hand task was completed in `research/ORIENTATION_MOD9_BOCKSTEIN_AUDIT_2026-09-19.md`.

For
\[
0\to\mathbf F_3\xrightarrow{3}\mathbf Z/9\to\mathbf F_3\to0
\]
the intrinsic connecting map
\[
\beta:H^1(G,\mathbf F_3)\to H^2(G,\mathbf F_3)
\]
was analyzed for
\[
r=x_1^3[x_1,x_2][x_3,x_4].
\]

The Bockstein detects the power-term direction: up to the fixed top-class/sign convention,
\[
\beta(\gamma_1)\neq0,\qquad
\beta(\gamma_2)=\beta(\gamma_3)=\beta(\gamma_4)=0.
\]
Classical Demushkin formulas identify this Bockstein with the power coefficients of the defining relation. This independently confirms that the finite-coefficient operation sees the q=3 power contribution.

Critical result: the intrinsic object is the map \(\beta\), not a canonically normalized scalar in \(\mathbf F_3\). Changing the generator of the one-dimensional \(H^2\) target rescales any displayed scalar. More importantly, \(\beta\) retains only the q=3 power/torsion shadow and does not retain the required first 3-adic orientation value
\[
\chi(x_2)\equiv4\pmod9.
\]

Gate decision:
- **M9-A PASS:** canonical Bockstein object defined.
- **M9-B PASS:** intrinsic as a cohomological connecting map; no preferred free lift.
- **M9-C FAIL:** no canonical recovery of the value 4 from this object.
- **M9-D CLOSED for this Bockstein candidate.**

This is a candidate-level closure, not a proof that every possible finite-coefficient construction is impossible. No finite scan is authorized.

Next route, if opened, must retain additional \(1+3\mathbf Z_3\)-valued/twisted-dualizing information rather than reinterpreting the Bockstein's q=3 signal as orientation.

## 2026-09-19 — Twisted mod-9 orientation recovery: PASS / filtered-graded factorization OPEN

The ordinary Bockstein candidate was closed, so the next authorized route was the canonical twisted-coefficient surjectivity criterion.

For a candidate
\[
\rho:G\to1+3\mathbf Z/9,\qquad \rho(x_i)=1+3a_i,
\]
the reduction
\[
H^1(G,I_2(\rho))\to H^1(G,I_1(\rho))
\]
is surjective exactly when every mod-3 cocycle lifts.

Direct cocycle evaluation on
\[
r=x_1^3[x_1,x_2][x_3,x_4]
\]
gives the lift condition
\[
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4=0
\quad(\bmod 3).
\]
Since the four \(f_i\) are independent in \(H^1(G,\mathbf F_3)\), surjectivity is equivalent to
\[
(a_1,a_2,a_3,a_4)=(0,1,0,0).
\]
Hence
\[
\rho(x_2)=4\pmod9,
\]
exactly the frozen canonical orientation.

This is a substantive PASS: unlike the trivial-coefficient Bockstein, the twisted action itself carries the missing first 3-adic digit.

Gate status:
- T9-A canonical twisted finite-level object: **PASS**
- T9-B unique mod-9 recovery: **PASS**
- T9-C explicit recovery of \(\chi\bmod9\): **PASS**
- T9-D factorization through the prescribed filtered/graded data: **OPEN**

Critical limitation: this proves intrinsic recovery from twisted cohomology/full group data, not yet from the Zassenhaus graded object alone. No finite scan is authorized until that factorization question is formally defined and audited.

Detailed derivation: `research/ORIENTATION_MOD9_TWISTED_SURJECTIVITY_GATE_2026-09-19.md`.

## 2026-09-19 — New filtered-factorization gate for twisted orientation

The twisted mod-9 calculation gives a genuine PASS for intrinsic group-level recovery:
\[
\rho:G\to1+3\mathbf Z/9
\]
is uniquely selected by surjectivity of
\[
H^1(G,I_2(\rho))\to H^1(G,I_1(\rho)),
\]
and the frozen presentation yields
\[
\rho(x_2)=4\pmod9.
\]

The remaining question is now sharply isolated. Writing
\[
\rho=1+3\lambda\pmod9,
\qquad \lambda\in H^1(G,\mathbf F_3),
\]
the explicit lift obstruction is
\[
B_\lambda(f)=(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4.
\]
The canonical \(\lambda\) is the unique zero of this obstruction.

A new gate asks whether \(B_\lambda\) and its zero set can be defined intrinsically from the prescribed first restricted/Zassenhaus layers, rather than from a full presentation or preferred free lift.

Status:
- F0 candidate carrier: **PASS / strong candidate**
- F1 definition: **OPEN**
- F2 presentation/lift independence: **OPEN**
- F3 automorphism naturality: **OPEN**
- F4 uniqueness: **OPEN** at the intrinsic-object level
- F5 filtered/graded factorization: **OPEN**

No finite scan is authorized. Detailed gate: `plans/ORIENTATION_MOD9_FILTERED_FACTOR_GATE_2026-09-19.md`.

## 2026-09-19 — F1-F4 filtered-quotient audit: PASS, F5 OPEN

A new hand audit is recorded in `research/ORIENTATION_MOD9_FILTERED_FACTOR_F1_F4_AUDIT_2026-09-19.md`.

The twisted mod-9 obstruction can be formulated without a chosen free presentation or preferred free lift as a canonical twisted cocycle-lifting obstruction on the finite filtered quotient
[
C_3=G/G_4
]
of the frozen Zassenhaus/p-central filtration. The coefficient action is through
[
ho=1+3lambdapmod9,qquad lambdain H^1(G,mathbf F_3).
]
In frozen coordinates, evaluation of this intrinsic lifting problem reproduces
[
B_lambda(f)=(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4.
]

Status:
- **F1 definition:** PASS at the canonical finite-filtered-quotient level.
- **F2 presentation/lift independence:** PASS at that level.
- **F3 automorphism naturality:** PASS at that level.
- **F4 uniqueness:** PASS; the zero set is the singleton ((0,1,0,0)).
- **F5 factorization through the prescribed filtered/graded datum:** OPEN.

Critical boundary: this construction uses filtered extension/multiplication data of (G/G_4), not merely the associated graded vector spaces and initial quadratic relation. The q=3 power term lies in the first non-quadratic filtered layer, so discarding extension data can erase the information needed for (chimod9).

Therefore the project must not yet claim recovery from the associated graded restricted Lie object alone. The next task is to formalize exactly what counts as the allowed filtered/graded datum and determine whether it contains (G/G_4), or an equivalent extension class. No finite scan is authorized.


## 2026-09-19 — F5-A restricted graded carrier audit: PASS / F5 OPEN

A hand audit is recorded in `research/ORIENTATION_MOD9_FILTERED_FACTOR_F5_AUDIT_2026-09-19.md`.

The q-sensitive carrier is already visible in restricted/Zassenhaus degree 3: the independent q=3 versus q=infinity calculation gives
[
operatorname{in}_3(s_3)-operatorname{in}_3(s_\infty)=X_1^{[3]}.
]
Therefore the earlier wording that the q=3 power information is necessarily invisible to the associated graded restricted object is too strong and is corrected.

The minimal plausible graded carrier is
[
D_3=(V,R_2,P_3),
]
with degree-one (V), the quadratic Demuškin relation (R_2), and the degree-three restricted-power contribution (P_3).

Status:
- **F5-A carrier existence:** PASS.
- **F5 canonical obstruction reconstruction:** OPEN.

What remains is to define presentation-free operations
[
operatorname{Defect}(P_3),qquad operatorname{Twist}_\lambda(R_2)
]
whose sum is exactly (B_\lambda), and prove functoriality and uniqueness on (D_3).

Thus the project still must not claim full filtered/graded recovery. No finite scan is authorized.


## 2026-09-19 — F5 structural reconstruction: PASS for enriched degree-3 relation jet

The structural F5 task is closed at the precise enriched-carrier level. The correct carrier is the degree-3 relation jet
\[
J_3=\langle(R_2,P_3)\rangle\subset L_2\oplus L_3^{res},
\]
not two independently rescalable classes. Define, intrinsically,
\[
\operatorname{Defect}_{P_3}(f)=f(P_3),\qquad
\operatorname{Twist}_{\lambda,R_2}(f)=(\lambda\wedge f)(R_2).
\]
Then
\[
\Theta_{R_2,P_3}(\lambda)(f)=f(P_3)+(\lambda\wedge f)(R_2).
\]
In frozen coordinates this is exactly
\[
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4=B_\lambda(f).
\]
Common rescaling of the relation-jet generator rescales \(\Theta\) but leaves its zero set unchanged. Nondegeneracy of \(R_2\) makes the zero set a singleton; \(\lambda_\chi=(0,1,0,0)\), hence \(\rho=(1,4,1,1)\bmod9\).

Decision:
- **F5 structural factorization through enriched relation jet \(D_3=(V,J_3)\): PASS.**
- **Bare associated-graded object with no distinguished relation jet:** not claimed; recovery of \(J_3\) itself is a separate structural gate.

Detailed audit: research/ORIENTATION_MOD9_FILTERED_FACTOR_F5_STRUCTURAL_2026-09-19.md.
No finite scan is authorized.

## 2026-09-19 — Critical review of F5 structural PASS

The previous F5 PASS is narrowed. The formula Theta_{R,P}(lambda)(f)=f(P)+(lambda wedge f)(R) is correct once the marked degree-3 relation jet J_3=< (R,P) > is supplied, but this makes the factorization through the enriched carrier partly formal. Presentation/lift independence and naturality were stated too quickly for the unmarked problem, and minimality of D_3 was not proved.

Correct status:
- F1-F4: PASS at canonical finite-filtered-quotient level.
- F5-A: PASS for q-sensitive degree-3 carrier existence.
- F5-marked: PASS, conditional on the enriched relation jet J_3 being part of the datum.
- **F5-bare: OPEN.** The remaining substantive problem is whether the originally allowed bare filtered/graded datum canonically determines the distinguished relation jet J_3, or admits an equivalent unmarked reconstruction.

No finite scan is authorized.

## 2026-09-19 — F5-bare structural obstruction: FAIL / CLOSED

The remaining bare-graded identification question is now closed structurally, without a finite scan.

Compare
G_3 = <x_1,x_2,x_3,x_4 | x_1^3[x_1,x_2][x_3,x_4]>
with
G_infinity = <x_1,x_2,x_3,x_4 | [x_1,x_2][x_3,x_4]>.

At p=3, the power term x_1^3 has Zassenhaus degree 3 while the commutator terms have degree 2. Hence both defining relators have the same initial quadratic form R_2=[X_1,X_2]+[X_3,X_4]. Standard Demushkin graded-presentation results identify the bare associated graded restricted Lie object from this initial relation, so the q=3 and q=infinity cases have the same bare graded object.

Nevertheless their orientations differ already mod 9:
chi_3(x_2)=4 mod 9, while chi_infinity(x_2)=1 mod 9.

Therefore the bare associated graded restricted Lie object cannot determine chi mod 9, and in particular cannot canonically reconstruct the marked coupling J_3=< (R_2,P_3) >.

Important correction to F5-A: P_3=X_1^[3] exists in the ambient degree-3 restricted layer, but its being the degree-3 component of the same filtered defining relation as R_2 is extra marking/coupling data. The bare graded object does not retain that coupling.

Final branch status:
- F1-F4: PASS at the canonical finite-filtered-quotient level.
- F5-A: PASS only for existence of a q-sensitive ambient degree-3 carrier.
- F5-marked: PASS, conditional on J_3 being supplied.
- F5-bare: FAIL / CLOSED.

This is an information-level obstruction, not a failed implementation. No finite scan is authorized for reopening this route.

Detailed audit: research/ORIENTATION_MOD9_FILTERED_FACTOR_F5_BARE_OBSTRUCTION_2026-09-19.md.


## 2026-09-19 — Minimal enriched carrier: projective relation jet

After closing F5-bare, the next task is to identify the weakest natural enrichment that can still recover chi mod 9. The candidate is the projective degree-3 relation jet J_3=< (R,P) > in L_2 direct-sum L_3^res, retaining the coupling between the quadratic relation R and its degree-3 filtered component P while forgetting common scalar normalization.

The construction Theta_J(lambda)(f)=f(P)+(lambda wedge f)(R) is sufficient: for nondegenerate R it has a unique zero, and in frozen coordinates R=[X_1,X_2]+[X_3,X_4], P=X_1^[3] gives lambda_chi=e_2^*. The q=3 versus q=infinity obstruction proves that some information beyond the bare graded object is necessary.

Important boundary: sufficiency is established conditional on J_3 being supplied. Intrinsicness/presentation-independence of J_3 is the new E1-E5 structural gate. Do not call J_3 mathematically minimal yet; only the weaker necessary lower bound is justified.

Detailed plan: research/ORIENTATION_MOD9_MINIMAL_ENRICHED_CARRIER_2026-09-19.md.
No finite scan is authorized.


## 2026-09-19 — E1 relator-gauge audit: local PASS / full intrinsicness OPEN

A critical no-scan audit tested the candidate projective degree-3 relation jet against relator conjugation. If a filtered relator has degree-(2,3) terms (R,P), replacing it by u r u^{-1} with degree-one term v leaves R unchanged and changes the degree-3 ordinary Lie component by P -> P+[v,R] (up to convention/sign). Therefore common scaling alone is not a sufficient presentation-independence argument.

The recovery functional nevertheless descends through this gauge: for f in V*=H^1(G,F_3), f([v,R])=0, so f(P+[v,R])=f(P), while (lambda wedge f)(R) is unchanged. Hence Theta_{R,P} and its zero set are invariant under relator conjugation.

Decision:
- **E1-local gauge compatibility: PASS.**
- **E1-full intrinsic definition: OPEN.**

The next task is to identify the canonical relation-module quotient containing all legitimate relator changes. In particular, [V,R] is a necessary gauge quotient but is not yet proved to be the complete gauge group. The projective relation jet remains a candidate sufficient carrier, not an intrinsic invariant yet. No finite scan is authorized.

Detailed audit: research/ORIENTATION_MOD9_E1_RELATOR_GAUGE_AUDIT_2026-09-19.md.


## 2026-09-19 — E1 relation-module candidate

The next structural step is to replace the chosen-relator jet by a relation-module container. For a minimal free presentation 1 -> R -> F -> G -> 1, the natural candidate is R/[F,R], which kills relator conjugation automatically. The desired degree-(2,3) jet should be extracted from its Zassenhaus-filtered image into L_2(F) direct-sum L_3^res(F).

This is only a candidate: R/[F,R] is relative to a chosen free presentation, and the degree-(2,3) jet map plus independence under changing minimal free presentation remain OPEN. Therefore E1 full intrinsicness is not PASS. No finite scan is authorized.

Detailed candidate audit: research/ORIENTATION_MOD9_E1_RELATION_MODULE_CANDIDATE_2026-09-19.md.
