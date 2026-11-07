# Project provenance and evidence boundaries

## What exists in this repository

The original README described an undergraduate **IntellCollab** project for academia-industry matching. At audit time, this repository contained **only a README**, not its original Flask API, React application, database configuration or trained recommendation artefacts.

The files introduced under `intellcollab/`, `tests/` and `examples/` are a **new, self-contained, safe reference demonstration** based on the concept of transparent NLP similarity and skill matching. They are **not** a recovered historical model or a claim that the original thesis used precisely the same scoring, coefficients or dataset.

## Historical repositories

Related, separately hosted historical code exists at:

- [IntellCollab — React coursework interface](https://github.com/Rifa-111/IntellCollab)
- [IntellCollab-Final — historical Python/Flask coursework](https://github.com/Rifa-111/IntellCollab-Final)

**Do not deploy the historical backend**: its source includes embedded database credentials and insecure password handling. Its checked-in virtual environment and potential datasets also require review. Rotate any real exposed credentials before sharing or reusing it. No credentials or datasets have been copied into this demonstrator.

## Verification standards for external claims

| Claim | What would substantiate it |
| --- | --- |
| Technical implementation | Public source history, code review, reproducible commands and passing CI |
| Original project evaluation | Versioned dissertation, exact dataset splits, scripts, metrics and independent corroboration |
| Research publication | DOI, publication status, journal/conference link and accurate author contribution |
| Adoption or impact | Independent deployments, usage statistics, third-party reports or verified users |
| External recognition | Independent invitation, reference letter, prize or verified third-party evaluation |

The CI tests demonstrate **new reference-code correctness on synthetic examples**. They do not validate the original FYP's reported accuracy, user uptake or real-world business outcomes. A new commit in 2026 must not be presented as work that existed in the 2024 project.

For a UK Global Talent evidence dossier, cite original dated material and clearly label later engineering, maintenance and open-source improvements. Do not imply that a public GitHub repository by itself proves independent recognition.
