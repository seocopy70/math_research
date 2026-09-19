# ORIENTATION MOD-9 — RELATIVE MINIMALITY AUDIT — 2026-09-19

## Objective

Push the remaining categorical-minimality question as far as possible without introducing an arbitrary category or running a finite scan.

The target is to distinguish a genuine lower-bound theorem from the stronger, currently unjustified statement that the projective degree-(2,3) relation jet is absolutely minimal.

---

## 1. Carrier under consideration

The established sufficient carrier is the projective relation jet

\[
J_3=[(R,P)]
\subset \mathbf P(L_2\oplus L_3^{res}),
\]

with nonzero quadratic projection, modulo the already audited degree-(2,3) gauge

\[
(R,P)\sim(uR,uP+[v,R]).
\]

The recovery functional is

\[
\Theta_J(\lambda)(f)
=
f(P)+(\lambda\wedge f)(R),
\]

and its zero set is the recovered mod-9 orientation digit.

For the frozen examples,

\[
J_3(3)=
[(X_1\wedge X_2+X_3\wedge X_4,\;X_1^{[3]})],
\]

while

\[
J_3(\infty)=
[(X_1\wedge X_2+X_3\wedge X_4,\;0)].
\]

---

## 2. A precise relative lower bound

Let \(\mathcal C_{2,3}\) be any class of admissible carriers obtained from the degree-(2,3) relation data by a natural forgetting/quotient operation, and suppose the mod-9 recovery map factors through it.

Then the carrier cannot identify two relation jets whose \(\Theta\)-zero sets are different.

Indeed, if

\[
Q(J)=Q(J')
\]

but

\[
Z(\Theta_J)\ne Z(\Theta_{J'}),
\]

a recovery map defined on \(Q(J)\) would have to return two different orientation digits from the same carrier object, which is impossible.

Therefore every successful quotient carrier must retain enough information to determine the zero set of \(\Theta\).

This is the exact categorical content available without choosing a larger category.

---

## 3. Consequence for the bare graded object

The bare associated graded restricted Lie object forgets the filtered coupling between \(R\) and \(P\).

For q=3 and q=infinity it identifies the quadratic graded relation while

\[
\chi_3\not\equiv\chi_\infty\pmod9.
\]

Equivalently,

\[
Z(\Theta_{J_3(3)})
=
\{e_2^*\},
\qquad
Z(\Theta_{J_3(\infty)})
=
\{0\}.
\]

Hence the recovery map cannot factor through the bare graded object.

This upgrades the earlier information-theoretic obstruction to a categorical statement **relative to the forgetful functor that discards the filtered relation coupling**:

\[
\boxed{
\mathsf{Rec}_{9}
\not\cong
\overline{\mathsf{Rec}}_{9}\circ
\mathsf{Forget}_{P}.
}
\]

Thus the degree-3 relation contribution is not optional within this carrier hierarchy.

---

## 4. Why this is not yet absolute minimality

There are at least three different notions that could all be called “smaller”:

1. a smaller vector-space realization;
2. a quotient object in a fixed category of relation jets;
3. a different natural invariant not presented as a quotient of \(J_3\).

Only (2) admits a meaningful categorical minimality question, and even there the category and morphisms must be fixed first.

Moreover, the mathematically smallest object through which a particular recovery function factors is formally its own image (here, essentially the recovered zero-set data). That would make the word “minimal” tautological unless the admissible carrier category is constrained independently of the recovery target.

Therefore the statement

> “\(J_3\) is categorically absolutely minimal”

cannot be proved from the current data alone.

---

## 5. Strongest result available now

The following relative minimality theorem is justified:

> **Relative lower-bound theorem.**
> In the category of admissible filtered relation carriers obtained by forgetting information from the degree-(2,3) relation jet, any carrier through which the intrinsic mod-9 orientation recovery factors must retain enough information to distinguish relation jets with different \(\Theta\)-zero sets. In particular, forgetting the degree-3 relation component and retaining only the bare quadratic/associated-graded relation cannot recover \(\chi\bmod9\).

This is stronger than merely saying “the bare graded calculation failed”: it identifies the precise information that any successful factorization must preserve.

---

## 6. The remaining categorical gap

To prove actual minimality one must first define a category whose objects include, at minimum,

\[
(V,[R], [P]\ \mathrm{relative\ to}\ R)
\]

with:

- admissible gauge equivalences;
- morphisms induced by filtered group isomorphisms;
- a forgetful functor to the quadratic graded datum;
- a precise notion of quotient/subobject or factorization.

Only after this category is frozen can one ask whether \(J_3\) is initial, terminal, minimal, or a minimal sufficient factor for the recovery functor.

No such category is currently fixed in the repository.

---

## 7. Decision

- **Relative lower bound:** PASS / CLOSED.
- **Bare graded forgetful factor:** FAIL / CLOSED.
- **Absolute categorical minimality of \(J_3\): OPEN.**
- No finite scan is authorized.

The next legitimate mathematical task is therefore **category definition first**, not a search for another numerical invariant.
