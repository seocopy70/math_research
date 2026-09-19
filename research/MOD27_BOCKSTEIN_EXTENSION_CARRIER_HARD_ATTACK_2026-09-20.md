# HARD ATTACK 16 — COEFFICIENT-9 BOCKSTEIN CARRIER CANDIDATE FOR MOD-27 — 2026-09-20

## Target

After the category-adequacy correction, test the first genuinely new candidate that is neither a higher-Bockstein slogan nor a Fox re-encoding:

\[
\mathcal B_{27}(G)=
\bigl(H^1(G,\mathbf F_3),H^1(G,\mathbf Z/9),
\mathrm{red},\iota,\smile,\beta_1,\beta_9\bigr),
\]

where \(\iota:\mathbf F_3\hookrightarrow\mathbf Z/9\) is multiplication by 3, \(\beta_1\) is the usual mod-3 Bockstein, and

\[
\beta_9:H^1(G,\mathbf Z/9)\to H^2(G,\mathbf F_3)
\]

is the connecting map for

\[
0\to\mathbf F_3\to\mathbf Z/27\to\mathbf Z/9\to0.
\]

All of these are functorial, q-blind, and defined without a candidate orientation.

## 1. Definition-level status

The carrier is genuinely coefficient-extension data, not the exact Fox row. It contains the already-audited mod-9 data as a visible subquotient:

\[
(H^1(G,\mathbf F_3),\smile,\beta_1)
\subset \mathcal B_{27}.
\]

Naturality under group isomorphisms is built into cohomology and connecting homomorphisms. No Nielsen presentation or relator normalization is selected.

Thus the candidate passes the first definition-level tests:

- Object: **PASS**
- q-blindness: **PASS**
- functoriality: **PASS / structural**
- reduction to the mod-9 carrier: **PASS / natural**
- non-tautological input: **PASS / LOCAL**

No Fox equation is used to define the object.

## 2. Exact frozen-family computation

For the standard rank-four relation

\[
r_q=x_1^q[x_1,x_2][x_3,x_4],
\qquad q=3^s,
\]

a class \(f\in H^1(G,\mathbf Z/9)\) may be lifted to \(\widetilde f\) with values in \(\mathbf Z/27\). The connecting obstruction is obtained by evaluating \(\widetilde f(r_q)\) and dividing by 9. The commutator factors have zero exponent sum, so the power term gives

\[
\beta_9(f)
=
\frac{q\,f(x_1)}9\,\omega
\quad\text{in }H^2(G,\mathbf F_3),
\]

whenever the defining relation forces the numerator to be divisible by 9.

For the first Bockstein,

\[
\beta_1(f_0)=
\frac{q\,f_0(x_1)}3\,\omega
\qquad
(f_0\in H^1(G,\mathbf F_3)).
\]

Hence the successive coefficient-extension layers distinguish exactly the first three mod-27 cases:

- \(q=3\): \(\beta_1\ne0\);
- \(q=9\): \(\beta_1=0\), while \(\beta_9\) has a nonzero descended component;
- \(q\equiv0\pmod{27}\): both relevant components vanish.

The key naturality identity is

\[
\beta_9\circ\iota=\beta_1.
\]

Therefore, when \(\beta_1=0\), \(\beta_9\) canonically descends through

\[
H^1(G,\mathbf Z/9)\twoheadrightarrow H^1(G,\mathbf F_3).
\]

This removes the main lift-choice ambiguity in the q=9/q\ge27 branch.

## 3. Candidate orientation bridge

Let \(R\) denote the nondegenerate mod-3 cup pairing. Any nonzero map

\[
V=H^1(G,\mathbf F_3)\to H^2(G,\mathbf F_3)
\]

is represented by a covector, and the symplectic pairing identifies that covector with a unique vector \(e\in V\).

The frozen-family calculation then gives the candidate bridge for the additive orientation digit

\[
\lambda_{27}:=\frac{\chi-1}{3}\pmod9:
\]

\[
\lambda_{27}=
\begin{cases}
e(\beta_1), & \beta_1\ne0,\\
3e(\overline\beta_9), & \beta_1=0,\ \overline\beta_9\ne0,\\
0, & \beta_1=0,\ \overline\beta_9=0.
\end{cases}
\]

For the standard family this yields

\[
q=3:\ \lambda_{27}=4e_2,
\qquad
q=9:\ \lambda_{27}=3e_2,
\qquad
q\equiv0\pmod{27}:\ \lambda_{27}=0,
\]

and therefore

\[
\chi(x_2)\equiv
13,10,1\pmod{27},
\]

respectively.

The formula is structurally consistent with

\[
\frac{(1-q)^{-1}-1}{3}
=
\frac{q/3}{1-q}
\pmod9.
\]

This is strong evidence, but not yet a theorem of intrinsic orientation recovery.

## 4. Critical attack on the bridge

Three gaps remain and are load-bearing:

1. **Canonical identification in the q=3 branch.** The nonzero \(\beta_1\) gives the already-audited mod-9 vector, but the exact interpretation of that vector as the first term of \((\chi-1)/3\pmod9\) must be stated as a natural theorem, not inferred from the standard presentation.

2. **q=9 descended Bockstein.** One must prove that the descended \(\overline\beta_9\), together with the mod-3 cup pairing, canonically produces exactly the coefficient 3 in the orientation digit and not merely a detector for q=9. The direct relation calculation establishes this in the frozen family; naturality under all admissible gauge/morphism maps remains to be proved.

3. **General admissible objects.** The formula has so far been verified on the standard Demuškin family. It is not yet proved for every object in the intended category, nor has the exact orientation target functor \(O_{27}\) been formalized in a way that makes the bridge independent of a chosen symplectic basis.

## 5. Separation and compatibility

The candidate separates the three relevant mod-27 orientation classes in the rank-four family:

\[
\chi_3(x_2)=13,\qquad
\chi_9(x_2)=10,\qquad
\chi_{27}(x_2)=1\pmod{27}.
\]

Its reduction retains \(\beta_1\) and the cup pairing, hence recovers the established \(\overline J_3\) at mod 9.

However, separation alone is not sufficient for PASS/CLOSED. The natural orientation bridge is still the unresolved theorem.

## 6. Relation to the previously closed higher-Bockstein route

This does NOT revive “higher Bocksteins alone.”

The earlier FAIL/CLOSED result concerned the unsupported inference

\[
\text{higher Bockstein classes}\Rightarrow\chi\text{ digits}.
\]

The present candidate is different: it packages the coefficient extension

\[
H^1(G,\mathbf F_3)
\leftarrow H^1(G,\mathbf Z/9)
\]

together with cup-duality and a specific finite-level assembly rule. The assembly rule itself is the theorem still to be proved.

## Decision

**MOD-27 Bockstein-extension carrier: OPEN / STRONG CANDIDATE.**

Current gate status:

- definition: **PASS**
- q-blindness: **PASS**
- functoriality: **PASS / structural**
- gauge naturality: **OPEN / theorem to write**
- reduction to J_9: **PASS / structural**
- separation: **PASS / LOCAL**
- orientation bridge: **OPEN / load-bearing**
- non-tautology: **PASS / LOCAL**
- strict compression below Fox: **OPEN**

No claim of full mod-27 reconstruction is made yet.

## Next authorized attack

Prove or disprove the orientation bridge intrinsically, without choosing the standard presentation as part of the definition. The cleanest test is a natural algebraic statement expressing the mod-27 logarithmic orientation digit through the coefficient-extension/cup-pairing data above. If that theorem fails under a Nielsen/gauge transformation, close this candidate. If it survives, the result is the first serious intrinsic J_27 candidate.


## HARD ATTACK 17 — IS THE “BRIDGE” JUST q-VALUATION REPACKAGED? — 2026-09-20

The previous candidate must now be attacked at the non-tautology level. The coefficient-extension data \(\beta_1,\overline\beta_9\) separate the standard family precisely by the 3-adic valuation class of q:
\[
v_3(q)=1,\quad v_3(q)=2,\quad v_3(q)\ge3.
\]
But the proposed orientation values
\[
\frac13\log((1-q)^{-1})\equiv 1,3,0\pmod9
\]
are themselves a known function of this q-valuation class. Therefore the implication
\[
\mathcal B_{27}\Rightarrow \lambda_{27}
\]
can be obtained by the two-step route
\[
\mathcal B_{27}\Rightarrow v_3(q)\text{-class}\Rightarrow q\text{-class}\Rightarrow\chi\text{-class},
\]
using the known Demuškin orientation formula. That is exactly the kind of classification/repackaging route excluded by the tightened PRE-MOD27 gate.

This does not show that \(\mathcal B_{27}\) is useless: it is a genuine intrinsic obstruction package and may be a natural detector of the first finite q-information layers. It does show that the currently proposed orientation bridge has not yet established a new obstruction-theoretic factorization. The direct standard-relator calculation cannot by itself distinguish a structural bridge from a disguised recovery of q followed by the known formula.

### Stronger counter-test

To certify non-tautology, one must produce a natural chain-level/coefficient-extension identity whose output is \(\frac13\log\chi\) without first identifying the q-class, or prove an independent universal property characterizing that logarithmic orientation functional. Merely observing the same three values on \(q=3,9,27\) is insufficient.

An even sharper test is to enlarge the frozen family to all admissible Demuškin orientations/automorphisms while holding the abstract coefficient-extension carrier fixed up to its natural isomorphism class. If the carrier only records the valuation/classification datum and loses the actual character action, then it cannot supply a genuinely new orientation bridge.

### Decision

**MOD-27 BOCKSTEIN-EXTENSION CARRIER AS AN ORIENTATION CARRIER: CONDITIONAL / NOT YET ADMISSIBLE.**

The coefficient-extension package itself remains **PASS / LOCAL as an intrinsic q-information detector**, but its proposed orientation bridge is downgraded from OPEN/STRONG CANDIDATE to **CONDITIONAL** because the current evidence is compatible with forbidden classification repackaging.

The next authorized attack is therefore not another numerical q-scan. It is a factorization test: determine whether a presentation-free universal identity produces the logarithmic orientation digit directly from \(\mathcal B_{27}\), or whether every such map necessarily factors through the q/classification invariant. If only the latter is available, close this carrier as a new orientation carrier while retaining its detector result.


## HARD ATTACK 18 — INTERNAL AUTOMORPHISM OBSTRUCTION TO THE MOD-27 ORIENTATION LIFT — 2026-09-20

A stronger obstruction appears at the level of the proposed carrier itself.

For the frozen \(q=3\) object, write \(H^1(G,\mathbf Z/9)\) by generator values \(a_i\). The relation forces \(a_1\in3\mathbf Z/9\), while \(a_2,a_3,a_4\) are unrestricted. The declared carrier structure consists of reduction, \(\iota(f)=3f\), the mod-3 cup product, \(\beta_1\), and \(\beta_9\).

Consider
\[
S(a_1,a_2,a_3,a_4)=(a_1,4a_2,a_3,a_4).
\]
This is \(\mathbf Z/9\)-linear. Since \(4\equiv1\pmod3\) and \(4\cdot3\equiv3\pmod9\), it fixes reduction and the image of \(\iota\). It leaves the mod-3 cup product unchanged and preserves \(\beta_9\), whose relation-level formula depends only on the \(a_1\)-component. Thus \(S\) is an automorphism of the declared coefficient-extension carrier while inducing the identity on \(H^1(G,\mathbf F_3)\).

For \(q=3\), the desired logarithmic digit is
\[
\lambda_{27}=\frac13\log\chi\equiv e_2\pmod9.
\]
But the carrier has no invariant characteristic-zero lift of the nonzero mod-3 direction \(e_2\): the coefficient-extension symmetry changes such a lift by the unit \(4\), while fixing every declared structural datum. Hence the proposed carrier cannot canonically rigidify the \(3\)-adic unit needed for the mod-27 orientation.

This is stronger than the previous q-repackaging objection. It is an internal-symmetry obstruction, not merely a criticism of one proof of the bridge.

### Decision

\[
\boxed{\mathcal B_{27}\text{ as a natural mod-27 orientation carrier: FAIL / CLOSED.}}
\]

Surviving results:
- \(\mathcal B_{27}\) as an intrinsic detector of the first finite \(3\)-adic valuation layers: **PASS / LOCAL**;
- separation of \(q=3,9,\ge27\) at the coefficient-extension level: **PASS / LOCAL**;
- recovery of \(\chi\bmod27\) from the declared carrier: **FAIL / CLOSED**;
- a different mod-27 carrier with additional rigidifying structure remains **OPEN**.

No further numerical scan of this Bockstein package is authorized. Any successor must contain genuinely new rigidifying structure or a different universal property.


## CORRECTION / HARD ATTACK 19 — FORMAL MORPHISM CATEGORY AND REALIZABILITY TEST — 2026-09-20

The previous Hard Attack 18 contained a genuine logical overreach. The map
\[
S(a_1,a_2,a_3,a_4)=(a_1,4a_2,a_3,a_4)
\]
was shown to be an automorphism of the **abstract declared carrier**, but not to be an admissible morphism in the project's formal input category. Therefore its existence alone cannot imply failure of a natural bridge from the group-level input.

The correct question is now categorical, not numerical.

### 1. Carrier category
Define \(\mathcal C_{27}^{\mathrm{abs}}\) to have objects
\[
(V,W,\mathrm{red},\iota,\smile,\beta_1,\beta_9)
\]
with the stated algebraic structure, and all structure-preserving isomorphisms as morphisms. Define \(\mathcal C_{27}^{\mathrm{real}}\) to be the subcategory consisting of the same carriers together with morphisms induced by admissible continuous group isomorphisms and declared gauge transformations of the filtered/relation input.

A factorization through the carrier is only required to be natural for the morphisms actually belonging to the declared input category.

### 2. Status of S
For the frozen q=3 carrier, S is a morphism of \(\mathcal C_{27}^{\mathrm{abs}}\): it preserves reduction, \(\iota\), the mod-3 cup pairing, and the displayed \(\beta_9\) structure. This establishes an **abstract-carrier symmetry**.

But S has not been shown to lie in \(\mathcal C_{27}^{\mathrm{real}}\). In particular, an admissible group automorphism inducing S would have to preserve the canonical orientation of the group. At mod 27 this is a stringent realizability condition, not implied by the mod-9 action on \(H^1(G,\mathbf Z/9)\).

Thus Hard Attack 18's statement “S proves a no-go” is superseded by the sharper statement:

> **S gives a conditional no-go: if the bridge is required to be natural for all abstract structure-preserving carrier isomorphisms, then the bridge cannot select the logarithmic orientation lift. Under the project's present group-induced morphism convention, realizability of S must be proved before that no-go is valid.**

### 3. Realizability attack
Assume an admissible group automorphism \(\alpha\) induced S on the coefficient carrier. Since the canonical orientation is intrinsic to the group, naturality gives
\[
\chi\circ\alpha=\chi.
\]
For q=3, the desired mod-27 logarithmic direction is the \(x_2\)-direction. If S acts by multiplication by 4 on that coefficient direction, then at the mod-27 level it would force compatibility with the multiplicative character action. This can be tested directly on the abelianized coefficient action.

The key point is that a mod-9 coincidence is not enough: \(4\equiv1\pmod3\), and even powers can appear invisible at lower precision, while the mod-27 character detects the lift. Therefore any attempted realization must be checked at the actual target precision, not merely on the carrier's mod-3 shadow.

### 4. Consequence of the two outcomes
- If S is realizable by an admissible group/gauge morphism, and the induced target action is nontrivial on the orientation lift, then the Bockstein carrier is **FAIL / CLOSED** as a mod-27 orientation carrier.
- If S is not realizable, the obstruction is itself informative: determine exactly which q-blind group-level/filtered datum forbids S. If that datum is merely the hidden canonical orientation, q, or an equivalent classification invariant, then it is not admissible as a new rigidifier. If it is a genuinely q-blind extension datum, it becomes the candidate missing structure.
- If the obstruction uses only higher characteristic-zero information already equivalent to the Fox orientation locus, the Bockstein carrier still fails the intended compression criterion.

### 5. Current classification after correction
- Abstract carrier symmetry S: **PASS / LOCAL**.
- Hard Attack 18 “absolute no-go”: **HISTORICAL / SUPERSEDED**.
- Bockstein package as finite q-layer detector: **PASS / LOCAL**.
- Bockstein package as mod-27 orientation carrier: **CONDITIONAL / OPEN**.
- Next stop: resolve realizability of S before any further numerical scan.

This correction is binding for subsequent work.


## HARD ATTACK 20 — FACTORIZATION THROUGH THE q-VALUATION QUOTIENT — 2026-09-20

Hard Attack 19 shows that the abstract symmetry S cannot be promoted to a no-go without proving realizability as a group-induced morphism. We therefore attack the candidate at a different, stronger level: whether its entire mod-27 information on the Demuškin test family is genuinely finer than the q-classification datum.

Let
\[
\nu_{27}(q)=
\begin{cases}
1,&v_3(q)=1,\\
2,&v_3(q)=2,\\
\ge3,&v_3(q)\ge3.
\end{cases}
\]
The coefficient-extension calculation gives exactly three carrier types on the rank-four family:
\[
\beta_1\neq0,\qquad
\beta_1=0,\ \overline\beta_9\neq0,\qquad
\beta_1=0,\ \overline\beta_9=0,
\]
corresponding respectively to \(\nu_{27}=1,2,\ge3\). No additional mod-27 orientation-sensitive invariant has been exhibited inside the declared package.

Hence, on this family, the isomorphism type of the declared Bockstein package factors through
\[
\mathcal B_{27}\longleftarrow \nu_{27}(q).
\]
At the same time the canonical orientation reduction is already known to factor through the same three classes:
\[
\frac13\log\chi\equiv e_2,\ 3e_2,\ 0\pmod9,
\]
with corresponding \(\chi(x_2)\equiv13,10,1\pmod{27}\).

Therefore any bridge from the **isomorphism type of this carrier alone** to the mod-27 orientation on this family is, extensionally, a function of the same three valuation/classification classes. The direct obstruction calculation has not produced an independent universal identity; it has only recovered the same finite classification partition.

This is not the claim that no abstract map \(\mathcal B_{27}\to O_{27}\) exists. Such a map can exist on the tested family. The claim is narrower and decisive for the project gate:

> The present package has not supplied an obstruction-theoretic factorization that is genuinely finer than, or independent of, the q-classification quotient. Its successful mod-27 values are completely explained by the same finite q-valuation partition.

Thus the candidate fails the project's operational non-tautology criterion unless a new structure inside the coefficient-extension package is exhibited that survives while the q-valuation class is held fixed and nevertheless distinguishes the orientation lift.

### Strong stop consequence
No further calculation of \(\beta_1,\beta_9\) on the same Demuškin q-family can establish novelty. To reopen the carrier, one must add genuinely new q-blind structure or produce an independent universal property/chain-level identity that does not pass through the valuation/classification quotient.

### Decision
- coefficient-extension package as finite q-layer detector: **PASS / LOCAL**;
- abstract carrier symmetry S: **PASS / LOCAL**;
- Hard Attack 18 unconditional symmetry no-go: **HISTORICAL / SUPERSEDED**;
- Bockstein package as a **new non-tautological mod-27 orientation carrier**: **FAIL / CLOSED** under the declared PRE-MOD27 gate;
- a different carrier with genuinely new rigidifying information: **OPEN**.
