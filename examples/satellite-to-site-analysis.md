# Example: Satellite To Site Analysis

User request:

```text
Use $ai-analysis-diagram-factory.
Task type: satellite image to professional site analysis diagram.
The uploaded satellite image is the only source for roads, water, building grain, terrain, and site position.
Style: dark low-saturation competition analysis map with orange site highlight, magenta connection network, blue water emphasis, and Chinese labels.
```

Expected skill output:

- Template selection: `satellite-to-site-analysis`
- Image role separation:
  - uploaded satellite image = factual evidence
  - style references, if any = visual language only
- Prompt sections:
  - preserve real spatial structure
  - convert satellite texture into dark analytical base
  - add vector site highlight, networks, ecological buffers, icons
  - use concise Chinese labels
  - avoid UI, map pins, fake roads, and gibberish text

QA focus:

- water edges are not moved
- roads follow the original structure
- labels are short and readable
- the output is a diagram, not a navigation map
