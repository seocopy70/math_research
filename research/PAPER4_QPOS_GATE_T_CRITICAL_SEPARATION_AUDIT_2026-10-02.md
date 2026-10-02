# PAPER 4 — GATE T CRITICAL SEPARATION AUDIT
## 2026-10-02

## Verdict

The first possible separating depth can be settled **for the structured relative finite window** over the fixed Demuškin quotient.

For
\[
G_{s,a}=\langle z,x_1,\ldots,x_d\mid z^{p^s}=r_D\rangle,
\qquad
r_D=x_1^{p^a}[x_1,x_2]\cdots[x_{d-1},x_d],
\qquad s>a,
\]
and
\[
W_n^{\mathrm{rel}}(G_{s,a})
=
\left(G_{s,a}/D_n(G_{s,a})\to D/D_n(D)\right),
\]
the following holds:

\[
W_n^{\mathrm{rel}}(G_{s,a})
\cong
W_n^{\mathrm{rel}}(G_{t,a})
\quad(n\le p^s),
\]
whereas at
\[
n=p^s+1
\]
the relative windows separate for every \(t>s\).

Thus, in the **relative-window category**,
\[
\boxed{n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1.}
\]

This does **not** yet prove the same statement for the completely unmarked underlying filtered groups
\(G_{s,a}/D_n(G_{s,a})\) with the quotient map to \(D/D_n(D)\) forgotten. That unmarked isomorphism problem remains separate.

---

## 1. Lower bound: no separation through \(p^s\)

For \(n\le p^s\),
\[
z^{p^s}\in D_{p^s}(F)\subseteq D_n(F).
\]
Functoriality of the Zassenhaus filtration gives
\[
G_{s,a}/D_n(G_{s,a})
\cong
F/(D_n(F),r_D).
\]
The same holds for every \(t\ge s\). The induced map to the fixed quotient
\(D/D_n(D)\) is therefore the same.

Hence
\[
W_n^{\mathrm{rel}}(G_{s,a})
\cong
W_n^{\mathrm{rel}}(G_{t,a})
\qquad(n\le p^s).
\]

This proves the information-theoretic lower bound
\[
n_{\mathrm{sep}}^{\mathrm{rel}}(s)\ge p^s+1.
\]

---

## 2. What changes at \(p^s+1\)

Put
\[
n=p^s+1.
\]

For \(G_{t,a}\) with \(t>s\),
\[
p^t\ge p^{s+1}>p^s+1=n,
\]
so
\[
z^{p^t}\in D_n.
\]
The defining relation therefore becomes
\[
r_D=1
\]
inside the finite relative window. Consequently the canonical \(x_i\)-lifts define a section
\[
D/D_n(D)\longrightarrow G_{t,a}/D_n(G_{t,a}).
\]
The relative extension is split at this depth.

For \(G_{s,a}\), however,
\[
z^{p^s}\notin D_{p^s+1}(F)
\]
at the free level, and the defining relation is
\[
r_D=z^{p^s}.
\]
The top surviving kernel layer contains the class
\[
\bar z^{p^s}\in D_{p^s}(G_{s,a})/D_{p^s+1}(G_{s,a}).
\]

The key point is that this is not merely a presentation coefficient. Project the extension to this top elementary-abelian layer. The induced central extension class is represented by the defining relation class of \(D\).

For a one-relator Demuškin presentation, the relation class generates the one-dimensional \(H^2(D,\mathbf F_p)\); equivalently, the standard presentation transgression identifies the defining relation with the generator of \(H^2\). This is the usual one-relator/Demuškin relation-module description. Hence the projected extension class is nonzero.

Therefore the relative extension for \(G_{s,a}\) is **non-split** at \(n=p^s+1\).

The distinction is consequently:

\[
\boxed{
\begin{array}{c|c}
G_{s,a} & \text{non-split relative extension at }p^s+1\\
G_{t,a},\ t>s & \text{split relative extension at }p^s+1
\end{array}}
\]

and the two relative windows cannot be isomorphic as extensions over
\(D/D_n(D)\).

The standard fact that extension classes in \(H^2\) detect splitting is used here. The one-relator/Demuškin setting has
\(\dim H^2(D,\mathbf F_p)=1\), and the defining relation represents its generator. citeturn5search5turn5search0

---

## 3. The exact threshold result

Combining §§1–2:

\[
\boxed{
W_n^{\mathrm{rel}}(G_{s,a})
\cong
W_n^{\mathrm{rel}}(G_{t,a})
\text{ for all }n\le p^s,
}
\]

while

\[
\boxed{
W_{p^s+1}^{\mathrm{rel}}(G_{s,a})
\not\cong
W_{p^s+1}^{\mathrm{rel}}(G_{t,a})
\quad(t>s).
}
\]

Therefore

\[
\boxed{
n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1.
}
\]

This is now a **threshold theorem for the structured relative finite-window problem**, not merely a lower bound.

The use of the Zassenhaus filtration is standard: its terms satisfy the power and commutator compatibility needed above, and the graded quotients are elementary abelian. citeturn3search0

---

## 4. Critical scope boundary

There are two distinct claims:

### A. Relative finite-window theorem
Input includes the natural map
\[
G_{s,a}/D_n(G_{s,a})
\longrightarrow D/D_n(D).
\]

Status:
\[
\boxed{\textbf{PASS / LOAD-BEARING}}
\]

with the exact threshold \(p^s+1\).

### B. Unmarked filtered-group theorem
Only
\[
G_{s,a}/D_n(G_{s,a})
\]
and its filtration are given; the map to the fixed Demuškin quotient is forgotten.

Status:
\[
\boxed{\textbf{OPEN}}
\]

The relative splitting/non-splitting invariant cannot simply be called an invariant of the unmarked group. Proving that the quotient map is intrinsically recoverable would be a separate theorem and is not supplied here.

This distinction is mandatory. No promotion from A to B is allowed without proof.

---

## 5. Consequences for the research program

The earlier Gate O result is strengthened:

1. Fixed-depth uniform recovery of unbounded \(s\):
   **FAIL / CLOSED**.

2. Any separating depth must satisfy:
   \[
   n\ge p^s+1.
   \]
   **PASS / LOCAL**.

3. The relative stress family attains the lower bound exactly:
   \[
   n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1.
   \]
   **PASS / LOAD-BEARING**.

4. Therefore another blind search for a smaller carrier is mathematically misdirected: the first surviving information appears exactly at the first possible depth in the structured relative window.

5. The class-2 norm candidate is no longer needed to establish this threshold theorem. It remains **SIDE / PAUSED** unless a separate compression theorem is desired.

---

## 6. Novelty boundary

The equality \(p^s+1\) itself is not automatically a new theorem in the broad literature merely because it appears here. The research contribution, if developed further, would have to be formulated at the level of:

- the declared stress-family/relative-window category;
- the information-theoretic lower bound;
- the critical-depth non-splitting mechanism;
- and, ultimately, a theorem connecting this threshold to the intended Demuškin/PD² recognition problem.

The current result should therefore not be advertised as a universal finite-window theorem for all free-by-Demushkin extensions.

---

## 7. Authoritative classification

- Gate O fixed-depth information no-go: **PASS / CLOSED**.
- Lower bound \(n_{\mathrm{sep}}\ge p^s+1\): **PASS / LOCAL**.
- Gate T in the structured relative-window category: **PASS / LOAD-BEARING**.
- Exact relative threshold \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\): **PASS / LOAD-BEARING**.
- Same theorem for unmarked filtered groups: **OPEN**.
- Universal theorem for all q>0 free-by-Demushkin extensions: **OPEN**.
- Class-2 norm as primary route: **SIDE / PAUSED**.
- RAAG route: **CLOSED-AS-MAIN-ROUTE**.

No claim is made that the unmarked finite window alone canonically recovers the Demuškin quotient map.
