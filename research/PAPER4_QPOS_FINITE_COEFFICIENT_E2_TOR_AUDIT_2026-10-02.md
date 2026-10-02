# PAPER 4 — Q>0 FINITE-COEFFICIENT E2 TOR CHECK — 2026-10-02

## New correction

The earlier closure “untwisted E2 has no q>0 continuation” is correct only for **Z_p coefficients**. With finite coefficients A_m=Z/p^m, a Tor term survives:

H_2(D,A_m) ≅ Tor_1^{Z_p}(H_1(D,Z_p),A_m)
        ≅ Tor_1(Z/p^a,Z/p^m)
        ≅ Z/p^{min(a,m)}

for standard odd-p Demushkin D with q=p^a>0.

This does NOT reopen the deep-tail route.

## Explicit stress-model transgression calculation

For
G_{s,a}=<z,x_1,...,x_d | z^{p^s}=r_D>,
the trivial-coefficient one-relator cellular row for D is multiplication by p^a in the x_1 coordinate.

If m>a, a generator of H_2(D,A_m) is represented in the 2-chain model by p^{m-a} times the relation cell. In G_{s,a}, the lifted relation defect is z^{p^s}. Therefore the finite-coefficient transgression sends the Tor generator to

    p^{m-a} z^{p^s}
    = p^{m-a+s} z

in the relevant cyclic coefficient quotient.

Hence if s>=a,

    m-a+s >= m,

so the image is zero in Z/p^m.

Thus for the deep regime s>a,

    finite-coefficient untwisted E2 transgression = 0

for every m.

For s<a, the same formula can carry partial information (the image has order p^{a-s}); this is a shallow-q regime and is irrelevant to the present deep-tail target.

## Interpretation

The finite-coefficient Tor source is real but its transgression is killed by exactly the p^{m-a} factor forced by the q=p^a torsion in H_1(D). Therefore it cannot recover extension depth s>a.

This strengthens, rather than weakens, the negative boundary:

q>0, s>a:
- Z_p H_2 source: absent;
- finite-coefficient Tor H_2 source: present but transgression-zero;
- H_1/coinvariant extension: saturated;
- ordinary mod-p graded: blind.

## Classification

- finite-coefficient H_2(D,Z/p^m): PASS / LOCAL;
- finite-coefficient E2 transgression for s>a in the stress model: FAIL / CLOSED;
- “all untwisted homological E2 layers are exhausted for the deep-tail target”: PASS / LOCAL for the stated one-relator stress model;
- arbitrary free-by-Demushkin universal closure: NOT CLAIMED;
- genuinely nonabelian relation/extension object: OPEN / LOAD-BEARING;
- finite-window factorization of such an object: OPEN.

## Important boundary

The calculation does not prove that every nonlinear invariant is finite-window blind. It proves that simply changing Z_p coefficients to Z/p^m does not rescue the untwisted E2 route.

Detailed next-gate audit remains:
research/PAPER4_QPOS_CRITICAL_REVIEW_NEXT_GATE_2026-10-02.md
