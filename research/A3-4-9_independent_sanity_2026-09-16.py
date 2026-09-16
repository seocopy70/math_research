"""
Independent sanity check for A3-4-9.

The primary certificate uses a column-oriented Gaussian elimination routine.
This script deliberately uses a separate row-oriented sparse elimination
algorithm over F_3 and checks the already-constructed W45, S and [L2,R]
matrices independently.

The goal is not to replace the primary certificate, but to ensure that the
critical ranks and inclusion result are not artifacts of one implementation
of modular rank.
"""

import runpy

MOD = 3
BASE = runpy.run_path(
    "research/phase2_22_A3_4_9_W45_true_relation_intersection_2026-09-16.py"
)

W = BASE["W"]
Sm = BASE["Sm"]
oldm = BASE["oldm"]


def row_rank_mod3(A):
    """Independent row-oriented rank over F_3 using sparse pivot rows."""
    rows = []
    for raw in A:
        row = {i: int(v) % MOD for i, v in enumerate(raw) if int(v) % MOD}
        rows.append(row)

    pivots = {}
    rank = 0

    for row in rows:
        while row:
            p = min(row)
            coeff = row[p] % MOD
            if p not in pivots:
                inv = 1 if coeff == 1 else 2
                if inv == 2:
                    row = {j: (v * 2) % MOD for j, v in row.items()}
                pivots[p] = row
                rank += 1
                break

            pivot = pivots[p]
            factor = coeff
            # row <- row - factor * pivot
            for j, v in pivot.items():
                nv = (row.get(j, 0) - factor * v) % MOD
                if nv:
                    row[j] = nv
                else:
                    row.pop(j, None)

    return rank


def combined(*mats):
    return __import__("numpy").concatenate(mats, axis=1)

# Convert the column-basis matrices into row matrices for the independent
# elimination routine.
import numpy as np

rank_W = row_rank_mod3(W.T)
rank_S = row_rank_mod3(Sm.T)
rank_old = row_rank_mod3(oldm.T)
rank_WS = row_rank_mod3(combined(W, Sm).T)
rank_S_old = row_rank_mod3(combined(Sm, oldm).T)

intersection = rank_W + rank_S - rank_WS
inclusion = rank_S_old == rank_S

print("A3-4-9 INDEPENDENT SANITY CHECK")
print("================================")
print(f"independent rank(W45) = {rank_W}")
print(f"independent rank(S) = {rank_S}")
print(f"independent rank([W45 | S]) = {rank_WS}")
print(f"independent dim(W45 intersection S) = {intersection}")
print(f"independent rank([S | [L2,R]]) = {rank_S_old}")
print(f"independent [L2,R] subset S = {inclusion}")

assert rank_W == 45
assert rank_S == 15
assert rank_old == 5
assert rank_WS == 60
assert intersection == 0
assert rank_S_old == 15
assert inclusion

print("INDEPENDENT SANITY CHECK PASSED")
