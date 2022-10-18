# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

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
