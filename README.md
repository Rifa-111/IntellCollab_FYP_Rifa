# IntellCollab
### Explainable project matching for academia–industry collaboration

**Research origin:** undergraduate final-year project exploring machine-learning and NLP-based recommendations for matching academic and industry interests. This repository now also includes a **new 2026, dependency-free, offline demonstrator** of a related recommendation concept. The demonstrator is **not a historical reproduction** of the original final-year system or its evaluated ML model.

[Run the demonstrator](#run-in-under-a-minute) · [Reproducibility](#reproducibility-and-testing) · [Provenance](docs/PROVENANCE_AND_EVIDENCE.md) · [Security](SECURITY.md)

## Why this project matters

Academic researchers and industry teams can struggle to identify projects that match skills, interests and research topics. The original IntellCollab project investigated NLP-driven recommendation techniques to support project discovery. The aim of this public repository is to make its **research motivation** understandable and provide a minimal, independently runnable illustration of text-based matching, while preserving a clear distinction between historical results and subsequent engineering improvements.

## What is actually available here

| Component | Status | Verification |
| --- | --- | --- |
| Research context and project description | Documented | Historical project context; not itself a tested outcome |
| Python text-similarity and skill-overlap demonstrator | Implemented **in this repository in 2026** | Deterministic source, synthetic records and offline tests |
| Synthetic project examples | Included | Explicitly fictional, without user or company records |
| CI and automated regression tests | Configured | GitHub Actions status must be checked for each commit |
| Original Flask and MongoDB backend | **Not included** | Historical source in another repository; unsafe to reuse without remediation |
| Original React interface | **Not included** | Historical front-end source in a separate repository |
| Original datasets, trained model and performance figures | **Not included** | Cannot be reproduced or inferred from this demonstrator |
| Production deployment or independent adoption | **Not demonstrated** | No external usage claims are made |

## How the new demonstrator works

```text
User-supplied skills + interests                 Synthetic project catalogue
                 |                                          |
                 +----------------+-------------------------+
                                  |
                  Normalise text and tokenise
                                  |
           Fit TF-IDF on query and project descriptions
                                  |
                    Cosine text similarity
                                  |
          Exact case-insensitive skill-overlap score
                                  |
         Score = 0.80 × similarity + 0.20 × overlap
                                  |
          Deterministic ranked results and score components
```

The weights are an **illustrative design choice in the new reference code**, not a recovered parameter from the undergraduate model. Scores are similarity rankings, not measured success rates or probabilities of a successful collaboration.

### Run in under a minute

Requires Python **3.10 or later**. The example does not need API credentials, MongoDB, Flask, React, network connectivity or third-party Python packages.

```bash
git clone https://github.com/Rifa-111/IntellCollab_FYP_Rifa.git
cd IntellCollab_FYP_Rifa
python -m intellcollab
```

The output is a JSON array containing up to three recommended **fictional** projects and their ranking components. During PR review, use the branch `improve/reproducible-safe-demonstrator-2026`, or wait until the branch has been merged before running these commands against `main`.

### Reproducibility and testing

```bash
python -m unittest discover -s tests -v
python -m compileall -q intellcollab tests
```

Tests cover tokenisation, score bounds, empty queries, deterministic ordering, input immutability, duplicate project identifiers and invalid input handling. The [CI workflow](.github/workflows/ci.yml) is configured for Python 3.10, 3.11 and 3.12. It does not test the original FYP or prove deployment readiness.

## Project structure

```text
intellcollab/
  recommender.py             # New 2026 reference scoring implementation
  __main__.py                # Offline demo command
examples/
  synthetic_projects.json    # Fictional project records only
tests/
  test_recommender.py        # Offline unit/regression tests
docs/
  PROVENANCE_AND_EVIDENCE.md # Historical vs later-work distinctions
.github/workflows/
  ci.yml                     # Automated offline checks
SECURITY.md                  # Data and credentials warning
CONTRIBUTING.md              # Review and contribution guidelines
```

## Historical source and research integrity

The full-stack coursework appears across separate repositories:

- [Historical React UI](https://github.com/Rifa-111/IntellCollab)
- [Historical Python/Flask prototype](https://github.com/Rifa-111/IntellCollab-Final)

**Security warning:** the historical backend contains embedded MongoDB credentials and unsafe password handling. Revoke any live exposed credentials and audit the old repository before using, deploying or sharing it as finished software. The reference demonstrator does not incorporate that backend or its data. See [SECURITY.md](SECURITY.md).

The repository's 2026 commits must not be passed off as work undertaken in the original final-year project. Research evaluation results should only be quoted if independently traceable to the original dissertation, dataset and scripts. No benchmark figures, uptake statistics or external awards have been inferred.


## Responsible reuse and future work

Potential next steps include integrating a safe reconstructed web interface, obtaining permission to publish appropriately anonymised evaluation data, evaluating rankings against a documented ground-truth benchmark and inviting independent review. These are **future tasks**, not delivered capabilities.

A top-level open-source licence has **not yet been selected**. The repository owner should choose one before making reuse or redistribution claims. Contributions should follow [CONTRIBUTING.md](CONTRIBUTING.md).
