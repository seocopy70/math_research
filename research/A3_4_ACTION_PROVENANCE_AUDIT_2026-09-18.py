import runpy
import numpy as np

P = 3
HIST = "research/phase2_1_invariant_space_verification_2026-09-15.py"
CURR = "research/A3_4_N_RECON_DIAGNOSTIC_2026-09-17.py"

print("=== A3-4 ACTION PROVENANCE AUDIT ===")
print("Historical:", HIST)
print("Current:", CURR)

h = runpy.run_path(HIST)
c = runpy.run_path(CURR)

# Compare the actual selected W basis in ambient degree-4 coordinates.
Hb = np.column_stack([h["vec4"](a) for a in h["basis"]]) % P
Cb = c["W"] % P
print("W_basis shapes:", Hb.shape, Cb.shape)
print("W_basis exact equal =", np.array_equal(Hb, Cb))
print("rank([H_W | C_W]) =", h["rank3"](np.column_stack([Hb, Cb])))

# Compare all five generator action matrices.
HA = [np.array(A, dtype=int) % P for A in h["action_matrices"]]
CA = [np.array(A, dtype=int) % P for A in c["AW"]]
for i, (a, b) in enumerate(zip(HA, CA), start=1):
    D = (a - b) % P
    print(f"A{i}: exact_equal={np.array_equal(a,b)} diff_rank={h['rank3'](D)}")

HB = sum(HA[1:]) % P
CB = sum(CA[1:]) % P
print("B exact equal =", np.array_equal(HB, CB))
print("rank(B_hist) =", h["rank3"](HB))
print("rank(B_curr) =", c["rank3"](CB))

# Cyclic/Krylov rank is the key conjugacy-invariant diagnostic.
def krylov_rank(A):
    powers = []
    cur = np.eye(A.shape[0], dtype=int)
    for _ in range(A.shape[0]):
        powers.append(cur.copy())
        cur = (cur @ A) % P
    K = np.column_stack([x.reshape(-1) for x in powers]) % P
    return h["rank3"](K)

print("Krylov rank hist =", krylov_rank(HB))
print("Krylov rank curr =", krylov_rank(CB))

print("=== END AUDIT ===")
