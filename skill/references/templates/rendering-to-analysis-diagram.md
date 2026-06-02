# rendering-to-analysis-diagram

## use_when
Use when an existing architectural/landscape rendering should become a spatial strategy or analysis diagram while preserving perspective and spatial coordinates.

## input_roles
- Evidence rendering: exact spatial geometry, perspective, massing, topography, and site layout.
- Style references: analysis overlay language only.

## geometry_lock
Maintain original 3D perspective, spatial coordinates, topography, building positions, landscape massing, and boundaries. Overlays must attach to existing geometry.

## style_rules
Convert realism into clean post-digital vector collage: white/gray conceptual masses, muted flat ground, abstract vegetation, saturated arrows, dashed lines, zoning polygons, node icons.

## layout_rules
Keep the original view as base. Add analysis overlays snapped to paths, spaces, slopes, boundaries, and nodes.

## text_rules
Use concise labels. If Chinese labels are required, keep them short and consider post-edit overlay.

## prompt_template
```text
Transform the uploaded rendering into a professional architectural and landscape spatial strategy diagram.
Strictly maintain the original spatial geometry, topography, structural layout, and perspective coordinates.
Strip photorealistic texture into a clean diagrammatic base: matte white/light-gray architectural masses, low-saturation flat ground colors, translucent geometric vegetation, and soft uniform global illumination.
Overlay infographic analysis elements that snap to the existing site: saturated arrows along real paths, dashed lines, precise zoning polygons, node icons, and strategy markers.
Do not deform, shift, or regenerate the buildings, landscape masses, terrain, or boundaries.
The result should look like a polished post-digital vector collage diagram by a top-tier urban design studio.
```

## negative_rules
No changed perspective, no shifted massing, no random overlays, no photorealistic textures, no harsh shadows, no decorative arrows detached from space.

## failure_modes
- Base geometry changes while restyling.
- Overlays float in screen space.
- Result remains a render, not an analysis diagram.

## revision_policy
If geometry changes, move geometry lock before style instructions and name exact structures to preserve.
