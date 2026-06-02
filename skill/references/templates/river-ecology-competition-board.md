# river-ecology-competition-board

## use_when
Use for uploaded satellite or river maps that should become a dense vertical landscape architecture competition board about river ecology, meander history, flood risk, remediation, agriculture, settlement, and tourism.

## input_roles
- Evidence image: satellite map or river map, only source for river morphology and geography.
- Style references: board density, Swiss grid, editorial hierarchy, collage/vector language only.

## geometry_lock
Preserve original river course, oxbows, water edges, roads, settlements, fields, and regional structure. Do not straighten, relocate, or simplify the river into a generic ribbon.

## style_rules
High-end LAF/ASLA-style academic board; off-white background, dark green river system, black/gray diagrams, subtle beige textures, vector precision, mixed media collage.

## layout_rules
Vertical A1 board. Dominant master plan with continuous river system. Add analysis diagrams, evolution sequence, hydrology arrows, regional maps, charts, timeline, photo collage, concept system diagram, strategy process, and bottom visual collage.

## text_rules
Use small clean English labels only. No large paragraphs. Keep labels diagrammatic and minimal.

## prompt_template
```text
Based on the uploaded satellite map, generate a complete vertical landscape architecture competition board for [river/site].
STRICT: preserve the original geographic structure and river morphology from the satellite image. Do not distort site layout.
Create a high-end competition board with Swiss grid layout, off-white background, dark green river system, black/gray diagrams, subtle beige textures, mixed media collage, and vector diagrams.
Include: dominant MASTER PLAN derived from the real river, meander evolution diagrams, oxbow formation diagrams, hydrological flow arrows, regional mapping, flood frequency chart, historical transformation timeline, grayscale problem photo collage, ecology/agriculture/settlement/tourism concept diagram, linear intervention strategy diagrams, and bottom photorealistic landscape collage.
Use ultra-thin lines, dashed arrows, layered transparency, architectural diagram aesthetics, dense information, crisp print-quality graphics, and minimal English labels.
This is a professional information-driven landscape architecture competition board, not illustration, concept art, or standalone rendering.
```

## negative_rules
No distorted river, no invented geography, no copied map labels, no UI, no watermarks, no empty poster areas, no decorative-only diagrams, no large paragraphs.

## failure_modes
- River shape becomes generic.
- Board turns into one illustration instead of information system.
- Text becomes dense unreadable filler.

## revision_policy
Tighten geometry lock first when river morphology drifts. Split into master-plan plus board-composition stages if density fails.
