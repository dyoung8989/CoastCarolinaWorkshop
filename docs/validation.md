# Validation

## Python 3.13 compatibility update

The notebook analysis cells and behavior checks passed in isolated Python 3.13.5 and Python 3.12.14 environments with the updated pins. CI now covers both Python 3.12 and 3.13. NumPy 2.2.6 and Click 8.4.2 replace older pins that conflicted with packages preinstalled in a reported Colab Python 3.13.16 session. spaCy and its setup dependencies were updated together to a compatible set. Setup output is no longer quiet.

These isolated checks do not reproduce Colab's entire preinstalled environment. Rehearse the updated setup in a fresh Colab session before the workshop. If a Drive copy contains the old installation cell, reopen the notebook from GitHub and save a new copy, or replace its setup cell with the current one. After an earlier setup has downgraded packages, use **Runtime → Disconnect and delete runtime** to get a fresh runtime, then reconnect and run the updated notebook from the top. Preserve any edits before replacing a copy.

## Package check — October 19, 2026

All analysis cells executed successfully in a Python 3.12 Jupyter kernel with the pinned workshop packages. Notebook structure, cleared student outputs, local document links, and behavior checks passed. The sample rewrite increased readiness from 0 to 73. On 20 held-out synthetic examples, accuracy was 75% versus a 50% majority baseline, and ROC AUC was 0.85. These are synthetic demo results, not real-world performance claims.

The Colab installation cell was skipped during kernel execution; dependencies and the language model were installed separately. A fresh Colab rehearsal is still required. The original weasel, typer, and click pins addressed a dependency problem in that environment; they have since been superseded by the Python 3.13 compatibility update above.

Run `python scripts/validate_notebook.py` for JSON structure, Python syntax, and cleared-output checks. Maintainer execution first upgrades the installer with `python -m pip install --upgrade "pip>=26.2"`, then uses `python -m pip install -r requirements-validation.txt` followed by `python scripts/validate_notebook.py --execute`. Students should use Colab instead.

Execution skips the Colab installation cell because dependencies are installed first. It runs every analysis cell in sequence and checks rewrite score improvement, disjoint training/test examples, probability ranges, action-keyword boundaries, and empty-text handling. An executed copy is written under `artifacts/` and excluded from version control. GitHub Actions saves it as a run artifact.

Automated execution does not replace a fresh Colab rehearsal, a check of repository visibility and the default branch, or a review of the learning activities with the actual audience.
