# PAPER 4 — GATE T1-C A=1 INDEPENDENT CLOSURE AUDIT — 2026-10-03

## Scope

This audit independently closes the previously unresolved boundary a=1 for the declared rank-two stress family
\[
G_{s,1}=\langle z,x,y\mid z^{p^s}=x^p[x,y]\rangle,
\qquad p\text{ odd},\ s\ge1.
\]
The result is about the **marked/relative finite-window problem**. It does not establish recovery from the unmarked abstract filtered group.

## 1. Lower bound

For every n\le p^s, the defining defect z^{p^s} lies in the p-Zassenhaus layer D_{p^s}, hence is invisible modulo D_n. The generator-lift map therefore gives a section of the relative quotient
\[
G_{s,1}/D_n(G_{s,1})\to D/D_n(D).
\]
Thus no relative separation occurs before p^s+1.

## 2. New a=1 pushout witness

Define a finite abelian p-group A by generators x,z and relations
\[
z^{p^{s+1}}=1,\qquad p x=p^s z
\]
(in additive notation), and let y act by
\[
yzy^{-1}=z^{1-p},\qquad yxy^{-1}=x.
\]
The relation is compatible with the action because
\[
p((1-p)z)=p^s z-p^{s+1}z=p^s z=px.
\]
Take y of order p^s; for odd p, (1-p)^{p^s}\equiv1\pmod{p^{s+1}}, so this defines a finite semidirect product
\[
H_s=A\rtimes\langle y\rangle.
\]
In multiplicative notation,
\[
x^p[x,y]=z^{p^s},
\]
because x is y-fixed and x^p=z^{p^s}. Hence there is a surjection
\[
G_{s,1}\twoheadrightarrow H_s.
\]

## 3. Exact critical filtration in the witness

The subgroup A is abelian and
\[
[y,z]=z^{-p},\qquad [y,x]=1.
\]
Consequently
\[
\gamma_i(H_s)\subseteq\langle z^{p^{i-1}}\rangle\quad(i\ge2).
\]
Using the Jennings-Zassenhaus formula
\[
D_n(H_s)=\prod_{i p^j\ge n}\gamma_i(H_s)^{p^j},
\]
and the elementary odd-p inequality
\[
i p^j\ge p^s+1,\quad i\ge2
\ \Longrightarrow\ i-1+j\ge s+1,
\]
every factor on the right is trivial at n=p^s+1. The A^{p^s} factor is also killed because z has order p^{s+1} and the relevant gamma/power index is p^s. Hence
\[
D_{p^s+1}(H_s)=1.
\]
But
\[
(y-1)^s z=(-p)^s z=\pm p^s z\ne0
\]
because z has order p^{s+1}. In particular z^{p^s}\ne1, so
\[
z^{p^s}\notin D_{p^s+1}(G_{s,1}).
\]
This independently verifies critical-layer survival for a=1.

## 4. Section-change obstruction

For
\[
r=x^p[x,y],
\]
the Fox derivatives are
\[
f_x=N_p(x)+x^p-y,\qquad f_y=x^{p+1}-1.
\]
In the pure Y-associated-graded direction (X=x-1 set to zero), this becomes
\[
f_x\mapsto p-Y,\qquad f_y\mapsto0.
\]
Therefore cancellation of the critical defect p^s\bar z by an integral section change would force, successively in Y-degree,
\[
(p-Y)A(Y)=p^s.
\]
The formal solution is
\[
\frac{p^s}{p-Y}=p^{s-1}\sum_{j\ge0}p^{-j}Y^j.
\]
The coefficient of Y^s is p^{-1}, hence no integral A(Y) exists. Equivalently, after all lower-order integral lift changes have been made, a nonzero Y^s residual remains modulo p.

The witness H_s detects this residual because Y acts on z as -p, so
\[
Y^s z=(-p)^s z\ne0.
\]
Thus the obstruction is not merely formal: it survives an actual quotient of the finite kernel. By naturality/pushout, the original relative extension class is nonzero.

## 5. Exact threshold

Combining the lower bound and the critical nonsplitting:
\[
\boxed{n_{\rm sep}^{\rm rel}(s)=p^s+1}
\]
for the rank-two a=1 stress family.

The same rank-two factor is the authorized stress quotient for the even-rank family; extra Demuškin generators may be sent into the abelian kernel so their extra commutators vanish. Therefore the rank-two result supplies the corresponding higher-rank stress-family obstruction, subject to the declared quotient/naturality formulation.

## 6. Independent verification boundary

The proof does **not** use the invalid cyclic-quotient argument. The depth statement is checked in a nonabelian finite semidirect witness using the Zassenhaus product formula. It also does not identify the metabelian witness with the actual kernel; it is used only as a functorial quotient/pushout target.

## Classification

- a=1 critical-layer survival: **PASS / CLOSED** for the declared stress family.
- a=1 integral Fox obstruction: **PASS / CLOSED**.
- a=1 critical nonsplitting: **PASS / CLOSED** for the declared relative stress family.
- exact relative threshold p^s+1: **PASS / CLOSED** for the declared stress family.
- all a>=1 relative threshold p^s+1: **PASS / CLOSED** for the declared rank-two stress family, with the a>=2 and a=1 witnesses now separated explicitly.
- unmarked filtered-group reconstruction: **OPEN / LOAD-BEARING**.
- universal free-by-Demushkin theorem beyond the declared stress family: **OPEN**.
- blind carrier search: **STOP / NOT AUTHORIZED**.

This supersedes the older a=1 OPEN status, while preserving it as historical provenance.


## Independent standard-filtration check

The only external structural input in the depth calculation is the standard Jennings-Lazard formula for the p-Zassenhaus filtration, D_n(G)=product_{i p^j >= n} gamma_i(G)^{p^j}. This is stated in the modern literature on the p-Zassenhaus filtration and follows from Lazard/Jennings theory. For the present witness, the required inequality reduces to max_{i>=2, i-1+j<=s} i p^j <= p^s for odd p, which is elementary; hence D_{p^s+1}(H_s)=1 follows directly from the displayed lower-central bounds.
