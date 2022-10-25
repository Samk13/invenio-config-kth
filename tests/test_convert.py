from invenio_subjects_cessda.convert import convert_voc

from tests.fixtures import create_yaml_path
from tests.data import test_data



def test_convert_vov():
    convert_voc(test_data, create_yaml_path)
    except
