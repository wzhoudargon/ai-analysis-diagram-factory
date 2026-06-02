# accurate-location-map-analysis

## use_when
Use for true map screenshots plus a style reference to generate accurate project location analysis diagrams, optionally with web-verified surrounding context.

## input_roles
- Map images: only spatial basis for roads, water, project location, boundaries, and nearby nodes.
- Style reference: layout, color, layer organization, labeling style only.
- Project name/location text: query seed for public verification.

## geometry_lock
Do not move real administrative boundaries, roads, water, project marker, transit nodes, or landmarks. If not verifiable, omit rather than invent.

## style_rules
Use the provided style reference. Keep an architectural, urban design, or landscape planning research quality.

## layout_rules
May include multi-scale location maps, main context map, 1km/3km/5km rings, surrounding functions, and concise summary labels.

## text_rules
Use accurate place names only. Avoid map-software POI clutter. Prefer short Chinese labels when the task is Chinese.

## prompt_template
```text
Based on the uploaded real map images, generate a project location analysis diagram for [project name/location].
Use map images as the only spatial framework. Read true administrative position, roads, water, project location, traffic nodes, and surrounding points. Do not invent or move real points.
Use the final style reference image only for layout, color, layer organization, label style, and overall mood. Do not copy its map content or text.
If web verification is available, verify only high-confidence public facts: administrative area, coordinates or approximate anchor, roads, transit, water, parks, commercial/residential/campus/cultural facilities, and useful 1km/3km/5km context. Omit uncertain information.
Create a clean professional location analysis diagram with preserved map structure, accurate relative positions, multi-level location insets, main context map, surrounding analysis rings, and concise labels.
```

## negative_rules
No invented roads/stations/landmarks, no abstract wrong map shape, no copied style-reference content, no fake labels, no cluttered POIs, no UI artifacts.

## failure_modes
- Web facts override uploaded map geometry.
- Labels are confident but false.
- Style reference content leaks.

## revision_policy
When uncertainty is high, reduce labels and privilege uploaded map geometry over completeness.
