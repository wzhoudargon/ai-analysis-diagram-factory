# satellite-to-site-analysis

## use_when
Use for satellite imagery to professional city/landscape site analysis maps, especially dark low-saturation bases with strong vector overlays.

## input_roles
- Satellite image: only source for spatial structure, roads, water, building grain, terrain, and site position.
- User labels/theme: allowed analysis content.

## geometry_lock
Preserve satellite map structure, road direction, water boundary, building grain, terrain relationship, and project site position.

## style_rules
Dark desaturated black/white/gray satellite-analysis base, orange/yellow project highlight, magenta city connection network, blue-white water system, white dashed arcs, icons, and abstract trees.

## layout_rules
Keep original aerial/bird view. Horizontal competition-board-ready composition unless the user specifies otherwise.

## text_rules
Use Chinese only when requested. Keep important names only. Remove low-importance map labels. No English in Chinese tasks.

## prompt_template
```text
Use the uploaded satellite image as the only spatial source. Preserve true spatial structure, roads, water boundaries, building grain, terrain, and project location.
Convert the satellite image into a dark, low-saturation analytical base while weakening photo texture.
Highlight the core project site with orange-yellow translucent fill and clear outline.
Add magenta urban connection networks aligned to actual roads and spatial axes, with magenta nodes at key intersections.
Strengthen water with white-to-light-blue translucent gradients, waterline outlines, and restrained contour/wave lines.
Add white dashed arcs for views, ecological migration, urban radiation, or cultural links. Add abstract tree silhouettes, landscape patches, node icons, and concise Chinese labels.
Final result: professional urban design / landscape competition analysis map with strong spatial narrative.
```

## negative_rules
No changed satellite structure, no fake roads, no English labels in Chinese tasks, no map UI, no brand logo, no overdecorated clutter, no ordinary navigation-map look.

## failure_modes
- Overlays do not follow real roads/water.
- Satellite base becomes too realistic or too illustrative.
- Chinese labels become unreadable.

## revision_policy
For label failure, reduce generated text and recommend deterministic overlay.
