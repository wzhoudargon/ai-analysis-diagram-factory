#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List

import new_template_card


SKILL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CASE_DIR = Path("docs/ai-analysis-diagram-factory/cases")
DEFAULT_CANDIDATE_DIR = SKILL_ROOT / "references" / "candidate-templates"


def load_case(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matching_cases(case_dir: Path, candidate_id: str) -> List[Dict[str, Any]]:
    cases = []
    for path in sorted(case_dir.glob("*.json")):
        record = load_case(path)
        if record.get("candidate_template_name") == candidate_id:
            cases.append(record)
    return cases


def bullet_list(values: Iterable[str], fallback: str) -> str:
    items = [value.strip() for value in values if value and value.strip()]
    if not items:
        return fallback
    return "\n".join(f"- {item}" for item in items)


def render_candidate(candidate_id: str, cases: List[Dict[str, Any]]) -> str:
    task_types = sorted({case.get("task_type", "") for case in cases if case.get("task_type")})
    goals = bullet_list((case.get("project_goal", "") for case in cases), "- [Add reusable project goals.]")
    style = bullet_list((case.get("reference_style_summary", "") for case in cases), "- [Add reusable style rules.]")
    worked = bullet_list((case.get("what_worked", "") for case in cases), "- [Add patterns that worked.]")
    failed = bullet_list((case.get("what_failed", "") for case in cases), "- [Add known failures.]")
    corrections = bullet_list((case.get("user_corrections", "") for case in cases), "- [Add user corrections if any.]")
    prompt_patterns = bullet_list((case.get("final_prompt_pattern", "") for case in cases), "- [Add reusable prompt pattern.]")

    sections = {
        "use_when": f"Candidate template extracted from {len(cases)} case(s). Use for: {', '.join(task_types) or '[task type]'}.",
        "input_roles": "- Evidence image(s): real project facts, geometry, site content, and required subject matter.\n- Style reference image(s): visual language, layout, material mood, color, and graphic grammar only.\n- Output reference image(s): target output type and quality only.",
        "geometry_lock": "Preserve factual geometry and subject identity from evidence images. If the case has no strict geometry source, preserve the user's named theme, object system, and program relationships instead of copying reference content.",
        "style_rules": f"{style}\n\nPatterns that worked:\n{worked}",
        "layout_rules": f"Derive layout from repeated successful case structure. Reusable goals observed:\n{goals}",
        "text_rules": "Use short, deliberate labels in the requested language. Avoid fake paragraphs, copied reference labels, and random glyphs. For exact Chinese, prefer deterministic post-edit overlays when needed.",
        "prompt_template": f"```text\n[Candidate template: {candidate_id}]\nUse the evidence image(s) as factual source and the style reference only for visual language.\n[Task / theme]: [fill in]\n[Geometry or subject lock]: [fill in]\n[Layout modules]: [fill in]\n[Style system]: [fill in]\n[Required labels]: [fill in]\n[Negative constraints]: do not copy reference text, watermark, logo, project content, or unsupported geometry.\n\nObserved reusable prompt patterns:\n{prompt_patterns}\n```",
        "negative_rules": "Do not copy reference-project content, do not invent unsupported site facts, do not merge old conversation evidence into the current case, and do not generate the wrong output type.",
        "failure_modes": f"{failed}\n\nUser corrections to respect:\n{corrections}",
        "revision_policy": "Candidate only. Review against real outputs, score with the rubric, and promote into stable templates only after explicit user approval.",
    }

    lines = [f"# {candidate_id}", ""]
    for field in new_template_card.REQUIRED_FIELDS:
        lines.extend([f"## {field}", sections[field], ""])
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract a candidate template card from sanitized case records.")
    parser.add_argument("--candidate-id", required=True, help="Hyphen-case candidate template id.")
    parser.add_argument("--case-dir", default=str(DEFAULT_CASE_DIR))
    parser.add_argument("--output-dir", default=str(DEFAULT_CANDIDATE_DIR))
    args = parser.parse_args()

    cases = matching_cases(Path(args.case_dir), args.candidate_id)
    if not cases:
        raise SystemExit(f"No case records found for candidate: {args.candidate_id}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / f"{args.candidate_id}.md"
    output.write_text(render_candidate(args.candidate_id, cases), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
