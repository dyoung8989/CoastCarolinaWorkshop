# Language, Writing, and AI

Companion materials for a 90-minute Coastal Carolina workshop for English students. No coding experience is required. Use Google Colab in your browser.

## Start here

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dyoung8989/CoastCarolinaWorkshop/blob/main/notebooks/nlp_workshop_notebook.ipynb)

1. Click **Open in Colab** above. No notebook upload or local Python installation is needed.
2. Sign in to Google and choose **File → Save a copy in Drive** to keep your own edits.
3. In your copy, run the setup cells, then work from top to bottom with **Shift + Enter**. Wait for setup to finish; if Colab requests a restart, restart the session and run from the top.
4. Follow the two student exercises. The instructor runs a separate prediction example locally; students do not run Tier 3 in this notebook.

### If the link does not open

A private GitHub repository may require additional authorization. If Colab cannot open it, download [`notebooks/nlp_workshop_notebook.ipynb`](notebooks/nlp_workshop_notebook.ipynb) from GitHub using **Download raw file**. Open [Google Colab](https://colab.research.google.com/), choose **Upload**, and select the downloaded notebook. Ask the facilitator for a copy if you cannot access GitHub.

## What you'll do

| Part | Activity | Time |
|---|---|---|
| Welcome and concepts | Connect language skills to NLP and content work | 20 min |
| Colab setup | Run your first Python cells | 10 min |
| Extraction | Find entities and likely action items | 15 min |
| Automated evaluation | Revise text and inspect a readiness score | 15 min |
| Prediction | Watch a model learn from simulated document outcomes | 15 min |
| Careers and questions | Discuss roles and choose a next step | 15 min |

## Materials

- [Student guide](docs/student-guide.md): exercises, troubleshooting, and reflection prompts.
- [Workshop agenda](docs/agenda.md): full 90-minute schedule and event description.
- [Facilitator guide](docs/facilitator-guide.md): preparation, teaching notes, and fallback plan.
- [Resources and glossary](docs/resources.md): links and terms used in the workshop.
- [Model and scoring notes](docs/model-notes.md): assumptions and limits behind the demos.
- [Sample documents](data/README.md): synthetic examples for editing practice.

## Reading the results

Extraction can miss or mislabel information. A readiness score is a discussion prompt, not a measure of writing quality. The instructor’s separate prediction example illustrates a method; its outcomes should not be treated as evidence about actual support tickets. Human judgment remains essential throughout.

## Maintainer checks

Students only need Colab. Maintainers can validate the notebook with `python scripts/validate_notebook.py`; the GitHub workflow also executes every student analysis cell, including the original/revision comparison table, with the workshop dependencies. See [validation notes](docs/validation.md).

Event date, room, slides, and facilitator contact details have not been supplied. See the facilitator checklist before sharing the workshop.

## License

Copyright (c) 2026 David Young. Code is licensed under [MIT](LICENSE-MIT); guides, sample text, and notebook explanations are licensed under [CC BY 4.0](LICENSE-CC-BY-4.0.txt). See [licensing details](LICENSE.md) for notebook scope, attribution, and third-party exclusions.
