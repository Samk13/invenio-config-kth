# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from invenio_subjects_cessda.utils import fix_url


def cessda_schema(json_row):
    """Return cessda voc schema."""
    return [
        {
            "id": fix_url(json_row[1]),
            "scheme": "CESSDA",
            "subject": f"{json_row[1]['title']}",
        }
    ]
