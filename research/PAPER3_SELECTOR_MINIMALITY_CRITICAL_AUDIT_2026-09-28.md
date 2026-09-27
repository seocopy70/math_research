# PAPER 3 — CRITICAL AUDIT OF SELECTOR MINIMALITY — 2026-09-28

Verdict: PASS / CLOSED, with one presentation correction required in the earlier minimality note.

The mathematical lower-window argument is sound for p=3, q=3, rank 4, all k>=2.

Important correction:
The proof is not literally “m<N implies chi_k does not factor”. The correct split is:
- m <= 3^(k-2): chi_k does not factor through W_m.
- 3^(k-2) < m <= 3^(k-1): chi_k does factor through W_m, but the Kummer lifting predicate fails even for chi_k.

For the second range, x_2 has exact order N=3^(k-1) in W_m because x_2^N lies in D_N subset D_m and its image in the abelianization has exact order N. Hence there is f in H^1(W_m,F_3) with f(x_2)=1.

If z lifted f to a crossed cocycle with canonical action u=(1-3)^(-1), then x_2^N=1 gives
S_N(u) z(x_2)=0,
S_N(u)=(u^N-1)/(u-1).
LTE gives v_3(S_N(u))=k-1, so z(x_2) is divisible by 3, contradicting f(x_2)=1.

Thus every m <= 3^(k-1) fails, while W_(3^(k-1)+1) is already known sufficient.

The proof is therefore a direct selector-minimality proof, not merely a consequence of affine factorization sharpness.

Additional scope caution:
The conclusion is for the fixed p=3, q=3, rank-4 group. The same endpoint calculation extends to q=p^f with f<k, but this does not establish a uniform theorem for all q, especially when f>=k and chi mod p^k is trivial.

Source audit:
Labute's canonical orientation formula for the standard relation x_1^q[x_1,x_2]... is independently supported in the literature, and the Zassenhaus formula is standard. Kummerianity is the surjectivity condition used here. Do not claim broader uniformity without a separate argument.

Status:
- fixed-group selector minimality: PASS/CLOSED
- proof's logical gap: CLOSED
- broader q-uniform minimality: OPEN
