# photo-to-section-analysis

## use_when
Use for site photos that should become ecological corridor section-analysis diagrams.

## input_roles
- Site photo: evidence for terrain, vegetation, paths, water, urban edge, and ecological corridor character.
- Style reference: section-board language only.

## geometry_lock
Extract real slope, horizon, vegetation masses, water/path positions, and built edges from the photo. Do not invent unsupported topography.

## style_rules
International landscape urbanism board; clean white background, fine linework, pale pink terrain fill, light green gradients, delicate tree silhouettes, muted red accents.

## layout_rules
Wide horizontal format. Continuous left-to-right terrain section, callouts, species icons, seasonal bands, distance scale, land-use labels, and small route/location inset.

## text_rules
Use concise labels. Chinese labels if requested. Avoid large paragraphs.

## prompt_template
```text
Create a professional landscape urbanism ecological corridor section-analysis diagram from the uploaded site photo.
Analyze visible terrain, vegetation, paths, water, buildings, and corridor conditions. Convert them into a continuous left-to-right terrain section.
Use clean white background, thin architectural linework, soft pale pink terrain fill, light green vegetation gradients, delicate tree silhouettes, tiny people and bicycles, circular ecological callouts, species icons, seasonal/time-sequence bands, distance scale, land-use segment labels, and a small route/location map inset.
Keep it analytical, refined, information-dense, airy, and legible.
```

## negative_rules
No copied reference labels, no unsupported geography, no photorealistic background, no fake section cut unrelated to photo.

## failure_modes
- Diagram ignores photo evidence.
- Becomes landscape illustration instead of section analysis.
- Too much text.

## revision_policy
If the section is generic, list exact visible photo elements in the prompt before style.
