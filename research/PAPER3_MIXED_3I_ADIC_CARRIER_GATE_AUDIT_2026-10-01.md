# MIXED (3,I)-ADIC FOX CARRIER — DEFINITONAL / FINITE-PAIR GATE AUDIT — 2026-10-01

## Scope

This audit is the first authorized attack on the remaining genuinely-new-carrier branch after the O_k universal-property route was exhausted.

The candidate is a finite truncation of the completed Fox obstruction construction over
\[
A_F=\mathbf Z_3[[F]],\qquad \mathfrak m=(3,I_F),
\]
with a projective Fox relation row/ideal and finite quotient modulo \(\mathfrak m^n\).

No numerical scan is used in this audit.

## 1. Object

The correct candidate is not a raw truncated coefficient vector. It is the finite-level projective obstruction ideal/scheme obtained from the universal Fox row in the completed coefficient ring and then reduced modulo \(\mathfrak m^n\).

This distinction is forced by the already-closed relator-gauge and Nielsen attacks on raw degree truncations.

The relevant completed Fox construction is standard in pro-p Fox calculus: completed group algebras, relation modules, and Fox Jacobians provide the differential/obstruction map; the canonical Demushkin orientation is an intrinsic group invariant, not a presentation choice. These background facts are consistent with Labute's classification and standard completed Fox-calculus treatments. cite references recorded in research log: Labute 1967; Minac–Pasini–Quadrelli–Tan 2021; NSW Ch. V §6.

## 2. Intrinsicity attack

### 2.1 Relator conjugation

For \(r'=grg^{-1}\), the crossed-derivation identity gives
\[
D(r')=\tau(g)D(r),
\]
after cancellation of the conjugating terms because \(\tau(r)=1\).

Thus the universal Fox row changes by a unit. Its projective ideal/zero locus is unchanged.

### 2.2 Relation-generator gauge

Changing a generator of the cyclic one-relator relation module multiplies the relation by a unit in the completed coefficient ring. The projective Fox ideal is therefore unchanged.

### 2.3 Nielsen/free-basis change

Fox's chain rule transforms the row by an invertible Jacobian together with the induced formal coordinate substitution. Since a free-basis automorphism sends \(U_i=T_i-1\) to series with zero constant term and invertible linear Jacobian, it preserves the maximal ideal
\[
\mathfrak m=(3,U_1,\ldots,U_d).
\]
Therefore the induced finite quotient modulo \(\mathfrak m^n\) is carried isomorphically to the corresponding quotient in the new coordinates.

### Intrinsicity verdict

At the **universal completed Fox level**, and for the projective ideal rather than a raw coefficient vector:

\[
\boxed{\text{INTRINSICITY = PASS / LOCAL}}
\]

This is not yet PASS/CLOSED for the intended new finite carrier, because finite-level functoriality and factorization through the chosen finite pair have not yet been established.

## 3. Important distinction: mixed finite algebra vs the O_k finite pair

The natural mixed finite object is
\[
A_F/\mathfrak m^n.
\]

This is a genuinely different finite input from the mod-3 Zassenhaus pair
\[
W_k=(G/D_{3^{k-1}+1},D_{3^{k-1}+1}/D_{3^{k-1}+2}).
\]

The standard literature identifies Zassenhaus levels with powers of the augmentation ideal in \(\mathbf F_3[[G]]\), not with the mixed \((3,I)\)-adic filtration over \(\mathbf Z_3[[G]]\). Hence one must not silently identify the two filtrations. citeturn2search0turn2search1

Therefore the assertion

\[
A_F/\mathfrak m^n
\quad\text{is determined by}\quad
W_k
\]

is a separate theorem. It is currently not proved.

## 4. Finite-pair factorization gate

The required statement is:

> For the relevant \(n=n(k)\), there is a natural functor
> \[
> W_k\longmapsto \mathcal M_k(W_k)
> \]
> whose value is the mixed Fox carrier, and this construction is independent of the choice of presentation/lift.

No such factorization has yet been established.

In particular, the earlier standard-family threshold results concern quotient-isomorphism information in the mod-3 Zassenhaus filtration; they do not imply that the characteristic-zero mixed coefficient algebra is a functor of that finite pair.

Thus:

\[
\boxed{\text{FINITE-PAIR FACTORIZATION = OPEN / LOAD-BEARING}}
\]

No computation is authorized until this is resolved.

## 5. Orientation bridge gate

If finite-pair factorization survives, the next theorem must be an intrinsic finite-level bridge
\[
\mathcal M_k(W_k)
\longrightarrow
\chi\pmod{3^k},
\]
without inserting \(q\), \(\chi\), or a presentation into the definition.

The bridge cannot merely be
\[
\mathcal M_k\to q\text{-class}\to\chi
\]
because the project explicitly excludes classification repackaging as the new carrier theorem.

The exact universal Fox scheme already supplies the characteristic-zero comparison object. Therefore the mixed carrier must prove that a finite \(\mathfrak m\)-level quotient contains precisely the information needed for the finite orientation residue.

Current status:

\[
\boxed{\text{ORIENTATION BRIDGE = OPEN / LOAD-BEARING}}
\]

## 6. Non-redundancy gate

The candidate is not automatically redundant merely because it is Fox-derived.

The project gate permits a Fox-derived carrier provided:

1. the finite object is intrinsic;
2. it is a genuine finite functor of the declared input;
3. it has a direct natural bridge to \(\chi\);
4. the bridge is not merely the known q/classification formula;
5. it carries information not already equivalent to the closed \(C_k\) selector.

The present audit has established only item 1 at the completed/projective level.

Therefore:

\[
\boxed{\text{NON-REDUNDANCY = OPEN}}
\]

## 7. Literature boundary

The literature supports the background ingredients but not the project's new finite factorization theorem.

Labute's classification gives the canonical orientation as an intrinsic invariant of a Demushkin group. Modern expositions also record the one-relator presentation and the canonical orientation. citeturn0search0turn0search7

Completed Fox calculus and relation-module machinery are standard in pro-p group theory, while the Zassenhaus filtration is tied to the completed \(\mathbf F_p[[G]]\) augmentation filtration. citeturn1search1turn2search0

Nothing in these sources supplies the required new theorem that a finite mixed \((3,I)\)-adic Fox quotient factors through the project's specific finite Zassenhaus pair.

## 8. Decision

The mixed candidate is **not closed**.

Its precise status is:

- object definition: **PASS / LOCAL**;
- projective relator-gauge invariance: **PASS / LOCAL**;
- Nielsen covariance of the completed construction: **PASS / LOCAL**;
- preservation of \(\mathfrak m=(3,I)\): **PASS / LOCAL**;
- finite-level intrinsicity: **CONDITIONAL / OPEN**;
- factorization through \(W_k\): **OPEN / LOAD-BEARING**;
- direct orientation bridge: **OPEN / LOAD-BEARING**;
- non-redundancy against \(C_k\): **OPEN**;
- numerical scan: **NOT AUTHORIZED**.

## 9. Next attack

The next and only authorized target is the finite-pair factorization theorem.

Either:

\[
W_k\Longrightarrow A_F/\mathfrak m^{n(k)}
\]

is proved naturally, in which case the bridge attack proceeds,

or a pair of admissible inputs with the same \(W_k\) but different mixed finite Fox data is constructed, in which case the mixed branch is **FAIL / CLOSED**.

Only after that decision may the orientation bridge be tested.

## 10. Stop rule

A hard time boundary is now part of the research protocol:

> **If intrinsicity of a genuinely new finite carrier cannot be established within two weeks of this branch opening, the branch is CLOSED.**

For the present mixed candidate, the completed/projective intrinsicity gate has passed locally; the two-week clock therefore applies to establishing the finite-level intrinsic carrier and its natural factorization, not to endlessly refining the completed Fox scheme.

No broad numerical scan, representation scan, or revival of closed Bockstein/cup-line branches is permitted before the gate is resolved.
