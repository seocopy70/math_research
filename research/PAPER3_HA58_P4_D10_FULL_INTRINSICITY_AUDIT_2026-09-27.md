# PAPER 3 — HA58 P4/D10 RESIDUAL FULL INTRINSICITY AUDIT — 2026-09-27

## Scope

This audit reconstructs HA58 and its calculation chain, then audits the proposed mod-27 higher power/relation residual in the required order:

1. definition;
2. coordinate dependence;
3. transport/functoriality;
4. projective direction;
5. scalar normalization.

Only the labels PROVED / COMPUTED / EXTERNAL / COUNTEREXAMPLE / DEFINITION REVISED / OPEN are used for final mathematical classification.

## 1. Exact reconstructed object

Frozen standard family:
\[
G_q=\langle x_1,x_2,x_3,x_4\mid x_1^q[x_1,x_2][x_3,x_4]=1\rangle,
\qquad q=3^s.
\]

HA58 uses the lower-3-central filtration
\[
P_1=G,\qquad P_{n+1}=P_n^3[P_n,G].
\]

The computed HA58 signal is a next power/relation contribution in the finite-depth mod-27 secondary calculation, with the standard-family pattern
\[
q=3:\text{ absorbed by the established Layer-B normalization},
\]
\[
q=9:\text{ nonzero new residual},
\]
\[
27\mid q:\text{ zero new residual}.
\]

Independent repository calculations verify that the degree-3 q=9 difference is zero and that the first q=9 power contribution occurs at degree 9 in the Magnus/p-Zassenhaus calculation. The later mod-27 crossed-word calculations verify the surviving /9 secondary source in the frozen q=3/q=9 branches.

## 2. Gate 1 — intrinsic definition

HA58's phrase “next power/relation class in P_3/P_4” is not yet a mathematical definition.

What is missing:

- a typed map whose image/kernel defines the residual;
- an exact quotient removing the already-known Layer-B information;
- an explicit subquotient of P_3/P_4 or of the relevant restricted graded object;
- a canonical map from the intrinsic torsion line to that residual.

The standard-family residual is therefore a real computed object, but the general presentation-free object is not defined.

**Decision: OPEN.**

## 3. Gate 2 — coordinate dependence

The filtration P_\bullet is characteristic and its associated power/commutator operations are functorial. This part is PROVED.

However, the HA58 residual is represented in normal-form coordinates by restricted power classes such as X_1^{[3]}. No theorem in the audited chain identifies the selected residual element/subspace independently of relation presentation and relator gauge.

The later HA61 conjugation audit gives a decisive obstruction to the naive single-vector compression: for a relation change r -> v r v^{-1}, the isolated residual transforms by a nontrivial [v,R] term, and in the frozen q=3 case this changes the putative t_2 by p for suitable v.

Thus the raw vector is not presentation-independent.

**Decision: COUNTEREXAMPLE for a single canonical vector; OPEN for a richer intrinsic carrier.**

## 4. Gate 3 — transport/functoriality

Functoriality of the lower-3-central filtration itself is PROVED.

Functoriality of the proposed residual is not established because the residual was never defined as a functorial subquotient/map.

The intrinsic object that survives the HA61 attack is instead the full connecting-obstruction family
\[
\rho_3\longmapsto\delta_{3,\rho_3},
\]
which is intrinsic under the audited relation/lift changes.

The attempted compression
\[
\{\delta_{3,\rho_3}\}\rightsquigarrow t_2
\]
does not descend to a single natural vector.

**Decision: OPEN for a richer carrier; COUNTEREXAMPLE to the single-vector transport claim.**

## 5. Gate 4 — projective direction

On the standard family, the residual direction is computationally visible and separates q=9 from 27|q.

The intrinsic torsion line itself is genuinely intrinsic in the audited q=3 rank-4 group: Tor(G^ab) is characteristic and its Frattini image is a canonical one-dimensional line. The intrinsic automorphism character on that line is also PROVED in the frozen category.

But no canonical natural map from that torsion line to the HA58 residual projective line has been established.

Moreover, HA61-B5-12 shows that the natural secondary object cannot be compressed to a single vector t_2. Quotienting t_2 by the shift line also fails because the secondary scalar contains f(t_2) while the primary-zero relation does not force f(p)=0.

**Decision: COMPUTED for the standard-family direction; OPEN as a canonical projective invariant.**

## 6. Gate 5 — scalar normalization

The frozen standard-family mod-27 calculation produces a definite scalar after division by 9; in the q=9 branch the unique zero occurs at the corresponding extension parameter value. This is COMPUTED.

That does not establish a category-independent canonical scalar normalization.

The stronger proposed route “choose a canonical vector t_2 and normalize it to the second 3-adic orientation digit” is blocked by the explicit relation-conjugation counterexample.

The coker/obstruction analysis shows the correct conceptual requirement: a scalar, if recoverable, must arise from compatibility of the higher connecting obstruction with the already normalized mod-9 obstruction, not from inserting the known q/orientation formula.

That compatibility has not been proved.

**Decision: OPEN.**

## 7. Finite-depth source audit

At the D_4 / mod-27 secondary depth, the source ledger is now sharply classified.

After division by 9 modulo 3:

1. F^9 power terms survive and give the genuinely new power source;
2. gamma_2^3 terms survive but belong to the already-known first-stage (lambda wedge f) sector;
3. gamma_3^3 and gamma_4 contributions vanish at this finite depth.

Therefore the earlier blanket claim “all D_4 errors vanish” is false, but the surviving finite source list is exhausted.

**Decision: PROVED for the finite-depth valuation classification as a finite statement; COMPUTED for the frozen explicit branches.**

The remaining issue is not hidden higher terms. It is whether the surviving F^9 functional admits a natural compression compatible with the full prefix/suffix and gauge ledger.

## 8. Decisive no-go result

HA61-B5-12 provides an explicit same-abstract-group / different-relation-coordinate witness.

For suitable relation conjugation r -> v r v^{-1},
\[
t_2\mapsto t_2+p
\]
when lambda(v)=1, while the intrinsic connecting-obstruction family remains unchanged.

Hence the following proposition is false:

> There exists a canonical presentation-independent vector t_2 whose evaluation, together with the fixed first-stage term, gives the full secondary connecting obstruction.

**Decision: COUNTEREXAMPLE.**

The two obvious finite repairs are also closed:

- t_2 modulo <p>: insufficient because f(t_2) does not descend while f(p) need not vanish on the primary-zero locus;
- diagonal (t_2,mu) quotient: already fails because it identifies distinct coefficient actions.

Thus the single-vector P_4 realization is not merely unproved; it is structurally ruled out.

## 9. Literature audit

Primary/secondary literature checks establish:

- canonical Demuškin orientation and its dualizing-module origin: EXTERNAL;
- Zassenhaus filtration, initial-form, and graded Demuškin framework: EXTERNAL;
- standard Demuškin quadratic relation/mildness framework: EXTERNAL;
- existing literature on orientation/Kummerian/1-cyclotomic coefficient lifting: EXTERNAL;
- existing literature showing that some Zassenhaus-only constructions can lose orientation information: EXTERNAL, with scope requiring care.

The literature does not, on the material audited here, supply the specific HA58 residual as an already-established intrinsic orientation invariant.

No novelty claim is made for the residual itself until a dedicated primary-source search proves equivalence or non-equivalence.

## 10. Final classification table

| Object/claim | Final label |
|---|---|
| lower-3-central filtration definition | PROVED |
| q=9 standard-family residual existence | COMPUTED |
| q=9 vs 27|q detection pattern | COMPUTED |
| degree-3 q=9 difference = 0 | COMPUTED |
| finite D_4 source classification at mod 27 | PROVED / COMPUTED |
| single presentation-independent residual vector | COUNTEREXAMPLE |
| intrinsic residual definition as HA58 intended | OPEN |
| residual transport/functoriality | OPEN |
| standard-family projective direction | COMPUTED |
| canonical projective map from torsion line | OPEN |
| frozen scalar normalization | COMPUTED |
| canonical scalar normalization | OPEN |
| intrinsic single-vector t_2 route | COUNTEREXAMPLE |
| intrinsic connecting-obstruction family delta_3 | PROVED |
| richer secondary carrier beyond t_2 | OPEN |
| literature background on orientation/Zassenhaus | EXTERNAL |

## 11. Strategic conclusion

HA58's central computational observation survives:
\[
q=9
\]
really produces a new finite-depth mod-27 power source not present for
\[
27\mid q.
\]

But the correct mathematical interpretation is now sharper:
\[
\boxed{
\text{HA58 residual is a COMPUTED standard-family phenomenon, not yet an intrinsic vector invariant.}
}
\]

More strongly,
\[
\boxed{
\text{the proposed single-vector intrinsic }t_2\text{ is ruled out by a presentation-conjugation counterexample.}
}
\]

The surviving intrinsic object is the richer function-valued connecting family
\[
\boxed{
\rho_3\longmapsto\delta_{3,\rho_3}.
}
\]

The next research question is therefore no longer “how do we define t_2?” but:
\[
\boxed{
\text{Can the intrinsic secondary obstruction family itself be compressed to a richer affine/torsor-valued carrier that preserves coefficient-lift dependence?}
}
\]

This is the correct successor to HA58/HA61-B. The single-vector P_4 route must not be resurrected.

## 12. Relation to Paper 3

This result strengthens the Paper 3 architecture
\[
W_n(G)\to O(G)\to T(G).
\]

The HA58 experience supplies a concrete example where:

- a finite filtered computation detects genuinely new information;
- a natural-looking compressed carrier is not intrinsic;
- the correct carrier may have to retain gauge/extension parameters;
- recognition of a coarser target can remain possible even when a naive vector-level factorization fails.

This is directly relevant to the final Paper 3 question:
\[
\boxed{
\text{How much filtered relation information is necessary and sufficient to recover the canonical p-adic orientation?}
}
\]

## 13. CRITICAL REVIEW CORRECTION — 2026-09-27

The critical review correctly identifies a presentation defect: several classifications were stated without reproducing the definitions/proofs needed to make the audit self-contained. The mathematical record is tightened as follows.

### 13.1 Intrinsic connecting family: PROVED, but only at the cohomological-object level

The family is explicitly defined by
\[
L(\rho_2)=\{\rho_3:G\to(\mathbf Z/27)^\times:\rho_3\bmod9=\rho_2\}
\]
and, for each \(\rho_3\in L(\rho_2)\),
\[
0\to\mathbf F_3\to\mathbf Z/27(\rho_3)\to\mathbf Z/9(\rho_2)\to0
\]
with
\[
\delta_{3,\rho_3}:H^1(G,\mathbf Z/9(\rho_2))\to H^2(G,\mathbf F_3).
\]

The HA61-B5-8/B5-10/B5-13 source chain contains the definition and naturality argument. The proof mechanism is ordinary cohomological naturality: connecting maps are defined on cohomology classes, coboundary changes do not alter the connecting class, and group isomorphisms carrying coefficient data induce morphisms of short exact coefficient sequences.

Therefore PROVED is retained only for the intrinsic cohomological family, not for a finite filtered carrier or orientation-reconstruction theorem.

### 13.2 The single-vector counterexample is independently auditable

The decisive witness is the HA61-B5-12 source record.

For the same abstract group, replace the relator by
\[
r'=vrv^{-1}.
\]
The full crossed-word obstruction family is unchanged. In the chosen relation-jet coordinate,
\[
P\mapsto P+[v,R],
\qquad
T([v,R])=\lambda(v)f(p)
\]
on the primary-zero locus.

For the frozen rank-four q=3 branch,
\[
\lambda=e_2^*,\qquad p=e_1\ne0.
\]
Choose \(v\) with \(\lambda(v)=1\). Then
\[
t_2\mapsto t_2+p.
\]
The intrinsic coefficient data and the full connecting family remain unchanged. Hence a presentation-independent single vector \(t_2\) cannot represent the full secondary obstruction.

This is a genuine COUNTEREXAMPLE.

The two immediate repairs are also blocked:
- quotienting by \(\langle p\rangle\) loses \(f(p)\), since primary-zero gives
  \[
  f(p)+(\lambda\wedge f)(R)=0,
  \]
  not \(f(p)=0\);
- the diagonal \((t_2,\mu)\)-quotient identifies distinct coefficient lifts, so it is not an admissible intrinsic orientation carrier.

### 13.3 Scope lock for PROVED

\[
\boxed{\text{intrinsic cohomological definition/naturality of }\delta_3=\mathrm{PROVED}}
\]
but
\[
\boxed{W_n(G)\to\{\delta_{3,\rho_3}\}_{\rho_3}=\mathrm{OPEN}}
\]
and
\[
\boxed{\{\delta_{3,\rho_3}\}_{\rho_3}\to\chi\bmod27=\mathrm{OPEN}}.
\]

Invoking the already-known orientation/Kummer lifting characterization does not count as a new filtered reconstruction theorem.

### 13.4 Split the finite-depth source status

The earlier combined “PROVED / COMPUTED” label is replaced by:
- explicit finite source ledger: COMPUTED;
- individual divisibility/vanishing identities already established in the ledger: PROVED.

### 13.5 Define “frozen”

“Frozen” means the presentation/relator normal form, coefficient-extension convention, basis, and transgression normalization are fixed for an explicit calculation. No presentation-independence is claimed.

Thus frozen scalar/detection statements remain COMPUTED.

### 13.6 Literature audit correction

The earlier literature paragraph was too broad.

Quadrelli (2024), Example 2.6, explicitly states that an infinite Demuškin group has a canonical orientation, unique among orientations completing it to a 1-cyclotomic oriented pro-p group, and for the standard presentation gives
\[
\chi(x_2)=(1-p^f)^{-1}.
\]
This is EXTERNAL support for the canonical-orientation/Kummer-lifting background. urlQuadrelli 2024, Example 2.6turn0search0

Mináč–Pasini–Quadrelli–Tân (2021) establishes relationships between quadratic duals of Galois cohomology and the p-Zassenhaus filtration. This supports the general filtered/cohomological background, but does not establish the HA58 residual. EXTERNAL. urlKoszul algebras and quadratic duals in Galois cohomologyturn0search1

The earlier sentence claiming that the third cited source directly established loss of orientation information from Zassenhaus data is withdrawn until a primary source and exact theorem/proposition are identified.

### 13.7 Corrected overall status

- HA58 standard-family residual: COMPUTED;
- intrinsic cohomological delta_3 family: PROVED;
- finite-filtered factorization into that family: OPEN;
- single-vector t_2: COUNTEREXAMPLE;
- t_2/<p> and diagonal quotient repairs: COUNTEREXAMPLE;
- canonical projective bridge: OPEN;
- canonical scalar normalization for a finite intrinsic carrier: OPEN;
- richer secondary carrier / finite-filtered zero-selector: OPEN.

The phrase “끝까지 진행했다” is corrected to mean: the authorized audit procedure was completed, not that the orientation-reconstruction problem was solved.
