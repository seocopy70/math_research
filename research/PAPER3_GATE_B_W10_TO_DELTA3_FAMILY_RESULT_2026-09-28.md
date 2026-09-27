# PAPER 3 — Gate B result: W_10 -> full delta_3 family

Date: 2026-09-28
Status: PASS / CLOSED

For Q=G/P_10 and N=P_10, the full family of connecting maps is determined functorially by W_10.

1. Gate A gives L(rho_2) = L_Q(rho_2) by inflation/restriction, and U2 gives H^1(Q,Z/9(rho_2)) ~= H^1(G,Z/9(rho_2)) for every candidate rho_3.

2. Since P_10 is contained in P_2=Phi(G), inflation H^1(Q,F_3) -> H^1(G,F_3) is an isomorphism. The five-term Hochschild-Serre sequence for 1 -> P_10 -> G -> Q -> 1 then makes inflation H^2(Q,F_3) -> H^2(G,F_3) injective.

3. Q is a nontrivial finite 3-group, so H^2(Q,F_3) is nonzero. Since G is Demushkin, dim H^2(G,F_3)=1. Hence inflation is an isomorphism:
H^2(Q,F_3) ~= H^2(G,F_3).

4. For every candidate rho_3, the coefficient short exact sequence exists already on Q:
0 -> F_3 -> Z/27(rho_3) -> Z/9(rho_2) -> 0.
Its quotient-level connecting map delta_Q is intrinsic. Naturality of connecting homomorphisms gives a commutative square with the corresponding G-level delta_G. Both vertical maps are isomorphisms, so delta_G is completely determined by delta_Q.

Therefore the entire family {delta_{3,rho_3}} is reconstructed from W_10 by finite quotient cohomology.

Independence checks:
- no presentation or relator gauge;
- no free-group lift;
- q is absent from the definition;
- only the already-closed mod-9 datum rho_2 is used;
- no H^2 basis normalization is needed.

U3 remains an independent explicit Fox realization, not the logical bridge.

Classification:
Gate B = PASS / CLOSED.

Detailed proof record is this document. The next gate is Gate C: whether the full family uniquely selects chi mod 27.
