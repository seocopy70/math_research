from pathlib import Path
import re
import subprocess

ROOT = Path('research')
PATTERNS = {
    'np.linalg.matrix_rank': re.compile(r'\b(?:np|numpy)\.linalg\.matrix_rank\b'),
    'np.linalg.det': re.compile(r'\b(?:np|numpy)\.linalg\.det\b'),
    'np.linalg family': re.compile(r'\b(?:np|numpy)\.linalg\.[A-Za-z_][A-Za-z0-9_]*\b'),
}

tracked = subprocess.check_output(['git', 'ls-files', 'research'], text=True).splitlines()
hits = []
for rel in tracked:
    path = Path(rel)
    if path.suffix not in {'.py', '.pyw'}:
        continue
    text = path.read_text(encoding='utf-8', errors='replace')
    for lineno, line in enumerate(text.splitlines(), 1):
        for label, pattern in PATTERNS.items():
            if pattern.search(line):
                hits.append((rel, lineno, label, line.strip()))

print('FINITE-FIELD RANK AUDIT')
print('tracked research Python files =', sum(Path(x).suffix in {'.py', '.pyw'} for x in tracked))
print('np.linalg occurrences =', len(hits))
for rel, lineno, label, line in hits:
    print(f'{rel}:{lineno}: [{label}] {line}')

# matrix_rank and det are categorically forbidden for the finite-field track.
forbidden = [h for h in hits if h[2] in {'np.linalg.matrix_rank', 'np.linalg.det'}]
if forbidden:
    raise SystemExit('FORBIDDEN REAL-FIELD LINEAR ALGEBRA FOUND')

print('AUDIT STATUS = PASS')
print('No np.linalg.matrix_rank or np.linalg.det calls found in tracked research Python files.')
print('Any future np.linalg use is surfaced above for explicit review.')
