#!/usr/bin/env bash
set -euo pipefail

PORT="${1:-5173}"

echo "Serving on http://localhost:${PORT}"
python3 -m http.server "$PORT"
