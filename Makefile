.DEFAULT_GOAL=ls

ls: # list available commands
	@grep '^[^#[:space:]].*:' Makefile

freeze: # show installed dependencies
	@pip freeze

format: # Black format and isort imports
	@black . && isort .

install: # Install py dependencies
	@pip install -e ".[tests]"

install-pipenv: # Install py dependencies using pipenv
	@pipenv install -e ".[tests]"

run: # fetch data, convert it to yaml, and then save it in invenio_subjects_cessda/vocabularies/cessda_voc.yaml
	@python main.py

test: # run tests
	@bash run-tests.sh

install-package-tools-pipenv: # Install twine using pipenv
	@pipenv install twine

install-package-tools: # Install twine
	@pip install twine

package-check: # check package if it pass pypi tests
	@twine check dist/*

package: # Package to tar.gz file for uploading to pypi
	@python setup.py sdist
