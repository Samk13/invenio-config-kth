# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

import json
from os import getcwd
from typing import Any, Callable, Dict, Iterator, NoReturn
from urllib.parse import urlparse, urlunparse

from click import secho
from yaml import dump


def funders_schema(json_row):
    """Return InvenioRDM funders schema."""
    return [{
            "id": json_row[1]["uri"],
            "scheme": "CESSDA",
            "subject": f"{json_row[0]}/{json_row[1]['notation']}"
        }]


def Json_read(data):
    """Read json file"""

    with open(data, encoding="utf-8") as f:
        json_data = json.load(f)
        return json_data

def write_line2yaml(data, destination, schema, mode="w+"):
    """write to YAML in append mode
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
    """Convert voc to yaml

    Args:
        data (arr): voc arr
    """
    for v in data:
        for s in v["data"]:
            write_line2yaml((v["name"], s), dpath, funders_schema, mode="a")
    secho("Converted successfully to ", fg="green", nl=False)
    secho(f"{dpath}", fg="yellow", bold=True)

# def convert(
#     f_input: str, f_output: str, schema: Callable, write_format: Callable
# ):
#     """Write results to output file as yaml"""
#     # print(f"Start Converting {f_input} ...")
#     secho(f"Start Converting {f_input} ...", fg="yellow")
#     json_data = Json_read(f_input)
#     for i in json_data:
#         for j in i:
#             write_format(j, f_output, schema)
#     secho("Converted successfully to ", fg="green", nl=False)
#     secho(f"{f_output}", fg="yellow", bold=True)


# class Writer_strategy(ABC):
#     """Abstract reader class
#     Args:
#     data (str): json row
#     destination (str): file path destination
#     schema (Callable): schema function
#     """

#     def write_data(self, data: str, destination: str, schema: Callable) -> NoReturn:
#         """Write to yaml"""




# cleanup data
def fix_url(url_in):
    """Fix broken url for certain vocabularies."""
    url_in_ = urlparse(url_in)
    if url_in_.netloc == "vocabularies.cessda.eu":
        # TODO replace code with voc from the API res
        new_path = str(url_in_.path.split("/")[2].replace("[CODE]", "sam"))
        new_url = url_in_._replace(netloc="rdf-vocabulary.ddialliance.org")._replace(
            path=new_path
        )
    return urlunparse(new_url)
