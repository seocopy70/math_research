# Paper 5 Gate B — exact identity and D6 correction audit — 2026-10-08

Status: PROVED for odd-p a=-1; PROVED for p=3 diag(a,1,a); OPEN / LOAD-BEARING for ord(a)>2.


## Exact identity

With [u,v]=u^{-1}v^{-1}uv and r=z^p x^{-p}[x,y]^{-1}, define
Phi(x)=x^{-1}, Phi(y)=x^{-(p+1)} y x^{p+1}, Phi(z)=z^{-1}.
For c=[x,y],
Phi(c)^{-1}=x^{-p} c x^p, hence
Phi(r)=z^{-p}x^p Phi(c)^{-1}=z^{-p}c x^p=z^{-p}r^{-1}z^p.

Therefore Phi preserves the relator normal closure and induces a continuous endomorphism of G. Its Frattini-quotient linear part is diag(-1,1,-1), hence it is surjective; finite generation plus Hopf gives an automorphism.

For p=3 this is diag(2,1,2), and therefore the full diag(a,1,a)-type diagonal torus is PROVED. This is not “all diagonal scalars”.

## Correct D6 discovery path

The earlier wording “Phi_0 passes through T=9” is SUPERSEDED. The accurate path is:

gauge structure -> Phi_0 -> correction pattern -> x^{-4} y x^4 -> exact identity.

Here k=1 (Phi_0) passes through D5 but fails at D6. One weight-4 correction repairs D6; one additional weight-5 correction closes D7. The coefficients match binom(4,j) mod 3 = (1,0,1,1), pointing to k=4=p+1. Thus the Magnus T<=9 evidence concerns k=4, not k=1.

The corrected group-level D6 realization remains PASS / LOCAL. The affine/gauge counts 729->81->27 and 27->3->1 are discovery evidence only. The earlier five-way D6 structural selection based on solver/gauge representatives is HISTORICAL / SUPERSEDED (artifact).

## p=5, a=2

Gate B requires only Phi(r) to lie in the relator normal closure. A conjugate of a power of r is merely a sufficient route, not the definition of success.

The earlier claim that a weight-(p+2) error must be cancelled by a weight-(p+1) correction is CONJECTURE / UNVERIFIED.

Next target: smallest finite filtered correction -> gauge quotient -> structural pattern -> exact all-degree factorization or compatible pro-p lift. Blind D7/D8 continuation is not authorized.

## Withdrawn routes

- old J-membership test: HISTORICAL / SUPERSEDED
- old xc-order route: HISTORICAL / SUPERSEDED
- “E_2 in ND_10 PASS” as a Gate-B conclusion: HISTORICAL / SUPERSEDED

The corrected D6 result itself remains PASS / LOCAL.

## Reproduction evidence

Free-group identity check: PAPER5_GATE_B_EXACT_IDENTITY_FREE_GROUP_CHECK.py. This named script is not currently present in the GitHub repository, so it is not claimed as a repo artifact. The identity was reported checked for p=3,5,7,11,13 and by hand. Magnus evidence: k=4 passes through T<=9; k=1 fails at D6.

## Current classification

- a=-1, odd p: PROVED
- p=3 diag(a,1,a) torus: PROVED
- p=3,a=2 finite D3-D6 realization: PASS / LOCAL
- general ord(a)>2: OPEN / LOAD-BEARING
- p=5,a=2 pro-p realization: OPEN / LOAD-BEARING
- full Paper 5 p^2 theorem: OPEN / LOAD-BEARING
