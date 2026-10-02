# POST-PAPER-3 EXPLORATION — EXTERNAL VERIFICATION LEDGER
## 2026-10-02

### Purpose

This document reconstructs the post-Paper-3 carrier exploration as an externally auditable chain of definitions, equations, counterexamples, literature controls, and logical boundaries.

The earlier status-only summaries ("PASS/CLOSED", "FROZEN/COMPLETE") were insufficiently evidentiary for external review. This ledger therefore separates:

1. what is proved directly in the project;
2. what follows from a standard categorical property;
3. what is supported by external literature;
4. what was independently checked;
5. what remains only a claim or conditional inference.

It is a verification ledger, not a replacement for the individual branch audits.

---

# 1. Scope and research question

Paper 3 is frozen as the completed finite-window recognition program.

The post-Paper-3 question is:

\[
\boxed{
W_k(G)
\longrightarrow
\mathcal O_k(G)
\longrightarrow
\chi_G\pmod {p^k}
}
\]

Can one find a finite carrier \(\mathcal O_k\) which is:

- determined by the declared finite filtered input;
- intrinsic/presentation-independent;
- gauge-independent;
- q-blind in its definition;
- naturally connected to the orientation;
- separating;
- and genuinely new rather than a repackaging of the already-established selector?

The active program is therefore **carrier discovery**, not reproof of Papers 1–3.

The standing decision order is:

\[
\text{Object}
\to
\text{Input}
\to
\text{Functoriality}
\to
\text{Gauge}
\to
\text{Orientation bridge}
\to
\text{q-blindness}
\to
\text{Separation}
\to
\text{Novelty}
\to
\text{Stop}.
\]

No large computation is authorized before the structural gates pass.

---

# 2. Candidate 1: the transgression quotient \(\mathcal O_k\)

## 2.1 Definition

For the relevant finite extension window

\[
1\to K_k\to E_k\to Q_k\to1
\]

with transgression

\[
\operatorname{tra}_k:H^1(K_k,\mathbf F_p)^{Q_k}
\to H^2(Q_k,\mathbf F_p),
\]

define

\[
\boxed{
\mathcal O_k
=
H^2(Q_k,\mathbf F_p)/
\operatorname{im}(\operatorname{tra}_k).
}
\]

Let

\[
\pi_k:H^2(Q_k,\mathbf F_p)\twoheadrightarrow\mathcal O_k
\]

be the quotient map.

The D2 work used the transgression quotient as a finite obstruction carrier: the finite transient sector is removed, while false candidates have obstruction witnesses surviving in the quotient.

This underlying carrier remains a valid finite obstruction object.

---

## 2.2 The part that is genuinely tautological

Suppose a proposed linear finite-pair carrier is

\[
(C,\omega_C)
\]

with

\[
\omega_C:H^2(Q_k,\mathbf F_p)\to C
\]

and

\[
\omega_C\circ\operatorname{tra}_k=0.
\]

Then the universal property of the quotient gives a unique map

\[
u_C:\mathcal O_k\to C
\]

such that

\[
\boxed{
\omega_C=u_C\circ\pi_k.
}
\]

This is not a new theorem about Demuškin groups. It is exactly the ordinary factorization property of a quotient/cokernel.

Thus the statement

\[
\mathcal O_k\to C
\]

is universal **inside the category whose objects are already defined by maps out of \(H^2(Q_k)\) annihilating the transgression sector**.

That is a valid categorical fact, but it cannot establish a new mathematical minimality theorem.

### Verification status

- quotient construction: **PASS/CLOSED**;
- factorization \(\mathcal O_k\to C\): **PASS/CLOSED**;
- mathematical content beyond the quotient definition: **NONE / TAUTOLOGICAL**.

This is a proof by the universal property of a quotient, not a numerical computation.

---

## 2.3 Why the opposite universal property fails

The stronger desired statement was:

\[
\boxed{
\text{every admissible separating carrier }C
\text{ admits a unique natural map }
C\to\mathcal O_k.
}
\]

That is a different categorical assertion.

Take

\[
C=\mathcal O_k\oplus\mathcal O_k
\]

with obstruction map

\[
\omega_C(\alpha)
=
(\pi_k(\alpha),\pi_k(\alpha)).
\]

Then \(C\) is still:

- finite-dimensional;
- linear;
- natural if \(\mathcal O_k\) is;
- annihilating \(\operatorname{im}(\operatorname{tra}_k)\);
- separating whenever \(\mathcal O_k\) separates.

But there are two distinct natural projections

\[
s_1,s_2:C\to\mathcal O_k,
\]

\[
s_1(u,v)=u,
\qquad
s_2(u,v)=v.
\]

For any nonzero \(\mathcal O_k\),

\[
s_1\ne s_2.
\]

Therefore a terminal-style universal property with **uniqueness** is false in any admissible carrier category containing this direct-sum construction.

### What this proves

\[
\boxed{
\text{universal }C\to\mathcal O_k\text{ with uniqueness}
=
\text{FAIL/CLOSED}.
}
\]

### What it does not prove

It does **not** prove that no particular carrier admits a map

\[
C\to\mathcal O_k.
\]

It only kills the universal uniqueness claim.

Therefore the earlier phrase "O_k is tautological" must be stated precisely:

> The \(\mathcal O_k\to C\) universal property is tautological; the proposed terminal \(C\to\mathcal O_k\) property is false with uniqueness, while general existence remains unproved.

### Verification strength

This is an explicit categorical counterexample, not a status assertion and not a computer experiment.

---

# 3. Candidate 2: Mixed \((3,I)\)-adic Fox carrier

## 3.1 Candidate object

For a free pro-3 presentation \(F\twoheadrightarrow G\), consider the completed group algebra

\[
A_F=\mathbf Z_3[[F]]
\]

with mixed maximal ideal

\[
\mathfrak m=(3,I_F),
\]

where \(I_F\) is generated by \(x_i-1\).

The candidate is **not** a raw coefficient vector. The intended object is a projective/stable Fox relation-module jet, truncated modulo a power of \(\mathfrak m\):

\[
\boxed{
\mathcal M^{\mathrm{mix}}_k
=
[\text{Fox/Lyndon relation-module jet}]
\bmod \mathfrak m^{n(k)}.
}
\]

The projectivization is essential because the relation generator and presentation choices introduce unit/gauge factors.

---

# 4. Explicit intrinsicity calculations for Mixed Fox

The previous status-only description is too weak. The following identities are the actual reason the local intrinsicity claim is plausible.

## 4.1 Crossed derivation and relator conjugation

For a crossed derivation

\[
D(ab)=D(a)+\chi(a)D(b),
\]

one has

\[
D(g^{-1})=-\chi(g)^{-1}D(g).
\]

Let

\[
r'=grg^{-1}.
\]

Then

\[
\begin{aligned}
D(r')
&=D(g)+\chi(g)D(r)+\chi(gr)D(g^{-1})\\
&=D(g)+\chi(g)D(r)
-\chi(gr)\chi(g)^{-1}D(g)\\
&=D(g)+\chi(g)D(r)-\chi(r)D(g).
\end{aligned}
\]

Since a relator satisfies \(\chi(r)=1\),

\[
\boxed{
D(grg^{-1})=\chi(g)D(r).
}
\]

Thus conjugating the relator multiplies the Fox/crossed-derivation row by a unit. Its projective class is unchanged.

This is the concrete calculation behind the "relator conjugation is gauge" statement.

---

## 4.2 Fox/Lyndon differential

For a minimal pro-p presentation

\[
1\to R\to F\to E\to1
\]

with generators \(x_1,\ldots,x_d\), the relation module is represented by the Fox differential

\[
\partial:
\Lambda_E^d\to\Lambda_E,
\qquad
e_i\mapsto x_i-1,
\]

and the relation generator maps by its Fox derivatives

\[
r\longmapsto
\left(
\frac{\partial r}{\partial x_1},
\ldots,
\frac{\partial r}{\partial x_d}
\right).
\]

The exact relation-module mechanism is standard pro-p Fox/Lyndon theory; Mel'nikov gives the corresponding exact sequence and Fox-derivative description. The project uses this standard mechanism, but the finite mixed truncation and its descent are project-specific. 

---

## 4.3 Nielsen change

If \(\phi:F\to F\) is a free-basis automorphism, Fox's chain rule gives a Jacobian transformation of the derivative row.

Schematically,

\[
J(r\circ\phi)
=
J(r)\,J(\phi).
\]

For a Nielsen automorphism, \(J(\phi)\) is invertible.

Writing

\[
U_i=x_i-1,
\]

a free-basis change sends each \(U_i\) to a formal series with zero constant term and invertible linear part. Hence

\[
\phi(\mathfrak m)=\mathfrak m.
\]

Therefore the truncated algebra

\[
A_F/\mathfrak m^n
\]

is carried isomorphically to the corresponding truncated algebra after a Nielsen change.

After projectivization, the invertible Jacobian does not alter the intrinsic projective relation object.

This is a structural covariance statement, not a numerical observation.

---

## 4.4 Relation-generator gauge

Replacing a generator of a cyclic relation module by a unit multiple

\[
r\mapsto ur,
\qquad
u\in A_F^\times,
\]

changes the relation row by an invertible factor. Projectivization removes this factor.

Hence the object is not tied to a chosen generator of the relation module.

---

# 5. Literature verification of the Fox mechanism

The external literature supports the ingredients but not the project's new finite-pair theorem.

Mel'nikov's pro-p relation-module exact sequence explicitly identifies the relation module with the kernel of the Fox differential and gives the Fox derivative map. citeturn0search14turn0search2

The completed group algebra/Magnus-Fox framework is also standard: the Zassenhaus filtration is naturally tied to the augmentation filtration of \(\mathbf F_p[[G]]\), while the project's mixed algebra is over \(\mathbf Z_3[[G]]\) with the additional p-adic direction. Mináč–Rogelstad–Tân explicitly formulate the completed \(\mathbf F_p[[G]]\) augmentation filtration and its relation to Zassenhaus graded pieces. citeturn2view0

Therefore the literature establishes:

\[
\text{Fox/Lyndon mechanism} = \text{standard},
\]

but does **not** establish

\[
W_k
\Longrightarrow
\mathcal M_k^{\mathrm{mix}}.
\]

That latter implication is the project-specific theorem.

---

# 6. The extension-window problem

The intended finite input was initially written as

\[
(Q_k,A_k).
\]

But

\[
A_k=D_N/D_{N+1}
\]

is not a subgroup of

\[
Q_k=G/D_N.
\]

The actual finite extension is

\[
\boxed{
1\to A_k\to E_k\to Q_k\to1,
}
\]

where

\[
E_k=G/D_{N+1}.
\]

Thus the Mixed Fox construction naturally sees the extension window, not merely the two abstract groups separately.

---

# 7. Explicit broad-category no-go: same \((Q,A)\), different extensions

This is not merely an appeal to the phrase "H^2 classifies extensions". There is a concrete example.

Take

\[
Q=C_3\times C_3,
\qquad
A=C_3.
\]

### Extension 1: abelian/power type

Let

\[
E_1=C_9\times C_3,
\]

with

\[
A=\langle x^3\rangle\cong C_3.
\]

Then

\[
E_1/A\cong C_3\times C_3.
\]

The extension has a nontrivial power/Bockstein component.

### Extension 2: Heisenberg/exponent-3 type

Let

\[
E_2=
\langle x,y,z
\mid
z^3=1, [z,x]=[z,y]=1, x^3=y^3=1, [x,y]=z
\rangle.
\]

Then

\[
A=\langle z\rangle\cong C_3,
\qquad
E_2/A\cong C_3\times C_3.
\]

Here the extension class is carried by the commutator component.

Thus the same forgotten pair

\[
(Q,A)
\]

supports non-isomorphic extensions.

Consequently

\[
\boxed{
(Q,A)\not\Rightarrow E
}
\]

in the broad category of finite central 3-extensions.

This closes only the **broad-category** descent claim.

It does not yet say anything negative about the restricted Demuškin family.

---

# 8. Demuškin-restricted reconstruction

For odd p and fixed finite rank d, the standard Demuškin relator has the form

\[
\boxed{
r=x_1^q[x_1,x_2][x_3,x_4]\cdots[x_{d-1},x_d],
}
\]

with

\[
q\in\{p,p^2,p^3,\ldots\}\cup\{0\}.
\]

This classification is classical; Labute's classification gives the standard normal form and identifies q as a power of p (with the usual q=0 convention). citeturn1search25turn1search23

For

\[
N_k=p^{k-1}+1,
\]

there are only two genuine q-ranges.

### Case A: \(q<N_k\)

Then q is a p-power below the target depth. The q-power term enters the relator at Zassenhaus degree q, before the boundary layer.

Therefore the intrinsic sequence

\[
d_j(G)=
\dim_{\mathbf F_p}D_j/D_{j+1},
\qquad j<N_k,
\]

contains the first q-dependent defect.

The Mináč–Rogelstad–Tân formulas explicitly compute the Zassenhaus graded dimensions for Demuškin groups. citeturn2view0

Thus, at the declared standard-family scope,

\[
Q_k\Rightarrow q
\qquad(q<N_k).
\]

### Case B: \(q>N_k\)

The q-power term begins after the target window. Hence through the required truncation the standard presentations have the same q-dependent part: the q-term is invisible.

Thus

\[
q,q'>N_k
\quad\Longrightarrow\quad
E_k(q)\cong E_k(q')
\]

at the truncated-window level.

### Crucial correction

The previously used case

\[
q=N_k
\]

must be removed.

Indeed,

\[
N_k=p^{k-1}+1
\]

is not a p-power, while standard odd-p Demuškin q is a p-power or 0.

Therefore the previous "q=N boundary-layer dimension" argument was not a valid branch. It was superseded by the corrected two-range argument.

This correction is important evidence that the exploration is being audited rather than merely accumulated as PASS labels.

---

# 9. What the Demuškin reconstruction actually proves

The strongest defensible statement is:

\[
\boxed{
(Q_k,A_k)
\Longrightarrow
[E_k\to Q_k]
}
\]

up to extension-window isomorphism **within the declared standard odd-p fixed-rank Demuškin family**.

This is not the same as:

\[
\text{all finite pairs determine all extensions}.
\]

The latter is false by the explicit C9×C3/Heisenberg counterexample.

Nor is it yet a fully formal functor

\[
\mathbf{Pair}_k\to\mathbf{ExtWin}_k
\]

for arbitrary non-invertible pair morphisms.

The proven/usable level is the isomorphism-class statement:

\[
W_k(G)\cong W_k(H)
\Longrightarrow
\mathsf W_k^{ext}(G)
\cong
\mathsf W_k^{ext}(H).
\]

---

# 10. Mixed Fox finite-pair descent

Combining the preceding steps gives the actual chain investigated:

\[
G
\longmapsto
W_k(G)
\longmapsto
\mathsf W_k^{ext}(G)
\longmapsto
[\mathcal M_k^{\mathrm{mix}}(G)].
\]

The first arrow is the canonical Zassenhaus window.

The second is the Demuškin-restricted reconstruction above.

The third uses the Fox/Lyndon relation-module construction, mixed maximal-ideal truncation, and projectivization.

At the isomorphism level this gives:

\[
\boxed{
W_k(G)\cong W_k(H)
\Longrightarrow
[\mathcal M_k^{\mathrm{mix}}(G)]
\cong
[\mathcal M_k^{\mathrm{mix}}(H)].
}
\]

This is enough for intrinsic **isomorphism-class** well-definedness.

It does not establish arbitrary non-invertible functoriality of a formally defined Pair_k category. That stronger statement remains OPEN and is not needed for the basic intrinsicity claim.

---

# 11. The orientation bridge: the critical non-redundancy test

Here the external literature gives an especially important control calculation.

For the standard Demuškin relator, Labute evaluates crossed derivations on the relator and obtains

\[
\theta(x_i)=1
\quad(i\ne2),
\]

and

\[
\boxed{
\theta(x_2)=(1-q)^{-1}.
}
\]

This is an explicit calculation in the literature, not a project discovery. citeturn2view2turn1search23

Therefore the known route is

\[
q
\longrightarrow
(1-q)^{-1}
\longrightarrow
\chi.
\]

If the Mixed Fox carrier is used only to recover q and then this known formula is applied, the result is **classification repackaging**.

That does not make the Mixed Fox construction false.

It means it fails the project's declared novelty test for a new recognition carrier.

---

# 12. Important logical correction to the previous "redundancy" claim

The strongest statement

> "every invariant carrier of the finite window can only contain q information, therefore it is automatically redundant"

would be too strong if interpreted as a general mathematical theorem.

A finite window can carry a rich internal structure even when the underlying Demuškin isomorphism class is classified by q and rank.

The defensible statement is narrower:

> At the declared fixed-rank standard Demuškin scope, if the proposed orientation bridge is obtained only by recovering the existing q-classification and then applying the known formula \(\chi(x_2)=(1-q)^{-1}\), it is not a genuinely new recognition theorem under the project's non-redundancy criterion.

Thus the Mixed Fox branch is closed **as a new recognition carrier**, not because a mathematical no-go theorem proves that no direct Fox-to-χ theorem could ever exist.

This distinction should be retained in all future summaries.

---

# 13. Final evidence ledger

| Claim | Concrete evidence | Independent control | Status |
|---|---|---|---|
| \(\mathcal O_k\) is the quotient obstruction carrier | explicit quotient definition | finite-dimensional cohomology / D2 inputs | PASS/CLOSED |
| \(\mathcal O_k\to C\) factorization | quotient universal property | elementary category theory | PASS/CLOSED, TAUTOLOGICAL |
| unique universal \(C\to\mathcal O_k\) | \(C=\mathcal O_k\oplus\mathcal O_k\), two projections | explicit categorical counterexample | FAIL/CLOSED |
| arbitrary \((Q,A)\Rightarrow E\) | \(C_9\times C_3\) vs Heisenberg extension | explicit group presentations | FAIL/CLOSED |
| Fox relator conjugation invariance | \(D(grg^{-1})=\chi(g)D(r)\) | crossed-derivation identity | PASS/LOCAL |
| relation-module/Fox mechanism | explicit Fox differential | Mel'nikov / Lyndon theory | PASS/LOCAL |
| Nielsen covariance | Fox chain rule + invertible Jacobian | standard Fox calculus | PASS/LOCAL |
| mixed ideal preservation | \(\phi(\mathfrak m)=\mathfrak m\) for free-basis changes | formal power-series/Jacobian argument | PASS/LOCAL |
| Zassenhaus data are intrinsic | \(D_j/D_{j+1}\) | Mináč–Rogelstad–Tân | PASS |
| q is a p-power or 0 | Demuškin classification | Labute | PASS |
| q<N is detected below window | first q-dependent graded defect | classification + Zassenhaus dimensions | PASS/LOCAL |
| q=N_k case | \(N_k=p^{k-1}+1\) not p-power | arithmetic correction | SUPERSEDED/REMOVED |
| q>N collapses at finite precision | q-term lies beyond truncation | standard relator degree argument | PASS/LOCAL |
| pair determines extension window | preceding restricted-family analysis | literature-controlled classification | PASS/CLOSED at isomorphism-class scope |
| pair gives full arbitrary functorial section | not constructed | no lift theorem | OPEN |
| Mixed Fox finite object is intrinsic | extension reconstruction + Fox covariance | standard relation-module machinery | PASS/LOCAL |
| Mixed Fox gives new χ recognition | only known q→χ bridge available | Labute's explicit formula | FAIL/CLOSED as currently constructed |
| Mixed Fox mathematical object is false | no such counterexample | — | NOT CLAIMED |
| genuinely new carrier exists | none found yet | — | OPEN |

---

# 14. What an external referee can reproduce

A referee should be able to check the current exploration without trusting the status labels by following this order:

### A. O_k

1. Write the quotient \(H^2(Q)/\operatorname{im}(\operatorname{tra})\).
2. Apply the quotient universal property to obtain \(\mathcal O_k\to C\).
3. Construct \(C=\mathcal O_k\oplus\mathcal O_k\).
4. Observe the two projections \(C\to\mathcal O_k\).
5. Conclude that terminal uniqueness is false.

### B. Broad extension no-go

1. Fix \(Q=C_3^2\), \(A=C_3\).
2. Write the presentations of \(C_9\times C_3\) and the exponent-3 Heisenberg group.
3. Quotient each by its central C3.
4. Obtain the same \((Q,A)\) but different extension classes.

### C. Mixed Fox

1. Start with \(D(ab)=D(a)+\chi(a)D(b)\).
2. Derive \(D(grg^{-1})=\chi(g)D(r)\).
3. Write the Fox derivative row.
4. Apply the chain rule under Nielsen changes.
5. Observe that the Jacobian is invertible and preserves \((3,U_1,\ldots,U_d)\).
6. Projectivize to remove unit/gauge ambiguity.

### D. Demuškin reconstruction

1. Use the standard relator \(x_1^q[x_1,x_2]\cdots\).
2. Use the intrinsic Zassenhaus degree of the q-power term.
3. For \(q<N_k\), identify q below the window.
4. For \(q>N_k\), observe that the q-term is outside the truncation.
5. Explicitly remove the impossible \(q=N_k\) case.

### E. Novelty

1. Consult the known crossed-derivation computation.
2. Recover
   \[
   \chi(x_2)=(1-q)^{-1}.
   \]
3. Check whether the proposed Mixed Fox bridge contains anything beyond
   \[
   \text{Mixed Fox}\to q\to\chi.
   \]
4. If not, classify the proposed carrier as redundant under the project's declared criterion.

---

# 15. Current research boundary

The correct current state is therefore:

\[
\boxed{
\begin{array}{ll}
\text{Paper 3 itself} & \textbf{FROZEN / COMPLETE},\\
\mathcal O_k\text{ carrier} & \textbf{PASS / CLOSED},\\
\mathcal O_k\text{ universal minimality} & \textbf{FAIL / CLOSED},\\
\text{arbitrary extension descent} & \textbf{FAIL / CLOSED},\\
\text{Demuškin-restricted reconstruction} & \textbf{PASS / CLOSED at isomorphism-class scope},\\
\text{Mixed Fox finite object} & \textbf{PASS / LOCAL},\\
\text{Mixed Fox as new recognition carrier} & \textbf{FAIL / CLOSED — REDUNDANT},\\
\text{genuinely new finite carrier} & \textbf{OPEN}.
\end{array}
}
\]

The key methodological correction is:

> **"PASS/CLOSED" is no longer allowed to mean merely "the argument sounds plausible." Every future closure must point to an explicit equation, counterexample, universal property, independently checkable literature theorem, or reproducible computation.**

---

# 16. Publication separation

The post-Paper-3 generalization search is logically independent of the frozen publication candidates.

A failure of the open carrier program does not invalidate the completed Papers 1–3.

Conversely, a future new carrier result should not be silently inserted into the existing papers without a separate novelty/proof audit.

Therefore the recommended publication discipline is:

\[
\boxed{
\text{freeze/submit completed papers independently}
\quad\parallel\quad
\text{continue carrier research separately}.
}
\]

This separation is now part of the research record.
