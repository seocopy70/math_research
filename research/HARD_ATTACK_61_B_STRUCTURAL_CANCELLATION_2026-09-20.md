# HARD ATTACK 61-B — STRUCTURAL CANCELLATION OF THE OLD COEFFICIENT ACTION — 2026-09-20

## Verdict

**PASS / LOCAL**, with a precise boundary.

The q=3 calculation in HA61-A is not merely an accidental numerical cancellation. At the level of the two-stage coefficient-extension obstruction, the apparent old-action contribution is not an independent obstruction term once the input (A_2)-valued cocycle is restricted to the primary-obstruction zero locus.

More precisely, for
[
0\to \mathbf F_3\to A_3\to A_2\to0,
qquad
\rho_3=\rho_2(1+9\mu),
]
the secondary obstruction is computed from an actual (A_2)-cocycle (z) lifting (f\in H^1(G,\mathbf F_3)). The terms coming from the already-present (ho_2)-action occur in the chosen (A_2)-lift and are constrained by
[
\delta_2(f)=0.
]
They therefore do not define a new additive functional (B_{\rho_2}(z)). After changing the (A_2)-lift by the usual coboundary gauge, the only new coefficient-extension contribution is the cup-type term
[
(\mu\wedge f)(R).
]
The remaining relation contribution is the genuinely new filtered power/relation residual (f(t_2)).

Thus the correct structural form is
[
\boxed{
\delta_3(z)
=
\bigl[f(t_2)+(\mu\wedge f)(R)\bigr]\omega
}
]
on the primary zero locus, subject to the explicit definition of (t_2).

## 1. What was actually attacked

HA61-A established the cancellation in two frozen normal forms:
- (q=3), where the old mod-9 action is nontrivial;
- (q=9), where the old mod-9 action is trivial.

The remaining question was whether the q=3 cancellation was caused by the special word
[
x_1^3[x_1,x_2][x_3,x_4]
]
or is forced by the coefficient-extension mechanism itself.

The structural answer is the latter, but only at the level of the secondary connecting obstruction. It does **not** yet identify (t_2) presentation-free.

## 2. Why an independent (B_{\rho_2}) cannot survive

Write an (A_3)-lift of the (A_2)-cocycle (z) and evaluate the relator. Split the coefficient action as
[
\rho_3=\widetilde{\rho_2}(1+9\mu).
]

There are then three sources of terms modulo (27):

1. terms already present in the (A_2)-cocycle equation;
2. terms linear in the new extension character (mu);
3. the next relation/power residual.

After division by (9), source (1) is precisely the old lifting obstruction. Because (z) is an (A_2)-valued cocycle and (f=\bar z) satisfies (\delta_2(f)=0), source (1) has no independent secondary class. Changing the (A_2)-lift changes this part by the corresponding coboundary/gauge term, so a putative (B_{\rho_2}(z)) is not an invariant of the secondary obstruction.

Source (2) survives and is the derivative of the coefficient action:
[
\rho_3/\rho_2=1+9\mu,
]
hence its degree-two relation contribution is exactly the bilinear term
[
(\mu\wedge f)(R).
]

Source (3) is independent new filtered information and is represented by (t_2):
[
f(t_2).
]

This is the conceptual reason the q=3 and q=9 calculations have the same secondary slope even though their old mod-9 actions differ.

## 3. The important qualification

This does **not** prove that every arbitrary presentation of every minimal one-relator Demuškin group automatically has a visibly identical crossed-word formula.

The structural statement is invariant; a concrete word-level representative still requires:
- a definition of the next filtered residual (t_2);
- proof that changing the relator by the permitted (P_4/D_4) gauge changes (t_2) only by the corresponding intrinsic equivalence;
- synchronization of the (H^2) generator with the mod-9 convention.

Therefore the cancellation theorem is stronger than the frozen q=3 computation but weaker than a complete arbitrary-input presentation-free (t_2) theorem.

## 4. Independent consistency checks

The structural prediction matches both HA61-A branches:

### q=3
The old action is
[
\rho_2(x_2)=4,
]
yet the secondary coefficient is still
[
-a\,f_1
]
for the compatible lift parameter (a). No additive constant remains.

### q=9
The old action is trivial and the obstruction is
[
(1-a)f_1.
]
The same coefficient of the new parameter appears.

Thus the difference between the branches is carried by (t_2), not by an additional (B_{\rho_2}).

## 5. What this closes

- The feared **independent additive old-action obstruction** is not a separate structural datum at the (n=2\to3) coefficient-extension stage.
- The HA60 compact secondary pattern survives the HA61-A hard attack, after replacing the informal “reduction” language by the correct successive-obstruction statement.
- The q=3 calculation is therefore a verification of a structural cancellation mechanism, not merely a lucky numerical cancellation.

## 6. What remains open

The decisive unresolved theorem is now sharply isolated:

[
\boxed{
\text{intrinsic filtered data}
\Longrightarrow
\text{canonical }t_2
\Longrightarrow
\delta_3=
[f(t_2)+(\mu\wedge f)(R)]\omega.
}
]

In particular:
1. presentation-free construction of (t_2);
2. naturality under filtered isomorphisms;
3. relator/lift gauge independence;
4. extension of the cancellation mechanism to arbitrary (n\to n+1);
5. whether the resulting tower is non-redundant/minimal in a declared carrier category.

## 7. Decision

- **HA61-B: PASS / LOCAL.**
- Independent (B_{\rho_2}) at the secondary stage: **FAIL / CLOSED** as a separate invariant term.
- Secondary obstruction shape, conditional on the intrinsic (t_2) definition: **PASS / LOCAL**.
- General presentation-free (t_2): **OPEN / LOAD-BEARING**.
- All-digit induction: **OPEN / DECISIVE**.
- No representation scan is authorized.

## Next attack

HA61-C should attack the **intrinsic definition and gauge-independence of (t_2)** before any (n\to n+1) induction. The right target is the canonical (P_3/P_4) restricted-power residual modulo the information already represented by the mod-9 relation/power carrier.
