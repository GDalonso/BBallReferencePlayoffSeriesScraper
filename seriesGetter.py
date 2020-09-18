import requests
from bs4 import BeautifulSoup, Tag as bs4Tag
from PlayffSeries import PlayoffGame, PlayoffSeries
from datetime import datetime
from patterns import YEAR_PATTERN, STRPTIME_GAME_PATTERN, SERIES_NAME_PATTERN
from re import findall as re_findall
from typing import List

"""
gets all the urls of the series in the season and scrap series by series data
"""
series_length_by_winner_wins = {"1": 1, "2": 3, "3": 5, "4": 7}


def parse_scores_from_series_page(urls: List[str]):
    prefix_url = "https://www.basketball-reference.com/"
    for url in urls:
        soup = BeautifulSoup(requests.get(prefix_url + url).content, "html.parser")
        series_games = parse_all_games_from_series(soup, url)

        pseries = parse_a_series(series_games, url)
        assert True


def parse_a_series(series_games: List[PlayoffGame], url: str):

    teams_and_wins = {
        series_games[:1].pop().winner: 1,
        series_games[:1].pop().loser: 0,
    }
    for game in series_games[1:]:
        # sum all the other wins
        teams_and_wins[game.winner] = teams_and_wins.get(game.winner) + 1
    series_winner = max(teams_and_wins, key=teams_and_wins.get)
    series_length = series_length_by_winner_wins.get(
        str(teams_and_wins.get(series_winner))
    )
    loser_definer = lambda dic, winner: (dic.keys() - [series_winner]).pop()
    series_loser = loser_definer(teams_and_wins, series_winner)
    series_name = re_findall(SERIES_NAME_PATTERN, url).pop()

    return PlayoffSeries(
        games=series_games,
        winner=series_winner,
        loser=series_loser,
        series_name=series_name,
    )


def parse_all_games_from_series(soup: BeautifulSoup, url: str) -> List[PlayoffGame]:
    "Get the data from all games of the series"
    series_games = []
    for game in soup.find_all("div", {"class": "game_summary expanded nohover"}):
        # processing scores
        winner, score_winner = list(
            game.tbody.find("tr", {"class": "winner"}).stripped_strings
        )[:2]
        loser, score_loser = list(
            game.tbody.find("tr", {"class": "loser"}).stripped_strings
        )[:2]

        # Processing game number and date
        game_number, date = game.tbody.find("tr", {"class": "date"}).string.split(",")
        year = re_findall(YEAR_PATTERN, url).pop()
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
        series_games.append(pgame)
    return series_games
