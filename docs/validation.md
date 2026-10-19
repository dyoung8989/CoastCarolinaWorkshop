# Validation

## Package check — October 19, 2026

All analysis cells executed successfully in a Python 3.12 Jupyter kernel with the pinned workshop packages. Notebook structure, cleared student outputs, local document links, and behavior checks passed. The sample rewrite increased readiness from 0 to 73. On 20 held-out synthetic examples, accuracy was 75% versus a 50% majority baseline, and ROC AUC was 0.85. These are synthetic demo results, not real-world performance claims.

The Colab installation cell was skipped during kernel execution; dependencies and the language model were installed separately. A fresh Colab rehearsal is still required. Explicit weasel, typer, and click pins address a dependency problem found during this check.

Run `python scripts/validate_notebook.py` for JSON structure, Python syntax, and cleared-output checks. Maintainer execution uses `python -m pip install -r requirements-validation.txt` followed by `python scripts/validate_notebook.py --execute`. Students should use Colab instead.

Execution skips the Colab installation cell because dependencies are installed first. It runs every analysis cell in sequence and checks rewrite score improvement, disjoint training/test examples, probability ranges, action-keyword boundaries, and empty-text handling. An executed copy is written under `artifacts/` and excluded from version control. GitHub Actions saves it as a run artifact.

Automated execution does not replace a fresh Colab rehearsal, a check of repository visibility and the default branch, or a review of the learning activities with the actual audience.
