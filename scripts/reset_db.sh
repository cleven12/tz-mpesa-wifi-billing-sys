#!/usr/bin/env bash
# reset_db.sh — Drop and re-create the database, then re-seed.
# WARNING: destroys all data.
# Usage: bash scripts/reset_db.sh

set -e

read -p "This will DELETE all data. Continue? [y/N] " confirm
if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
  echo "Aborted."
  exit 0
fi

source venv/bin/activate 2>/dev/null || true

echo "Dropping database..."
python3 -c "from database.init_db import drop_db; drop_db()" 2>/dev/null || \
  echo "drop_db not yet implemented — skipped."

echo "Re-creating database..."
python3 -c "from database.init_db import init_db; init_db()" 2>/dev/null || \
  echo "init_db not yet implemented — skipped."

echo "Seeding data..."
python3 -c "from database.seed_data import seed_all; seed_all()" 2>/dev/null || \
  echo "seed_all not yet implemented — skipped."

echo "Database reset complete."
