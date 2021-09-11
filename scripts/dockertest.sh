#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

cd "$(dirname "$0")/.."
docker build -t freeplane_tools_test -f docker/Dockerfile .
docker run -it --rm freeplane_tools_test ./scripts/test.py
