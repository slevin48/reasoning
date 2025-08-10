# How to work on this repo

## Setup
- Use Python 3.11+
- Install with: pip install -r requirements.txt
- Key deps: streamlit, pytest, ruff

## Build & test
- Lint: ruff check .
- Unit tests: pytest -q
- Smoke check: python -m streamlit hello || true

## Conventions
- Follow Black/PEP8 style; run ruff --fix where safe
- All new code needs a small test

## Done criteria
- All checks pass; create a PR with a summary of changes
