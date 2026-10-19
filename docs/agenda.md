# NLP and Python for English Majors: Career Workshop

A 90-minute workshop on language, writing, and AI. Students complete two exercises in Colab. The instructor drives a separate prediction demo on their own machine.

## Audience and setup

- **Audience:** English students with little or no coding experience.
- **Student setup:** A laptop, browser, Google account, and the student Colab notebook.
- **Group size:** About 10 to 30 students. Adjust group activities as needed.
- **Instructor setup:** A tested local prediction example and slides for the concepts. A helper can assist with Colab setup.

## Learning objectives

By the end of the workshop, students should be able to:

1. Explain what NLP is and name a few ways people use it.
2. Connect writing skills to roles in documentation, content, and AI.
3. Run and make small changes to notebook code.
4. Extract information from a paragraph and compare an original text with a revision.
5. Explain what these tools miss and where human judgment is needed.
6. Choose a resource or exercise to try next.

## The three tiers

**Tier 1: Extraction.** Students use spaCy to identify entities and a keyword rule to find likely action items. They review the results and look for mistakes.

**Tier 2: Automated evaluation.** Students use a readiness score to review readability, passive voice, sentence length, and structure. They enter text in `original` and `revision`, then compare scores and flags in a table. The score is a teaching tool. It does not check whether the writing is correct or complete.

**Tier 3: Prediction.** Instructor drives. The instructor runs a separate example locally to show how a model learns from examples and makes predictions. Students watch and discuss the results. They do not install or run prediction code in Colab.

## Career paths

Connect the activities to work such as technical writing, content operations, documentation quality, UX writing, conversation design, localization, data annotation, and AI evaluation. Explain the work involved in each role. These are examples to explore, not promises about job availability.

## 90-minute agenda

| Time | Duration | Segment | What happens |
|---|---|---|---|
| 0:00 to 0:08 | 8 min | Welcome | Introduce the workshop, career examples, and the three tiers. Explain that students will run two exercises and watch the instructor's prediction demo. |
| 0:08 to 0:20 | 12 min | What is NLP? | Explain tokens, entities, sentiment, and embeddings with short examples. Connect them to the activities. |
| 0:20 to 0:30 | 10 min | Python and Colab | Open the shared notebook, save a Drive copy, and run setup together. Wait for setup to finish before continuing. |
| 0:30 to 0:45 | 15 min | Tier 1: Extraction | Students run the sample, review entity labels and likely action items, and try their own paragraph. Discuss missed items and incorrect matches. |
| 0:45 to 1:00 | 15 min | Tier 2: Evaluation | Students run `score_doc()`, enter text in `original` and `revision`, and compare both versions in the output table. Discuss the flags and whether the revision preserves the meaning. |
| 1:00 to 1:15 | 15 min | Tier 3: Prediction | Instructor drives. Run the separate example locally and explain the inputs, training examples, and results. Students discuss what the model can and cannot tell us. No student code to run. |
| 1:15 to 1:27 | 12 min | Careers and questions | Connect the activities to specific roles and answer questions. |
| 1:27 to 1:30 | 3 min | Wrap-up | Share the resources and ask each student to choose one next step. |

## Resources

Share the [resources and glossary](resources.md). Suggestions include Write the Docs, spaCy's introduction, and the Hugging Face course. Recommend one starting point based on the student's interests.

## Event description

This 90-minute workshop introduces English students to ways language and writing skills connect to AI, technical writing, and content work. No coding experience is required. Students use Google Colab in a browser, so there is no local Python installation.

After an introduction to NLP, students complete two activities. First, they use code to find entities and likely action items in a paragraph. Then they compare an original text with a revision using a readiness score and specific feedback. The instructor drives a separate prediction demo on their own machine. The workshop closes with career examples, questions, and resources for further practice.
