# HARD ATTACK 41 — k=2 PUSH-FORWARD VS INTRINSIC MOD-9 CARRIER
## 2026-09-20

### Target

Test the sharpened question from Hard Attacks 39–40:

> Is the scalar push-forward of the finite Yoneda extension class e_2 exactly the already-closed intrinsic degree-(2,3) obstruction (R,p)?

The critical requirement is to keep object types and the ambient H^2(rho)-dependence separate.

### 1. First type check: literal equality is not the right statement

At k=2 we have the finite extension
1 -> M_2 -> E_2 -> Q_2 -> 1
with e_2 in H^2(Q_2,M_2).

For a scalar coefficient A_2(rho)=Z/9(rho) and an equivariant map phi:M_2->A_2(rho), Yoneda/LHS naturality gives
phi_*(e_2) in H^2(Q_2,A_2(rho)).

By contrast, the intrinsic mod-9 carrier [(R,p)] is a projective relation-jet object, and its recovery functional is
Theta_(R,p)(lambda)(f)=f(p)+(lambda wedge f)(R).

Therefore the statement
phi_*(e_2) = (R,p)
is literally ill-typed: the two sides live in different constructions.

The correct target is equality after the canonical finite-level transgression/evaluation identification that sends the pushed-out extension class to its scalar lifting obstruction.

### 2. The corrected equality

For rho(x_i)=1+3a_i mod 9, write lambda=sum a_i e_i^*.

The twisted lifting obstruction for a mod-3 class f=(f_1,...,f_4) is
O_rho(f)
 = (1-a_2)f_1 + a_1 f_2 - a_4 f_3 + a_3 f_4.

Independently, for
R=[X_1,X_2]+[X_3,X_4],
p=X_1^(1),
the established intrinsic carrier gives
Theta_(R,p)(lambda)(f)
 = f(p)+(lambda wedge f)(R)
 = (1-a_2)f_1 + a_1 f_2 - a_4 f_3 + a_3 f_4.

Hence the scalar obstruction obtained from the pushed-out extension class agrees exactly with the intrinsic functional:
[finite transgression of phi_*(e_2)] = Theta_(R,p)
up to the already-controlled common H^2/transgression normalization.

This is stronger than agreement of the zero set: the complete coefficient-linear obstruction functional is the same.

### 3. Why this is genuinely an e_2 statement

Hard Attack 38 established
d_2(phi)=phi_*(e_2)
for the finite extension, up to the conventional global sign.

The twisted lifting obstruction is the same LHS transgression obstruction for lifting H^1(Q_2,F_3) through the coefficient extension F_3 -> Z/9(rho).

Therefore the chain is now explicit:

e_2
 -> phi_*(e_2)
 -> scalar transgression/lifting obstruction
 = Theta_(R,p).

The final equality uses the already audited Bockstein/relation-jet identification and the direct twisted calculation. It is not obtained by declaring Fox coordinates to be intrinsic.

### 4. What this closes

**PASS / CLOSED at k=2, at the level of the scalar obstruction functional:**

The actual finite Yoneda push-forward does not merely produce a numerically compatible mod-9 answer. After the canonical transgression identification, its scalar obstruction is exactly the previously established intrinsic degree-(2,3) functional [(R,p)].

Thus the mod-9 intrinsic carrier is not an unrelated parallel construction: it is the scalar shadow of the finite extension class e_2.

This closes the previously OPEN equality question in its correctly typed form.

### 5. What this does NOT close

It does not prove that the scalar-character family is faithful on e_2.

It also does not prove unique maximality of
|coker T_{e_2}(A_2(rho))|
without PD^2.

Most importantly, the equality of obstruction functionals does not remove the rho-dependence of the ambient group
H^2(Q_2,A_2(rho)).
The selector quantity is
|coker T_{e_2}(A_2(rho))|,
and the coker size depends on both:
- the ambient H^2(Q_2,A_2(rho));
- the image of the pushed-forward extension/transgression.

Thus identifying the numerator-side obstruction does not by itself establish maximality.

### 6. Strategic consequence

Hard Attack 41 changes the main question.

The issue is no longer whether the known intrinsic mod-9 carrier has anything to do with e_2. It does.

The remaining finite-level obstruction is precisely the ambient-size problem plus the comparison of image dimensions:

C_2(rho) = H^2(Q_2,A_2(rho)) / im(delta_{2,rho}).

The next serious theorem target is therefore a rho-uniform calculation/bound on
h_2(rho)=|H^2(Q_2,A_2(rho))|
together with the already identified scalar obstruction.

If h_2(rho) is constant on the candidate character space, the intrinsic Theta calculation would immediately control the coker profile. If h_2(rho) varies, its variation must be incorporated explicitly; no maximality claim may ignore it.

### Decision

- Literal equality e_2-push-forward = (R,p): **FAIL / CLOSED as ill-typed formulation**.
- Correctly typed equality after transgression/evaluation: **PASS / CLOSED at k=2**.
- Intrinsic [(R,p)] as the scalar shadow of e_2: **PASS / CLOSED at mod 9**.
- Restricted Kummer faithfulness K_2=0: **OPEN / DECISIVE**.
- Unique scalar-character coker maximizer without PD^2: **OPEN / DECISIVE**.
- Ambient H^2(rho)-uniformity/control: **OPEN / LOAD-BEARING**.

### Bottom line

Hard Attack 41 does reach the intended bridge, but the bridge is a naturality/evaluation identity, not a literal equality of differently typed objects.

The mod-9 intrinsic carrier is now anchored directly to the finite Yoneda extension e_2. The remaining front is narrower and harder: control the rho-dependent ambient H^2 term before making any maximality claim.

No broad numerical scan is authorized.
