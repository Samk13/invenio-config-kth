# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from invenio_subjects_cessda.schemas import cessda_schema
from tests.data import expected_schema, test_data


def test_cessda_schema():
    """Test Schema output."""
    assert cessda_schema(("Type of Address", test_data[0])) == expected_schema
