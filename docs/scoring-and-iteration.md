# Scoring And Iteration

Use `skill/references/scoring-rubric.md` for output QA.

Categories:

- Geometry / factual fidelity: 30
- Style stability: 20
- Layout and information hierarchy: 15
- Text and label hygiene: 15
- Image role separation: 10
- Professional finish: 10

Score a failure:

```bash
python3 skill/scripts/score_case.py \
  --template-id satellite-to-site-analysis \
  --task-goal "Create a dark satellite site analysis diagram." \
  --failure-description "The output moved the shoreline and generated unreadable Chinese labels."
```

## Veto Flags

Treat the result as not ready if:

- key geography or plan geometry changed
- reference content, watermark, logo, or text leaked
- output type is wrong
- critical labels are gibberish

## Capturing New Reusable Cases

Use `capture_case.py` when a task creates a new reusable style or a useful correction:

```bash
python3 skill/scripts/capture_case.py \
  --task-type "new diagram style" \
  --template-candidate new-diagram-style \
  --what-worked "..." \
  --what-failed "..." \
  --user-corrections "..."
```

Extract a candidate:

```bash
python3 skill/scripts/extract_template_candidate.py \
  --candidate-id new-diagram-style
```

Promote only after review:

```bash
python3 skill/scripts/promote_template.py \
  --candidate new-diagram-style \
  --description "short index description." \
  --confirm PROMOTE
```
