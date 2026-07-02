"""Tests for the FastAPI sandbox app."""

from fastapi.testclient import TestClient

from app import __version__
from app.main import app

client = TestClient(app)


def test_version_endpoint():
    res = client.get("/api/version")
    assert res.status_code == 200
    assert res.json() == {"version": __version__}


def test_hello_default():
    res = client.get("/api/hello")
    assert res.status_code == 200
    assert res.json() == {"message": "Hello, world!"}


def test_hello_named():
    res = client.get("/api/hello", params={"name": "Ada"})
    assert res.status_code == 200
    assert res.json() == {"message": "Hello, Ada!"}


def test_index_served():
    res = client.get("/")
    assert res.status_code == 200
    assert "PSR Sandbox" in res.text
