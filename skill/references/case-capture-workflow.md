# Case Capture Workflow

Use this workflow when a task creates a reusable new diagram type, prompt pattern, or user correction that is not yet in the stable template library.

## Default Locations

- Case logs: `docs/ai-analysis-diagram-factory/cases/`
- Candidate templates: `references/candidate-templates/`
- Stable templates: `references/templates/`

## Capture Rules

Record a sanitized case note when:

- The user says a new style or workflow should be reused.
- A new prompt pattern succeeds across a meaningful task.
- A repeated failure reveals a reusable guardrail.
- A user correction would prevent future template drift.

Do not record:

- full private prompts
- client/customer names
- secrets, tokens, emails, or credentials
- absolute local project paths
- private document content
- complete copyrighted source text

## Promotion Rules

1. Capture the case with `scripts/capture_case.py`.
2. If the case is reusable, extract a candidate with `scripts/extract_template_candidate.py`.
3. Keep the candidate in `references/candidate-templates/` until reviewed.
4. Score related outputs with `references/scoring-rubric.md` or `scripts/score_case.py`.
5. Promote only after explicit user approval using `scripts/promote_template.py --confirm PROMOTE`.
6. After promotion, run script tests and skill validation.

## Example

```bash
python3 scripts/capture_case.py \
  --task-type "heritage cultural product board" \
  --template-candidate "heritage-cultural-product-board" \
  --reference-style-summary "aged paper, hand-drawn packaging system, large calligraphy title, product modules" \
  --what-worked "separating main poster, brochure, package, color swatches, and pattern extraction" \
  --what-failed "model may copy reference text or collapse the board into a single illustration" \
  --user-corrections "replace only the theme content; keep the board structure" \
  --should-promote unsure
```

```bash
python3 scripts/extract_template_candidate.py \
  --candidate-id heritage-cultural-product-board
```

```bash
python3 scripts/promote_template.py \
  --candidate heritage-cultural-product-board \
  --description "heritage, cultural tourism, and product visual-system boards." \
  --confirm PROMOTE
```
