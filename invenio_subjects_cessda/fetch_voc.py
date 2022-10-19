# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.
import asyncio
from json import dumps
from os import getcwd, path
from urllib.parse import urlparse, urlunparse

import aiohttp
from click import secho

from invenio_subjects_cessda.config import urls


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


# Data fetching
async def fetch(session, url_obj, result):
    """fetch API calls"""
    async with session.get(url_obj["endpoint"]) as res:
        data = await res.json()
        resp = dict(name=url_obj["name"], data=data)
        result.append(resp)
        return result


async def get_data(result):
    """gather workers"""

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url, result) for url in urls]
        await asyncio.gather(*tasks)

def fetch_voc():
    """main entry point"""
    result = []
    asyncio.run(get_data(result))
    f_path = getcwd()
    file_path = "invenio_subjects_cessda/downloads"
    file_name = "result.json"
    data_file_path = path.join(f_path, file_path, file_name)

    with open(data_file_path, "w+", encoding="utf-8") as f:
        f.write(dumps(result, indent=2))
    secho(f"Data downloaded and saved successfully in {data_file_path}", fg="green")
