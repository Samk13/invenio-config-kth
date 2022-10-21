# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.
from os import getcwd

from invenio_subjects_cessda.convert import convert_voc
from invenio_subjects_cessda.fetch_voc import fetch_voc


def main():
    """main entry point"""
    dpath = f"{getcwd()}/invenio_subjects_cessda/vocabularies/cessda_voc.yaml"
    result = fetch_voc()
    convert_voc(result, dpath)


if __name__ == "__main__":
    main()
