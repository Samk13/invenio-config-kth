from invenio_subjects_cessda.schemas import cessda_schema
from tests.data import expected_schema, test_data


def test_cessda_schema():
    """Test Schema output."""
    assert cessda_schema(("Type of Address", test_data[0])) == expected_schema
