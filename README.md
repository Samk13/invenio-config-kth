# invenio-config-kth
## Installation

From your instance active venv:
```console
pip install invenio-config-kth
```

As default, you can add role name `community-manager` to user programmatically in invenio:

```bash
# Create a role
invenio roles create community-manager # This needed to be added once if role doesn't exists
# Add community-manager role to an user, by its emails
invenio roles add <user_email> community-manager
```
you can also pre-add your list of emails as controlled vocabularies:

There are possibility to change the default role name in `invenio_congig_kth/config.py`
```python
CONFIG_KTH_COMMUNITY_MANAGER_ROLE = "community-manager"
```
Or turn the read only mode:
```python
CONFIG_KTH_READ_ONLY_MODE = False
```

## Usage
After installation, you are ready to go:
- Create new communities will be restricted to users with role "community-manager"
- Publishing records will be restricted to community admins (Curator, Manager, Owner)
- Only super users can publish records without selecting a community.
- you can switch new creation to off if you turn
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
> When running tests you will get a warning from [black formatter](https://github.com/shopkeep/pytest-black/issues/55), should bump pytest-black version when it's done
## Upload to pypi

```bash
make install-package-tools # this will install twine (install-package-tools-pipenv if you use pipenv)
make package # this will zip the package into dist dir
make package-check # verify if the package pass twine checks
twine upload -u <USERNAME> -p <PASSWORD> --repository-url https://test.pypi.org/legacy/ dist/* --verbose
```
