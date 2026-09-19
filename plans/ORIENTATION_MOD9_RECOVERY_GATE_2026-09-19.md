# ORIENTATION MOD-9 RECOVERY GATE — 2026-09-19

## Objective

Return to the original target after closing the \(\mu\)-bridge: determine whether the first nontrivial \(3\)-adic orientation layer
\[
\chi\bmod 9:G\to(\mathbf Z/9)^\times
\]
can be recovered from canonical filtered/graded or first-lift data.

For the frozen \(q=3\) presentation,
\[
\chi(x_1)=\chi(x_3)=\chi(x_4)=1,\qquad
\chi(x_2)=(1-3)^{-1}\equiv4\pmod9.
\]

The mod-3 reduction is trivial, so any successful observable must live one layer above the ordinary \(\mathbf F_3\)-graded data.

## 1. Important distinction

The previous \(\mu\)-observable is now understood as a canonical \(\operatorname{Aut}(G)\)-character on the top-duality line, and for \(p=3\) agrees with its inverse automatically. It does not contain the \(1+3\mathbf Z_3\) information of \(\chi\).

Therefore the next target is not another mod-3 automorphism scalar.

## 2. Canonical candidate: first coefficient lift

A natural first candidate is the mod-9 cohomological lift of the Demushkin duality pairing. For a one-relator pro-\(p\) presentation, the cup-product matrix with coefficients \(\mathbf Z/p^m\) is controlled by the Magnus/Fox coefficients of the defining relation. Literature records, for a standard relation, that the coefficients of the relation determine the cup-product matrix over \(\mathbf Z/p^m\), including the diagonal contribution from the power \(x_1^q\). citeturn0search5turn1search4

For \(q=3\), the first nonzero lift beyond mod 3 is therefore expected to appear at mod 9. This is only a candidate mechanism at this gate, not yet a proved recovery theorem.

## 3. Intrinsic orientation characterization

The canonical orientation of a Demushkin/PD2 group is characterized by the dualizing module. A general PD2 criterion states that a character \(\rho:G\to\mathbf Z_p^\times\) equals the orientation exactly when the corresponding twisted top cohomology has the correct size at every \(p^m\)-level. citeturn1search1

Thus there is a rigorous intrinsic target:
\[
\rho=\chi
\quad\Longleftrightarrow\quad
|H^2(G,I_m(\rho))|=p^m
\quad\text{for every }m.
\]

This criterion is not itself a filtered/graded recovery, but it identifies precisely what a successful first-lift construction must reproduce.

## 4. What must be proved before computation

### M9-A
Define the canonical first-lift object using only data already admitted by the project (filtered group / Magnus data / cohomological lift), with no chosen free lift of an automorphism.

### M9-B
Prove that its mod-3 shadow is the known Demushkin pairing and that its first nontrivial \(3\)-adic coefficient is well-defined under all presentation/lift ambiguities already known to cause failures.

### M9-C
Show that the coefficient distinguishes the orientation layer
\[
\chi(x_2)\equiv4\pmod9
\]
from the trivial lift \(1\) (and, where relevant, the other \(1+3\mathbf Z/9\) possibility \(7\)).

### M9-D
Only after A-C pass, compare the object with \(\chi\bmod9\).

## 5. Explicit warning

Do **not** reuse the failed rank-2 relator-unit scalar. That construction failed lift-independence. The new object must be canonical before any scan.

Do **not** infer that the mod-9 cup-product matrix automatically equals the orientation character. It only supplies a possible first-lift carrier.

## Gate status

**OPEN. No finite scan authorized.**

Next hand task: derive the mod-9 cup/Bockstein structure of the frozen \(q=3\) Demushkin presentation and test whether its first \(3\)-adic coefficient canonically determines \(\chi\bmod9\).
