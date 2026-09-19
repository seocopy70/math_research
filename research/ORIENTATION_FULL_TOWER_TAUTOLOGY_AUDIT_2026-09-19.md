# HARD ATTACK — FULL FILTERED TOWER TAUTOLOGY AUDIT — 2026-09-19

## Executive finding

A genuine weak link was found in the previously declared theorem

\[
\text{compatible full filtered relation-jet tower}\Longrightarrow\chi.
\]

The inverse-limit mathematics is correct, but the proposed input tower \(J_n\) was not independently constructed. It was defined using essentially the same coefficient-evaluation information that the theorem later extracts from it.

Therefore the previous “PASS / THEOREM CLOSED” status is too strong.

## 1. The circularity

The earlier definition says, in substance, that \(J_n\) contains the filtered relation data “required for the crossed-derivation calculation modulo \(3^n\).”

Then the extraction map is defined by evaluating that same datum:

\[
\mathcal C_n(J_n,\rho),
\]

and

\[
\Phi_n(J_n)=\{\rho:\mathcal C_n(J_n,\rho)=0\}.
\]

For the frozen presentation, the coefficient equations have a unique solution, so

\[
\Phi_n(J_n)=\{\chi_n\}.
\]

This implication is valid **if the stated \(J_n\) is already supplied as an independently defined object carrying those evaluations**.

But the construction does not prove:

1. that such a \(J_n\) exists canonically;
2. that it can be defined from the filtered relation module without mentioning the desired evaluation family;
3. that it is finite/non-tautological;
4. that arbitrary presentation changes preserve it;
5. that an independently defined filtered tower maps to the required coefficient-evaluation data.

Thus the theorem has an input-definition gap, not an inverse-limit gap.

## 2. What survives

The following remains sound.

### Fixed presentation

For

\[
r=x_1^3[x_1,x_2][x_3,x_4],
\]

the exact crossed-derivation equations force

\[
r_1=r_3=r_4=1,
\qquad
2+r_2^{-1}=0,
\]

hence

\[
r_2=(1-3)^{-1}=-1/2.
\]

The same equation modulo \(3^n\) gives the unique finite reduction. This is a genuine calculation.

### Inverse limit

If a compatible family \((\chi_n)\) has independently been obtained, then

\[
\mathbf Z_3^\times\cong\varprojlim_n(\mathbf Z/3^n)^\times
\]

does give a unique continuous \(\chi\). This step is not in doubt.

### Mod-9 carrier

The separately audited projective degree-(2,3) carrier

\[
[(R,p)]
\]

and its intrinsic twisted obstruction remain at their previously stated scope. The attack does not invalidate that finite-level result.

## 3. What is NOT proved

The following implication is currently unsupported as a substantive theorem:

\[
\boxed{
\text{canonical filtered relation-jet tower}
\Longrightarrow
\text{exact coefficient-evaluation tower}.
}
\]

The previously used definition of \(J_n\) effectively builds the right-hand side into the left-hand side.

Therefore “full compatible filtered relation-jet tower \(\Rightarrow\chi\)” must not be presented as an independent mathematical discovery until this bridge is supplied.

## 4. Correct theorem hierarchy after the attack

The strongest defensible hierarchy is now:

\[
\text{fixed q=3 defining relation + standard canonical-orientation criterion}
\Longrightarrow
\text{exact }\chi
\]

for the frozen presentation;

\[
\text{intrinsic degree-(2,3) projective carrier}
\Longrightarrow
\chi\bmod9;
\]

and

\[
\text{independently supplied exact finite-level evaluation data}
\Longrightarrow
(\chi_n)_n
\Longrightarrow
\chi.
\]

The missing arrow is the non-tautological construction

\[
\text{intrinsic filtered relation data}
\Longrightarrow
\text{exact finite-level evaluation data}.
\]

## 5. Required gates for any repair

A repaired full-tower theorem must pass all five gates independently:

1. **Intrinsic definition:** define the tower without referring to \(\chi\) or to “whatever data the evaluation needs”.
2. **Non-tautological information content:** identify explicit algebraic objects, not a quotient by the kernel of the desired observable unless that quotient is itself independently characterized.
3. **Gauge/presentation naturality:** prove change-of-presentation behavior.
4. **Evaluation factorization:** prove the crossed-derivation coefficient maps factor through the independently defined object.
5. **Level compatibility:** prove reduction from level \(n+1\) to \(n\).

Only after all five pass may the full-tower implication be upgraded to CLOSED.

## 6. Additional hostile check

A dangerous false shortcut is:

> “The full filtered relation contains the whole relation, therefore it automatically contains every crossed-derivation evaluation.”

This is not a proof of a canonical factorization. A relation element in a free presentation and an intrinsic filtered quotient are different mathematical objects, and the crossed-derivation evaluation also depends on the coefficient action \(\rho\). The evaluation must be shown to descend through the proposed quotient with the claimed gauge invariance.

## 7. Final decision

**FAIL / CLOSED — previous full-tower closure retracted.**

This is a productive failure: it isolates a genuine theorem-level gap rather than a computational error.

The exact frozen-presentation calculation is retained.

The next authorized target is the construction of a **non-tautological exact filtered evaluation carrier**, or a proof that no finite/concrete carrier of the desired kind exists.

No broad computation is justified until that definition gate is passed.
