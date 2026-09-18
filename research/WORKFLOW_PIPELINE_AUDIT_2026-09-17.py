"""Repository-wide CI shell reliability audit.

Detects risky shell pipelines in GitHub Actions workflows, especially
`| gap` and `| python`, and requires an explicit pipefail setting.

Also forbids fragile inline GAP probes where shell quoting/escape layers
feed GAP through printf/echo/command substitution. GAP probes must use a
heredoc or a checked-in .g source file so GAP parses its own source directly.

This is a CI reliability check, not a mathematical computation.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WF_DIR = ROOT / ".github" / "workflows"

# Restrict whitespace after "|" to horizontal whitespace. Otherwise YAML's
# block-scalar "run: |" can accidentally consume the following "python ..."
# line and look like a shell pipeline.
PIPE_RE = re.compile(r"\|[ \t]*(?:gap(?:[ \t]|$)|python(?:\d*)?(?:[ \t]|$)|bash(?:[ \t]|$)|sh(?:[ \t]|$))")
PIPEFAIL_RE = re.compile(r"set\s+-[A-Za-z]*o?\s*pipefail|set\s+-[A-Za-z]*e[A-Za-z]*u[A-Za-z]*o[A-Za-z]*\s+pipefail|pipefail")
CANONICAL_PIPEFAIL_RE = re.compile(r"set\s+-euo\s+pipefail|set\s+-o\s+pipefail")

INLINE_GAP_RE = re.compile(
    r"(?:printf|echo)\s+[^\n]*\|\s*gap(?:\s+-q)?|"
    r"(?:printf|echo)\s+[^\n]*gap\s+-q|"
    r"\$\([^\n]*gap\s+-q"
)
GAP_REF_RE = re.compile(r"\bGModuleByMats\s*\(")
HEREDOC_RE = re.compile(r'''<<[-']?[A-Za-z_][A-Za-z0-9_]*['"]?''')

workflows = sorted(WF_DIR.glob("*.yml")) + sorted(WF_DIR.glob("*.yaml"))
findings = []
inline_gap_findings = []

for path in workflows:
    text = path.read_text(encoding="utf-8")
    matches = list(PIPE_RE.finditer(text))
    if matches:
        has_pipefail = bool(CANONICAL_PIPEFAIL_RE.search(text) or PIPEFAIL_RE.search(text))
        for m in matches:
            line = text.count("\n", 0, m.start()) + 1
            snippet = text.splitlines()[line - 1].strip()
            findings.append((path.relative_to(ROOT).as_posix(), line, snippet, has_pipefail))

    if GAP_REF_RE.search(text) and not HEREDOC_RE.search(text):
        for i, line_text in enumerate(text.splitlines(), 1):
            if re.search(r"(?:printf|echo).*gap\s+-q|gap\s+-q.*(?:printf|echo)|\$\(.*gap\s+-q", line_text):
                inline_gap_findings.append((path.relative_to(ROOT).as_posix(), i, line_text.strip()))

print(f"WORKFLOW_COUNT = {len(workflows)}")
print(f"RISKY_PIPELINE_OCCURRENCES = {len(findings)}")
for path, line, snippet, has_pipefail in findings:
    status = "PROTECTED" if has_pipefail else "FAIL_OPEN_RISK"
    print(f"{status}: {path}:{line}: {snippet}")

print(f"INLINE_GAP_PROBE_OCCURRENCES = {len(inline_gap_findings)}")
for path, line, snippet in inline_gap_findings:
    print(f"INLINE_GAP_PROBE_FORBIDDEN: {path}:{line}: {snippet}")

unprotected = [x for x in findings if not x[3]]
if unprotected or inline_gap_findings:
    print("RESULT = FAIL")
    if unprotected:
        print("Every risky shell pipeline must be protected by pipefail.")
    if inline_gap_findings:
        print("GAP probes must use heredoc or a checked-in .g file; inline shell strings are forbidden.")
    sys.exit(1)

print("RESULT = PASS")
