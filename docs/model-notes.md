# How the demos work

## Extraction

spaCy's small English pipeline supplies sentence boundaries, dependency parses, and entity labels. Those are learned components with imperfect outputs. The action detector separately matches complete keywords or phrases; it does not understand whether an instruction is relevant or safe.

## Readiness

The score starts at 100 and subtracts: `max(0, 60 - readability)`, half the passive-sentence percentage, twice the excess average sentence length over 20 words, and 15 points when no Markdown heading or numbered step is detected. The result is rounded and clipped to 0–100. The flag thresholds differ slightly from the scoring thresholds; they are teaching choices, not externally validated standards.

The Flesch estimate uses a simple vowel-group syllable counter. It is approximate and English-specific. Sentence segmentation and passive detection also make mistakes. The structure detector checks formatting, not information architecture. Empty or punctuation-only input raises a clear error. None of these signals checks correctness, completeness, accessibility, audience fit, or whether a reader can finish a task.

## Prediction (separate instructor example)

Tier 3 has been removed from the student notebook. The notes below describe the previous synthetic demonstration as background; they do not document code or validation in the current student notebook. Prepare and validate the local instructor example separately.

A fixed random seed creates 80 synthetic examples. An invented formula associates readability, passive voice, age, and structure with a binary support-ticket label, with added noise. Sentence length is included as a feature but has no direct effect in that generating formula. Labels are split at the synthetic signal's median; this artificial class balance does not represent a real ticket rate.

A stratified 75/25 split reserves 20 examples for testing. A pipeline fits a standard scaler and logistic regression using only the training examples. Test accuracy, ROC AUC, and a majority-class baseline illustrate evaluation; the small sample makes results unstable. Standardized coefficients describe fitted associations, not causes or guaranteed importance.

Current-document features are invented examples, not measurements extracted from actual current documents. Their predicted probabilities belong to this synthetic setting. They are not calibrated operational risk estimates. In real use, define an observation window, normalize for readership/exposure, check label quality and subgroup performance, use time-aware evaluation where appropriate, and assess calibration before deciding what action to take.
