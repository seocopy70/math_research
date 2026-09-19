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
