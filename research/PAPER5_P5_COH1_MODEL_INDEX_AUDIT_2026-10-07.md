# Paper 5 — P5-MODEL-1 / P5-COH-1 Audit — 2026-10-07

## 0. Indexing convention

There are two notations in the Paper 5 record and they must not be conflated.

### GAP/window notation
[
mathcal W_n^{m GAP}:=G/D_n(G).
]

Thus the recorded values
[
p=3:quad n=3,4,5,
qquad
p=5:quad n=5,6
]
refer to (G/D_n).

### Free-presentation window notation
When
[
W_m:=F/(R D_{m+1}(F)),
]
then
[
oxed{W_m=mathcal W_{m+1}^{m GAP}=G/D_{m+1}(G)}
]
for the actual one-relator group.

Hence the first nontrivial relation-jet window called (W_p) in the free-presentation notation is the GAP window (n=p+1).

In particular:
[
W_p=mathcal W_{p+1}^{m GAP}.
]

The equality (W_{p+1}=W_p) belongs to the corrected central-model theorem only; it must not be silently transferred to the actual (G_{1,1}) family.

---

## 1. Relator and minimal presentation

For the actual model
[
G=G_{1,1}
=
langle z,x,ymid z^p=x^p[x,y]angle,
]
take
[
F=F(z,x,y),qquad
r=z^p x^{-p}[x,y]^{-1}.
]

For odd (p),
[
rin D_2(F)
]
and its initial terms at the two relevant degrees are:

- degree (2):
  [
  [x,y]^{-1};
  ]
- degree (p):
  [
  z^p x^{-p}.
  ]

The presentation is minimal because (rinPhi(F)=D_2(F)).

Since this is a one-relator pro-(p) presentation, (H^2(G,mathbf F_p)) is one-dimensional. Write a chosen generator as (eta).

---

## 2. Direct derivation of (omega)

Let
[
x^*,y^*,z^*
]
be the basis of (H^1(G,mathbf F_p)) dual to (x,y,z).

The standard minimal-presentation relation formula identifies the commutator coefficient of the relator modulo the third p-central/Zassenhaus level with the cup-product coefficients.

Here the only nonzero degree-two commutator coefficient is the (xy)-coefficient. Therefore, after choosing the sign of (eta),
[
oxed{x^*smile y^*=eta}
]
and all other independent degree-two cup products vanish.

Hence
[
oxed{omega=x^*wedge y^*}.
]

This is not merely a numerical fit. It is forced by the quadratic initial form of the actual relator.

For standard background, see Quadrelli, *Pro-p groups with few relations*, Proposition 3.2, and the minimal-presentation cup-product formula (NSW, Prop. 3.9.13).

---

## 3. Direct derivation of (eta)

For odd (p), the same minimal-presentation calculation identifies the p-power coefficients of the relator with the Bockstein coefficients.

Modulo the third relevant level, the p-power part is
[
z^p x^{-p}.
]

Thus, with the same choice of (eta),
[
eta(z^*)=-eta,qquad
eta(x^*)=+eta,qquad
eta(y^*)=0.
]

Therefore
[
oxed{
eta(lambda)
=
(lambda(x)-lambda(z)),eta.
}
]

A simultaneous replacement (etamapsto-eta) changes both displayed signs and has no effect on the stabilizer.

The identification of p-power coefficients with Bockstein classes is the standard companion to the cup-product relation formula (NSW, Prop. 3.9.14; Labute's corresponding presentation formula).

Thus the former status “candidate (omega,eta)” can now be upgraded to a theorem-level derivation for the global group, subject only to the declared basis/sign convention.

---

## 4. Intrinsic stabilizer

Let (V=H_1(G,mathbf F_p)) with ordered basis ((x,y,z)), and let (Ain GL(V)) be the matrix of an automorphism.

Preservation of the one-dimensional image of
[
smile:Lambda^2H^1	o H^2
]
and the fact that
[
omega=x^*wedge y^*
]
has radical (langle zangle) imply preservation of the corresponding two-plane (langle x,yangle).

Write the induced matrix in the established column convention as
[
A=
egin{pmatrix}
B&u\
0&a_{33}
end{pmatrix},
qquad Bin GL_2(mathbf F_p).
]

The cup-product line is scaled by the inverse determinant of the (2	imes2) block. Naturality of (eta) then imposes
[
A(e_x-e_z)=det(B)(e_x-e_z).
]

Solving these equations gives
[
B=
egin{pmatrix}
a&b\
0&1
end{pmatrix},
qquad
a_{33}=a,
qquad
u=0.
]

Therefore
[
oxed{
S_{m coh}(p)
=
left{
egin{pmatrix}
a&b&0\
0&1&0\
0&0&a
end{pmatrix}
:
ainmathbf F_p^	imes, binmathbf F_p
ight}.
}
]

Hence
[
oxed{|S_{m coh}(p)|=p(p-1)}.
]

Moreover
[
S_{m coh}(p)congmathbf F_ptimesmathbf F_p^	imes.
]

This is now a genuine cohomological stabilizer calculation, not an order fit.

---

## 5. What this closes — and what it does not

For the actual pro-p group (G_{1,1}), every automorphism acts naturally on mod-p cohomology and commutes with the Bockstein. Therefore
[
oxed{
operatorname{Im}igl(operatorname{Aut}(G)	o GL(H^1(G,mathbf F_p))igr)
subseteq S_{m coh}(p).
}
]

This upper bound is now CLOSED / GENERAL in the declared odd-p scope.

It does **not** yet prove equality.

The remaining equality problem is precisely
[
S_{m coh}(p)
subseteq
operatorname{Im}igl(operatorname{Aut}(G)	o GL(H^1(G,mathbf F_p))igr).
]

The b-unipotent part is already explicitly realized. The only load-bearing part is the diagonal family
[
operatorname{diag}(a,1,a),
qquad ainmathbf F_p^	imes.
]

---

## 6. Finite-window upper bound remains separate

The global cohomological upper bound does NOT automatically imply
[
L_{W_p}subseteq S_{m coh}(p),
]
because an arbitrary finite-window automorphism need not lift to an automorphism of (G).

Therefore the finite-window upper bound remains a separate intrinsic relation-jet problem.

The correct target is now:

[
oxed{
operatorname{Im}igl(operatorname{Aut}(W_p)	o GL(V)igr)
subseteq S_{m coh}(p),
}
]
where (W_p=G/D_{p+1}) in the present indexing convention.

The degree-two relation supplies (omega), while the degree-(p) restricted-power relation supplies (eta). This is exactly the two-level relation-jet mechanism. The proof must be formulated intrinsically in (W_p), not by asserting that a finite-window automorphism lifts to (G).

---

## 7. Numerical interpretation

The previous local data now have a clean interpretation.

For (p=3):
[
|mathrm{GL}_3(mathbf F_3)|=11232,
qquad
11232/864=13=|mathbf P^2(mathbf F_3)|.
]

For (p=5):
[
|mathrm{GL}_3(mathbf F_5)|=1,488,000,
qquad
1,488,000/48,000=31=|mathbf P^2(mathbf F_5)|.
]

Thus the (n=p) GAP images are the expected maximal parabolic order
[
p^3(p-1)^3(p+1)
]
and have index
[
p^2+p+1.
]

This numerical observation is consistent with stabilization of the distinguished plane/radical data at the pre-(W_p) level, but it is not yet promoted to an embedded-equality theorem.

The first verified relation-jet collapse is:
[
864	o6quad(p=3),
qquad
48000	o20quad(p=5).
]

Under the present indexing these are
[
G/D_p	o G/D_{p+1}=W_p,
]
not two successive genuinely new (W_m)-windows.

---

## 8. Diagonal realization — current gate

The required diagonal automorphism has induced matrix
[
operatorname{diag}(a,1,a).
]

A naive assignment
[
xmapsto x^lambda,qquad ymapsto y,qquad zmapsto z^lambda
]
does not automatically preserve
[
z^p=x^p[x,y],
]
because (x^lambda) does not commute with ([x,y]).

Therefore the correct construction must be a corrected map
[
xmapsto X_lambda,qquad
ymapsto y,qquad
zmapsto Z_lambda
]
with
[
X_lambdaequiv x^lambda,quad
Z_lambdaequiv z^lambdapmod{D_2},
]
and with
[
Z_lambda^p=X_lambda^p[X_lambda,y]
]
solved recursively in the Zassenhaus filtration.

This is the legitimate Hensel/Newton formulation. The existence of the correction sequence has not yet been proved.

A direct p=3 extraction attempt was audited against the exact Zassenhaus window, but the final generator-coordinate extraction is not yet closed; it is therefore not used as evidence for the general realization. The previously certified image-order result remains PASS / LOCAL.

Classification:
[
oxed{	ext{diagonal realization: OPEN / LOAD-BEARING}.}
]

---

## 9. Current theorem target

The clean theorem target is now:

[
oxed{
operatorname{Im}
igl(
operatorname{Aut}(G_{1,1})
	o GL_3(mathbf F_p)
igr)
=
S_{m coh}(p)
cong
mathbf F_ptimesmathbf F_p^	imes
}
]

for odd (p), with

[
S_{m coh}(p)
=
operatorname{Stab}(omega,eta).
]

Then, separately, prove the intrinsic finite-window upper bound at (W_p=G/D_{p+1}). If the diagonal realization is closed, the persistence theorem follows from

[
S_{m coh}(p)
subseteq
operatorname{Im}operatorname{Aut}(G)
subseteq
L_n
subseteq
L_{p+1}
subseteq
S_{m coh}(p)
]
for all (nge p+1) in GAP notation.

No (p=5,n=7) computation is needed for the theorem.

## Classification

- indexing correction: **PASS / CLOSED**;
- (omega) from the relator: **PASS / CLOSED / GENERAL**;
- (eta) from the relator: **PASS / CLOSED / GENERAL**;
- (S_{m coh}(p)) calculation: **PASS / CLOSED / GENERAL**;
- global automorphism-image upper bound: **PASS / CLOSED / GENERAL**;
- finite-window (W_p) upper bound: **OPEN / LOAD-BEARING**;
- b-unipotent realization: **PASS / CLOSED / GENERAL**;
- diagonal realization: **OPEN / LOAD-BEARING**;
- global equality: **OPEN / LOAD-BEARING**;
- (n=p) maximal-parabolic interpretation: **PASS / LOCAL**, embedded equality still to be certified.
