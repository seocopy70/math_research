# HARD ATTACK 39 — YONEDA / COEFFICIENT-PROFILE COMPLETENESS
## 2026-09-20

### Purpose

Hard Attack 38 established, for the finite extension
1 -> M_k -> E_k -> Q_k -> 1
with extension class e_k in H^2(Q_k,M_k), that the LHS transgression is the push-forward
d_2^{0,1}(phi) = phi_*(e_k)
for phi in Hom_{Q_k}(M_k,A), up to the conventional global sign.

Hard Attack 39 attacks the stronger statement suggested by the phrase
"e_k <-> universal transgression profile".

The central distinction is between:

(A) the profile over ALL Q_k-modules A and all equivariant maps phi:M_k->A;

(B) the restricted profile actually used by the Kummer selector, namely the family of coefficient modules A_k(rho), rho:Q_k->U_k.

These are not automatically equivalent.

### 1. Full coefficient-category profile: exact Yoneda completeness

Let C=Mod_{Z[Q_k]} (or the appropriate finite Q_k-module category), and define
T_e(A): Hom_Q(M_k,A) -> H^2(Q_k,A),
phi |-> phi_*(e).

The class e_k is itself recovered by evaluating the profile at
A=M_k, phi=id_{M_k}:
T_{e_k}(M_k)(id_{M_k}) = e_k.

Conversely, e_k determines every T_e(A) by functorial push-forward.

Therefore the map
e in H^2(Q_k,M_k)
  -> {T_e(A)}_{A in C}
is bijective onto its image, and in fact is injective for the trivial reason that the identity coefficient object is included.

Classification:
**PASS / CLOSED — full coefficient-category profile is information-complete.**

But this is a Yoneda-level tautology, not yet the desired orientation theorem. It says only that the entire extension class is equivalent to its action under all coefficient push-forwards.

### 2. Restricted Kummer profile: completeness is a new theorem, not automatic

The actual selector only probes the family
A_k(rho)=Z/3^k with twisted Q_k-action,
for candidate rho.

Define the restricted observation map
Phi_k:
H^2(Q_k,M_k)
 -> product_{rho} product_{phi in Hom_Q(M_k,A_k(rho))}
    H^2(Q_k,A_k(rho)),
e |-> (phi_*(e))_{rho,phi}.

Its kernel is
K_k =
intersection_{rho,phi} ker(phi_*).

Hence the restricted coefficient profile determines e_k iff
K_k=0.

Nothing in the Yoneda identity implies K_k=0, because the family A_k(rho) does not contain M_k in general and there is no automatic density/generator theorem for this restricted family.

This is the decisive correction to the naive statement
e_k <-> T_{e_k}
when T is understood only on the Kummer coefficient family.

Classification:
**OPEN — restricted Kummer profile completeness.**

### 3. What this means for the selector problem

The selector does not require recovery of the entire e_k in principle. It only requires enough of e_k to determine the cardinality/function
|coker T_{e_k}(A_k(rho))|
for every rho.

Thus the relevant object is weaker than full extension-class reconstruction.

Define the selector-observation functor
O_k(e)(rho) =
coker[
Hom_Q(M_k,A_k(rho))
 -> H^2(Q_k,A_k(rho))
].

The PD^2 theorem says, externally, that this cardinality is maximal exactly at chi mod 3^k.

The remaining PD²-independent theorem is therefore not
"recover e_k from all coefficient modules",
but the sharper statement:

For the specific Demushkin extension e_k, the function
rho |-> |O_k(e_k)(rho)|
has a unique maximizer, and this maximizer is the canonical orientation residue.

That statement is genuinely finite and q-blind in its input, but it is still OPEN without an independent orientation theorem.

### 4. Stronger structural reformulation: annihilator quotient

The restricted family sees only the quotient
H^2(Q_k,M_k)/K_k.

Equivalently, e_k may be replaced by any e'_k with
e_k-e'_k in K_k
without changing ANY push-forward class into the allowed Kummer coefficient modules.

Therefore, if K_k is nonzero, the full extension class contains information invisible to the selector.

This yields a precise candidate for the "coarsest coefficient-visible extension datum":
[e_k]_{Kummer} in H^2(Q_k,M_k)/K_k.

This is not yet proved to be a small or minimal carrier; it is only the exact quotient detected by the chosen coefficient family.

### 5. Coordinate Fox comparison: what is now legitimate

Hard Attack 38 changed the status of the Fox row.

It is now legitimate to ask whether, after choosing a presentation and cocycle representatives, the known twisted Fox obstruction is the coordinate expression of
phi_*(e_k).

A proof would have to:

1. construct the extension cocycle representing e_k from a section Q_k -> E_k;
2. push it out along phi;
3. identify the resulting H^2(Q_k,A_k(rho)) class with the crossed-word/Fox obstruction;
4. verify invariance under changing the section and presentation.

Only after these steps may the Fox row be used as a computational realization of the intrinsic map.

The prior Nielsen-change failure of naive degree-3 Fox truncation remains fully compatible with this: a coordinate expression of the FULL intrinsic push-forward may be natural even when a fixed low-degree truncation of that expression is not.

### 6. Attempt to remove PD² at the finite-cohomology level

The finite-input target is now:

For Q_k=G/P_{k+1}, M_k=P_{k+1}/(P_{k+1}^{3^k}[P_{k+1},P_{k+1}]), and the Demushkin extension class e_k, prove directly from finite group/coefficient data that
|O_k(e_k)(rho)| <= 3^k
with equality for exactly one rho,
without identifying O_k(e_k) with H^2(G,A_k(rho)) and without invoking the canonical dualizing action.

The basic identity
coker(delta)=im(inflation)
is not sufficient by itself: it identifies the coker with the image of H^2(Q_k,A) in H^2(E_k,A), but gives no intrinsic reason why one candidate action should maximize that image.

Thus the finite cohomology attack has not yet closed the selector gate.

### 7. Critical logical boundary

The following implications are now separated:

e_k
  -> full coefficient profile T_e
is **PASS / CLOSED**, by evaluation at (M_k,id).

e_k
  -> restricted Kummer profile
is **OPEN** unless K_k=0 is proved.

restricted Kummer profile
  -> unique rho
is **OPEN / decisive** without PD².

PD²
  -> unique rho=chi mod 3^k
is already **PASS / LOCAL** from the established finite coker theorem.

Therefore Hard Attack 39 does NOT prove the hoped-for complete equivalence in the restricted setting. Instead it removes a hidden ambiguity in the word "profile" and makes the remaining problem strictly sharper.

### 8. Research consequence

The next attack should not waste effort proving the full Yoneda statement; that part is now closed and structurally elementary.

The two serious targets are:

(A) prove K_k=0 or identify a smaller sufficient quotient of e_k for the Kummer family; and/or

(B) directly prove uniqueness/maximality of rho from the restricted push-forward coker profile.

A numerical scan is still not authorized. The next computation, if any, must first be tied to a theorem about K_k, the restricted coefficient family, or the explicit finite extension cocycle.

### Final classification

- e_k -> full coefficient-category transgression profile: **PASS / CLOSED** (Yoneda-complete, but tautological at the level of information completeness).
- e_k -> restricted Kummer coefficient profile: **OPEN**.
- restricted profile -> unique orientation selector without PD²: **OPEN / DECISIVE**.
- Fox row as coordinate realization of phi_*(e_k): **OPEN**.
- PD²-based finite selector: **PASS / LOCAL**.
- carrier minimality: **OPEN**.
- strict carrier-tower naturality: **OPEN**.

### Bottom line

The phrase
e_k <-> T_{e_k}
is correct only when T ranges over a coefficient category containing M_k and the identity map.

For the actual Kummer family A_k(rho), this is a separate nontrivial faithfulness problem.

That is the precise logical boundary exposed by Hard Attack 39.
