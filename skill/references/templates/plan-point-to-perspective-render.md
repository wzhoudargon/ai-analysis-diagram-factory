# plan-point-to-perspective-render

## use_when
Use when the first image is a project plan/master plan with a marked point and arrow, and the user wants a human-eye-level architectural or landscape collage perspective from that point.

## input_roles
- Image 1: only spatial and factual source.
- Other images: style references only for mood, collage language, material expression, color, and atmosphere.

## geometry_lock
Use target point and arrow as camera location and direction. Preserve nearby roads, paths, plazas, edges, buildings, water, planting, openings, focal points, and foreground/midground/background hierarchy.

## style_rules
Low-saturation architectural competition collage; quiet, misty, elegant, paper collage plus watercolor wash, soft rendering, pale sky, layered plants, cut-out people.

## layout_rules
One complete human-eye-level or slightly raised pedestrian perspective. Not bird's-eye, axonometric, section, plan, or commercial render.

## text_rules
No text in final image unless explicitly requested. Never show plan labels, red points, arrows, view cones, dimensions, logos, watermarks, or UI.

## prompt_template
```text
You will receive multiple images.
Image 1 is the project plan/master plan and is the only spatial and factual source.
All other images are style references only. Use them for atmosphere, collage language, material expression, color, and composition mood. Do not copy buildings, scenes, watermarks, logos, text, or copyrighted information.
Target point: [point label]. If an arrow/view cone is present, strictly use it as the camera direction. If no direction is provided, infer the most reasonable eye-level view from nearby roads, openings, entrances, plaza, buildings, water, and green space.
Camera height: about 1.6m.
Translate the plan around this point into a real walking perspective. Preserve nearby paths, roads, plazas, edges, building massing, planting, water, activity nodes, and foreground/midground/background relationships.
Style: quiet low-saturation architectural competition collage, pale gray-white sky, diffuse misty daylight, warm gray/gray-green/off-white/beige palette, paper texture, watercolor vegetation, clean simple architecture, cut-out people, restrained detail.
Final output: one polished perspective suitable for presentation, clearly generated from the marked point.
```

## negative_rules
No plan itself, no target circle, no arrow, no labels, no dimensions, no logo, no watermark, no random text, no invented major buildings/water/bridges/towers/mountains/skylines, no commercial render, no anime/cartoon.

## failure_modes
- Output is bird's-eye or axonometric.
- Plan marker or labels remain visible.
- Major spatial elements invented outside the plan.

## revision_policy
If viewpoint is wrong, create an intermediate viewpoint brief before the image prompt.
