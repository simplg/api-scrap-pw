from __future__ import annotations
import requests

# The scrapping can be done with the coinmarketcap api
# The advantage with this approach, we get a json result and we can precise how many results per page
# so it can be done quickly
# The disadvantage, the results are only refreshed every five minutes
# ---------
# Another way, would be to use puppeteer in order to get the html and the tables updated with information
# from the websocket connection. However, since it is not possible to change the number of items shown
# inside the webpage, puppeteer would be too slow (5 seconds per page at least on a low-end server,
# which is around 5 minutes for the 59 pages)

async def scrap_website(page=0, total_cur=None) -> (list | None):
    """Scrap coinmarketcap asynchronously starting at the page specified

    Args:
        page (int, optional): Starting page to scrap. Defaults to 0
        total_cur (int, optional): Total number of items inside the page. Defaults to None

    Returns:
        list | None: List of cryptocurrencies scraped for this page and the subsequent ones.
    """
    # in case there is nothing to scrap anymore, we return an empty list and stop the recurssive function
    if total_cur is not None and page * 1000 > total_cur:
        return []
    
    # the url of the api change each page, we are asking for 1000 items each page
    url = f'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start={page*1000+1}&limit=1000&sortBy=market_cap&sortType=desc&convert=USD&cryptoType=all&tagType=all&audited=false'
    resp = requests.get(url)

    # if the page doesn't answer back
    if resp.status_code != 200:
        return None
    result = resp.json()
    cryptos = []
    if result["status"]["error_code"] == "0" and "data" in result:
        next_list = await scrap_website(page + 1, int(result["data"]["totalCount"]))
        cryptos = result["data"]["cryptoCurrencyList"] + next_list
    return cryptos

async def scrap_last_day() -> dict[str, list]:
    """Scrap coinmarketcap to get the first 10 and last 10 cryptocurrencies percent change in the last 24H

    Returns:
        dict[str, list]: A dictionnary with the last_ups and last_downs.
    """
    rows = sorted(await scrap_website(), key=lambda x: x["quotes"][0]["percentChange24h"])
    return {"last_ups": rows[-10:], "last_downs": rows[:10] }

async def scrap_last_week() -> dict[str, list]:
    """Scrap coinmarketcap to get the first 10 and last 10 cryptocurrencies percent change in the last 7 days

    Returns:
        dict[str, list]: A dictionnary with the last_ups and last_downs.
    """
    rows = sorted(await scrap_website(), key=lambda x: x["quotes"][0]["percentChange7d"])
    return {"last_ups": rows[-10:], "last_downs": rows[:10] }
