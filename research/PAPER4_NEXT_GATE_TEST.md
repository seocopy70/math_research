# Paper 4 next gate test

## Status — 2026-10-05

The theorem-strengthening gate is now PASS / CLOSED.

### 1. General transfer-depth law

From
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K)
and Jennings–Lazard,
m=\lceil n/p\rceil,  e(n)=\lceil\log_p m\rceil
gives
\operatorname{im}(D_n(F)\cap K\to K^{ab})\subseteq p^{e(n)}K^{ab}.

Critical specialization:
n=p^s+1 \Longrightarrow e(n)=s,
hence TF_s.

Classification: PASS / CLOSED.

### 2. Complete critical-window classification

For W_{s,a}=W_{p^s+1}(G_{s,a}), the critical window is classified by a:

| range of a | critical-window information |
|---|---|
| 1\le a<s | pairwise distinguished by W_{s,a}^{ab}\cong \mathbf Z_p/p^a\oplus(\mathbf Z_p/p^{s+1})^d |
| a=s | same abelianization as a=\infty, but separated by \varepsilon_s |
| a>s | exactly equal to the a=\infty window |

Thus a=s is the unique nontrivial critical boundary and a>s is fully saturated.

Classification: PASS / CLOSED.

### 3. Intrinsic scope

The result is certified only for the declared intrinsic scope:
- odd p;
- s\ge2;
- even d;
- nondegenerate alternating quadratic initial relation r_2.

The nondegeneracy assumption is required for the current canonical cup-radical construction of K. Degenerate r_2 remains OPEN as an intrinsic-extension problem. The s=1 case remains unpromoted.

### 4. Publication-level interpretation

SC is infrastructure, not the novelty center. The stronger theorem is:

At the critical Zassenhaus window W_{p^s+1}, the stress-family exponent parameter a is completely classified: a<s survives in abelianization, a=s survives only through the intrinsic transfer obstruction \varepsilon_s, and a>s is invisible and exactly coincides with a=\infty.

The general SC-to-transfer law is a theorem-strengthening result; it should be presented with full attribution to the prior Zassenhaus/Jennings-Lazard/weighted-Schreier infrastructure and without claiming foundational novelty for SC itself.

### 5. Remaining work

The next high-value task is manuscript integration and independent proof/evidence audit, not further generic SC literature search.

Do not reopen:
- SC literature audit;
- arbitrary-r degree-only theorem;
- old order-jump proof;
- degenerate intrinsic construction without a new canonicality argument;
- s=1 by analogy alone.
