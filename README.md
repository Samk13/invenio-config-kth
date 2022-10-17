# invenio-subjects-cessda

 CESSDA Vocabulary for [InvenioRDM](https://inveniosoftware.org/products/rdm/)
This package is inspired by [invenio-subjects-mesh](https://github.com/galterlibrary/invenio-subjects-mesh)
Install this extension to get CESSDA Voc. subject terms used to index and retrieve materials in the STI Repository into your instance.

## Installation

From your instance active venv:
```console
pip install invenio-subjects-cessda
```

This will add it to your Pipfile.

you can double check by running
```console
pip freeze | grep invenio-subjects-cessda
```
in your invenio instance run:
```console
invenio rdm-records fixtures
invenio-cli run
```
the above commands could take long time to finish so be patient.

### Versions

This repository follows [SemVer versioning](https://semver.org/):


## Usage

There are 2 types of users for this package. Maintainers of the package and instance administrators.

### Instance administrators

For instance administrators, after you have installed the extension as per the steps above,
please read [Invenio subjects documentation](https://inveniordm.docs.cern.ch/customize/vocabularies/subjects/)

**Note**

There is always a room for improvements specially the performance, feel free to drop a PR for that.
TODO:
- write more tests
- improve performance, maybe using Pandas or numpy instead, etc ...


## Maintainers
TODO
- how to fetch new versions
- setup dev env
- run tests

```console
pip install -e ".[tests]"
```
```console
./run-tests
```
