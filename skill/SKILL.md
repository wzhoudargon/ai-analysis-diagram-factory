---
name: ai-analysis-diagram-factory
description: Build AI image-generation prompts and updateable template workflows for architecture, landscape, urban design, satellite-map, site-photo, plan-to-perspective, location-analysis, competition-board, and rendering-to-analysis diagram tasks. Use when Codex needs to choose a design-analysis image template, separate factual evidence images from style references, write reusable and project-specific image prompts, score generated results, capture reusable new cases, or propose template-library revisions without automatically overwriting stable templates.
---

# AI Analysis Diagram Factory

## Purpose

Generate professional design-analysis image prompts from a maintained template library. Treat this as a prompt production, QA, and template-capture system, not model training.

## Core Workflow

1. Classify the user's request and input images.
2. Read `references/template-index.md` and select the closest template card from `references/templates/`.
3. If the task needs strict map, plan, satellite, photo, or rendering fidelity, read `references/universal-rules.md`.
4. Produce:
   - Project fact register
   - Chosen template ID and selection reason
   - Image role separation: factual evidence, style reference, output reference
   - Reusable prompt template with placeholders
   - Project-specific prompt
   - Negative constraints
   - QA score using `references/scoring-rubric.md`
   - Candidate iteration notes
5. If the user asks to improve a template from a failure case, read `references/iteration-loop.md` and use `scripts/score_case.py` to draft a candidate revision. Do not directly change stable templates unless the user explicitly approves the merge.
6. If the task produces a reusable new diagram type, prompt pattern, or user correction that is not yet in the library, read `references/case-capture-workflow.md`. Record a sanitized case with `scripts/capture_case.py`, extract a candidate template only when appropriate, and never promote it to stable templates without explicit user approval.

## Image Role Rules

- Factual evidence images provide real spatial structure, project facts, geometry, and content.
- Style reference images provide only layout, atmosphere, visual grammar, color, material handling, and annotation language.
- Output reference images provide target output type only, not facts to copy.
- Never copy reference-project names, labels, watermarks, logos, geography, landmarks, building forms, or copyrighted text into the new output.
- When factual evidence is a map, plan, CAD, satellite image, site photo, or rendering, preserve analysis-critical geometry unless the user explicitly asks for redesign.

## Template Selection

Use the template index first. If two templates match:

- Prefer the one matching the user's input type over the desired style.
- Prefer geometry-lock templates for maps, satellite images, CAD, plans, and existing renderings.
- Prefer board templates when the user asks for a complete presentation board.
- Prefer scene templates when the user asks for one perspective, collage, or rendering.

## Resources

- `references/template-index.md` - template selection map.
- `references/universal-rules.md` - cross-template hard rules.
- `references/scoring-rubric.md` - 100-point QA scoring.
- `references/iteration-loop.md` - safe update process.
- `references/case-capture-workflow.md` - capture new cases and promote candidate templates safely.
- `references/templates/` - individual template cards.
- `references/candidate-templates/` - unmerged candidate cards.
- `scripts/new_template_card.py` - generate a new template card skeleton.
- `scripts/score_case.py` - score a result and draft candidate revision notes.
- `scripts/capture_case.py` - record a sanitized reusable case note.
- `scripts/extract_template_candidate.py` - draft a candidate template from case notes.
- `scripts/promote_template.py` - promote an approved candidate template and update the index.

## Output Shape

For normal prompt production:

```markdown
**Project Fact Register**

**Template Selection**

**Image Role Separation**

**Reusable Prompt Template**

**Project-Specific Prompt**

**Negative Constraints**

**QA Score**

**Candidate Iteration Notes**
```

For template updates, make the candidate revision explicit and label it as not merged until approved.

For reusable new cases, report where the case was captured, whether a candidate template was created, and whether it still needs approval before promotion.
