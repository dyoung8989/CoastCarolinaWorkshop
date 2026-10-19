# Language, Writing, and AI

Companion materials for a 90-minute Coastal Carolina workshop for English students. No coding experience is required. Use Google Colab in your browser.

## Start here

1. Open [Google Colab](https://colab.research.google.com/), choose **Upload**, and upload [`notebooks/nlp_workshop_notebook.ipynb`](notebooks/nlp_workshop_notebook.ipynb). Download the notebook from GitHub with **Download raw file** first.
2. Sign in to Google and save a copy in Drive if you want to keep your edits.
3. Run the setup cells, then work from top to bottom with **Shift + Enter**.
4. Follow the two student exercises; the instructor leads the prediction demo.

Once these files are on the repository's `main` branch, use [Open in Colab](https://colab.research.google.com/github/dyoung8989/CoastCarolinaWorkshop/blob/main/notebooks/nlp_workshop_notebook.ipynb). If that link cannot access the repository, use the upload route above. A private repository may require additional authorization.

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

Extraction can miss or mislabel information. A readiness score is a discussion prompt, not a measure of writing quality. The prediction data is synthetic: the demo illustrates a method, not evidence about actual support tickets. Human judgment remains essential throughout.

## Maintainer checks

Students only need Colab. Maintainers can validate the notebook with `python scripts/validate_notebook.py`; the GitHub workflow also executes every analysis cell with the workshop dependencies. See [validation notes](docs/validation.md).

Event date, room, slides, and facilitator contact details have not been supplied. See the facilitator checklist before sharing the workshop.

## License

Copyright (c) 2026 David Young. Code is licensed under [MIT](LICENSE-MIT); guides, sample text, and notebook explanations are licensed under [CC BY 4.0](LICENSE-CC-BY-4.0.txt). See [licensing details](LICENSE.md) for notebook scope, attribution, and third-party exclusions.
