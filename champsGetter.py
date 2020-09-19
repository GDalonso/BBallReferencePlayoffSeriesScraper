import requests
from bs4 import BeautifulSoup

URL = "https://www.basketball-reference.com/playoffs/"


def retieve_nba_champs_since_merger(url: str = URL):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    champs_table = soup.find_all("div", {"id": "div_champions_index"}).pop()
    years = champs_table.find_all("th", {"data-stat": "year_id"})[1:]
    champs = champs_table.find_all("td", {"data-stat": "champion"})

    champs_dict = {}
    for index in range(0, len(champs)):
        # locking it to 1977 when the merger happened
        if int(years[index].string) < 1977:
            return champs_dict
        champs_dict[years[index].string] = champs[index].string
