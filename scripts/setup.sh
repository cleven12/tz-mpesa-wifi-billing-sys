#!/usr/bin/env bash
# setup.sh — Create venv, install dependencies, copy .env, init DB.
# Usage: bash scripts/setup.sh

set -e

# TODO: check Python version >= 3.8
# TODO: python3 -m venv venv
# TODO: source venv/bin/activate
# TODO: pip install --upgrade pip
# TODO: pip install -r requirements.txt
# TODO: cp .env.example .env if .env missing, warn user to fill in credentials
# TODO: python -c "from database.init_db import init_db; init_db()"
# TODO: python -c "from database.seed_data import seed_all; seed_all()"

echo "Setup complete. Edit .env then run: source venv/bin/activate && python app.py"
