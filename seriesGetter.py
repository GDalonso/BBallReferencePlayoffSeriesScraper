import requests
from bs4 import BeautifulSoup, Tag as bs4Tag
from PlayffSeries import PlayoffGame
from datetime import datetime
from patterns import YEAR_PATTERN, STRPTIME_GAME_PATTERN
from re import findall as re_findall

"""
gets all the urls of the series in the season and scrap series by series data
"""


def parse_scores_from_series_page(urls: [str]):
    prefix_url = "https://www.basketball-reference.com/"
    for url in urls:
        soup = BeautifulSoup(requests.get(prefix_url + url).content, "html.parser")
        for game in soup.find_all("div", {"class": "game_summary expanded nohover"}):
            # processing scores
            winner, score_winner = list(
                game.tbody.find("tr", {"class": "winner"}).stripped_strings
            )[:2]
            loser, score_loser = list(
                game.tbody.find("tr", {"class": "loser"}).stripped_strings
            )[:2]

            # Processing game number and date
            game_number, date = game.tbody.find("tr", {"class": "date"}).string.split(
                ","
            )
            year = re_findall(YEAR_PATTERN, url)[0]
            date = datetime.strptime(date.strip() + year, STRPTIME_GAME_PATTERN)
            game_number = int(game_number.replace("Game ", ""))

            pgame = PlayoffGame(
                winner=winner,
                loser=loser,
                score_winner=score_winner,
                score_loser=score_loser,
                date=date,
                game_number=game_number,
            )
            assert True


# def parse_a_game(game_contents:bs4Tag):
#     " get a single playoff game parsed"
