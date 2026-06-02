#!/usr/bin/env python3
import argparse
from pathlib import Path

REQUIRED_FIELDS = [
    "use_when",
    "input_roles",
    "geometry_lock",
    "style_rules",
    "layout_rules",
    "text_rules",
    "prompt_template",
    "negative_rules",
    "failure_modes",
    "revision_policy",
]


def render_card(template_id: str, use_when: str = "[Describe when to use this template.]") -> str:
    sections = {
        "use_when": use_when,
        "input_roles": "- Evidence image(s): [facts and geometry]\n- Style reference image(s): [visual language only]\n- Output reference image(s): [target output type only]",
        "geometry_lock": "[Name the exact site elements that must keep observed shape, position, direction, and relationship.]",
        "style_rules": "[Reusable visual language, color, material, atmosphere, and rendering rules.]",
        "layout_rules": "[Canvas ratio, board grid, module order, hierarchy, and composition.]",
        "text_rules": "[Language, label limits, text placement, and anti-gibberish constraints.]",
        "prompt_template": "```text\n[Write the reusable AI image-generation prompt with placeholders.]\n```",
        "negative_rules": "[What to avoid, including copied references, geometry drift, UI, watermarks, and wrong output type.]",
        "failure_modes": "- [Known failure 1]\n- [Known failure 2]",
        "revision_policy": "Record failures as candidate revisions first. Merge into this card only after user approval.",
    }

    lines = [f"# {template_id}", ""]
    for field in REQUIRED_FIELDS:
        lines.extend([f"## {field}", sections[field], ""])
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a template card skeleton.")
    parser.add_argument("template_id", help="Hyphen-case template id")
    parser.add_argument("--use-when", default="[Describe when to use this template.]")
    parser.add_argument("--output", help="Optional output path")
    args = parser.parse_args()

    card = render_card(args.template_id, args.use_when)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(card, encoding="utf-8")
    else:
        print(card, end="")


if __name__ == "__main__":
    main()
