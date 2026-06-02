# Example: Plan Point To Perspective

User request:

```text
Use $ai-analysis-diagram-factory.
Task type: convert one marked point on a master plan into a human-eye-level landscape perspective.
Image 1 is the only spatial source.
Other uploaded images are style references only.
Follow the red arrow direction if present.
```

Expected skill output:

- Template selection: `plan-point-to-perspective-render`
- Camera logic:
  - target point = viewer position
  - arrow/view cone = camera direction
  - default eye height = pedestrian eye level
- Prompt sections:
  - foreground, midground, background organization
  - geometry lock for paths, water, buildings, planting, plazas
  - competition collage style
  - no plan labels, arrows, red points, logos, or watermarks in final image

QA focus:

- the result is not bird's-eye or axonometric
- visible spatial relationships match the plan
- style references do not leak their project content
