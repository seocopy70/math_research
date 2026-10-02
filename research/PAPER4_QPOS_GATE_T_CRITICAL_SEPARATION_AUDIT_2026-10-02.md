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
# PAPER 4 — GATE T CRITICAL SEPARATION AUDIT / CORRECTION
## 2026-10-02

## Authoritative correction

The earlier Gate-T audit is **not promoted as written**. A critical review correctly demanded an independent recheck of the relative-window construction and, more importantly, the distinction between the free presentation relator and its image in the Demuškin quotient. That review itself contains one decisive overcorrection:

For
\[
D=\langle x_1,\ldots,x_d\mid r_D\rangle,
\qquad
G_{s,a}=\langle z,x_1,\ldots,x_d\mid z^{p^s}=r_D\rangle,
\]
the assignment
\[
z\mapsto1,\qquad x_i\mapsto\bar x_i\in D
\]
is in fact a well-defined epimorphism
\[
\pi_s:G_{s,a}\twoheadrightarrow D,
\]
because the image of the defining relation is
\[
1=r_D\quad\text{in }D.
\]
Thus the natural quotient map is **not** the obstruction claimed in the submitted T0 critique. The statement “\(r_D\) is only a free-group relator and is not 1 in \(D\)” confuses the word-level relator in the free group with its image in the presented quotient.

Accordingly:

- **T0 as ‘does \(G_{s,a}\to D\) exist?’: PASS / LOCAL.**
- **T0 as a full finite-relative-window legitimacy theorem: OPEN.**

The existence of \(\pi_s\) is elementary; what still needs proof is the precise induced finite extension and its filtration compatibility at the claimed critical depth.

## 1. What remains unverified

The genuinely load-bearing step is not the existence of \(\pi_s\), but the assertion that at
\[
n=p^s+1
\]
the relative extension
\[
1\to K_n\to G_{s,a}/D_n(G_{s,a})
\xrightarrow{\bar\pi_s}
D/D_n(D)\to1
\]
has a nonzero class for \(s\), while the corresponding extension for \(t>s\) splits.

In particular, the following implication used by the previous audit is not automatic:
\[
z^{p^s}\in D_{p^s}(G_{s,a})
\quad\Longrightarrow\quad
\bar z^{p^s}\neq0\text{ in }D_{p^s}/D_{p^s+1}.
\]
The quotient relation can alter the actual Zassenhaus filtration. This must be proved in \(G_{s,a}\), not inferred from the free presentation alone.

Likewise, identifying the surviving class with the defining relation class in
\(H^2(D,\mathbf F_p)\) requires an explicit finite-layer transgression/extension-class lemma. The one-dimensionality of \(H^2(D,\mathbf F_p)\) by itself does not establish that the particular finite extension has nonzero class.

## 2. Correct gate order

The correct sequence is therefore
\[
\boxed{
\text{T0: canonical }\pi_s:G_{s,a}\to D
\;
\longrightarrow\;
\text{finite relative extension exists}
\;
\longrightarrow\;
\text{critical-layer calculation}
\;
\longrightarrow\;
\text{splitting/non-splitting}
}
\]

The first arrow is PASS/LOCAL. The remaining arrows are not yet closed.

## 3. Current threshold status

The rigorous information-level lower bound remains:
\[
n\le p^s
\Longrightarrow
z^{p^s}\in D_n(F),
\]
so the **presentation-level deep-tail invisibility** argument gives the natural lower-bound mechanism. Its transfer to an exact relative-window theorem is still subject to the finite-extension verification above.

Therefore the exact equality
\[
n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1
\]
must currently be classified
\[
\boxed{\textbf{OPEN / LOAD-BEARING}}.
\]

The previous **PASS / LOAD-BEARING** label is superseded.

## 4. Authoritative classification

- canonical epimorphism \(G_{s,a}\twoheadrightarrow D\): **PASS / LOCAL**;
- relative finite-window object at the definition level: **PASS / LOCAL**;
- fixed-depth deep-tail blindness: **PASS / LOCAL**;
- lower-bound heuristic/information mechanism \(n\ge p^s+1\): **PASS / LOCAL**;
- nonzero critical class at \(p^s+1\): **OPEN / LOAD-BEARING**;
- critical non-splitting for \(G_{s,a}\): **OPEN / LOAD-BEARING**;
- exact relative threshold \(p^s+1\): **OPEN / LOAD-BEARING**;
- unmarked filtered-group theorem: **OPEN**;
- universal q>0 free-by-Demushkin theorem: **OPEN**;
- class-2 norm: **SIDE / PAUSED**;
- RAAG: **CLOSED-AS-MAIN-ROUTE**.

## 5. Next authorized task

Do **not** jump to Gate U and do **not** start a new carrier hunt.

The singular next task is:

> **T0/T1 finite-layer verification:** compute the actual Zassenhaus layer and the induced extension class of \(G_{s,a}/D_{p^s+1}(G_{s,a})\to D/D_{p^s+1}(D)\), and independently verify whether the \(s\)-case is nonsplit while every \(t>s\) case splits.

Only a proof of that finite-layer statement may restore the exact threshold claim.


---

## 2026-10-02 — FINAL RE-AUDIT: CRITICAL LAYER SURVIVES, BUT NON-SPLITTING IS STILL OPEN

The previous correction identified the right logical gap, but a further independent audit sharpens it in both directions.

### 1. The critical class really does survive

Set
\[
n=p^s+1,\qquad s>a,
\]
and consider the finite class-2 \(p\)-group
\[
H_s=
\langle z,u,v\mid
z\ {\rm central},\ z^{p^{s+1}}=1,\ u^{p^a}=1,\ v^{p^{s+1}}=1,\ [u,v]=z^{p^s}
\rangle .
\]
Map
\[
z\mapsto z,\qquad x_1\mapsto u,\qquad x_2\mapsto v,\qquad
x_i\mapsto1\ (i\ge3).
\]
Because
\[
r_D\mapsto u^{p^a}[u,v]=z^{p^s},
\]
the defining relation \(z^{p^s}=r_D\) is satisfied, so
\[
G_{s,a}\twoheadrightarrow H_s.
\]

The group \(H_s\) has class \(2\), exponent dividing \(p^{s+1}\), and
\(\gamma_2(H_s)=\langle z^{p^s}\rangle\) of order \(p\). For odd \(p\),
\[
2p^{s-1}<p^s+1,
\]
so the Zassenhaus formula gives
\[
D_{p^s+1}(H_s)
\subseteq H_s^{p^{s+1}}\gamma_2(H_s)^{p^s}=1.
\]
Hence \(H_s\) factors through \(G_{s,a}/D_{p^s+1}(G_{s,a})\), while
\(z^{p^s}\ne1\) in \(H_s\). Therefore
\[
\boxed{z^{p^s}\notin D_{p^s+1}(G_{s,a}).}
\]

Classification:
\[
\boxed{\text{critical-layer survival at }p^s=\textbf{PASS / LOCAL}.}
\]

This is independent of any mildness/initial-form argument.

### 2. But this still does NOT prove non-splitting

There is a genuine \(q>0\) obstruction to the previous \(H^2\)-shortcut.

The Demuškin relation is
\[
r_D=x_1^{p^a}[x_1,x_2]\cdots[x_{d-1},x_d].
\]
At coefficient level \(p^s\), the torsion term \(x_1^{p^a}\) can absorb a would-be scalar defect by changing a lift of \(x_1\) by a \(p^{s-a}\)-power of the kernel generator.

At the centralized test level, put
\[
E'=\langle t,x_1,\ldots,x_d\mid
t\ {\rm central},\ t^{p^{s+1}}=1,\ D_n(F)=1,\ r_D=t^{p^s}\rangle .
\]
The apparent defect \(t^{p^s}\) is not automatically a nonzero \(H^2\)-class: it can be altered by a coboundary coming from a homomorphism \(F\to\langle t\rangle\), because
\[
x_1^{p^a}\mapsto t^{p^s}
\quad\text{when}\quad
x_1\mapsto t^{p^{s-a}}.
\]
Thus the previous implication
\[
\text{“relation class generates }H^2\text{”}
\Longrightarrow
\text{“finite relative extension is nonsplit”}
\]
is invalid without controlling lift-change/coboundary terms.

This is exactly the \(q>0\) phenomenon already seen in the closed untwisted \(H_1/E_2\) layer: the torsion term can absorb the naive scalar defect.

### 3. What survives

- \(G_{s,a}\twoheadrightarrow D\): **PASS / LOCAL**;
- deep-tail blindness for \(n\le p^s\): **PASS / LOCAL**;
- \(z^{p^s}\notin D_{p^s+1}(G_{s,a})\): **PASS / LOCAL**;
- critical extension class at \(p^s+1\): **OPEN / LOAD-BEARING**;
- non-splitting at \(p^s+1\): **OPEN / LOAD-BEARING**;
- exact threshold \(n_{\rm sep}^{\rm rel}(s)=p^s+1\): **OPEN / LOAD-BEARING**;
- unmarked filtered-group theorem: **OPEN**.

The earlier **PASS / LOAD-BEARING** threshold claim is **HISTORICAL / SUPERSEDED**.

### 4. The real next obstruction

The remaining problem is now sharply formulated:

> Determine the finite relative extension class in
> \[
> H^2\!\left(D/D_{p^s+1}(D),K_{p^s+1}^{\rm ab}\right)
> \]
> (or the appropriate first nonabelian quotient of the kernel), after quotienting all lift-change coboundaries.

The scalar \(z^{p^s}\) alone is not the invariant. The relevant object is the **module-valued defect together with the \(D/D_n(D)\)-action**.

Therefore the class-2/norm-action route is now the correct next finite-layer test. This is a narrowly targeted promotion, not a return to unrestricted carrier hunting.

### 5. Authoritative status

\[
\boxed{
\begin{array}{ll}
\text{Gate O fixed-depth no-go} & \mathbf{PASS/CLOSED}\\
\text{critical-layer survival at }p^s & \mathbf{PASS/LOCAL}\\
\text{critical non-splitting at }p^s+1 & \mathbf{OPEN/LOAD-BEARING}\\
\text{exact relative threshold }p^s+1 & \mathbf{OPEN/LOAD-BEARING}\\
\text{unmarked theorem} & \mathbf{OPEN}\\
\text{class-2 norm/action finite-layer test} & \mathbf{NEXT\ AUTHORIZED}
\end{array}}
\]

No Gate-U jump and no blind carrier search is authorized.


---

## 8. FINAL CORRECTION — VISIBILITY IS NOT IDENTIFIABILITY

The previous sections are retained for provenance, but their claimed nonsplitting conclusion is superseded by the following correction.

The class-2 quotient
\\[
H_s=\\langle z,u,v\\mid z\\text{ central},\\ z^{p^{s+1}}=1, u^{p^a}=1, v^{p^{s+1}}=1, [u,v]=z^{p^s}\\rangle
\\]
with \\(x_1\\mapsto u\\), \\(x_2\\mapsto v\\), and the remaining generators trivial, is a quotient of \\(G_{s,a}\\). Since \\(D_{p^s+1}(H_s)=1\\) while \\(z^{p^s}\\ne1\\), one rigorously obtains
\\[
z^{p^s}\\notin D_{p^s+1}(G_{s,a}).
\\]
Hence **critical-layer visibility = PASS / LOCAL**.

But this does not identify the relative extension class. The naive scalar central extension test admits lift changes; specifically the \\(x_1^{p^a}\\) term can absorb a \\(p^s\\)-scalar defect after changing a lift by a \\(p^{s-a}\\)-power of the central kernel generator. Therefore the previous implication “surviving scalar layer + one-dimensional \\(H^2\\) = nonsplit finite extension” is not valid without an explicit coboundary quotient calculation.

The correct decomposition is:

1. **Visibility:** \\(z^{p^s}\\) survives the actual finite filtration — **PASS / LOCAL**.
2. **Identifiability:** the finite relative extension class remains after all lift changes — **OPEN / LOAD-BEARING**.
3. **Threshold:** \\(n_{\\rm sep}^{\\rm rel}(s)=p^s+1\\) — **OPEN / LOAD-BEARING** until (2) is proved.

The next object is therefore the actual finite kernel
\\[
K_s=\\ker\\left(G_{s,a}/D_{p^s+1}(G_{s,a})\\to D/D_{p^s+1}(D)\\right),
\\]
its \\(D/D_{p^s+1}(D)\\)-action, the quotient by lift-change coboundaries, and the resulting module-valued extension class. A class-2/norm calculation is only a **CONDITIONAL reduction** after this kernel/action is established; it is not an independently authorized replacement for T1.

**Authoritative classification:**
- critical-layer survival: **PASS / LOCAL**;
- scalar \\(H^2\\) nonsplitting shortcut: **FAIL / CLOSED**;
- actual module-valued extension class: **OPEN / LOAD-BEARING**;
- exact relative threshold: **OPEN / LOAD-BEARING**;
- prior exact-threshold PASS: **HISTORICAL / SUPERSEDED**.

No Gate-U jump and no blind carrier hunt is authorized.
