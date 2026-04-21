#!/usr/bin/env bash
# reset_db.sh — Drop and re-create the database, then re-seed.
# WARNING: destroys all data.
# Usage: bash scripts/reset_db.sh

set -e

# TODO: read -p "This will DELETE all data. Continue? [y/N] " confirm
# TODO: if [[ "$confirm" != "y" ]]; then echo "Aborted."; exit 0; fi
# TODO: source venv/bin/activate
# TODO: python -c "from database.init_db import drop_db; drop_db()"
# TODO: python -c "from database.init_db import init_db; init_db()"
# TODO: python -c "from database.seed_data import seed_all; seed_all()"

echo "Database reset complete."
