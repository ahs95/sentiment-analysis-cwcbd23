import warnings
import nbformat
from pathlib import Path
import uuid
from nbformat.validator import MissingIDFieldWarning

# suppress the specific warning coming from nbformat.validate(nb)
warnings.filterwarnings("ignore", category=MissingIDFieldWarning)

def ensure_cell_id(cell):
    if not isinstance(cell.get("id"), str) or not cell["id"]:
        cell["id"] = uuid.uuid4().hex
        return True
    return False

def fix_notebook(path):
    nb = nbformat.read(path, as_version=nbformat.NO_CONVERT)
    changed = False
    for cell in nb.get("cells", []):
        if ensure_cell_id(cell):
            changed = True
        mw = cell.get("metadata", {}).get("widgets")
        if isinstance(mw, dict):
            if "state" not in mw:
                mw["state"] = {}
                changed = True
        elif mw is not None:
            cell["metadata"].pop("widgets", None)
            changed = True
    if changed:
        nbformat.write(nb, path)
        print("Fixed:", path)

for p in Path(".").rglob("*.ipynb"):
    try:
        fix_notebook(p)
    except Exception as e:
        print("Error processing", p, e)
