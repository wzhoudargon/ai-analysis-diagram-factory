# rendering-to-sasaki-board

## use_when
Use for converting an existing site rendering into a professional Sasaki-like post-digital analysis board with a locked left base and extracted right-side modules.

## input_roles
- Site Base rendering: absolute geometry, topology, terrain, and perspective.
- Style instruction/reference: Sasaki-like post-digital diagram board language.

## geometry_lock
Do not alter Site Base topology, terrain, or 3D perspective coordinates. All analysis must be extracted from and attached to the base geometry.

## style_rules
Post-digital collage illustration, Sasaki-like flat materials, matte white/light-gray building models, low-saturation ground, translucent vector vegetation, cyan/orange arrows, dashed lines, node icons, high-key AO light.

## layout_rules
4:3 board. Left 40% main visual converted from Site Base. Right 60% vertical analysis column with three modules: structure enlargement, ecological atlas, construction section. Bottom 5% white information band.

## text_rules
Use minimal sans-serif placeholders or short labels. Avoid dense text.

## prompt_template
```text
Generate a professional international landscape design competition board in post-digital collage style.
Highest priority: do not change the Site Base image's spatial topology, terrain, or 3D perspective coordinates.
Left 40%: convert Site Base into a Sasaki-like post-digital section/perspective with flat materials, white/light-gray conceptual architecture, low-saturation ground, translucent vector vegetation, cyan/orange circulation arrows, dashed lines, zoning polygons, and node icons attached to existing geometry.
Right 60%: three stacked rectangular modules extracted from the left base: top structure enlargement line-art, middle ecological plant atlas, bottom construction/runoff/planting layer section.
Bottom 5%: pure white narrow information band with minimalist sans-serif placeholder labels.
Use thin dashed leaders from right modules to corresponding locations in the left base.
```

## negative_rules
No perspective shift, no deformed massing, no unrelated right modules, no glossy rendering, no harsh shadows, no overfilled text.

## failure_modes
- Right modules are generic and not extracted from base.
- Left base geometry changes.
- Board loses 40/60/5 layout.

## revision_policy
When extraction fails, name specific structures/plants/runoff elements visible in the Site Base.
