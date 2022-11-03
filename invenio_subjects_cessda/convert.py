# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.


# from typing import Any, Callable, Dict, Iterator, NoReturn


from click import secho

from invenio_subjects_cessda.schemas import cessda_schema
from invenio_subjects_cessda.writer import write2yaml


def convert_voc(data, dpath):
    """Convert voc to yaml.

    Args:
        data (arr): voc arr
    """
    for v in data:
        for s in v["data"]:
            write2yaml((v["name"], s), dpath, cessda_schema, mode="a")
    secho("Converted successfully to ", fg="green", nl=False)
    secho(f" {dpath}", fg="yellow", bold=True)
