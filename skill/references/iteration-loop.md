# Iteration Loop

Use this process when a generation fails or the user wants the skill to improve.

1. Record case facts: template ID, input roles, user goal, prompt used, output issue.
2. Score with `scripts/score_case.py` or the rubric.
3. Draft candidate revision notes.
4. Decide update level:
   - One-off issue: add to case notes only.
   - Repeated issue in one template: update that card's `failure_modes` or `prompt_template`.
   - Repeated issue across templates: update `universal-rules.md`.
5. If the issue suggests a reusable new diagram type rather than a revision to an existing card, follow `case-capture-workflow.md` and create a candidate template first.
6. Do not modify stable templates until the user explicitly approves the merge.
7. Preserve older wording when uncertain by appending a dated note under `revision_policy`.

Default case log location for this project:

`docs/ai-analysis-diagram-factory/cases/`

Default candidate template location:

`references/candidate-templates/`
