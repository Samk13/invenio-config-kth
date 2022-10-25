# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from invenio_subjects_cessda.utils import fix_url
from tests.data import res_data, test_data


def test_fix_url():
    """test fix_url"""
    for i, u in enumerate(test_data):
        assert fix_url(u) == res_data[i]
