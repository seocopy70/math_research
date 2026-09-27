# FINITE-WINDOW RECOGNITION THRESHOLDS — FOUNDATIONAL DEFINITIONS AND N0/N1 AUDIT
## 2026-09-27

## Status

- Gate N0: **PASS / CLOSED**
- Gate N1: **PASS / CLOSED**
- Gate N2: **OPEN**
- Paper 2 affine factorization threshold \(f_{\mathrm{aff}}(k)=p^{k-1}+1\): **PASS / CLOSED** in the declared affine crossed-cocycle category.
- Equality between recognition and factorization thresholds: **OPEN**; no identification is assumed.
- Absolute carrier-independent minimality: **OPEN / category-dependent**.

This branch starts a new research program. It does not modify the frozen/current Paper 2 publication manuscript.

---

## 1. Pre-check

### Object

The new object is a category-relative recognition threshold attached to a target invariant \(T\), a class/category \(\mathcal C\), and a natural filtration \(D_\bullet\).

### Input

Only the finite filtered observation specified by the declared \(n\)-window is admissible. The target \(T\), the canonical orientation \(\chi\), and \(q\) are not inserted into the observation unless explicitly declared as part of the target or category.

### Functoriality

The finite window must be regarded as a filtered object, not merely as an unstructured list of vector spaces. Isomorphisms of \(n\)-windows are required to preserve the underlying quotient/group structure and the induced filtration.

### Gauge

No presentation, relator, Fox coordinate, preferred generator, or lift normalization is part of the definition.

### Orientation bridge

For the first target \(T_k=\chi\bmod p^k\), the bridge to the already proved affine/Kummer theory is deliberately postponed to Gate N2. The definition itself does not use the bridge.

### q-blindness

For the recognition invariant itself, \(q\) is not supplied to the window. Any later theorem must state whether the class \(\mathcal C\) fixes \(q\), allows varying \(q\), or uses a subclass on which \(q\) is externally part of the object.

### Separation

A lower bound requires an explicit pair \(G,H\in\mathcal C\) with isomorphic \(n\)-windows but non-isomorphic target values. No such pair is claimed here.

### Novelty

The definition is a framework-level construction. Novelty of any concrete theorem is a separate Gate N4/literature question. The known canonical Demushkin orientation is not claimed as new.

### Stop

No higher computation is authorized by this document until the observation category and target category are fixed for the concrete N2 problem.

---

## 2. Correct finite-window object

Let \(\mathcal C\) be an admissible class/category of filtered pro-\(p\) groups. For each \(G\in\mathcal C\), let
\[
G=D_1(G)\supseteq D_2(G)\supseteq\cdots
\]
be a natural filtration.

The notation \(D_{\le n}G\) is shorthand only. The actual \(n\)-window is the filtered quotient
\[
W_n(G):=
\bigl(G/D_{n+1}(G),\,D_1/D_{n+1},\ldots,D_n/D_{n+1}\bigr).
\]

Thus
\[
G\sim_n H
\]
means that \(W_n(G)\) and \(W_n(H)\) are isomorphic as filtered objects.

This avoids the ambiguity that would arise if \(D_{\le n}G\) were interpreted merely as an unordered collection of graded pieces.

---

## 3. Gate N0 — Recognition threshold

Let
\[
T:\mathcal C\longrightarrow\mathcal T
\]
be a target invariant, understood up to the declared notion of isomorphism in \(\mathcal T\).

Define
\[
\boxed{
r_T(\mathcal C;D_\bullet)
=
\min\left\{
n\ge1:
G\sim_n H\Longrightarrow T(G)\cong T(H)
\quad\forall\,G,H\in\mathcal C
\right\},
}
\]
with
\[
r_T(\mathcal C;D_\bullet)=\infty
\]
if no such \(n\) exists.

Equivalently, \(T\) is constant on the equivalence classes of \(\sim_n\).

This is a genuinely category-level definition: fixing one \(G\) would make \(T(G)\) already fixed and therefore would not define a meaningful recognition problem.

### Basic consequence

If \(r_T<\infty\), then every \(m\ge r_T\) also recognizes \(T\), provided the filtration windows are nested in the evident way.

Hence the threshold is a least recognizing depth, not merely an arbitrary admissible depth.

---

## 4. Factorization threshold

Let
\[
\mathcal O_k:\mathcal C\to\mathcal X_k
\]
be an observation functor and suppose \(G/P_n(G)\) is the relevant finite quotient.

Define
\[
\boxed{
f_{\mathcal O}(k)
=
\min\left\{
n:
\mathcal O_k
\text{ factors naturally through }
G\mapsto G/P_n(G)
\right\},
}
\]
with value \(\infty\) if no such \(n\) exists.

The word "naturally" is essential: factorization is a statement about the observation functor on the whole declared class, not about one selected group.

For the established affine crossed-cocycle observation of Paper 2,
\[
\boxed{
f_{\mathrm{aff}}(k)=p^{k-1}+1
}
\]
in the already audited affine category.

No claim is made here that
\[
r_T=f_{\mathcal O}.
\]

---

## 5. Gate N1 — Basic propositions

### Proposition N1.1 — Monotonicity

If
\[
r_T(\mathcal C;D_\bullet)=r<\infty,
\]
then every \(m\ge r\) recognizes \(T\).

**Proof.**
If \(W_m(G)\cong W_m(H)\), truncation gives \(W_r(G)\cong W_r(H)\). The defining property at depth \(r\) therefore gives \(T(G)\cong T(H)\). \(\square\)

---

### Proposition N1.2 — Separation lower bound

If there exist \(G,H\in\mathcal C\) such that
\[
W_n(G)\cong W_n(H)
\]
but
\[
T(G)\not\cong T(H),
\]
then
\[
\boxed{r_T(\mathcal C;D_\bullet)>n.}
\]

**Proof.**
The defining implication for recognition fails at depth \(n\). \(\square\)

This is the fundamental lower-bound mechanism for all future sharpness arguments.

---

### Proposition N1.3 — Target monotonicity

Suppose
\[
T=F\circ S
\]
for a functor \(F\) on the target category. Then
\[
\boxed{
r_T(\mathcal C;D_\bullet)
\le
r_S(\mathcal C;D_\bullet).
}
\]

**Proof.**
If the \(r_S\)-window determines \(S(G)\) up to isomorphism, applying \(F\) determines \(T(G)\) up to isomorphism. \(\square\)

In particular, for
\[
T_j(G)=\chi_G\bmod p^j,
\]
the reduction maps give
\[
r_{\chi\bmod p}
\le
r_{\chi\bmod p^2}
\le
r_{\chi\bmod p^3}
\le\cdots
\]
whenever all targets are defined on the same admissible class.

---

### Proposition N1.4 — Joint targets

Let
\[
T=(T_1,T_2).
\]
Then, with the product target equipped with componentwise isomorphism,
\[
\boxed{
r_{(T_1,T_2)}
=
\max\{r_{T_1},r_{T_2}\},
}
\]
with the usual convention that \(\max\) of an infinite value is infinite.

**Proof.**
For the upper bound, a window of depth \(\max(r_{T_1},r_{T_2})\) determines both components.

For the lower bound, if the joint target were recognized at depth \(n\), each component would be recognized by composing with the corresponding projection. Thus \(n\ge r_{T_i}\) for \(i=1,2\). \(\square\)

---

## 6. Important distinction: recognition versus factorization

The two thresholds answer different questions.

Factorization asks:

\[
\text{How deep must the finite window be before the chosen observation itself stops seeing deeper data?}
\]

Recognition asks:

\[
\text{How deep must the finite window be before the target is forced to be the same?}
\]

Therefore neither implication is automatic:

\[
f_{\mathcal O}(k)=n
\quad\not\Rightarrow\quad
r_T=n.
\]

A smaller recognition threshold can occur if the target is insensitive to information retained by \(\mathcal O\). Conversely, factorization of one observation does not imply that the target is intrinsically recoverable from the resulting quotient.

This distinction is now a controlling definition for the successor program.

---

## 7. Gate N2 — First concrete question

For a nontrivial recognition problem, fix an admissible Demuškin class containing at least the standard family members whose orientations are to be distinguished (in particular, the varying-(f) family used in the sharpness/q-collapse analysis), and let
\[
D_\bullet=\text{Zassenhaus filtration},
\qquad
T_k(G)=\chi_G\bmod p^k.
\]

The first substantive question is

\[
\boxed{
r_{\chi\bmod p^k}(\mathcal C;D_\bullet)
\stackrel{?}{=}
p^{k-1}+1.
}
\]

The right-hand side is already established as the affine factorization threshold, not yet as the recognition threshold.

### Authorized routes

The lower-bound route must use genuinely different admissible groups, not two presentations of one fixed group. In particular, a class containing only one isomorphism class makes the recognition problem degenerate.

1. **Lower bound:** construct \(G,H\in\mathcal C\) with
   \[
   W_{p^{k-1}}(G)\cong W_{p^{k-1}}(H)
   \]
   but
   \[
   \chi_G\bmod p^k\not\cong\chi_H\bmod p^k.
   \]

2. **Upper bound:** prove that the \((p^{k-1}+1)\)-window determines the target on the entire declared class.

3. If either route fails, classify the resulting boundary rather than assuming equality.

No absolute category-independent minimality claim is authorized.

---

## 8. Current classification

**N0: PASS / CLOSED.**

The recognition threshold is now defined at the correct category level using a genuine filtered finite-window object.

**N1: PASS / CLOSED.**

Monotonicity, separation lower bound, target monotonicity, and joint-target equality are proved.

**N2: OPEN.**

The relation between
\[
r_{\chi\bmod p^k}
\quad\text{and}\quad
f_{\mathrm{aff}}(k)=p^{k-1}+1
\]
is unresolved and is the next substantive gate.

No closed Fox/\(t_2\) branch is reopened. No new computation is claimed by this record.
