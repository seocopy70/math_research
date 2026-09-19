# HARD ATTACK 9 — EXACT FOX CARRIER TO INTRINSIC MOD-9 CARRIER — 2026-09-19

## Target

After closing the Fox-row identification theorem, the next question is whether the intrinsic mod-9 carrier already obtained in the filtered program is the first nontrivial reduction of the exact Fox orientation equation.

This is a sharper question than asking whether both methods recover the same numerical character.

## 1. Normalize the exact q=3 Fox equations

Use
\[
A=1+3a,\qquad B=1+3b,\qquad C=1+3c,\qquad D=1+3d.
\]

For the projective exact Fox ideal, use
\[
F_1=B(1+A)+A^2,
\quad F_2=A-1,
\quad F_3=D-1,
\quad F_4=C-1.
\]

Direct expansion gives
\[
F_1=3+6b+9a+9a^2+9ab,
\]
hence
\[
\frac{F_1}{3}\equiv 1+2b\pmod3.
\]

Likewise
\[
\frac{F_2}{3}=a,\qquad
\frac{F_3}{3}=d,\qquad
\frac{F_4}{3}=c.
\]

Therefore the exact Fox zero condition modulo 9 is precisely
\[
a=c=d=0,\qquad 1+2b=0\pmod3.
\]

Equivalently
\[
(A,B,C,D)\equiv(1,4,1,1)\pmod9.
\]

## 2. Match with the intrinsic relation-jet carrier

The intrinsic degree-(2,3) carrier was already shown to have
\[
R=[X_1,X_2]+[X_3,X_4],
\qquad
p(P_3)=X_1^{(1)}
\]
for q=3, and its recovery functional
\[
\Theta(\lambda)(f)=f(p(P_3))+ (\lambda\wedge f)(R)
\]
has the unique zero
\[
\lambda=e_2^*.
\]

In the frozen basis, writing the first 3-adic character digit as
\[
\chi(x_i)=1+3a_i,
\]
the zero condition is
\[
a_1=a_3=a_4=0,\qquad a_2=1\pmod3.
\]

This is exactly the same system obtained above from the normalized exact Fox equations.

Thus the Fox reduction is not merely numerically compatible with the mod-9 carrier: its first nontrivial 3-adic normalized obstruction is the same degree-(2,3) functional.

## 3. Why this is non-circular

The exact Fox carrier and the intrinsic relation-jet carrier were constructed by different routes:

- Fox side: characteristic-zero crossed-derivation/Fox calculus plus the canonical Demuškin orientation theorem.
- Filtered side: Zassenhaus/relation-jet, cup+Bockstein identification, and the projective degree-(2,3) gauge quotient.

The equality occurs only after independently computing both sides.

The Fox calculation therefore supplies a characteristic-zero realization of the first filtered obstruction rather than defining the filtered carrier by fiat.

## 4. Presentation dependence

For the two Nielsen transformations already audited, the exact Fox row transports by the evaluated Fox Jacobian, and the normalized mod-9 zero transports with it.

The intrinsic mod-9 carrier is independently presentation/gauge invariant at the recovery-functional level.

Therefore the two constructions agree in the tested presentation changes, not just in the frozen normal form.

A general theorem that the exact Fox filtration/initial-form construction canonically equals the abstract relation-jet functor for every minimal presentation is still stronger than what has been proved.

## 5. New status

- exact Fox row = canonical orientation criterion: **PASS / CLOSED**.
- exact Fox q=3 row-zero equations: **PASS / CLOSED**.
- first normalized Fox obstruction modulo 9 = intrinsic mod-9 recovery functional: **PASS / CLOSED for the frozen q=3 carrier and tested coordinate changes**.
- general natural identification of the full exact Fox filtered object with the intrinsic relation-jet functor: **OPEN**.
- full \(3\)-adic filtered-to-Fox factorization at every level n: **OPEN**.

## 6. Next attack

The next useful attack is not another finite computation. It is to formulate the exact finite-level Fox condition
\[
J_r(\rho)\equiv0\pmod{3^n}
\]
as a functorial coefficient-level object and compare its successive normalized associated-graded layers with the compatible filtered relation-jet tower.

The decisive question is:

\[
\boxed{
\text{Does the exact Fox coefficient tower admit a canonical filtered realization,
without defining the filtered object from Fox evaluations themselves?}
}
\]

If yes, the project obtains a genuine bridge from intrinsic filtered data to the full \(3\)-adic orientation. If no, the precise obstruction will be the dependence of higher coefficient layers on characteristic-zero crossed-derivation data not retained by the filtered relation tower.
