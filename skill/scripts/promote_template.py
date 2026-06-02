#!/usr/bin/env python3
import argparse
import shutil
from pathlib import Path

import new_template_card


SKILL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CANDIDATE_DIR = SKILL_ROOT / "references" / "candidate-templates"
DEFAULT_TEMPLATE_DIR = SKILL_ROOT / "references" / "templates"
DEFAULT_INDEX = SKILL_ROOT / "references" / "template-index.md"


def validate_card(text: str) -> None:
    missing = [field for field in new_template_card.REQUIRED_FIELDS if f"## {field}" not in text]
    if missing:
        raise SystemExit("Candidate template is missing fields: " + ", ".join(missing))


def ensure_index_entry(index_path: Path, template_id: str, description: str) -> None:
    index = index_path.read_text(encoding="utf-8")
    if f"`{template_id}`" in index:
        return
    section = "## Candidate Promoted Templates"
    entry = f"- `{template_id}`: {description}\n"
    if section not in index:
        index = index.rstrip() + f"\n\n{section}\n\n" + entry
    else:
        index = index.rstrip() + "\n" + entry
    index_path.write_text(index, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Promote a candidate template into stable templates after explicit approval.")
    parser.add_argument("--candidate", required=True, help="Candidate markdown path or candidate id.")
    parser.add_argument("--description", default="newly promoted reusable design-analysis template.")
    parser.add_argument("--confirm", required=True, help="Must be PROMOTE.")
    parser.add_argument("--remove-candidate", action="store_true", help="Remove candidate file after successful copy.")
    args = parser.parse_args()

    if args.confirm != "PROMOTE":
        raise SystemExit("Refusing to promote without --confirm PROMOTE")

    candidate_path = Path(args.candidate)
    if not candidate_path.exists():
        candidate_path = DEFAULT_CANDIDATE_DIR / f"{args.candidate}.md"
    if not candidate_path.exists():
        raise SystemExit(f"Candidate not found: {args.candidate}")

    template_id = candidate_path.stem
    text = candidate_path.read_text(encoding="utf-8")
    validate_card(text)

    DEFAULT_TEMPLATE_DIR.mkdir(parents=True, exist_ok=True)
    output = DEFAULT_TEMPLATE_DIR / f"{template_id}.md"
    if output.exists():
        raise SystemExit(f"Stable template already exists: {output}")

    shutil.copy2(candidate_path, output)
    ensure_index_entry(DEFAULT_INDEX, template_id, args.description)
    if args.remove_candidate:
        candidate_path.unlink()
    print(output)


if __name__ == "__main__":
    main()
