# HARD ATTACK 38 — EXTENSION-CLASS TRANSGRESSION / BASIS-FREE RECONSTRUCTION
## 2026-09-20

### Purpose

Attack the exact load-bearing gap from Hard Attack 37:

\[
(Q_k,M_k,E_k,\rho)
\Longrightarrow
\text{intrinsic evaluation of the finite 2-cell transgression}.
\]

The question is whether \(\delta_{k,\rho}\) can be defined and interpreted directly from the finite extension class
\[
e_k\in H^2(Q_k,M_k),
\]
without a presentation, Fox row, chosen relator, or the known orientation.

### 1. Frozen finite object

Let
\[
1\to M_k\to E_k\to Q_k\to1
\]
be the finite extension with
\[
Q_k=G/P_{k+1},\qquad
M_k=P_{k+1}/(P_{k+1}^{3^k}[P_{k+1},P_{k+1}]).
\]

Because the kernel is abelian, the extension determines canonically a class
\[
e_k=[E_k]\in H^2(Q_k,M_k).
\]

For a candidate
\[
\rho:Q_k\to U_k,
\qquad
A=A_k(\rho),
\]
the kernel \(M_k\) acts trivially on \(A\).

### 2. Basis-free identification of the transgression

Since \(M_k\) acts trivially on \(A\),
\[
H^1(M_k,A)=\operatorname{Hom}(M_k,A),
\]
with the natural \(Q_k\)-action. Hence
\[
H^1(M_k,A)^{Q_k}
=
\operatorname{Hom}_{Q_k}(M_k,A).
\]

The Hochschild–Serre five-term sequence for
\[
1\to M_k\to E_k\to Q_k\to1
\]
contains the transgression
\[
d_2^{0,1}:
\operatorname{Hom}_{Q_k}(M_k,A)
\to H^2(Q_k,A).
\]

The key Yoneda/pushout identity is:

\[
\boxed{
d_2^{0,1}(\phi)=\phi_*(e_k)
}
\]

up to the single conventional sign attached to the chosen spectral-sequence differential convention.

Here \(\phi_*(e_k)\) is the push-forward of the extension class along
\[
\phi:M_k\to A.
\]

Equivalently, push out the finite extension by \(\phi\):
\[
1\to A\to E_{k,\phi}\to Q_k\to1.
\]
Its extension class is exactly \(\phi_*(e_k)\), and this is the transgression of \(\phi\).

This construction uses only:
- the finite extension \(E_k\to Q_k\);
- its intrinsic kernel \(M_k\);
- the candidate coefficient module \(A_k(\rho)\).

It does not use \(q\), \(\chi\), a relator, Fox coordinates, \(H^2(G,A)\), or the dualizing module.

### 3. Consequence: the coker is already an intrinsic extension-class object

Therefore
\[
\boxed{
C_k(\rho)
=
\operatorname{coker}\delta_{k,\rho}
=
H^2(Q_k,A_k(\rho))
/
\{\phi_*(e_k):\phi\in\operatorname{Hom}_{Q_k}(M_k,A_k(\rho))\}.
}
\]

Thus the former phrase “evaluate the finite 2-cell transgression” can be made completely basis-free.

A more structural formulation is to regard \(e_k\) as defining a natural transgression profile
\[
\mathcal T_{e_k}(A):
\operatorname{Hom}_{Q_k}(M_k,A)
\to H^2(Q_k,A),
\qquad
\phi\mapsto\phi_*(e_k).
\]

The candidate \(\rho\) changes only the coefficient module \(A=A_k(\rho)\).

### 4. What this closes

The following logical gap from Hard Attack 37 is closed:

\[
\boxed{
\text{finite extension class}
\Longrightarrow
\text{basis-free finite transgression}
}
\]

No presentation-level relator row is needed to define \(\delta_{k,\rho}\).

In particular, the coker carrier is not merely an abstractly intrinsic object whose transgression was still conceptually undefined: its defining map is the canonical push-forward action of the extension class.

This also gives a clean gauge statement. Replacing a chosen cocycle representative of \(e_k\) by a cohomologous representative changes no push-forward class. No preferred basis of \(M_k\) is required.

### 5. Critical remaining attack: does this prove selector uniqueness?

No.

The identity
\[
\delta_{k,\rho}(\phi)=\phi_*(e_k)
\]
does **not** by itself imply
\[
|C_k(\rho)|=3^k
\iff
\rho=\chi\pmod{3^k}.
\]

That equivalence still requires a theorem controlling the size of
\[
H^2(Q_k,A_k(\rho))
\]
and the image of the push-forward map as \(\rho\) varies.

The previous PD² proof obtains this by identifying the coker with
\(H^2(G,A_k(\rho))\) and invoking the PD² orientation criterion. That remains valid but external to the finite extension calculation.

Therefore the exact boundary is now sharper:

\[
\boxed{
(Q_k,M_k,e_k,\rho)
\Longrightarrow
\delta_{k,\rho}
\quad\text{is intrinsic and basis-free;}
}
\]

but

\[
\boxed{
\delta_{k,\rho}
\Longrightarrow
\text{unique canonical orientation}
}
\]

remains **OPEN without PD²**.

### 6. New structural reformulation

The remaining problem is no longer “how do we define the transgression?”

It is:

> For the intrinsic finite extension class \(e_k\), characterize the coefficient modules \(A_k(\rho)\) for which the natural transgression profile \(\mathcal T_{e_k}(A_k(\rho))\) has maximal coker.

Thus the main object can be reformulated as the finite functorial profile
\[
A\longmapsto
\left[
\operatorname{Hom}_{Q_k}(M_k,A)
\xrightarrow{\;\phi\mapsto\phi_*(e_k)\;}
H^2(Q_k,A)
\right].
\]

This is potentially stronger than a single numerical coker: it packages the entire extension class as a natural transformation in the coefficient module.

### 7. Attack on hidden circularity

The standard Fox/one-relator obstruction row may still be used as a coordinate computation **after** the above identification, but it cannot be used as the definition.

The correct logical order is now:

\[
e_k
\to
\mathcal T_{e_k}
\to
\delta_{k,\rho}
\to
C_k(\rho)
\]

intrinsically,

and only afterwards, if desired,

\[
\text{chosen presentation}
\to
\text{Fox coordinates}
\to
\text{coordinate formula for }\mathcal T_{e_k}.
\]

This removes the specific circularity attacked in Hard Attack 37.

What remains to be checked is whether the coordinate Fox row is actually a computation of this intrinsic push-forward profile, rather than merely an independently equal-looking construction. That comparison is now a legitimate secondary verification problem.

### 8. Harder possible obstruction

There is a genuine new danger.

The pair \((Q_k,e_k)\) may contain substantially more information than the intended “filtered finite carrier” category was supposed to permit. Since \(e_k\) is the complete extension class of
\[
1\to M_k\to E_k\to Q_k\to1,
\]
the construction is not merely a graded shadow; it retains the entire finite 2-cell extension.

Therefore no claim should yet be made that this is a minimal carrier, or that the orientation is encoded by a small amount of data.

The correct claim is only that the existing finite carrier already has a canonical cohomological evaluation mechanism.

### 9. Classification

- basis-free definition of \(\delta_{k,\rho}\) from \(e_k\): **PASS / CLOSED**;
- intrinsicity/gauge independence of the transgression: **PASS / CLOSED**;
- finite coker as push-forward quotient of \(e_k\): **PASS / CLOSED**;
- Fox row = coordinate realization of this intrinsic map: **OPEN / verification target**;
- PD²-independent selector uniqueness: **OPEN / decisive**;
- PD²-based finite selector: **PASS / LOCAL**;
- minimality of \((Q_k,M_k,E_k)\): **OPEN**;
- carrier-tower naturality: **OPEN**.

### 10. Next authorized attack

The next attack should not return to broad scans.

The sharp next question is:

\[
\boxed{
\text{Can the finite transgression profile }\mathcal T_{e_k}
\text{ be evaluated from }e_k
\text{ in a way that exposes the candidate }\rho
\text{ without any PD}^2\text{ input?}
}
\]

There are two legitimate sub-attacks:

1. **Coordinate comparison:** prove that the known twisted Fox row is exactly the coordinate expression of \(\phi_*(e_k)\), using the finite extension only as the source of the calculation.

2. **Finite cohomology attack:** determine whether \(H^2(Q_k,A_k(\rho))\) and the push-forward image admit a basis-free structural description whose maximality condition singles out \(\rho\).

Only if one of these succeeds should a numerical test be authorized.

### Final result

Hard Attack 38 does not yet remove PD² from the recognition theorem.

It does something more precise: it removes the ambiguity about the transgression itself.

The finite 2-cell is not merely an analogy to a Postnikov \(k\)-invariant. It is literally an extension class whose push-forward is the transgression.

The remaining bottleneck is therefore reduced from

\[
\text{“find an intrinsic transgression”}
\]

to

\[
\boxed{
\text{“understand the intrinsic coefficient-module dependence of }
\phi_*(e_k)
\text{ strongly enough to obtain a unique selector.”}
}
\]

This is the new main target.
