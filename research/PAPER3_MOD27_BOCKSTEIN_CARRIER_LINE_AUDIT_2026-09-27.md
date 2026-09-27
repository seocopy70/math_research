# Paper 3 — Candidate B MOD-27 Bockstein-Extension Carrier: Line-by-Line Literature + Mathematical Audit
Date: 2026-09-27
Status: **FAIL / CLOSED as a new orientation carrier; PASS / LOCAL as a finite q-layer detector**
Scope: fixed odd-p Demushkin / Paper 3 filtered-relation input, with the declared non-tautology gate.

## Executive conclusion

The proposed
\[
\mathcal B_{27}(G)=
(H^1(G,\mathbf F_3),H^1(G,\mathbf Z/9),\mathrm{red},\iota,\smile,\beta_1,\beta_9)
\]
does **not** survive as the Paper 3 mod-27 orientation carrier.

The decisive reasons are cumulative:

1. The construction is mathematically well-defined and functorial.
2. Its trivial-coefficient Bockstein layers reproduce finite 3-adic torsion/q-information, but this is already adjacent to established Demushkin/Kummer/Bockstein theory.
3. On the standard rank-four family, the full structured carrier has been explicitly classified into the three valuation classes \(v_3(q)=1,2,\ge3\).
4. Earlier internal-symmetry objections were correctly downgraded because abstract carrier automorphisms were not shown to be group-realizable.
5. Nevertheless, after the full structured-family classification, the carrier has supplied no genuinely independent orientation-sensitive datum beyond the same finite q/classification partition.
6. The literature independently shows that Demushkin orientation is characterized through canonical dualizing/Kummerian structure and that Bockstein data can be used to construct characteristic level subgroups. In particular, Simons (1989) explicitly describes construction of level subgroups from a Bockstein operator on \(H^1(X,\mathbf Z/q)\), while Efrat–Quadrelli and later work characterize the canonical Kummerian orientation.
7. Therefore the present \(\mathcal B_{27}\to\chi\bmod27\) bridge would either be a classification/q-layer repackaging or require genuinely new rigidifying data not contained in the declared carrier.

The correct surviving result is:
\[
\boxed{\mathcal B_{27}\text{ is a finite q-layer detector, not a new orientation carrier.}}
\]

---

# Part I — Exact object audit

## Line 1: definition

Claim:
\[
\mathcal B_{27}
=
(H^1(G,\mathbf F_3),H^1(G,\mathbf Z/9),\mathrm{red},\iota,\smile,\beta_1,\beta_9).
\]

### Mathematical check
PASS.

For trivial coefficients:
- \(H^1(G,A)=\operatorname{Hom}_{\mathrm{cont}}(G,A)\) for finite abelian A;
- \(\mathrm{red}\) is induced by \(\mathbf Z/9\twoheadrightarrow\mathbf F_3\);
- \(\iota\) is induced by multiplication by 3;
- \(\beta_1\) is the connecting map for
  \[
  0\to\mathbf F_3\to\mathbf Z/9\to\mathbf F_3\to0;
  \]
- \(\beta_9\) is the connecting map for
  \[
  0\to\mathbf F_3\to\mathbf Z/27\to\mathbf Z/9\to0.
  \]

These are functorial under continuous group homomorphisms.

### Audit status
**PASS / CLOSED.**

---

# Part II — Exact frozen-family calculation

For
\[
G_q=\langle x_1,x_2,x_3,x_4\mid x_1^q[x_1,x_2][x_3,x_4]\rangle,
\qquad q=3^s,
\]
with A=Z/9,
\[
H^1(G_q,A)=\{(a_1,a_2,a_3,a_4)\in A^4:q a_1=0\}.
\]

Hence
\[
H^1(G_q,\mathbf Z/9)
=
\begin{cases}
3A\times A^3,&s=1,\\
A^4,&s\ge2.
\end{cases}
\]

The previously audited connecting-map calculation gives the normal forms
\[
\beta_1(f)=\frac q3f(x_1)\,\omega,
\]
and the mod-27 coefficient extension detects the next q-layer through \(\beta_9\), with the relation-imposed divisibility understood.

Thus the three classes are:
\[
v_3(q)=1:\ \beta_1\ne0,
\]
\[
v_3(q)=2:\ \beta_1=0,\ \overline\beta_9\ne0,
\]
\[
v_3(q)\ge3:\ \beta_1=0,\ \overline\beta_9=0.
\]

The compatibility
\[
\beta_9\circ\iota=\beta_1
\]
is PASS.

### Audit status
**PASS / CLOSED on the standard family.**

No further same-family Bockstein scan is authorized.

---

# Part III — Full structured-carrier classification

The earlier project record correctly identified a logical gap: Bockstein ranks alone did not classify the whole structured carrier.

That gap was subsequently repaired.

For the standard family, the full structured object
\[
(H^1(\mathbf F_3),H^1(\mathbf Z/9),\mathrm{red},\iota,\smile,\beta_1,\beta_9)
\]
has explicit structure-preserving normal forms depending only on
\[
\nu_{27}(q)=1,2,\ge3.
\]

Therefore:
\[
\boxed{
\mathcal B_{27}(G_q)\cong\mathcal C_{\nu_{27}(q)}
}
\]
on this family.

Important qualification: this is a family theorem, not a universal theorem for every admissible filtered/relation object.

### Audit status
**PASS / CLOSED (standard family).**

---

# Part IV — Non-tautology test

The project gate excludes a carrier whose successful orientation reconstruction is merely

\[
\mathcal B_{27}
\to
v_3(q)\text{-class}
\to
q\text{-classification}
\to
\chi.
\]

This matters because Demushkin classification already says that rank together with the appropriate torsion/orientation invariant determines the group, and the canonical orientation is intrinsic.

The current carrier has exhibited no independent datum that survives after fixing the q-valuation class and nevertheless distinguishes a mod-27 orientation lift.

The strongest surviving statement is therefore:

> On the standard family, the carrier is extensionally a finite q-layer detector. The project has not established a presentation-free universal obstruction identity from this carrier to the logarithmic orientation digit.

### Audit status
**FAIL / CLOSED as a new non-tautological orientation carrier.**

This is deliberately narrower than the superseded unconditional “abstract symmetry proves no-go” claim.

---

# Part V — Internal symmetry audit: correction preserved

An earlier Hard Attack 18 proposed an abstract carrier automorphism
\[
S(a_1,a_2,a_3,a_4)=(a_1,4a_2,a_3,a_4)
\]
as an absolute no-go.

That was correctly downgraded in Hard Attack 19: S was shown to preserve the abstract carrier structure, but it was not proved to arise from an admissible group automorphism/gauge morphism.

Therefore:

- abstract carrier symmetry S: **PASS / LOCAL**;
- “S proves absolute no-go”: **HISTORICAL / SUPERSEDED**;
- present closure does **not** depend on S being group-realizable.

This distinction is binding.

---

# Part VI — Literature audit

## L1. Demushkin classification / orientation

Modern sources restate the classical fact that an infinite Demushkin group has a canonical orientation character and that rank together with the orientation image determines the group.

A recent 2024 account states explicitly that the canonical orientation \(\chi:G\to1+p\mathbf Z_p\) is uniquely characterized by the 1-cyclotomic/Kummerian property, and gives the standard presentation
\[
G=\langle x_1,\ldots,x_d\mid
x_1^{p^f}[x_1,x_2]\cdots[x_{d-1},x_d]\rangle
\]
with
\[
\chi(x_2)=(1-p^f)^{-1}.
\]
This confirms that the orientation/q relationship used in the project's standard-family audit is classical, not a new bridge.

Source: Quadrelli-related 1-cyclotomicity literature and the 2024 survey/article. citeturn3search1turn2search2

**Status: PRIOR ART / CLOSED as novelty.**

## L2. Efrat–Quadrelli: Kummerian characterization

Efrat–Quadrelli define Kummerian cyclotomic pro-p pairs by surjectivity of coefficient-lift maps
\[
H^1(G,\mathbf Z_p(1)/p^n)
\to
H^1(G,\mathbf Z_p(1)/p)
\]
for all n, and prove a group-theoretic characterization for torsion-free pairs. Their Demushkin discussion identifies the unique canonical orientation completing a torsion-free Demushkin group to a Kummerian pair.

This is important because it shows that coefficient-lifting towers are already a standard language for the canonical orientation. A trivial-coefficient tower \(H^1(G,\mathbf Z/p^n)\) therefore needs a very strong independent obstruction claim before it can be presented as a new orientation carrier.

Source: Efrat–Quadrelli, *The Kummerian Property and Maximal Pro-p Galois Groups*. citeturn1search0turn1search1

**Status: PRIOR ART / CLOSED as novelty boundary.**

## L3. Simons 1989: Bockstein construction of characteristic level subgroups

This is the most direct prior-art hit for Candidate B.

Simons' *Z_p-Towers in Demushkin Groups* explicitly states that level subgroups of the basic \(\mathbf Z_p\)-tower can be constructed without directly invoking the dualizing module by using a Bockstein operator
\[
B:H^1(X,\mathbf Z/q\mathbf Z)
\to H^2(X,\mathbf Z/q\mathbf Z)
\]
coming from
\[
0\to\mathbf Z/q\mathbf Z
\to\mathbf Z/q^2\mathbf Z
\to\mathbf Z/q\mathbf Z
\to0.
\]
The kernel of this Bockstein has codimension one, and its cup-orthogonal complement supplies the relevant level character; the resulting kernel is the characteristic level subgroup. citeturn4view0

This is materially overlapping with the conceptual claim that finite coefficient-extension/Bockstein data can recover finite layers of the canonical Demushkin tower.

It does **not** by itself prove that the exact \(\mathcal B_{27}\) object is identical to Simons' construction, so the correct conclusion is overlap/antecedent, not identity.

**Status: STRONG PRIOR-ART OVERLAP / CLOSED as a novelty claim.**

## L4. Bockstein and presentation-level cohomology

Efrat–Quadrelli explicitly use the Bockstein associated to
\[
0\to\mathbf Z/p\to\mathbf Z/p^2\to\mathbf Z/p\to0
\]
and relate it to defining-relation coefficients in Demushkin/one-relator computations. This confirms that the mod-p Bockstein is classical relation/cohomology data in precisely the relevant setting. citeturn1search1

**Status: PRIOR ART / CLOSED.**

## L5. Higher Bockstein/generalized Bockstein literature

Generalized Bockstein maps for profinite groups and their relation to higher cohomological structure/Massey products are already developed in the literature. The existence of a higher Bockstein layer is therefore not itself novel. citeturn2search0turn2academia6

Likewise, recent work on Bockstein spectral sequences treats the entire tower of Bockstein differentials functorially. citeturn2search1

**Status: PRIOR ART / CLOSED as novelty of “higher Bockstein package” alone.**

## L6. Pál–Quick 2026

Pál–Quick's 2026 work proves an \(A_3\)-formality distinction for odd-prime Demushkin groups: q-invariant 3 versus q-invariant not equal to 3. This is not the same invariant as \(\mathcal B_{27}\), but it reinforces that finite cohomological structures can detect q-specific information and that q=3 is already a recognized cohomological boundary.

Source: Pál–Quick, *A_3-formality for Demushkin groups at odd primes*. citeturn0academia4

**Status: ADJACENT PRIOR ART / no direct identity established.**

## L7. Blumer–Quadrelli 2026

The 2026 Blumer–Quadrelli paper studies whether Demushkin-type groups admit a 1-cyclotomic orientation and constructs families that do not. This is directly relevant to any proposed finite orientation criterion: the orientation property is already an active structural object, so a new finite carrier must be distinguished from merely restating 1-cyclotomic/Kummerianity.

Source: *Variations of Demushkin Groups that are not Absolute Galois Groups*. citeturn5academia2

**Status: ADJACENT PRIOR ART / novelty gate remains stringent.**

## L8. Palaisti 2026

Palaisti's 2026 work concerns higher Massey products in Demushkin variations and explicitly tracks support/projective directions and the persistence of the power term \(x_1^q\). It is not a direct prior-art match for \(\mathcal B_{27}\), but it is relevant to the project's broader finite-layer strategy and should not be confused with a new orientation carrier.

Source: *Higher Massey Products in Demuškin Variations...*. citeturn5academia1

**Status: ADJACENT / no direct identity.**

---

# Part VII — Candidate-B gate, line by line

| Gate | Result | Reason |
|---|---|---|
| Exact object exists | PASS | finite cohomology + connecting maps |
| Functoriality | PASS | cohomological naturality |
| q not supplied in definition | PASS | definition uses coefficients only |
| Standard-family computation | PASS | exact relation/Bockstein calculation |
| Full structured carrier classified on test family | PASS | explicit normal forms |
| Detects q=3 vs 9 vs >=27 | PASS / LOCAL | finite q-layer detector |
| Strictly beyond ordinary mod-9 Bockstein | PASS / LOCAL | detects 9 vs >=27 |
| Independent of known q/classification route | FAIL | no independent bridge established |
| New orientation-sensitive rigidifier inside carrier | FAIL | none exhibited |
| Prior art absent | FAIL | strong overlap with Bockstein/Kummerian level constructions |
| Universal orientation bridge | FAIL | not proved |
| Carrier suitable as Paper 3 load-bearing novelty | **FAIL / CLOSED** | fails non-tautology + novelty gate |

---

# Part VIII — Important distinction: what survives

The closure is **not** “Bockstein is useless.”

The following survive:

\[
\boxed{
\mathcal B_{27}
\text{ is a natural finite coefficient-extension detector of the first three q-layers.}
}
\]

In particular, it demonstrates a real information boundary:
\[
\text{mod-9 Layer B}
<
\text{mod-27 coefficient-extension/q-layer detector}.
\]

But the desired stronger statement
\[
\mathcal B_{27}
\Longrightarrow
\chi\pmod{27}
\]
as a genuinely new, presentation-free, non-classification orientation bridge is not established and should not be claimed.

---

# Part IX — Strategic next step

The existing project record already identifies the cleaner next object:

\[
\mathcal R_{27}^{\mathrm{res}}
=
\text{the first higher power/relation residual at }P_4/D_{10},
\]
which distinguishes
\[
q=9
\quad\text{from}\quad
27\mid q
\]
after the mod-9 Layer-B information has been factored out.

That residual is genuinely filtered/relation data and is not merely another trivial-coefficient Bockstein package.

The next authorized audit is therefore:

1. define \(\mathcal R_{27}^{\mathrm{res}}\) intrinsically;
2. define its transport/morphism category;
3. prove its projective direction;
4. prove or disprove the missing scalar normalization;
5. only then compare its factorization depth with the coarser orientation target.

No further \(\beta_1,\beta_9\) scan is authorized.

## Final classification

\[
\boxed{
\begin{array}{ll}
\mathcal B_{27}\text{ as finite q-layer detector} & \textbf{PASS / LOCAL},\\
\mathcal B_{27}\text{ as new mod-27 orientation carrier} & \textbf{FAIL / CLOSED},\\
\text{P}_4\text{ higher-power residual} & \textbf{OPEN / DECISIVE}.
\end{array}}
\]

This audit supersedes the earlier “OPEN / STRONG CANDIDATE” wording for Candidate B.
