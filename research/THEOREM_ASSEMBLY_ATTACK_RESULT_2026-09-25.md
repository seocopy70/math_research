# THEOREM ASSEMBLY ATTACK — CORRECTED ZASSENHAUS WINDOW — 2026-09-25

## Scope
Assembly-level attack on the complete theorem, not another independent U1/U2/U3/U4/U5 repetition.

Target:
\[
\mathsf K_k(Q_k,\rho)\Longleftrightarrow\rho=\chi_G\pmod{3^k},
\qquad Q_k=G/P_{3^{k-1}+1}(G),\quad k\ge2.
\]

## 1. Dependency DAG
\[
\boxed{\text{actual Zassenhaus calculation}}
\to
\boxed{\text{U2 twisted factorization}}
\to
\boxed{\mathsf K_k(G,\rho)\iff\mathsf K_k(Q_k,\bar\rho)}
\]
together with
\[
\boxed{\text{U3 finite Fox criterion}}
\to
\boxed{\text{U4 base case }k=2}
\]
and independent classical existence
\[
\boxed{\chi_G\text{ is Kummerian}}
\to
\boxed{\chi_G\bmod3^k\text{ satisfies the finite predicate}},
\]
followed by
\[
\boxed{\text{U5 reduction + variation + PD}^2+\cup\text{-nondegeneracy}}
\to
\boxed{\text{higher-level uniqueness}}
\to
\boxed{\text{main theorem}}.
\]

U5 does not create existence. Existence is imported independently from classical Demushkin theory.

## 2. Finding A — corrected Zassenhaus window
The older research U1 file proves the analogous statement for the lower 3-central series and cannot by itself justify the corrected Zassenhaus window.

The repaired manuscript now uses the Jennings–Lazard description
\[
P_n(S_k)=\prod_{i3^j\ge n}\gamma_i(S_k)^{3^j}.
\]
For \(S_k=A_k\rtimes U_1\),
\[
\gamma_2(S_k)=3A_k,\qquad
\gamma_i(S_k)=3^{i-1}A_k\ (i\ge2),
\]
and
\[
S_k^{3^j}=3^jA_k\rtimes U_{j+1}.
\]
Thus
\[
P_n(S_k)=3^{e(n)}A_k\rtimes U_{e(n)+1},
\qquad e(n)=\lceil\log_3 n\rceil,
\]
and hence
\[
P_{3^{k-1}}(S_k)=3^{k-1}A_k\ne1,\qquad
P_{3^{k-1}+1}(S_k)=1.
\]

**Verdict: PASS / REPAIRED.**

## 3. Finding B — hidden target H1 identification
U2 gave the twisted isomorphism
\[
H^1(Q_k,A_k(\bar\rho))\cong H^1(G,A_k(\rho)),
\]
but the predicate also targets \(H^1(-,\mathbf F_3)\).

Because
\[
P_{3^{k-1}+1}(G)\subseteq P_2(G)=\Phi(G),
\]
inflation gives
\[
H^1(Q_k,\mathbf F_3)\xrightarrow{\sim}H^1(G,\mathbf F_3).
\]
Naturality of coefficient reduction gives the required commutative square.

**Verdict: PASS / REPAIRED.**

This was a genuine hidden assembly dependency.

## 4. Finding C — U3/U4 quantifier direction
U3 applies to an arbitrary candidate, not only to the canonical orientation. U4 is used only for the \(k=2\) base case. The superseded all-\(k\) coordinate recurrence is not needed.

**Verdict: PASS.**

## 5. Finding D — U5 circularity
The dangerous possible cycle
finite predicate → canonical branch → PD2 injectivity → uniqueness → finite predicate
does not occur.

PD2 uses the independently known canonical dualizing orientation only inside the injectivity lemma. The induction hypothesis supplies the canonical lower-level branch. No conclusion of the desired theorem is used to prove PD2 injectivity.

**Verdict: PASS — no fatal circularity found.**

## 6. Finding E — U5 connecting-map logic
For
\[
0\to A_{k-1}(\rho_{k-1})\to A_k(\rho_k)\to\mathbf F_3\to0,
\]
surjectivity of the lifting map is equivalent to vanishing of its connecting map
\[
\delta_{\rho_k}:H^1(G,\mathbf F_3)\to H^2(G,A_{k-1}(\rho_{k-1})).
\]
The variation identity, PD2 socle injection, and cup-product nondegeneracy then force the next digit difference \(\nu\) to vanish.

**Verdict: PASS.**

## 7. Finding F — existence/uniqueness separation
Existence comes from classical Kummerianity of \(\chi_G\), then U1/U2 transfer its finite lifting problem to \(Q_k\). Uniqueness comes from U4 at \(k=2\) and U5 at higher levels.

**Verdict: PASS.**

## 8. Finding G — q-blindness
The selector input is only \((Q_k,\rho)\). It contains no q, presentation, relator, Fox coordinates, or pre-supplied canonical orientation. This is q-blindness of the input definition, not q-uniformity of the theorem.

**Verdict: PASS.**

## 9. Finding H — minimality
The proof establishes sufficiency of
\[
Q_k=G/P_{3^{k-1}+1}.
\]
It does not prove minimality.

**Verdict: PASS with minimality OPEN.**

## 10. Finding I — prior art
Canonical Demushkin orientation and global Kummerian characterization are classical. The remaining publication question is whether the exact bare finite quotient, arbitrary-candidate selector and automatic factorization formulation is already an equivalent corollary somewhere in the literature.

**Verdict: OPEN / CONDITIONAL novelty.**

## 11. Final assembly verdict

Fatal circularity: **NONE FOUND.**

Fatal mathematical contradiction in the current assembly: **NONE FOUND.**

Real hidden dependency: **YES — target H1 identification; repaired.**

Real filtration risk: **YES — older research U1 was lower 3-central; repaired manuscript now uses actual Zassenhaus/Jennings–Lazard calculation.**

Current status:
\[
\boxed{\text{THEOREM ASSEMBLY: PASS / PROVISIONAL}}
\]

This is not yet submission-level closure. A fresh line-by-line audit of the repaired manuscript and a clean LaTeX build remain mandatory.

## 12. Next authorized gate
1. Re-read repaired paper/main.tex from line 1.
2. Check every displayed map's domain/codomain.
3. Check every filtration index against \(P_{3^{k-1}+1}\).
4. Independently rederive the U1 boundary values.
5. Recheck U5 PD2 dual modules and reduction map.
6. Clean LaTeX build.
7. Only then classify manuscript proof status as submission-ready.

No new Fox computation was authorized or performed.
