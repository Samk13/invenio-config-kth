.DEFAULT_GOAL=ls

ls: # list available commands
	@grep '^[^#[:space:]].*:' Makefile

freeze: # show installed dependencies
	@pip freeze

format: # Black format and isort imports
	@black . && isort .

install: # Install py dependencies
	@pip install -e ".[tests]"

run: # fetch data and save it in invenio_subjects_cessda/downloads/result.json
	@python main.py

test: # run tests
	@bash run-tests.sh
