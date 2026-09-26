# SUCCESSOR PUBLICATION CANDIDATE AUDIT — 2026-09-26

## Scope
This branch contains a new successor manuscript source, paper/successor_main.tex, constructed from the authoritative successor audits after the exact uploaded followup_merged.tex source could not be recovered from the repository or indexed conversation files. It is therefore a new working publication candidate, not a byte-for-byte repair of the uploaded source.

The frozen preceding manuscript paper/main.tex is untouched.

## Mathematical gates

### 1. Affine factorization depth
For
\[
S_k=A_k\rtimes U_{1,k},\qquad A_k=\mathbf Z/p^k\mathbf Z,
\]
the Zassenhaus calculation gives
\[
P_n(S_k)=p^{\lceil\log_p n\rceil}A_k\rtimes U_{\lceil\log_p n\rceil+1},
\]
hence
\[
P_{p^{k-1}}(S_k)\ne1,\qquad P_{p^{k-1}+1}(S_k)=1.
\]
Classification: PASS / CLOSED.

### 2. Arbitrary-candidate factorization
Every crossed cocycle defines a homomorphism to S_k; functoriality kills P_{p^{k-1}+1}. Classification: PASS / CLOSED.

### 3. Sharpness
- f < k: canonical orientation plus z(x_1)=1.
- f >= k: rho(x_2)=1+p, z(x_2)=1, using LTE.
- The second witness uses only x_1,x_2, so d=2 is included.
- No surjectivity of the orientation component is assumed.
Classification: PASS / CLOSED.

Thus
\[
n_{\mathrm{aff}}(k)=p^{k-1}+1
\]
is sharp for all odd p, all f>=1, and all even d>=2 in the specified affine crossed-cocycle category.

### 4. q-collapse
For f>=k, x_1^{p^f} dies in the finite quotient because it lies in P_{p^f} and p^f>p^{k-1}+1. The canonical orientation also reduces to the trivial principal-unit character at level p^k. Classification: PASS / LOCAL.

### 5. Recognition versus factorization
The free pro-p example is deliberately limited to the statement that the Kummer predicate itself does not force uniqueness, since cd_p(F_d)=1 makes every finite-level lifting map surjective. It is not presented as a universal impossibility theorem for every natural selector. Classification: PASS / LOCAL.

### 6. Free-product uniformity
The truncation functor T_n(G)=G/P_n(G) is a reflector onto the P_n=1 subcategory and preserves pro-p coproducts. This closes the mixed-commutator factorization issue for finite free products of Demushkin blocks. Classification: PASS / CLOSED.

Broader recursively defined elementary-type classes remain outside scope.

## Publication gates
- Preceding manuscript preservation: PASS / CLOSED.
- Successor source syntax: PASS / LOCAL static audit; exact GitHub CI result is not exposed by the available workflow-run status endpoint.
- Independent CI build: CONFIGURED / awaiting externally reported Actions result.
- Literature novelty: OPEN / CONDITIONAL.
- Absolute minimality beyond the affine category: OPEN / category-dependent.
- Broad ET_p uniformity: OPEN.

## Required next gate
Run the successor CI build from the exact branch commit, then perform a source-level audit of the CI-built manuscript. Do not promote this branch to a final submission package until CI and the independent audit both pass.
