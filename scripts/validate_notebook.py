"""Validate structure and execute workshop analysis without notebook setup downloads."""
import argparse
import ast
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--execute", action="store_true")
args = parser.parse_args()
path = ROOT / "notebooks/nlp_workshop_notebook.ipynb"
notebook = json.loads(path.read_text(encoding="utf-8"))
for cell in notebook["cells"]:
    if cell["cell_type"] == "code":
        assert cell["outputs"] == [], "Distribute the notebook with outputs cleared"
        assert cell["execution_count"] is None
        source = "".join(cell["source"])
        if not source.lstrip().startswith("# Install"):
            ast.parse(source)
print("Notebook structure, cleared outputs, and Python syntax passed.")
for document in ROOT.rglob("*.md"):
    for target in re.findall(r"\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
        if "://" not in target:
            assert (document.parent / target.split("#")[0]).exists(), (document, target)
print("Local Markdown file links passed.")

if args.execute:
    import nbformat
    from nbclient import NotebookClient
    nb = nbformat.read(path, as_version=4)
    nbformat.validate(nb)
    # CI already installs the exact workshop dependencies. Skip only Colab setup.
    nb.cells = [c for c in nb.cells if not (
        c.cell_type == "code" and c.source.lstrip().startswith("# Install"))]
    nb.cells.append(nbformat.v4.new_code_cell("""
assert result2['readiness_score'] > result['readiness_score']
assert original_result == score_doc(original)
assert revision_result == score_doc(revision)
assert list(comparison.columns) == ['Original', 'Revision']
assert comparison.shape == (6, 2)
for column, scores in [('Original', original_result), ('Revision', revision_result)]:
    assert comparison.loc['Readiness score (0–100)', column] == scores['readiness_score']
    assert comparison.loc['Flags', column] == ('; '.join(scores['flags']) or 'No flags')
assert original_result['flags'], 'The starter original should demonstrate feedback'
assert revision_result['readiness_score'] > original_result['readiness_score']
assert extract_actions('The mustard is yellow.') == []
assert len(extract_actions('Please save the file.')) == 1
try:
    score_doc('   ')
except ValueError:
    pass
else:
    raise AssertionError('Empty input must have a useful error')
print('Workshop behavior checks passed.')
"""))
    NotebookClient(nb, timeout=300, kernel_name="python3").execute(cwd=str(ROOT))
    destination = ROOT / "artifacts/executed-workshop.ipynb"
    destination.parent.mkdir(exist_ok=True)
    nbformat.write(nb, destination)
    print("Executed all analysis cells and behavior checks:", destination)
