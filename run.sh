#!/usr/bin/env bash
set -euo pipefail

HOST="${HOST:-0.0.0.0}"
PORT="${PORT:-8000}"
PACKAGE_MANAGER="poetry"

usage() {
    cat <<'EOF'
Usage: run.sh [options]

Options:
  -pm, --package-manager <poetry|pip>  Package manager to use (default: poetry)
  -h,  --help                          Show this help message
EOF
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -pm|--package-manager)
            PACKAGE_MANAGER="${2:-}"
            shift 2
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "Unknown option: $1" >&2
            usage >&2
            exit 1
            ;;
    esac
done

case "$PACKAGE_MANAGER" in
    poetry)
        poetry install
        poetry run uvicorn app.main:app --host "$HOST" --port "$PORT" --reload
        ;;
    pip)
        pip install -r requirements.txt
        uvicorn app.main:app --host "$HOST" --port "$PORT" --reload
        ;;
    *)
        echo "Invalid package manager: $PACKAGE_MANAGER (expected 'poetry' or 'pip')" >&2
        exit 1
        ;;
esac
