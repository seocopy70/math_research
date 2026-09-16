"""A3-4-11 verification entrypoint.

This wrapper deliberately runs the corrected phase2_24 implementation from
this same checkout.  Keeping a distinct entrypoint makes the Actions run
unambiguous: the verification must execute the corrected L5^4 embedding,
not the pre-fix version that produced the 816-vs-204 dimension error.
"""

from pathlib import Path
import runpy

TARGET = Path(__file__).with_name(
    "phase2_24_A3_4_11_L5_obstruction_compression_2026-09-16.py"
)

print("PHASE 2-25 / A3-4-11 CORRECTED VERIFICATION ENTRYPOINT")
print("TARGET =", TARGET.name)
print("EXPECTED L5^4 RELATION EMBEDDING = 816 x 20")

runpy.run_path(str(TARGET), run_name="__main__")
