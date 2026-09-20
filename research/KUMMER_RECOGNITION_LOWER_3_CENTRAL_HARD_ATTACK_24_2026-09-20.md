# HARD ATTACK 24 — Exact lower-3-central Kummer factorization and recognition boundary — 2026-09-20

## 1. Objective

Re-audit the claim that the lower 3-central quotient
\[
Q_k(G)=G/P_{k+1}(G)
\]
is sufficient for finite Kummer/orientation data. The previous record correctly separated factorization from recognition; this attack tightens the factorization proof and then asks whether the finite Kummer carrier itself contains a canonical selector.

## 2. Exact factorization lemma

Let
\[
A_k=\mathbf Z/3^k,\qquad U_k=1+3A_k\subset A_k^\times,
\]
and
\[
H_k=A_k\rtimes U_k,
\]
with multiplication
\[
(a,u)(b,v)=(a+ub,uv).
\]

Define the lower 3-central series by
\[
P_1(H_k)=H_k,\qquad P_{n+1}(H_k)=P_n(H_k)^3[P_n(H_k),H_k].
\]

For every \(n\ge1\),
\[
P_n(H_k)\subseteq 3^{n-1}A_k\rtimes(1+3^nA_k).
\tag{*}
\]

### Induction

For \(n=1\), the right side is exactly \(A_k\rtimes U_k\).

Assume (*). Write an element of \(P_n\) as \((a,u)\), with
\[
a\in3^{n-1}A_k,\qquad u\in1+3^nA_k.
\]

For the cube,
\[
(a,u)^3=(a(1+u+u^2),u^3).
\]
Because \(u\equiv1\pmod{3^n}\),
\[
1+u+u^2\equiv3\pmod{3^n},
\]
so the translation component lies in \(3^nA_k\). Also
\[
u^3\in1+3^{n+1}A_k
\]
(with the usual interpretation that the subgroup becomes trivial once the indicated power of 3 vanishes).

For a commutator with \((b,v)\in H_k\), the translation component is a sum of terms of the form
\[
(1-v)a
\quad\text{and}\quad
(u-1)b,
\]
up to sign/conjugation convention. Here
\[
1-v\in3A_k,\qquad u-1\in3^nA_k,
\]
so both terms lie in \(3^nA_k\). The \(U_k\)-component remains in \(1+3^{n+1}A_k\), since \(U_k\) is abelian and hence its internal commutators vanish.

Thus
\[
P_{n+1}(H_k)\subseteq3^nA_k\rtimes(1+3^{n+1}A_k),
\]
proving (*).

At \(n=k+1\),
\[
3^kA_k=0,\qquad1+3^{k+1}A_k=\{1\},
\]
hence
\[
\boxed{P_{k+1}(H_k)=1.}
\]

The edge case \(k=1\) is included: \(U_1=\{1\}\) and \(P_2(H_1)=3A_1=0\).

## 3. Consequence for candidate Kummer data

For any candidate
\[
\rho:G\to U_k
\]
and any crossed homomorphism
\[
f(gh)=f(g)+\rho(g)f(h),
\]
the map
\[
\Phi_{\rho,f}(g)=(f(g),\rho(g))
\]
is a homomorphism \(G\to H_k\). Since \(P_{k+1}(H_k)=1\),
\[
\Phi_{\rho,f}(P_{k+1}(G))=1.
\]
Therefore \((\rho,f)\) factors through \(Q_k(G)\).

This is now a clean theorem:

> **Finite Kummer factorization theorem (local).** Every finite candidate orientation/crossed-homomorphism pair with values in \(A_k\rtimes U_k\) is determined by its induced data on \(G/P_{k+1}(G)\).

No presentation choice enters this factorization statement.

## 4. Stronger recognition attack: the complete finite Kummer carrier

The natural q-blind finite object associated with this target is not a single crossed homomorphism but the entire family
\[
\mathcal K_k(Q)
=
\coprod_{\rho\in\operatorname{Hom}(Q,U_k)}
Z^1(Q,A_k(\rho)),
\]
together with its evident projection to the candidate-character set
\[
\pi:\mathcal K_k(Q)\to\operatorname{Hom}(Q,U_k).
\]

This makes the logical situation exact:

- factorization proves that the canonical pair, once known, lands inside \(\mathcal K_k(Q_k)\);
- recognition would require an intrinsically defined subobject
\[
\mathcal K_k^{\mathrm{can}}(Q)\subseteq\mathcal K_k(Q)
\]
whose projection selects exactly one \(\rho\), namely \(\chi\bmod3^k\);
- neither the existence of a point in a fiber nor nonzero \(f\) gives such a subobject.

Thus the problem is not merely “find a clever crossed homomorphism.” It is a **finite canonical-selection problem** inside a finite family of candidate coefficient actions.

## 5. A stronger obstruction to the naive route

Any criterion of the form
\[
\exists f\in Z^1(Q,A_k(\rho))
\]
is automatically true for every candidate \(\rho\), because \(f=0\) is always present.

Replacing existence by
\[
\exists f\ne0
\]
only asks whether the corresponding finite coefficient module has nontrivial first cohomology. That is an intrinsic property of the pair \((Q,\rho)\), but it is not by itself tied to the Demuškin orientation. To become a recognition theorem it would have to be proved that exactly one candidate \(\rho\) has the required property on the entire admissible category. No such uniqueness theorem is presently available.

Likewise, imposing a perfect-pairing or duality condition can select the known orientation, but unless the condition is independently derived from the declared finite filtered input, it risks simply restating the dualizing-module characterization of the orientation. Such a construction would fail the project's non-tautology gate.

## 6. New precise boundary

The lower-central threshold has therefore survived the strongest definitional attack available at this stage, but only at the factorization level:

\[
\boxed{
G/P_{k+1}
\text{ is sufficient to carry every finite }A_k\rtimes U_k\text{-Kummer pair.}
}
\]

The following stronger statement remains unproved:

\[
\boxed{
G/P_{k+1}
\text{ intrinsically and uniquely recognizes }
\chi\bmod3^k.
}
\]

The gap is exactly the construction of a q-blind, functorial, non-circular selector.

## 7. Binding next attack

The next attack is therefore not another numerical scan. It should test the selector problem itself:

1. Define the admissible finite-carrier category precisely.
2. Determine what information beyond \(\mathcal K_k(Q)\) is legitimately allowed: filtered commutator structure, extension classes, cup/Bockstein data, or another group-sensitive invariant.
3. Test whether any such structure yields a functorial singleton selector of \(\rho\).
4. In parallel, search for an admissible pair
\[
J_k(G)\cong J_k(G'),\qquad
O_k(G)\not\cong O_k(G'),
\]
which would give a genuine universal no-go.
5. Do not call the factorization theorem an orientation-recovery theorem.

## Decision

- Exact \(P_{k+1}(H_k)=1\) proof: **PASS / LOCAL**.
- Candidate Kummer factorization through \(G/P_{k+1}\): **PASS / LOCAL**.
- Complete finite Kummer carrier \(\mathcal K_k(Q)\): **PASS / LOCAL** as the correct bookkeeping object.
- Naive crossed-homomorphism existence as selector: **FAIL / CLOSED**.
- Nonzero crossed-homomorphism existence as selector: **OPEN / insufficient**.
- Canonical q-blind orientation selector from \(Q_k\): **OPEN**.
- Universal same-carrier/different-orientation no-go: **OPEN**.

No further numerical scan is authorized until a concrete selector predicate or an admissible counterexample construction is available.
