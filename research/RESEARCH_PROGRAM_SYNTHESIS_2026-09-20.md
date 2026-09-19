# RESEARCH PROGRAM SYNTHESIS — 2026-09-20 00:55 KST

## 0. One-sentence research question

For the rank-four Demuškin pro-3 group
\[
G_q=\langle x_1,x_2,x_3,x_4\mid x_1^q[x_1,x_2][x_3,x_4]=1\rangle,
\]
especially the frozen case \(q=3\), determine **exactly how much filtered/relation information is necessary and sufficient to recover the canonical 3-adic orientation**
\[
\chi:G\to\mathbf Z_3^\times,
\]
with the stronger objective of identifying a presentation-natural, q-blind intrinsic carrier that is genuinely smaller than the full characteristic-zero Fox/presentation data.

The project is not merely “find a formula for \(\chi\)”. The central problem is the **information boundary**: what is visible in the associated graded object, what first extension data adds, what is sufficient for all 3-adic digits, and whether that information admits a non-tautological intrinsic compression.

---

## 1. Refined research architecture

### Layer A — graded information
Start from the intrinsic Zassenhaus/Jennings–Lazard mod-3 associated graded object.

Question:
\[
\operatorname{gr}_3(G)\Rightarrow\chi\ ? 
\]

Current answer: **NO**. The full mod-3 graded Demuškin object is q-blind in the present odd-prime setting.

### Layer B — first filtered extension
Add the first non-graded degree-(2,3) relation information:
\[
J_3=\langle R_2,P_3\rangle,
\qquad
\overline J_3=[(R,p(P_3))].
\]

Question:
\[
\overline J_3\Rightarrow\chi\bmod 9?
\]

Current answer: **YES**, intrinsically at the stated mod-9 level.

### Layer C — higher finite levels
For each \(n\ge2\), ask whether there is an intrinsic finite-level carrier
\[
J_{3^n}(G)
\]
that is presentation/Nielsen-gauge independent, separates \(\chi\bmod 3^n\), and admits natural reduction
\[
J_{3^{n+1}}\to J_{3^n}.
\]

This is the present principal OPEN program.

### Layer D — inverse limit
If such a compatible intrinsic tower exists,
\[
J_{27}\to J_9,quad J_{81}\to J_{27},\ldots,
\qquad
J_\infty=\varprojlim_nJ_{3^n},
\]
then test whether
\[
J_\infty\Rightarrow\chi
\]
and whether this tower is genuinely smaller than the completed Fox/presentation object.

### Layer E — exact characteristic-zero comparison
The universal exact Fox obstruction carrier is known to recover the full \(\chi\) and is presentation-covariant under the audited hypotheses.

The remaining question is **not** whether Fox works. It is whether an independently defined intrinsic filtered object factors naturally into it while retaining strictly less information.

---

## 2. What is now firmly established

### PASS / CLOSED

1. **Canonical full orientation for the frozen q=3 relation.**
   The intrinsic crossed-derivation characterization gives
   \[
   \chi(x_1)=\chi(x_3)=\chi(x_4)=1,
   \qquad
   1+2\chi(x_2)=0,
   \]
   hence
   \[
   \chi(x_2)=-\frac12=(1-3)^{-1}.
   \]
   Therefore
   \[
   \chi(x_2)=4\pmod9,\ 13\pmod{27},\ 40\pmod{81},\ldots
   \]

2. **Bare mod-3 associated graded is insufficient even in full degree.**
   The complete mod-3 graded Demuškin algebra is q-blind in the relevant fixed-rank odd-prime setting. Thus
   \[
   \operatorname{gr}_3G\not\Rightarrow q\not\Rightarrow\chi.
   \]
   This is stronger than a bounded-degree obstruction.

3. **First non-graded extension layer recovers mod 9.**
   The projective degree-(2,3) carrier
   \[
   \overline J_3=[(R,p)]
   \]
   is intrinsic under the audited cup/Bockstein/transgression conventions and recovers
   \[
   \chi\bmod9=(1,4,1,1)
   \]
   for q=3.

4. **Bockstein identification is load-bearing and audited.**
   The Bockstein direction agrees projectively with the restricted-cubic power direction \(p(P_3)\), up to the standard common gauge/sign/unit.

5. **The full compatible filtered extension tower is sufficient in a formal inverse-limit sense.**
   If the input literally retains compatible filtered relation residues, completeness reconstructs the completed relation; continuous Fox calculus then recovers the exact orientation. This is **PASS / LOCAL**, not a compression theorem.

6. **Exact universal Fox carrier works.**
   The universal twisted Fox obstruction scheme is non-circular as an input object; its zero locus gives the orientation, and its presentation covariance has been audited under the stated one-relator/Fox hypotheses.

7. **The fixed-q=3 local Fox algebra is already reduced.**
   \[
   \mathcal A_{Fox}
   =\mathbf Z_3[[u_1,u_2,u_3,u_4]]/(u_1,u_3,u_4,2u_2+3)
   \cong\mathbf Z_3.
   \]
   Therefore there is no proper quotient of this local algebra that preserves the full characteristic-zero point.

---

## 3. What has been positively ruled out

### FAIL / CLOSED

1. **Bare graded carrier → mod 9/full chi.**
   The q=3 and q=∞ controls have the same relevant graded object but different orientations.

2. **Naive \(\mathbf Z_3\)-augmentation jet \(\langle r-1\rangle\subset I^2/I^4\).**
   In ordinary \(\mathbf Z_3[[F]]\) augmentation degree,
   \[
   r-1=3X_1+[X_1,X_2]+[X_3,X_4]+O(I^3),
   \]
   so \(r-1\notin I^2\).

3. **Naive scalar extension of the characteristic-3 restricted-Lie carrier to \(\mathbf Z_3\).**
   The characteristic-3 p-operation does not become the required exact characteristic-zero structure by scalar extension.

4. **Fixed-normal-form degree-3 Fox truncation as an intrinsic object.**
   A Nielsen-equivalent presentation gives a nonzero residual
   \[
   -243/2
   \]
   at the transported canonical point although the full exact row vanishes.

5. **Higher Bockstein tower alone ⇒ full \(\chi\).**
   Higher Bocksteins may encode lifting depth, but no q-blind character-valued factorization has been established; candidate-twisted coefficient systems are circular as input.

6. **Full associated-graded tower ⇒ full \(\chi\).**
   Extension/gluing information is missing.

7. **Universal bounded-degree + bounded 3-adic precision ⇒ full \(\chi\).**
   The family \(q=3^s\) defeats every fixed degree/precision bound.

8. **Quotient compression of the exact local Fox algebra.**
   Since the local algebra is \(\mathbf Z_3\), quotienting it cannot produce a strictly smaller full-3-adic-preserving carrier.

---

## 4. What has NOT been proved

These are deliberately still OPEN.

1. **Information-theoretic minimality of \(P_3\).**
   We proved that some non-graded information is necessary and that \(P_3+R_2\) is sufficient for mod 9. We did **not** prove that \(P_3\) is the unique/minimal possible extension datum.

2. **Absolute minimality of \(\overline J_3\) among arbitrary carrier categories.**
   It is coarsest in the explicitly defined quotient-observable category, not universally minimal among every imaginable non-quotient construction.

3. **A genuinely intrinsic exact finite-level carrier \(J_{27}\).**
   This is the next decisive Gate.

4. **A compatible intrinsic tower \(J_{3^{n+1}}\to J_{3^n}\).**

5. **An intrinsic inverse-limit carrier strictly smaller than full Fox/presentation data.**

6. **A theorem that full orientation intrinsically requires “characteristic-zero information” in an absolute category-independent sense.**
   The current no-go statements establish precise boundaries, not this global claim.

7. **A non-tautological intrinsic factorization from filtered extension data to the exact Fox coefficient tower.**

---

## 5. Why the next task is mod 27

Mod 9 is no longer the right stress point: it is already solved by \(\overline J_3\).

The first genuinely informative question is therefore:
\[
\boxed{\text{Does there exist a q-blind intrinsic }J_{27}\text{ recovering }\chi\bmod27?}
\]

The Gate requires simultaneously:

- **Input:** \(J_{27}=J_{27}(G)\), defined without the unknown \(\chi\).
- **Intrinsicity:** independent of presentation, Nielsen/free-basis choice, relator gauge, and auxiliary coordinates.
- **Separation:** \(J_{27}\Rightarrow\chi\bmod27\).
- **Compatibility:** a natural map \(J_{27}\to J_9\) reducing to the already established mod-9 carrier.
- **Non-circularity:** the object may not simply be “Fox equations modulo 27” renamed.
- **Compression:** if it claims to improve on Fox, the structural information retained must actually be smaller, not merely re-encoded.

### Stop rule

If the definition fails before intrinsicity is even meaningful, record **FAIL / CLOSED** immediately.

If a candidate survives definition but fails Nielsen/gauge invariance, **FAIL / CLOSED**.

If it is intrinsic but does not separate mod 27, **FAIL / CLOSED**.

Only a candidate passing all gates earns a continuation to \(3^4\) and beyond.

---

## 6. Overall research map at this moment

\[
\boxed{
\operatorname{gr}_3G
\;\xrightarrow{\text{q-blind}}\;
\text{FAIL}
}
\]

\[
\boxed{
\overline J_3=[(R,p)]
\;\xrightarrow{}\;
\chi\bmod9
\quad\text{PASS}
}
\]

\[
\boxed{
J_{27}
\;\xrightarrow{?}\;
\chi\bmod27
\quad\text{OPEN — NEXT GATE}
}
\]

\[
\boxed{
\{J_{3^n}\}_{n\ge2}
\;\xrightarrow{?}\;
\chi
\quad\text{OPEN}
}
\]

\[
\boxed{
\text{full compatible filtered extension tower}
\;\xrightarrow{\text{inverse limit}}
\chi
\quad\text{PASS / LOCAL, but not compressed}
}
\]

\[
\boxed{
\text{exact Fox carrier}
\;\xrightarrow{}
\chi
\quad\text{PASS}
}
\]

\[
\boxed{
\text{intrinsic strict compression of Fox}
\quad\text{OPEN}
}
\]

### Strategic conclusion

The project is not at a dead end and is not entitled to claim the stronger “full Fox is necessary/minimal” conclusion. The strongest defensible statement now is:

> **The complete mod-3 associated graded loses the orientation; the first non-graded degree-(2,3) extension layer recovers the mod-9 orientation; the full compatible filtered extension tower is sufficient by inverse limit; exact Fox data recovers the full character; and the unresolved mathematical problem is whether the higher 3-adic extension information admits a genuinely intrinsic, presentation-natural, non-tautological compression.**

The next move is therefore **mod 27 intrinsic-carrier existence/no-go**, not another broad scan and not another attempt to optimize the already closed Fox quotient.
