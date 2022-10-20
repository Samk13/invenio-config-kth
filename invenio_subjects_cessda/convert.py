# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

import json
from os import getcwd

# from typing import Any, Callable, Dict, Iterator, NoReturn
from urllib.parse import urlparse

from click import secho
from yaml import dump


# cleanup data
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


def cessda_schema(json_row):
    """Return InvenioRDM funders schema."""
    return [
        {
            "id": fix_url(json_row[1]),
            "scheme": "CESSDA",
            "subject": f"{json_row[0]}/{json_row[1]['notation']}",
        }
    ]


def Json_read(data):
    """Read json file."""
    with open(data, encoding="utf-8") as f:
        json_data = json.load(f)
        return json_data


def write2yaml(data, destination, schema, mode="w+"):
    """Write to YAML in append mode.

    Args:
        data (str): json row
        destination (str): file path destination
        schema (Callable): schema function
    """
    with open(destination, mode, encoding="utf-8") as yaml_f:
        data = schema(data)
        if not data:
            return
        dump(data, yaml_f, allow_unicode=True, sort_keys=False)


fpath = f"{getcwd()}/invenio_subjects_cessda/downloads/result.json"
dpath = f"{getcwd()}/invenio_subjects_cessda/vocabularies/cessda_voc.yaml"

x = Json_read(fpath)


def convert_voc(data):
    """Convert voc to yaml.

    Args:
        data (arr): voc arr
    """
    for v in data:
        for s in v["data"]:
            write2yaml((v["name"], s), dpath, cessda_schema, mode="a")
    secho("Converted successfully to ", fg="green", nl=False)
    secho(f"{dpath}", fg="yellow", bold=True)


# test = [
#     {
#         "id": 3202,
#         "uri": "http://rdf-vocabulary.ddialliance.org/cv/LifecycleEventType/1.0/[CODE]",
#         "notation": "InstrumentDesign",
#         "title": "Instrument design",
#         "definition": "Building the data collection instrument, for example, the questionnaire or interview questions, focus group topics, observation forms for an observational design, standardized record review, independent and dependent variables for an experimental design, etc.",
#         "position": 3,
#         "deprecated": False,
#     },
#     {
#         "id": 3204,
#         "uri": "http://rdf-vocabulary.ddialliance.org/cv/LifecycleEventType/1.0/[CODE]",
#         "notation": "QuestionnaireAdaptation",
#         "title": "Questionnaire adaptation",
#         "definition": "Changing the wording of questions to reflect cultural or institutional differences if same-language questionnaires are administered in different regions or countries.",
#         "position": 5,
#         "deprecated": False,
#     },
#     {
#         "id": 10537,
#         "uri": "https://vocabularies.cessda.eu/vocabulary/CountryNamesAndCodes_[CODE]?v=1.0",
#         "notation": "CL",
#         "title": "Chile",
#         "definition": "",
#         "position": 43,
#         "deprecated": False
#       },
#       {
#         "id": 10538,
#         "uri": "https://vocabularies.cessda.eu/vocabulary/CountryNamesAndCodes_[CODE]?v=1.0",
#         "notation": "CN",
#         "title": "China",
#         "definition": "",
#         "position": 44,
#         "deprecated": False
#       },
# ]

# for t in test:
#     print(fix_url(t))
