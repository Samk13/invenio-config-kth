# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from urllib.parse import urlparse


def fix_url(obj_in):
    """Fix broken urls for certain vocabularies."""
    url_in_ = urlparse(obj_in["uri"])
    netloc = url_in_.netloc
    path = url_in_.path.split("/")
    base = "https://vocabularies.cessda.eu/vocabulary"
    vcode = "".join(obj_in["notation"]).rsplit(".", maxsplit=1)[-1]

    if netloc == "rdf-vocabulary.ddialliance.org":
        return f"{base}/{path[2]}_{vcode}?v={path[3]}&id={obj_in['id']}"
    else:
        nyurl = "".join(f"{obj_in['uri']}".replace("[CODE]", vcode))
        return f"{nyurl}&id={obj_in['id']}"
