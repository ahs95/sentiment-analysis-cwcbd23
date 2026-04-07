import nbformat
from pathlib import Path

def fix_notebook(path):
    nb = nbformat.read(path, as_version=nbformat.NO_CONVERT)
    changed = False
    for cell in nb.get('cells', []):
        mw = cell.get('metadata', {}).get('widgets')
        if isinstance(mw, dict):
            if 'state' not in mw:
                mw['state'] = {}
                changed = True
        elif mw is not None:
            # if it's not a dict, remove it
            cell['metadata'].pop('widgets', None)
            changed = True
    if changed:
        nbformat.write(nb, path)
        print("Fixed:", path)

for p in Path('.').rglob('*.ipynb'):
    try:
        fix_notebook(p)
    except Exception as e:
        print("Error processing", p, e)
