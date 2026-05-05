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
