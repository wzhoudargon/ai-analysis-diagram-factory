#!/usr/bin/env python3
import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict


DEFAULT_CASE_DIR = Path("docs/ai-analysis-diagram-factory/cases")


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return slug or "case"


def build_case_record(args: argparse.Namespace) -> Dict[str, Any]:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    candidate = slugify(args.template_candidate or args.task_type)
    case_id = args.case_id or f"{timestamp}-{candidate}"
    return {
        "case_id": case_id,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "task_type": args.task_type,
        "input_roles": args.input_roles,
        "reference_style_summary": args.reference_style_summary,
        "project_goal": args.project_goal,
        "prompt_used_summary": args.prompt_used_summary,
        "what_worked": args.what_worked,
        "what_failed": args.what_failed,
        "user_corrections": args.user_corrections,
        "final_prompt_pattern": args.final_prompt_pattern,
        "candidate_template_name": candidate,
        "should_promote": args.should_promote,
        "privacy_note": "Sanitized case record. Do not store full private prompts, client data, secrets, or absolute project paths.",
    }


def write_case(record: Dict[str, Any], case_dir: Path) -> Path:
    case_dir.mkdir(parents=True, exist_ok=True)
    output = case_dir / f"{record['case_id']}.json"
    output.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Record a sanitized reusable image-prompt case.")
    parser.add_argument("--case-id", help="Optional stable case id. Defaults to timestamp + candidate slug.")
    parser.add_argument("--case-dir", default=str(DEFAULT_CASE_DIR), help="Case log directory. Defaults to project docs.")
    parser.add_argument("--task-type", required=True)
    parser.add_argument("--input-roles", default="")
    parser.add_argument("--reference-style-summary", default="")
    parser.add_argument("--project-goal", default="")
    parser.add_argument("--prompt-used-summary", default="")
    parser.add_argument("--what-worked", default="")
    parser.add_argument("--what-failed", default="")
    parser.add_argument("--user-corrections", default="")
    parser.add_argument("--final-prompt-pattern", default="")
    parser.add_argument("--template-candidate", default="")
    parser.add_argument("--should-promote", choices=["yes", "no", "unsure"], default="unsure")
    args = parser.parse_args()

    output = write_case(build_case_record(args), Path(args.case_dir))
    print(output)


if __name__ == "__main__":
    main()
