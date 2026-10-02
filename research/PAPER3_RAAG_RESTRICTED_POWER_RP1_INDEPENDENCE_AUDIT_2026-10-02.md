# RP-1 — Restricted-q-Power Independence Lemma — 2026-10-02

## Decision

The previously unproved independence assertion in the complete 3-vertex counterexample can be closed.

For
G = <s,a,b | a s a^{-1}=s^{1+q}, b s b^{-1}=s^{1+q}, [a,b]=1>,
with q=p^f (f>=1), the three classes
  \bar s^[q], \bar a^[q], \bar b^[q] in L_q=D_q/D_{q+1}
are linearly independent.

Consequently
  P_q^{-1}(im B_q)=F_p \bar s
is PASS / LOCAL in the complete 3-vertex model.

The proof is presentation-independent in the required sense: it uses only natural quotient homomorphisms and functoriality of the Zassenhaus filtration, together with the intrinsic Jennings characterization.

## 1. Exact statement

Let
  L_1=D_1/D_2,  L_q=D_q/D_{q+1}.
Because the underlying complete graph is abelian at degree 1, the restricted q-power map P_q on L_1 is F_p-linear. We must prove
  {\bar s^[q],\bar a^[q],\bar b^[q]}
is linearly independent in L_q.

It is enough to prove that each coefficient in
  alpha \bar s^[q] + beta \bar a^[q] + gamma \bar b^[q] = 0
vanishes.

## 2. Detection of the a- and b-directions

Set s=b=1. The defining relations become trivial and the quotient is the pro-p cyclic group <a> ~= Z_p.

For Z_p, the Zassenhaus filtration is D_n=<a^{p^e}> where p^e>=n. Hence a^q lies in D_q but not D_{q+1}; equivalently
  \overline{a^q} != 0 in D_q/D_{q+1}.

The natural map G -> <a> induces
  L_q(G) -> L_q(<a>)
and sends
  \bar a^[q] -> \overline{a^q},
  \bar s^[q], \bar b^[q] -> 0.

Therefore beta=0.

The same argument with s=a=1 gives gamma=0.

## 3. Detection of the s-direction

The remaining coefficient alpha is detected by the finite semidirect quotient
  H = C_{p^{f+1}} \rtimes C_p,
where
  C_p=<t>,
  C_{p^{f+1}}=<u>,
and
  t u t^{-1} = u^{1+q}.

This is well-defined because
  (1+q)^p \equiv 1 mod p^{f+1}
for q=p^f.

Define G -> H by
  s -> u,  a -> t,  b -> 1.
All defining relations of G are respected.

In the group algebra F_p[H], Jennings' theorem identifies D_n(H) with the elements h for which h-1 lies in the n-th power of the augmentation ideal I. In the cyclic subgroup <u> of order p^{f+1},
  u^q-1 = (u-1)^q
in characteristic p.
Moreover (u-1)^q is nonzero modulo I^{q+1}; the powers
  1,(u-1),...,(u-1)^{p^{f+1}-1}
are linearly independent in F_p[C_{p^{f+1}}].

Hence
  u^q \notin D_{q+1}(H),
so
  \overline{u^q} != 0 in L_q(H).

The induced graded map sends
  \bar s^[q] -> \overline{u^q},
  \bar a^[q] -> \overline{t^q}=0,
  \bar b^[q] -> 0.
Thus alpha=0.

Therefore the three classes are linearly independent.

## 4. Linearity of P_q in this model

This point must be stated precisely.

A restricted p-operation is not generally additive. However here L_1 is abelian:
  [L_1,L_1]=0.
For an abelian restricted Lie algebra over F_p, the Jacobson cross terms vanish, so
  (x+y)^[p]=x^[p]+y^[p].
Since scalars lie in F_p, (lambda x)^[p]=lambda x^[p].
Iterating gives an F_p-linear map
  P_q=L_1 -> L_q.

Thus the preimage calculation is legitimate in this complete model. The argument does not claim that P_q is linear for arbitrary specially oriented graphs.

## 5. Consequence for the complete 3-vertex counterexample

The intrinsic extension defect satisfies
  im B_q = F_p \overline{s^q}.
The independence lemma gives
  P_q^{-1}(im B_q)=F_p \bar s.

So the correct local chain is
  finite extension defect -> defect image in L_q
  -> restricted q-power source -> sinkhole line.

This is strictly stronger than the failed Grassmannian carrier: the Grassmannian support forgets the distinction between the sinkhole and tilted planes, whereas the restricted-power source map retains it.

## 6. Presentation-independence audit

The proof does not use a preferred normal form inside L_q beyond naming the three generators for the concrete test model.

The actual vanishing/nonvanishing tests are transported by group homomorphisms. The Zassenhaus filtration is functorial under homomorphisms, and its associated graded is a restricted Lie algebra. Thus the independence conclusion is a statement about the concrete filtered group and its natural quotient maps, not about a choice of coordinates in a presentation.

This is sufficient for the local lemma. It is not yet a theorem that an arbitrary abstract finite window can reconstruct the individual source quotient maps without additional intrinsic construction.

## 7. What this does NOT prove

1. It does not prove that P_q is linear on a general specially oriented RAAG.
2. It does not define a q-blind carrier for the general class.
3. It does not prove functoriality of the proposed carrier beyond the local filtered-group construction.
4. It does not provide the orientation bridge in general.
5. It does not prove a canonical sinkhole complement in the rank-2 case.
6. It does not establish novelty.

## 8. Classification

- RP-1 independence in complete 3-vertex model: **PASS / LOCAL**.
- P_q^{-1}(im B_q)=F_p \bar s in that model: **PASS / LOCAL**.
- General restricted-power preimage carrier: **OPEN / LOAD-BEARING**.
- General linearity of P_q: **FAIL as a blanket claim / CLOSED**; only special models with the required abelian degree-one bracket justify it.
- Categorical no-go for all finite-window carriers: **OPEN / NOT ESTABLISHED**.

## 9. Next authorized gate

The next gate is not another Grassmannian calculation.

It is:

**RP-2 — determine the correct intrinsic meaning of the restricted-power preimage when L_1 is non-abelian, starting with the 3-vertex common-sink model and then the smallest non-complete graph.**

The key question is whether one can replace the nonlinear map P_q by a canonical filtered construction whose q-degree source can still be separated from the ordinary degree-2 sector.

No universal orientation theorem is claimed before that gate is closed.
