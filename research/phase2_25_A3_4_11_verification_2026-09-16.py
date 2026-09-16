"""A3-4-11 / Phase 2-25 Actions entrypoint."""
from pathlib import Path
import runpy

TARGET = Path(__file__).with_name(
    "phase2_25_A3_4_11_L5_relation_span_2026-09-16.py"
)

print("PHASE 2-25 / A3-4-11 PURE L5 RELATION-SPAN VERIFICATION")
print("TARGET =", TARGET.name)
print("NO (R)_5 DIMENSION IS ASSUMED IN ADVANCE")

runpy.run_path(str(TARGET), run_name="__main__")
