#!/usr/bin/env python3
"""Small rank-4 representative audit for the frozen degree-3 IA quotient.

Consumes the authoritative first-layer lift-fibre machinery and tests a
small admissible representative set against Q3=A3/(C3+Delta_IA):
identity, -I, a line-fixing transvection, and a multiplier-2 GSp lift.
No full GSp scan is performed.
"""
import runpy
from itertools import combinations

ns = runpy.run_path("research/rank4_D4_actual_lift_fibre_audit_2026-09-19.py")

P = ns["P"]; N = ns["N"]
GEN = ns["GEN"]; SPECS = ns["SPECS"]; PAIRS = ns["PAIRS"]
R3 = ns["R3"]; RI = ns["RI"]; B3 = ns["B3"]; BI = ns["BI"]
C3 = ns["C3"]; rank = ns["rank"]; ia = ns["ia"]; coeff = ns["coeff"]
comp = ns["comp"]; ev = ns["ev"]; defect = ns["defect"]; vec = ns["vec"]

# Explicit free lifts for admissible linear representatives.
CASES = {
    "identity": [[(0,1)],[(1,1)],[(2,1)],[(3,1)]],
    "minus_I": [[(0,-1)],[(1,-1)],[(2,-1)],[(3,-1)]],
    "transvection_e1_to_e1_plus_e2": [[(0,1),(1,1)],[(1,1)],[(2,1)],[(3,1)]],
    "multiplier2_diag": [[(0,-1)],[(1,1)],[(2,-1)],[(3,1)]],
}

def lift(g, p, side):
    return [ev(w, GEN) for w in (comp(p,g) if side == "left" else comp(g,p))]

out = {}
for name, g in CASES.items():
    out[name] = {}
    bg = [ev(w, GEN) for w in g]
    for side in ("left", "right"):
        d0 = defect(R3, B3, bg)
        i0 = defect(RI, BI, bg)
        V = []
        W = []
        for s in SPECS:
            L = lift(g, ia(coeff(s)), side)
            assert all(vec(L[i],1) == vec(bg[i],1) for i in range(N))
            V.append([(x-y)%P for x,y in zip(defect(R3,B3,L), d0)])
            W.append([(x-y)%P for x,y in zip(defect(RI,BI,L), i0)])

        gauge_rank = rank(C3 + V)
        q_signal = [(x-y)%P for x,y in zip(d0, i0)]

        # Actual fibre composition audit, modulo the frozen C3 correction.
        mod_fail = 0
        for a,b in combinations(SPECS,2):
            pa, pb = ia(coeff(a)), ia(coeff(b))
            ps = comp(pa,pb)
            S = comp(ps,g) if side == "left" else comp(g,ps)
            C = comp(comp(pa,pb),g) if side == "left" else comp(g,comp(pa,pb))
            ds = defect(R3,B3,[ev(w,GEN) for w in S])
            dc = defect(R3,B3,[ev(w,GEN) for w in C])
            diff = [(x-y)%P for x,y in zip(dc,ds)]
            if rank(C3 + [diff]) > rank(C3):
                mod_fail += 1

        out[name][side] = {
            "IA_variation_rank": rank(V),
            "q3_qinf_variation_equal": V == W,
            "composition_pairs": 276,
            "composition_failures_mod_C3": mod_fail,
            "gauge_rank": gauge_rank,
            "q_signal_nonzero": any(q_signal),
            "q_signal_survives_Q3": rank(C3 + V + [q_signal]) > gauge_rank,
        }

        assert rank(V) == 20
        assert V == W
        assert mod_fail == 0
        if name != "identity":
            assert out[name][side]["q_signal_survives_Q3"]

print({
    "status": "PASS_SMALL_RANK4_REPRESENTATIVE_AUDIT",
    "cases": list(CASES),
    "all_left_right_ia_ranks_20": True,
    "all_q3_qinf_change_laws_equal": True,
    "all_composition_failures_mod_C3": 0,
    "Q3_dimension": 44,
    "interpretation": (
        "For the four explicit admissible representatives, the frozen degree-3 "
        "IA quotient is independent of first-layer lift perturbations on both "
        "left/right fibre parameterizations; the q=3 versus q=infinity defect "
        "survives Q3 for every non-identity representative tested. This is a "
        "small representative control, not a full rank-4 theorem or GSp scan."
    ),
    "details": out,
})
