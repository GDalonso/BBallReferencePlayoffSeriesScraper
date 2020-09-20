import requests
from bs4 import BeautifulSoup, Tag as bs4Tag

from constants import keys_playoffs_depr, keys_playoffs

"""
Get all the urls for the playoff series trough seasons
"""


def scrap_seasons(first_season: int, last_season: int):
    urls = []
    for season in range(first_season, last_season + 1):
        url = f"https://www.basketball-reference.com/playoffs/NBA_{season}.html"

        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        urls = urls + get_container_with_series(soup)

    return urls


def get_container_with_series(soup):
    series = soup.find_all("table", {"id": "all_playoffs"})[0].find_all(
        {"span": "tooltip opener open"}
    )
    link_tags = filter(filter_series_link, series[0].next_elements)
    return [link.get("href") for link in link_tags]


def filter_series_link(r):
    # not r.a is for filtering the TDs and leaving only the links
    if isinstance(r, bs4Tag) and r.string == "Series Stats" and not r.a:
        return True


def get_container_with_series_deprecated(soup):
    container = soup.find(id="bottom_nav_container")
    for c in container.children:
        if isinstance(c, bs4Tag):
            if c.string in keys_playoffs_depr:  # find the first playoffs round
                return fetch_all_series_urls_deprecated(c.fetchNextSiblings())


def fetch_all_series_urls_deprecated(playoff_round_confs: bs4Tag):
    urls = []
    for playoff_round_conf in playoff_round_confs:
        if playoff_round_conf.string in keys_playoffs_depr:  # remove os headers
            continue
        elif (
            playoff_round_conf.string
            and "Reg. Season Summary" in playoff_round_conf.string
        ):  # identifica que a lista acabou
            return urls
        for series_link in playoff_round_conf.contents:
            if isinstance(series_link, bs4Tag):
                urls.append(series_link.contents[0].contents[0].attrs.get("href", None))
