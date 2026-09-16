"""Repository-wide CI shell-pipeline audit.

Detects risky shell pipelines in GitHub Actions workflows, especially
`| gap` and `| python`, and requires an explicit pipefail setting in any
workflow containing such a pipeline.

This is a CI reliability check, not a mathematical computation.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WF_DIR = ROOT / ".github" / "workflows"

PIPE_RE = re.compile(r"\|\s*(?:gap(?:\s|$)|python(?:\d*)?(?:\s|$)|bash(?:\s|$)|sh(?:\s|$))")
PIPEFAIL_RE = re.compile(r"set\s+-[A-Za-z]*o?\s*pipefail|set\s+-[A-Za-z]*e[A-Za-z]*u[A-Za-z]*o[A-Za-z]*\s+pipefail|pipefail")

# The second expression intentionally also accepts the canonical
# `set -euo pipefail` spelling directly.
CANONICAL_PIPEFAIL_RE = re.compile(r"set\s+-euo\s+pipefail|set\s+-o\s+pipefail")

workflows = sorted(WF_DIR.glob("*.yml")) + sorted(WF_DIR.glob("*.yaml"))
findings = []

for path in workflows:
    text = path.read_text(encoding="utf-8")
    matches = list(PIPE_RE.finditer(text))
    if not matches:
        continue
    has_pipefail = bool(CANONICAL_PIPEFAIL_RE.search(text) or PIPEFAIL_RE.search(text))
    for m in matches:
        line = text.count("\n", 0, m.start()) + 1
        snippet = text.splitlines()[line - 1].strip()
        findings.append((path.relative_to(ROOT).as_posix(), line, snippet, has_pipefail))

print(f"WORKFLOW_COUNT = {len(workflows)}")
print(f"RISKY_PIPELINE_OCCURRENCES = {len(findings)}")

for path, line, snippet, has_pipefail in findings:
    status = "PROTECTED" if has_pipefail else "FAIL_OPEN_RISK"
    print(f"{status}: {path}:{line}: {snippet}")

unprotected = [x for x in findings if not x[3]]
if unprotected:
    print("RESULT = FAIL")
    print("Every risky shell pipeline must be protected by pipefail.")
    sys.exit(1)

print("RESULT = PASS")
