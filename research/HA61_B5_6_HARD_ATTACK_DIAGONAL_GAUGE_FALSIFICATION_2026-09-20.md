# HA61-B5-6 — HARD ATTACK: IS THE (t2,mu) DIAGONAL SHIFT AN ACTUAL GAUGE ACTION? — 2026-09-20

## Verdict

The proposed diagonal law
(t2,mu) -> (t2+a p, mu+a lambda)
cannot yet be accepted as an actual presentation/lift gauge action. A stronger structural objection appears: for a pure relator-conjugation change, the abstract group G, the intrinsic coefficient character rho_2, the class lambda, and the candidate coefficient lift parameter mu are unchanged. Therefore a transformation of the actual coefficient-extension datum mu -> mu+a lambda is not induced merely by relator conjugation.

This does not prove the whole secondary construction impossible, but it invalidates the shortcut “relator conjugation is quotiented by a diagonal action on (t2,mu)” unless an additional change of coefficient trivialization/section is explicitly included and shown to be part of the admissible gauge category.

## 1. Pure relator-conjugation test

Take a filtered relator
r=(R,P)+O(4)
and replace it by
r'=v r v^{-1}.
At degree 2, R is unchanged; at degree 3,
P -> P+[v,R].

This is a presentation of the same abstract group. Hence any intrinsic coefficient action
rho_n:G -> (Z/3^n)^×
and its reductions/lift parameters are unchanged as abstract cohomology classes.

In particular, if
rho_3=rho_2(1+9 mu),
then under pure relator conjugation the abstract mu in H^1(G,F_3) is unchanged.

## 2. Tension with the formal compensator

The audited crossed-word calculation gives
T_{lambda,f}([v,R])
 = -lambda(v)(lambda wedge f)(R)
 = lambda(v) f(p)
on the primary-zero locus.

Writing a representative-level secondary formula as
delta_3 = [f(t2)+(mu wedge f)(R)] omega
therefore produces the formal compensation
t2 -> t2+a p,  mu -> mu+a lambda,
a=lambda(v),
if one insists that the displayed formula remain unchanged term-by-term.

But the second transformation is not a consequence of pure relator conjugation: mu is the abstract coefficient-extension parameter and remains fixed unless an additional coefficient trivialization/lift-coordinate change is simultaneously performed.

Thus the previous “diagonal gauge action” mixes two different operations:
(A) presentation/relator gauge on the relation jet;
(B) coordinate/gauge change in the coefficient-extension representative.

They must not be identified without constructing the combined group and its action.

## 3. Consequence for the quotient claim

The notation
[(t2,mu)] in (V^(2) direct sum V*) / F3(p,lambda)
is therefore not justified by relator conjugation alone.

More seriously, quotienting the mu-coordinate by lambda would identify distinct coefficient-action candidates unless the admissible object explicitly regards those candidates as the same coordinate representation of one intrinsic extension. That identification is currently unproved.

Hence:

- “obstruction-preserving compensator”: PASS / LOCAL;
- “relator-conjugation induces diagonal action on (t2,mu)”: FAIL / CLOSED as currently formulated;
- “some enlarged presentation+coefficient-trivialization gauge group induces a diagonal action”: OPEN / LOAD-BEARING;
- “canonical affine quotient/torsor”: OPEN / LOAD-BEARING, with the previous simple quotient construction superseded.

## 4. Important diagnostic

This attack exposes a likely source of the earlier apparent cancellation.

The term from [v,R] may be cancelled either by:
1. an actual change in the coefficient-extension coordinate/trivialization; or
2. a missing representative-level old-action/lift term in the decomposition.

Therefore the earlier statement
“gamma_2^3 gives no independent functional, hence it can simply be absorbed into the affine quotient”
is too strong.

What is established is only that its contribution lies in the span of the already occurring obstruction terms on the primary-zero locus. Its role in the intrinsic representative construction remains unresolved.

## 5. New authorized target

The next attack must define two distinct gauge groups:

Gamma_pres = presentation/relator/lift changes of the filtered one-relator data;

Gamma_coeff = coefficient-extension cocycle/trivialization/section changes.

Then determine whether there is a legitimate combined semidirect/crossed action
Gamma_pres ⋉ Gamma_coeff -> transformations of the chosen obstruction model.

Do not quotient the candidate orientation parameter mu unless the action is proved to identify coordinate choices of the same coefficient extension rather than distinct rho_3 classes.

For pure Gamma_pres action, test whether the intrinsic obstruction formula forces t2 itself to be invariant after all legitimate representative terms are included. If not, the carrier must be enlarged or redefined.

## 6. Classification update

- D4/D5 quotient: FAIL / CLOSED.
- G/P4 and D10 information window: PASS / LOCAL.
- gamma_2^3 independent new functional: FAIL / CLOSED only in the limited sense “not an independently detected scalar functional on the primary-zero obstruction”; its gauge role remains OPEN.
- cubic [v,R] calculation: PASS / LOCAL.
- raw t2 intrinsicity: FAIL / CLOSED.
- formal diagonal compensator: PASS / LOCAL.
- actual diagonal gauge action under pure presentation change: FAIL / CLOSED.
- enlarged combined presentation+coefficient gauge action: OPEN / LOAD-BEARING.
- canonical affine quotient/torsor: OPEN / LOAD-BEARING.
- HA61-B: OPEN / LOAD-BEARING.
- HA61-C: not opened.

This supersedes the stronger wording in HA61-B5-3 that treated the diagonal law as an already established combined affine action.
