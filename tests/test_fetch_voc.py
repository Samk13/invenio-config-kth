from unittest import result
import pytest

from invenio_subjects_cessda.fetch_voc import fetch_voc


@pytest.mark.asyncio
async def test_fetch_voc():
    res = []
    result = await fetch_voc(res)
    assert result

