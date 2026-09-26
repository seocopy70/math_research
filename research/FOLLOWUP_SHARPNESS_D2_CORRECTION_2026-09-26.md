# 2026-09-26 — FOLLOW-UP SHARPNESS AUDIT CORRECTION

The prior follow-up audit incorrectly promoted the failure of a surjective witness G_f -> S_k in rank 2, f>1, to failure of affine factorization sharpness.

These are distinct claims:
1. existence of a surjective affine representation onto the full target S_k;
2. minimality of the uniform n such that every affine representation G -> S_k kills P_n(G).

Only (2) defines factorization-depth sharpness.

A direct witness closes the issue for rank d >= 2, every f >= 1, and every k >= 2: take the trivial coefficient character rho=1 and the additive cocycle/homomorphism z:G -> A_k with z(x_2)=1 and all other presentation generators sent to 0. The Demushkin relator has zero x_2-exponent sum, so this descends to G. Its image contains the full translation group A_k, and P_{p^{k-1}}(A_k)=p^{k-1}A_k is nonzero. Hence P_{p^{k-1}}(G) is not killed.

Combined with P_{p^{k-1}+1}(S_k)=1, this proves n_aff(k)=p^{k-1}+1 is sharp for the full affine crossed-cocycle category.

The earlier statement “rank 2, f>1: sharpness FAILS” is HISTORICAL / SUPERSEDED. The narrower statement “a surjective witness onto S_k may fail in rank 2, f>1” remains separate and is not load-bearing.

Other active classifications:
- undefined \\Fp source defect: FAIL/CLOSED;
- corrected crossed-cocycle equation and a_2=(1-p^f)^(-1): PASS/CLOSED;
- q-collapse threshold f >= k: PASS/LOCAL;
- Newton O(kd): CONDITIONAL pending an explicit input/cost model;
- recognition minimality: OPEN;
- frozen publication manuscript: unchanged.

A corrected successor draft was locally rebuilt three times; PDF SHA-256:
4dd138ec0b95a26963e7c0ae574c3257b8e9b556a2fd3aa434f86cc63eaed077

A corrected standalone audit report was also rebuilt three times; PDF SHA-256:
e3440c341551f266c0d70834a7686017f81111ef87d48afbd1d4

Next authorized step: integrate the corrected sharpness statement into the successor paper, then audit the ET_p / abstract-Q_k impossibility section separately.