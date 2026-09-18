""""O2-9 small follow-up: compare the B1-admissible V20 images.

Only (a,b)=(1,0),(1,1),(1,2) are B1-admissible.
The existing full O2-9 computation is reused unchanged except that its
aggregate all_rank10 assertions are neutralized, because a=2 transports
are known to have rank 45 and are outside B1.

Question:
    Im D_(1,0) == Im D_(1,1) == Im D_(1,2) ?

PASS means only transport-independence within the verified B1 family.
It does NOT mean filtration-intrinsicity.
"""

from pathlib import Path
import runpy
import tempfile
import numpy as np

ROOT = Path(__file__).parent
src = (ROOT / "O2_9_full_transport_invariance_2026-09-18.py").read_text()
src = src.replace(
    "assert all_rank10",
    'if not all_rank10: print("O2-9 full-family rank diagnostic: a=2 transports are rank 45; continuing for B1-only comparison.")'
)

with tempfile.TemporaryDirectory() as td:
    p = Path(td) / "o2_9_full_transport_diagnostic.py"
    p.write_text(src)
    ns = runpy.run_path(str(p))

images = ns["images"]
rank3 = ns["rank3"]
column_basis = ns["column_basis"]
keys = [(1,0), (1,1), (1,2)]
ranks = {k: int(rank3(images[k])) for k in keys}
pairwise = {}
for i, k1 in enumerate(keys):
    for k2 in keys[i+1:]:
        joined = column_basis(np.column_stack([images[k1], images[k2]]))
        pairwise[f"{k1}={k2}"] = {
            "join_rank": int(rank3(joined)),
            "equal": int(rank3(joined)) == ranks[k1] == ranks[k2],
        }

same = all(v["equal"] for v in pairwise.values()) and all(r == 10 for r in ranks.values())
print("O2-9 B1 V20 TRANSPORT-INDEPENDENCE CHECK")
print("B1 transports =", keys)
print("individual ranks =", ranks)
print("pairwise equality =", pairwise)
print("V20 transport-independent within B1 =", same)
print("INTERPRETATION =", "PASS" if same else "FAIL")
print("SCOPE = B1 transport family only; NOT filtration-intrinsicity")
assert all(r == 10 for r in ranks.values())
assert all(v["equal"] for v in pairwise.values())

# diagnostic revision: explicit three-way span check
all_three = column_basis(np.column_stack([images[k] for k in keys]))
print("three-way span rank =", int(rank3(all_three)))
"