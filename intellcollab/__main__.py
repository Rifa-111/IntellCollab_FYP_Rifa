"""Run the offline synthetic-data recommender demonstration."""
import json
from pathlib import Path

from .recommender import recommend


def main() -> None:
    fixture = Path(__file__).resolve().parents[1] / "examples" / "synthetic_projects.json"
    projects = json.loads(fixture.read_text(encoding="utf-8"))
    results = recommend(
        user_skills=["Python", "machine learning"],
        user_interests=["healthcare", "clinical research"],
        projects=projects,
        top_k=3,
    )
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
