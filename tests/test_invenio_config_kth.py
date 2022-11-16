# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-config-kth is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.
from flask import Flask

from invenio_config_kth import InvenioConfigKTH, __version__


def test_version():
    """Test version import."""
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    ext = InvenioConfigKTH(app)
    assert "InvenioConfigKTH" not in app.extensions
    ext.init_app(app)
    assert "invenio-config-kth" in app.extensions
