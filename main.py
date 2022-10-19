# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.
from os import getcwd
from urllib.parse import urlparse, urlunparse

from invenio_subjects_cessda.convert import convert_voc
from invenio_subjects_cessda.fetch_voc import fetch_voc, write_voc


# cleanup data
def fix_url(url_in):
    """fix broken url for certain vocabularies"""
    url_in_ = urlparse(url_in)
    if url_in_.netloc == "vocabularies.cessda.eu":
        # TODO replace code with voc from the API res
        new_path = str(url_in_.path.split("/")[2].replace("[CODE]", "sam"))
        new_url = url_in_._replace(netloc="rdf-vocabulary.ddialliance.org")._replace(
            path=new_path
        )
    return urlunparse(new_url)


def main():
    """main entry point"""
    result = fetch_voc()
    # fpath = f"{getcwd()}/invenio_subjects_cessda/downloads/result.json"
    # write_voc(fpath, result, "w+")
    convert_voc(result)


if __name__ == "__main__":
    main()
