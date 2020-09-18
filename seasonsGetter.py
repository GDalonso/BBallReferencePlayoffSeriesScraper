import requests
from bs4 import BeautifulSoup, Tag as bs4Tag

"""
Get all the urls for the playoff series trough seasons
"""
keys_playoffs = [
    "East Conf 1st Round",
    "West Conf 1st Round",
    "East Conf Semis",
    "West Conf Semis",
    "East Conf Finals",
    "West Conf Finals",
    "Finals",
]


def scrap_seasons(first_season: int, last_season: int, keys_playoffs=keys_playoffs):
    urls = []
    for season in range(first_season, last_season + 1):
        url = f"https://www.basketball-reference.com/playoffs/NBA_{season}.html"

        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        urls = urls + get_container_with_series(soup)
    return urls


def get_container_with_series(soup):
    container = soup.find(id="bottom_nav_container")
    for c in container.children:
        if isinstance(c, bs4Tag):
            if c.string in keys_playoffs:  # find the first playoffs round
                return fetch_all_series_urls(c.fetchNextSiblings())


def fetch_all_series_urls(playoff_round_confs: bs4Tag):
    urls = []
    for playoff_round_conf in playoff_round_confs:
        if playoff_round_conf.string in keys_playoffs:  # remove os headers
            continue
        elif (
            playoff_round_conf.string
            and "Reg. Season Summary" in playoff_round_conf.string
        ):  # identifica que a lista acabou
            return urls
        for series_link in playoff_round_conf.contents:
            if isinstance(series_link, bs4Tag):
                urls.append(series_link.contents[0].contents[0].attrs.get("href", None))
