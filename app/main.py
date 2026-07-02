"""FastAPI application for the python-semantic-release sandbox."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app import __version__

STATIC_DIR = Path(__file__).parent / "static"

app = FastAPI(
    title="PSR Sandbox API",
    description="Tiny FastAPI service to test python-semantic-release.",
    version=__version__,
)


@app.get("/api/version")
def get_version() -> dict[str, str]:
    """Return the current application version."""
    return {"version": __version__}


@app.get("/api/hello")
def hello(name: str = "world") -> dict[str, str]:
    """Return a friendly greeting."""
    return {"message": f"Hello, {name}!"}


# Serve the tiny frontend from the static directory.
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def index() -> FileResponse:
    """Serve the frontend entry point."""
    return FileResponse(STATIC_DIR / "index.html")
