# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.
import asyncio
import json
import os
from urllib.parse import urlparse, urlunparse

import aiohttp
from click import secho

from invenio_subjects_cessda.config import urls

result = []

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
async def fetch(session, url_obj):
    """fetch API calls"""
    async with session.get(url_obj["endpoint"]) as res:
        data = await res.json()
        resp = dict(name=url_obj["name"], data=data)
        result.append(resp)


async def get_data():
    """gather workers"""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)


def main():
    """main entry point"""
    asyncio.run(get_data())
    path = os.getcwd()
    file_path = "invenio_subjects_cessda/downloads"
    file_name = "result.json"
    data_file_path = os.path.join(path, file_path, file_name)

    with open(data_file_path, "w+", encoding="utf-8") as f:
        f.write(json.dumps(result, indent=2))
    secho("Data downloaded successfully!", fg="green")


if __name__ == "__main__":
    main()
