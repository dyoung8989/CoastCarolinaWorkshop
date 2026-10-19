# Student guide

Bring a laptop, a browser, and a Google account. Open the notebook using the [README instructions](../README.md#start-here). You do not need to install Python or use GitHub yourself.

## Colab basics

A notebook mixes explanations with code cells. Select a code cell and press **Shift + Enter** to run it. A running cell shows activity beside it. Wait for setup to finish before running the next cell. Variables keep information in memory; later cells use information created earlier.

Read the comments beginning with `#`. You can change quoted sample text without understanding every line of code. Keep the opening and closing triple quotes around paragraphs.

## Exercise 1: extract information (15 minutes)

1. Run the sample procedure and extraction cells.
2. Pick one entity label you agree with and one you question. Entity recognition uses a trained language model; keyword matching uses rules.
3. Replace `your_text` with a short, non-sensitive paragraph. Run that cell to see its entities and likely actions.
4. Add an instruction that avoids all the action keywords. Does the tool miss it? Add a sentence mentioning a keyword without instructing anyone. Does it incorrectly flag it?

Discuss: what would a writer need to check before using these labels in a real documentation system?

## Exercise 2: revise and evaluate (15 minutes)

1. Run the readiness function and messy-document example.
2. Choose one flag and change only the relevant sentence or structure.
3. Run the revision cell and compare both the score and the meaning.
4. Read the provided rewrite critically. What information did it omit? Could it earn a higher score while being less complete?

The goal is a more useful document, not a perfect number. Passive voice can be appropriate; technical terms may be necessary.

## Prediction demo (15 minutes)

Watch the instructor generate synthetic historical documents, separate training and test examples, fit a model, and rank three simulated current documents. Ask which outcomes are missing and whether the test examples resemble the documents people actually use.

## If something breaks

| Symptom | Try this |
|---|---|
| `NameError` | Run earlier cells in order; a variable or function has not been created. |
| Missing spaCy model or import error | Rerun setup. If Colab requests a restart, restart the session and run from the top. |
| Syntax error after editing text | Check the triple quotes around your paragraph. |
| Session disconnected | Reconnect and rerun cells from the top; memory disappears when a session ends. |
| Setup download fails | Pair with a classmate or follow the instructor's saved demo. |
| Colab link cannot access GitHub | Download the notebook and upload it directly to Colab. |

Use only writing you can share. Avoid private coursework, personal information, or confidential workplace documents.

## Leave with one next step

Choose a public paragraph, apply one exercise, and write three sentences: what the tool found, what it missed, and what your judgment added. Describe it as an exploratory workshop exercise using synthetic data, not a production system or a validated business result.
