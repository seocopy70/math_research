# HARD ATTACK 32 — LHS MIDDLE/TOP ROW AUDIT AFTER HARD ATTACK 31

## 2026-09-20

### 1. Critical review of the current bottleneck

Hard Attack 31 correctly closes the naive cokernel/Fitting defect
\[
\operatorname{coker}\bigl(\operatorname{Hom}_Q(M,A)\xrightarrow{\delta}H^2(Q,A)\bigr),
\]
because it is exactly the quotient-inflation image in \(H^2(G,A)\). This is the \(q=0\) edge contribution and therefore cannot reproduce the canonical PD^2 top class.

However, the phrase “the remaining possibility is a genuinely secondary operation” must be sharpened. There are two qualitatively different candidates in the LHS filtration:

1. the middle term
\[
E_\infty^{1,1}\subseteq H^1(Q,H^1(N,A)),
\]
which uses only \(H^1(N,A)\), hence is potentially recoverable from the finite relation module \(M=N/(N^{3^k}[N,N])\);

2. the top term
\[
E_\infty^{0,2}\subseteq H^2(N,A)^Q,
\]
and the differential
\[
d_3^{0,2}:E_3^{0,2}\to E_3^{3,0}.
\]
The second candidate is immediately suspect: its domain carries the \(Q\)-action on \(H^2(N,A)\), which for a PD^2 open subgroup is already orientation-bearing. Using it directly risks re-importing the target.

Thus the genuinely non-tautological next object is **not** \(d_3\) by itself. It is the middle-row survivor \(E_\infty^{1,1}\), provided its differential can be reconstructed from the finite extension data without importing \(H^2(N,A)\).

### 2. What the spectral sequence actually says

For
\[
1\to N\to G\to Q\to1,
\qquad A=A_k(\rho),
\]
the LHS spectral sequence is
\[
E_2^{p,q}=H^p(Q,H^q(N,A))\Rightarrow H^{p+q}(G,A).
\]
The low-degree filtration of \(H^2(G,A)\) has the three possible graded pieces
\[
E_\infty^{2,0},\qquad E_\infty^{1,1},\qquad E_\infty^{0,2}.
\]
The seven-term extension of the five-term sequence places the middle term in
\[
H^1(Q,H^1(N,A))\longrightarrow H^3(Q,A),
\]
with the displayed map being the relevant \(d_2^{1,1}\). Standard spectral-sequence bookkeeping confirms that \(E_\infty^{1,1}\) is the kernel of this differential once the preceding page is reached. citeturn0search21turn0search0

This is important because \(E_\infty^{1,1}\) is not the same object as the cokernel closed in Hard Attack 31.

### 3. Finite-input legitimacy gate

There is a real load-bearing issue here.

Although
\[
H^1(N,A)\cong\operatorname{Hom}(M,A)
\]
is determined by the finite module \(M\), it does **not automatically follow** that the LHS differential
\[
d_2^{1,1}:H^1(Q,H^1(N,A))\to H^3(Q,A)
\]
is determined by the truncated extension \((Q,M,E)\).

The differential is an extension-level secondary operation. It must therefore be constructed from the finite extension itself, or from an explicitly defined finite derived object canonically equivalent to that differential. Merely observing that its source is finite is insufficient.

This is the exact analogue of the earlier mistake “H^2(G,A) should factor through Q because rho and Z^1 do.” The source being finite does not prove the differential is finite-input functorial.

### 4. The d3 route is even more dangerous

Because \(G\) and \(N\) have cohomological dimension 2, the only potentially relevant higher differential leaving the top row is
\[
d_3^{0,2}:H^2(N,A)^Q\to H^3(Q,A).
\]
But the \(Q\)-module structure of \(H^2(N,A)\) is precisely where the restricted PD^2 orientation enters. For the canonical coefficient action \(A_k(\chi)\), the twisted top class is the expected orientation-compatible class.

Therefore:

- defining \(d_3\) after explicitly adjoining \(H^2(N,A)\): **FAIL / CLOSED** as a non-tautological filtered carrier;
- defining a finite object whose construction independently reconstructs the same top-row action: **OPEN**, but this is the original hard problem in different notation.

No claim is made that \(d_3\) itself is impossible; only that it does not pass the non-tautological input gate merely by existing.

### 5. A sharper candidate: the middle-row survivor

Define, if and only if the finite-extension construction below can be proved:
\[
T_k^{\mathrm{mid}}(G,\rho)
:=
E_\infty^{1,1}
\subseteq
H^1(Q_k,\operatorname{Hom}(M_k,A_k(\rho))).
\]

The intended selector would be a basis-free condition on this finite module, for example vanishing, prescribed Fitting length, or a prescribed annihilator filtration.

This is genuinely different from Hard Attack 31:
- it is not the quotient-inflation image;
- it does not require a preferred element of \(\operatorname{Hom}_Q(M,A)\);
- it uses the interaction between the candidate coefficient action and the extension's secondary obstruction.

But **uniqueness is completely unproved**. In particular, \(T_k^{\mathrm{mid}}=0\) must not yet be advertised as a selector.

### 6. Canonical orientation sanity check

For the canonical coefficient action, PD^2 duality gives
\[
|H^2(G,A_k(\chi))|=3^k.
\]
The quotient-inflation piece is zero by Hard Attack 31. The canonical top class survives in the top row. Hence the middle graded piece must be trivial:
\[
E_\infty^{1,1}(G,\chi)=0.
\]

This is a useful **necessary condition**, not a recognition theorem:
\[
\rho=\chi\quad\Longrightarrow\quad T_k^{\mathrm{mid}}(G,\rho)=0.
\]
The converse is the decisive unknown.

### 7. Current logical boundary

The research state is therefore:

- Hard Attack 31: quotient/cokernel defect — **FAIL / CLOSED**.
- Direct \(H^2(N,A)\) or top-row action — **FAIL / CLOSED** as non-tautological input.
- Raw \(d_3^{0,2}\) — **FAIL / CLOSED** as a carrier definition if its top-row module is imported.
- Finite reconstruction of \(d_2^{1,1}\) from \((Q,M,E)\) — **OPEN / load-bearing**.
- Middle survivor \(T_k^{\mathrm{mid}}=E_\infty^{1,1}\) — **OPEN / decisive**.
- Selector \(T_k^{\mathrm{mid}}=0\iff\rho=\chi\) — **OPEN**.
- Universal no-go — **OPEN**.

### 8. Discovery insight

The structural pattern is now clearer:

\[
\boxed{
\text{q=0 quotient row}
\;\xrightarrow{\text{closed}}
\;\text{q=1 middle extension row}
\;\xrightarrow{?}
\;\text{q=2 orientation row}
}
\]

The first row is too shallow; the third row is tautological if imported. The middle row is the only remaining spectral-sequence layer that can plausibly carry a new finite, q-blind obstruction without directly inserting the orientation class.

This is therefore the next attack/discovery target, not another arbitrary enrichment.

### 9. Stop rule

No numerical scan is authorized yet. Before computation, one must prove:

1. a canonical finite definition of the relevant \(d_2^{1,1}\) or equivalent middle-row defect from \((Q_k,M_k,E_k)\);
2. functoriality under admissible group/gauge morphisms;
3. independence from presentations and coefficient bases;
4. q-blindness;
5. a precise candidate selector predicate.

Only after these gates pass is a standard-family scan logically authorized.
