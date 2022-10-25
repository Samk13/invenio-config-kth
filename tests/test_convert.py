from invenio_subjects_cessda.convert import convert_voc
from tests.data import test_data
from tests.fixtures import create_yaml_path


def test_convert_vov(create_yaml_path):
    """Test convert_voc."""
    voc_path = create_yaml_path
    test_d = [{"data": test_data, "name": "Test name"}]
    convert_voc(test_d, voc_path)
    with open(voc_path, "r", encoding="utf-8") as f:
        data = f.read()
        assert len(data) > 0