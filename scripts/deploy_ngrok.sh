#!/usr/bin/env bash
# deploy_ngrok.sh — Start Flask + ngrok tunnel in parallel.
# Usage: bash scripts/deploy_ngrok.sh

set -e

if ! command -v ngrok &>/dev/null; then
  echo "ngrok not found. Install: https://ngrok.com/download"
  exit 1
fi

if [ ! -f .env ]; then
  echo ".env file missing. Run: cp .env.example .env"
  exit 1
fi

source venv/bin/activate 2>/dev/null || true
mkdir -p logs

echo "Starting Flask..."
python3 app.py > logs/flask.log 2>&1 &
FLASK_PID=$!

sleep 2

if ! kill -0 "$FLASK_PID" 2>/dev/null; then
  echo "Flask failed to start. Check logs/flask.log"
  exit 1
fi

echo "Flask running (PID $FLASK_PID). Starting ngrok tunnel..."
ngrok http 5000 --region=eu &
NGROK_PID=$!

sleep 2

NGROK_URL=$(curl -s http://localhost:4040/api/tunnels 2>/dev/null \
  | python3 -c "import sys,json; d=json.load(sys.stdin); \
    print(d['tunnels'][0]['public_url'])" 2>/dev/null || true)

if [ -n "$NGROK_URL" ]; then
  echo ""
  echo "Public URL : $NGROK_URL"
  echo "IPN URL    : $NGROK_URL/webhook/pesapal"
  echo "Callback   : $NGROK_URL/webhook/pesapal/callback"
  echo ""
  echo "Add these to your .env:"
  echo "  PESAPAL_IPN_URL=$NGROK_URL/webhook/pesapal"
  echo "  PESAPAL_CALLBACK_URL=$NGROK_URL/webhook/pesapal/callback"
fi

trap "kill $FLASK_PID $NGROK_PID 2>/dev/null" EXIT
wait
