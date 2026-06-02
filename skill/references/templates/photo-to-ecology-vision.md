# photo-to-ecology-vision

## use_when
Use for real site photo/map/plan to panoramic ecological landscape vision diagram with calm analysis overlays.

## input_roles
- Style reference: misty ecological wetland vision and annotation language.
- Factual site reference: real spatial organization.

## geometry_lock
Preserve main water body, shoreline, paths, boardwalks, bridges, decks, plazas, buildings, trees, slopes, urban edge, and activity nodes from factual image.

## style_rules
Soft semi-realistic Photoshop landscape collage, watercolor mist, low-saturation natural colors, pale sky, calm reflective water, controlled vegetation, refined ecological mood.

## layout_rules
Ultra-wide 2:1 panorama. Central water/landscape system. Flowing path/shoreline/corridor. Thin annotation leader lines, small colored dots, teal ecological pictogram icons.

## text_rules
Use sparse short Chinese labels. No dense paragraphs. Labels must explain real spatial or ecological functions.

## prompt_template
```text
Generate a wide 2:1 panoramic ecological landscape vision diagram for [project type/location].
Use Image 1 as style reference only. Use Image 2 as factual site reference.
Translate the factual site into the reference visual language while preserving real spatial organization: [water], [path/boardwalk], [buildings/landmarks], [trees/grass/wetland], [activity nodes].
Show [stormwater retention / flood resilience / habitat restoration / slow mobility / waterfront public life / ecological education] as analysis content.
Add thin annotation leader lines, small colored category dots, teal circular ecological pictogram icons, and sparse Chinese labels.
Keep the image mature, restrained, clean, and professionally rendered with clear foreground, midground, and background.
```

## negative_rules
No raw photo, no generic fantasy landscape, no noisy vegetation, no crowded overlays, no unsupported labels, no high-frequency texture.

## failure_modes
- Analysis overlay becomes decorative.
- Site organization is replaced by generic wetland.
- Too much surface noise.

## revision_policy
If generic, provide a tighter fact register before prompt generation.
