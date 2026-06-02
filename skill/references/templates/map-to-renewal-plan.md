# map-to-renewal-plan

## use_when
Use for map/satellite evidence to generate a soft pastel 2.5D axonometric urban-life design analysis or renewal plan.

## input_roles
- Project evidence image: real geometry and site elements.
- Reference image: style, layout, drawing language, colors, public-life atmosphere, and analysis structure.

## geometry_lock
Preserve water, wetland/green space, main roads, paths, buildings, boundary, and major spatial relationships.

## style_rules
Soft pastel 2.5D axonometric urban-life analysis illustration, white background, pale buildings, pale green open space, soft cyan water, light roads, delicate trees, small people, dashed arrows, icons, callouts.

## layout_rules
Wide horizontal board with main 2.5D site drawing and simple bottom legend or callouts.

## text_rules
Exact Simplified Chinese only when requested. Keep labels short.

## prompt_template
```text
Create a professional urban design analysis diagram in the same style as the reference image.
Use the reference image only for visual style and analysis structure.
Use the project evidence image only for real facts and geometry. Preserve [water], [green space], [roads], [paths], [buildings], [boundary], and spatial relationships.
Redraw the site in soft pastel 2.5D axonometric style with pale buildings, pale green open space, cyan water, light gray roads, delicate trees, people, cyclists, dashed arrows, icons, white callout bubbles, and bottom legend.
Project: [project name/location/theme/scope].
Use only these Chinese labels: [labels].
```

## negative_rules
No raw map screenshot base, no fake roads, no fake lake shape, no unsupported buildings, no foreign language, no illegible Chinese.

## failure_modes
- Raw map stays visible.
- Geometry lock conflicts with axonometric restyle.
- Chinese labels drift or become wrong.

## revision_policy
For strict text, recommend deterministic post-edit labels.
