# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from asyncio import gather, run

from aiohttp import ClientSession

from invenio_subjects_cessda.config import urls


# Data fetching
async def fetch(session, url_obj, result):
    """Fetch API calls."""
    async with session.get(url_obj["endpoint"]) as res:
        data = await res.json()
        resp = dict(name=url_obj["name"], data=data)
        result.append(resp)
        return result


async def gather_data(result):
    """Gather workers."""
    async with ClientSession() as session:
        tasks = [fetch(session, url, result) for url in urls]
        await gather(*tasks)


def fetch_voc():
    """Fetch CESSDA voc and return a list."""
    result = []
    run(gather_data(result))
    return result
