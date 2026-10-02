# RP-2 — Common-Sink Nonlinearity and Span-Preimage Refinement — 2026-10-02

## Decision

The naive statement
  P_q^{-1}(im kappa_q) = origin plane
is too strong in the 3-vertex common-sink model when the origin subgroup is non-abelian.

The correct local statement is the **span-preimage** identity:
  Span_Fp{ x in L_1 : P_q(x) in im kappa_q }
  = V_1,
where V_1 is the ordinary/origin plane.

This removes the need for P_q to be linear.

## Model

G=<x,y,z | x y x^{-1}=y^{1+q}, x z x^{-1}=z^{1+q}>,
with V=<y,z> free pro-p and x the common sinkhole.

At degree q the extension-defect image is
  im kappa_q = span{ \bar y^[q], \bar z^[q] }
inside L_q.

## 1. Why the raw preimage is not the origin plane

The origin subgroup V is free pro-p, hence its associated graded restricted Lie algebra is the free restricted Lie algebra on \bar y,\bar z.

For p=3 and q=3, the Jacobson identity gives
  (\bar y+\bar z)^[3]
   = \bar y^[3] + \bar z^[3] + Lambda_3(\bar y,\bar z),
where the cross term Lambda_3 is a nonzero degree-3 Lie element in the free restricted Lie algebra.

Therefore
  \bar y+\bar z notin P_3^{-1}(span{\bar y^[3],\bar z^[3]}).

So the raw preimage is not the whole origin plane. This is the concrete manifestation of the nonlinearity warning.

## 2. But the linear span of the preimage is exactly the origin plane

First, \bar y and \bar z themselves lie in the preimage because
  P_q(\bar y)=\overline{y^q},
  P_q(\bar z)=\overline{z^q},
and both classes belong to im kappa_q.

Hence
  V_1=span{\bar y,\bar z}
is contained in the span of the preimage.

Conversely, let
  x_0 = alpha \bar x + u,
  u in V_1,
be any degree-one class whose q-power lies in im kappa_q.

Consider the natural quotient
  G -> <x> ~= Z_p
obtained by killing y and z.

The image of im kappa_q is zero in L_q(<x>), while the image of P_q(x_0) is
  alpha^q \bar x^[q].
The q-th power of the generator of Z_p is nonzero in degree q. Hence alpha=0.

Therefore every element of the raw preimage already lies in V_1, and so
  Span(preimage) subseteq V_1.

Combining both inclusions:
  Span(preimage)=V_1.

## 3. Classification

- blanket linearity of P_q: **FAIL / CLOSED**.
- raw preimage equals origin plane in the non-abelian-origin model: **FAIL / CLOSED**.
- span-preimage equals origin plane in the common-sink model: **PASS / LOCAL**.
- intrinsic common-sink origin-plane recognition: **PASS / LOCAL**, conditional on the intrinsic extension-defect image.
- general non-abelian W_q defect construction: **OPEN / LOAD-BEARING**.
- general directed/sinkhole separation: **OPEN / LOAD-BEARING**.

## 4. Structural consequence

The restricted-power refinement should therefore not be defined as a preimage set. The correct candidate is

  C_q(G)
  := Span_Fp { x in L_1 : P_q(x) in Delta_q },

where Delta_q is the intrinsically defined degree-q extension-defect image.

The span operation is essential: it converts a nonlinear fiber into a canonical vector subspace.

This is a materially stronger candidate than the raw preimage and survives both tested local geometries:

1. complete 3-vertex model:
   C_q = F_p \bar s;

2. 3-vertex common-sink model:
   C_q = span{\bar y,\bar z}.

In both cases the complementary quotient
  L_1/C_q
is the sinkhole direction.

## 5. Critical limitation

This does not yet solve the general case. For non-abelian W_q, Delta_q cannot simply be defined as the image of a global bilinear kappa_q. A separate intrinsic construction must isolate the degree-q extension defect after the ordinary degree-2 sector is removed.

Thus RP-2 closes the **nonlinearity issue at the local model level**, but it does not close the general carrier.
