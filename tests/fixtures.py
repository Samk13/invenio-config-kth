# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

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
