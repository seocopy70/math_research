# HA60 CRITICAL REVIEW — SCOPE CORRECTION AND LOAD-BEARING GAPS — 2026-09-20

## 1. Verdict

The proposed critical review of HA60 is accepted and should be strengthened.

HA60 is a genuine structural advance: it replaces the naive delta_3 -> delta_2 square by a successive lifting-obstruction ladder and gives direct standard-family mod-27 computations. However, the previous HA60 status labels **PASS / CLOSED** were too strong.

The correct present classification is:

- successive coefficient-extension mechanism at the audited two-stage level: **PASS / LOCAL**;
- P_4 residual compatibility with the mod-9 mechanism on the standard family: **PASS / LOCAL**;
- scalar normalization for the standard-family calculation relative to the chosen filtered normal form: **PASS / LOCAL**;
- intrinsic presentation-independent definition of t_2: **OPEN / LOAD-BEARING**;
- general formula for delta_3: **OPEN / LOAD-BEARING**;
- all-n induction: **OPEN / DECISIVE**.

## 2. Critical issue: the displayed delta_3 formula may be incomplete

The formula

delta_3(z) = [z_bar(t_2) + (mu wedge z_bar)(R)] omega

must not yet be promoted to a general theorem.

At n=2 -> 3, the base A_2-action may already be nontrivial. In particular, the q=3 standard-family case has rho_2(x_2)=4 mod 9, whereas the q=9 case has trivial rho_2.

Therefore a complete crossed-word expansion must first establish whether the secondary obstruction contains an additional term depending on the already-fixed rho_2 / first-stage lift data, schematically

delta_3(z) = [ z_bar(t_2) + B_{rho_2}(z) + (mu wedge z_bar)(R) ] omega,

with B_{rho_2} either identically zero by a structural cancellation theorem or explicitly identified.

The q=9 calculation alone cannot rule this out, because rho_2 is trivial there. The q=3 calculation must be re-derived term-by-term before using the displayed formula as the template for induction.

This is the most important mathematical audit point in HA60.

## 3. The t_2 problem is more fundamental than scalar normalization

There are three logically distinct claims:

1. a standard-family word calculation detects the next digit;
2. a canonical filtered residual t_2 exists in that calculation;
3. t_2 is an intrinsic, presentation-independent natural transformation of the admissible filtered input.

HA60 securely supports (1). It gives substantial evidence for (2). It does not yet prove (3).

Therefore the phrase “the canonical filtered power map fixes the scalar” is currently too strong. What is established is:

> once the residual is represented by the chosen filtered power map in the standard family, its coefficient fixes the scalar selected by the obstruction.

The remaining theorem is that the same residual and coefficient are canonically defined under generator changes, relator gauge, and arbitrary admissible Demushkin isomorphisms.

## 4. Primary-lift hypothesis needs explicit domain

The secondary connecting map is defined on H^1(G,A_2), so the existence of an A_2 lift is not an automatic premise for an arbitrary rho_2.

The tower must therefore be formulated on the zero locus of the previous obstruction:

Lift_n(rho_n) := { z in H^1(G,A_n) : red(z)=f and delta_n(z)=0 }.

Only on this domain is the next connecting obstruction naturally evaluated.

For the orientation-selection problem this may be sufficient, because candidate rho_n are precisely filtered by successive solvability. But it must be stated as part of the theorem rather than hidden in the notation.

## 5. omega normalization

The H^2 generator omega is not intrinsically a scalar basis without additional orientation/fundamental-class normalization.

At the first stage, a common rescaling is harmless because the zero locus is unchanged. At the higher stage, however, claims about an exact scalar digit must specify which normalization has already been transported from the mod-9 obstruction.

Thus scalar normalization has two separate components:

- normalization of the filtered residual t_2;
- normalization of the target omega.

HA60 substantially addresses the first inside the chosen construction, but the second must be explicitly carried through the coefficient-extension diagram.

## 6. Corrected strategic interpretation

The strongest defensible statement after HA60 is not yet

“the P_4 scalar normalization is closed.”

It is:

> HA60 shows that the P_4 residual participates in a genuine secondary coefficient-extension obstruction and that, in the audited standard-family normal forms, the obstruction uniquely selects the expected next digit without importing the known orientation formula.

This is already a strong result.

The next gate is not a broad search. It is a **structural reconstruction of the n=2 -> 3 calculation**, followed immediately by a gauge/naturality test.

## 7. Authorized HA61 target

HA61 should proceed in this exact order:

### HA61-A — full n=2 -> 3 crossed-word derivation

Derive delta_3 from

0 -> F_3 -> Z/27(rho_3) -> Z/9(rho_2) -> 0

for a general crossed cocycle z lifting f.

Separate every term into:

1. old rho_2-dependent terms;
2. new extension parameter mu terms;
3. quadratic R terms;
4. new P_4/power residual terms;
5. D_4/P_4 error terms.

Do not assume the compact HA60 formula.

### HA61-B — cancellation test

Determine whether the rho_2-dependent contribution B_{rho_2} vanishes identically, is absorbed into the transported mod-9 normalization, or survives as an additional term.

This is a decisive branch.

### HA61-C — intrinsic t_2 gate

Only after the formula is correct, define t_2 as a natural filtered extension class rather than by the standard normal form.

Test invariance under:

- generator/Nielsen changes;
- relator conjugation;
- multiplication by allowed relator-gauge terms;
- change of fundamental-class representative.

### HA61-D — only then formulate n -> n+1

The induction ansatz is admissible only after n=2 -> 3 has been proved in an intrinsic form.

## 8. Research-level conclusion

HA60 should be retained as a major positive local result, but its CLOSED labels should be downgraded.

The important conceptual achievement remains:

graded information alone is insufficient, and the next 3-adic digit appears through a successive coefficient-extension obstruction coupled to the next filtered power/relation layer.

The decisive unresolved issue is now sharper than before:

\[
\boxed{
\text{Does the secondary obstruction formula itself admit an intrinsic, gauge-natural, all-input formulation?}
}
\]

If yes, the tower program becomes mathematically credible. If no, the exact surviving rho_2-dependent or gauge-dependent term will identify the logical boundary.

Record status: **HA60 = PASS / LOCAL, not PASS / CLOSED.**
