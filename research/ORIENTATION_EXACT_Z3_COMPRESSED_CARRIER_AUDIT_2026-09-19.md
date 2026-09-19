# ORIENTATION — EXACT Z_3 COMPRESSED CARRIER AUDIT — 2026-09-19

## Goal

Test whether the mod-3 compressed carrier
\[
\overline J_3=[(R,p(P))]
\]
has a genuine exact \(\mathbf Z_3\)-analogue that recovers the full q=3 orientation.

## 1. First obstruction: do not naively replace F_3 by Z_3 in the restricted-Lie construction

The mod-3 quotient
\[
L^{res}_3(V)/[V,L_2(V)]\cong V^{(1)}
\]
uses the restricted Lie algebra structure in characteristic 3. A restricted Lie algebra, by definition, is a Lie algebra over a field of characteristic p equipped with a p-operation. The exact coefficient ring \(\mathbf Z_3\) is characteristic zero, so the phrase “restricted Lie algebra over \(\mathbf Z_3\)” is not the same structure and cannot be used as a formal coefficient lift.

Therefore the previous symbolic expression
\[
L^{res}_3(V_{\mathbf Z_3})/[V,L_2]\cong V^{(1)}
\]
must NOT be asserted as an established exact carrier.

This is a genuine mathematical boundary, not a cosmetic issue.

## 2. Correct exact replacement

The exact q=3 result already available is formulated through the filtered relation together with coefficient-level crossed-derivation evaluation. Therefore the correct exact carrier must be defined from the filtered relation module / augmentation filtration, not by a nonexistent \(\mathbf Z_3\)-restricted Lie algebra.

Let
\[
1\to N\to F\to G\to1
\]
be a minimal one-relator pro-3 presentation and let
\[
M=N/[F,N].
\]
The relation line is projective because changing the relator generator multiplies it by a unit.

At exact coefficient level, define the degree-(2,3) observable quotient of the relation jet by the common kernel of all coefficient evaluations used by the finite-level crossed-derivation conditions \(\mathcal C_n\). Equivalently, two exact jets are identified precisely when every admissible coefficient evaluation \(\mathcal C_n\) gives the same value for every \(n\) and every degree-one test datum.

This gives a canonical “evaluation quotient” without pretending that a restricted Lie algebra exists over \(\mathbf Z_3\).

## 3. What survives

The relator-conjugation term still has the form
\[
P\mapsto P+[v,R]
\]
at the first relevant filtered level, and degree-one evaluations kill the bracket contribution. Common unit scaling multiplies the whole coefficient functional by the same unit and therefore leaves its zero set unchanged.

Thus the projective/gauge mechanism survives.

However, unlike the mod-3 linear functional
\[
\Theta(\lambda)(f)=f(P)+(\lambda\wedge f)(R),
\]
the exact crossed-derivation coefficient condition is generally nonlinear in the orientation values. Therefore one cannot simply declare that the exact carrier is the pair \(([R],p(P))\) and reuse the same linear \(\Theta\).

## 4. Exact q=3 recovery

For the frozen q=3 relation
\[
r=x_1^3[x_1,x_2][x_3,x_4],
\]
the previously established exact hand derivation gives
\[
\rho(x_1)=\rho(x_3)=\rho(x_4)=1,
\qquad
1+2\rho(x_2)=0,
\]
hence
\[
\rho(x_2)=-\frac12=(1-3)^{-1}\in\mathbf Z_3^\times.
\]

Therefore the exact evaluation quotient is sufficient for full \(\chi\) **provided its defining observable family is taken to be the exact coefficient-level crossed-derivation family**.

## 5. Can the exact carrier be compressed further?

Yes, formally one can quotient by the common kernel of all \(\mathcal C_n\). But there is a serious categorical warning.

If the observable family is defined only as “whatever is needed to recover \(\chi\),” the resulting quotient is tautological. To retain mathematical content, the observable family must be fixed independently as the coefficient evaluations arising from the filtered relation and the natural crossed-derivation construction.

Thus the exact branch has a clean but weaker endpoint:

\[
\boxed{
\text{filtered relation jet}
\longrightarrow
\text{canonical exact evaluation quotient}
\longrightarrow
\{\chi_n\}_n
\longrightarrow
\chi.
}
\]

What is NOT yet proved is an equally concrete two-component formula
\[
\overline J^{ex}_3=[(R,p)]
\]
with a simple exact analogue of the mod-3 \(\Theta\).

## 6. Universal/minimal consequence

The mod-3 categorical theorem remains valid:

\[
J_3\twoheadrightarrow\overline J_3
\]
is the coarsest quotient preserving the full degree-one linear evaluation family.

The exact \(\mathbf Z_3\) problem is different. Its natural universal object is the coefficient-evaluation quotient, but proving that this quotient collapses to a finite concrete algebraic pair requires an additional theorem about the exact crossed-derivation coefficient maps.

## 7. Decision

### PASS / CLOSED

- The exact fixed-q=3 branch still recovers the full \(\chi\).
- The projective/gauge mechanism remains the correct invariance mechanism.
- An exact evaluation-quotient carrier can be defined without choosing a generator of the relation line.

### FAIL / CLOSED

- Naively defining an exact “restricted Lie degree-3 carrier over \(\mathbf Z_3\)” is invalid.
- The mod-3 compressed pair \(([R],p(P))\) cannot simply be promoted to \(\mathbf Z_3\) by scalar extension and the same linear \(\Theta\).

### OPEN — sharply isolated

The only remaining exact categorical question is:

> Does the exact coefficient-evaluation quotient admit a non-tautological finite/concrete description analogous to \(([R],p(P))\)?

This is now the correct next target. A successful proof would strengthen the fixed-q=3 full-orientation result. Failure would establish that the exact full-\(\chi\) carrier intrinsically requires the coefficient-evaluation tower rather than a finite two-component jet.
