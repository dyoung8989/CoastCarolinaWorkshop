# NLP & Python for English Majors: Career Workshop

*A 90-minute agenda for introducing English students to NLP/ML-adjacent careers through light Python and hands-on technical writing exercises, structured as a three-tier difficulty progression.*

## Working assumptions (adjust as needed)

- **Audience:** English majors/students with little or no coding background.
- **Setup:** Google Colab (browser-based, no local installs) so class time goes to concepts and practice instead of troubleshooting Python installs.
- **Group size:** Works for roughly 10–30 students; scale small-group segments up or down as needed.
- **Facilitator:** One instructor, optionally with a TA/helper for the hands-on blocks (very useful for catching stuck laptops).

---

## Learning objectives

By the end of the workshop, students should be able to:

1. Explain in plain language what NLP is and name 3–4 ways it shows up in the working world.
2. Point to specific job titles and career paths where an English degree plus light technical/NLP fluency is a real asset.
3. Run and lightly modify Python code in a notebook — without having "learned to code" in the traditional sense.
4. Complete at least one hands-on exercise that mirrors real technical-writing/content work (e.g., scoring a document's readability, or pulling key terms out of a body of text).
5. Leave with concrete next steps: tools to explore, communities to join, and language to use on a resume.

## The progression: three levels of NLP sophistication

Structure the hands-on portion as a difficulty ladder so students see NLP as a spectrum rather than one skill:

**Tier 1 — Extraction.** The computer pulls structured information out of unstructured text: key terms, named entities, action items. This is "here's what a machine can already find for you" — low complexity, immediately legible.

**Tier 2 — Automated evaluation.** Instead of just pulling information out, the tool judges the text: is this document actually ready for a reader — or a downstream machine — to consume? Combine a few signals (readability, passive-voice rate, sentence length, missing structure) into a composite "doc readiness" score that flags specific problem areas. Still rule-based — you decide the thresholds — but now it's a real tool, not a party trick.

**Tier 3 — Prediction (machine learning).** Instead of hand-coding the rules, the system learns them from historical outcomes. Feed it past documents plus a signal of what actually went wrong (support ticket volume, edit frequency, negative feedback), and it learns to predict which *current* documents are likely problem areas before anyone complains. This is the "the computer noticed a pattern we didn't" moment, and the clearest bridge to why a content/documentation team would ever need someone who understands both writing and modeling.

## Career paths worth naming explicitly

Technical writer / content strategist working alongside NLP tooling; content operations and documentation quality roles (readability scoring, terminology consistency, "doc health" audits); UX writer / conversation designer; linguistic data analyst; AI trainer / data annotation / model evaluation roles; localization and terminology management; instructional designer working with AI tools; AI content strategist / prompt engineer. Naming real job titles like these — not just "AI stuff" — is often the single most useful thing in the room for students who don't yet see the bridge between their degree and this field.

---

## 90-Minute Agenda (Tiered: Extraction → Evaluation → Prediction)

Structured around the three-tier progression above so students feel the complexity — and the payoff — increase step by step.

| Time | Duration | Segment | What happens |
|---|---|---|---|
| 0:00–0:08 | 8 min | Welcome & the roadmap | Hook: language skills are a genuine bottleneck in AI systems right now. Preview the career paths (below) and the three-tier arc for the session — extraction, evaluation, prediction — so students know where things are headed. |
| 0:08–0:20 | 12 min | What is NLP? (concepts) | Plain-language tour: tokenization, entities, sentiment, embeddings — use analogies, not math. Frame each concept as "this is what powers Tier 1 / Tier 2 / Tier 3" so the concepts and the hands-on arc reinforce each other. |
| 0:20–0:30 | 10 min | Meet Python & Colab | Everyone opens a pre-built Colab notebook (link shared in advance). Run the first cell together so everyone sees output before anything gets typed. |
| 0:30–0:45 | 15 min | Tier 1 — hands-on: extraction | Students run a few lines of code (e.g., spaCy, or a simple regex pass) to pull key terms, named entities, or action items ("must," "should," "please") out of a sample procedure document. Swap in their own paragraph if time allows. Takeaway: *the machine can already find things for you.* |
| 0:45–1:00 | 15 min | Tier 2 — hands-on: the doc readiness checker | Run a provided `score_doc()` function that combines readability, passive-voice rate, sentence length, and structure checks into one score plus a list of flagged issues. Students run it against a sample doc, edit a flagged sentence, and rerun to watch the score improve. Takeaway: *the machine can judge readiness, not just extract.* |
| 1:00–1:15 | 15 min | Tier 3 — live demo: prediction (synthetic data) | You drive this one — building a model live isn't realistic in 15 minutes with this audience. Walk through, conceptually and with real output: feed historical docs plus an outcome signal (support tickets, edit frequency, negative feedback) into a model, and show it predicting which *current* documents are highest-risk before any complaints come in. Takeaway: *the machine learned the pattern instead of being told the rule.* |
| 1:15–1:27 | 12 min | Career paths & Q&A | Map the three tiers directly onto roles: Tier 1 → content ops/tagging roles, Tier 2 → documentation quality/tooling roles, Tier 3 → data-adjacent content strategy roles. Invite questions. |
| 1:27–1:30 | 3 min | Wrap-up & resources | Hand out the resource list (below) and one clear next step. |

---

## Materials & prep checklist

- One pre-built Colab notebook covering all three tiers, shared as a link in advance (test it fresh the morning of — Colab library versions drift).
- Slides for the concept sections (tokenization, embeddings, etc. — keep visuals simple and metaphor-driven, not equations).
- Printed or linked resource handout (see below).
- A TA or helper for the hands-on blocks, if possible — most delays come from individual notebook hiccups, not the material itself.

**Tier-specific prep:**

- **Tier 1 (extraction):** a short procedure/how-to document with a handful of clear action items and named entities (product names, tools, roles) for students to pull out — anonymized real docs work well; avoid anything under NDA.
- **Tier 2 (evaluation):** the `score_doc()` function pre-written in the notebook (readability + passive-voice rate + sentence length + a structure check, e.g. "has headers," "has a summary line"), plus a sample document with 2–3 deliberately flaggable issues so the demo has something concrete to fix.
- **Tier 3 (prediction):** a small pre-built dataset pairing document features (length, readability, age, topic) with an outcome signal (support tickets, edit frequency) — real or plausibly mocked — and a pre-trained model or a pre-run notebook, so the live demo doesn't depend on training finishing on time.

## Suggested resource handout

Communities and resources worth pointing students to afterward: Write the Docs (community + Slack), the r/technicalwriting community, an intro NLP course (e.g., Hugging Face's free NLP course), and a short reading list connecting writing and NLP (e.g., pieces on "documentation as AI training data" or "content as infrastructure"). Swap in whichever of these you have the strongest personal opinion about — a specific recommendation lands better than a long neutral list.

## Event description (for marketing team)

This 90-minute, hands-on workshop introduces English students to careers where language skills meet AI, such as technical writing and content strategy. No coding experience is required. The session opens with a plain-language introduction to natural language processing (NLP) — what it is and how it already shows up in everyday tools — before moving into a guided environment setup using Google Colab, a free, browser-based platform that lets students run real Python code without installing anything on their own laptops.

From there, students work through two hands-on activities followed by an instructor-led demonstration. First, they use code to extract information directly from a piece of text, such as key terms or action items. Next, they build on that by running a tool that evaluates a document's overall readiness for a reader — combining several measures, such as readability and sentence structure, into a single score with specific areas flagged for improvement. Finally, students see a live demonstration of a machine learning model that goes a step further: rather than following fixed rules, it learns from patterns in past documentation and feedback to predict where problems are likely to appear in current documents, before anyone reports them. The workshop closes with a discussion of specific job titles, professional communities, and concrete next steps for students interested in pursuing this kind of work.
