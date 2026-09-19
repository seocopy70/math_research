# Q3/Q9 — S9 degree-9 source-map definition gate

Date: 2026-09-19

## Status

**OPEN — definition only; no downstream invariant computation authorized.**

This gate follows Gate C (first source degree 9) and the closed S9 H-stability / C3 provenance failures.

## 1. Purpose

Define, before any new numerical invariant, a mathematically typed map from the presentation-derived source

\[
S_9=X_1^{[9]}=\Delta_9(9)
\]

to a target that is already determined by the frozen baseline construction.

The purpose is to prevent an implicit reuse of the degree-3 N/J construction and to keep the non-H-stable source line separate from the H-stable target.

## 2. Frozen input

The following are inputs, not hypotheses to be recomputed here:

\[
\dim (I_\infty)_9=13524,
\qquad
L_9^{res}=L_9\oplus L_3^{[3]}\oplus L_1^{[9]},
\]

\[
S_9=X_1^{[9]}\in L_1^{[9]},
\qquad
S_9\notin(I_\infty)_9,
\]

and

\[
\Delta_9(9)=S_9.
\]

The naive q=9 relation space is **not** an H-module, and the H-closure
\(\langle H\cdot S_9\rangle\) is not a valid replacement for the fixed
q=9 presentation.

## 3. Target convention

The first admissible target is the **frozen baseline quotient**

\[
Q_9^{\infty}:=L_9^{res}/(I_\infty)_9.
\]

This target is defined without inserting \(S_9\), and therefore does not alter the q=∞ baseline.

Because the baseline relation is generated from the H-invariant quadratic relation \(R_2\), the induced H-action on \(Q_9^{\infty}\) is the relevant target-side action. This H-stability must still be checked explicitly in the implementation gate; it is not assumed merely because the notation is natural.

## 4. Source-map convention

The source object is deliberately **not** declared to be an H-module.

Define the one-dimensional source line

\[
E_9:=\langle S_9\rangle
\]

only as an \(\mathbf F_3\)-vector space, and define

\[
\phi_9:E_9\longrightarrow Q_9^{\infty},
\qquad
\phi_9(S_9)=[S_9].
\]

S9-B guarantees that \(\phi_9\) is nonzero.

No H-equivariance statement for \(\phi_9\) is made or required: the source line is not H-stable.

## 5. Derived target-side object

The first target-side H-stable object allowed by this definition is the orbit span

\[
\mathcal O_9:=\langle H\cdot\phi_9(S_9)\rangle
\subseteq Q_9^{\infty},
\]

provided the induced H-action on \(Q_9^{\infty}\) passes the implementation audit.

This is a target-side construction. It is **not** the same object as the fixed q=9 relation space and must not be interpreted as adding H-closed relations to the presentation.

## 6. Required definition audit before computation

A PASS requires all of the following:

1. **Target well-definedness:** \((I_\infty)_9\) is exactly the frozen baseline relation space used for the quotient.
2. **H-action:** every generator of the fixed H-action preserves \((I_\infty)_9\), so the quotient action on \(Q_9^{\infty}\) is well-defined.
3. **Coordinate compatibility:** the representative of \(S_9\) and the quotient coordinates use the same frozen restricted-layer convention.
4. **Source nonzero:** \(S_9\notin(I_\infty)_9\), already supplied by S9-B.
5. **No hidden q=9 insertion:** the target and its action are constructed from the q=∞ baseline only.
6. **No inherited N/J definition:** no degree-3 \(N\), \(d_3\), or previously defined \(J\) object is silently reused.

## 7. Pass/fail consequence

### PASS

The map \(\phi_9\) and target action are well-defined under the frozen conventions. Only then may \(\mathcal O_9\) and a separately preregistered target-side invariant be computed.

### FAIL

If the target action or quotient convention is not well-defined, this source-map route is blocked. Do not repair it by inserting the artificial H-closure of \(S_9\), by modifying \((I_\infty)_9\), or by importing the degree-3 N/J map.

## 8. Critical boundary

This gate does **not** claim that \(\mathcal O_9\) is canonical in the broader sense, that it distinguishes q=3 from q=∞, or that it recovers the orientation character.

Those are separate questions.

The immediate task is only to audit the typed source map and its H-stable target.

## 9. Execution order

\[
\boxed{
\text{target/action audit}
\to
\text{source-map audit}
\to
\text{Gate PASS/FAIL}
\to
\text{only then compute }\mathcal O_9
}
\]

