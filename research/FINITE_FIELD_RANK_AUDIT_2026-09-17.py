import ast
import subprocess
from pathlib import Path

FORBIDDEN = {'np.linalg.matrix_rank', 'numpy.linalg.matrix_rank',
             'np.linalg.det', 'numpy.linalg.det'}


def dotted_name(node):
    parts = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if isinstance(node, ast.Name):
        parts.append(node.id)
        return '.'.join(reversed(parts))
    return None

tracked = subprocess.check_output(['git', 'ls-files', 'research'], text=True).splitlines()
files = [Path(x) for x in tracked if Path(x).suffix in {'.py', '.pyw'}]
hits = []

for path in files:
    tree = ast.parse(path.read_text(encoding='utf-8', errors='replace'), filename=str(path))
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = dotted_name(node.func)
            if name and name.startswith(('np.linalg.', 'numpy.linalg.')):
                hits.append((str(path), node.lineno, name))

print('FINITE-FIELD RANK AUDIT')
print('tracked research Python files =', len(files))
print('np.linalg call sites =', len(hits))
for path, lineno, name in hits:
    print(f'{path}:{lineno}: {name}(...)')

forbidden = [h for h in hits if h[2] in FORBIDDEN]
if forbidden:
    raise SystemExit('FORBIDDEN REAL-FIELD LINEAR ALGEBRA CALL FOUND')

print('AUDIT STATUS = PASS')
print('No numpy.linalg.matrix_rank or numpy.linalg.det calls found.')
print('Any other np.linalg call is surfaced above for explicit review.')
