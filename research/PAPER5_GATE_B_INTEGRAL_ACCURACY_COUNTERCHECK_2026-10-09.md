# Paper 5 Gate B — integral filtration comparison and accuracy counterexample audit (2026-10-09)

## Decision and scope

This is the agreed B-1 pre-check: test the accuracy claim before attempting the relation-level reduction or any higher-degree computation. Three claims are kept separate:

1. **Definition:** the integral weighted Magnus filtration is well-typed.
2. **Comparison:** its membership filtration agrees with the canonical mod-p Zassenhaus filtration on the free pro-p group.
3. **Precision extraction:** a particular coefficient in a relation residual yields a specified nonzero class in a specified associated-graded layer.

The proof below closes item 2 under the standard Zassenhaus product formula. It does **not** by itself prove item 3.

## 1. Definition

Let
\[
\mathcal A=\mathbb Z_p\langle\!\langle X,Y\rangle\!\rangle,
\qquad J=(X,Y).
\]
For each integer n>=1 define
\[
I_n^{\mathrm{int}}
=\overline{\sum_{\substack{i\ge1,\ j\ge0\\ ip^j\ge n}}p^jJ^i},
\]
where closure is in the completed (p,J)-adic topology. The index i starts at 1. The factor p^j is a scalar coefficient; it is not a group exponent.

Let F be the free pro-p group on x,y, and let mu:F -> 1+J be the integral Magnus homomorphism, mu(x)=1+X, mu(y)=1+Y.

## 2. Comparison theorem

**Theorem (integral weighted Magnus membership comparison).** For every n>=1 and g in F,
\[
\boxed{g\in D_n(F)\quad\Longleftrightarrow\quad \mu(g)-1\in I_n^{\mathrm{int}}.}
\]
Here D_n is the standard p-Zassenhaus filtration.

### Proof

**(a) Reduction modulo p.** The image of I_n^int in
\(\mathcal A/p\mathcal A=\mathbb F_p\langle\!\langle X,Y\rangle\!\rangle\)
is exactly J^n: all summands with j>=1 vanish, while the j=0 summands are J^i for i>=n. Hence
\[
\mu(g)-1\in I_n^{\mathrm{int}}
\implies \bar\mu(g)-1\in J^n
\implies g\in D_n(F),
\]
using the standard Magnus characterization of D_n.

**(b) The reverse inclusion.** By the Zassenhaus product formula,
\[
D_n(F)=\prod_{ip^j\ge n}\gamma_i(F)^{p^j}.
\]
For c in gamma_i(F), write \(\mu(c)=1+u\), with u in J^i; this is the integral Magnus lower-central estimate. Then
\[
\mu(c^{p^j})-1=(1+u)^{p^j}-1
=\sum_{k=1}^{p^j}\binom{p^j}{k}u^k.
\]
For k<p^j, the elementary identity
\[
k\binom{p^j}{k}=p^j\binom{p^j-1}{k-1}
\]
implies \(v_p(\binom{p^j}{k})\ge j-v_p(k)\). Thus the k-th term belongs to
\(p^{j-v_p(k)}J^{ik}\), whose defining weight satisfies
\[
ik\,p^{j-v_p(k)}\ge ip^j\ge n.
\]
The final term k=p^j is in J^{ip^j} and has the same required bound. Therefore \(\mu(c^{p^j})-1\in I_n^{\mathrm{int}}\). Since I_n^int is a two-sided ideal and products of units of the form 1+I_n^int remain in 1+I_n^int, the Zassenhaus product formula gives \(\mu(g)-1\in I_n^{\mathrm{int}}\) for every g in D_n. Taking closures preserves the inclusion. This proves the equivalence.

### Independent algebra check

The key valuation inequality was not assumed as an equality. It follows from the displayed identity and is sufficient for the weight bound. For k=p^j, use the separate final-term argument; do not apply j-v_p(k), which would be zero or negative.

**Classification: PASS / CLOSED**, conditional only on the standard Magnus characterization of D_n and the standard Zassenhaus product formula explicitly cited above.

## 3. Minimal accuracy countercheck

The comparison theorem is a membership theorem. It does **not** imply that p-adic coefficient precision shifts degree additively.

For a one-letter monomial X, the term p^r X lies in I_n^int exactly up to the threshold n<=p^r (and is not in I_{p^r+1}^int). Its weighted level is therefore p^r, not 1+r. In particular, the tempting additive rule “coefficient p^r on a degree-i term raises the degree to i+r” is **FAIL / CLOSED** for this filtration. The correct elementary weight rule for a monomial coefficient p^r J^i is multiplicative: its guaranteed level is i p^r.

This is a genuine counterexample to the additive-accuracy formulation, not a counterexample to the membership comparison theorem.

## 4. What remains open: the actual relation-residual accuracy statement

The research target must now specify a concrete coefficient functional and a concrete layer before it can be tested. The current notes do not yet define a canonical map from the integral residual
\[
\mu(\psi(w_0)w_0^{-\tilde\alpha})-1
\]
to a named one-dimensional or finite-dimensional quotient which is both:
- independent of integral Magnus coordinates / choices of lift; and
- sensitive to the proposed \(\delta_p(\tilde\alpha)\bmod p\) in a genuinely noncommutative relation residual.

The pure-power test is already a closed negative result:
\[
(x^{\tilde\alpha})^p x^{-p\tilde\alpha}=1.
\]
So no coefficient of that residual can detect \(\delta_p\). The coefficient must be derived from the two-variable relation residual after the degree-2 and degree-p cancellations, not guessed from the pure-power expansion.

### Pre-registered stop criterion

Do not run a higher-degree expansion until the next lemma states all four items:
1. the exact residual word and the allowed automorphism/lift parameters;
2. the exact quotient of \(I_m^{\mathrm{int}}/I_{m+1}^{\mathrm{int}}\) or other named target receiving its coefficient;
3. invariance under changing the integral Magnus coordinates / representative lift;
4. a falsification criterion: if the claimed \(\delta_p\)-coefficient vanishes identically in the first admissible noncommuting test, or changes under an allowed coordinate change, abandon that detector rather than increasing the degree.

## 5. Final classification

- Integral ambient object and weighted filtration definition: **PASS / LOCAL** (definition).
- Integral weighted Magnus membership comparison with D_n: **PASS / CLOSED** (proof above, under standard cited formulas).
- Additive coefficient-to-degree accuracy rule i+r: **FAIL / CLOSED**.
- Exact relation-level coefficient detector for \(\delta_p\): **OPEN / LOAD-BEARING**.
- Exact pro-p lift / Gate B: **OPEN / LOAD-BEARING**.

This audit does not promote Gate B. The next authorized action is to define the relation-level coefficient functional before computing it; no blind D_5/D_6/D_{p^k} sweep.


## 6. Reviewer clarification — scope of the accuracy counterexample (2026-10-09)

The user-side proof review confirms the membership comparison in Section 2: for group elements, integral membership is equivalent to the ordinary mod-p Magnus membership test. Thus the comparison theorem adds no p-adic precision to the *membership predicate* itself. Any additional information must come from a separately defined coefficient functional on a noncommutative relation residual, with a specified target quotient and lift/coordinate invariance. That functional remains undefined and **OPEN / LOAD-BEARING**.

The counterexample in Section 3 is intentionally narrow. The exact rejected candidate was the additive rule
`“a degree-i term with coefficient p^r has filtration degree i+r”`.
The monomial `p^r X` refutes that rule because its level under the defined weighted filtration is `p^r`. This does **not** refute a distinct relation-level coefficient-extraction theorem, nor any candidate formulation not asserting the additive `i+r` rule. Keep **FAIL / CLOSED** only for this explicitly stated additive rule; do not generalize it to “the accuracy theorem fails.”

No relation-residual computation is authorized until its exact residual word, target quotient/coefficient functional, invariance under allowed coordinate and lift changes, and pre-registered falsification criterion are specified.
