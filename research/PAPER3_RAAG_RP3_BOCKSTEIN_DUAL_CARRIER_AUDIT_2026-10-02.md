# RP-3 — Bockstein-dual carrier candidate — 2026-10-02

## Critical result

The load-bearing Delta_q problem admits a materially simpler intrinsic candidate: do not try to reconstruct a degree-q defect image inside L_q first. Recover the sinkhole sector from the first nonzero higher Bockstein on H^1.

For q=p^f, let beta_f denote the first potentially nonzero higher Bockstein detected by the coefficient tower. Define
  K_f := ker(beta_f) subset H^1(G,F_p),
and
  C_f := K_f^perp subset L_1 = H^1(G,F_p)^*.

In the two audited local models this C_f agrees with the RP span-preimage carrier:
- complete special 3-vertex: C_f = F_p sbar;
- common-sink model: C_f = span{ybar,zbar}.

## General special-digraph calculation

For a specially oriented oriented pro-p RAAG with q=p^f, let S be the set of sinkholes. From the minimal presentation, abelianization has the form
  G^ab ~= Z_p^{V-S} direct-sum (Z/q)^S.
Indeed, every directed relation contributes w^q=1 in abelianization, while ordinary-edge relations contribute no abelian relation; special orientation ensures directed edges point into the sinkhole vertex.

For a cyclic factor Z_p, all higher Bocksteins on H^1 vanish.
For a cyclic factor Z/q=Z/p^f, the first nonzero higher Bockstein occurs at level f and is nonzero on its degree-one generator. This is the standard cyclic Bockstein calculation; Efrat's p-Zassenhaus/cohomology framework identifies one-letter Bockstein classes with p-power directions.

Consequently, for the direct-sum abelianization above, beta_f has kernel exactly the character subspace supported on V-S, and therefore
  (ker beta_f)^perp = span_Fp{sinkhole classes}.
Thus the sinkhole sector can be recovered intrinsically from cohomology, without constructing Delta_q inside L_q.

## q-blindness

The construction is q-blind if f is not supplied. Scan the Bockstein tower for H^1(G,F_p) and take the first level f at which the higher Bockstein is nonzero. Then q=p^f is discovered rather than input.

For the special RAAG class, this is exactly the first exponent appearing in the abelianization torsion.

## Important boundary

This does NOT yet prove that beta_f is computable from exactly the previously fixed finite window W_q,W_{q+1}, nor that the construction agrees with span P_q^{-1}(Delta_q) for arbitrary nonabelian W_q. Those are separate statements.

It does, however, show that Delta_q is not logically necessary for the final orientation carrier if the Paper 3 object is allowed to use intrinsic cohomology of the finite quotient.

## Classification

- Intrinsic sinkhole carrier via first nonzero Bockstein: **PASS / LOCAL** on complete and common-sink models; **PASS / LOCAL-to-GENERAL candidate** for specially oriented RAAGs, pending finite-window factorization.
- General Delta_q construction: **OPEN / NON-LOAD-BEARING for orientation recovery**.
- q-blind discovery via first nonzero Bockstein: **OPEN / LOAD-BEARING only for finite-window factorization**.
- Orientation bridge after Bockstein carrier: **PASS / LOCAL-to-GENERAL candidate**; the quotient dual identifies sinkhole vs non-sinkhole directions.
- Restricted-power carrier remains useful as a structural cross-check, not necessarily the primary carrier.

## Literature alignment

Efrat's p-Zassenhaus work explicitly identifies one-letter cohomology classes with Bockstein classes and establishes their duality with p-power directions in the filtration; higher-length classes correspond to Massey products. This is exactly the separation needed here. The oriented pro-p RAAG literature defines the canonical orientation by assigning 1+q to sinkholes and 1 to non-sinkholes.

Next gate: prove finite-window factorization of this Bockstein carrier, preferably directly from W_{q+1} rather than via Delta_q.
