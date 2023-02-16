.DEFAULT_GOAL=ls

ls: # List available commands
	@grep '^[^#[:space:]].*:' Makefile

freeze: # Show installed dependencies
	@pip freeze

format: # Black format and isort imports
	@black . && isort .

install: # Install py dependencies
	@pip install -e ".[tests]"

install-pipenv: # Install py dependencies using pipenv
	@pipenv install -e ".[tests]"

test: # Run tests
	@bash run-tests.sh

# Packagin
package-create: # Package to tar.gz file for uploading to pypi
	rm -rf dist
	./increment_version.sh invenio_config_kth/__init__.py $(ARG)
	@python setup.py sdist
	@twine check dist/*

package-check: # Check package if it pass pypi tests
	@twine check dist/*

package-upload: # upload to pypi after prompting your user and pass
	twine upload -u $(USER) -p $(PASS) dist/* --verbose
