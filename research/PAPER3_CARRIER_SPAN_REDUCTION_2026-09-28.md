# PAPER 3 — CARRIER MINIMALITY: CORRECTED LINEAR-QUOTIENT REDUCTION — 2026-09-28

## Critical review status

A further audit found one important overstatement in the previous version.

D2 proves that **for each false candidate** there exists at least one witness whose obstruction has nonzero global inflation. It does **not** prove that every obstruction output produced by an arbitrary witness has nonzero global inflation.

Therefore the previous statement
\[
o\in\mathscr F_k\implies\lambda_k(o)\ne0
\]
was too strong if \(\mathscr F_k\) means the set of *all* finite outputs.

The corrected object is the **witness-detecting set**
\[
\mathscr W_k
=
\left\{
o_{\rho,f}\in\mathcal O_k:
\rho\ne\chi_k,\ 
\operatorname{inf}_G(o_{\rho,f})\ne0
\right\}.
\]

D2 proves:
\[
\boxed{
\forall\rho\ne\chi_k,\quad
\exists o_{\rho,f}\in\mathscr W_k.
}
\]

This is exactly what is needed for recognition. It is not necessary that every possible witness output belong to \(\mathscr W_k\).

## 1. Fixed finite carrier

For
\[
Q_k=G/D_{p^{k-1}+1},\qquad
E_k=G/D_{p^{k-1}+2},
\]
define
\[
\mathcal O_k
=
H^2(Q_k,\mathbf F_p)/\operatorname{im}(\operatorname{tra}_k).
\]

Global inflation induces
\[
\lambda_k:\mathcal O_k\to H^2(G,\mathbf F_p),
\]
because every transgression class dies in \(E_k\) and therefore dies after inflation to \(G\).

The canonical branch gives zero connecting map. For each false first-order candidate
\[
\rho_k=\chi_k(1+p^{k-1}\nu),\qquad\nu\ne0,
\]
D2 supplies at least one witness \(f\) such that
\[
\lambda_k([\delta_{k,\rho_k}(f)])\ne0.
\]

## 2. Exact recognition criterion

Let \(\mathscr W_\rho\subset\mathcal O_k\setminus\{0\}\) be the set of witness-detecting obstruction classes for a fixed false candidate \(\rho\):
\[
\mathscr W_\rho
=
\left\{
[\delta_{k,\rho}(f)]:
\lambda_k([\delta_{k,\rho}(f)])\ne0
\right\}.
\]

D2 says
\[
\boxed{\mathscr W_\rho\ne\varnothing}
\]
for every \(\rho\ne\chi_k\).

For a linear quotient
\[
\pi:\mathcal O_k\twoheadrightarrow C,
\]
the quotient detects every false candidate exactly when
\[
\boxed{
\forall\rho\ne\chi_k,\quad
\exists o\in\mathscr F_\rho:
\pi(o)\ne0,
}
\]
where \(\mathscr F_\rho\) is the full finite obstruction set for \rho.

Equivalently, the kernel must not contain the entire obstruction set of any false candidate:
\[
\boxed{
\ker\pi\not\supseteq\mathscr F_\rho
\quad\text{for every }\rho\ne\chi_k.
}
\]

This is the exact recognition criterion.

The stronger condition
\[
\ker\pi\cap\operatorname{span}(\mathscr F_k)=\{0\}
\]
is sufficient but not necessary.

## 3. Global one-dimensional detector

Because
\[
\dim_{\mathbf F_p}H^2(G,\mathbf F_p)=1,
\]
and D2 gives, for every false candidate, a witness with nonzero \lambda_k-image, the map
\[
\lambda_k:\mathcal O_k\to H^2(G,\mathbf F_p)
\]
is a **one-dimensional recognition detector in the global category**.

Important correction:

This does **not** say every finite obstruction output survives globally. It says every false candidate has at least one output that survives globally.

Thus the logical implication is:
\[
\boxed{
\rho\ne\chi_k
\Longrightarrow
\exists f:\lambda_k(\delta_{k,\rho}(f))\ne0.
}
\]

That is exactly the selector property.

## 4. Finite-pair intrinsic category

The global detector uses the inflation map into
\[
H^2(G,\mathbf F_p),
\]
which is not part of the finite pair
\[
E_k\to Q_k.
\]

Therefore the actual intrinsic question remains:
\[
\boxed{
\text{Can an equivalent one-dimensional detector be reconstructed functorially
from }E_k\to Q_k\text{ alone?}
}
\]

This is genuinely OPEN.

However, one should **not** yet phrase the negation as “the finite pair cannot recover \lambda_k.” There is no proof of non-recoverability. In particular, a canonical functional might be determined indirectly by the extension class of
\[
1\to K_k\to E_k\to Q_k\to1
\]
together with the Demuškin structure.

So the current frontier is a reconstruction problem, not an impossibility claim.

## 5. 45-dimensional calculation

The old
\[
\dim(P_4/P_5)=45,\qquad
\ker(H^2(W_4)\to H^2(W_5))\cong Q_4^*
\]
calculation is still not required for D2/D3 or for the global one-dimensional detector.

It becomes relevant only if abstract reconstruction fails or cannot be decided, and we need to analyze the finite-pair extension/module structure concretely.

Thus:

\[
\boxed{\text{45-dimensional calculation remains DEFERRED.}}
\]

## 6. Final critical classification

| Item | Status |
|---|---|
| D2 false-candidate separation | PASS / CLOSED |
| Global \(\lambda_k\) factors through \(\mathcal O_k\) | PASS / CLOSED |
| 1D global recognition detector | PASS / CLOSED |
| “every obstruction output has nonzero global shadow” | **FAIL / CLOSED — overstatement** |
| Exact quotient-recognition criterion | PASS / CLOSED |
| Finite-pair 1D reconstruction | OPEN / LOAD-BEARING |
| Finite-pair non-recoverability | OPEN / NOT CLAIMED |
| \(\mathcal O_k\) absolute minimality | FAIL / CLOSED as ill-posed |
| Functorial finite-pair minimality | OPEN |
| 45-dimensional recomputation | DEFERRED |

## Next target

The mathematically sharp next question is:

\[
\boxed{
\text{Does the extension }E_k\to Q_k
\text{ canonically determine a nonzero functional on the D2 witness family?}
}
\]

If yes, the finite intrinsic carrier may collapse to one dimension.

If no, one must identify the smallest additional filtered data required.
