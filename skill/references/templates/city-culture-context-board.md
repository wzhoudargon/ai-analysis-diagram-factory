# city-culture-context-board

## use_when
Use for city or country architecture/culture/context analysis boards based on uploaded photos and/or web-researched public city facts.

## input_roles
- Target city/country: research basis.
- Uploaded photos: priority visual evidence if provided.
- Reference board: style, layout rhythm, collage language, theme color, and analysis structure only.

## geometry_lock
Use real city geography and landmarks. Do not include landmarks from the wrong city. Map should be faded support, not dominant unless requested.

## style_rules
Vintage architecture-school collage, aged paper, printed grain, newspaper texture, black-white cutouts, one strong city color, red/black analysis lines, axonometric tiles, map texture, hand-made dense layout.

## layout_rules
Vertical board. Progressive urban journey around one route: axis, river, coast, ring, mountain-water corridor, historical street, or transit path. One main visual, 3-5 medium anchors, small fragments, bottom continuous long-section collage.

## text_rules
Use short accurate Chinese labels, 4-10 characters where possible. Avoid long paragraphs and tourism poster copy.

## prompt_template
```text
Create a vertical architecture and urban culture analysis board for [city/country].
Use the reference board only for visual style: vintage architecture-school collage, aged paper, dense urban research layout, black-white cutouts, one theme color, analytical lines, axonometric tiles, map texture, timeline, and hand-made composition.
Research or use provided facts to define one narrative theme: [theme].
Organize content along this route: [node 1] -> [node 2] -> [node 3] -> [node 4] -> [node 5] -> [node 6] -> [node 7].
Map is faded background only, no more than 20-25% visual weight.
Include title, Chinese title, subtitle, route nodes, 4-5 analytical tiles, timeline, landmarks, geography, material/culture fragments, and bottom continuous architectural long-section collage.
```

## negative_rules
No tourist poster, no clean corporate infographic, no oversized central map, no wrong-city landmarks, no repeated buildings, no cloned images, no fake long text.

## failure_modes
- Board becomes a landmark collage wall.
- Wrong city content appears.
- Map dominates the composition.

## revision_policy
If facts are not verified, stop at research plan and prompt draft rather than generating false content.
