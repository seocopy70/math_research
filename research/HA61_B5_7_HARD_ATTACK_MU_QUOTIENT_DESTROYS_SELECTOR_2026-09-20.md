# HA61-B5-7 — HARD ATTACK: QUOTIENTING MU DESTROYS THE NEXT-DIGIT SELECTOR — 2026-09-20

## Stronger verdict

The simple affine quotient
(T2,mu) / <(p,lambda)>
is not merely unproved; as an orientation carrier it has a structural defect. The coordinate mu is the coefficient-extension parameter distinguishing different lifts rho_3=rho_2(1+9mu). These are precisely the candidate next-digit coefficient actions. A presentation gauge cannot identify mu with mu+a lambda without identifying distinct coefficient actions.

Thus the proposed quotient cannot be the canonical orientation-recognition object in the stated category.

## 1. Why mu is not a disposable gauge coordinate

Fix an intrinsic rho_2 and lambda. The three values
mu, mu+lambda, mu+2lambda
are distinct H^1(G,F_3) classes when lambda != 0, and they define distinct coefficient characters rho_3=rho_2(1+9mu) modulo 27.

The secondary obstruction is intended to select one of these lifts. Therefore an equivalence relation
mu ~ mu+a lambda
would identify the very alternatives that the secondary obstruction is supposed to distinguish.

This is not a mere presentation-normalization issue.

## 2. Coefficient-module gauge does not repair this

Automorphisms of the rank-one coefficient module are global units; changing a section/lift representative changes cocycle representatives, not the underlying character rho_3. Such changes therefore cannot legitimately turn two distinct rho_3 into the same intrinsic coefficient action.

Consequently, an enlarged coefficient-coordinate gauge may change the formula used to represent the obstruction, but it cannot be allowed to quotient distinct rho_3 values if the target is orientation reconstruction.

## 3. Interpretation of the previous compensator

The law
(t2,mu) -> (t2+a p,mu+a lambda)
can still be an identity between two coordinate descriptions of the same numerical obstruction expression, but then the two sides must correspond to different coordinate charts/trivializations, not to an intrinsic orbit relation on the candidate orientation data.

The correct intrinsic object is therefore more plausibly the entire obstruction family
( rho_2, rho_3 ; delta_3 )
or, after eliminating presentation coordinates, a natural affine functional in the coefficient-action variable.

## 4. New structural target

Instead of quotienting (t2,mu), define the intrinsic secondary obstruction as a function of the candidate coefficient action:

delta_3 : {rho_3 lifting rho_2} -> H^2(G,F_3).

Then prove that changing a presentation/lift representative leaves this function unchanged as a function on the same intrinsic set of coefficient actions.

At the representative level, the t2/[v,R] change must be paired with whatever change occurs in the coordinate expression for delta_3, while the abstract rho_3 (hence mu) stays fixed.

Only after this function is shown intrinsic should one ask whether it admits a coordinate expression
f(t2)+(mu wedge f)(R)
with a representative-dependent t2.

## 5. Consequence for B5

The following stronger claim is now closed:

- canonical orientation carrier obtained by quotienting mu along the diagonal direction: **FAIL / CLOSED**.

The following remain open:

- intrinsic function-valued secondary obstruction on the affine space of coefficient lifts: **OPEN / LOAD-BEARING**;
- presentation-independent construction of its coordinate-free t2/affine representative: **OPEN / LOAD-BEARING**;
- whether the resulting function has the expected unique zero: **PASS / LOCAL** only on the already audited standard-family normal forms;
- HA61-B overall: **OPEN / LOAD-BEARING**.

This is a genuine correction, not merely a downgrade: the quotient strategy is now ruled out as the orientation carrier because it collapses the parameter the obstruction is supposed to select.
