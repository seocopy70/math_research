# ORIENTATION MOD-9 — INDEPENDENT TWISTED-RECOVERY / CARRIER FACTORIZATION AUDIT — 2026-09-19

## Purpose

Independently audit the previously obtained
\[
\chi\pmod 9=(1,4,1,1)
\]
without using the trivial-coefficient Bockstein as the recovery criterion.

The independent criterion is the canonical twisted-surjectivity condition
\[
H^1(G,\mathbf Z/9(\rho))\longrightarrow H^1(G,\mathbf F_3)
\]
being surjective, where \(\rho:G\to1+3\mathbf Z/9\).

The key question is then whether the resulting obstruction functional is exactly the already-defined degree-(2,3) functional \(\Theta\), rather than merely giving the same answer in one presentation.

## 1. Direct mod-9 character check

For
\[
\rho(x_i)=1+3a_i\pmod9,
\]
the frozen relator
\[
r=x_1^3[x_1,x_2][x_3,x_4]
\]
gives, for a mod-3 cocycle with generator values \(f_i\),
\[
z(r)/3
=
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4
\in\mathbf F_3
\]
under the frozen commutator/transgression convention.

Therefore every mod-3 class lifts iff
\[
1-a_2=a_1=a_3=a_4=0.
\]
The unique solution is
\[
(a_1,a_2,a_3,a_4)=(0,1,0,0),
\]
so
\[
\rho=(1,4,1,1)\pmod9.
\]

This calculation does not use the Bockstein map.

## 2. Independent verification of the defining relation

For \(\rho=(1,4,1,1)\), the target is abelian, hence
\[
\rho([x_1,x_2])=\rho([x_3,x_4])=1.
\]
Also
\[
\rho(x_1)^3=1.
\]
Thus
\[
\rho(r)=1,
\]
as required.

This is a consistency check, not the recovery argument.

## 3. Exact identification of the twisted obstruction with Theta

Write
\[
R=[X_1,X_2]+[X_3,X_4],\qquad p=X_1^{(1)}.
\]
For \(\lambda=\sum a_i e_i^*\), define
\[
\Theta_{(R,p)}(\lambda)(f)
=
f(p)+(\lambda\wedge f)(R).
\]
Direct evaluation gives
\[
\Theta_{(R,p)}(\lambda)(f)
=
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4.
\]

Hence the twisted-surjectivity obstruction functional is exactly
\[
\boxed{\Theta_{(R,p)}}.
\]

This is stronger than merely observing that both methods recover the same coordinate vector: the twisted lifting condition factors through the same projective degree-(2,3) carrier.

## 4. Gauge/sign check

The twisted-surjectivity condition is a vanishing condition, so multiplying the obstruction by a nonzero common scalar does not change its zero set.

The projective carrier uses the same common transgression/H² normalization for \(R\) and \(p\). Therefore the previously frozen warning remains essential:

- \(R\mapsto uR\) and \(p\mapsto up\) together leave the zero set unchanged;
- \(p\mapsto-p\) with \(R\) fixed is not a gauge transformation.

Thus the independent twisted route is compatible with the already-closed sign synchronization.

## 5. Consequence for the filtered-carrier question

The twisted criterion is intrinsically defined at the group/cohomology level, while the projective relation carrier was already shown to be obtained from cup product plus Bockstein, with the relation-jet identification justified by the standard one-relator transgression/Bockstein formula.

The direct equality
\[
\boxed{
\text{twisted mod-9 lifting obstruction}
=
\Theta_{[(R,p)]}
}
\]
therefore supplies the missing factorization bridge at the first nontrivial 3-adic level:

\[
\text{projective degree-(2,3) carrier}
\longrightarrow
\text{twisted-surjectivity criterion}
\longrightarrow
\chi\pmod9.
\]

No preferred free lift, Nielsen lift, or H² generator is required by the criterion itself.

## 6. Critical boundary

This audit does **not** prove that the twisted-surjectivity object is recoverable from the bare Zassenhaus restricted graded Lie algebra.

It does establish a stronger result for the already-admitted enriched carrier: the independent twisted-cohomological orientation criterion is represented exactly by the same \(\Theta\) functional.

Thus the former T9-D question is closed **at the projective degree-(2,3) carrier level**, while the stronger bare-graded factorization problem remains open/closed according to its existing separate gate.

No broad finite scan was used or authorized.

## Decision

- Independent twisted-surjectivity recovery: **PASS / CLOSED**.
- Direct relation verification: **PASS**.
- Equality of twisted obstruction and \(\Theta\): **PASS / CLOSED**.
- Factorization through the projective degree-(2,3) carrier: **PASS / CLOSED**.
- Recovery from bare associated graded alone: **NOT ESTABLISHED**.
- Higher 3-adic digits: **OPEN / separate program**.
