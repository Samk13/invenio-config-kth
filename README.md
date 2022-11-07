# invenio-config-kth
## Installation

From your instance active venv:
```console
pip install invenio-config-kth
```


## Usage
## Maintainers

### Setup dev env
after cloning the repo:
```bash
make install
make test
```

### Run tests
```bash
make test
```
> When doing tests you will get a warning from [black formatter](https://github.com/shopkeep/pytest-black/issues/55), should bump pytest-black version when it's done
## Upload to pypi

```bash
make install-package-tools # this will install twine (install-package-tools-pipenv if you use pipenv)
make package # this will zip the package into dist dir
make package-check # verify if the package pass twine checks
twine upload -u <USERNAME> -p <PASSWORD> --repository-url https://test.pypi.org/legacy/ dist/* --verbose
```
