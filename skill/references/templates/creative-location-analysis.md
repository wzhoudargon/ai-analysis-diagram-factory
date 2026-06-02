# creative-location-analysis

## use_when
Use for project location maps that should become a creative city-surface analysis image: foreground street canyon, middle low urban model, far lifted-axis skyline, all from one map.

## input_roles
- Uploaded location map: only spatial source.
- Project name/map labels: optional public verification for names only.

## geometry_lock
Preserve real roads, secondary roads, main axis, cross roads, rivers, parks, bridges, density distribution, public nodes, and project core if visible.

## style_rules
Architectural publication-style city model plus information design. Gray-white model, blue-gray water, yellow roads/nodes, sparse green parks, restrained shadows, no photorealism.

## layout_rules
Vertical 2:3. Bottom foreground street canyon along main axis. Middle low flattened city model. Far background axis lifts into dramatic skyline. Sides flatten and stretch to fill the image.

## text_rules
Use few clear Chinese labels only. Omit uncertain names. Avoid map-software POI clutter.

## prompt_template
```text
Generate a creative urban design location analysis image from the uploaded project map.
The uploaded map is the only spatial basis. Preserve roads, water, parks, bridges, density, and key public nodes.
Transform the same continuous map surface from bottom foreground street canyon into middle low city model and then into far lifted-axis skyline. This must be one continuous city surface, not separate scenes.
Foreground: main urban axis enters from bottom center, with tall gray street-wall buildings and strong canyon feeling.
Middle: city compresses into low gray-white blocks with map-like roads, water, and parks.
Far: central axis lifts dramatically into high slender city core; side areas stay lower, stretched, and flattened.
Use blue-gray water, gray-white buildings, yellow roads and nodes, sparse green parks, publication-style layout, and limited Chinese labels.
```

## negative_rules
No ordinary 3D map, no simple curled map, no random skyline, no hard scene cut, no unrelated city, no UI, no POI icons, no colorful commercial map.

## failure_modes
- Becomes a generic bird's-eye city model.
- Entire map lifts uniformly.
- Sides leave blank space.

## revision_policy
If the concept fails, restate the three-part continuous transformation as the highest priority.
