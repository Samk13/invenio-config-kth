# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.
import asyncio
from json import dumps

import aiohttp
from click import secho

from invenio_subjects_cessda.config import urls


# Data fetching
async def fetch(session, url_obj, result):
    """Fetch API calls."""
    async with session.get(url_obj["endpoint"]) as res:
        data = await res.json()
        resp = dict(name=url_obj["name"], data=data)
        result.append(resp)
        return result


async def get_data(result):
    """Gather workers."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url, result) for url in urls]
        await asyncio.gather(*tasks)


def write_voc(data_file_path, result, mode="w+"):
    """Write result to disk.

    Args:
        data_file_path (str): file path
        result (arr): data arr
        mode (str): open mode
    """
    with open(data_file_path, mode, encoding="utf-8") as f:
        f.write(dumps(result, indent=2))
        secho(f"Data downloaded and saved successfully in{data_file_path}", fg="green")


def fetch_voc():
    """Fetch CESSDA voc and save it to disk."""
    result = []
    asyncio.run(get_data(result))
    return result
