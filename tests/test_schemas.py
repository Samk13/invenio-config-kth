from invenio_subjects_cessda.schemas import cessda_schema
from tests.data import data2


def test_cessda_schema():
    res_row = [
        {
            "id": "https://vocabularies.cessda.eu/vocabulary/TypeOfAddress_Mailing?v=1.1&id=8812",
            "scheme": "CESSDA",
            "subject": "Type of Address/Mailing",
        }
    ]
    for index, row in enumerate(data2["data"]):
        assert cessda_schema(row) == res_row[index]
