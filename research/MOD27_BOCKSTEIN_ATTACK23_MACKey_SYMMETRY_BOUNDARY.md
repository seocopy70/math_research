# HARD ATTACK 23 — MACKEY/TRANSFER ENRICHMENT SYMMETRY TEST — 2026-09-20

## Target

The previous attack suggested enriching \(\mathcal B_{27}\) by restriction/corestriction data over open subgroups. This attack tests whether that enrichment can actually rigidify the missing logarithmic lift.

## 1. Candidate enrichment

Let \(\mathfrak B_{27}(G)\) denote the system of
\[
\mathcal B_{27}(U)
=
(H^1(U,\mathbf F_3),H^1(U,\mathbf Z/9),\mathrm{red},\iota,\smile,\beta_1,\beta_9)
\]
for open subgroups \(U\le G\), together with the natural restriction, corestriction, and conjugation maps wherever defined.

This is substantially richer than the single-group carrier and is genuinely group-functorial.

## 2. Universal coefficient symmetry

For every \(c\in(\mathbf Z/9)^\times\) with
\[
c\equiv1\pmod3
\]
there is a coefficient automorphism
\[
T_c:H^1(U,\mathbf Z/9)\to H^1(U,\mathbf Z/9),\qquad a\mapsto ca,
\]
for every open subgroup \(U\).

Take identity on \(H^1(U,\mathbf F_3)\) and on \(H^2(U,\mathbf F_3)\). Then:
- \(T_c\) commutes with reduction because \(c\equiv1\pmod3\);
- \(T_c\) commutes with \(\iota\) because \(3c=3\pmod9\);
- the mod-3 cup product is unchanged;
- \(\beta_9(T_c a)=c\,\beta_9(a)=\beta_9(a)\) in \(H^2(U,\mathbf F_3)\);
- \(\beta_1\) is unchanged for the same reason;
- all restriction, corestriction, and conjugation maps commute with multiplication by \(c\).

Thus the entire Mackey/transfer-enriched package has a global coefficient symmetry \(T_c\).

## 3. Effect on the desired orientation

The logarithmic orientation class satisfies
\[
\lambda_{27}(G)=\frac13\log\chi_G\in H^1(G,\mathbf Z/9).
\]
For \(q=3\),
\[
\lambda_{27}(x_2)=1\pmod9.
\]
Hence
\[
T_4(\lambda_{27})=4\lambda_{27}\ne\lambda_{27}.
\]

Therefore the enriched cohomological package, even after adding all subgroup restriction/corestriction data, does not by itself carry a canonical choice of the characteristic-zero lift in the abstract coefficient-functor category.

This is stronger than the original \(S\)-symmetry: the symmetry is now compatible with the entire Mackey system, not just one \(H^1\)-group.

## 4. Crucial admissibility boundary

As before, \(T_c\) is a coefficient-system automorphism, not an automorphism of the underlying group. The project's current admissible morphisms are group isomorphisms/gauges, so this is **not** a group-level no-go theorem.

But it closes a tempting successor route:

> merely adding restriction/corestriction/conjugation to the trivial-coefficient Bockstein package does not remove the coefficient-lift symmetry.

To break this symmetry, the next carrier must contain some genuinely group-sensitive extension datum that is not equivariant under \(T_c\).

## 5. Literature cross-check

Generalized Bockstein constructions are naturally tied to augmentation filtrations, open-subgroup comparison, corestriction, and Massey products. They therefore validate the structural relevance of Mackey/transfer enrichment. But these constructions do not, by themselves, supply the canonical Demuškin orientation character. Any use of a procyclic quotient character \(\chi\) as defining input would be circular for this project.

## 6. Decision

- Mackey/transfer enrichment is mathematically natural: **PASS / LOCAL**;
- global coefficient-lift symmetry survives the enrichment: **PASS / CLOSED**;
- Mackey/transfer enrichment alone as a new mod-27 orientation carrier: **FAIL / CLOSED** as an abstract coefficient-functor carrier;
- group-level universal no-go: **OPEN**;
- independent orientation bridge: **OPEN**;
- Bockstein branch: **CONDITIONAL / OPEN**, but only with genuinely new group-sensitive structure.

## 7. Stop consequence

The project should **not** spend further effort enlarging the same trivial-coefficient Bockstein/Mackey package. The missing information is not more bookkeeping of the same coefficient-extension system.

The next meaningful carrier must break the \(c\equiv1\pmod3\) coefficient symmetry by using genuinely group-sensitive filtered extension information. Candidate directions include:
1. a mixed filtered relation datum whose extension class transforms nontrivially under the coefficient symmetry;
2. a secondary/tertiary cohomological operation with an intrinsic, non-circular defining system;
3. a characteristic-zero filtered object strictly below the full Fox carrier.

No one of these is yet authorized as a positive construction. The branch is closed against further Bockstein/Mackey elaboration.
