# Paper 4 — SC Sharpness and Index-p^s Strengthening Audit — 2026-10-05

## Gate

**Target:** strengthen the certified subgroup-depth comparison
\[
D_n(F)\cap K\subseteq D_{\lceil n/p^s\rceil}(K),\qquad [F:K]=p^s,
\]
by (i) proving the factor \(p^s\) is uniformly sharp and (ii) isolating the exact index-\(p^s\) generalization.

**Classification: PASS / CLOSED** for both theorem statements below.

## 1. Index-p^s generalization

Let \(F\) be a finitely generated free pro-p group and let \(K\le F\) be open of index \(p^s\). Since \(F/K\) is a finite p-group, choose a subnormal chain
\[
F=K_0>K_1>\cdots>K_s=K,\qquad [K_{i-1}:K_i]=p.
\]
Every \(K_i\) is again free pro-p.

Applying the certified index-p comparison successively gives
\[
D_n(K_{i-1})\cap K_i
\subseteq D_{\lceil n/p\rceil}(K_i).
\]
Induction therefore yields
\[
\boxed{D_n(F)\cap K\subseteq D_{\lceil n/p^s\rceil}(K).}
\tag{SC_s}
\]

The ceiling identity needed at each step is, for integer \(m\ge1\),
\[
\left\lceil\frac{\lceil m/p\rceil}{p}\right\rceil
=\left\lceil\frac{m}{p^2}\right\rceil,
\]
and hence iteratively
\[
\left\lceil\frac{\cdots\lceil m/p\rceil\cdots}{p}\right\rceil
=\left\lceil\frac{m}{p^s}\right\rceil.
\]
This is an elementary integer identity.

## 2. Sharpness

The correct sharpness statement is **uniform sharpness**, not pointwise sharpness for every integer n.

Let \(F=\langle a,b\rangle\) be free pro-p and
\[
K=\ker\bigl(F\to C_{p^s}\bigr),
\qquad a\mapsto1,\quad b\mapsto0.
\]
A Schreier basis for \(K\) contains
\[
c_0=a^{p^s}.
\]
Thus \(c_0\) is a free generator of \(K\), so by the exact Zassenhaus degree of a free generator and its p-power tower,
\[
c_0^{p^{m-1}}\in D_{p^{m-1}}(K)\setminus D_{p^{m-1}+1}(K).
\]
Set
\[
g_m=a^{p^{m+s-1}}=c_0^{p^{m-1}},
\qquad n_m=p^{m+s-1}.
\]
Then
\[
g_m\in D_{n_m}(F)\cap K
\]
and
\[
g_m\notin D_{\lceil n_m/p^s\rceil+1}(K),
\qquad
\lceil n_m/p^s\rceil=p^{m-1}.
\]
Hence the replacement
\[
D_n(F)\cap K\subseteq D_{\lceil n/p^s\rceil+1}(K)
\]
is false in general, already on the infinite sequence \(n=n_m\).

For \(s=1\), this specializes to the simpler witness \(a^{p^m}\), with \(K=\ker(F\to C_p)\).

### Important scope correction

The stronger sentence sometimes proposed for arbitrary
\(n=p(m-1)+r\) — namely that suitable commutator corrections produce a sharp witness for every n — is **not needed and is not promoted**. It has not been independently proved here. The infinite family \(n=p^{m+s-1}\) is sufficient to establish optimality of the uniform factor \(p^s\).

## 3. What this proves for Paper 4

The universal theorem package is now:

1. **SC (index p):**
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K).
\]

2. **SC_s (index p^s):**
\[
D_n(F)\cap K\subseteq D_{\lceil n/p^s\rceil}(K).
\]

3. **Uniform sharpness:** the factor \(p^s\) cannot be replaced uniformly by a stronger depth bound \(\lceil n/p^s\rceil+1\).

4. **Critical transfer consequence:** combining SC_s with Jennings–Lazard gives the corresponding depth compression needed for the Paper-4 stress family; at \(n=p^s+1\) the previously certified transfer exponent is exactly \(s\).

The distinction is important: SC/SC_s are universal filtration infrastructure; the genuinely Paper-4-specific theorem remains the intrinsic transfer obstruction and the exact critical-window separation in the declared nondegenerate quadratic stress-family scope.

## 4. Result classification

- Index-p SC: **PASS / CLOSED**.
- Index-p^s SC_s: **PASS / CLOSED**.
- Uniform sharpness of SC_s: **PASS / CLOSED**.
- Pointwise sharpness for every n: **OPEN / not required**.
- SC as standalone literature novelty: **not claimed**; the audited weighted-Schreier literature supplies the component machinery.
- Paper-4 downstream intrinsic separation: **PASS / CLOSED** in the declared scope.

## 5. Publication wording

Do **not** write “we discovered the subgroup-depth inequality from scratch.” The defensible statement is:

> The paper isolates and proves the precise index-p subgroup-depth comparison needed for the finite-window argument, extends it functorially along index-p^s chains, and proves that the resulting p^s compression factor is uniformly optimal. The subsequent intrinsic transfer obstruction and critical-window separation are the Paper-4-specific contribution.

