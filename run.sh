#!/usr/bin/env bash
# Ubuntu From Zero — launch the Tkinter lesson browser
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"
if ! command -v python3 >/dev/null; then
  echo "python3 is required" >&2
  exit 1
fi
exec python3 "$DIR/app.py"
