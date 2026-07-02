# PSR Sandbox

A tiny **FastAPI** API plus a minimal static frontend used to experiment with
[**python-semantic-release**](https://python-semantic-release.readthedocs.io/)
(PSR). It is configured to work with **both Poetry and pip**.

## Project layout

```
.
├── app/
│   ├── __init__.py          # exposes __version__ (bumped by PSR)
│   ├── main.py              # FastAPI app + endpoints
│   └── static/index.html    # tiny frontend
├── tests/test_main.py
├── .github/workflows/release.yml
├── pyproject.toml           # Poetry metadata + PSR config
├── requirements.txt         # runtime deps for pip
└── requirements-dev.txt     # dev deps for pip
```

## Setup

### Option A — Poetry

```bash
poetry install
poetry run uvicorn app.main:app --reload
poetry run pytest
```

### Option B — pip

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
pip install -e .            # installs the package so importlib metadata works
uvicorn app.main:app --reload
pytest
```

Open http://127.0.0.1:8000 for the frontend, or hit the API directly:

- `GET /api/version` → current app version
- `GET /api/hello?name=Ada` → greeting

## How versioning works

The version lives in **two** places kept in sync by PSR:

1. `pyproject.toml` → `[tool.poetry] version` (via `version_toml`)
2. `app/__init__.py` → `__version__` fallback constant (via `version_variables`)

At runtime the app reads the installed package version through
`importlib.metadata`, falling back to `__version__` when it is not installed
as a package.

## Conventional Commits

PSR decides the next version from commit messages:

| Commit prefix        | Release |
| -------------------- | ------- |
| `fix:` / `perf:`     | patch   |
| `feat:`              | minor   |
| `feat!:` / `BREAKING CHANGE:` footer | major |
| `docs:` `chore:` etc | none    |

Examples:

```
feat: add /api/hello endpoint
fix: correct version reporting
feat!: change response schema

BREAKING CHANGE: /api/hello now returns a list
```

## Try a release locally (dry run)

```bash
# Poetry
poetry run semantic-release version --print

# pip
semantic-release version --print
```

Add `--no-push --no-vcs-release` to simulate without touching the remote, or
run `semantic-release version` on a clean `main` branch to actually bump the
version, update the changelog, commit and tag.

## CI

`.github/workflows/release.yml` runs PSR on pushes to `main`/`master`. It needs
the default `GITHUB_TOKEN` (already granted `contents: write` in the workflow)
to create the release commit, tag and GitHub Release.
