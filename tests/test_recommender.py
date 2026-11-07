"""Offline regression tests: synthetic inputs, no customer records or API keys."""
import json
from pathlib import Path
import unittest

from intellcollab.recommender import recommend, tfidf_cosine_similarity, tokenise


class RecommenderTests(unittest.TestCase):
    def setUp(self):
        fixture = Path(__file__).resolve().parents[1] / "examples" / "synthetic_projects.json"
        self.projects = json.loads(fixture.read_text(encoding="utf-8"))

    def test_tokenisation_is_case_insensitive(self):
        self.assertEqual(tokenise("Python, NLP!"), ["python", "nlp"])

    def test_cosine_similarity_is_bounded(self):
        scores = tfidf_cosine_similarity("python clinical", ["python clinical", "finance"])
        self.assertEqual(len(scores), 2)
        self.assertTrue(all(0 <= score <= 1 for score in scores))
        self.assertGreater(scores[0], scores[1])

    def test_empty_query_returns_zero_scores(self):
        self.assertEqual(tfidf_cosine_similarity("", ["one", "two"]), [0, 0])

    def test_recommendations_are_deterministic_and_ranked(self):
        args = (["Python", "machine learning"], ["clinical"], self.projects)
        first = recommend(*args, top_k=3)
        self.assertEqual(first, recommend(*args, top_k=3))
        self.assertEqual(len(first), 3)
        self.assertEqual([r["score"] for r in first], sorted([r["score"] for r in first], reverse=True))
        self.assertEqual(first[0]["id"], "demo-001")

    def test_explanatory_scores_and_no_mutation(self):
        projects_before = json.dumps(self.projects, sort_keys=True)
        scores = recommend(["Python"], ["healthcare"], self.projects, top_k=2)
        self.assertTrue(all({"score", "text_similarity", "skill_overlap"} <= set(r) for r in scores))
        self.assertEqual(json.dumps(self.projects, sort_keys=True), projects_before)

    def test_no_projects(self):
        self.assertEqual(recommend(["Python"], ["NLP"], []), [])

    def test_duplicate_ids_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate project id"):
            recommend(["Python"], [], [self.projects[0], self.projects[0]])

    def test_invalid_top_k(self):
        for value in (0, -1, True, "3"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                recommend(["Python"], [], self.projects, top_k=value)

    def test_bad_skill_shape_rejected(self):
        with self.assertRaises(TypeError):
            recommend("Python", ["NLP"], self.projects)

    def test_metadata_validation(self):
        with self.assertRaises(ValueError):
            recommend(["Python"], [], [{"id": "x", "title": "Example", "description": "", "skills": "Python"}])


if __name__ == "__main__":
    unittest.main()
