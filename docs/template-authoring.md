# Template Authoring

Stable templates live in `skill/references/templates/`.

Create a skeleton:

```bash
python3 skill/scripts/new_template_card.py my-template-id \
  --use-when "Use for ..." \
  --output skill/references/candidate-templates/my-template-id.md
```

Every template must include:

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

## Good Template Pattern

Write reusable rules, not one-off project content.

Good:

```text
Preserve uploaded map water edges, roads, building grain, and project site position.
```

Bad:

```text
Preserve the exact lake and street names from this private project.
```

## Image Role Separation

Use this language consistently:

- evidence image = facts and geometry
- style reference = visual language only
- output reference = target output type only

## Geometry Lock

If the task uses a map, plan, satellite image, CAD, photo, or existing rendering, name exactly what must not drift.

Examples:

- shoreline
- road network
- building massing
- courtyard voids
- paths and entrances
- terrain and water
- perspective coordinates

## Failure Modes

A useful failure mode is specific and reusable:

```text
- May copy reference text into the new board.
- May turn a board task into a single illustration.
- May move the shoreline when stylizing the satellite base.
```
