#!/usr/bin/env bash
# setup.sh — First-time project setup.
# Usage: bash scripts/setup.sh

set -e

echo "=== WiFi Billing System Setup ==="

# 1. Python virtual environment
if [ ! -d "venv" ]; then
  echo "[1/5] Creating virtual environment..."
  python3 -m venv venv
else
  echo "[1/5] Virtual environment already exists."
fi

# 2. Install dependencies
echo "[2/5] Installing Python dependencies..."
source venv/bin/activate
pip install --upgrade pip -q
pip install -r requirements.txt -q

# 3. Environment file
if [ ! -f ".env" ]; then
  echo "[3/5] Copying .env.example → .env"
  cp .env.example .env
  echo "      ⚠  Edit .env with your credentials before running the app."
else
  echo "[3/5] .env already exists."
fi

# 4. Initialize database
echo "[4/5] Initializing database..."
python3 -c "from database.init_db import init_db; init_db()" 2>/dev/null || \
  echo "      ⚠  init_db not yet implemented — skipped."

# 5. Seed data
echo "[5/5] Seeding sample data..."
python3 -c "from database.seed_data import seed_all; seed_all()" 2>/dev/null || \
  echo "      ⚠  seed_all not yet implemented — skipped."

echo ""
echo "Setup complete! Run: source venv/bin/activate && python3 app.py"
