"""Test subjects extension conforms to subjects extension interface."""


import pkg_resources

from invenio_subjects_cessda import __version__


def test_version():
    """Test version import."""
    assert __version__


def test_vocabularies_yaml():
    """Test vocabularies.yaml structure."""
    extensions = [
        ep.load()
        for ep in pkg_resources.iter_entry_points("invenio_rdm_records.fixtures")
    ]

    assert len(extensions) == 1
