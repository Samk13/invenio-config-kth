from invenio_subjects_cessda.utils import fix_url
from tests.data import res_data, test_data


def test_fix_url():
    """test fix_url"""
    for i, u in enumerate(test_data):
        assert fix_url(u) == res_data[i]
