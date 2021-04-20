import asyncio

import aiohttp
import asynctest
import pytest
import pytest_asyncio
import task01
from aioresponses import aioresponses
from bs4 import BeautifulSoup
from task01.task01 import *


@pytest.mark.asyncio
async def test_get_company_info(monkeypatch):
    def fake_page(url, smth):
        with open("Apple.html", "r") as file:
            return file.read()

    fake_get_page = asynctest.CoroutineMock(get_html_content, side_effect=fake_page)
    monkeypatch.setattr(task01.task01, "get_html_content", fake_get_page)
    res = {
        "name": "AAPL",
        "growth": 85.68,
        "code": "AAPL",
        "p_e": 35.60,
        "price": 10257.72,
        "potential profit": 1.19,
    }
    session = aiohttp.ClientSession()
    actual_res = await get_company_info(
        session, {"name": "AAPL", "href": "/stocks/aapl-stock", "growth": 85.68}, 76.0
    )
    assert res == actual_res


@pytest.mark.asyncio
async def test_get_company_name_href_growth(monkeypatch):
    def fake_page(url, smth):
        with open("main_page.html") as file:
            return file.read()

    fake_get_page = asynctest.CoroutineMock(get_html_content, side_effect=fake_page)
    monkeypatch.setattr(task01.task01, "get_html_content", fake_get_page)

    actual_res = await get_company_name_href_growth("path", 1)
    assert actual_res[0]["name"] == "3M"
    assert actual_res[1]["href"] == "/stocks/aos-stock"
    assert actual_res[2]["growth"] == "37.87"
