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
