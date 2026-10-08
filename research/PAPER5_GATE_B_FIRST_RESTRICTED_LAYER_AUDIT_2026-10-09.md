# Paper 5 Gate B — First restricted layer audit — 2026-10-09

## Scope

This audit reviews the proposed correction to the hand proof at the first restricted layer for
\[
w_0=x^p[x,y],\qquad p\ge3,
\]
under the already stated triangular/Frattini normalization and the conditional hypothesis
\[
\psi(w_0)\equiv w_0^{\tilde\alpha}\pmod{D_{p+1}}.
\]

The purpose is only to close the **first restricted-layer quotient calculation**. It does not prove exact relator equality, all-degree lifting, or Gate-B closure.

## 1. Degree separation

The earlier expression
\[
w_0=X^{[p]}+[X,Y]
\]
as one homogeneous graded element is incorrect.

Correctly:
\[
\bar w_0=[X,Y]\in D_2/D_3,
\]
while its degree-p restricted component is
\[
X^{[p]}\in D_p/D_{p+1}.
\]
This correction is essential and is accepted.

## 2. First variation

For
\[
C_m:x\mapsto xu,\quad y\mapsto yv,\qquad u,v\in D_m,
\]
the degree-(m+1) ordinary-bracket variation is
\[
d\Phi_m(u,v)=[u,Y]+[X,v].
\]
The p-power contributions lie above the stated first ordinary correction layer for p>=3,m>=2. Thus the image relevant to the first variation is the ordinary-bracket part, not all of the restricted graded piece.

This is a correction to the former overstatement
\(L_{m+1}=[L_m,L_1]\) for the full restricted graded piece.

## 3. Restricted quotient

For the free restricted Lie algebra on X,Y,
\[
L_p/[L_{p-1},L_1]
\cong
\mathbf F_p X^{[p]}\oplus\mathbf F_pY^{[p]}.
\]

The justification is by the standard restricted Hall/PBW description: degree-p basis elements consist of the two p-powers of degree-one generators together with ordinary bracket words of length p. The latter span \([L_{p-1},L_1]\). Hence the quotient is exactly the two-dimensional restricted-p-power span.

This is **PASS / LOCAL at the lemma level**; a manuscript proof should state the precise free-restricted-Lie basis theorem being invoked rather than leave “restricted Hall basis” informal.

## 4. Vanishing of the commutator/variation contribution

After the degree-2 determinant condition has cancelled the degree-2 part of
\(\psi([x,y])\), the degree-p contribution coming from the commutator branch lies in the ordinary-bracket subspace. Likewise
\[
d\Phi_{p-1}(u,v)\in[L_{p-1},L_1].
\]
Therefore both project to zero in the restricted quotient.

Important boundary: this statement must be formulated as a statement about the degree-p component **after the lower-degree cancellation**, not as the literal claim that \(\psi([x,y])\in D_p\). The latter is false in general.

## 5. p-power projection

Write
\[
\psi(x)\equiv x^a y^c\pmod{D_2}.
\]
Then in the degree-p restricted quotient,
\[
\pi_{\rm res}(\psi(x)^p)
=
a^pX^{[p]}+c^pY^{[p]}.
\]
The mixed/Jacobson terms are ordinary Lie degree-p terms and hence vanish under \(\pi_{\rm res}\). The group-word commutator terms have Zassenhaus weight at least 2p and therefore do not affect \(D_p/D_{p+1}\).

Since
\[
\pi_{\rm res}(w_0^{\tilde\alpha})
=
\tilde\alpha X^{[p]},
\]
the residual is
\[
\boxed{
\pi_{\rm res}(E_p)
=
(a^p-\tilde\alpha)X^{[p]}+c^pY^{[p]}.
}
\]

Thus
\[
E_p=0\text{ in }D_p/D_{p+1}
\Longrightarrow
a^p=\tilde\alpha,\qquad c=0.
\]

With the declared Teichmuller normalization \(a=\tilde\alpha\in\mathbf F_p^*\), Frobenius gives \(a^p=a=\tilde\alpha\), and the determinant condition \(ad-bc=\alpha\) gives \(d=1\).

## 6. Critical caveat: exact-equality input remains conditional

The proposition starts from
\[
\psi(w_0)\equiv w_0^{\tilde\alpha}\pmod{D_{p+1}}.
\]
Labute's weaker “sending r into r'” statement does not supply this equality. Therefore the calculation is a necessary-condition lemma for any independently obtained exact-power/conjugate-of-power lift; it is not a construction of such a lift.

## Classification

- degree-2 separation: **PASS / CLOSED**;
- first-variation ordinary-bracket statement: **PASS / CLOSED** under the stated filtration hypotheses;
- restricted quotient \(L_p/[L_{p-1},L_1]\): **PASS / LOCAL**;
- residual projection formula: **PASS / LOCAL**, conditional on the filtered exact-equality hypothesis and the standard group-to-restricted-Lie identification;
- forced conditions \(a^p=\tilde\alpha,c=0\): **PASS / LOCAL**;
- Teichmuller consequence \(a=\tilde\alpha,d=1\): **CONDITIONAL** on the preceding hypotheses;
- exact-power/conjugate-of-power realization: **OPEN / LOAD-BEARING**;
- all-degree pro-p lift: **OPEN / LOAD-BEARING**;
- Gate B: **OPEN / LOAD-BEARING**.

## Next authorized gate

Do not mark “D5 first restricted stage closed” or “Gate B closed”. The next load-bearing task is to formalize the group-to-restricted-Lie passage used in the residual projection and then attack the exact-power/conjugate-of-power realization. No blind higher-degree sweep is authorized by this lemma alone.
