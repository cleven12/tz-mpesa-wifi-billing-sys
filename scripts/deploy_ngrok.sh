#!/usr/bin/env bash
# deploy_ngrok.sh — Start Flask + ngrok tunnel in parallel.
# Usage: bash scripts/deploy_ngrok.sh

set -e

# TODO: check ngrok is installed, print install hint if missing
# TODO: check .env exists
# TODO: source venv/bin/activate
# TODO: mkdir -p logs
# TODO: start Flask in background: python app.py > logs/flask.log 2>&1 &
# TODO: FLASK_PID=$!
# TODO: sleep 2 to let Flask bind to port
# TODO: ngrok http 5000 --region sa

trap "kill \$FLASK_PID 2>/dev/null" EXIT
