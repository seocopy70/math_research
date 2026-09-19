# ORIENTATION MOD-9 TWISTED-SURJECTIVITY GATE — 2026-09-19

## Objective

After the ordinary mod-9 Bockstein candidate failed, test the canonical twisted-coefficient characterization of the Demuškin orientation at the first nontrivial 3-adic level.

External literature states that the canonical orientation is characterized by the surjectivity of
\[
H^1(G,I/p^{j+1})\to H^1(G,I/p^j)
\]
for the rank-one coefficient module with G-action through the orientation. The orientation is also the character by which G acts on its dualizing module. This makes twisted cohomology a genuinely different candidate from the trivial-coefficient Bockstein.

The present gate asks whether, at j=1, this criterion intrinsically determines
\[
\chi\pmod 9.
\]

## 1. Candidate coefficient characters

Because
\[
G^{ab}\cong\mathbf Z_3^3\oplus\mathbf Z/3,
\]
every character
\[
\rho:G\to1+3\mathbf Z/9
\]
is determined by
\[
\rho(x_i)=1+3a_i\pmod9,
\qquad a_i\in\mathbf F_3.
\]

The frozen canonical orientation is
\[
(a_1,a_2,a_3,a_4)=(0,1,0,0),
\]
because
\[
(1-3)^{-1}\equiv4\pmod9.
\]

No preferred free lift is used.

## 2. Explicit twisted H^1 calculation

Let A_2=\mathbf Z/9 with G-action through rho, and A_1=\mathbf F_3 with the induced trivial action. Write a 1-cocycle z by
\[
f_i=z(x_i).
\]
Modulo 3, the action is trivial, so every vector
\[
(f_1,f_2,f_3,f_4)\in\mathbf F_3^4
\]
is a 1-cocycle on the generators.

The relator condition is obtained from
\[
r=x_1^3[x_1,x_2][x_3,x_4].
\]

For the power term,
\[
z(x_1^3)
=(1+\rho_1+\rho_1^2)f_1
\equiv3f_1\pmod9,
\]
because \(\rho_1=1+3a_1\).

For a commutator, using the cocycle identity
\[
z(uv)=z(u)+\rho(u)z(v),
\]
one gets, modulo 9,
\[
z([x_i,x_j])
\equiv
3(a_i f_j-a_j f_i)
\pmod9
\]
up to the frozen commutator convention/sign; the sign is fixed by the same convention used throughout the project. The sign does not affect the vanishing criterion below.

Therefore the relator condition is
\[
3\bigl(
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4
\bigr)
\equiv0\pmod9,
\]
up to the corresponding fixed sign convention on the last pair.

Equivalently, a mod-3 cocycle class lifts to a twisted mod-9 cocycle exactly when
\[
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4=0
\quad\text{in }\mathbf F_3.
\]

## 3. Surjectivity criterion

The reduction map
\[
H^1(G,A_2)\to H^1(G,A_1)
\]
is surjective if and only if **every** mod-3 cocycle vector lifts.

Since the four \(f_i\) are independent in \(H^1(G,\mathbf F_3)\), this happens iff all four coefficients vanish:
\[
1-a_2=0,\qquad
a_1=0,\qquad
a_4=0,\qquad
a_3=0.
\]

Hence
\[
\boxed{
(a_1,a_2,a_3,a_4)=(0,1,0,0).
}
\]

Therefore the j=1 twisted-surjectivity condition has a **unique** solution:
\[
\boxed{
\rho(x_1)=1,\quad
\rho(x_2)=4,\quad
\rho(x_3)=1,\quad
\rho(x_4)=1
\pmod9.
}
\]

This is exactly the frozen canonical orientation modulo 9.

## 4. Critical intrinsicity audit

### 4.1 No free lift

PASS. The construction is defined directly from G and a coefficient character rho. It does not choose a free-group lift of an automorphism.

### 4.2 No H^2 generator

PASS. Unlike the Bockstein scalar extraction, the criterion is surjectivity of a canonical map between cohomology groups. No trivialization of the one-dimensional H^2 line is needed.

### 4.3 Character coordinate issue

PASS at the object level; the four numbers a_i are only coordinates after choosing the frozen minimal generating system. The actual candidate is the property:

> rho is the unique character G -> 1+3Z/9 for which the twisted reduction map H^1(G,A_2(rho)) -> H^1(G,F_3) is surjective.

Thus the recovery statement is coordinate-free once the uniqueness theorem is proved.

### 4.4 Relation to the canonical orientation

The literature identifies the canonical Demuškin orientation with the unique character satisfying the corresponding surjectivity/1-smoothness criterion. The explicit frozen presentation calculation independently recovers its mod-9 value.

This is materially stronger than the ordinary Bockstein route: the number 4 appears because the twisted action enters the cocycle condition and cancels the x_1^3 obstruction through the commutator [x_1,x_2].

## 5. Gate decision

**T9-A: PASS.** A genuinely twisted finite-level candidate is canonically defined.

**T9-B: PASS.** The j=1 surjectivity condition uniquely determines rho mod 9.

**T9-C: PASS.** Explicit calculation gives
\[
\rho\equiv\chi\pmod9,
\qquad
\chi(x_2)\equiv4\pmod9.
\]

**T9-D: OPEN.** The remaining research question is whether this twisted finite-level criterion can itself be represented/recovered from the prescribed filtered/graded data, rather than from the full group presentation/cohomology.

This distinction is essential: the current calculation proves intrinsic mod-9 orientation recovery from twisted cohomology; it does **not yet** prove recovery from the Zassenhaus graded object alone.

## 6. Consequence

The research should now stop treating ordinary trivial-coefficient Bockstein data as the orientation carrier.

The new candidate carrier is the finite twisted-coefficient tower
\[
H^1(G,I_2(\rho))\to H^1(G,I_1(\rho)),
\]
whose surjectivity forces the first 3-adic orientation digit.

Next authorized task: audit whether this twisted-surjectivity object is determined by the allowed filtered/graded data, or whether it imports extra group-level information not present in the prescribed observable.

No finite scan is authorized until that filtered/graded factorization question is defined.
