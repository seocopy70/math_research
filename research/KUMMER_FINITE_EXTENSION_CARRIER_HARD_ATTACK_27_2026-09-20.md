# KUMMER FINITE EXTENSION CARRIER HARD ATTACK 27 — 2026-09-20

## Active gate

Hard Attack 26 closed only the automatic inference
P_{k+1}(A_k(rho)⋊U_k)=1 => H^2(G,A_k(rho)) is determined by Q_k=G/P_{k+1}(G).

The next candidate was a finite extension/2-cell carrier (Q_k,E_k). This attack asks whether the most obvious intrinsic finite extension object is well-defined, finite, q-blind, and sufficient for the twisted top obstruction.

## 1. Candidate definition

Fix k>=1 and put

N=P_{k+1}(G),  Q_k=G/N,

and define the finite N-module

M_k(G)=N / (N^{3^k}[N,N]).

Because G is finitely generated pro-3 and N=P_{k+1}(G) has finite index, N is finitely generated; hence M_k(G) is finite.

The subgroup N^{3^k}[N,N] is characteristic in N and N is characteristic in G. Therefore it is normal in G, and we obtain a finite extension

1 -> M_k(G) -> E_k(G) -> Q_k -> 1,

where

E_k(G)=G/(N^{3^k}[N,N]).

The Q_k-action on M_k is part of the object, so the candidate carrier is the extension object

J_k^{ext}(G)=(Q_k,M_k,E_k).

This construction uses only the lower-3-central filtered input. It does not insert q or chi.

## 2. Why this is the correct first extension datum

For every candidate rho:Q_k->U_k, the module A_k(rho) is N-trivial. Therefore

H^1(N,A_k(rho)) = Hom_cont(N,A_k(rho))

and, because A_k has exponent 3^k,

Hom_cont(N,A_k(rho)) is determined by M_k(G).

Thus J_k^{ext} contains exactly the finite kernel information that appears in the first nontrivial extension term of the Hochschild–Serre five-term sequence.

This is a genuine strengthening over the bare quotient Q_k: it retains the first-order 2-cell/extension information lost when N is discarded.

The general Hochschild–Serre spectral sequence has
E_2^{p,q}=H^p(Q_k,H^q(N,A_k(rho))),
so the dependence on the extension kernel is structurally real.

## 3. Hard attack: is J_k^{ext} sufficient for H^2?

No automatic sufficiency theorem follows.

The total-degree-two terms include not only

H^2(Q_k,A_k(rho))

and

H^1(Q_k,H^1(N,A_k(rho))),

but also

H^0(Q_k,H^2(N,A_k(rho))).

The last term is invisible from M_k alone. In general, H^2(N,A_k(rho)) is not determined by the abelianized exponent-3^k quotient M_k.

Therefore the implication

J_k^{ext}(G)  =>  H^2(G,A_k(rho))

is NOT established merely from the definition of J_k^{ext}.

This is not a counterexample to J_k^{ext}; it is a sufficiency failure of the proposed proof route. A genuine counterexample pair has not been constructed.

## 4. Demushkin-specific circularity test

For the present Demushkin setting, N=P_{k+1}(G) is an open subgroup. Its H^2 is therefore part of the same PD^2/duality structure that carries orientation information.

Consequently, simply adjoining enough data to recover H^2(N,A_k(rho)) risks importing the desired dualizing action or an equivalent orientation object.

This exposes a sharp design constraint:

- adding M_k is legitimate finite extension information;
- adding H^2(N,A_k(rho)) as an independent component is potentially circular;
- any successful enrichment must encode the needed top-degree obstruction through a q-blind relation/extension class, not by attaching the canonical orientation itself.

## 5. Relation to the standard one-relator calculation

The standard-family obstruction row

d_1=q+u_2^{-1}-1,
d_2=0,
d_3=-(u_4-1)/(u_3u_4),
d_4=(u_3-1)/(u_3u_4)

still gives the unique rho=chi mod 3^k.

Hard Attack 27 does NOT yet prove that this row is a functor of J_k^{ext}. That would require an explicit natural map from the finite extension object to the relevant relation/2-cell obstruction.

Thus no standard-family numerical scan is authorized merely because J_k^{ext} has been defined.

## 6. Gate audit

Object: PASS / LOCAL.
Input: PASS / LOCAL — q and chi are absent.
Functoriality: PASS / LOCAL at the level of characteristic subgroups and induced finite extension.
Finiteness: PASS / LOCAL.
Gauge/presentation independence: OPEN — must be proved for the induced extension object and its use in the obstruction.
Orientation bridge: OPEN.
q-blindness: PASS / LOCAL at construction level.
Separation: OPEN for this carrier as a carrier, despite known standard-family separation of Q_k itself.
Novelty: OPEN.
Sufficiency of J_k^{ext}: OPEN; the naive H^2-factorization proof route fails.
Compression: OPEN and not yet meaningfully testable.

## 7. Decision

The candidate finite extension

J_k^{ext}(G)=(Q_k,M_k,E_k)

survives the definition gate and is the first precise finite replacement for the vague phrase “extension/2-cell data”.

However, the attack shows that the obvious relation-module truncation is not by itself enough to reconstruct twisted top cohomology. The missing piece is a finite, non-circular representation of the relevant 2-cell/top obstruction.

Classification:

- finite extension carrier definition: **PASS / LOCAL**;
- automatic H^2 reconstruction from (Q_k,M_k,E_k): **FAIL / CLOSED as an inference**;
- J_k^{ext} as a universal orientation carrier: **OPEN**;
- adding H^2(N,A_k(rho)) directly: **CONDITIONAL / circularity risk**;
- genuine finite 2-cell obstruction attached to J_k^{ext}: **OPEN / next target**.

## 8. Exact next attack

Do not enlarge the carrier blindly.

The next attack is to determine whether the one-relator PD^2 relation itself has a finite extension-theoretic representative inside E_k, namely a canonical class/function of the finite extension whose evaluation on A_k(rho) reproduces the twisted obstruction row.

The required theorem has the form

J_k^{ext}(G)
  ->  T_k(G)

where T_k is a finite, q-blind, gauge-independent obstruction object, followed by

T_k(G) + rho
  ->  Z/3^k

whose vanishing is equivalent to rho=chi mod 3^k on the admissible Demushkin category.

If no such T_k can be defined without importing H^2/duality orientation data, that failure should be promoted to a precise logical boundary rather than replaced by a larger circular carrier.
