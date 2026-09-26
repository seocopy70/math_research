# SUCCESSOR TWO REMAINING PROBLEMS — CLOSURE AUDIT — 2026-09-26

## Scope

This audit addresses the two remaining successor-paper questions identified in CURRENT_STATE.md:
1. minimality of the finite depth, and
2. publication novelty / prior-art boundary.

The frozen publication manuscript is not modified.

## 1. Recognition minimality: category-relative closure

Absolute minimality over arbitrary invariants is not a well-posed claim without an admissible carrier category. The correct category already singled out by the successor theorem is:

> finite depth n for which every affine crossed-cocycle representation
> rho: G -> U_{1,k}, z: G -> A_k(rho)
> factors through Q_n(G)=G/P_n(G).

For the standard Demushkin family
G_f=<x_1,...,x_d | x_1^{p^f}[x_1,x_2][x_3,x_4]...=1>,
with odd p and d>=2, the threshold n(k)=p^{k-1}+1 is sharp.

### Lower-bound witness for f<k

Take the canonical orientation rho, with
rho(x_1)=1 and rho(x_2)=(1-p^f)^{-1}; all remaining generator values are 1.
Set z(x_1)=1 and z(x_i)=0 for i>1.

The relation obstruction is
p^f + rho(x_2)^{-1}(1-rho(x_2))
= p^f - p^f = 0 mod p^k,
so z is a valid crossed cocycle.

For m=p^{k-1},
z(x_1^m)=m=p^{k-1} != 0 mod p^k.
Since x_1^m lies in P_{p^{k-1}}(G_f) but its image under z is nonzero, this affine representation cannot factor through Q_{p^{k-1}}.

### Lower-bound witness for f>=k, including d=2

For d>=3 one may use the previously recorded x_3 witness. More importantly, d=2 is also covered directly.

Take
rho(x_1)=1, rho(x_2)=1+p,
z(x_1)=0, z(x_2)=1.

Because f>=k, the power term x_1^{p^f} is trivial modulo p^k. For the commutator relation,
z([x_1,x_2])=rho(x_2)^{-1}(1-rho(x_2))z(x_1)=0,
so z is a valid crossed cocycle.

For m=p^{k-1},
z(x_2^m)=((1+p)^m-1)/p.
By the standard lifting-the-exponent valuation,
v_p((1+p)^{p^{k-1}}-1)=k,
hence v_p(z(x_2^m))=k-1 and therefore
z(x_2^m) != 0 mod p^k.

Thus x_2^{p^{k-1}} is not annihilated by this affine representation, so factorization through Q_{p^{k-1}} fails.

The same argument works for every d>=2 by setting the unused generator values/cocycles to zero.

### Conclusion

The successor depth is not merely sufficient. In the affine crossed-cocycle factorization category, it is exactly sharp:

n_aff(k)=p^{k-1}+1, for d>=2 and all f>=1.

Classification:
**PASS / CLOSED — category-relative recognition-factorization minimality.**

This does not imply absolute minimality for arbitrary carriers.

## 2. Novelty / prior-art boundary

The literature audit confirms that the following are classical or already explicitly available:

- existence and uniqueness of the canonical Demushkin orientation as the unique Kummerian orientation: Labute, as summarized in later literature;
- Kummerian / 1-cyclotomic criteria and quotient-inheritance results: Efrat–Quadrelli and Quadrelli;
- standard oriented elementary-type constructions and Kummerian closure results: Quadrelli–Weigel;
- the 2026 Blumer–Quadrelli and Pál–Quick papers concern related orientation/cohomological/formality phenomena, but do not state the present finite-window affine factorization theorem.

The 2024 Quadrelli paper explicitly describes Kummerianity through finite-level twisted H^1 lifting and proves quotient-inheritance under additional restriction-surjectivity hypotheses. This is adjacent prior art, but it does not itself identify the sharp universal Zassenhaus depth p^{k-1}+1 for arbitrary affine crossed-cocycle representations.

The 2026 Pál–Quick papers detect q=3 versus q!=3 through A_3-formality/canonical Hochschild classes. They do not provide the present Q_k recognition/factorization statement.

The 2026 Blumer–Quadrelli paper studies failures of 1-cyclotomic orientation for other pro-p groups; it does not give the present sharp finite-window recognition theorem.

Therefore the defensible novelty boundary is:

1. “Canonical Demushkin orientation is new” — CLOSED / NON-NOVEL.
2. “Kummerianity/1-cyclotomicity is new” — CLOSED / NON-NOVEL.
3. “A finite quotient Q_k can be used in the present affine twisted-obstruction factorization” — distinct and not located verbatim in the audited literature.
4. “The exact depth p^{k-1}+1 is sharp for all affine crossed-cocycle representations” — distinct from the classical orientation theorem and not located verbatim in the audited literature.
5. “Bare abstract Q_k determines the canonical orientation without naturality/functoriality hypotheses” — not established and must not be claimed.
6. The publication-level novelty of the combined theorem remains **CONDITIONAL**, because an exhaustive literature search cannot prove absence of an equivalent formulation, and some ingredients are consequences/reformulations of known Kummerian theory.

Classification:
**OPEN / CONDITIONAL — novelty cannot honestly be promoted to unconditional CLOSED solely by literature search.**

## 3. Final successor status

The two genuine open questions are therefore reduced to:

- absolute minimality over a broader, explicitly defined carrier category;
- exact publication-priority wording / exclusion of an equivalent prior formulation.

The first has now been closed in the natural affine crossed-cocycle factorization category.
The second remains conditional by its nature and should be handled as a novelty-boundary statement, not as a mathematical gap.

No further computational scan is authorized merely to strengthen either conclusion.
