"""Transparent, dependency-free text-similarity demonstration for IntellCollab.

This module is a new reference implementation of a recommendation concept.
It does NOT reconstruct or claim to reproduce the original FYP model, data,
evaluation metrics, or historical deployment.
"""
from __future__ import annotations

from collections import Counter
from math import log, sqrt
import re
from typing import Any, Mapping, Sequence


def tokenise(value: str) -> list[str]:
    """Case-fold text into reproducible ASCII word tokens."""
    if not isinstance(value, str):
        raise TypeError("Expected a string")
    return re.findall(r"[a-z0-9]+", value.casefold())


def _tfidf_vectors(documents: Sequence[str]) -> list[dict[str, float]]:
    tokens = [tokenise(doc) for doc in documents]
    n_documents = len(tokens)
    if not n_documents:
        return []
    document_frequency = Counter(token for doc in tokens for token in set(doc))
    vectors = []
    for words in tokens:
        counts = Counter(words)
        vector = {
            word: count * (log((1 + n_documents) / (1 + document_frequency[word])) + 1)
            for word, count in counts.items()
        }
        length = sqrt(sum(v * v for v in vector.values()))
        vectors.append({word: val / length for word, val in vector.items()} if length else {})
    return vectors


def tfidf_cosine_similarity(query: str, candidates: Sequence[str]) -> list[float]:
    """Fit TF-IDF on query and candidates and return bounded cosine scores."""
    if not isinstance(query, str):
        raise TypeError("query must be text")
    if any(not isinstance(x, str) for x in candidates):
        raise TypeError("candidate descriptions must be text")
    if not candidates:
        return []
    vectors = _tfidf_vectors([query, *candidates])
    query_vector = vectors[0]
    return [
        min(1.0, max(0.0, sum(weight * candidate.get(token, 0.0) for token, weight in query_vector.items())))
        for candidate in vectors[1:]
    ]


def recommend(
    user_skills: Sequence[str],
    user_interests: Sequence[str],
    projects: Sequence[Mapping[str, Any]],
    top_k: int = 5,
) -> list[dict[str, Any]]:
    """Rank projects by combined TF-IDF and exact skill overlap.

    Projects must contain unique string ids, string titles and descriptions,
    and a list of skill strings. Input is not mutated. Output includes a score
    and two interpretable components, but scores are NOT calibrated probabilities.
    """
    if not isinstance(top_k, int) or isinstance(top_k, bool) or top_k < 1:
        raise ValueError("top_k must be a positive integer")
    if isinstance(user_skills, (str, bytes)) or isinstance(user_interests, (str, bytes)):
        raise TypeError("skills and interests must be sequences of strings")
    if not all(isinstance(s, str) for s in [*user_skills, *user_interests]):
        raise TypeError("skills and interests must contain strings")
    if not projects:
        return []

    validated = []
    seen_ids: set[str] = set()
    for project in projects:
        if not isinstance(project, Mapping):
            raise TypeError("each project must be a mapping")
        project_id = project.get("id")
        title = project.get("title")
        description = project.get("description")
        skills = project.get("skills")
        if not all(isinstance(x, str) and x.strip() for x in (project_id, title)):
            raise ValueError("each project needs a non-empty string id and title")
        if not isinstance(description, str):
            raise ValueError("project description must be text")
        if isinstance(skills, (str, bytes)) or not isinstance(skills, (list, tuple)):
            raise ValueError("project skills must be a list or tuple of strings")
        if not all(isinstance(s, str) for s in skills):
            raise ValueError("project skills must contain strings")
        if project_id in seen_ids:
            raise ValueError(f"duplicate project id: {project_id}")
        seen_ids.add(project_id)
        validated.append(project)

    skills_lower = {skill.strip().casefold() for skill in user_skills if skill.strip()}
    query_text = " ".join([*user_skills, *user_interests])
    candidate_texts = [
        " ".join([p["title"], p["description"], *p["skills"]]) for p in validated
    ]
    similarities = tfidf_cosine_similarity(query_text, candidate_texts)
    results: list[dict[str, Any]] = []
    for project, similarity in zip(validated, similarities):
        project_skills = {s.strip().casefold() for s in project["skills"] if s.strip()}
        overlap = len(skills_lower & project_skills) / len(skills_lower) if skills_lower else 0.0
        score = 0.8 * similarity + 0.2 * overlap
        results.append({
            "id": project["id"],
            "title": project["title"],
            "score": round(score, 6),
            "text_similarity": round(similarity, 6),
            "skill_overlap": round(overlap, 6),
        })
    # Tie-break on project id to guarantee deterministic rankings.
    results.sort(key=lambda item: (-item["score"], item["id"]))
    return results[:top_k]
