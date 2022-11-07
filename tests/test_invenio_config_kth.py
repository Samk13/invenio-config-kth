# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-config-kth is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

"""Module tests."""


def test_version():
    """Test version import."""
    from invenio_config_kth import __version__

    assert __version__
