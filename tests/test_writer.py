# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

import yaml
from yaml.loader import SafeLoader

from invenio_subjects_cessda.schemas import cessda_schema
from invenio_subjects_cessda.writer import write2yaml, write_voc
from tests.data import test_data
from tests.fixtures import create_json_path, create_yaml_path


def test_write2yaml(create_yaml_path):
    """Test write2yaml"""
    voc_path = create_yaml_path
    write2yaml(("Mailing address", test_data[0]), voc_path, cessda_schema)
    with open(voc_path, "r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=SafeLoader)
        assert data[0]["subject"] == f"{test_data[0]['title']}"
        assert data[0]["scheme"] == "CESSDA"


def test_write_voc(create_json_path):
    """Test write json"""
    voc_path = create_json_path
    write_voc(voc_path, test_data, "w+")
    with open(voc_path, "r", encoding="utf-8") as f:
        data = f.read()
        assert len(data) > 0
