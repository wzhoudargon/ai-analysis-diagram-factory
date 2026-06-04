# AI Analysis Diagram Factory

A Codex-compatible skill for producing architecture, landscape, urban-design, planning, and design-analysis image prompts.

It helps an agent:

- separate factual evidence images from style references
- choose reusable design-analysis templates
- preserve map, plan, satellite, rendering, and photo geometry when accuracy matters
- write reusable and project-specific AI image-generation prompts
- score generated outputs with a 100-point rubric
- capture successful new cases into a candidate template queue
- promote approved candidates into a stable template library

This project is model-agnostic. It does not include, train, fine-tune, or call any image model. It is a prompt-template and workflow skill.

## Who It Is For

Use it when you repeatedly create:

- site analysis diagrams
- satellite-to-analysis maps
- location analysis diagrams
- urban renewal boards
- landscape architecture competition boards
- plan-point-to-perspective collage renderings
- rendering-to-analysis diagrams
- site-photo-to-section diagrams
- architecture exploded axonometric diagrams
- city culture and context boards

## Repository Layout

```text
.
├── skill/                         # installable Codex-compatible skill
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/
│   │   ├── template-index.md
│   │   ├── universal-rules.md
│   │   ├── scoring-rubric.md
│   │   ├── iteration-loop.md
│   │   ├── case-capture-workflow.md
│   │   ├── templates/
│   │   └── candidate-templates/
│   └── scripts/
├── examples/
└── docs/
```

## Install

Clone the repository and copy the `skill/` directory into your local Codex skills folder:

```bash
git clone https://github.com/wzhoudargon/ai-analysis-diagram-factory.git
mkdir -p ~/.codex/skills
cp -R ai-analysis-diagram-factory/skill ~/.codex/skills/ai-analysis-diagram-factory
```

Validate the skill:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  ~/.codex/skills/ai-analysis-diagram-factory

python3 ~/.codex/skills/ai-analysis-diagram-factory/scripts/test_skill_scripts.py
```

## Basic Usage

Ask Codex:

```text
Use $ai-analysis-diagram-factory.
Task: convert a satellite image into a dark professional site-analysis diagram.
The uploaded satellite image is the only geometry source.
Use Chinese labels.
```

The skill should produce:

- project fact register
- selected template ID
- image role separation
- reusable prompt template
- project-specific prompt
- negative constraints
- QA score
- candidate iteration notes

You can also start with a shorter natural-language request:

```text
Use $ai-analysis-diagram-factory to replicate this analysis diagram style and give me a reusable image-generation prompt.
```

For more stable results, include:

- which uploaded image is the style reference
- which uploaded image is the factual source
- the project theme and output language
- whether labels should be Chinese, English, or bilingual

## Template Library

Stable templates live in:

```text
skill/references/templates/
```

The index lives in:

```text
skill/references/template-index.md
```

Every template card uses the same fields:

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

## Capture New Cases

When you use the skill for a new reusable diagram style, record a sanitized case instead of immediately modifying stable templates:

```bash
python3 skill/scripts/capture_case.py \
  --task-type "heritage cultural product board" \
  --template-candidate heritage-cultural-product-board \
  --reference-style-summary "aged paper, calligraphy title, product-system modules" \
  --what-worked "separate main poster, brochure, packaging, swatches, and motifs" \
  --what-failed "may copy reference text or collapse into a single illustration" \
  --user-corrections "replace theme content only" \
  --should-promote unsure
```

Extract a candidate template:

```bash
python3 skill/scripts/extract_template_candidate.py \
  --candidate-id heritage-cultural-product-board
```

Promote only after review:

```bash
python3 skill/scripts/promote_template.py \
  --candidate heritage-cultural-product-board \
  --description "heritage, cultural tourism, and product visual-system boards." \
  --confirm PROMOTE
```

## Privacy

Do not store private prompts, client names, secrets, credentials, emails, absolute project paths, or private document content in case logs or templates.

Use summaries such as:

```text
worked: separating main poster, product modules, and swatches
failed: model copied reference title text
correction: replace theme content only
```

## License

Apache-2.0. See [LICENSE](LICENSE).
