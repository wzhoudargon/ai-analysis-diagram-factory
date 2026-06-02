# style-transfer-design-board

## use_when
Use when one image is a board style/layout reference and another is a factual map, satellite image, or plan whose content must replace the reference content.

## input_roles
- Image 1: style and layout reference only.
- Image 2: factual content and spatial structure only.

## geometry_lock
Preserve Image 2 geography, road network, river/water, blocks, boundary, and urban fabric. Remove Image 2 labels unless explicitly needed.

## style_rules
Follow Image 1 grid, hierarchy, color system, diagram language, icon style, and presentation density. Do not copy Image 1 content.

## layout_rules
Rebuild Image 2's content through Image 1's layout logic. Keep the same information hierarchy and module scale relationships as Image 1.

## text_rules
Use sparse labels aligned with the new project. Do not preserve reference text or satellite-map labels.

## prompt_template
```text
Use Image 1 only as visual style and board layout reference. Use Image 2 only as factual site content and spatial structure.
Strictly preserve Image 2 geography, river/water, roads, urban grain, boundary, and scale relationships.
Remove all original labels from Image 2.
Reconstruct a professional design board using Image 1's grid system, module hierarchy, color palette, line weights, icon grammar, and information density.
Replace all reference content with new site analysis: [theme], [key systems], [intervention strategy], [urban/ecological relationships].
Do not copy Image 1 names, maps, landmarks, graphics, or text.
```

## negative_rules
No copied reference city/content, no changed factual map, no pasted raw satellite screenshot unless style requires it, no fake labels, no wrong output type.

## failure_modes
- Style transfer copies reference content.
- Factual image geometry drifts.
- Board becomes generic collage.

## revision_policy
When style leaks facts, make input roles the first paragraph and repeat "style only / facts only" before layout instructions.
