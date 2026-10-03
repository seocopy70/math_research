# PAPER 5 — TARGET CLASS INTRINSIC CHARACTERIZATION AUDIT
## 2026-10-03

### Question

Can the admissible target class itself be characterized from the finite target group, without naming the externally supplied Demushkin group (D), the marked quotient map (W_n\twoheadrightarrow Q_n), or a characteristic kernel in (W_n)?

### Scope

Odd (p), even rank (d\ge2), critical depth (n\ge3). Let (F_d) be the free pro-(p) group of rank (d), with Zassenhaus filtration (D_i(F_d)). Let
[
e(n)=\lceil\log_p n\rceil,
qquad
A_{d,n}=(\mathbf Z/p^{e(n)}\mathbf Z)^d.
]
Let (D^{(0)}_d) denote the rank-(d), torsion-invariant (q=0) Demushkin group and
[
Q_{d,n}=D^{(0)}_d/D_n(D^{(0)}_d).
]

The target-free class candidate is the following.

### Definition: finite Demushkin shadow class (mathcal C_{d,n})

A finite (p)-group (H) belongs to (mathcal C_{d,n}) iff there exist

1. a free pro-(p) group (F_d) of rank (d);
2. a relator (r\in D_2(F_d)\setminus D_3(F_d));
3. whose initial form (ar r\in D_2(F_d)/D_3(F_d)) induces a nondegenerate alternating bilinear form on (F_d/D_2(F_d)\cong\mathbf F_p^d);

such that
[
H\cong F_d/\bigl(\overline{\langle\!\langle r\rangle\!\rangle D_n(F_d)}\bigr)
]
and
[
H^{\mathrm{ab}}\cong A_{d,n}.
]

No (D), orientation, quotient map, chosen generator, or (q)-parameter occurs in this definition.

### Main theorem

[
oxed{\mathcal C_{d,n}=\{Q_{d,n}\}}
]
up to abstract isomorphism.

Thus the admissible target class is intrinsically characterized as a singleton isomorphism class by an existential finite one-relator/Demuškin-shadow condition plus the intrinsic abelianization condition.

### Proof

Let (H\in\mathcal C_{d,n}). Choose (F_d,r) as in the definition and put
[
G=F_d/\overline{\langle\!\langle r\rangle\!\rangle}.
]

Because the presentation is minimal and has one relator, (G) is a one-relator pro-(p) group. The degree-two initial relation is nondegenerate alternating. The standard relation--cup-product formula identifies this initial form with the mod-(p) cup pairing. Hence the cup product on (H^1(G,\mathbf F_p)) is nondegenerate. In the odd-(p) case this is exactly the Demushkin condition for the one-relator group. Labute's classification therefore applies.

For an infinite Demushkin group of odd (p), the isomorphism type is determined by rank (d) and the torsion invariant (q\in\{0,p,p^2,\ldots\}). In the standard normal form,
[
r\sim x_1^q[x_1,x_2][x_3,x_4]\cdots[x_{d-1},x_d].
]
The finite quotient at Zassenhaus depth (n) is obtained by imposing (D_n(F_d)=1).

Set (e=\lceil\log_p n\rceil). In the abelianization of (F_d), the image of (D_n(F_d)) is (p^e\mathbf Z_p^d). Therefore the abelianization of the (q=0) shadow is
[
Q_{d,n}^{\mathrm{ab}}\cong(\mathbf Z/p^e)^d.
]

If the classified Demushkin lift has (q=p^a<n), then its abelianization before truncation is
[
\mathbf Z_p^{d-1}\oplus \mathbf Z_p/p^a\mathbf Z_p,
]
and after quotienting by (D_n) one obtains
[
H^{\mathrm{ab}}
\cong
(\mathbf Z/p^e)^{d-1}\oplus
\mathbf Z/p^a,
]
which contradicts the defining condition
(H^{\mathrm{ab}}\cong(\mathbf Z/p^e)^d).

Consequently the classified lift has either (q=0) or (q\ge p^e\ge n).

If (q\ge n), then (x_1^q\in D_q(F_d)\subseteq D_n(F_d)), so the power term disappears in the depth-(n) quotient. Hence
[
F_d/\bigl(\overline{\langle\!\langle
x_1^q[x_1,x_2]\cdots[x_{d-1},x_d]
\rangle\!\rangle D_n(F_d)\bigr)
\cong
F_d/\bigl(\overline{\langle\!\langle
[x_1,x_2]\cdots[x_{d-1},x_d]
\rangle\!\rangle D_n(F_d)\bigr)
=Q_{d,n}.
]

The (q=0) case is already (Q_{d,n}). Thus every (H\in\mathcal C_{d,n}) is isomorphic to (Q_{d,n}).

Conversely, the standard (q=0) Demushkin presentation has nondegenerate degree-two initial form and its depth-(n) quotient has abelianization (A_{d,n}), so (Q_{d,n}\in\mathcal C_{d,n}).

This proves the equality.

### What is genuinely intrinsic here

The definition uses only:

- the abstract finite (p)-group (H);
- its minimal generator rank;
- existence of a one-relator pro-(p) lift;
- the intrinsic Zassenhaus filtration of the free lift;
- nondegeneracy of the degree-two relation/cup form;
- the abstract abelianization of (H).

It does **not** use:

- the previously selected quotient (W_n\twoheadrightarrow Q_n);
- a characteristic kernel of (W_n);
- a chosen (z,x_i) in the source window;
- the canonical orientation;
- the stress parameter (q=p^a);
- the external identity of (D).

The construction is therefore target-free at the level of the target class.

### Why this does not contradict the C2 no-go

C2 ruled out a characteristic kernel in (W_n) selecting a unique marked quotient map. The present theorem does something different: it characterizes the *isomorphism class of the target object* by a presentation-free existential property of the target group itself.

Thus:

- unique quotient kernel inside (W_n): impossible;
- unique target isomorphism class: possible;
- unique marked quotient map: still impossible;
- realization groupoid of admissible maps: one component;
- target class as an internal isomorphism class: now characterized.

The distinction is essential.

### Functoriality and gauge

The class (mathcal C_{d,n}) is invariant under abstract group isomorphism by construction. Different choices of free lift, free basis, and relator are gauge data. Labute's classification removes that gauge at the level of the resulting infinite Demushkin group, and the depth-(n) quotient is consequently independent of those choices.

The target-side object is therefore a genuine isomorphism class, not a marked presentation.

### q-blindness

The construction is deliberately q-blind. It does not attempt to recover the stress parameter (q=p^a). The abelianization condition only excludes (q<n); all (q\ge n), together with (q=0), collapse to the same finite target at depth (n). This is not a defect: it is exactly the finite-window equivalence expected from the Zassenhaus truncation.

Hence the correct intrinsic target is the equivalence class
[
q=0\quad\text{or}\quad q\ge n,
]
not an individual infinite Demushkin parameter.

### Orientation bridge

This theorem characterizes the target group (Q_n), but it does not by itself recover the orientation character on (D), nor does it recover the marked map from (W_n). The orientation bridge remains the separate relative obstruction theorem already established.

The combined Paper-5 architecture is therefore:
[
W_n
longrightarrow
\text{intrinsically characterized target class }\mathcal C_{d,n}
\cong\{Q_n\}
]
followed by
[
\text{admissible quotient-realization orbit/category}
longrightarrow
\text{relative split/non-split Boolean}.
]

### Logical boundary

The theorem is target-class characterization, not yet coarsest compression.

It does not prove that the target class can be reconstructed *from (W_n) alone without first knowing that an admissible realization exists*. That is a separate existence/factorization statement.

It also does not prove a universal theorem for arbitrary finite (p)-groups or arbitrary free-by-Demushkin extensions.

### Literature boundary

The underlying classification input is classical: Demushkin groups are one-relator pro-(p) groups with one-dimensional (H^2) and nondegenerate cup product, and Labute's classification gives the normal form and complete invariants. The modern literature also records the quadratic/graded characterization of Demushkin groups. These facts are not claimed as new.

The new structural statement for this project is the finite-shadow consequence:

> after forgetting the external target (D), the class of finite critical targets is still a singleton isomorphism class, because the only residual Demushkin parameter visible at depth (n) is whether (q<n), and the intrinsic abelianization condition excludes exactly that case.

This is the finite target-class factorization needed to remove the external target label from the realization category.

### Independent verification

1. The Zassenhaus formula
[
D_n(F)=\prod_{ip^j\ge n}\gamma_i(F)^{p^j}
]
shows (p^eF\subseteq D_n(F)\) on abelianization, with (e=\lceil\log_p n\rceil). citeturn4search0
2. Labute's classification gives the odd-(p) normal form (x_1^q\prod[x_{2i-1},x_{2i}]) and completeness by rank and (q). citeturn3search0turn3search18
3. The one-relator/nondegenerate-cup-product criterion is standard in the Demushkin classification. citeturn0search0turn2search12
4. The graded restricted-Lie / quadratic-dual description confirms that the degree-two relation is an intrinsic Demushkin shadow, rather than an arbitrary presentation artifact. citeturn1search1turn2search16

### Classification

- finite Demushkin-shadow target class (mathcal C_{d,n}): **PASS / CLOSED**;
- target-class uniqueness up to abstract isomorphism: **PASS / CLOSED**;
- canonical marked quotient map (W_n\twoheadrightarrow Q_n): **FAIL / CLOSED** from C2;
- target-free realization category of admissible quotients: **PASS / LOCAL → upgrade justified once existence is attached to the C2 orbit theorem**;
- recovery of the target class from (W_n) alone without an existence hypothesis: **OPEN**;
- coarsest intrinsic finite realization/minimality: **OPEN**;
- full universal Paper-5 theorem for arbitrary free-by-Demushkin families: **OPEN**.

### Stop / next boundary

The target-class problem itself is closed for the declared odd-(p), even-rank Demushkin stress family.

The remaining load-bearing question is no longer “what is the target class?” It is:

> Can the existence of an admissible realization (W_n\twoheadrightarrow H) with (H\in\mathcal C_{d,n}) be characterized intrinsically from (W_n), and can the resulting realization groupoid be defined without any external reference to (D)?

No new carrier search is authorized before that input/existence question is settled.
