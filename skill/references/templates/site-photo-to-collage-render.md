# site-photo-to-collage-render

## use_when
Use for real site photos and point information to white-background architectural stage collage renderings.

## input_roles
- Uploaded site photos: primary factual visual evidence.
- Public web context: only direct same-place supporting facts, if available.
- Style requirement: white-background stage collage and competition composition.

## geometry_lock
Use only visible or verified same-place buildings, water, roads, bridges, landmarks, skyline, activities, materials, and landscape features. Do not insert unrelated cities or buildings.

## style_rules
White paper background, hard-cut collage edges, black-white and color fragments, large foreground people with white cutout edges, transparent color blocks, analysis lines, paper grain, faded reproduction texture.

## layout_rules
60/25/10/5 hierarchy: 60% main building/space, 25% foreground life scenes, 10% secondary same-place landmarks, 5% analytical marks.

## text_rules
Step 1 no major text. Step 2 may add sparse Chinese labels on tracing-paper tags with thin dashed leader lines.

## prompt_template
```text
Create a horizontal white-background stage-style architectural competition collage from the uploaded site photos and [project/location].
Use only content visible in uploaded photos or publicly verified as the same place. Do not use unrelated buildings, cities, parks, or landmarks.
Organize the image with 60% main architectural/landscape anchor, 25% foreground life scenes, 10% secondary same-place landmarks, and 5% restrained drawing marks.
Use hard collage cuts, white paper background, black-white and color fragments, large scale people with white cutout edges, transparent blue/green/beige/orange blocks, thin outline drawings, dashed movement lines, small anchors, and paper grain.
People must stand only on real accessible ground, steps, plazas, boardwalks, bridge decks, corridors, lawns, or platforms.
```

## negative_rules
No full-photo background, no unrelated city, no floating people, no people in water/reflection, no fake Chinese signs, no sticker clutter, no over-saturation.

## failure_modes
- Full photo remains as background.
- Collage uses unrelated landmarks.
- People float or stand in impossible locations.

## revision_policy
When place identity fails, reduce public-context additions and rely on uploaded photos only.
