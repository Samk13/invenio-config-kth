.DEFAULT_GOAL=ls

ls: # list available commands
	@grep '^[^#[:space:]].*:' Makefile

freeze: # show installed dependencies
	@pip freeze

format: # format the code using black
	@black .

sort: # format imports using isort
	@isort .

install: # Install py dependencies
	@pip install -e ".[tests]"

run: # fetch data and save it in invenio_subjects_cessda/downloads/result.json
	@python main.py

test: # run tests
	@bash run-tests.sh
