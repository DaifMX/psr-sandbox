# CHANGELOG


## v0.3.0 (2026-07-03)

### Features

- Dark mode toggle
  ([`3a3f6df`](https://github.com/DaifMX/psr-sandbox/commit/3a3f6df7f537c552d07b0a6a4b4d10f7b245d58b))


## v0.2.0 (2026-07-02)

### Features

- **api**: Enrich hello greeting and polish frontend UI
  ([`081d1de`](https://github.com/DaifMX/psr-sandbox/commit/081d1de682ad8fd95fe0d02a56181e391f670d8e))

Return a personalized, title-cased greeting with a welcome message and the resolved name. Redesign
  the frontend as a centered card with a gradient background, styled inputs/buttons, and
  Enter-to-greet support.


## v0.1.0 (2026-07-02)

### Chores

- Add run script
  ([`ae1764c`](https://github.com/DaifMX/psr-sandbox/commit/ae1764c11548bf71aa3912c231c9e6474b38d348))

### Continuous Integration

- **release**: Authenticate semantic-release git push
  ([`abd7a8c`](https://github.com/DaifMX/psr-sandbox/commit/abd7a8c1ed0f93a19497ae61bcc7250e277b2e2f))

Persist checkout credentials so python-semantic-release can push the release commit and tag, fixing
  the "could not read Username" failure.

- **release**: Run semantic-release via pip instead of marketplace action
  ([`df415f2`](https://github.com/DaifMX/psr-sandbox/commit/df415f27ac608d782b5dd45db4799f509d242f71))

The python-semantic-release action is blocked by the org's allowed-actions policy. Install the CLI
  with pip and invoke `semantic-release version` and `publish` directly, setting a Git identity and
  GH_TOKEN for the run.

### Features

- Scaffold FastAPI PSR sandbox
  ([`f8e0538`](https://github.com/DaifMX/psr-sandbox/commit/f8e0538221c09f6c70139bc76f09e632d1788d04))
