#!/usr/bin/env python3
import tempfile
import unittest
from pathlib import Path

import capture_case
import extract_template_candidate
import new_template_card
import promote_template
import score_case


SKILL_ROOT = Path(__file__).resolve().parents[1]


class TemplateCardTests(unittest.TestCase):
    def test_render_card_contains_required_sections(self):
        card = new_template_card.render_card("test-template", "Use for test tasks.")
        for heading in new_template_card.REQUIRED_FIELDS:
            self.assertIn(f"## {heading}", card)
        self.assertIn("# test-template", card)
        self.assertIn("Use for test tasks.", card)

    def test_architecture_exploded_template_is_indexed_and_self_styled(self):
        template_id = "architecture-exploded-axonometric-diagram"
        index = (SKILL_ROOT / "references" / "template-index.md").read_text(encoding="utf-8")
        self.assertIn(f"`{template_id}`", index)

        card_path = SKILL_ROOT / "references" / "templates" / f"{template_id}.md"
        self.assertTrue(card_path.exists())
        card = card_path.read_text(encoding="utf-8")
        for heading in new_template_card.REQUIRED_FIELDS:
            self.assertIn(f"## {heading}", card)
        self.assertIn("no style reference", card.lower())
        self.assertIn("built-in style", card.lower())
        self.assertIn("most recent", card.lower())
        self.assertIn("ignore all earlier", card.lower())


class ScoreCaseTests(unittest.TestCase):
    def test_score_report_includes_scores_and_candidate_revision_without_writing_template(self):
        with tempfile.TemporaryDirectory() as tmp:
            template = Path(tmp) / "template.md"
            template.write_text("stable template", encoding="utf-8")

            report = score_case.build_report(
                template_id="satellite-to-site-analysis",
                task_goal="Create a dark satellite site analysis diagram.",
                failure_description="The output moved the shoreline and generated unreadable Chinese labels.",
                scores={
                    "geometry": 12,
                    "style": 16,
                    "layout": 12,
                    "text": 4,
                    "role": 8,
                    "finish": 8,
                },
            )

            self.assertIn("satellite-to-site-analysis", report)
            self.assertIn("Total Score: 60/100", report)
            self.assertIn("Candidate Template Revision", report)
            self.assertIn("geometry", report.lower())
            self.assertEqual("stable template", template.read_text(encoding="utf-8"))


class CaseCaptureTests(unittest.TestCase):
    def test_capture_extract_and_promote_candidate_template(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            case_dir = root / "cases"
            candidate_dir = root / "candidate-templates"
            template_dir = root / "templates"
            index_path = root / "template-index.md"
            index_path.write_text("# Template Index\n", encoding="utf-8")

            args = type(
                "Args",
                (),
                {
                    "case_id": "case-001",
                    "task_type": "heritage product board",
                    "input_roles": "reference is style only; theme text is content",
                    "reference_style_summary": "aged paper, calligraphy title, product-system modules",
                    "project_goal": "turn a new cultural theme into a product visual-system board",
                    "prompt_used_summary": "sanitized prompt summary",
                    "what_worked": "separate main poster, brochure, packaging, swatches, and motifs",
                    "what_failed": "may copy reference text",
                    "user_corrections": "replace theme content only",
                    "final_prompt_pattern": "use evidence for content and reference for layout",
                    "template_candidate": "heritage-cultural-product-board",
                    "should_promote": "yes",
                },
            )()
            record = capture_case.build_case_record(args)
            output = capture_case.write_case(record, case_dir)
            self.assertTrue(output.exists())

            cases = extract_template_candidate.matching_cases(case_dir, "heritage-cultural-product-board")
            self.assertEqual(1, len(cases))
            candidate = extract_template_candidate.render_candidate("heritage-cultural-product-board", cases)
            for heading in new_template_card.REQUIRED_FIELDS:
                self.assertIn(f"## {heading}", candidate)
            candidate_path = candidate_dir / "heritage-cultural-product-board.md"
            candidate_dir.mkdir(parents=True)
            candidate_path.write_text(candidate, encoding="utf-8")

            original_candidate_root = promote_template.DEFAULT_CANDIDATE_DIR
            original_template_root = promote_template.DEFAULT_TEMPLATE_DIR
            original_index = promote_template.DEFAULT_INDEX
            try:
                promote_template.DEFAULT_CANDIDATE_DIR = candidate_dir
                promote_template.DEFAULT_TEMPLATE_DIR = template_dir
                promote_template.DEFAULT_INDEX = index_path
                promote_template.validate_card(candidate)
                promote_template.ensure_index_entry(
                    index_path,
                    "heritage-cultural-product-board",
                    "heritage and cultural product boards.",
                )
                promoted = template_dir / "heritage-cultural-product-board.md"
                template_dir.mkdir(parents=True)
                promoted.write_text(candidate, encoding="utf-8")

                self.assertTrue(promoted.exists())
                self.assertIn("`heritage-cultural-product-board`", index_path.read_text(encoding="utf-8"))
            finally:
                promote_template.DEFAULT_CANDIDATE_DIR = original_candidate_root
                promote_template.DEFAULT_TEMPLATE_DIR = original_template_root
                promote_template.DEFAULT_INDEX = original_index


if __name__ == "__main__":
    unittest.main()
