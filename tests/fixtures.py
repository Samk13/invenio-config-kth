import os

import pytest


@pytest.fixture(scope="session", autouse=True)
def create_path():
    """set a temp path for testing

    Yields:
        str: file path
    """
    f_path = f"{os.getcwd()}/tests/test.yaml"
    yield f_path
    os.remove(f_path)
