# Facilitator guide

This is one 90-minute session for English students with no assumed coding background. Colab is the student environment. The first two tiers are hands-on in the student notebook. Tier 3 is a separate instructor-led example run locally on your own machine; its code is not distributed in the student notebook.

## Before the event

- Confirm the date, room, audience size, Wi-Fi, projection, and Google/Colab access.
- Put this [direct Colab link](https://colab.research.google.com/github/dyoung8989/CoastCarolinaWorkshop/blob/main/notebooks/nlp_workshop_notebook.ipynb) in the workshop invitation and opening slide. Students should save their own Drive copy before editing.
- For access without GitHub authorization, make the repository public. Test the Colab link while signed out of GitHub, then rehearse setup and all cells in a fresh Colab session. Keep a downloadable notebook copy as a fallback.
- Run the notebook in a fresh Colab session the morning of the event. Setup downloads libraries and a language model; allow several minutes on a slow connection.
- Save a separate executed copy of the student notebook and a readable PDF/printout of its outputs for a network outage. Prepare and test your local prediction example separately. Keep the distributed student notebook's outputs clear.
- Arrange a helper if possible. Prepare concept slides separately; no deck is included here.
- Use the synthetic examples, or substitute material you have permission to share. Preview every replacement.

## Teaching cues

Follow the [agenda](agenda.md). At 30 minutes, start extraction; at 45, move to evaluation; at 60, take over for prediction. Preserve the final 15 minutes for careers, questions, and next steps.

**Concepts:** a token is a small unit of text; an entity is a labeled mention; an embedding represents text numerically. Sentiment estimates expressed tone and can misread context. Use these as explanations, not additional coding exercises.

**Extraction:** ask students to challenge a label. The spaCy parser and entity recognizer already use trained models. Only the action-keyword heuristic is rule-based. The tiers describe tasks, not a clean divide between rules and machine learning.

**Evaluation:** students type complete text blocks into `original` and `revision`, then run the cell to display both scores and full flags in a comparison table. Edit one issue at a time. Ask whether a lower reading level fits the intended reader. Point out that the sample rewrite omits detail; a higher score does not establish semantic fidelity or task success.

**Prediction:** explain features, outcome labels, training data, and held-out data before fitting. The model uses standardized features so coefficient magnitudes share a scale, but correlated inputs still complicate interpretation. Show test results as a small synthetic example. Do not frame the probabilities as measured business risk or causal evidence.

**Careers:** connect extraction to tagging/content operations, evaluation to documentation quality/tooling, and prediction to collaboration between content specialists and data teams. These are examples of work, not a required career ladder or promises of job availability.

## If time or connectivity is limited

Pair students and run the sample without custom text. Have them propose a revision aloud. Use your separately prepared local example or saved outputs for Tier 3. If the whole room loses connectivity, compare the sample paragraphs on screen and ask students to identify features and possible missing outcomes manually.

## Discussion and wrap-up

Ask: Who defines readiness? Whose language is the parser best at? What other factors drive support volume (traffic, product complexity, audience)? What would you validate before acting on a risk ranking? Close by asking each student to choose one follow-up exercise from the student guide.
