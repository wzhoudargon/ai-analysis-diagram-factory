# Contributing

Contributions should improve reusable design-analysis prompt workflows without adding private project data.

## What To Contribute

- New template cards
- Safer geometry-lock wording
- Better failure modes
- Scoring improvements
- Script tests
- Model-agnostic examples

## Template Contribution Rules

Every template card must include:

- `use_when`
- `input_roles`
- `geometry_lock`
- `style_rules`
- `layout_rules`
- `text_rules`
- `prompt_template`
- `negative_rules`
- `failure_modes`
- `revision_policy`

Do not include:

- private project names
- client data
- exact copyrighted source text
- watermarks or logos from references
- secrets, tokens, or credentials
- absolute local paths

## Safe Workflow

1. Record a sanitized case with `capture_case.py`.
2. Extract a candidate card with `extract_template_candidate.py`.
3. Review and edit the candidate.
4. Score real outputs with `score_case.py`.
5. Promote only when the template is reusable.
6. Run validation.

```bash
python3 skill/scripts/test_skill_scripts.py
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill
```

## Style

Keep `SKILL.md` concise. Put detailed workflow material in `references/`.
