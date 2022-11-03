# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from json import dumps

from click import secho
from yaml import dump

# from os import getcwd


# from invenio_subjects_cessda.fetch_voc import fetch_voc


def write_voc(data_file_path, res, mode="w+"):
    """Write result to disk.

    Args:
        data_file_path (str): file path
        result (arr): data arr
        mode (str): open mode
    """
    with open(data_file_path, mode, encoding="utf-8") as f:
        f.write(dumps(res, indent=2))
        secho(
            f"Data downloaded and saved successfully in: {data_file_path}", fg="green"
        )


# result = fetch_voc()
# fpath = f"{getcwd()}/invenio_subjects_cessda/vocabularies/result.json"
# write_voc(fpath, result, "w+")


def write2yaml(data, destination, schema, mode="w+"):
    """Write data to YAML.

    Args:
        data (str): JSON
        destination (str): file path destination
        schema (Callable): schema function
    """
    with open(destination, mode, encoding="utf-8") as yaml_f:
        data = schema(data)
        if not data:
            return
        dump(data, yaml_f, allow_unicode=True, sort_keys=False)
