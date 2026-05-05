.PHONY: install venv

venv:
	python3 -m venv venv

install: venv
	. venv/bin/activate && pip install -r requirements.txt

.PHONY: run run-debug

run:
	. venv/bin/activate && python3 app.py

run-debug:
	. venv/bin/activate && FLASK_DEBUG=1 python3 app.py

.PHONY: test lint

test:
	. venv/bin/activate && pytest tests/ -v --tb=short

lint:
	. venv/bin/activate && python3 -m py_compile app.py wsgi.py

.PHONY: db-init db-seed db-reset

db-init:
	. venv/bin/activate && python3 -c "from database.init_db import init_db; init_db()"

db-seed:
	. venv/bin/activate && python3 -c "from database.seed_data import seed_all; seed_all()"

db-reset:
	bash scripts/reset_db.sh

.PHONY: docker-up docker-down clean

docker-up:
	docker compose -f docker/docker-compose.yml up --build -d

docker-down:
	docker compose -f docker/docker-compose.yml down

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null; true
	find . -name "*.pyc" -delete 2>/dev/null; true
