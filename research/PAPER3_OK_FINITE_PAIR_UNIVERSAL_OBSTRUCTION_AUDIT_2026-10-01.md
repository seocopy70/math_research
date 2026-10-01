# PAPER 3 — O_k FINITE-PAIR UNIVERSAL OBSTRUCTION PROPERTY AUDIT — 2026-10-01

## Status

**The proposed finite-pair universal obstruction property, if formulated with existence + uniqueness of a factorization from every admissible carrier into O_k, FAIL / CLOSED at the categorical level.**

The failure is not a failure of the finite obstruction carrier O_k itself. It is a failure of the proposed universal property as a nontrivial minimality theorem.

The correct result splits into two different statements:

1. A natural **quotient/universal property in the opposite direction**
   \[
   \mathcal O_k \to C
   \]
   is automatic once an obstruction carrier is defined as a linear finite-pair quotient annihilating the transgression sector. This is only the universal property of the cokernel
   \[
   H^2(Q_k)\twoheadrightarrow
   H^2(Q_k)/\operatorname{im}(\operatorname{tra}_k).
   \]
   It is therefore **tautological as a new theorem**.

2. The stronger proposed property
   \[
   C\to\mathcal O_k
   \]
   for every admissible separating carrier is not forced by the finite-pair data. In particular, if uniqueness is included in the universal-property claim, it is false.

This closes the attempted O_k universal-minimality route. O_k itself remains a valid PASS/CLOSED proof carrier.

---

## 1. Fixed finite pair

For
\[
N_k=p^{k-1},\qquad
Q_k=G/D_{N_k+1},\qquad
E_k=G/D_{N_k+2},
\]
write
\[
1\to K_k\to E_k\to Q_k\to1,
\qquad
K_k=D_{N_k+1}/D_{N_k+2}.
\]

The intrinsic transgression quotient is
\[
\mathcal O_k
=
H^2(Q_k,\mathbf F_p)/
\operatorname{im}(\operatorname{tra}_k).
\]

The previously established D2 theorem gives:

- the transgression sector is exactly the one-step finite transient sector;
- the canonical branch has zero obstruction;
- every false candidate has at least one obstruction witness whose class is nonzero in \(\mathcal O_k\);
- no claim is made that every obstruction output is globally nonzero.

These facts are treated as frozen inputs here.

---

## 2. The only precise admissible linear-carrier category that can be obtained directly from the obstruction map

A natural finite-pair linear obstruction carrier can be described by data
\[
(C,\omega_C),
\]
where:

- \(C\) is a finite-dimensional \(\mathbf F_p\)-vector-space-valued functor of the finite pair \(E_k\to Q_k\);
- \(\omega_C:H^2(Q_k,\mathbf F_p)\to C\) is natural and linear;
- \(\omega_C\circ\operatorname{tra}_k=0\);
- the carrier is separating if, for every false candidate \(\rho\), at least one finite obstruction witness \(\alpha\) satisfies
  \[
  \omega_C(\alpha)\ne0.
  \]

The condition
\[
\omega_C\circ\operatorname{tra}_k=0
\]
is exactly the condition needed for the finite transient sector not to be load-bearing.

No orientation, presentation, q-label, or global \(H^2(G)\) is inserted.

---

## 3. What is actually universal

Let
\[
\pi_k:H^2(Q_k,\mathbf F_p)\twoheadrightarrow\mathcal O_k
\]
be the quotient map.

For every carrier \((C,\omega_C)\) satisfying
\[
\omega_C\circ\operatorname{tra}_k=0,
\]
the ordinary universal property of the quotient gives a unique natural linear map
\[
u_C:\mathcal O_k\to C
\]
such that
\[
\boxed{
\omega_C=u_C\circ\pi_k.
}
\]

Thus:

\[
\boxed{
\mathcal O_k\longrightarrow C
}
\]

is universal in the category of carriers whose obstruction map is required to annihilate the transgression sector.

But this result contains no new mathematical content beyond the definition of \(\mathcal O_k\). It is precisely the universal property of a cokernel/quotient.

Therefore it cannot serve as a substantive Paper-3 universal-obstruction theorem.

Classification:

**O_k → C quotient universality: PASS / CLOSED, but TAUTOLOGICAL / NOT LOAD-BEARING.**

---

## 4. The proposed direction C → O_k is a different theorem

The requested stronger statement is of the form

\[
\boxed{
\text{every admissible separating carrier }C
\longrightarrow
\mathcal O_k.
}
\]

This does not follow from the quotient definition.

A carrier may contain, discard, or reorganize finite-pair information in ways not represented by a canonical map into \(H^2(Q_k)/\operatorname{im}(\operatorname{tra}_k)\).

To obtain such a map one would need an additional theorem saying that every admissible carrier is canonically controlled by the specific degree-2 obstruction quotient.

No such theorem is supplied by D2, functoriality, or the five-term sequence.

In particular, the fact that \(\mathcal O_k\) detects every false candidate only establishes sufficiency of \(\mathcal O_k\); it does not establish terminality among all carriers.

---

## 5. Uniqueness is decisively impossible in any category closed under direct sums

Suppose the proposed universal statement includes uniqueness of the factorization.

Take the already admissible carrier
\[
C=\mathcal O_k\oplus\mathcal O_k
\]
with obstruction map
\[
\omega_C(\alpha)
=
(\pi_k(\alpha),\pi_k(\alpha)).
\]

This carrier is still finite, linear, functorial, annihilates the transgression sector, and separates every false candidate because each nonzero witness is sent to a nonzero diagonal vector.

There are at least two distinct natural maps
\[
s_1,s_2:C\to\mathcal O_k
\]
given by the two projections.

Both are compatible with detection in the evident sense, and they are distinct whenever \(\mathcal O_k\ne0\).

Hence a terminal-style claim

\[
\boxed{
\text{every admissible carrier admits a unique map }C\to\mathcal O_k
}
\]

is false.

This is a categorical counterexample; no numerical computation is required.

The same direct-sum obstruction applies to any proposed universal object whose admissible carrier category is closed under finite direct sums and whose morphisms do not impose an extra rigidifying structure.

---

## 6. Why this does not prove non-existence of every map C → O_k

The preceding argument must not be overstated.

It proves:

\[
\boxed{
\text{universal factorization with uniqueness: FAIL / CLOSED}.
}
\]

It does **not** prove:

\[
\boxed{
\text{no natural map }C\to\mathcal O_k
\text{ can exist for any individual carrier }C.
}
\]

For particular carriers such as the intrinsic cup-line carrier \(C_k\), a natural inclusion into \(\mathcal O_k\) is available through
\[
C_k\subset H^2(Q_k,\mathbf F_p)
\twoheadrightarrow\mathcal O_k,
\]
and the nonzero cup line survives the transgression quotient.

Thus the correct boundary is categorical, not an impossibility theorem about every carrier.

---

## 7. The deeper problem: "all admissible carriers" is still too broad

There are now only two coherent choices.

### Choice A — define carriers by maps out of H²(Q)

Then
\[
\mathcal O_k
=
\operatorname{coker}(\operatorname{tra}_k)
\]
is automatically universal toward every such carrier.

This is mathematically correct but tautological.

### Choice B — allow genuinely independent finite-pair constructions

Then a carrier can use extension/module/cup/Bockstein/other functorial data not presented as a quotient of H²(Q).

For this larger category, the statement
\[
C\to\mathcal O_k
\]
requires an actual new comparison theorem. It is not a consequence of D2.

No evidence currently establishes that comparison theorem.

Therefore it cannot be promoted to PASS.

---

## 8. Consequence for O_k

The attack therefore separates three claims that had been dangerously close to being conflated:

| Claim | Status |
|---|---|
| \(\mathcal O_k\) is a valid finite intrinsic obstruction carrier | **PASS / CLOSED** |
| \(\mathcal O_k\) is universal among quotient carriers annihilating transgression, in the direction \(\mathcal O_k\to C\) | **PASS / CLOSED but TAUTOLOGICAL** |
| Every independent admissible separating carrier canonically factors \(C\to\mathcal O_k\) | **OPEN / NOT PROVED** |
| Every such factorization is unique | **FAIL / CLOSED** |
| \(\mathcal O_k\) is an absolute minimal carrier | **FAIL / CLOSED as ill-posed** |
| A genuinely smaller intrinsic selector carrier exists | **PASS / CLOSED: \(C_k\) is already known** |

The last item is important: the existing one-dimensional cup-line carrier is not a new discovery generated by this attack. It is already the established recognition carrier.

---

## 9. Research consequence

The proposed \(\mathcal O_k\)-universal-property route is therefore exhausted.

It cannot produce a new theorem in its present form:

\[
\boxed{
\text{O_k universal obstruction minimality}
\quad\Longrightarrow\quad
\text{STOP}.
}
\]

The remaining mathematically nontrivial direction is not to enlarge \(\mathcal O_k\) or repeat its calculation. It is to identify a genuinely independent finite-pair carrier whose construction is not merely a quotient/subquotient of the existing \(H^2\)-obstruction package and then test:

1. intrinsicity;
2. functoriality;
3. gauge independence;
4. q-blindness;
5. orientation bridge;
6. non-redundancy against the already closed \(C_k\) selector.

No large computation is authorized before those six checks.

---

## 10. Final classification

\[
\boxed{
\begin{aligned}
&\mathcal O_k\text{ finite obstruction carrier}
&&\textbf{PASS / CLOSED},\\
&\mathcal O_k\to C\text{ quotient universality}
&&\textbf{PASS / CLOSED — TAUTOLOGICAL},\\
&C\to\mathcal O_k\text{ universal existence}
&&\textbf{OPEN / NOT PROVED},\\
&C\to\mathcal O_k\text{ universal uniqueness}
&&\textbf{FAIL / CLOSED},\\
&\mathcal O_k\text{ absolute minimality}
&&\textbf{FAIL / CLOSED},\\
&\text{next genuinely new carrier}
&&\textbf{OPEN / LOAD-BEARING}.
\end{aligned}
}
\]

This is the boundary that should control the next branch.