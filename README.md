# invenio-subjects-cessda

 CESSDA Vocabulary for [InvenioRDM](https://inveniosoftware.org/products/rdm/)
This package is inspired by [invenio-subjects-mesh](https://github.com/galterlibrary/invenio-subjects-mesh)
Install this extension to get CESSDA Voc. subject terms used to index and retrieve materials in the STI Repository into your instance.

## Installation

From your instance active venv:
```console
pip install invenio-subjects-cessda
```

in your invenio instance run:
```console
invenio rdm-records fixtures
invenio-cli run
```

### Versions

This repository follows [SemVer versioning](https://semver.org/):


## Usage

There are 2 types of users for this package. Maintainers of the package and instance administrators.

### Instance administrators

For instance administrators, after you have installed the extension as per the steps above,
please read [Invenio subjects documentation](https://inveniordm.docs.cern.ch/customize/vocabularies/subjects/)

To implement CESSDA in your instance:
make sure you activate your invenio instance venv, then:
```bash
pip install invenio-subjects-cessda
invenio rdm-records fixtures
invenio-cli run
```
at this point you are ready to go.

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

### Fetch new CESSDA versions

Last updated in 31/10/2022
Inspect version in the [config.py](invenio_subjects_cessda/config.py) and update the version in desired endpoint link.

- delete file [cessda_voc](invenio_subjects_cessda/vocabularies/cessda_voc.yaml)
> Notice that if you don't delete the old file it will append to it

then run:
```bash
make run
```
This will generate the new yaml file that can be used in your instance.


## Upload to pypi

```bash
make install-package-tools # this will install twine (install-package-tools-pipenv if you use pipenv)
make package # this will zip the package into dist dir
make package-check # verify if the package pass twine checks
twine upload -u <USERNAME> -p <PASSWORD> --repository-url https://test.pypi.org/legacy/ dist/* --verbose
```
