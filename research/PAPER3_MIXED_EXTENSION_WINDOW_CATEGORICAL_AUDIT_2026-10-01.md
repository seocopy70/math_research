# MIXED (3,I)-ADIC FOX — EXTENSION-WINDOW CATEGORICAL AUDIT — 2026-10-01

## Result

The categorical packaging has now been pushed one step further, and the decisive boundary is sharper than the previous audit stated.

Set
\[
N_k=3^{k-1}+1,\qquad
Q_k=G/D_{N_k},\qquad
E_k=G/D_{N_k+1},\qquad
A_k=D_{N_k}/D_{N_k+1}.
\]
There is a central extension
\[
1\to A_k\to E_k\to Q_k\to1.
\]

The correct finite input for the proposed mixed Fox construction is therefore an **extension window**, not the bare pair \((Q_k,A_k)\).

The important new conclusion is:

> The extension-window construction is a legitimate finite-input candidate, but adding \(E_k\to Q_k\) is a genuine strengthening of the input unless a separate reconstruction theorem shows that the extension class is already determined by the original finite pair.

Thus an extension-window descent theorem, even if completed, would not by itself prove the original finite-pair carrier theorem.

## 1. Exact extension-window category

Define the provisional category \(\mathbf{ExtWin}_k\) as follows.

An object is a diagram
\[
\mathsf W_k^{\mathrm{ext}}(G)
=
\bigl(A_k\hookrightarrow E_k\twoheadrightarrow Q_k\bigr),
\]
with
\[
E_k=G/D_{N_k+1},\quad Q_k=G/D_{N_k},\quad
A_k=D_{N_k}/D_{N_k+1},
\]
and with the induced central extension structure.

A morphism is a commutative morphism of extensions preserving the distinguished kernel \(A_k\). Isomorphisms are isomorphisms of the whole diagram, not separate isomorphisms of \(Q_k\) and \(A_k\).

This removes the type defect identified in the previous audit.

## 2. The forgetful map exposes the real issue

There is a forgetful operation
\[
U:\mathbf{ExtWin}_k\longrightarrow\mathbf{Pair}_k,
\qquad
(A_k\hookrightarrow E_k\twoheadrightarrow Q_k)
\longmapsto(Q_k,A_k).
\]

The fibers of \(U\) contain extension-class information. Abstractly, central extensions of a fixed \(Q\) by a fixed trivial \(Q\)-module \(A\) are classified by a second-cohomology class (with the usual equivalence conventions).

Therefore the data
\[
(Q_k,A_k)
\]
do not, merely by their type, contain the extension class of
\[
1\to A_k\to E_k\to Q_k\to1.
\]

For the special Zassenhaus windows considered here, the extension is of course canonically produced from the original filtered group \(G\). But the required theorem would be stronger:

\[
(Q_k,A_k)\cong(Q_k',A_k')
\quad\Longrightarrow\quad
\mathsf W_k^{\mathrm{ext}}(G)\cong
\mathsf W_k^{\mathrm{ext}}(H).
\]

No such reconstruction theorem has been proved in the current branch.

Hence the extension window must presently be classified as **additional input**, not as a proven canonical enrichment of the original pair.

## 3. What can be made intrinsic from the extension window

For a finite pro-3 group \(E\), choose a minimal free pro-3 presentation
\[
1\to R\to F_d\to E\to1.
\]

The completed Fox/Lyndon sequence gives the relation-module realization
\[
0\to R^{\mathrm{ab}}_{(3)}
\longrightarrow
\Lambda_E^d
\xrightarrow{(x_i-1)}
I_E
\to0
\]
in the standard pro-3 formulation, with the Fox rows representing the relation-module inclusion.

At the finite extension-window level one can form the mixed coefficient ring
\[
\Lambda_E=\mathbf Z_3[E],
\qquad
\mathfrak m_E=(3,I_E),
\]
and take the relation/Fox image modulo \(\mathfrak m_E^{k+1}\), followed by the already audited stable/projective quotient.

This gives a candidate functor
\[
\mathsf{ExtWin}_k
\longrightarrow
\mathbf{ProjFox}_k,
\qquad
\mathsf W_k^{\mathrm{ext}}\longmapsto\mathcal M_k^{\mathrm{ext}}.
\]

The remaining presentation issue is controlled by stable relation-module equivalence and projective change of coordinates; the underlying Fox/Lyndon mechanism is established in the cited pro-p literature. Mel'nikov's exact sequence gives the pro-p relation-module/Fox realization, while the current project-specific weighted estimate supplies the mixed-order truncation control. citeturn0search24turn0search4

## 4. Why this does not yet prove the desired theorem

The desired original statement was

\[
W_k(G)=(Q_k,A_k)
\quad\Longrightarrow\quad
\mathcal M_k(G).
\]

The extension-window statement is instead

\[
\mathsf W_k^{\mathrm{ext}}(G)
\quad\Longrightarrow\quad
\mathcal M_k^{\mathrm{ext}}(G).
\]

These are logically different.

The latter may be a perfectly legitimate finite-input factorization theorem. But if the input contains \(E_k\), then the theorem has not shown that the original pair \((Q_k,A_k)\) carries enough information.

The weighted Magnus estimate only says that deep elements of \(D_{N_k}\) are invisible to the mixed jet below the relevant precision and that the first boundary contribution lies in \(A_k\). It does **not** by itself prove that the extension class is reconstructible from \((Q_k,A_k)\).

That is the exact point at which the previous argument was in danger of changing the problem.

## 5. The correct categorical diagram

The honest structure is

\[
\boxed{
G
\longmapsto
\mathsf W_k^{\mathrm{ext}}(G)
\xrightarrow{\;F_k\;}
\mathcal M_k(G)
}
\]

together with the forgetful map

\[
\boxed{
\mathsf W_k^{\mathrm{ext}}(G)
\xrightarrow{\;U\;}
W_k(G)=(Q_k,A_k).
}
\]

The original finite-pair theorem requires a factorization

\[
\boxed{
F_k=\overline F_k\circ U
}
\]

for some natural \(\overline F_k\).

Equivalently, \(F_k\) must be constant on the fibers of the forgetful functor \(U\), up to canonical projective equivalence.

This is the cleanest formulation of the original load-bearing question.

## 6. Decisive test

The next attack is therefore **not** to prove the extension-window theorem and declare victory.

It is:

### Test A — Fiber invariance

Determine whether two admissible extension windows with isomorphic bare pair
\[
(Q,A)
\]
can have non-projectively-equivalent mixed Fox jets.

- If yes, construct such a pair explicitly.

Then
\[
\boxed{\text{FAIL / CLOSED}}
\]
for the original finite-pair carrier.

- If no, prove that \(F_k\) is invariant on every admissible fiber of \(U\).

Then the extension-window construction descends to the original pair.

### Test B — Reconstruction

A stronger route is to prove a canonical reconstruction theorem
\[
(Q_k,A_k)
\longmapsto
[E_k\to Q_k]
\]
within the declared category.

Such a theorem would make the extension window a canonical enrichment rather than an illicit strengthening.

No such reconstruction is currently established.

## 7. A useful refinement: the extension window itself may already be enough

There is one important positive point.

Because \(E_k\) is finite, the mixed Fox object can be defined directly from its finite group algebra and relation module rather than from an infinite characteristic-zero lift of \(G\). The weighted Magnus result then explains why this finite object is compatible with the precision-k mixed jet of \(G\).

So the extension-window branch is not illegitimate or circular.

Its status is:

\[
\boxed{
\text{finite extension-window carrier}
=
\text{legitimate candidate}
}
\]

but not yet

\[
\boxed{
\text{finite-pair carrier}
}
\]

and not yet

\[
\boxed{
\text{genuinely new result}.
}
\]

## 8. Relation to prior literature

The literature supports the structural ingredients, not the present factorization theorem.

Mel'nikov gives the pro-p relation-module exact sequence with Fox derivatives. citeturn0search24turn0search4

Efrat's work gives natural finite-level Zassenhaus/Magnus constructions and cohomological descriptions of finite Zassenhaus quotients. citeturn0academia23turn0academia26

The current branch still requires the project-specific statement that the mixed \((3,I)\)-adic projective relation jet is determined by the finite extension window at the stated precision, and, for the original target, that it is constant on the fibers of \(U\).

Neither cited ingredient supplies that final factorization automatically.

## Classification

- extension-window object definition: **PASS / CLOSED**;
- type correctness of \((Q_k,A_k)\) versus extension data: **PASS / CLOSED**;
- finite extension-window → projective mixed Fox construction: **PASS / LOCAL** as a well-defined proof target and architecture; full natural-transformation proof still requires formal verification;
- extension-window as canonical enrichment of the original pair: **OPEN**;
- original \((Q_k,A_k)\to\mathcal M_k\) descent: **OPEN / LOAD-BEARING**;
- original finite-pair carrier status: **OPEN**;
- new mathematical result: **OPEN**;
- next decisive action: **fiber-invariance/reconstruction test**, not a larger Fox computation.

Hard stop: if an admissible same-pair/different-extension example with different projective mixed jets is found, close the original finite-pair Mixed Fox branch as **FAIL / CLOSED**. If fiber invariance is proved, then and only then promote the extension-window theorem to a finite-pair factorization theorem.
