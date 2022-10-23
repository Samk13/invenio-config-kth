import os

import yaml
from yaml.loader import SafeLoader

from invenio_subjects_cessda.schemas import cessda_schema
from invenio_subjects_cessda.writer import write2yaml, write_voc
from tests.data import test_data
from tests.fixtures import create_json_path, create_yaml_path


def test_write2yaml(create_yaml_path):
    """Test write2yaml"""
    voc_path = f"{os.getcwd()}/tests/test.yaml"
    write2yaml(("Mailing address", test_data[0]), voc_path, cessda_schema)
    with open(voc_path, "r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=SafeLoader)
        assert data[0]["subject"] == f"Mailing address/{test_data[0]['notation']}"
        assert data[0]["scheme"] == "CESSDA"


def test_write_voc(create_json_path):
    """Test write json"""
    voc_path = f"{os.getcwd()}/tests/test.json"
    write_voc(voc_path, test_data, "w+")
    with open(voc_path, "r", encoding="utf-8") as f:
        data = f.read()
        assert len(data) > 0
