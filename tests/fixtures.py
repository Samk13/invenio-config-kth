import os

import pytest


@pytest.fixture()
def create_yaml_path():
    """Set a temp path for testing. and remove it after closing the session."""
    f_path = f"{os.getcwd()}/tests/test.yaml"
    yield f_path
    os.remove(f_path)


@pytest.fixture()
def create_json_path():
    """Set a temp path for testing. and remove it after closing the session."""
    f_path = f"{os.getcwd()}/tests/test.json"
    yield f_path
    os.remove(f_path)
