# PAPER 4 — GATE E1: K–Z RELATION DEFECT AUDIT — 2026-10-02

For G_s=<x,y,z | z^(p^s)=[x,y]>, N_s=cl(<z>) and D=G_s/N_s ~= Z_p^2, Palaisti's relation defect is the coinvariant class of the lifted D-relator in W_s=N_s/Phi(N_s).

The lifted relator is w=[x,y]=z^(p^s). Since Phi(N_s)=N_s^p[N_s,N_s] and z^(p^s) is a p-power in N_s for s>=1, w belongs to Phi(N_s). Therefore

delta_{G_s}=0 in (W_s)_D.

This is gauge-robust: the allowed scalar normalization of the transgression cannot change zero to nonzero.

Classification:
- E1 computation delta_{G_s}=0: PASS / CLOSED.
- delta_G as carrier of the K–Z deep-tail parameter s: FAIL / CLOSED.
- bridge deep correction <-> Palaisti delta_G: FAIL / CLOSED.
- filtered/p-adic/higher relation-module successor: OPEN / LOAD-BEARING.
- matched cd=3 control: OPEN, but not authorized yet.

The key boundary is that the K–Z correction survives in the ambient group but is annihilated at the first Frattini quotient. Literature confirms that Zassenhaus-filtered relation modules and initial-form methods are legitimate objects for pro-p presentations, but this does not yet establish finite-window factorization.

Next authorized task: fresh pre-check of the smallest filtered relation object retaining the p-power tail without simply re-encoding the presentation; only if it survives intrinsicity, gauge, finite-window and non-reencoding tests may the cd=3 matched-control search resume.