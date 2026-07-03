"""PSR sandbox application package."""

from importlib.metadata import PackageNotFoundError, version

# Fallback version constant. python-semantic-release bumps this value
# (see ``version_variables`` in pyproject.toml) so the app can report a
# version even when installed package metadata is not available.
__version__ = "0.3.0"

try:
    __version__ = version("psr-sandbox")
except PackageNotFoundError:  # pragma: no cover - not installed as a package
    pass
