"""O2-6: basepoint-independence of the transport-variation direction.

Within the frozen B1 admissible family
    tau_b = tau o (I + bN), b in F_3,
O2-5 defined Delta D = D_1 - D_0.

This checkpoint asks whether changing the basepoint changes the variation
direction. Over F_3 the cyclic finite differences are:
    D_1-D_0,
    D_2-D_1,
    D_0-D_2.
The test requires them to be exactly equal, not merely to have the same rank.

Scope:
- This is a basepoint-independence test inside the already verified B1
  admissible family.
- It does not by itself establish a filtration-only characterization of
  Delta O, nor q=3 versus q=infinity.
"""
from pathlib import Path
import runpy
import numpy as np

ROOT = Path(__file__).parent
ns = runpy.run_path(str(ROOT / "O2_5_affine_variation_2026-09-18.py"))

P = 3
D0 = np.array(ns["D0"], dtype=np.int64) % P
D1 = np.array(ns["D1"], dtype=np.int64) % P
D2 = np.array(ns["D2"], dtype=np.int64) % P
rank3 = ns["rank3"]

delta01 = (D1 - D0) % P
delta12 = (D2 - D1) % P
delta20 = (D0 - D2) % P

print("O2-6 BASEPOINT-INDEPENDENCE OF TRANSPORT VARIATION")
print("Frozen admissible family = tau_b = tau o (I+bN), b=0,1,2")
print("rank(delta_01) =", rank3(delta01))
print("rank(delta_12) =", rank3(delta12))
print("rank(delta_20) =", rank3(delta20))

same_01_12 = np.array_equal(delta01, delta12)
same_12_20 = np.array_equal(delta12, delta20)
same_20_01 = np.array_equal(delta20, delta01)

print("DELTA_01_EQUALS_DELTA_12 =", same_01_12)
print("DELTA_12_EQUALS_DELTA_20 =", same_12_20)
print("DELTA_20_EQUALS_DELTA_01 =", same_20_01)

# Stronger than equality of images: the actual variation maps coincide.
assert same_01_12
assert same_12_20
assert same_20_01
assert rank3(delta01) == 10
assert rank3(delta12) == 10
assert rank3(delta20) == 10

DeltaO_dim = rank3(delta01)
print("DELTA_O_DIM =", DeltaO_dim)
print("O2-6 RESULT = PASS")
