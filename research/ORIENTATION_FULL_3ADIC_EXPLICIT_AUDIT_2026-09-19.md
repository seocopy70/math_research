# FULL 3-ADIC ORIENTATION — EXPLICIT CROSSED-DERIVATION AUDIT — 2026-09-19

## Goal

Replace the abbreviated coefficient statement in the hand derivation by an explicit calculation, so the claim that the same equation determines every finite 3-adic digit is independently checkable.

## 1. Crossed inverse and commutator formulas

Let \(A=\mathbf Z_3\) with action \(g\cdot z=\rho(g)z\), and write
\[
\rho(x_i)=r_i,\qquad D(x_i)=f_i.
\]
From
\[
D(g^{-1})=-\rho(g)^{-1}D(g)
\]
and \([x,y]=x^{-1}y^{-1}xy\), one obtains
\[
D([x,y])
=x^{-1}\text{-coefficient}\;\rho(x)^{-1}(\rho(y)^{-1}-1)D(x)
+\rho(y)^{-1}(1-\rho(x)^{-1})D(y),
\]
that is, for \(a=\rho(x),b=\rho(y)\),
\[
D([x,y])=a^{-1}(b^{-1}-1)D(x)+b^{-1}(1-a^{-1})D(y).
\]

Also
\[
D(x^3)=(1+a+a^2)D(x).
\]

## 2. Apply to the defining relation

For
\[
r=x_1^3[x_1,x_2][x_3,x_4],
\]
use
\[
D(uvw)=D(u)+\rho(u)D(v)+\rho(uv)D(w).
\]
The coefficient of \(f_2\) is
\[
C_2=a^3\,b^{-1}(1-a^{-1}).
\]
Since \(a,b\) are units, \(C_2=0\) implies
\[
a=r_1=1.
\]

With \(a=1\), the coefficient of \(f_4\) is
\[
C_4=b\,d^{-1}(1-c^{-1}),
\]
so
\[
c=r_3=1.
\]
Then the coefficient of \(f_3\) is
\[
C_3=b\,c^{-1}(d^{-1}-1),
\]
so
\[
d=r_4=1.
\]

Finally, with \(a=c=d=1\), the coefficient of \(f_1\) is obtained directly from
\[
D(x_1^3)=3f_1,
\qquad
D([x_1,x_2])=(b^{-1}-1)f_1,
\]
so
\[
C_1=3+b^{-1}-1=2+b^{-1}.
\]
Thus
\[
2+b^{-1}=0,
\qquad
b=-\frac12=(1-3)^{-1}.
\]

This is an exact identity in \(\mathbf Z_3\), not a finite-level congruence.

## 3. Finite levels

Reducing the same identity modulo \(3^n\) gives uniquely
\[
\rho_n(x_1)=\rho_n(x_3)=\rho_n(x_4)=1,
\qquad
\rho_n(x_2)=(-2)^{-1}\pmod{3^n}.
\]
The first values are
\[
4\pmod9,\quad13\pmod{27},\quad40\pmod{81},\quad121\pmod{243}.
\]
No new independent digit-by-digit obstruction is required for the fixed \(q=3\) relation.

## 4. Logical scope

This calculation proves uniqueness of the crossed-derivation character satisfying the defining relation in the fixed q=3 normal form. To identify that character with the **canonical Demuškin orientation**, one still invokes the standard intrinsic characterization/uniqueness theorem for the canonical orientation. Literature independently describes the canonical orientation of infinite Demuškin pro-p groups and its role as a group invariant.

Therefore the strongest exact statement is:

\[
\boxed{\text{fixed q=3 filtered relation + canonical orientation characterization}
\Longrightarrow\text{full }\chi.}
\]

It is not a proof that the finite degree-(2,3) carrier alone contains all higher digits.

## 5. Status

- Explicit crossed-derivation equations: **PASS / CLOSED**.
- Full \(\mathbf Z_3\)-value for the frozen q=3 normal form: **PASS / CLOSED**, conditional only on the standard intrinsic canonical-orientation characterization.
- Full orientation from the degree-(2,3) jet alone: **OPEN / not claimed**.
- New independent higher obstruction at each digit: **NOT NEEDED for this fixed q=3 normal form**.
- Universal bounded finite-information carrier: **IMPOSSIBLE in the stated family**, by the q=3^s degree/precision obstruction.
