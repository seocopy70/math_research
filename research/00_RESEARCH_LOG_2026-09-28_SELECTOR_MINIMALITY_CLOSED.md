# PAPER 3 — RESEARCH LOG ADDENDUM — 2026-09-28

## Intrinsic selector-window minimality CLOSED

The previously open absolute selector-window minimality question is now resolved for the fixed rank-4, q=3 pro-3 Demuškin group.

Let
\[
N=3^{k-1},\qquad W_m=G/D_m(G).
\]
The established theorem recognizes the canonical orientation at W_{N+1}. To prove that no W_m with m<=N suffices, split the lower range.

### 1. Very shallow range: m <= 3^{k-2}

In the free abelian x_2-direction, the Zassenhaus filtration is the power filtration. If e=ceil(log_3 m)<=k-2, then
\[
x_2^{3^e}\in D_m(G),
\]
while
\[
\chi_k(x_2)^{3^e}\ne1
\]
because chi_k(x_2)=(1-3)^(-1) has exact order 3^{k-1}. Hence chi_k does not factor through W_m.

### 2. Final block: 3^{k-2}<m<=3^{k-1}

Here ceil(log_3 m)=k-1. Thus chi_k does factor through W_m, but x_2 has exact order N=3^{k-1} in W_m: x_2^N lies in D_N(G) subset D_m(G), while the abelianization shows the order cannot be smaller.

Choose
\[
f\in H^1(W_m,F_3),\qquad f(x_2)=1.
\]
If f lifted to z in Z^1(W_m,A_k(chi_k)), then
\[
0=z(x_2^N)=S_N(u)z(x_2),
\quad u=(1-3)^{-1},
\]
with
\[
S_N(u)=\frac{u^N-1}{u-1}.
\]
LTE gives
\[
v_3(S_N(u))=k-1.
\]
Therefore p=3 divides z(x_2), contradicting z(x_2) mod 3 = f(x_2)=1.

So
\[
K_k(W_m,chi_k)\text{ fails}
\]
for every m in the final block.

Combining both ranges:
\[
\boxed{n_{selector}(k)=3^{k-1}+1.}
\]

This is a direct selector-minimality proof, not a deduction from affine-category sharpness.

### Final classification
- selector-window sufficiency at W_{3^{k-1}+1}: PASS/CLOSED;
- selector-window necessity at all m<=3^{k-1}: PASS/CLOSED;
- absolute intrinsic selector-window minimality at fixed p=3,q=3,d=4: PASS/CLOSED;
- extension to q=p^f with f<k: PASS/LOCAL from the same LTE calculation;
- uniform minimality for q with f>=k (where chi mod p^k becomes trivial): OPEN/separate;
- 1D cup carrier: PASS/CLOSED;
- O_k -> F_p canonical functional from E_k -> Q_k alone: OPEN/NOT LOAD-BEARING;
- publication novelty: OPEN/CONDITIONAL.

Detailed proof: research/PAPER3_SELECTOR_WINDOW_MINIMALITY_CLOSED_2026-09-28.md.
