# PAPER 4 — GATE T1-B: CRITICAL NORM BOUNDARY — 2026-10-03

## Decision

The class-2/norm branch has been pushed to its exact logical boundary. The norm identity is valid, but at the *critical depth for the same parameter* it becomes homogeneous and therefore does not by itself certify finite nonsplitting.

For
\[
G_{s,a}=\langle z,x_1,\ldots,x_d\mid z^{p^s}=r_D\rangle,
\qquad
r_D=x_1^{p^a}[x_1,x_2]\cdots[x_{d-1},x_d],
\qquad s>a,
\]
and
\[
W_s=G_{s,a}/D_{p^s+1}(G_{s,a}),
\]
the class-2 kernel data satisfy, for every \(x\in D\),
\[
N_{p^s}(T_x)c_x(\bar z)=[r_D,x].
\]
But in \(G_{s,a}\),
\[
r_D=z^{p^s},
\]
hence
\[
[r_D,x]=[z^{p^s},x]\in[D_{p^s},D_1]\subseteq D_{p^s+1}.
\]
Therefore in the critical quotient
\[
N_{p^s}(T_x)c_x(\bar z)=0.
\]

This is a decisive logical boundary: **critical-layer visibility of \(z^{p^s}\) does not turn the norm identity into a nonzero obstruction.**

## 1. What is proved

### Lemma — critical norm annihilation

At \(n=p^s+1\), the class-2 norm-action identity reduces to
\[
\boxed{N_{p^s}(T_x)c_x(\bar z)=0}
\]
for every quotient generator \(x\).

Proof:
\[
z^{p^s}=r_D
\]
and the Zassenhaus commutator estimate
\[
[D_i,D_j]\subseteq D_{i+j}
\]
give
\[
[r_D,x]=[z^{p^s},x]\in D_{p^s+1}.
\]
Passing to the finite critical window kills the right-hand side.

This is independent of the choice of section; it is a consequence of the defining relation plus filtration.

## 2. Consequence for the previous T1-A claim

The earlier classification “class-2/norm obstruction = OPEN / LOAD-BEARING” must be narrowed.

The norm identity is still a genuine non-coinvariant datum, but **the identity itself is not a nonzero extension-class witness at the exact critical depth**.

Thus:

- critical scalar/coinvariant defect: **FAIL / CLOSED**;
- critical norm equation as a nonsplitting witness: **FAIL / CLOSED**;
- non-coinvariant module action as structure: **PASS / LOCAL**;
- full module-valued extension class: **OPEN / LOAD-BEARING**.

This does **not** prove that the finite relative extension splits. It only closes the proposed norm-equation shortcut as a proof of nonsplitting.

## 3. Fixed-threshold T1 is different

For a fixed external threshold \(m>a\), take a window deep enough to contain the \(p^m\)-layer.

Then for \(s<m\),
\[
[r_D,x]=[z^{p^s},x]
\]
can occur at filtration depth \(p^s+1\le p^m\), whereas for \(s\ge m\),
\[
[z^{p^s},x]\in D_{p^m+1}
\]
is invisible.

Hence the norm identity has a genuine *potential* threshold signal:
\[
s<m \quad\Longrightarrow\quad
[r_D,x]\text{ may survive},
\]
\[
s\ge m \quad\Longrightarrow\quad
[r_D,x]=0
\text{ in the }p^m+1\text{ window}.
\]

However, this is not yet a T1 theorem. To promote it, one must prove that the surviving/non-surviving commutator condition is an intrinsic invariant of the compressed class-2 extension after quotienting all kernel automorphisms and changing lifts. In particular, one may not name \(z\) or a chosen \(x\)-lift in the final invariant unless those are characterized intrinsically.

## 4. Independent algebraic check: Fox/module boundary

For the rank-two stress relation
\[
r_D=x^q[x,y],\qquad q=p^a,
\]
the evaluated Fox row in the Demuškin quotient simplifies to
\[
\frac{\partial r_D}{\partial x}
=
N_q(x)+x^q-y,
\qquad
\frac{\partial r_D}{\partial y}
=
x^{q+1}-1,
\]
where
\[
N_q(x)=1+x+\cdots+x^{q-1}.
\]

This confirms the structural source of the previous coinvariant cancellation: applying augmentation sends the first coefficient to \(q\), so the scalar defect \(p^s\) can be absorbed by a correction of size \(p^{s-a}\).

Before coinvariants, the residual contains the non-scalar \((y-1)\)-direction. This identifies exactly where a genuine module-valued obstruction *could* live.

But this calculation is **not** promoted to a theorem of non-splitting yet: a complete proof requires the actual finite kernel module \(A_s\), its quotient by all lift-change coboundaries, and verification that the residual class survives the finite Zassenhaus truncation. The Fox row is therefore supporting evidence, not a new PASS.

## 5. Literature/method control

Pro-p relation-module theory gives an exact Fox-derivative description of the relation module and its group action; this is the correct formalism for the remaining module-valued calculation. citeturn1search19turn1search3

The literature supports using the conjugation-action relation module rather than a presentation-dependent scalar coefficient, but it does not supply the present finite-window extension-class calculation. No novelty claim is made from the Fox formulas alone.

## 6. Authoritative classification after T1-B

- critical-layer visibility \(z^{p^s}\ne0\): **PASS / LOCAL**;
- scalar central H^2 shortcut: **FAIL / CLOSED**;
- abelianized/coinvariant obstruction: **FAIL / CLOSED**;
- critical norm identity as nonsplitting witness: **FAIL / CLOSED**;
- non-coinvariant module action: **PASS / LOCAL**;
- full finite module-valued extension class: **OPEN / LOAD-BEARING**;
- fixed-threshold T1 via norm visibility: **CONDITIONAL / NOT YET PROMOTED**;
- exact relative threshold \(p^s+1\): **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

## 7. Next authorized action

The next step is no longer “try another norm.”

Compute the actual finite abelianized kernel module \(A_s\) and its relation-module presentation at \(n=p^s+1\), then determine whether the extension-defect class is zero in
\[
H^2(Q_s,A_s)
\]
after **all** lift changes.

The rank-two Fox row above is the starting differential, not the conclusion.

If that class vanishes, the critical relative extension may split and the exact-threshold claim must be downgraded. If it survives, the surviving class is the first rigorous candidate for a load-bearing threshold obstruction.
