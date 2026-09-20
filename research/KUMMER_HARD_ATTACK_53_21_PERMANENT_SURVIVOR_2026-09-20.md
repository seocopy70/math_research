# HARD ATTACK 53 — THE 19-DIMENSIONAL (2,1) SURVIVOR IS PERMANENT

Date: 2026-09-20

## Target

HA52 established
\[
\dim E_3^{2,1}=19.
\]
The next question is whether higher LHS differentials can remove this 19-dimensional sector.

## Spectral-sequence degree obstruction

The LHS differential has bidegree
\[
d_r:E_r^{p,q}\longrightarrow E_r^{p+r,q-r+1}.
\]

For a source class in \(E_3^{2,1}\), every differential with \(r\ge3\) has target
\[
E_r^{2+r,,2-r}.
\]
For \(r=3\), the target is \(E_3^{5,-1}=0\), and for every \(r>3\) the second index is even more negative. Thus there are no outgoing higher differentials.

There are also no incoming higher differentials into \(E_r^{2,1}\), because an incoming \(d_r\) would originate at
\[
E_r^{2-r,,r},
\]
whose first index is negative for every \(r\ge3\).

Therefore
\[
\boxed{E_3^{2,1}=E_\infty^{2,1}.}
\]

Combining with HA52,
\[
\boxed{\dim E_\infty^{2,1}=19.}
\]

This is stronger than merely saying that a nonzero survivor exists: the entire 19-dimensional page-3 sector is a permanent LHS filtration piece.

## Consequence

The central-extension LHS calculation has now produced a forced 19-dimensional contribution to
\[
H^3(Q_2,\mathbf F_3)
\]
through filtration \((2,1)\).

This also closes the possibility that the fiber correction is merely a transient page-3 artifact. It is a genuine associated-graded piece of the finite-group cohomology.

However, this still does not identify the 19-dimensional piece as an H-module, nor does it determine the action of the twisted coefficient Bockstein \(\beta_\rho^2\) on it. Those remain separate questions.

## Decision

- \(\dim E_3^{2,1}=19\): **PASS / CLOSED** (HA52).
- no higher outgoing differentials from \((2,1)\): **PASS / CLOSED**.
- no higher incoming differentials into \((2,1)\): **PASS / CLOSED**.
- \(E_3^{2,1}=E_\infty^{2,1}\): **PASS / CLOSED**.
- \(\dim E_\infty^{2,1}=19\): **PASS / CLOSED**.
- H-module structure: **OPEN / LOAD-BEARING**.
- twisted \(\beta_\rho^2\) on the 19-dimensional sector: **OPEN / LOAD-BEARING**.
- unique coker maximizer without PD²: **OPEN / DECISIVE**.

## Next authorized attack

Identify the 19-dimensional permanent survivor as an H-module, or at minimum derive its canonical quotient/kernel description from the extension class. Then compute the induced twisted Bockstein on this exact filtration piece.
