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

## 2. Candidate, but not yet canonical recovery: mod-9 cup/Bockstein

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
Show that a **canonical, basis/trivialization-independent** construction from the mod-9 data distinguishes the orientation layer
\[
\chi(x_2)\equiv4\pmod9
\]
from the trivial lift \(1\) (and, where relevant, the other \(1+3\mathbf Z/9\) possibility \(7\)).

### M9-D
Only after A-C pass, compare the object with \(\chi\bmod9\).

## 5. Explicit warning

Do **not** reuse the failed rank-2 relator-unit scalar. That construction failed lift-independence. The new object must be canonical before any scan.

Do **not** infer that the mod-9 cup-product matrix automatically equals the orientation character. It only supplies a possible first-lift carrier.

## Critical-review status

The gate remains **OPEN**, but the candidate has been weakened. The following stronger claim is **NOT established**:

> mod-9 cup product automatically recovers \(\chi\bmod9\).

What is established is only that mod-9 finite-coefficient cohomology detects the q=3 power-term contribution of the defining relation. The recovery of the specific orientation value 4 requires an additional canonical construction and an ambiguity proof.

**No finite scan authorized.**

Next hand task: derive the Bockstein/finite-coefficient invariant explicitly and test whether it is invariant under change of (H^2)-generator and admissible basis/presentation changes. If it collapses to the q=3 torsion invariant without retaining the value 4, this route must be marked FAIL/CLOSED rather than upgraded by interpretation.

Next hand task: derive the mod-9 cup/Bockstein structure of the frozen \(q=3\) Demushkin presentation and test whether its first \(3\)-adic coefficient canonically determines \(\chi\bmod9\).


## 2026-09-19 — Bockstein audit result

The explicit next hand task was completed in `research/ORIENTATION_MOD9_BOCKSTEIN_AUDIT_2026-09-19.md`.

Using
\[
0\to\mathbf F_3\xrightarrow{3}\mathbf Z/9\to\mathbf F_3\to0,
\]
the intrinsic Bockstein
\[
\beta:H^1(G,\mathbf F_3)\to H^2(G,\mathbf F_3)
\]
was derived for the frozen relation. It detects the unique q=3 power-term direction:
\[
\beta(\gamma_1)\neq0,qquad
\beta(\gamma_2)=\beta(\gamma_3)=\beta(\gamma_4)=0
\]
up to the fixed top-class/sign convention.

The candidate passes canonicality/intrinsicity but fails the recovery requirement. Its invariant content is the q=3 power/torsion shadow; it does not canonically retain
\[
\chi(x_2)\equiv4\pmod9.
\]
A scalar coordinate also depends on a generator choice for the one-dimensional (H^2) target.

### Gate decision

- **M9-A: PASS**
- **M9-B: PASS**
- **M9-C: FAIL**
- **M9-D: CLOSED for the ordinary mod-9 Bockstein candidate**

This does not establish impossibility of all finite-coefficient or twisted constructions. It closes only this candidate. No finite scan is authorized.

The next route, if opened, must retain additional (1+3\mathbf Z_3)-valued/twisted-dualizing information rather than reinterpreting the Bockstein's q=3 signal as the orientation value.