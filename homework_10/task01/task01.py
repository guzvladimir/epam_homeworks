"""
Homework
Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с данного сайта: <br>
https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:
* Текущая стоимость в рублях (конвертацию производить по текущему курсу, взятому с сайта [центробанка РФ]
(http://www.cbr.ru/development/sxml/))
* Код компании (справа от названия компании на странице компании)
* P/E компании (информация находится справа от графика на странице компании)
* Годовой рост/падение компании в процентах (основная таблица)
* Высчитать какую прибыль принесли бы акции компании (в процентах), если бы они были куплены на уровне 52 Week Low и
проданы на уровне 52 Week High (справа от графика на странице компании)

Сохранить итоговую информацию в 4 JSON файла:
1. Топ 10 компаний с самими дорогими акциями в рублях.
2. Топ 10 компаний с самым низким показателем P/E.
3. Топ 10 компаний, которые показали самый высокий рост за последний год
4. Топ 10 комппаний, которые принесли бы наибольшую прибыль, если бы были куплены на самом минимуме и проданы на самом
 максимуме за последний год.
<br>Пример формата:
```
[
{
    "code": "MMM",
    "name": "3M CO.",
    "price" | "P/E" | "growth" | "potential profit" : value,
},
...
]
```
For scrapping you cans use `beautifulsoup4` <br>
For requesting `aiohttp`
"""
import asyncio
import json
import re
from datetime import datetime
from typing import Dict, List, Optional, Tuple

import aiohttp
from bs4 import BeautifulSoup


async def get_current_dollar_value(session: aiohttp.ClientSession) -> float:
    date_req = datetime.today().strftime("%d/%m/%Y")
    cbr_url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_req}"
    page = BeautifulSoup(await get_html_content(session, cbr_url), "lxml")
    dollar_value = page.find("valute", id="R01235").find("value").text.replace(",", ".")
    return float(dollar_value)


def get_value(parameter: str, soup: BeautifulSoup) -> Optional[float]:
    search_value = re.search(r"([0-9]*\.[0-9]*)\r\n.*" + parameter, str(soup))
    return float(search_value.group(1).replace(",", "")) if search_value else None


def get_potential_profit(soup) -> Optional[float]:
    low52week_value = get_value("52 Week Low", soup.find("div", {"class": "snapshot"}))
    high52week_value = get_value(
        "52 Week High", soup.find("div", {"class": "snapshot"})
    )
    return (
        round((high52week_value / low52week_value - 1) * 100, 2)
        if low52week_value and high52week_value
        else None
    )


async def get_html_content(session: aiohttp.ClientSession, url_link: str) -> str:
    async with session.get(url_link) as response:
        return await response.text()


async def get_company_name_href_growth(
    url: str, session: aiohttp.ClientSession
) -> List[Dict]:
    company_name_href_growth = []
    data_companies = (
        BeautifulSoup(await get_html_content(session, url), "lxml")
        .find_all("table")[1]
        .find_all("tr")[1:]
    )
    for company_values in data_companies:
        name = company_values.find_all("a")[0].text
        href = company_values.find_all("a")[0].get("href")
        growth = float(
            company_values.find_all("td")[9]
            .find_all("span")[1]
            .text.replace("%", "")
            .replace("%", "")
        )
        company_name_href_growth.append({"name": name, "href": href, "growth": growth})
    return company_name_href_growth


async def get_company_info(
    session: aiohttp.ClientSession,
    company_name_href_growth: List[Dict],
    dollar_value: float,
) -> Dict:
    company_url = (
        "https://markets.businessinsider.com" + company_name_href_growth["href"]
    )
    soup = BeautifulSoup(await get_html_content(session, company_url), "lxml")
    price_in_dollars = soup.find(class_="price-section__current-value").text.replace(
        ",", ""
    )
    company_info = {
        "name": company_name_href_growth["name"],
        "code": soup.find(class_="price-section__category").find("span").text[2:],
        "price": round(float(price_in_dollars) * dollar_value, 2),
        "p_e": get_value(
            "P/E Ratio", soup.find_all("div", class_="snapshot__data-item")
        ),
        "growth": company_name_href_growth["growth"],
        "potential profit": get_potential_profit(soup),
    }
    return company_info


def save_json(sorted_data: List[Dict], description: str, key: str) -> None:
    data_to_json = [
        {"code": company["code"], "name": company["name"], f"{key}": company[key]}
        for company in sorted_data
    ]
    json_name = "top_10_" + description + "_" + key + ".json"
    with open(json_name, "w") as file:
        json.dump(data_to_json, file, indent=4)


def top_10_most_expensive(data: List) -> None:
    sorted_data = sorted(data, key=lambda x: x["price"], reverse=True)[:10]
    save_json(sorted_data, "largest", key="price")


def top_10_lowest_p_e(data: List) -> None:
    sorted_data = sorted(
        filter(lambda d: d["p_e"], data),
        key=lambda x: x["p_e"],
        reverse=False,
    )[:10]
    save_json(sorted_data, "lowest", key="p_e")


def top_10_largest_growth(data: List) -> None:
    sorted_data = sorted(data, key=lambda x: x["growth"], reverse=True)[:10]
    save_json(sorted_data, "largest", key="growth")


def top_10_largest_potential_profit(data: List) -> None:
    sorted_data = sorted(
        filter(lambda d: d["potential profit"], data),
        key=lambda x: x["potential profit"],
        reverse=True,
    )[:10]
    save_json(sorted_data, "largest", key="potential profit")


async def main() -> Tuple:
    pages = [
        "https://markets.businessinsider.com/index/components/s&p_500?p=" + str(value)
        for value in range(1, 11)
    ]
    async with aiohttp.ClientSession() as session:
        tasks_1 = [
            asyncio.create_task(get_company_name_href_growth(url, session))
            for url in pages
        ]
        dollar_value = (
            await asyncio.gather(*tasks_1, get_current_dollar_value(session))
        )[10]
        data_pages = (
            await asyncio.gather(*tasks_1, get_current_dollar_value(session))
        )[:10]
        tasks_2 = [
            asyncio.create_task(get_company_info(session, company, dollar_value))
            for data_page in data_pages
            for company in data_page
        ]
        return await asyncio.gather(*tasks_2)


if __name__ == "__main__":
    companies_data = asyncio.get_event_loop().run_until_complete(main())
    top_10_most_expensive(companies_data)
    top_10_lowest_p_e(companies_data)
    top_10_largest_growth(companies_data)
    top_10_largest_potential_profit(companies_data)
