# architecture-exploded-axonometric-diagram

## use_when
Use when the user provides a building image, architectural drawing, model screenshot, plan/section bundle, or building reference and wants a professional architectural exploded axonometric diagram. Use this template when no style reference is uploaded: the exploded drawing style is built into the prompt.

## input_roles
- Evidence image(s): the only source for building massing, roof form, facade rhythm, entrances, courtyard/voids, structural cues, site plinth, and visible circulation.
- In a multi-turn conversation with several previous images, use the most recent user-uploaded building image as the evidence source unless the user explicitly names another file. Ignore all earlier building images and earlier style references by default.
- Optional plan/section images: stronger evidence for floor plates, rooms, vertical circulation, and structure.
- Optional output/style references: use only if provided; otherwise use the built-in style rules below.

## geometry_lock
Preserve the factual building identity from the evidence: primary volume proportions, roof silhouette, courtyard or atrium voids, facade openings, main entrance, stairs, colonnades, structural rhythm, site base, and major alignment. If the evidence does not reveal interior plans, generate abstract zoning blocks instead of fake detailed rooms.

## style_rules
Built-in style: clean vertical architectural exploded axonometric diagram. Default is white and pale-gray linework, but if the user asks to avoid white-model style, switch to extremely simple low-saturation rendering: warm off-white concrete/plaster, pale beige slabs, light blue-gray glass, soft ambient shadows, muted green trees, still with ultra-thin black/dark-gray outlines, gray dashed vertical alignment guides, muted warm-orange program highlights, red dashed circulation arrows, sparse gray leader lines, off-white background, and refined architecture competition / portfolio drawing quality.

## layout_rules
Use a vertical composition. Stack 3-5 exploded horizontal layers with consistent spacing and one shared axonometric angle. Typical layers: roof system, upper envelope/room layer, main program floor, ground/entry floor, site plinth/base. Keep layers aligned so the building reads as one coherent object.

## text_rules
Use only short labels provided by the user or these safe defaults: ROOF SYSTEM, PUBLIC SPACE, COURTYARD, MAIN ENTRY, CIRCULATION, SUPPORT SPACE, STRUCTURE, SITE PLINTH. Prefer English labels unless the user asks for Chinese. Do not generate paragraphs or copied reference labels.

## prompt_template
```text
Generate one professional architectural exploded axonometric analysis diagram from the uploaded building evidence.

Input roles:
- If the conversation contains previous building images or reference diagrams, ignore all earlier images. Use the most recent user-uploaded building image only, unless the user explicitly says to use multiple images.
- The uploaded building image(s) are the only factual source. Use them for building massing, roof form, facade rhythm, visible openings, entrance position, courtyard/atrium voids, structural rhythm, site plinth, stairs, colonnades, and visible circulation.
- No style reference is required. Use the built-in style described below.
- If additional plan/section images are present, use them to improve floor plate, room, circulation, and structural accuracy.

Core task:
Create a clean vertical exploded axonometric architectural diagram of [building/project].
Separate the building into [3-5] clear horizontal layers:
1. [roof system]
2. [upper envelope / upper floor]
3. [main program / public floor]
4. [ground floor / entry layer]
5. [site plinth / structural base]

Geometry and fact constraints:
- Preserve the recognizable building identity from the uploaded evidence.
- Preserve roof silhouette, main volume proportions, facade openings, entrance relationship, courtyard/atrium voids, colonnades, stair positions, and site base when visible.
- Keep all layers in one coherent axonometric angle and align them with thin gray dashed vertical guide lines.
- If interior layouts are not visible, show restrained conceptual zoning blocks instead of invented detailed room plans.
- Do not invent extra towers, wings, bridges, courtyards, stairs, floors, structural systems, or room layouts unsupported by the evidence.

Built-in visual style:
- Clean off-white or pale gray background.
- White and pale-gray building bodies with ultra-thin black/dark-gray outlines by default.
- If the user asks for simple rendering rather than white model style, use extremely restrained low-saturation material rendering: warm off-white concrete/plaster, pale beige floor slabs, light blue-gray glass transparency, muted green vegetation, and very soft ambient shadows while keeping the diagram clean.
- Crisp architectural drafting linework, precise roof/floor outlines, minimal material shading.
- Muted warm-orange translucent fills for key program zones or public spaces.
- Red dashed arrows and red dotted paths for circulation routes.
- Gray dashed leader lines and vertical alignment guides.
- Minimal soft gray shadows only where needed for depth.
- Sparse human silhouettes only if useful for scale.
- Elegant, technical, uncluttered, print-sharp, architecture competition / portfolio quality.

Analysis content:
- Highlight [key program zones] with muted orange.
- Show [main circulation system] with red dashed paths.
- Show [structural/spatial logic] with gray guide lines.
- Add only these labels: [label list].

Text constraints:
- Use short clean labels only.
- Do not generate paragraphs.
- Do not add extra random text, fake labels, watermark, logo, copyright mark, UI elements, or reference-image text.

Final output:
One high-resolution vertical architectural exploded axonometric analysis diagram, suitable for architecture portfolio, competition board, or design presentation.
```

## negative_rules
No required style reference, no copied style-reference content if one is provided, no distorted building massing, no invented floors, no fake detailed room plans, no unsupported towers/wings/bridges/courtyards/stairs, no mechanical product-explosion look, no photorealistic rendering, no cartoon style, no random text, no watermark, no logo, no UI, no paragraphs.

## failure_modes
- In long conversations, the model may accidentally reuse an earlier building or style reference instead of the latest uploaded building. Fix by saying "ignore all earlier images; use the most recent uploaded building only" at the top of the prompt.
- The model invents detailed rooms from a single exterior image.
- The output becomes a photorealistic render instead of a linework diagram.
- Layers drift and no longer align as one building.
- Red circulation and orange highlights float without attaching to floors or paths.
- It copies labels or content from an optional style reference.

## revision_policy
If users repeatedly omit plans/sections, keep the prompt conservative: use abstract zoning blocks and visible building layers only. If style drifts, strengthen the built-in style paragraph rather than requiring a style reference.
