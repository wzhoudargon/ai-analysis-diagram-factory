#!/usr/bin/env python3
import argparse
from typing import Dict, Mapping, Optional

CATEGORIES = {
    "geometry": ("Geometry / factual fidelity", 30),
    "style": ("Style stability", 20),
    "layout": ("Layout and information hierarchy", 15),
    "text": ("Text and label hygiene", 15),
    "role": ("Image role separation", 10),
    "finish": ("Professional finish", 10),
}

VETO_PATTERNS = {
    "geometry": ["moved", "distorted", "changed shoreline", "wrong road", "wrong plan", "relocated"],
    "text": ["gibberish", "unreadable", "乱码", "wrong language"],
    "role": ["watermark", "logo", "copied reference", "copied text"],
    "layout": ["wrong output type", "became illustration", "not a board", "not a diagram"],
}


def _clamp_score(value: int, maximum: int) -> int:
    return max(0, min(maximum, int(value)))


def detect_vetoes(failure_description: str) -> list[str]:
    lower = failure_description.lower()
    vetoes = []
    for category, patterns in VETO_PATTERNS.items():
        if any(pattern.lower() in lower for pattern in patterns):
            vetoes.append(category)
    return vetoes


def default_scores(failure_description: str) -> Dict[str, int]:
    scores = {key: maximum for key, (_, maximum) in CATEGORIES.items()}
    for veto in detect_vetoes(failure_description):
        scores[veto] = min(scores[veto], CATEGORIES[veto][1] // 3)
    return scores


def build_report(
    template_id: str,
    task_goal: str,
    failure_description: str,
    scores: Optional[Mapping[str, int]] = None,
) -> str:
    raw_scores = dict(scores or default_scores(failure_description))
    normalized = {
        key: _clamp_score(raw_scores.get(key, maximum), maximum)
        for key, (_, maximum) in CATEGORIES.items()
    }
    total = sum(normalized.values())
    vetoes = detect_vetoes(failure_description)

    lines = [
        f"# Case Score: {template_id}",
        "",
        f"Task Goal: {task_goal}",
        "",
        f"Failure Description: {failure_description}",
        "",
        "## Scores",
    ]
    for key, (label, maximum) in CATEGORIES.items():
        lines.append(f"- {label}: {normalized[key]}/{maximum}")
    lines.extend(["", f"Total Score: {total}/100", ""])

    if vetoes:
        lines.extend(["## Veto Flags", *[f"- {item}" for item in vetoes], ""])

    lines.extend(
        [
            "## Candidate Template Revision",
            "Do not merge automatically. Review and apply only after user approval.",
            "",
            "- Tighten geometry lock language for the failed elements named above.",
            "- Move repeated failure wording into `failure_modes`.",
            "- If the same issue appears in three or more cases, promote the fix into `prompt_template`.",
            "- If the issue crosses multiple templates, update `references/universal-rules.md` instead of this single card.",
        ]
    )
    return "\n".join(lines) + "\n"


def parse_score(raw: str) -> tuple[str, int]:
    if "=" not in raw:
        raise argparse.ArgumentTypeError("Scores must use key=value.")
    key, value = raw.split("=", 1)
    key = key.strip()
    if key not in CATEGORIES:
        raise argparse.ArgumentTypeError(f"Unknown score category: {key}")
    return key, int(value)


def main() -> None:
    parser = argparse.ArgumentParser(description="Score an image-generation case and draft candidate revisions.")
    parser.add_argument("--template-id", required=True)
    parser.add_argument("--task-goal", required=True)
    parser.add_argument("--failure-description", required=True)
    parser.add_argument("--score", action="append", default=[], type=parse_score, help="Optional key=value score override.")
    args = parser.parse_args()

    scores = dict(args.score) if args.score else None
    print(build_report(args.template_id, args.task_goal, args.failure_description, scores), end="")


if __name__ == "__main__":
    main()
